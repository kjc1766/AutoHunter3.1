"""流量记录与证据固化（3.1 新增）。

对标 artex 的 traffic + evidence 模块，但按我们的架构实现：

artex 的做法：内嵌 go-mitmproxy，所有流量落成文件树 + SQLite 索引。
我们的做法：不内嵌代理（Python 里跑 MITM 太重，2 核扛不住），
            而是在 HTTP 层做「带指纹的落盘 + SQLite 索引」，达成同样目的：
            ① 每个请求响应可回查（报告里的证据能复现）
            ② 漏洞证据独立固化（不随流量清理丢失）
            ③ 支持按 host/path/状态码分页检索

为什么值得做：
上游/2.1 的证据只在 finding 的 raw_request/raw_response 字段里，
出问题时无法回查「当时还发过什么、周边接口返回什么」。
实测写 report 时经常要翻回溯，没有索引只能重新发包（有些目标已修复/被 WAF 封）。
"""

from __future__ import annotations

import hashlib
import json
import logging
import os
import re
import sqlite3
import threading
import time
from typing import Any
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

# 落盘根目录（与 autohunter 现有 data 目录并列）
TRAFFIC_ROOT = os.environ.get("TRAFFIC_ROOT", "/app/data/traffic")
# 单文件最大保存字节（超出截断，防撑爆磁盘）
MAX_BODY_STORE = int(os.environ.get("TRAFFIC_MAX_BODY", str(2 * 1024 * 1024)))
# 最多保留多少个任务目录
MAX_TASK_DIRS = int(os.environ.get("TRAFFIC_MAX_TASKS", "20"))
# 敏感头：落盘前脱敏
_SENSITIVE_HEADERS = re.compile(
    r"^(authorization|cookie|set-cookie|x-api-key|api-key|x-auth-token|proxy-authorization)$",
    re.I,
)
# 命中这些模式的内容视为「有证据价值」，优先保留完整 body
_EVIDENCE_HINT = re.compile(
    r'"code"\s*:\s*(?:200|0)|"total"\s*:|"rows"\s*:|"data"\s*:|password|passwd|secret|'
    r'token|身份证|手机号|studentNo|memberPwd',
    re.I,
)

_lock = threading.Lock()


def _sha(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8", "replace")).hexdigest()[:16]


def _redact_headers(headers: dict[str, str]) -> dict[str, str]:
    """落盘前脱敏敏感头（Cookie/token 只留长度，不留明文）。"""
    out = {}
    for k, v in (headers or {}).items():
        if _SENSITIVE_HEADERS.match(k or ""):
            out[k] = f"<redacted len={len(str(v))}>"
        else:
            out[k] = str(v)[:500]
    return out


class TrafficRecorder:
    """按任务隔离的请求/响应落盘 + SQLite 索引。

    目录结构：
      /app/data/traffic/<task_id>/
        index.db                    # sqlite 索引
        exchanges/<hash>.json       # 单次交换完整记录
        evidence/<finding_id>/      # 漏洞证据（不被流量清理影响）
    """

    def __init__(self, task_id: str, root: str = TRAFFIC_ROOT):
        self.task_id = re.sub(r"[^A-Za-z0-9_-]", "", task_id or "unknown")[:40]
        self.dir = os.path.join(root, self.task_id)
        self.ex_dir = os.path.join(self.dir, "exchanges")
        self.ev_dir = os.path.join(self.dir, "evidence")
        self.db_path = os.path.join(self.dir, "index.db")
        self._init_db()

    def _init_db(self) -> None:
        os.makedirs(self.ex_dir, exist_ok=True)
        os.makedirs(self.ev_dir, exist_ok=True)
        with _lock, sqlite3.connect(self.db_path, timeout=10) as c:
            c.execute("PRAGMA journal_mode=WAL")
            c.execute("""
                CREATE TABLE IF NOT EXISTS exchanges (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    ts REAL NOT NULL,
                    method TEXT, url TEXT, host TEXT, path TEXT,
                    status INTEGER, size INTEGER,
                    req_hash TEXT, file TEXT,
                    has_evidence INTEGER DEFAULT 0
                )""")
            c.execute("CREATE INDEX IF NOT EXISTS ix_ex_host ON exchanges(host)")
            c.execute("CREATE INDEX IF NOT EXISTS ix_ex_path ON exchanges(path)")
            c.execute("CREATE INDEX IF NOT EXISTS ix_ex_status ON exchanges(status)")
            c.execute("""
                CREATE TABLE IF NOT EXISTS evidence (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    finding_id TEXT, name TEXT, file TEXT, sha TEXT, ts REAL
                )""")
            c.execute("CREATE INDEX IF NOT EXISTS ix_ev_finding ON evidence(finding_id)")
            c.commit()

    # ---------- 记录 ----------
    def record(
        self,
        *,
        method: str,
        url: str,
        status: int,
        req_headers: dict | None = None,
        req_body: str = "",
        resp_headers: dict | None = None,
        resp_body: str = "",
    ) -> dict[str, Any] | None:
        """记录一次交换。返回 {id, file, has_evidence}。"""
        try:
            p = urlparse(url)
            host = (p.hostname or "").lower()
            path = p.path or "/"
            body = resp_body or ""
            store_body = body[:MAX_BODY_STORE]
            truncated = len(body) > MAX_BODY_STORE
            has_ev = bool(_EVIDENCE_HINT.search(store_body[:200000]))

            rec = {
                "ts": time.time(),
                "method": method.upper(),
                "url": url,
                "status": status,
                "req_headers": _redact_headers(req_headers or {}),
                "req_body": (req_body or "")[:MAX_BODY_STORE],
                "resp_headers": _redact_headers(resp_headers or {}),
                "resp_body": store_body,
                "resp_truncated": truncated,
                "resp_len": len(body),
            }
            fname = f"{_sha(url + method + str(status))}_{int(rec['ts'] * 1000) % 1000000}.json"
            fpath = os.path.join(self.ex_dir, fname)
            with open(fpath, "w", encoding="utf-8") as f:
                json.dump(rec, f, ensure_ascii=False)

            with _lock, sqlite3.connect(self.db_path, timeout=10) as c:
                cur = c.execute(
                    "INSERT INTO exchanges(ts,method,url,host,path,status,size,req_hash,file,has_evidence)"
                    " VALUES (?,?,?,?,?,?,?,?,?,?)",
                    (rec["ts"], rec["method"], url, host, path, status, len(body),
                     _sha(url + method), fname, 1 if has_ev else 0),
                )
                c.commit()
                return {"id": cur.lastrowid, "file": fpath, "has_evidence": has_ev}
        except Exception as e:
            logger.debug("[traffic] 记录失败: %s", str(e)[:80])
            return None

    # ---------- 证据固化 ----------
    def save_evidence(self, finding_id: str, name: str, content: str) -> dict[str, str] | None:
        """把漏洞证据单独固化（不随流量清理丢失）。"""
        try:
            d = os.path.join(self.ev_dir, re.sub(r"[^A-Za-z0-9_-]", "", finding_id)[:32] or "unknown")
            os.makedirs(d, exist_ok=True)
            safe = re.sub(r"[^A-Za-z0-9_.-]", "_", name)[:60] or "evidence"
            fpath = os.path.join(d, safe)
            with open(fpath, "w", encoding="utf-8") as f:
                f.write(content)
            h = _sha(content)
            with _lock, sqlite3.connect(self.db_path, timeout=10) as c:
                c.execute("INSERT INTO evidence(finding_id,name,file,sha,ts) VALUES (?,?,?,?,?)",
                          (finding_id, name, fpath, h, time.time()))
                c.commit()
            return {"file": fpath, "sha": h}
        except Exception as e:
            logger.debug("[traffic] 固证失败: %s", str(e)[:80])
            return None

    # ---------- 检索 ----------
    def search(
        self, *, host: str = "", path_like: str = "", status: int | None = None,
        only_evidence: bool = False, limit: int = 50, offset: int = 0,
    ) -> list[dict]:
        sql = "SELECT id,ts,method,url,host,path,status,size,file,has_evidence FROM exchanges WHERE 1=1"
        args: list[Any] = []
        if host:
            sql += " AND host = ?"
            args.append(host.lower())
        if path_like:
            sql += " AND path LIKE ?"
            args.append(f"%{path_like}%")
        if status is not None:
            sql += " AND status = ?"
            args.append(int(status))
        if only_evidence:
            sql += " AND has_evidence = 1"
        sql += " ORDER BY id DESC LIMIT ? OFFSET ?"
        args += [max(1, min(limit, 200)), max(0, offset)]
        with _lock, sqlite3.connect(self.db_path, timeout=10) as c:
            c.row_factory = sqlite3.Row
            return [dict(r) for r in c.execute(sql, args)]

    def stats(self) -> dict[str, Any]:
        with _lock, sqlite3.connect(self.db_path, timeout=10) as c:
            total = c.execute("SELECT COUNT(*) FROM exchanges").fetchone()[0]
            ev = c.execute("SELECT COUNT(*) FROM exchanges WHERE has_evidence=1").fetchone()[0]
            evi = c.execute("SELECT COUNT(*) FROM evidence").fetchone()[0]
        return {"exchanges": total, "with_evidence": ev, "finding_evidence": evi, "dir": self.dir}


# ---------- 全局回收 ----------
def prune_traffic(root: str = TRAFFIC_ROOT, keep: int = MAX_TASK_DIRS, keep_days: int = 3) -> int:
    """清理旧任务流量目录，保留 evidence/。返回清理的任务数。"""
    if not os.path.isdir(root):
        return 0
    now = time.time()
    items = []
    for name in os.listdir(root):
        p = os.path.join(root, name)
        if not os.path.isdir(p):
            continue
        try:
            items.append((os.path.getmtime(p), name))
        except OSError:
            continue
    items.sort(reverse=True)
    removed = 0
    for idx, (mtime, name) in enumerate(items):
        too_many = idx >= keep
        too_old = (now - mtime) > keep_days * 86400
        if not (too_many or too_old):
            continue
        p = os.path.join(root, name)
        ev = os.path.join(p, "evidence")
        # 有证据的目录不整体删，只清 exchanges 与索引
        try:
            if os.path.isdir(ev) and os.listdir(ev):
                ex = os.path.join(p, "exchanges")
                for f in os.listdir(ex) if os.path.isdir(ex) else []:
                    try:
                        os.remove(os.path.join(ex, f))
                    except OSError:
                        pass
                continue
            import shutil
            shutil.rmtree(p, ignore_errors=True)
            removed += 1
        except OSError:
            pass
    return removed


CLEANUP_INTERVAL_HOURS = int(os.environ.get("TRAFFIC_CLEANUP_INTERVAL_HOURS", "12"))


async def run_periodic_traffic_cleanup() -> None:
    """定时清理流量记录（挂到 FastAPI lifespan）。

    不清理会撑爆数据卷：单任务 5000 次请求 × 平均 50KB ≈ 250MB，
    20 个任务就是 5GB。有 evidence 的目录只清 exchanges，证据不丢。
    """
    import asyncio

    interval = max(1, CLEANUP_INTERVAL_HOURS) * 3600
    logger.info("流量记录清理已启动: 间隔 %dh, 保留最新 %d 个任务 / %d 天",
                CLEANUP_INTERVAL_HOURS, MAX_TASK_DIRS, 3)
    while True:
        try:
            await asyncio.sleep(interval)
            n = prune_traffic()
            if n:
                logger.info("流量记录清理完成: 删除 %d 个任务目录", n)
        except asyncio.CancelledError:
            logger.info("流量记录清理已停止")
            break
        except Exception:
            logger.exception("流量记录清理异常")
