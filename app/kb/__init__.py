"""知识库按需检索（融合自 clown-src-6k-skill 的 49 份实战手册）。

设计原则：
- 不把 1.6 万行塞进 system prompt（会撑爆 context、每轮都付费）。
- 只给 worker 一份「目录 + 一句话摘要」，遇到具体场景再按 slug 取正文。
- 取正文时支持按小节标题裁剪，避免大文件一次吃掉几千 token。
- 保留 6k 的禁用标记：cors / llm-security 不提供，401-403 等压缩篇标注为 stub。
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

_DATA_DIR = Path(__file__).resolve().parent / "data"
_INDEX: dict[str, Any] | None = None

# 单次返回正文的硬上限（字符）。超了按小节切，并在结果里告知可用章节。
MAX_BODY_CHARS = 12000


def _load_index() -> dict[str, Any]:
    global _INDEX
    if _INDEX is None:
        path = _DATA_DIR / "index.json"
        if not path.exists():
            _INDEX = {"meta": {"count": 0}, "entries": []}
        else:
            _INDEX = json.loads(path.read_text(encoding="utf-8"))
    return _INDEX


def catalog(category: str = "", limit: int = 0) -> dict[str, Any]:
    """返回知识库目录。

    两种形态（重要，关系 token 成本）：
      - 不传 category：只给「分类 + 每类条目数 + 该类代表条目 slug」的概览。
        导入 HackerOne 语料后条目涨到 184 个，全量列出要 ~8800 token，
        每轮 summarize 都调 catalog 会直接吃掉大半上下文预算。
      - 传 category：只展开该分类的完整条目（slug / 标题 / 摘要），用于确定要查哪篇。

    worker 的典型用法：catalog() 看有哪些类 → catalog("注入") 看该类有什么 → kb_lookup 取正文。
    """
    idx = _load_index()
    entries = idx["entries"]

    if category:
        key = category.strip().lower()
        out: list[dict[str, Any]] = []
        for e in entries:
            if key not in e["category"].lower():
                continue
            item = {
                "slug": e["slug"], "title": e["title"],
                "lines": e["lines"], "summary": e["summary"],
            }
            if e.get("banned"):
                item["status"] = "banned"
            elif e.get("stub"):
                item["status"] = "stub"
            out.append(item)
        if limit and limit > 0:
            out = out[:limit]
        return {"ok": True, "category": category, "count": len(out), "items": out}

    # 概览模式：每类只给计数 + 前 3 个 slug 做样例
    buckets: dict[str, dict[str, Any]] = {}
    for e in entries:
        cat = e["category"]
        b = buckets.setdefault(cat, {"count": 0, "sample": []})
        b["count"] += 1
        if len(b["sample"]) < 3:
            b["sample"].append(e["slug"])
    return {
        "ok": True,
        "total": idx["meta"].get("count", 0),
        "note": "这是分类概览。要看某类全部条目传 category；要查具体内容用 kb_search 或 kb_lookup。",
        "categories": buckets,
    }


def _split_sections(text: str) -> list[tuple[str, str]]:
    """按 markdown 二级及以上标题切节，返回 [(标题, 正文)]。首节标题为空串。"""
    lines = text.splitlines()
    sections: list[tuple[str, list[str]]] = [("", [])]
    for ln in lines:
        m = re.match(r"^(#{1,3})\s+(.+)$", ln)
        if m:
            sections.append((m.group(2).strip(), [ln]))
        else:
            sections[-1][1].append(ln)
    return [(t, "\n".join(body)) for t, body in sections]


def _truncate_by_lines(text: str, max_chars: int) -> tuple[str, bool]:
    """按行截断，尽量切在完整行上。表格类文件（无小节可切）用这个。"""
    if len(text) <= max_chars:
        return text, False
    out: list[str] = []
    used = 0
    for ln in text.splitlines(keepends=True):
        if used + len(ln) > max_chars:
            break
        out.append(ln)
        used += len(ln)
    return "".join(out), True


def lookup(slug: str, section: str = "", max_chars: int = MAX_BODY_CHARS) -> dict[str, Any]:
    """按 slug 取正文。slug 不存在/禁用时返回明确错误，不静默返回空。

    section 为空则返回全文（超 max_chars 时只给前若干节 + 章节目录）；
    指定 section 时按标题子串匹配，返回该节（及下一节之前的内容）。
    """
    idx = _load_index()
    entry = next((e for e in idx["entries"] if e["slug"] == slug), None)
    if entry is None:
        # 容错：允许带 .md 后缀或中文标题
        s = slug[:-3] if slug.endswith(".md") else slug
        entry = next((e for e in idx["entries"] if e["slug"] == s or e["title"] == slug), None)
    if entry is None:
        return {
            "ok": False,
            "kind": "not_found",
            "error": f"知识库没有 `{slug}`",
            "guidance": "先调 kb_catalog 看可用的 slug；不要凭猜测反复试 slug。",
        }
    if entry.get("banned"):
        return {
            "ok": False,
            "kind": "banned",
            "error": f"`{slug}` 在原技能包中被标记为禁开",
            "guidance": "CORS 本方案不挖；越狱类教材不提供。换对应漏洞类型的手册。",
        }

    path = _DATA_DIR / entry["file"]
    if not path.exists():
        return {"ok": False, "kind": "missing_file", "error": f"文件缺失: {entry['file']}"}
    text = path.read_text(encoding="utf-8", errors="replace")

    if entry.get("stub"):
        return {
            "ok": True,
            "slug": slug,
            "title": entry["title"],
            "status": "stub",
            "content": text.strip(),
            "note": "这是「不要在本类耗精力」的决策说明，不是缺失内容。按它指到的模块去挖。",
        }

    sections = _split_sections(text)

    if section:
        key = section.strip().lower()
        idx_hits = [i for i, (t, _) in enumerate(sections) if key in t.lower()]
        if not idx_hits:
            titles = [t for t, _ in sections if t][:30]
            return {
                "ok": False,
                "kind": "section_not_found",
                "error": f"`{slug}` 里没有包含「{section}」的小节",
                "available_sections": titles,
                "guidance": "改用 available_sections 里的标题，或 section 留空取全文。",
            }
        # 取匹配到的第一处，但要把它的子节一起带上（否则只拿到一行标题）
        start = idx_hits[0]
        end = len(sections)
        for j in range(start + 1, len(sections)):
            t = sections[j][0]
            if t and not re.match(r"^#{3}", sections[j][1].split("\n")[0] if sections[j][1] else ""):
                end = j
                break
        body = "\n".join(b for _, b in sections[start:end])
        if len(body.strip()) < 40 and start + 1 < len(sections):
            # 命中的是父标题、正文在子节：把后面几节并进来
            body = "\n".join(b for _, b in sections[start:start + 3])
        return {
            "ok": True,
            "slug": slug,
            "title": entry["title"],
            "section": section,
            "matched": len(idx_hits),
            "content": body[:max_chars],
            "truncated": len(body) > max_chars,
        }

    if len(text) <= max_chars:
        return {
            "ok": True, "slug": slug, "title": entry["title"],
            "lines": entry["lines"], "content": text,
            "truncated": False,
        }

    # 超长：给章节目录 + 前若干节；若切出来几乎是空（表格类文件），改为按行截断
    titles = [t for t, _ in sections if t]
    chunks: list[str] = []
    used = 0
    for t, b in sections:
        if used + len(b) > max_chars:
            break
        chunks.append(b)
        used += len(b)
    body = "\n".join(chunks)
    if len(body) < max_chars * 0.5:
        # 表格/无小节文件：直接按行截断，避免返回几乎空的内容
        body, _ = _truncate_by_lines(text, max_chars)
        return {
            "ok": True,
            "slug": slug,
            "title": entry["title"],
            "lines": entry["lines"],
            "content": body,
            "truncated": True,
            "note": (
                f"全文 {len(text)} 字符超上限，这里是前 {max_chars} 字符（按行截断）。"
                "该篇以表格为主，建议用 kb_search 按关键词定位，或调高关注点后直接照表执行。"
            ),
        }
    return {
        "ok": True,
        "slug": slug,
        "title": entry["title"],
        "lines": entry["lines"],
        "content": body,
        "truncated": True,
        "available_sections": titles[:40],
        "note": "全文超长，这里是前几节。用 section 参数取具体小节，或按 available_sections 继续。",
    }


def search(keyword: str, limit: int = 8) -> dict[str, Any]:
    """在目录摘要里搜关键词，返回候选 slug。找不到再去正文里扫一遍。"""
    if not (keyword or "").strip():
        return {"ok": False, "error": "keyword 不能为空"}
    kw = keyword.strip().lower()
    idx = _load_index()
    hits: list[dict[str, Any]] = []
    for e in idx["entries"]:
        hay = (e["slug"] + " " + e["title"] + " " + e["summary"]).lower()
        if kw in hay:
            hits.append({"slug": e["slug"], "title": e["title"],
                         "category": e["category"], "summary": e["summary"],
                         "match": "index"})
    if len(hits) < limit:
        for e in idx["entries"]:
            if any(h["slug"] == e["slug"] for h in hits) or e.get("banned"):
                continue
            p = _DATA_DIR / e["file"]
            if not p.exists():
                continue
            try:
                body = p.read_text(encoding="utf-8", errors="replace").lower()
            except Exception:
                continue
            if kw in body:
                hits.append({"slug": e["slug"], "title": e["title"],
                             "category": e["category"], "summary": e["summary"],
                             "match": "body"})
            if len(hits) >= limit * 2:
                break
    return {"ok": True, "keyword": keyword, "count": len(hits), "results": hits[:limit]}
