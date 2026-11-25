"""静态 JS 深度提取（3.1 新增）。

补齐三处与 artex 的差距：

① 递归下载所有 chunk
   主包（如 /web/assets/index.523c6654.js）里含 387 个 chunk 文件名，
   但它们是**裸字符串**（"award.d30d8917.js"），不是 import/src 形式，
   现有 _JS_REF_RE 匹配不到 → 只能拿到 HTML 里引用的那几个。

② 抽相对路径 + 拼 baseURL
   主包只声明 `baseURL: "/api"`，真实接口在 chunk 里是相对形式：
       "/ims/contest/award/attachment"
   拼上 baseURL 才是完整接口 /api/ims/contest/award/attachment。
   现有 _find_urls_and_paths 只找完整 /api/xxx，所以抽不到。

③ 分号矩阵绕过（见 ruauth.py）

实测依据（racelink.ccnu.edu.cn 2026-11-23）：
  只解析主包 → 1 个 API 路径
  递归 387 个 chunk + 拼 baseURL → 数十个业务接口（含 /api/pool/* 隐藏业务线）
"""

from __future__ import annotations

import logging
import time as _t
import re
from collections import deque
from typing import Any
from urllib.parse import urljoin, urlparse

logger = logging.getLogger(__name__)

# 懒加载 chunk 的真实形态（Vite import() 打包）：
#   ()=>import("./UserAgreement.c0a93a64.js")
#   "award.d30d8917.js"
# 必须同时覆盖 "./name.js" 与裸 name.js 两种写法。
_BARE_JS_NAME = re.compile(
    r"""["'`](?:\./)?([A-Za-z0-9_\-@]{1,80}\.(?:[a-f0-9]{8}\.)?js)["'`]"""
)
# 完整 JS 相对路径："/web/assets/xxx.js"
_JS_PATH = re.compile(
    r"""["'`](/(?:[A-Za-z0-9_\-./]+/)\.?([A-Za-z0-9_\-]{1,80}(?:\.[a-f0-9]{8})?\.js))["'`]"""
)

# baseURL 声明：baseURL: "/api" / baseUrl:'/api' / VITE_API = "/api"
_BASE_URL_DECL = re.compile(
    r"""(?:baseURL|baseUrl|base_url|API_BASE|API_BASE_URL|VUE_APP_API|VITE_API[A-Z_]*)\s*[:=]\s*["'`]([^"'`]{1,80})["'`]""",
    re.I,
)
# 相对接口路径："/ims/contest/award/config"（首段是小写字母开头，2 段以上）
_REL_ENDPOINT = re.compile(
    r"""["'`](/[a-z][A-Za-z0-9_\-]*(?:/[A-Za-z0-9_\-{}$:.]+){1,6})["'`]"""
)
# 常见 API 前缀（用于判别相对路径是否像接口，而不是静态资源目录）
_API_SEGMENT_HINT = re.compile(
    r"^/(?:api|rest|service|services|gateway|graphql|v\d|ims|eac|cli|pool|system|"
    r"credit|contest|user|admin|backend|open|auth|file|upload|export|report|"
    r"application|award|member|org|dept|role|menu|dict|log|monitor|tool)\b",
    re.I,
)
_ASSET_SEG = re.compile(r"^/(?:web|static|assets|libs|css|js|img|images|fonts|media|dist|public)\b", re.I)

# chunk 下载总时长上限（秒）。顺序下载 + 单请求 12s 超时，2 核机器必须设上限，
# 否则 400 个 chunk 最坏能拖 80 分钟。实测接口集中在前 100 个 chunk 内。
CHUNK_BUDGET_SEC = int(__import__("os").environ.get("DEEP_CHUNK_BUDGET_SEC", "180"))
_MAX_CHUNKS = 400          # 单次最多下载多少 chunk（实测一个站 320 个，取不全就漏业务线）
_MAX_TOTAL_BYTES = 40 * 1024 * 1024   # 汇总文本上限，防内存爆


def _looks_like_endpoint(path: str) -> bool:
    """判断一个相对路径是否像业务接口（而非静态资源）。"""
    if _ASSET_SEG.match(path):
        return False
    if re.search(r"\.(?:js|css|png|jpe?g|gif|svg|ico|woff2?|ttf|map|webp|mp4)$", path, re.I):
        return False
    return bool(_API_SEGMENT_HINT.match(path))


def extract_chunk_names(text: str) -> list[str]:
    """从主包文本里抽出所有 chunk 文件名（裸字符串形式）。

    这是与 artex 对齐的关键：主包用 `"award.d30d8917.js"` 这种裸字符串列出了
    全部懒加载 chunk，现有 import/src 正则完全匹配不到。
    """
    names: list[str] = []
    seen: set[str] = set()
    for m in _BARE_JS_NAME.finditer(text):
        n = m.group(1)
        if n not in seen:
            seen.add(n)
            names.append(n)
    for m in _JS_PATH.finditer(text):
        n = m.group(2) or m.group(1)
        n = n.lstrip("/")
        if n and n not in seen:
            seen.add(n)
            names.append(n)
    return names


def detect_base_url(text: str) -> str:
    """从主包里推断 axios 的 baseURL。找不到返回空串。"""
    m = _BASE_URL_DECL.search(text)
    if not m:
        return ""
    v = m.group(1).strip()
    # 排掉明显的非接口值
    if not v.startswith("/") or v in ("/", "/web", "/static"):
        return ""
    return v.rstrip("/")


def extract_relative_endpoints(text: str) -> list[str]:
    """从 chunk 文本里抽相对接口路径（"/ims/contest/award/config" 形式）。"""
    out: list[str] = []
    seen: set[str] = set()
    for m in _REL_ENDPOINT.finditer(text):
        p = m.group(1).rstrip("/")
        if p in seen or not _looks_like_endpoint(p):
            continue
        seen.add(p)
        out.append(p)
    return out


def _chunk_url_candidates(entry_js_url: str, chunk_name: str, js_dir: str) -> list[str]:
    """给一个 chunk 文件名生成候选 URL。

    Vite 的懒加载 chunk 与主包**同目录**（`./UserAgreement.c0a93a64.js` 相对主包），
    所以主包 URL 的目录是第一候选。
    """
    pair = []
    if js_dir:
        pair.append(js_dir.rstrip("/") + "/" + chunk_name)
    pair.append(urljoin(entry_js_url, chunk_name))
    pair.append(urljoin(entry_js_url, "/web/assets/" + chunk_name))
    pair.append(urljoin(entry_js_url, "/assets/" + chunk_name))
    return list(dict.fromkeys(pair))


def harvest_chunks(
    *,
    entry_js_url: str,
    main_js_text: str,
    fetch_text,
    max_chunks: int = _MAX_CHUNKS,
    timeout: float = 10.0,
) -> dict[str, Any]:
    """递归下载主包里的所有 chunk，返回合并文本与统计。

    fetch_text(url, timeout) -> (text, content_type) 由调用方注入，
    以便复用现有的 httpx 客户端、代理、UA、限流策略。
    """
    names = extract_chunk_names(main_js_text)
    if not names:
        return {"text": "", "fetched": 0, "candidates": 0, "errors": [], "names": []}

    t0 = _t.monotonic()
    js_dir = entry_js_url.rsplit("/", 1)[0] if "/" in entry_js_url else ""
    total = 0
    fetched = 0
    errors: list[dict[str, str]] = []
    parts: list[str] = []
    seen_urls: set[str] = set()

    for name in names[:max_chunks]:
        if total >= _MAX_TOTAL_BYTES:
            break
        # 总时长保护：2 核机器上顺序下载 400 个 chunk，
        # 若某些请求各自超时 12s，最坏会拖到 80 分钟，拖垮整个任务。
        # 超过 CHUNK_BUDGET_SEC 秒就停，把已拿到的先返回（接口通常集中在前几十个）。
        if (_t.monotonic() - t0) > CHUNK_BUDGET_SEC:
            errors.append({"chunk": "(remaining)", "error": f"总时长超 {CHUNK_BUDGET_SEC}s，提前结束"})
            break
        for cand in _chunk_url_candidates(entry_js_url, name, js_dir):
            if cand in seen_urls:
                continue
            seen_urls.add(cand)
            try:
                text, ctype = fetch_text(cand, timeout)
            except Exception:
                continue
            if not text or ("html" in (ctype or "").lower() and "<html" in text[:200].lower()):
                continue
            fetched += 1
            total += len(text)
            parts.append(f"\n/* ===== CHUNK: {cand} ===== */\n{text}\n")
            break
        else:
            errors.append({"chunk": name, "error": "all_candidates_failed"})

    logger.info("[chunks] %s → 候选 %d，成功下载 %d", entry_js_url.rsplit("/", 1)[-1],
                len(names), fetched)
    return {
        "text": "\n".join(parts),
        "fetched": fetched,
        "candidates": len(names),
        "errors": errors[:20],
        "names": names,
    }


def build_full_endpoints(relative: list[str], base_url: str) -> list[dict[str, str]]:
    """把相对路径拼成完整接口。base_url 为空时原样返回。"""
    out: list[dict[str, str]] = []
    seen: set[str] = set()
    for p in relative:
        full = f"{base_url}{p}" if base_url else p
        if full in seen:
            continue
        seen.add(full)
        out.append({"path": full, "raw": p, "base": base_url})
    return out


def deep_static_analyze(
    *,
    entry_js_url: str,
    main_js_text: str,
    fetch_text,
    max_chunks: int = _MAX_CHUNKS,
) -> dict[str, Any]:
    """一站式深度静态分析：主包 → chunk → 相对路径 → 完整接口。"""
    base_url = detect_base_url(main_js_text)
    main_paths = extract_relative_endpoints(main_js_text)

    ch = harvest_chunks(entry_js_url=entry_js_url, main_js_text=main_js_text, fetch_text=fetch_text)
    chunk_paths = extract_relative_endpoints(ch["text"]) if ch["text"] else []

    merged: list[str] = []
    seen: set[str] = set()
    for p in main_paths + chunk_paths:
        if p not in seen:
            seen.add(p)
            merged.append(p)

    full = build_full_endpoints(merged, base_url)
    # 带参数的排前面（才是注入候选）
    full.sort(key=lambda x: ("{" not in x["raw"], x["raw"]))
    return {
        "base_url": base_url,
        "chunks_candidates": ch["candidates"],
        "chunks_fetched": ch["fetched"],
        "chunks_errors": ch["errors"],
        "relative_count": len(merged),
        "endpoints": full,
    }


_TEMPLATE_VAR = re.compile(r"\$\{[^}]*\}")


def _normalize_template(path: str) -> str:
    """把 `${n.contestPoolId}` 这类模板变量归一成 `{}`。

    真实前端里同一个 handler 会有很多变量名变体：
        /pool/contest/${n.contestPoolId}/award
        /pool/contest/${o.contestPoolId}/award
        /pool/contest/${n}/award
    归一后都是一条 `/pool/contest/{}/award`，能砍掉大量重复。
    """
    return _TEMPLATE_VAR.sub("{}", path)


def _group_key(path: str, base: str) -> str:
    """取接口的分组前缀。

    实测按 2 段分组会碎成 112 组（大量 1~2 个的小组），worker 读起来散、还占 token。
    改成：**只按第 1 段分组**（/pool、/ims、/credit、/system），
    /api/pool/contest/list 与 /api/pool/rankings 同组，业务线一目了然。
    """
    p = path
    if base and p.startswith(base):
        p = p[len(base):]
    segs = [s for s in p.split("/") if s]
    if not segs:
        return "(root)"
    return "/" + segs[0]


def format_deep_result(r: dict[str, Any], max_items: int = 0, per_group: int = 60) -> str:
    """渲染给 worker 看的接口清单。

    关键：**按业务线分组输出，不丢业务线；组内超长时限流**。
    - 实测某站 522 条接口 → 归一化后 456 条，分 13 组（/ims 一组就 292 条）
    - 组内优先保留带 `{}` 的业务接口，纯静态路径排后面
    - per_group 默认 60：既能覆盖主流接口，又不会把 token 拉到 7000+
      实测 456 条全列 ~7750 token；每组截 60 后约 3000~4000 token
    """
    eps = r.get("endpoints") or []
    if not eps:
        return ""

    base = r.get("base_url") or ""
    groups: dict[str, list[dict]] = {}
    _seen_norm: set[str] = set()
    _raw_total = 0
    for ep in eps:
        # 模板变量归一后去重：/pool/contest/${n}/award 与 ${o}/award 是同一条
        norm = _normalize_template(ep["path"])
        _raw_total += 1
        if norm in _seen_norm:
            continue
        _seen_norm.add(norm)
        item = dict(ep)
        item["_norm"] = norm
        groups.setdefault(_group_key(norm, base), []).append(item)

    # 组内：带占位符的业务接口排前，纯静态路径排后
    for k in groups:
        groups[k].sort(key=lambda x: ("{" not in x["_norm"], x["_norm"]))

    # 组间：按接口数降序（业务线大的优先给）
    ordered = sorted(groups.items(), key=lambda kv: -len(kv[1]))

    with_param = sum(1 for v in groups.values() for e in v if "{" in e["_norm"])
    uniq_total = len(_seen_norm)
    lines = [
        "## 静态深度提取的真实接口（主包 + 全部 chunk，已拼 baseURL）",
        "",
        f"- 主包 baseURL: `{base or '(无)'}`",
        f"- chunk 候选 {r.get('chunks_candidates')}，实际下载 {r.get('chunks_fetched')}",
        f"- **抽出接口 {uniq_total} 个**（原 {_raw_total} 条，模板变量已归一去重；"
        f"其中带 `{{}}` 占位符 {with_param} 个），分 {len(groups)} 条业务线",
        "",
        "**这些路径来自真实前端代码，一定存在于该系统。优先对带 `{}` 的做注入/越权探测：**",
        "",
    ]

    shown = 0
    truncated_groups: list[str] = []
    for key, items in ordered:
        uniq: list[dict] = []
        seen_local: set[str] = set()
        for ep in items:
            if ep["_norm"] in seen_local:
                continue
            seen_local.add(ep["_norm"])
            uniq.append(ep)
        cap = per_group if per_group > 0 else len(uniq)
        lines.append(f"### {key}  （{len(uniq)} 个）")
        for ep in uniq[:cap]:
            mark = " ★" if "{" in ep["_norm"] else ""
            lines.append(f"- `{ep['_norm']}`{mark}")
            shown += 1
        if len(uniq) > cap:
            truncated_groups.append(f"{key}(+{len(uniq) - cap})")
        lines.append("")
        if max_items and shown >= max_items:
            lines.append(f"（已达总量上限 {max_items}，其余业务线未展开）")
            break

    if truncated_groups:
        lines.append(
            f"（以下业务线有省略，如需全量可再调 analyze_javascript 并传 deep_max_chunks："
            f"{', '.join(truncated_groups[:10])}）"
        )
    return "\n".join(lines)
