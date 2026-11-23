"""把 Finding 渲染成 SRC 平台可直接提交的报告（格式取自 clown-src-6k-skill 的 vuln-report-format）。

分层原则：
- Finding 是内部流转结构（机器消费），本模块只负责「导出给人看」。
- 不改 Finding 内部字段语义；缺字段时降级，不要让渲染抛异常打断流水线。

排版铁律（来自 6k 原文）：
- 标题 / 目标网站URL / 漏洞等级 各占一行，中间不空行
- 「漏洞描述：」「漏洞危害：」冒号后换行再写正文
- 危害每种伤害单独一行
- 大块之间用单独一行全角「＃」，禁止半角 #
- 不出现多余空行
"""
from __future__ import annotations

import json
from typing import Any

SEP = "＃"  # 全角，6k 原文要求


def _v(obj: Any, name: str, default: str = "") -> str:
    """兼容 pydantic model / dict / Enum 三种形态。

    注意：str Enum 的 str() 会给出 "Severity.high"，这里必须取 .value，
    否则报告等级会渲染成英文枚举名。
    """
    if obj is None:
        return default
    if isinstance(obj, dict):
        val = obj.get(name, default)
    else:
        val = getattr(obj, name, default)
    if val is None:
        return ""
    # Enum（含 str 子类 Enum）：优先 .value
    value = getattr(val, "value", None)
    if value is not None and not isinstance(val, (str, int, float)):
        return str(value)
    if isinstance(val, str) and "." in val and val.split(".")[0] in (
        "Severity", "Verdict", "ReviewVerdict", "Confidence"
    ):
        # 兜底：已是 "Severity.high" 字符串时取最后一段并按映射转中文
        tail = val.split(".")[-1]
        return _SEVERITY_CN.get(tail, tail)
    return str(val)


_SEVERITY_CN = {
    "critical": "严重",
    "high": "高危",
    "medium": "中危",
    "low": "低危",
}


def _clean_multiline(text: str) -> list[str]:
    """去掉首尾空白和多余空行，返回非空行列表。"""
    return [ln.rstrip() for ln in (text or "").splitlines() if ln.strip()]


def _as_list(value: Any) -> list[str]:
    """把 steps 归一化成字符串列表。

    生产库里 steps 列是 TEXT 但存的是 JSON 数组字符串（如 '["GET /test ...", "GET /test/view?id=1"]'），
    只判断 isinstance(list) 会把整段步骤当空，报告里显示「缺复现步骤」——这是真实数据踩出来的坑。
    """
    if value is None:
        return []
    if isinstance(value, str):
        s = value.strip()
        if not s:
            return []
        if s[:1] in "[{":
            try:
                parsed = json.loads(s)
                return _as_list(parsed)
            except (ValueError, TypeError):
                return [s]
        return [s]
    if isinstance(value, (list, tuple)):
        out: list[str] = []
        for v in value:
            if isinstance(v, (dict, list)):
                try:
                    out.append(json.dumps(v, ensure_ascii=False))
                except (TypeError, ValueError):
                    out.append(str(v))
            elif v is not None:
                t = str(v).strip()
                if t:
                    out.append(t)
        return out
    return [str(value)]


def render_report(f: Any, fallback_impact: str = "") -> str:
    """渲染单个 Finding 为完整版 SRC 报告 markdown。

    fallback_impact: Finding.impact 为空时退回用的文本（通常是 affected_scope），
    避免危害块开天窗。
    """
    title = _v(f, "title").strip() or "（未命名漏洞）"
    url = _v(f, "target_url").strip()
    severity = _v(f, "severity_claimed").strip() or "中危"
    desc = _v(f, "description").strip()
    scope = _v(f, "affected_scope").strip()
    fix = _v(f, "fix_suggestion").strip()
    poc = _v(f, "poc").strip()
    raw_req = _v(f, "raw_request").strip()
    raw_resp = _v(f, "raw_response").strip()
    owner = _v(f, "owner").strip()
    vuln_type = _v(f, "vuln_type").strip()

    steps: list[str] = _as_list(
        f.get("steps") if isinstance(f, dict) else getattr(f, "steps", None)
    )

    out: list[str] = []

    # ---- 头部三行：不空行、不分隔 ----
    out.append(title)
    if url:
        out.append(f"目标网站URL：{url}")
    out.append(f"漏洞等级：{severity}")
    # CVSS 向量紧跟等级行：人工复审据此复算定级，不再只有一句主观结论。
    # 注意取值路径：_finding_dict 把 review 相关字段放在嵌套的 review 子对象里，
    # 直接 f.get("cvss_vector") 取不到（实测报告里一直空白）。两处都查。
    cvss_vec = _v(f, "cvss_vector").strip()
    if not cvss_vec and isinstance(f, dict):
        rv = f.get("review")
        if isinstance(rv, dict):
            cvss_vec = str(rv.get("cvss_vector") or "").strip()
    if cvss_vec:
        try:
            from app.tools.cvss31 import base_score, parse_vector
            mm = parse_vector(cvss_vec)
            if mm:
                sc = base_score(mm)
                out.append(f"CVSS 3.1：{cvss_vec} → {sc.score:.1f}（{sc.band_zh}）")
            else:
                out.append(f"CVSS 3.1：{cvss_vec}")
        except Exception:
            out.append(f"CVSS 3.1：{cvss_vec}")
    if owner:
        out.append(f"归属单位：{owner}")

    # ---- 漏洞描述 ----
    out.append("")
    out.append("漏洞描述：")
    if desc:
        out.extend(_clean_multiline(desc))
    else:
        out.append("（缺描述：提交时未填写 description）")

    # ---- 漏洞危害 ----
    out.append(SEP)
    out.append("漏洞危害：")
    # 只用 impact 本身判断「有没有写危害」。以前拿 affected_scope 兜底填进危害栏，
    # 结果「没写 impact」的 finding 报告里危害段被一段影响范围文字占位，既不像伤害描述
    # 也看不出缺什么（真实数据踩出来的问题）。现在分开：impact 空就明确提示，scope 单独列。
    impact_lines = _clean_multiline(_v(f, "impact"))
    if impact_lines:
        out.extend(impact_lines)
    else:
        fb = _clean_multiline(fallback_impact)
        if fb:
            out.append("（worker 未填写 impact，以下为影响范围，需人工补成伤害描述）")
            out.extend(fb)
        else:
            out.append("（缺危害描述：请补 impact；只写最终伤害，每种单独一行并举例）")
    if scope and scope not in impact_lines and scope not in (fallback_impact or ""):
        out.append(f"影响范围：{scope}")

    # ---- 涉及接口清单 ----
    out.append(SEP)
    out.append("涉及接口清单：")
    api_lines: list[str] = []
    for i, s in enumerate(steps, 1):
        # 步骤里如果直接给了完整 URL，提一行出来当接口
        for token in s.split():
            if token.startswith(("http://", "https://")):
                api_lines.append(f"{len(api_lines) + 1}. {token}")
                break
    if not url and not api_lines:
        out.append("（缺接口信息）")
    else:
        if url and not api_lines:
            out.append(f"1. {url}")
        else:
            out.extend(api_lines)

    # ---- 复现步骤 ----
    out.append(SEP)
    out.append("复现步骤：")
    if steps:
        import re as _re
        for i, s in enumerate(steps, 1):
            lines = _clean_multiline(s)
            if not lines:
                continue
            # 步骤本身可能已带 "1." / "1、" / "-" 编号，先剥掉，避免渲染成「1. 1. xxx」
            head = lines[0]
            head = _re.sub(r"^\s*(?:\d+[.、)）]|[-*•])\s*", "", head)
            out.append(f"{i}. {head}")
            for extra in lines[1:]:
                extra = _re.sub(r"^\s*(?:\d+[.、)）]|[-*•])\s*", "", extra)
                out.append(f"   {extra}")
    else:
        out.append("（缺复现步骤）")

    # ---- 整包（请求/响应）----
    if raw_req:
        out.append(SEP)
        out.append("请求包：")
        out.append("```http")
        out.extend(_clean_multiline(raw_req))
        out.append("```")
    if raw_resp:
        out.append(SEP)
        out.append("响应包：")
        out.append("```http")
        # 响应包只留前 80 行，避免报告被巨量 body 淹没
        resp_lines = _clean_multiline(raw_resp)
        out.extend(resp_lines[:80])
        if len(resp_lines) > 80:
            out.append(f"...（省略 {len(resp_lines) - 80} 行）")
        out.append("```")

    # ---- PoC ----
    if poc and not raw_req:
        out.append(SEP)
        out.append("PoC：")
        out.append("```")
        out.extend(_clean_multiline(poc))
        out.append("```")

    # ---- 修复建议 ----
    out.append(SEP)
    out.append("修复建议：")
    if fix:
        out.extend(_clean_multiline(fix))
    else:
        out.append("（缺修复建议：请补 fix_suggestion，要贴合本洞给出可落地方案）")

    # ---- 尾部元信息（审核用，不占正文版式）----
    out.append(SEP)
    meta = [f"漏洞类型：{vuln_type}" if vuln_type else "漏洞类型：未标注"]
    out.append("　".join(meta))

    # 压缩连续多空行，保证「不出现多余空行」
    result: list[str] = []
    prev_blank = False
    for ln in out:
        blank = not ln.strip()
        if blank and prev_blank:
            continue
        result.append(ln)
        prev_blank = blank
    return "\n".join(result).strip() + "\n"


def safe_filename(title: str, max_len: int = 80) -> str:
    """文件名就是漏洞标题那一行。去掉路径分隔符和非法字符。"""
    bad = '\\/:*?"<>|\r\n\t'
    name = "".join("_" if c in bad else c for c in (title or "未命名")).strip()
    name = name.strip(" .")
    if len(name) > max_len:
        name = name[:max_len].rstrip(" .")
    return (name or "未命名") + ".md"
