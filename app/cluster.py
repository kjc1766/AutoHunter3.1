"""同类漏洞聚合（Clustering）。

背景：LLM 每次描述同一个洞会写不同的标题与 vuln_type 自由文本，
`dedup.fingerprint` 按类型名做 key，导致同一洞被判成多条独立 finding。
实测：鑫贝帝一个弱口令洞产生 10 条，报修系统一个 SQLi 产生 6 条。

设计目标：**只做展示聚合，不改判重、不改状态机**。
- 每个 finding 仍然独立存在、独立复核、独立提交；
- 只是在前端列表里把「同一漏洞的多种描述」折叠成一行，点开看变体；
- 任何 finding 的判定结果都保留，聚合不影响 flow。

聚类维度（满足其一即同组）：
1. 同 host + 同语义大类 + 同端点路径
2. 同 host + 同语义大类 + 标题相似度 ≥ 阈值
3. 同产品名 + 同语义大类 + 标题相似度 ≥ 阈值（跨 host，处理域名/CDN 别名）

语义大类是关键：把「默认口令」「弱密码」「admin/admin123」都折叠到 weak_cred，
即使 LLM 写「弱口令+后台越权」也能归到同一族。
"""
from __future__ import annotations

import re
from difflib import SequenceMatcher

from app.dedup import normalize_endpoint_path, normalize_host, normalize_text

TITLE_SIM_THRESHOLD = 0.42

# (大类, 关键词 tuple)。关键词用小写，匹配标题 + vuln_type 拼接后的文本。
_SEMANTIC_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    # 顺序即优先级：先命中先返回。高特异性的类型必须排在前面，
    # 否则「wxConfig 泄露 corpsecret」会被 sign_bypass 的 "secret" 抢先吞掉
    # （实测把企业微信凭据泄露误判成签名绕过，连带报修审批越权也进了这个桶）。
    ("sqli", (
        "sql注入", "sql 注入", "sqlinjection", "sql injection", "sql_injection",
        "报错注入", "盲注", "union 注入", "union注入", "error-based", "orderby 注入",
        "order by 注入", "注入点",
    )),
    ("rce", (
        "rce", "命令执行", "code execution", "反序列化", "deserialization",
        "webshell", "任意代码", "远程代码", "jsp webshell", "getshell",
    )),
    ("weak_cred", (
        "弱口令", "弱密码", "默认口令", "默认密码", "默认账号", "default credential",
        "weak password", "default password", "admin/admin", "admin123", "manager11",
        "硬编码密码", "hardcoded password", "硬编码账号", "口令爆破", "密码爆破",
    )),
    ("upload", (
        "任意文件上传", "文件上传", "upload 接口", "arbitrary file upload", "上传漏洞",
        "任意文件写入", "importseal", "importsignature", "传jsp", "传 shell",
    )),
    ("traversal", (
        "路径穿越", "traversal", "任意文件读取", "任意文件下载", "lfi",
        "目录穿越", "arbitrary file read", "路径遍历",
    )),
    ("ssrf", ("ssrf", "服务端请求伪造", "server-side request")),
    # 签名绕过放在 ssrf 之后、info_leak 之前：HS256/JWT 伪造这类标题常同时提到
    # SSRF 或密钥泄露，靠前会被抢走。关键词只保留签名强相关词。
    ("sign_bypass", (
        "签名绕过", "伪造sign", "伪造 sign", "签名校验", "签名盐", "签名密钥",
        "signbypass", "signature bypass", "验签绕过", "jwt 伪造", "jwt伪造",
        "hs256", "硬编码密钥", "硬编码签名", "伪造令牌", "令牌伪造",
    )),
    ("xss", ("xss", "跨站脚本", "cross-site scripting")),
    ("csrf", ("csrf", "跨站请求伪造")),
    ("idor", (
        "越权", "idor", "bfla", "bola", "功能级授权", "横向越权", "纵向越权",
        "水平越权", "垂直越权", "未授权写", "越权写", "越权读", "missing function",
        "mass assignment", "批量赋值",
    )),
    ("auth_bypass", (
        "绕过鉴权", "认证绕过", "authentication bypass", "鉴权绕", "未授权访问",
        "unauthorized", "未鉴权", "免登录", "零cookie", "无cookie", "未登录",
        "会话签发", "伪造任意用户", "登录态伪造", "免鉴权", "零凭据", "无认证",
        "未认证", "完全未鉴权", "referer 绕过", "白名单绕过",
    )),
    ("info_leak", (
        "信息泄露", "敏感信息", "exposure", "disclosure", "数据泄露", "dump",
        "corpsecret", "凭据泄露", "密码哈希", "证件号", "通讯录", "敏感数据",
    )),
)

_OTHER = "other"


def semantic_class(*texts: str) -> str:
    """把自由描述折叠到语义大类。按规则顺序匹配，先命中先返回。"""
    blob = " ".join((t or "").lower() for t in texts)
    for name, kws in _SEMANTIC_RULES:
        for kw in kws:
            if kw in blob:
                return name
    return _OTHER


def title_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, normalize_text(a)[:70], normalize_text(b)[:70]).ratio()


# 产品名提取的候选：中文字段 或 连续英文/数字
_PROD_RE = re.compile(r"[\u4e00-\u9fa5]{2,12}|[A-Za-z][A-Za-z0-9._-]{3,20}")


def product_keys(title: str) -> set[str]:
    """从标题里抽产品名候选，用于跨 host 归组。

    比 dedup.title_product_key 宽松：那个只取分隔符前的前缀，这里扫全标题，
    因为「鑫贝帝科技官网后台弱口令」这类标题产品名不在开头分隔位置。
    """
    out: set[str] = set()
    for m in _PROD_RE.finditer(title or ""):
        w = m.group(0).strip().lower()
        if len(w) >= 4:
            out.add(w)
    return out


class _DSU:
    """并查集。"""

    def __init__(self, n: int) -> None:
        self.p = list(range(n))
        self.rank = [0] * n

    def find(self, x: int) -> int:
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.rank[ra] < self.rank[rb]:
            ra, rb = rb, ra
        self.p[rb] = ra
        if self.rank[ra] == self.rank[rb]:
            self.rank[ra] += 1


def _cluster_key(item: dict) -> tuple[str, str, str]:
    url = item.get("target_url") or item.get("host") or ""
    return (
        normalize_host(url),
        semantic_class(item.get("title", ""), item.get("vuln_type", "")),
        normalize_endpoint_path(url),
    )


def group_findings(items: list[dict]) -> list[list[int]]:
    """把 findings 聚成若干组，返回每组的索引列表（组内按传入顺序）。

    items 需含: title / vuln_type / target_url（或 host）。
    """
    n = len(items)
    if n <= 1:
        return [list(range(n))] if n else []

    dsu = _DSU(n)
    keys = [_cluster_key(it) for it in items]
    prods = [product_keys(it.get("title", "")) for it in items]

    for i in range(n):
        hi, si, ei = keys[i]
        for j in range(i + 1, n):
            hj, sj, ej = keys[j]
            if si != sj:
                continue
            ti, tj = items[i].get("title", ""), items[j].get("title", "")
            # 条件 1：同 host 同大类，端点相同
            if hi and hi == hj and ei and ei == ej:
                dsu.union(i, j)
                continue
            # 条件 2：同 host 同大类，标题相似
            if hi and hi == hj and title_similarity(ti, tj) >= TITLE_SIM_THRESHOLD:
                dsu.union(i, j)
                continue
            # 条件 3：跨 host，但产品名有交集且标题相似（处理 CDN/别名域名）
            if prods[i] & prods[j] and title_similarity(ti, tj) >= TITLE_SIM_THRESHOLD + 0.1:
                dsu.union(i, j)

    buckets: dict[int, list[int]] = {}
    order: list[int] = []
    for i in range(n):
        r = dsu.find(i)
        if r not in buckets:
            buckets[r] = []
            order.append(r)
        buckets[r].append(i)
    return [buckets[r] for r in order]


_SEV_RANK = {"严重": 4, "高危": 3, "中危": 2, "低危": 1, "info": 0}


def build_clusters(items: list[dict]) -> list[dict]:
    """聚合并生成展示用结构。

    每个 cluster:
      {
        "primary": 代表条目（最重要 + 证据最全的一条）,
        "variants": [其余条目...],
        "count": 组内总数,
        "host": 归一化 host,
        "semantic": 语义大类,
        "severity": 组内最高定级,
        "indexes": 原始下标（便于前端映射）
      }
    代表条目选取：定级高 > 有 PoC 长 > 创建早（先发现的作为主）。
    """
    groups = group_findings(items)
    out: list[dict] = []
    for idxs in groups:
        def rank(i: int):
            it = items[i]
            return (
                _SEV_RANK.get(str(it.get("severity_claimed") or ""), 0),
                len(str(it.get("poc") or "")),
                -i,  # 越早越优先
            )

        primary_i = max(idxs, key=rank)
        primary = dict(items[primary_i])
        variants = [dict(items[i]) for i in idxs if i != primary_i]
        severities = [_SEV_RANK.get(str(items[i].get("severity_claimed") or ""), 0) for i in idxs]
        top_rank = max(severities) if severities else 0
        sev_name = next((k for k, v in _SEV_RANK.items() if v == top_rank), "")

        primary["variant_count"] = len(idxs)
        primary["variant_ids"] = [items[i].get("id") for i in idxs if i != primary_i][:50]
        primary["cluster_severity"] = sev_name
        primary["is_cluster_primary"] = len(idxs) > 1
        out.append({
            "primary": primary,
            "variants": variants,
            "count": len(idxs),
            "host": keys_host(items[primary_i]),
            "semantic": semantic_class(primary.get("title", ""), primary.get("vuln_type", "")),
            "severity": sev_name,
            "indexes": idxs,
        })
    # 组内条数多的排前，同数量按定级
    out.sort(key=lambda c: (-c["count"], -_SEV_RANK.get(c["severity"], 0)))
    return out


def keys_host(item: dict) -> str:
    return normalize_host(item.get("target_url") or item.get("host") or "")
