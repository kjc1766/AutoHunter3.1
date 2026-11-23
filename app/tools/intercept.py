"""可配置的操作拦截规则（3.1 新增，对标 artex 的 intercept 模块）。

与现有 guard.py 的区别：
- guard.py 是**硬编码**的安全红线（禁脱库、禁自毁环境），不可配置、不可绕过。
- 本模块是**用户自定义**的拦截规则，按优先级匹配，支持三种动作：

    allow  立即放行，跳过后续更低优先级规则
    deny   直接拒绝，把原因返回给模型
    ask    挂起等人工确认（返回 pending，人工在前端点通过/拒绝）

典型用法（用户视角）：
- 「对 xx.edu.cn 的写操作必须问我」→ ask
- 「禁止访问 /admin/* 除非我批」→ ask
- 「这个内网段一律放行」→ allow
- 「生产库路径的 delete 一律拒」→ deny

为什么要做：现在只有「硬拦截」和「靠提示词劝阻」两档，
中间缺「让 AI 停下来等我点头」这一档。实测有些操作不算破坏，
但需要人判断（比如改测试账号的密码验证重置漏洞）。
"""

from __future__ import annotations

import json
import logging
import os
import re
import threading
import time
import uuid
from typing import Any

logger = logging.getLogger(__name__)

RULES_FILE = os.environ.get("INTERCEPT_RULES", "/app/data/intercept_rules.json")

ACTION_ALLOW = "allow"
ACTION_DENY = "deny"
ACTION_ASK = "ask"

# 待人工确认的记录（内存级，重启丢失可接受——重启本身就等于拒绝）
_pending: dict[str, dict[str, Any]] = {}
_pending_lock = threading.Lock()
PENDING_TTL = int(os.environ.get("INTERCEPT_PENDING_TTL", "600"))  # 10 分钟

_rules_cache: list[dict] | None = None
_rules_mtime: float = 0.0


def _load_rules() -> list[dict]:
    """从文件加载规则，按 mtime 缓存（改完不用重启）。"""
    global _rules_cache, _rules_mtime
    try:
        m = os.path.getmtime(RULES_FILE)
    except OSError:
        return []
    if _rules_cache is not None and m == _rules_mtime:
        return _rules_cache
    try:
        with open(RULES_FILE, encoding="utf-8") as f:
            data = json.load(f)
        rules = data if isinstance(data, list) else data.get("rules", [])
    except Exception as e:
        logger.info("[intercept] 规则加载失败（忽略）: %s", str(e)[:80])
        return []
    # 按 priority 降序
    rules = [r for r in rules if isinstance(r, dict)]
    rules.sort(key=lambda r: -int(r.get("priority") or 0))
    _rules_cache, _rules_mtime = rules, m
    return rules


def _match(rule: dict, tool: str, subject: str) -> bool:
    """判断规则是否命中。

    rule 字段：
      tools:   ["http_request", "run_shell"] 或空=全部
      pattern: 正则，匹配 tool 名 + 主要参数拼成的串
    """
    tools = rule.get("tools") or []
    if tools and tool not in tools:
        return False
    pat = rule.get("pattern") or ""
    if not pat:
        return True
    try:
        return bool(re.search(pat, subject, re.I))
    except re.error:
        return False


def _subject(tool: str, args: dict) -> str:
    """把 tool 的关键参数拼成用于匹配的串。

    顺序固定为 tool | method | url | command | ...，
    让规则可以按「方法 + 域名 + 动作」三段顺序书写正则。
    """
    parts = [tool]
    m = args.get("method")
    if m:
        parts.append(str(m).upper())
    for k in ("url", "command", "code", "path", "target"):
        v = args.get(k)
        if v:
            parts.append(str(v)[:2000])
    if len(parts) == 1:
        try:
            parts.append(json.dumps(args, ensure_ascii=False)[:2000])
        except Exception:
            pass
    return " | ".join(parts)


def check(tool: str, args: dict) -> tuple[str, dict | None]:
    """检查一次工具调用。

    返回 (action, payload)：
      (allow, None)
      (deny, {"reason": ...})
      (ask, {"pending_id": ..., "reason": ...})
    """
    rules = _load_rules()
    if not rules:
        return ACTION_ALLOW, None
    subject = _subject(tool, args)
    for r in rules:
        if not _match(r, tool, subject):
            continue
        act = (r.get("action") or ACTION_ALLOW).lower()
        name = r.get("name") or r.get("id") or ""
        if act == ACTION_ALLOW:
            return ACTION_ALLOW, None
        if act == ACTION_DENY:
            return ACTION_DENY, {"reason": r.get("message") or f"被规则「{name}」拒绝"}
        if act == ACTION_ASK:
            pid = uuid.uuid4().hex[:12]
            rec = {
                "id": pid,
                "tool": tool,
                "subject": subject[:800],
                "reason": r.get("message") or f"规则「{name}」要求人工确认",
                "rule": name,
                "created": time.time(),
                "decision": "",
            }
            with _pending_lock:
                _pending[pid] = rec
                # 清理过期
                now = time.time()
                for k in [k for k, v in _pending.items() if now - v["created"] > PENDING_TTL]:
                    _pending.pop(k, None)
            return ACTION_ASK, {"pending_id": pid, "reason": rec["reason"]}
    return ACTION_ALLOW, None


def decide(pending_id: str, approved: bool) -> bool:
    """人工裁决。返回是否成功。"""
    with _pending_lock:
        rec = _pending.get(pending_id)
        if not rec or rec["decision"]:
            return False
        rec["decision"] = "approved" if approved else "denied"
        rec["decided_at"] = time.time()
        return True


def get_decision(pending_id: str) -> str:
    """查决策状态：approved / denied / pending / expired。"""
    with _pending_lock:
        rec = _pending.get(pending_id)
        if not rec:
            return "expired"
        if rec["decision"]:
            return rec["decision"]
        if time.time() - rec["created"] > PENDING_TTL:
            return "expired"
        return "pending"


def list_pending() -> list[dict]:
    with _pending_lock:
        now = time.time()
        return [
            {k: v for k, v in r.items() if k != "subject"} | {"subject": r["subject"][:200]}
            for r in _pending.values()
            if not r["decision"] and (now - r["created"]) <= PENDING_TTL
        ]


DEFAULT_RULES_EXAMPLE = {
    "_comment": "示例规则。放到 /app/data/intercept_rules.json 生效，改完不用重启。",
    "rules": [
        {
            "id": "ask-write-to-edu",
            "name": "教育站点写操作需确认",
            "priority": 100,
            "tools": ["http_request"],
            "pattern": r"(POST|PUT|DELETE)\s*\|\s*https?://[^|]*\.edu\.cn[^|]*(save|delete|update|remove|reset)",
            "action": "ask",
            "message": "对教育站点的写/删/重置操作，需人工确认后再执行",
        },
        {
            "id": "deny-prod-db",
            "name": "禁止碰生产库路径",
            "priority": 90,
            "tools": ["run_shell"],
            "pattern": r"/opt/(?:prod|live)/.*\.(?:sql|db)",
            "action": "deny",
            "message": "生产库文件禁止直接操作",
        },
        {
            "id": "allow-intranet",
            "name": "内网测试段放行",
            "priority": 50,
            "tools": [],
            "pattern": r"10\.10\.0\.\d+",
            "action": "allow",
        },
    ],
}


def write_example(path: str = RULES_FILE) -> str:
    """写一份示例规则文件（不存在时才写）。"""
    if os.path.exists(path):
        return path
    try:
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w", encoding="utf-8") as f:
            json.dump(DEFAULT_RULES_EXAMPLE, f, ensure_ascii=False, indent=2)
    except Exception:
        pass
    return path
