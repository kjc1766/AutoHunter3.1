"""运行时接口收割（3.1 新增）。

为什么需要这一层：
上游/2.1 的接口发现靠「LLM 读 JS 文本 + 发包试探」。一旦目标把 swagger 关了
（RuoYi `/v3/api-docs` 返回 36 字节空），worker 就完全看不见 `/api/pool/*`
这类业务线 —— 实测因此漏掉过 `orderByColumn` 的 ORDER BY 注入。

本模块用真实浏览器打开页面，监听所有 XHR/fetch，把「前端自己会调用的接口」
录下来。后端返回什么不重要 —— 401/空数据都行 —— 重要的是前端发出了哪些请求。

设计约束（2 核机器）：
- 短跑：单次最多 HARVEST_TIMEOUT 秒，用完立即关闭浏览器
- 全局锁：同一时刻只允许 1 个浏览器实例（避免 10 并发 × Chromium 打爆 CPU）
- 降级：没装 playwright 或启动失败时返回空结果，不阻塞任务
- 只录不测：本层不做任何漏洞探测，纯侦察；越权/注入交给 worker
"""

from __future__ import annotations

import asyncio
import logging
import os
import re
import time
from typing import Any
from urllib.parse import parse_qsl, urljoin, urlparse

logger = logging.getLogger(__name__)

# 单次收割总时长上限（秒）。2 核机器上 Chromium 会吃满约 1 核，
# 90 秒足够渲染常见 SPA 并触发首屏 XHR，再长收益递减。
HARVEST_TIMEOUT = int(os.environ.get("HARVEST_TIMEOUT_SEC", "90"))

# 页面静置多久就认为「不再有新请求」可提前结束（秒）
HARVEST_IDLE_SEC = int(os.environ.get("HARVEST_IDLE_SEC", "8"))

# 全局锁：同一时刻只跑一个浏览器
_HARVEST_LOCK = asyncio.Lock()

# 静态资源后缀：不是接口，录了也没用
_STATIC_EXT = re.compile(
    r"\.(?:js|css|png|jpe?g|gif|svg|ico|woff2?|ttf|eot|map|webp|avif|mp4|mp3)(?:\?|$)",
    re.IGNORECASE,
)
# 追踪/埋点域名，不录
_TRACKING_HOST = re.compile(
    r"(google-analytics|googletagmanager|doubleclick|sentry|hotjar|"
    r"cnzz|baidu\.com/hm\.js|umeng|beacon)",
    re.IGNORECASE,
)


def _is_api_request(url: str) -> bool:
    """判断一个请求是否值得记为接口。

    过滤静态资源、追踪埋点、data:/blob: 等。
    """
    if not url or url.startswith(("data:", "blob:", "about:")):
        return False
    if _STATIC_EXT.search(url.split("?")[0]):
        return False
    if _TRACKING_HOST.search(url):
        return False
    return True


def _normalize_endpoint(url: str, base_host: str) -> dict[str, Any] | None:
    """把一条请求 URL 归一成接口条目。

    返回 {path, method, params:[{name,value}], has_query}；非本域返回 None。
    """
    try:
        p = urlparse(url)
    except Exception:
        return None
    if p.hostname != base_host:
        return None
    path = p.path or "/"
    params = [{"name": k, "value": v} for k, v in parse_qsl(p.query, keep_blank_values=True)]
    return {
        "path": path,
        "method": "",
        "params": params,
        "has_query": bool(p.query),
    }


def _merge(endpoints: dict[str, dict], item: dict) -> None:
    """按 path 归并，合并 method 与参数名集合。"""
    key = item["path"]
    cur = endpoints.get(key)
    if cur is None:
        endpoints[key] = item
        return
    if item["method"] and item["method"] not in cur["methods"]:
        cur["methods"].append(item["method"])
    known = {x["name"] for x in cur["params"]}
    for prm in item["params"]:
        if prm["name"] not in known:
            cur["params"].append(prm)
            known.add(prm["name"])


async def harvest_endpoints(
    url: str,
    *,
    cookies: list[dict] | None = None,
    headers: dict[str, str] | None = None,
    timeout: int | None = None,
) -> dict[str, Any]:
    """打开页面并录制所有 XHR/fetch，返回接口清单。

    返回结构：
      {
        "ok": bool,
        "reason": str,           # 失败原因（ok=False 时）
        "base": str,             # 起点 URL
        "elapsed_ms": int,
        "count": int,            # 去重后的接口数
        "endpoints": [
          {"path": "/api/pool/list", "methods": ["GET"], "params": [{name,value}]},
        ],
        "raw_count": int,        # 原始请求条数（去重前）
      }
    """
    started = time.perf_counter()
    empty = {
        "ok": False, "reason": "", "base": url, "elapsed_ms": 0,
        "count": 0, "endpoints": [], "raw_count": 0,
    }

    try:
        from playwright.async_api import async_playwright
    except ImportError:
        empty["reason"] = "playwright_not_installed"
        logger.info("[harvest] playwright 未安装，跳过接口收割")
        return empty

    limit = timeout or HARVEST_TIMEOUT
    host = (urlparse(url).hostname or "").lower()
    if not host:
        empty["reason"] = "bad_url"
        return empty

    async with _HARVEST_LOCK:
        endpoints: dict[str, dict] = {}
        raw_count = 0
        last_seen = time.monotonic()

        try:
            async with async_playwright() as pw:
                browser = await pw.chromium.launch(
                    headless=True,
                    args=[
                        # 降低被 headless 检测识别的概率（瑞数等 WAF）
                        "--disable-blink-features=AutomationControlled",
                        "--no-sandbox",
                        "--disable-dev-shm-usage",   # 容器 /dev/shm 小，必须加
                        "--disable-gpu",
                        "--disable-extensions",
                        "--disable-background-networking",
                    ],
                )
                context = await browser.new_context(
                    user_agent=(
                        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                        "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
                    ),
                    viewport={"width": 1366, "height": 768},
                    locale="zh-CN",
                    ignore_https_errors=True,
                )
                # 去掉 webdriver 指纹
                await context.add_init_script(
                    "Object.defineProperty(navigator,'webdriver',{get:()=>undefined});"
                )
                if cookies:
                    try:
                        await context.add_cookies(cookies)
                    except Exception as e:
                        logger.info("[harvest] cookies 注入失败（忽略）: %s", str(e)[:80])

                page = await context.new_page()

                def _on_request(req) -> None:
                    nonlocal raw_count, last_seen
                    try:
                        if not _is_api_request(req.url):
                            return
                        item = _normalize_endpoint(req.url, host)
                        if not item:
                            return
                        item["methods"] = [req.method.upper()]
                        raw_count += 1
                        last_seen = time.monotonic()
                        _merge(endpoints, item)
                    except Exception:
                        pass

                page.on("request", _on_request)

                deadline = time.monotonic() + limit
                try:
                    await page.goto(url, wait_until="domcontentloaded", timeout=min(45000, limit * 1000))
                except Exception as e:
                    logger.info("[harvest] goto 异常（继续录）: %s", str(e)[:100])

                # 等待：直到超时或连续 HARVEST_IDLE_SEC 无新请求
                while time.monotonic() < deadline:
                    await asyncio.sleep(1)
                    if (time.monotonic() - last_seen) >= HARVEST_IDLE_SEC and raw_count > 0:
                        break

                await context.close()
                await browser.close()
        except Exception as e:
            logger.warning("[harvest] 浏览器异常: %s", str(e)[:200])
            empty["reason"] = f"browser_error: {str(e)[:120]}"
            empty["raw_count"] = raw_count
            empty["elapsed_ms"] = int((time.perf_counter() - started) * 1000)
            return empty

    result = {
        "ok": True,
        "reason": "",
        "base": url,
        "elapsed_ms": int((time.perf_counter() - started) * 1000),
        "count": len(endpoints),
        "endpoints": sorted(endpoints.values(), key=lambda x: x["path"]),
        "raw_count": raw_count,
    }
    logger.info("[harvest] %s → %d 个接口（原始请求 %d 条，%d ms）",
                host, result["count"], raw_count, result["elapsed_ms"])
    return result


def format_for_prompt(harvest: dict[str, Any], max_items: int = 60) -> str:
    """把接口清单渲染成给 worker 看的紧凑文本（省 token）。"""
    if not harvest.get("ok") or not harvest.get("endpoints"):
        return ""
    lines = [
        "## 运行时收割到的真实接口（浏览器录制，前端实际发出过）",
        "",
        "以下接口不一定都能未授权访问，但**确认存在于该系统**，优先对带参数的做注入/越权探测：",
        "",
    ]
    # 带参数的排前面：它们才是注入候选
    eps = sorted(harvest["endpoints"], key=lambda x: (not x["params"], x["path"]))
    for ep in eps[:max_items]:
        methods = "/".join(ep.get("methods") or []) or "?"
        prm = ""
        if ep["params"]:
            names = ",".join(x["name"] for x in ep["params"][:8])
            prm = f"  参数: {names}"
        lines.append(f"- `{methods} {ep['path']}`{prm}")
    if len(eps) > max_items:
        lines.append(f"- …（共 {len(eps)} 个，已省略 {len(eps) - max_items} 个）")
    return "\n".join(lines)
