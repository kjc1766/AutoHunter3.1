"""Worker Agent：1:1 绑定一个目标，LLM + 工具真实挖洞。

流程（对应设计文档 §5.5）：
  只给一个裸 target → LLM 完全自主侦察+挖掘（function calling 循环）
  → 发现漏洞调 submit_finding → 挖完调 finish → 产出 WorkerResult。
"""
from __future__ import annotations

import json
import os
import re
import threading
import time
from typing import Any, Callable, Optional
from urllib.parse import urlparse

from pydantic import ValidationError

from app.agents.history import compact_messages
from app.agents.prompts import is_enterprise_src, normalize_worker_prompt_version, worker_system_prompt
from app.agents.backdoor_proof import weak_backdoor_block_reason
from app.agents.edu_scope import edu_bombing_block_reason
from app.agents.write_proof import HARMLESS_PROTOCOL, weak_write_block_reason
from app.agents import auth_bootstrap
from app.config import worker_config
from app.tools.cookie_manager import CookieHub
from app import dedup
from app.llm.client import LLMClient, LLMError, llm_error_event_fields
from app.schemas import Finding, Verdict, WorkerResult
from app.tools.executor import ToolExecutor
from app.tools.schemas import (
    JS_ANALYZER_TOOL_SCHEMAS,
    KB_TOOL_SCHEMAS,
    SESSION_TOOL_SCHEMAS,
    TOOL_SCHEMAS,
)


_BROAD_NMAP_RE = re.compile(r"\bnmap\b[\s\S]*(?:-p\s*(?:-|1-10000|1-65535|0-65535)|--top-ports\s+\d{3,})", re.IGNORECASE)
_SLEEP_RE = re.compile(r"\bsleep\s+(\d+)", re.IGNORECASE)
# 同类漏洞产量熔断：同一个语义大类（sqli / unauthorized_access / weak_cred …）
# 命中 quota 条后，worker 不再继续在该类上耗轮次——写够报告即可，剩下的交给人工点「深挖」。
# 实测同一个 rprOrder SQL 注入被写出 10 个变体、鑫贝帝弱口令 15 个变体，
# 后 8~13 条对最终报告没有增量，纯烧 token。
VULN_CLASS_QUOTA = int(os.environ.get("VULN_CLASS_QUOTA", "2"))
_FOR_LIST_RE = re.compile(r"\bfor\s+\w+\s+in\s+([^;\n]+);", re.IGNORECASE)
# 循环项像「注入/绕过 payload」而不是「路径/子域」的特征：
# 引号、SQL 关键字、逻辑运算符、注释符、编码站点。
_PAYLOAD_HINT = re.compile(
    r"['\"]|--|\b(and|or|union|select|sleep|benchmark|waitfor)\b|<>!=|%[0-9a-f]{2}|\$\{",
    re.IGNORECASE,
)
# 「接口/文档路径」特征：这类枚举是 SRC 找未授权接口的核心手段，不算低价值目录爆破。
_API_PATH_HINT = re.compile(
    r"(^|/)(api|open|rest|swagger|api-docs|swagger-resources|doc\.html|v[12])"
    r"|\.(json|wsdl)$",
    re.IGNORECASE,
)
_JS_INTENT_RE = re.compile(
    r"(?i)(?:审计|分析|提取|查看|深入|打|挖).{0,24}(?:js|javascript|前端|script|接口|密钥|secret|token)"
    r"|(?:^|[\s/\"'=])[\w./-]+\.js(?:[?#\"'\s>)]|$)|<script\b|id=[\"'](?:app|root)[\"']"
)
_WORKER_STATIC_PREFIX = (
    "下一条是目标/情报。只打当前目标；确认无攻击面才快速 finish。工具按信号开放，JS 线索再用 analyze_javascript。"
)

# LLM 调用失败时，worker 内软重试次数（清粘性后换端点/同端点再试），耗尽才整轮收尾回队。
_WORKER_LLM_SOFT_RETRIES = int(os.environ.get("WORKER_LLM_SOFT_RETRIES", "3"))
_WORKER_LLM_SOFT_RETRY_KINDS = {
    "rate_limit", "timeout", "network", "upstream", "provider_cooldown",
    "blocked", "unknown", "quota",
}


class Worker:
    def __init__(
        self,
        target: str,
        llm: Optional[LLMClient] = None,
        on_event: Optional[Callable[[str, dict], None]] = None,
        deepen_context: Optional[dict] = None,
        target_meta: Optional[dict] = None,
        duplicate_history: Optional[list[dict]] = None,
        cancel_event: Optional[threading.Event] = None,
        src_type: str = "edusrc",
        fofa_key: str = "",
        fofa_base_url: str = "",
        engine: str = "fofa",
        prompt_version: str | None = None,
        src_rules: str = "",
        redline_checks: Any = None,
        pop_directive: Optional[Callable[[], Optional[str]]] = None,
        task_id: str = "",
    ):
        self.target = target
        self.task_id = task_id or ""
        self.llm = llm or LLMClient()
        self.cancel_event = cancel_event or threading.Event()
        self.src_type = src_type
        self._enterprise = is_enterprise_src(src_type)
        self.src_rules = src_rules or ""
        # 用户勾选的任务级红线，渲染成提示词片段拼在 system 末尾
        try:
            from app.redlines import render_redline_prompt
            self.redline_prompt = render_redline_prompt(redline_checks)
        except Exception:
            self.redline_prompt = ""
        self.prompt_version = normalize_worker_prompt_version(prompt_version or worker_config.prompt_version)
        self.executor = ToolExecutor(
            target, cancel_event=self.cancel_event,
            enterprise=self._enterprise, fofa_key=fofa_key, fofa_base_url=fofa_base_url,
            engine=engine, task_id=self.task_id,
        )
        self._cookie_hub = CookieHub(self.task_id, target)
        self.executor._cookie_hub = self._cookie_hub
        self.findings: list[Finding] = []
        # 同类漏洞命中计数（按语义大类）。达到 quota 后 worker 停止继续挖同类、
        # 只写报告并标记"可深挖"，省 token。见 _vuln_class_quota_exceeded。
        self._class_hits: dict[str, int] = {}
        # 已经触发过熔断的类别：重复命中时只提示停止，不再重复建议深挖
        self._class_capped: set[str] = set()
        self.on_event = on_event or (lambda kind, data: None)
        self._finished: Optional[dict] = None
        # 审核打回的定向深挖任务：{directive, vuln_type, original_title, original_summary}
        self.deepen_context = deepen_context or None
        # 人工 mid-run 指令：编排层按轮次弹出一条，注入下一轮 user 消息。
        self.pop_directive = pop_directive
        # 资产情报：候选归属学校/org/title，供 worker 核实并写进报告 owner
        self.target_meta = target_meta or {}
        # 同一 target 历史已提交漏洞摘要，用于 worker 提交前查重（superseded 不传入）
        self.duplicate_history = duplicate_history or []
        # JS 审计工具 schema 体积较大，默认只在目标/情报/响应出现 JS 信号后开放。
        self._js_tool_enabled = self._initial_js_tool_enabled()
        self._js_signal_seen = self._js_tool_enabled
        self._tool_counts: dict[str, int] = {}
        self._http_urls: list[str] = []
        self._last_js_analysis_round = 0
        self._post_js_validation_count = 0
        # worker 主动上报的可复用情报（纯内存收集，由编排层 async 统一落全局情报库）
        self._reported_intel: list[dict] = []
        # 单站协作覆盖记录（API/入口/测试项摘要），由编排层写入事件流供后续 worker 复用。
        self._reported_coverage: list[dict] = []

    def _emit(self, kind: str, **data: Any) -> None:
        self.on_event(kind, data)

    def _initial_js_tool_enabled(self) -> bool:
        if worker_config.js_tool_always_on:
            return True
        meta = self.target_meta or {}
        if (meta.get("site_collab_route") or {}).get("js_first"):
            return True
        text = "\n".join([
            self.target,
            str(meta.get("title") or ""),
            str(meta.get("priority_reason") or ""),
            str((meta.get("playbook_route") or {}).get("route_id") or ""),
            " ".join((meta.get("playbook_route") or {}).get("tags") or []),
            str(meta.get("playbook_block") or ""),
            json.dumps(self.deepen_context or {}, ensure_ascii=False),
        ])
        low = text.lower()
        if _JS_INTENT_RE.search(text):
            return True
        return any(marker in low for marker in (
            "spa", "webpack", "vue", "react", "angular", "frontend", "front-end",
            "javascript", "script", "api_exposed", "secret", "前端",
        ))

    def _intel_block(self) -> str:
        m = self.target_meta or {}
        school = (m.get("school") or "").strip()
        org = (m.get("org") or "").strip()
        title = (m.get("title") or "").strip()
        source = (m.get("source") or "").strip()
        site = self._site_collab_block()
        priority_reason = (m.get("priority_reason") or "").strip()
        playbook = self._playbook_block()
        # 即使没有资产情报，只要有泄露凭证/情报库命中也要带出去（企业目标常无 school/org/title）。
        if not (school or org or title or source):
            return site + playbook + self._user_auth_block() + self._creds_block() + self._intel_lib_block()
        owner_label = "候选归属单位/系统" if is_enterprise_src(self.src_type) else "候选归属学校"
        prefix = [b.rstrip() for b in (site, playbook) if b.strip()]
        lines = prefix + ["# 资产情报（搜集阶段提供，需你核实）"]
        if school:
            lines.append(f"- {owner_label}：{school}")
        if org:
            lines.append(f"- 单位(org)：{org}")
        if title:
            lines.append(f"- 站点标题：{title}")
        if source == "killsweep":
            lines.append("- 来源：通杀验证目标（已由通杀分析找到同款系统并验证过 1 个点）")
            if priority_reason:
                lines.append(f"- 通杀上下文：{priority_reason}")
            lines.append("注意：你只负责把当前站点的实际漏洞证据打出来，不要围绕该产品继续做通杀扩散判断。")
        lines.append("提交漏洞时，请核实归属（域名/备案/证书CN/页脚版权/FOFA org/登录页品牌）后把最终归属写进 submit_finding 的 owner 字段。")
        return "\n".join(lines) + "\n\n" + self._user_auth_block() + self._creds_block() + self._intel_lib_block()

    def _user_auth_block(self) -> str:
        """用户在凭据区提供的 Cookie/账密（系统已尝试后的回执）。"""
        ctx = (self.target_meta or {}).get("user_auth") or (self.target_meta or {}).get("auth_context")
        attempt = (self.target_meta or {}).get("auth_attempt")
        if not ctx and not attempt:
            return ""
        return auth_bootstrap.user_auth_prompt_block(ctx, attempt)

    def _bootstrap_user_auth(self) -> None:
        """启动时：全局 Cookie 优先，否则用用户凭据登录；失败则后续 http 自动重登。"""
        ctx = (self.target_meta or {}).get("user_auth") or (self.target_meta or {}).get("auth_context")
        if not isinstance(ctx, dict):
            ctx = None
        hub = self._cookie_hub
        if ctx:
            hub.remember_from_auth_context(ctx)
        elif hub.creds().get("username") and hub.creds().get("password"):
            stored = hub.creds()
            ctx = {
                "matched": True,
                "kinds": ["password"],
                "username": stored.get("username") or "",
                "password": stored.get("password") or "",
                "login_url": stored.get("login_url") or "",
                "matched_by": "shared",
                "binding_target": "全局会话",
            }
            self.target_meta["user_auth"] = ctx
            self.target_meta["auth_context"] = ctx
        hub.bootstrapping = True
        result = None
        login_base = auth_bootstrap.login_origin(self.target) or self.target
        try:
            if hub.apply(self.executor):
                names = sorted(getattr(self.executor, "_session_cookies", {}).keys())[:30]
                headers = sorted(getattr(self.executor, "_session_headers", {}).keys())[:20]
                result = auth_bootstrap.AuthAttemptResult(
                    used=True, matched=True, status="injected",
                    kinds=["cookie"], matched_by="shared", binding_target="全局会话",
                    reason="复用本站全局 Cookie",
                    cookie_names=names, header_names=headers,
                )
            if result is None and ctx:
                with hub.login_turn() as action:
                    if action == "reuse" and hub.apply(self.executor):
                        names = sorted(getattr(self.executor, "_session_cookies", {}).keys())[:30]
                        result = auth_bootstrap.AuthAttemptResult(
                            used=True, matched=True, status="injected",
                            kinds=["cookie"], matched_by="shared", binding_target="全局会话",
                            reason="复用本站全局 Cookie",
                            cookie_names=names,
                        )
                    else:
                        result = auth_bootstrap.bootstrap_auth(self.executor, ctx, login_base)
                        if result.status in ("injected", "login_ok"):
                            hub.ingest(self.executor, status=result.status)
        finally:
            hub.bootstrapping = False
        if result is None:
            return
        payload = result.as_event()
        self.target_meta["auth_attempt"] = payload
        self._emit(
            "auth_status",
            message=auth_bootstrap.format_auth_status_message(result),
            **payload,
        )

    def _playbook_block(self) -> str:
        """目标打法路由：编排层生成的短路线块。"""
        return (self.target_meta or {}).get("playbook_block") or ""

    def _site_collab_block(self) -> str:
        """单站协作路线块：当前 worker 的分工和已有覆盖摘要。"""
        return (self.target_meta or {}).get("site_collab_block") or ""

    def _intel_lib_block(self) -> str:
        """全局情报库命中（编排层触发式检索后注入的现成文本块）。"""
        return (self.target_meta or {}).get("intel_block") or ""

    def _creds_block(self) -> str:
        """泄露凭证情报：搜集阶段查到的该域已泄露账号密码（已过滤打分）。"""
        ctx = (self.target_meta or {}).get("user_auth") or (self.target_meta or {}).get("auth_context")
        if auth_bootstrap.has_login_material(ctx):
            return ""
        if self._cookie_hub.creds().get("username"):
            return ""
        creds = (self.target_meta or {}).get("leaked_creds") or []
        if not creds:
            return ""
        lines = [
            "# 泄露凭证情报（搜集阶段已过滤打分）",
            "以下账密按可用概率排序；它们只是深挖入场券，不是漏洞本身。",
        ]
        for c in creds[:12]:
            u = (c.get("username") or "")[:40]
            p = (c.get("password") or "")[:40]
            h = (c.get("host") or "")[:40]
            lines.append(f"- {u} : {p}  （泄露于 {h}）")
        lines.append("纪律：登录成功/CASTGC/session/个人中心本身不算洞；必须继续实证死规矩敏感数据、越权、敏感写操作、注入/上传 getshell 或具体业务系统危害。没实锤就写 deepen_lead；试 2-3 个高价值凭证失败就换攻击面；严禁改密。")
        return "\n".join(lines) + "\n\n"

    def _duplicate_block(self) -> str:
        if not self.duplicate_history:
            return ""
        lines = ["# 统一查重上下文（跨任务同 host / 通杀明细，勿重复提交）"]
        lines.append(f"后端完整查重池含 {len(self.duplicate_history)} 条；这里只列摘要。提交前必须调用 check_duplicate_finding。")
        lines.append("duplicate=true 才禁止提交同系统同洞；其它 endpoint/类型/证据链可继续。")
        for item in self.duplicate_history[:6]:
            reason = (item.get("dedup_reason") or "")[:80]
            lines.append(
                f"- 来源={item.get('source','history')}；[{item.get('vuln_type','')}] {item.get('title','')} "
                f"@ {item.get('target_url','')}（状态：{item.get('status','')}；原因：{reason or '已存在'}）"
            )
        if len(self.duplicate_history) > 6:
            lines.append(f"- 其余 {len(self.duplicate_history) - 6} 条仅在后台查重池中。")
        return "\n".join(lines) + "\n\n"

    def run(self) -> WorkerResult:
        # 用户凭据：在任何 LLM 轮次前强制尝试，结果写进 target_meta 供 prompt 与看板。
        try:
            self._bootstrap_user_auth()
        except Exception as e:
            self._emit("auth_status", used=True, matched=True, status="login_fail",
                       kinds=[], reason=f"凭据启动异常: {type(e).__name__}: {e}"[:300],
                       message=f"凭据启动异常: {e}")

        # 上一轮 LLM 中断留下的进度：笔记 + 会话态先恢复，再开挖
        self._restore_interrupt_progress()

        if self.deepen_context:
            user_content = self._intel_block() + self._duplicate_block() + self._deepen_brief()
            self._emit("worker_start", target=self.target, mode="deepen", prompt_version=self.prompt_version)
        else:
            user_content = (
                self._intel_block()
                + self._duplicate_block()
                + f"目标：{self.target}\n\n"
                + "只挖此目标；自主侦察取证，结束调用 finish。"
            )
            self._emit("worker_start", target=self.target, prompt_version=self.prompt_version)
        messages: list[dict[str, Any]] = [
            {"role": "system", "content": worker_system_prompt(self.src_type, self.prompt_version, src_rules=self.src_rules)
             + (("\n\n" + self.redline_prompt) if self.redline_prompt else "")},
            {"role": "user", "content": _WORKER_STATIC_PREFIX},
            {"role": "user", "content": user_content},
        ]

        rounds = 0
        no_tool_rounds = 0
        # auto 兼容模式下，检测到「哑模型」(全程零工具)时只自愈切一次提示词模拟，避免反复切
        tool_compat_selfheal_tried = False
        consecutive_failures = 0
        consecutive_blocked = 0
        consecutive_arg_errors = 0
        consecutive_network_failures = 0
        consecutive_llm_failures = 0
        # 按 src_type 取预算：企业模式给更大深挖空间（110/60），edu 走量沿用 90/45。
        max_rounds, soft_rounds = self._route_rounds(*worker_config.rounds_for(self.src_type))
        while rounds < max_rounds:
            if self.cancel_event.is_set():
                return self._cancelled_result(rounds)
            # 人工实时指令：在开新一轮 LLM 前注入，优先于自主打法。
            # 用 getattr：部分单测用 Worker.__new__ 绕过 __init__。
            directive = ""
            pop_directive = getattr(self, "pop_directive", None)
            if pop_directive:
                try:
                    directive = (pop_directive() or "").strip()
                except Exception:
                    directive = ""
            if directive:
                messages.append({
                    "role": "user",
                    "content": (
                        "# 人工实时指令（优先执行）\n"
                        f"{directive}\n\n"
                        "请按上述指令调整本轮打法，继续调用工具验证或 finish。"
                    ),
                })
                self._emit("worker_directive", round=rounds + 1, text=directive[:500])
            rounds += 1
            try:
                self._emit("llm_round_start", round=rounds)
                tools = list(TOOL_SCHEMAS)
                # 会话保持工具全模式开放：拿到泄露/用户凭证登录后固化登录态再深挖。
                tools += SESSION_TOOL_SCHEMAS
                if self._js_tool_enabled:
                    tools += JS_ANALYZER_TOOL_SCHEMAS
                # 实战手册知识库：按需检索，不预载正文（1.6 万行进 system prompt 会撑爆 context）。
                tools += KB_TOOL_SCHEMAS
                send_messages = compact_messages(messages, rounds)
                # 每轮注入当前状态块（会话态 + 工作笔记）——临时消息，不存入 messages 历史，
                # 避免累积膨胀；每轮新鲜生成，始终反映最新的 cookie/token/notes。
                # 这是连续性的核心：即使旧历史被压缩成摘要，worker 仍能看到自己当前
                # 持有哪些登录态、记录了哪些关键进度，不会跨轮"失忆"重复扫。
                send_messages.append({"role": "user", "content": self.executor.session_status_block()})
                msg = self.llm.chat(send_messages, tools=tools, tool_choice="auto")
                consecutive_llm_failures = 0
            except Exception as e:
                fields = llm_error_event_fields(e)
                self._emit("llm_error", **fields)
                failure_kind = e.kind if isinstance(e, LLMError) else ""
                retry_after = e.retry_after if isinstance(e, LLMError) else 0
                if self._should_soft_retry_llm(e) and consecutive_llm_failures < _WORKER_LLM_SOFT_RETRIES:
                    consecutive_llm_failures += 1
                    clearer = getattr(self.llm, "clear_sticky_provider", None)
                    if callable(clearer):
                        clearer()
                    wait_s = min(2 ** (consecutive_llm_failures - 1), 8)
                    if retry_after:
                        wait_s = max(wait_s, min(int(retry_after), 30))
                    self._emit(
                        "llm_soft_retry",
                        round=rounds,
                        attempt=consecutive_llm_failures,
                        max_attempts=_WORKER_LLM_SOFT_RETRIES,
                        failure_kind=failure_kind or "unknown",
                        wait_seconds=wait_s,
                        error=str(e)[:240],
                        error_copy=fields.get("error_copy") or str(e),
                        detail=fields.get("detail") or "",
                        diagnostic=fields.get("diagnostic") or "",
                    )
                    # 不消耗轮次预算：基础设施抖动不应吃掉挖掘配额
                    rounds = max(0, rounds - 1)
                    if self.cancel_event.wait(wait_s):
                        return self._cancelled_result(rounds)
                    continue
                err_text = str(e)
                if not err_text.startswith("LLM"):
                    err_text = f"LLM 调用失败：{err_text}"
                return self._llm_interrupt_result(
                    rounds=rounds,
                    error=err_text,
                    failure_kind=failure_kind,
                    retry_after=retry_after,
                )
            if self.cancel_event.is_set():
                return self._cancelled_result(rounds)

            # 模型可能只回文本（思考），也可能带 tool_calls
            tool_calls = getattr(msg, "tool_calls", None)
            assistant_msg: dict[str, Any] = {"role": "assistant", "content": msg.content or ""}
            if tool_calls:
                assistant_msg["tool_calls"] = [
                    {
                        "id": tc.id,
                        "type": "function",
                        "function": {"name": tc.function.name, "arguments": tc.function.arguments},
                    }
                    for tc in tool_calls
                ]
            messages.append(assistant_msg)

            # 是否在本轮要插入 JS 工具提示。注意：若本轮带 tool_calls，这条 user 提示必须
            # 延迟到所有 tool 响应 append 之后再插入，否则会破坏 assistant(tool_calls) → tool
            # 的连续性，触发 400。
            js_hint_pending = False
            if msg.content:
                self._emit("worker_thought", round=rounds, text=msg.content[:500])
                if self._maybe_enable_js_tool(msg.content, "模型明确提出 JS/前端分析意图"):
                    js_hint_pending = True
            js_hint_msg = {
                "role": "user",
                "content": "JS 工具已开放：analyze_javascript 只给线索，必须再用 http_request/run_shell 实证。",
            }
            if js_hint_pending and not tool_calls:
                messages.append(js_hint_msg)
                js_hint_pending = False

            if not tool_calls:
                no_tool_rounds += 1
                # auto 自愈：全程一个工具都没调过 + 是 auto 兼容模式 → 疑似「接受 tools 但不真正
                # 调工具」的哑模型。提前(第3轮)让 LLM 客户端把当前端点切成提示词模拟再给它机会，
                # 而不是空转到第6轮才放弃、还要用户手动设 AUTOHUNTER_TOOL_COMPAT=prompt。
                # getattr 防御：单测里 self.llm 可能是 mock，没有该方法。
                if (not tool_compat_selfheal_tried
                        and no_tool_rounds >= 3
                        and sum(self._tool_counts.values()) == 0):
                    switch = getattr(self.llm, "force_prompt_tools_current", None)
                    if callable(switch) and switch():
                        tool_compat_selfheal_tried = True
                        no_tool_rounds = 0
                        self._emit("tool_compat_switch", round=rounds,
                                   detail="模型全程零工具，自动切提示词模拟工具调用重试")
                        messages.append({"role": "user", "content": "（已切换为提示词模拟工具调用）请按工具协议继续调用工具，或 finish。"})
                        continue
                if no_tool_rounds >= 6:
                    # 两种情况分开说清楚，别再堆黑话：
                    # ① 全程一个工具都没调过 → 是所选模型本身不会 function calling（哑模型）。
                    #    注意：真·报错「不支持 tools」的已被 LLM 层自动切提示词模拟兜底，走不到这里；
                    #    能走到这里说明模型没报错、返回正常，只是从不发起工具调用。
                    # ② 之前调过工具、但最近连续 6 轮又不调也不 finish → 模型在原地绕圈，空转收尾。
                    if sum(self._tool_counts.values()) == 0:
                        if tool_compat_selfheal_tried:
                            reason_msg = (
                                "没挖成：当前模型不会调用工具，已自动尝试提示词模拟仍无效。"
                                "请更换支持工具调用的模型(DeepSeek/GPT/Claude/通义/Kimi 等)。"
                            )
                        else:
                            reason_msg = (
                                "没挖成：当前模型不会调用工具(function calling)，连续 6 轮只回文字、不调工具，没法挖。"
                                "不是目标站问题，也不是报错，是模型能力不够。"
                                "解决：换个支持工具调用的模型(DeepSeek/GPT/Claude/通义/Kimi 等)，"
                                "或在服务端设 AUTOHUNTER_TOOL_COMPAT=prompt 强制模拟。设置页「测试连接」可检测。"
                            )
                    else:
                        reason_msg = (
                            "自动收尾：模型连续 6 轮既不调工具也不结束(finish)，在原地绕圈，已收尾。"
                            "可重试或换更强的模型。"
                        )
                    self._auto_finish(reason_msg, "model_behavior")
                    break
                # 没有工具调用也没结束，提醒模型继续或收尾
                messages.append({"role": "user", "content": "继续调用工具验证，或 finish。"})
                continue
            no_tool_rounds = 0

            # 逐个执行工具调用。
            # 关键：OpenAI 协议要求 assistant.tool_calls 里【每一个】tool_call_id 都必须有
            # 对应的 tool 响应消息，否则下一轮请求会 400（insufficient tool messages）。
            # 因此用 answered 跟踪已响应的 id，无论循环怎么提前退出（收敛 break / 取消），
            # 循环结束后都补齐所有未响应的 tool_call，保证 messages 历史始终合法。
            answered: set[str] = set()
            cancelled_mid = False
            blocked_nudge_pending = False
            for tc in tool_calls:
                if self.cancel_event.is_set():
                    cancelled_mid = True
                    break
                name = tc.function.name
                try:
                    args = json.loads(tc.function.arguments or "{}")
                except json.JSONDecodeError as e:
                    args = {}
                    result = self._tool_arg_error(
                        name, "valid JSON arguments",
                        f"工具参数不是合法 JSON：{e}。请修正后只做一个高价值验证请求；无明确验证动作就 finish(no_vuln)。",
                    )
                    self._emit("tool_arg_error", round=rounds, tool=name, error=str(e))
                else:
                    try:
                        result = self._dispatch(name, args, rounds)
                    except Exception as e:
                        result = {
                            "ok": False,
                            "error": f"工具执行异常: {type(e).__name__}: {e}",
                            "guidance": "不要重复触发同一异常。请换成最小可验证请求；若无明确路径就 finish(no_vuln)。",
                        }
                        self._emit("tool_exception", round=rounds, tool=name, error=str(e))
                # 工具失败时注入针对性恢复提示，帮模型在同流里快速纠偏而非从头推理。
                hint = self._recovery_hint(name, result)
                if hint:
                    result.setdefault("guidance", hint)
                messages.append({
                    "role": "tool",
                    "tool_call_id": tc.id,
                    "content": json.dumps(result, ensure_ascii=False),
                    "_round": rounds,
                    "_tool": name,
                })
                answered.add(tc.id)

                outcome = self._tool_outcome(result)
                if outcome == "ok":
                    consecutive_failures = 0
                    consecutive_blocked = 0
                    consecutive_arg_errors = 0
                    consecutive_network_failures = 0
                    continue

                consecutive_failures += 1
                consecutive_blocked = consecutive_blocked + 1 if outcome == "blocked" else 0
                consecutive_arg_errors = consecutive_arg_errors + 1 if outcome == "arg_error" else 0
                consecutive_network_failures = consecutive_network_failures + 1 if outcome in ("network", "timeout") else 0

                if consecutive_blocked >= 2:
                    # 被策略拦截的是“方向错”，不是目标无漏洞。以前这里直接 auto_finish，
                    # 会造成目标在 1-2 秒内被判 no_vuln/dead。现在只纠偏，不把目标判死。
                    blocked_nudge_pending = True
                    consecutive_failures = 0
                    consecutive_blocked = 0
                    continue
                if consecutive_arg_errors >= 3:
                    self._auto_finish(
                        "连续 3 次工具参数错误，模型未修正，本轮未得到可靠结论。",
                        "tool_argument",
                    )
                    break
                if consecutive_network_failures >= 3:
                    self._auto_finish("连续 3 次网络/超时失败，目标当前不可稳定验证，系统自动收敛。")
                    break
                if consecutive_failures >= 8:
                    self._auto_finish("连续 8 次工具失败且无新证据，系统自动收敛。")
                    break

            # 补齐所有未响应的 tool_call，保证消息历史合法（防 400）。
            for tc in tool_calls:
                if tc.id not in answered:
                    messages.append({
                        "role": "tool",
                        "tool_call_id": tc.id,
                        "content": json.dumps(
                            {"ok": False, "error": "该工具调用未执行（本轮已收敛或被取消）。"},
                            ensure_ascii=False,
                        ),
                    })

            if cancelled_mid:
                return self._cancelled_result(rounds)

            # tool 响应已全部 append，此时再补上延迟的 JS 工具提示，保证顺序合法。
            if js_hint_pending:
                messages.append(js_hint_msg)

            if self._finished is not None:
                break

            if blocked_nudge_pending:
                messages.append({
                    "role": "user",
                    "content": (
                        "低价值动作已拦截。改做 JS/API/登录/上传/导出/Swagger/actuator 等明确入口的最小实证；别泛扫或打姊妹域。"
                    ),
                })

            # 早收敛提醒：尽早打断低价值空转，但只提醒，不硬杀复杂目标。
            if not self.findings and rounds in (12, 20, 30):
                messages.append({
                    "role": "user",
                    "content": (
                        f"收敛检查：{rounds} 轮无实锤。若仍是枚举/网络/公开数据，打最后一个明确验证或 finish(no_vuln)。"
                    ),
                })

            # 软引导：超过软阈值后，每轮催 worker 收尾，避免低价值空转（不硬杀）
            if rounds >= soft_rounds:
                remaining = max_rounds - rounds
                if remaining <= 5:
                    nudge = (
                        f"仅剩 {remaining} 轮：有洞 submit_finding 后 finish；无实锤立即 finish(no_vuln)。"
                    )
                else:
                    nudge = (
                        f"已 {rounds} 轮：聚焦实锤；别再穷举。无明确突破就 finish(no_vuln)。"
                    )
                messages.append({"role": "user", "content": nudge})

        # 容错：_finished 里的 verdict 若非枚举值（模型乱填/旧格式），降级为 error 而不是抛异常中断整条流水线。
        try:
            verdict = Verdict(self._finished["verdict"]) if self._finished else Verdict.inconclusive
        except (ValueError, KeyError):
            verdict = Verdict.error
        # 没主动 finish = 跑满轮次还没定论，这属于 inconclusive（做了但说不清），
        # 不是系统 error。用 error 会被当成故障走 transient 分支，还可能污染 LLM 健康度统计；
        # inconclusive 则会正常换角度重试一次，这才符合「挖了很多但没结论」的事实。
        if not self._finished and not self.findings:
            verdict = Verdict.inconclusive
        # 以实际结果为准：只要真提交了漏洞，就不该被记成任何「非 found」结论。
        # 原来只纠正 no_vuln，导致 worker 说 blocked/inconclusive 但实际出了洞时，
        # 目标会被挂起/重试，漏洞却被埋在库里没进复审。
        if self.findings and verdict != Verdict.found:
            verdict = Verdict.found
        return WorkerResult(
            target=self.target,
            verdict=verdict,
            findings=self.findings,
            summary=(self._finished or {}).get("summary", ""),
            rounds=rounds,
            error=(self._finished or {}).get("error") or (
                None if self._finished else f"达到最大轮数 {max_rounds} 未主动结束"
            ),
            failure_kind=(self._finished or {}).get("failure_kind", ""),
            deepen_lead=(self._finished or {}).get("deepen_lead", ""),
            block_reason=(self._finished or {}).get("block_reason", ""),
            unblock_condition=(self._finished or {}).get("unblock_condition", ""),
            reported_intel=self._reported_intel,
            reported_coverage=self._reported_coverage,
        )

    def _route_rounds(self, max_rounds: int, soft_rounds: int) -> tuple[int, int]:
        """按打法路线微调软收敛节奏。

        deep 路线（Actuator/Nacos/API docs/低代码等）更容易需要多步链路，延后软催收；
        static_low_value 才收紧硬上限，避免门户/官网长时间空转。
        """
        route = (self.target_meta or {}).get("playbook_route") or {}
        route_id = str(route.get("route_id") or "")
        intensity = str(route.get("intensity") or "")
        if intensity == "deep":
            soft_rounds = max(soft_rounds, min(max_rounds, 36 if not self._enterprise else 48))
        elif route_id == "static_low_value":
            soft_rounds = min(soft_rounds, 12)
            max_rounds = min(max_rounds, 30)
        elif intensity == "quick":
            soft_rounds = min(soft_rounds, 18)
        return max(1, max_rounds), max(1, min(soft_rounds, max_rounds))

    def _cancelled_result(self, rounds: int) -> WorkerResult:
        self._emit("worker_cancelled", target=self.target, round=rounds)
        return WorkerResult(
            target=self.target,
            verdict=Verdict.error,
            findings=self.findings,
            summary="任务已被 pause/stop 控制面取消，结果由 orchestrator 丢弃。",
            rounds=rounds,
            error="worker cancelled by task control",
            resume_context=self._build_resume_context(rounds),
        )

    @staticmethod
    def _should_soft_retry_llm(exc: BaseException) -> bool:
        """限流/超时/网络/冷却/策略拦截等：同轮内再试（池模式会换端点）。"""
        if isinstance(exc, LLMError):
            return exc.kind in _WORKER_LLM_SOFT_RETRY_KINDS or not exc.kind
        # 非 LLMError 的瞬时异常也给一次机会
        text = str(exc).lower()
        return any(k in text for k in ("timeout", "timed out", "connection", "network", "429", "rate"))

    def _build_resume_context(self, rounds: int) -> dict:
        snap = self.executor.export_resume_state()
        notes = (snap.get("worker_notes") or "").strip()
        cookies = snap.get("session_cookies") or {}
        headers = snap.get("session_headers") or {}
        has_progress = bool(notes or cookies or headers or self.findings or rounds >= 2)
        if not has_progress:
            return {}
        directive_bits = [
            "上一轮因 LLM 调用中断，请从已有进度继续，不要从头泛扫。",
        ]
        if notes:
            directive_bits.append(f"工作笔记：\n{notes[:1500]}")
        if cookies or headers:
            directive_bits.append(
                f"已恢复会话态（cookie {sorted(cookies.keys())}，鉴权头 {sorted(headers.keys())}），"
                "优先用现有登录态继续深挖。"
            )
        if self.findings:
            directive_bits.append(
                f"本轮已提交 {len(self.findings)} 个漏洞，继续挖其它入口或 finish。"
            )
        return {
            "directive": "\n".join(directive_bits)[:2000],
            "worker_notes": notes[:4000],
            "session_cookies": cookies,
            "session_cookie_jar": snap.get("session_cookie_jar") or [],
            "session_headers": headers,
            "rounds_done": rounds,
            "source": "llm_interrupt",
            "original_summary": notes[:1000],
        }

    def _restore_interrupt_progress(self) -> None:
        ctx = self.deepen_context or {}
        if ctx.get("source") != "llm_interrupt" and not (
            ctx.get("worker_notes") or ctx.get("session_cookies") or ctx.get("session_headers")
        ):
            return
        notes = str(ctx.get("worker_notes") or "")
        cookies = ctx.get("session_cookies") if isinstance(ctx.get("session_cookies"), dict) else {}
        jar = ctx.get("session_cookie_jar") if isinstance(ctx.get("session_cookie_jar"), list) else []
        headers = ctx.get("session_headers") if isinstance(ctx.get("session_headers"), dict) else {}
        self.executor.restore_resume_state(
            worker_notes=notes,
            session_cookies=cookies,
            session_headers=headers,
            session_cookie_jar=jar,
        )
        if cookies or headers or jar:
            try:
                self._cookie_hub.ingest(self.executor, status="injected")
            except Exception:
                pass
        self._emit(
            "worker_resume",
            notes_len=len(notes),
            cookies=sorted(cookies.keys())[:20],
            headers=sorted(headers.keys())[:20],
            rounds_done=int(ctx.get("rounds_done") or 0),
        )

    def _llm_interrupt_result(
        self,
        *,
        rounds: int,
        error: str,
        failure_kind: str,
        retry_after: int,
    ) -> WorkerResult:
        resume = self._build_resume_context(rounds)
        self._emit(
            "llm_interrupt",
            round=rounds,
            failure_kind=failure_kind or "unknown",
            has_resume=bool(resume),
            findings=len(self.findings),
            error=error[:240],
        )
        return WorkerResult(
            target=self.target,
            verdict=Verdict.error,
            findings=self.findings,
            summary="LLM 调用失败，已保存进度供回队续挖。" if resume else "",
            rounds=rounds,
            error=error,
            failure_kind=failure_kind,
            retry_after_seconds=int(retry_after or 0),
            resume_context=resume,
        )

    def _deepen_brief(self) -> str:
        ctx = self.deepen_context or {}
        directive = ctx.get("directive", "").strip()
        original = ctx.get("original_title", "") or ctx.get("vuln_type", "")
        summary = (ctx.get("original_summary", "") or "").strip()
        if ctx.get("source") == "llm_interrupt":
            parts = [
                f"目标：{self.target}",
                "",
                "⚡ 这是一次【断点续挖】：上一轮 LLM 中断，会话态与工作笔记已恢复。",
            ]
            if summary:
                parts.append(f"已有进度摘要：{summary[:800]}")
            parts += [
                "",
                f"👉 继续任务：{directive or '从已有笔记与登录态接着打，不要重新泛扫。'}",
                "",
                "要求：直接接上进度验证/深挖；打穿就 submit_finding；确认无增量就 finish。",
            ]
            return "\n".join(parts)
        parts = [
            f"目标：{self.target}",
            "",
            "⚡ 这是一次【定向深挖任务】，不是普通自由挖掘。",
            f"上一轮在此目标发现了线索：{original}",
        ]
        if summary:
            parts.append(f"原始线索摘要：{summary[:800]}")
        parts += [
            "",
            "审核判定：线索真实有价值，但利用链没打穿，所以打回让你专门攻这一个点。",
            f"👉 你这一轮的唯一任务：{directive}",
            "",
            "要求：",
            "1. 直奔主题，优先把上面这条利用链打穿，不要重新从头泛泛侦察。",
            "2. 打穿了（取到真实数据/造成实锤危害）就用 submit_finding 提交完整利用链 + 原始请求响应证据。",
            "3. 反复尝试确实打不穿、证明只是理论可能，就 finish(verdict=no_vuln) 并说明卡在哪，绝不交半成品。",
        ]
        return "\n".join(parts)

    def _dispatch(self, name: str, args: dict, rnd: int) -> dict:
        # ===== 3.1：用户自定义拦截规则（allow/deny/ask）=====
        # 与 guard.py 的硬红线不冲突：硬红线在后，这里跑在前面。
        try:
            from app.tools import intercept as _ic
            _act, _pl = _ic.check(name, args or {})
            if _act == _ic.ACTION_DENY:
                self._emit("intercept_denied", tool=name, reason=(_pl or {}).get("reason", ""))
                return {
                    "ok": False, "blocked": True, "intercepted": True,
                    "error": f"[拦截] {(_pl or {}).get('reason', '被拦截规则拒绝')}",
                    "guidance": "该操作被任务规则禁止，换一个方向；不要重试同一调用。",
                }
            if _act == _ic.ACTION_ASK:
                pid = (_pl or {}).get("pending_id", "")
                self._emit("intercept_ask", tool=name, pending_id=pid,
                           reason=(_pl or {}).get("reason", ""))
                # 轮询人工裁决（最多等 60 秒，避免占死 worker 槽位）
                import time as _t
                deadline = _t.time() + 60
                while _t.time() < deadline:
                    st = _ic.get_decision(pid)
                    if st == "approved":
                        break
                    if st in ("denied", "expired"):
                        return {
                            "ok": False, "blocked": True, "intercepted": True,
                            "error": f"[人工{'拒绝' if st == 'denied' else '未响应'}] {(_pl or {}).get('reason', '')}",
                            "guidance": "人工未批准该操作。跳过它，继续其它方向。",
                        }
                    _t.sleep(1.5)
                else:
                    return {
                        "ok": False, "blocked": True, "intercepted": True, "pending_id": pid,
                        "error": f"[待人工确认] {(_pl or {}).get('reason', '')}",
                        "guidance": "该操作在等待人工确认（pending_id 已上报）。先做别的，稍后可重试。",
                    }
        except Exception:
            pass

        if name == "http_request":
            self._mark_tool_used(name, rnd)
            url = (args.get("url") or "").strip()
            if not url:
                return self._tool_arg_error(
                    "http_request", "url",
                    "必须传完整 URL。不要因为工具参数缺失中断任务；修正参数后只做一次高价值请求，"
                    "若没有明确攻击面就 finish(verdict=no_vuln)。",
                )
            self._emit("tool_http", round=rnd, url=url, method=args.get("method", "GET"))
            self._http_urls.append(url)
            if len(self._http_urls) > 80:
                self._http_urls = self._http_urls[-80:]
            self._maybe_enable_js_tool(url, "worker 主动请求 JS 资源")
            result = self.executor.http_request(
                url=url,
                method=args.get("method", "GET"),
                headers=args.get("headers"),
                data=args.get("data"),
                json_body=args.get("json_body"),
                files=args.get("files"),
                follow_redirects=args.get("follow_redirects", False),
                confirm_destructive=args.get("confirm_destructive", False),
                confirm_reason=args.get("confirm_reason") or "",
            )
            if not self._js_tool_enabled and isinstance(result, dict):
                headers = result.get("response_headers") if isinstance(result.get("response_headers"), dict) else {}
                probe_text = "\n".join([
                    url,
                    str(result.get("url") or ""),
                    str(headers.get("content-type") or headers.get("Content-Type") or ""),
                    str(result.get("body") or "")[:1400],
                ])
                if self._maybe_enable_js_tool(probe_text, "HTTP 响应出现 JS/SPA/前端接口信号"):
                    result["guidance"] = (
                        (result.get("guidance") or "")
                        + " 检测到 JS/SPA/前端接口信号；下一轮可使用 analyze_javascript 提取接口和密钥线索。"
                    ).strip()
            return result

        if name == "analyze_javascript":
            self._mark_tool_used(name, rnd)
            if not self._js_tool_enabled:
                return {
                    "ok": False,
                    "blocked": True,
                    "error": "JS 分析工具尚未开放：只有明确进入 JS/前端接口/密钥审计方向后才能调用。",
                    "guidance": "如果你确实要审计 JS，请先说明具体 JS 方向和原因；否则继续常规攻击面验证。",
                }
            url = (args.get("url") or "").strip()
            text = args.get("text") or ""
            self._emit("tool_js_analyze", round=rnd, url=url[:200], has_text=bool(text))
            return self.executor.analyze_javascript(
                url=url,
                text=text,
                max_depth=args.get("max_depth", 2),
                max_assets=args.get("max_assets", 80),
                deep=bool(args.get("deep")),
                deep_max_chunks=int(args.get("deep_max_chunks") or 200),
                browser=bool(args.get("browser")),
                browser_timeout=int(args.get("browser_timeout") or 90),
            )

        if name == "run_shell":
            self._mark_tool_used(name, rnd)
            command = (args.get("command") or args.get("cmd") or args.get("shell") or "").strip()
            if not command:
                return self._tool_arg_error(
                    "run_shell", "command",
                    "必须传要执行的命令字符串。不要重复空调用；若已经没有明确验证动作就 finish(verdict=no_vuln)。",
                )
            low_value = self._low_value_shell_reason(command, rnd)
            if low_value:
                # 记录完整命令（1000 字）而不是 200：截断后无法判断拦截是否误判，
                # 之前排查「姊妹域误拦」就因为只存了前 200 字，看不到命中的 host 而卡住。
                self._emit("tool_shell_blocked", round=rnd, command=command[:1000], reason=low_value)
                return {
                    "ok": False,
                    "blocked": True,
                    "error": low_value,
                    "guidance": (
                        "该动作会高概率造成低价值空转。请改为一个具体、可证明危害的最小验证请求；"
                        "如果没有这样的请求，立即调用 finish(verdict=no_vuln)。"
                    ),
                }
            self._emit("tool_shell", round=rnd, command=command[:200])
            return self.executor.run_shell(
                command,
                timeout=args.get("timeout"),
                confirm_destructive=args.get("confirm_destructive", False),
                confirm_reason=args.get("confirm_reason") or "",
            )

        if name == "decode_transform":
            self._mark_tool_used(name, rnd)
            value = args.get("value") or ""
            self._emit("tool_decode", round=rnd, mode=args.get("mode", "auto"), value_len=len(str(value)))
            return self.executor.decode_transform(value=value, mode=args.get("mode", "auto"))

        if name == "eval_javascript":
            self._mark_tool_used(name, rnd)
            code = args.get("code") or ""
            if not str(code).strip():
                return self._tool_arg_error("eval_javascript", "code", "必须传要执行的 JS，结果 console.log 出来。")
            self._emit("tool_eval_js", round=rnd, code_len=len(str(code)))
            return self.executor.eval_javascript(code=code, timeout=args.get("timeout", 8))

        if name == "suggest_waf_bypass":
            self._mark_tool_used(name, rnd)
            payload = args.get("payload") or ""
            if not payload:
                return self._tool_arg_error(
                    "suggest_waf_bypass", "payload",
                    "必须传被 WAF 拦截的最小 payload 或可控参数值；不要空调用。",
                )
            self._emit("tool_waf_advice", round=rnd, context=args.get("context", "generic"), payload_len=len(str(payload)))
            return self.executor.suggest_waf_bypass(
                payload=payload,
                status_code=args.get("status_code"),
                response_headers=args.get("response_headers"),
                response_body=args.get("response_body", ""),
                context=args.get("context", "generic"),
            )

        if name == "fofa_lookup":
            self._mark_tool_used(name, rnd)
            query = (args.get("query") or "").strip()
            if not query:
                return self._tool_arg_error(
                    "fofa_lookup", "query",
                    '必须传 FOFA 语法（如 ip="1.2.3.4"）；无明确测绘需求就别空调用。',
                )
            self._emit("tool_fofa_lookup", round=rnd, query=query[:120])
            return self.executor.fofa_lookup(query=query, size=args.get("size", 10))

        if name == "session_set":
            self._mark_tool_used(name, rnd)
            self._emit("tool_session_set", round=rnd,
                       has_cookies=bool(args.get("cookies")), has_headers=bool(args.get("headers")))
            return self.executor.session_set(
                cookies=args.get("cookies"),
                headers=args.get("headers"),
                clear=bool(args.get("clear", False)),
            )

        if name == "update_notes":
            self._mark_tool_used(name, rnd)
            return self.executor.update_notes(notes=args.get("notes", ""))

        if name == "kb_catalog":
            self._mark_tool_used(name, rnd)
            from app.kb import catalog as _kb_catalog
            cat = (args.get("category") or "").strip()
            self._emit("tool_kb", round=rnd, action="catalog", category=cat[:40])
            return _kb_catalog(category=cat)

        if name == "kb_lookup":
            self._mark_tool_used(name, rnd)
            from app.kb import lookup as _kb_lookup
            slug = (args.get("slug") or "").strip()
            if not slug:
                return self._tool_arg_error(
                    "kb_lookup", "slug",
                    "必须传 slug。先调 kb_catalog 拿可用 slug，不要凭猜测。",
                )
            self._emit("tool_kb", round=rnd, action="lookup", slug=slug[:60])
            return _kb_lookup(slug=slug, section=(args.get("section") or "").strip())

        if name == "kb_search":
            self._mark_tool_used(name, rnd)
            from app.kb import search as _kb_search
            kw = (args.get("keyword") or "").strip()
            if not kw:
                return self._tool_arg_error(
                    "kb_search", "keyword",
                    "必须传 keyword；没有明确要查的手法就别空调用。",
                )
            self._emit("tool_kb", round=rnd, action="search", keyword=kw[:60])
            return _kb_search(kw)

        if name == "rotate_proxy":
            self._mark_tool_used(name, rnd)
            reason = (args.get("reason") or "").strip()
            self._emit("tool_rotate_proxy", round=rnd, reason=reason[:200])
            result = self.executor.rotate_proxy_tool(reason=reason)
            if isinstance(result, dict):
                self._emit(
                    "proxy_rotated",
                    round=rnd,
                    proxy=str(result.get("proxy_label") or result.get("proxy") or ""),
                    remaining=result.get("remaining"),
                )
            return result

        if name == "report_intel":
            self._mark_tool_used(name, rnd)
            return self._report_intel(args)

        if name == "record_fact":
            self._mark_tool_used(name, rnd)
            return self._record_fact(args)

        if name == "report_coverage":
            self._mark_tool_used(name, rnd)
            return self._report_coverage(args)

        if name == "submit_finding":
            self._mark_tool_used(name, rnd)
            return self._submit_finding(args)

        if name == "check_duplicate_finding":
            self._mark_tool_used(name, rnd)
            return self._check_duplicate(args)

        if name == "finish":
            # 先做 verdict 自身的合法性校验，再判断 premature：
            # 否则 blocked 缺 unblock_condition 时会被 premature 分支抢先驳回，报错信息驴唇不对马嘴。
            _verdict = (args.get("verdict") or "no_vuln").strip().lower()
            _block_reason = (args.get("block_reason") or "").strip()
            _unblock = (args.get("unblock_condition") or "").strip()
            if _verdict == "blocked" and not _unblock:
                return {
                    "ok": False,
                    "kind": "blocked_needs_unblock_condition",
                    "error": "verdict=blocked 时必须填 unblock_condition。",
                    "guidance": (
                        "说清「满足什么条件就能继续挖」，例如：换未被封的出口 IP / 拿到有效会话 / 目标从 502 恢复。"
                        "如果写不出解锁条件，说明这不是受阻——用 no_vuln（真挖透了）或 inconclusive（判不出来）。"
                    ),
                }
            # inconclusive 是「做了但判不出来」，不是免检通道：至少要有实质动作才允许这么收尾，
            # 否则模型会用 inconclusive 绕过 premature 覆盖度检查。
            if _verdict == "inconclusive":
                _acts = sum(self._tool_counts.values())
                if _acts < 5 and not self.findings:
                    self._emit("finish_blocked", round=rnd, reason="inconclusive 动作过少")
                    return {
                        "ok": False,
                        "kind": "inconclusive_needs_work",
                        "error": f"判不出来也要先做够动作：当前仅 {_acts} 次工具调用。",
                        "guidance": (
                            "inconclusive 表示你确实测了但结论不明确。至少完成 JS 审计 + 2~3 个高价值接口实证，"
                            "再来收尾；如果连入口都没摸到，那是没挖而不是判不出来。"
                        ),
                    }

            premature = self._premature_finish_reason(args, rnd)
            if premature:
                self._emit("finish_blocked", round=rnd, reason=premature[:300])
                return {
                    "ok": False,
                    "kind": "premature_finish",
                    "error": premature,
                    "guidance": (
                        "继续补齐入口覆盖：读完 JS/API 线索，挑高价值接口做最小实证；"
                        "只有真不可达/纯静态/无交互，或线索已验证打不穿，才 finish(no_vuln)。"
                        "注意：被 WAF/验证码/限流挡住的现象不算「试不穿」，那应该用 blocked。"
                    ),
                }
            self._finished = {
                "verdict": _verdict,
                "summary": args.get("summary", ""),
                "deepen_lead": (args.get("deepen_lead") or "").strip(),
                "block_reason": _block_reason,
                "unblock_condition": _unblock,
            }
            self._report_provider_success()
            self._emit("worker_finish", verdict=self._finished["verdict"],
                       summary=self._finished["summary"][:300],
                       deepen_lead=self._finished["deepen_lead"][:300])
            return {"ok": True, "message": "已记录结束。"}

        return {"ok": False, "error": f"未知工具: {name}"}

    def _mark_tool_used(self, name: str, rnd: int) -> None:
        self._tool_counts[name] = self._tool_counts.get(name, 0) + 1
        if name == "analyze_javascript":
            self._last_js_analysis_round = rnd
            self._post_js_validation_count = 0
        elif name in {"http_request", "run_shell"} and self._last_js_analysis_round:
            self._post_js_validation_count += 1

    def _premature_finish_reason(self, args: dict, rnd: int) -> str:
        if (args.get("verdict") or "no_vuln") != "no_vuln" or self.findings:
            return ""
        if self.deepen_context:
            return ""
        exposed = self._untested_exposed_endpoint()
        if exposed:
            return (
                f"过早结束：搜集阶段已确认暴露端点 {exposed}，不能按纯前端静态站收尾。"
                "先 GET 该路径验证是否真实开放，再决定是否无洞。"
            )
        if self._js_signal_seen and not self._tool_counts.get("analyze_javascript"):
            return (
                f"过早结束：已出现 JS/API/前端接口信号，但第 {rnd} 轮仍未调用 analyze_javascript。"
                "先抓取/审计关联 JS，提取接口、路由、secret/token/sign，再决定是否无洞。"
            )
        if self._last_js_analysis_round and self._post_js_validation_count == 0:
            return (
                "过早结束：已经分析 JS，但还没有对 JS 提取出的高价值接口/链路做 http_request/run_shell 实证。"
                "至少挑登录/找回/导出/用户/管理/上传/配置等高价值端点验证一次。"
            )
        tool_actions = sum(self._tool_counts.values())
        if (rnd < 12 or tool_actions < 8) and not self._quick_no_vuln_allowed(args):
            return (
                f"过早结束：仅 {rnd} 轮、{tool_actions} 次工具动作，不足以确认有攻击面的站点无洞。"
                "除非已明确证明目标不可达，或纯静态且无登录/表单/API/JS/可控参数，否则继续覆盖首页、登录/API/JS/高价值端点。"
            )
        return ""

    @staticmethod
    def _quick_no_vuln_allowed(args: dict) -> bool:
        text = "\n".join([
            str(args.get("summary") or ""),
            str(args.get("deepen_lead") or ""),
        ]).lower()
        unreachable = (
            "不可达", "连不上", "连接失败", "拒连", "超时", "timeout",
            "connection refused", "could not resolve", "dns", "下线",
        )
        static_or_empty = (
            "纯静态", "静态页", "空壳", "无交互", "无攻击面",
        )
        no_surface = (
            "无登录", "无表单", "无api", "无 api", "无js", "无 js",
            "无可控参数", "没有登录", "没有表单", "没有api", "没有 api",
        )
        return any(x in text for x in unreachable) or (
            any(x in text for x in static_or_empty) and any(x in text for x in no_surface)
        )

    def _exposed_endpoint_hints(self) -> list[str]:
        text = "\n".join([
            str((self.target_meta or {}).get("priority_reason") or ""),
            str((self.target_meta or {}).get("playbook_block") or ""),
            " ".join((self.target_meta or {}).get("playbook_route", {}).get("tags") or [])
            if isinstance((self.target_meta or {}).get("playbook_route"), dict) else "",
            self.target or "",
        ])
        found = re.findall(
            r"(/druid(?:/index\.html)?|/actuator(?:/[a-z0-9._-]+)?|/nacos/?)",
            text,
            re.I,
        )
        out: list[str] = []
        for item in found:
            low = item.lower()
            if low not in out:
                out.append(low)
        return out

    def _untested_exposed_endpoint(self) -> str:
        hints = self._exposed_endpoint_hints()
        if not hints:
            return ""
        hit = " ".join(self._http_urls).lower()
        for ep in hints:
            token = ep.rstrip("/").split("/")[-1]
            if token and token in hit:
                continue
            if ep in hit:
                continue
            return ep
        return ""

    def _maybe_enable_js_tool(self, text: str, reason: str) -> bool:
        if self._js_tool_enabled:
            return False
        if not _JS_INTENT_RE.search(text or ""):
            return False
        self._js_tool_enabled = True
        self._js_signal_seen = True
        self._emit("js_analyzer_enabled", reason=reason)
        return True

    @staticmethod
    def _tool_arg_error(tool: str, missing: str, guidance: str) -> dict:
        return {
            "ok": False,
            "kind": "arg_error",
            "error": f"{tool} 工具参数缺失：{missing}",
            "guidance": guidance,
        }

    def _recovery_hint(self, tool: str, result: dict) -> str:
        """工具失败时返回针对性恢复提示，帮模型在同流里快速纠偏而非从头推理。

        只在 result 不含 guidance 时才会被采用（调用方用 setdefault）。
        针对 http_request 的各类状态码、run_shell 的各类失败、以及通用错误分别给提示。
        """
        if result.get("ok") is True or result.get("guidance"):
            return ""
        if tool == "http_request":
            sc = result.get("status_code")
            err = str(result.get("error", ""))
            if sc == 401:
                return "401 未授权：需要登录态。若已 session_set 过，可能 session 过期了——重新登录或换凭证；若本就是测未授权，401 说明接口有鉴权，换个不需要登录的入口或测越权。"
            if sc == 403:
                return "403 禁止：常见原因——路径不对(试目录爆破/换路径)、需要特定角色/IP、WAF 拦截(看响应体有无 WAF 特征，用 suggest_waf_bypass)、或缺少 CSRF token。若判断是 WAF 封当前出口（整站持续拦截页、换路径和 payload 都无效）再调 rotate_proxy 后重试。普通 Forbidden 不要换 IP。"
            if sc == 404:
                return "404 不存在：路径不对。从 JS/首页/接口文档里重新找正确路径，或试常见变体(/api/v1/、/api/v2/、大小写、尾斜杠)。"
            if sc in (500, 502, 503):
                return f"{sc} 服务端错误：可能是 payload 触发了异常(注入/RCE 线索)或服务临时不可用。保留这个请求作为证据，换参数复现确认；若多次稳定 500 可作为注入/异常漏洞线索。"
            if sc == 302:
                loc = (result.get("response_headers", {}) or {}).get("Location", "")
                return f"302 跳转到 {loc[:120]}：若是跳登录页说明需要登录态；若是跳 ticket/SSO 链，设 follow_redirects=true 跟完整个登录链。"
            if "timed out" in err.lower() or "timeout" in err.lower():
                return "请求超时：目标可能慢或不可达。换更小范围的请求、加大 timeout、或确认目标是否在线；连续超时就 finish。"
            if "connection" in err.lower() or "refused" in err.lower() or "unreachable" in err.lower() or "reset" in err.lower():
                return "连接失败：常见是网关按扫描器 UA 掐 TCP，不是 WAF 拦截页。http_request 已默认 Chrome UA；若用 run_shell 的 httpx/curl，加浏览器 UA 再试一次。没有拦截页就不要 suggest_waf_bypass。仍不通再 finish。"
        if tool == "run_shell":
            rc = result.get("return_code")
            if rc and rc != 0:
                return f"命令退出码 {rc}：检查命令语法/参数/路径是否正确。换最小命令验证环境，别重复跑同一条失败的命令。"
            if result.get("timed_out"):
                return "命令超时：可能命令本身耗时(如 nmap 全端口)或挂起。换更小范围或加 timeout 参数；别重复跑超时命令。"
            if result.get("blocked"):
                return ""  # blocked 已有自己的 guidance
        if "参数" in str(result.get("error", "")) or "JSON" in str(result.get("error", "")):
            return "参数格式错误：检查工具参数是否合法 JSON、必填字段是否齐全。对照工具 schema 修正后重试一次。"
        return ""

    def _auto_finish(self, reason: str, failure_kind: str = "") -> None:
        if failure_kind:
            self._finished = {
                "verdict": "error",
                "summary": reason,
                "error": reason,
                "failure_kind": failure_kind,
            }
            self._report_provider_failure(reason, failure_kind)
            self._emit(
                "worker_auto_finish",
                verdict="error",
                failure_kind=failure_kind,
                summary=reason[:300],
                error=reason[:500],
                error_copy=reason,
            )
            return
        verdict = "found" if self.findings else "no_vuln"
        self._finished = {"verdict": verdict, "summary": reason}
        self._emit("worker_auto_finish", verdict=verdict, summary=reason[:300])

    def _report_provider_failure(self, reason: str, failure_kind: str) -> None:
        if failure_kind not in {"model_behavior", "tool_argument"}:
            return
        reporter = getattr(self.llm, "report_current_provider_failure", None)
        if not reporter:
            return
        try:
            reporter(reason, kind=failure_kind)
        except Exception as exc:
            self._emit("provider_degrade_error", error=str(exc), failure_kind=failure_kind)

    def _report_provider_success(self) -> None:
        reporter = getattr(self.llm, "report_current_provider_success", None)
        if not reporter:
            return
        try:
            reporter()
        except Exception as exc:
            self._emit("provider_health_error", error=str(exc))

    @staticmethod
    def _tool_outcome(result: dict) -> str:
        if result.get("ok") is True:
            return "ok"
        if result.get("kind") == "needs_more_evidence":
            return "ok"
        if result.get("blocked"):
            return "blocked"
        if result.get("kind") == "arg_error" or "工具参数缺失" in str(result.get("error", "")):
            return "arg_error"
        if result.get("timed_out"):
            return "timeout"
        if result.get("cancelled"):
            return "timeout"
        text = (str(result.get("error", "")) + "\n" + str(result.get("output", ""))).lower()
        if any(marker in text for marker in ("timed out", "timeout", "超时")):
            return "timeout"
        if any(marker in text for marker in (
            "connection refused", "connection reset", "connection timed out",
            "network is unreachable", "no route to host", "name or service not known",
            "temporary failure", "http 请求异常",
        )):
            return "network"
        return "error"

    def _low_value_shell_reason(self, command: str, rnd: int) -> str:
        cmd = command.strip()
        lower = cmd.lower()
        target_host = urlparse(self.target if "://" in self.target else f"http://{self.target}").netloc.lower()

        sleep_values = [int(m.group(1)) for m in _SLEEP_RE.finditer(lower)]
        if sleep_values and max(sleep_values) >= 30:
            return "禁止长 sleep/等待式探测：这会占住 worker 且不产生漏洞证据。"

        if _BROAD_NMAP_RE.search(lower):
            return "禁止宽端口 nmap 扫描：请只验证当前 Web 服务相关端口或直接收尾。"

        # 「只查工具在不在」的统一判定，必须定义在所有工具泛扫规则之前。
        # 曾经定义在 sqlmap 那行旁边，但 nuclei 规则在它前面引用 → UnboundLocalError，
        # 直接让整个 worker 崩溃。这类顺序错误编译期查不出来，只能靠真实调用测。
        _probes_only = bool(re.search(
            r"\b(which|command\s+-v|type|hash)\s+[^\n;&|]*$",
            lower.strip().split("\n")[-1],
        ))

        # 只拦「真的在跑 nuclei 泛扫」。which/command -v 只是查工具在不在，不算执行。
        if "nuclei" in lower and " -t " not in lower and " -tags " not in lower and " -id " not in lower and not _probes_only:
            runs_nuclei = bool(re.search(r"(^|[;&|]\s*|\btimeout\s+\d+\s+)nuclei\b", lower)) or "nuclei -" in lower
            if runs_nuclei:
                return "禁止无模板/无 tag 的 nuclei 泛扫：先用接口/JS/逻辑分析形成假设，再用具体模板或最小请求验证。"

        # 实测 `which nmap nuclei httpx whatweb sqlmap` 这种探测命令被 sqlmap/nuclei
        # 两条规则各拦一次——命令本身连扫描动作都没有，纯属误伤。
        if "sqlmap" in lower and not _probes_only and not any(marker in lower for marker in ("?", "--data", " -r ", "--cookie", "--headers")):
            return "禁止无具体参数/请求包的 sqlmap 泛扫：必须先定位可控参数或原始请求，再做针对性注入验证。"

        if re.search(r"\b(ffuf|gobuster|dirsearch|feroxbuster)\b", lower):
            if not any(marker in lower for marker in ("api", "swagger", "actuator", "druid", "nacos", "upload", "login")):
                return "禁止泛目录爆破：优先测试已发现的接口、登录/改密/上传/越权逻辑；目录扫描只能针对高价值路径簇。"

        if "socket.socket" in lower and rnd >= 6:
            return "禁止在中后期用 raw socket 死磕协议异常：网络/协议不可达应收敛为 no_vuln。"

        # /dev/tcp 探端口：判定「低价值端口枚殂」，但少量、且针对已知服务的定向探测要放行。
        # 实测 worker 探 mail.shupl.edu.cn 的 25/465/587/993（邮件协议）共 7 个端口被拦——
        # 这是邮件系统 SRC 的合理侦察，不是泛扫。阈值放到 12 个，且探测的是同站主机才管。
        if "/dev/tcp/" in lower and "for port in" in lower and rnd >= 8:
            m_ports = re.search(r"for\s+port\s+in\s+([^;\n]+)", lower)
            ports = [x for x in re.split(r"\s+", m_ports.group(1).strip()) if x] if m_ports else []
            if len(ports) > 12:
                return "禁止中后期用 /dev/tcp 大面积循环探端口：这属于低价值端口枚举，应聚焦当前 Web 入口。"

        if "curl" in lower and "for " in lower:
            match = _FOR_LIST_RE.search(cmd)
            if match:
                items = [x for x in re.split(r"\s+", match.group(1).strip()) if x]
                # 只把「路径/子域枚举」当低价值。循环项是注入 payload（带引号/运算符/
                # s#elect 等）时属于参数验证，不是枚举——实测 SQLi 的
                # `for p in "020300' AND '1'='1" ...` 被误判成"大列表路径枚举"挡掉了。
                looks_like_payload = any(
                    _PAYLOAD_HINT.search(x) for x in items[:20]
                )
                # 接口路径枚举（/api/vX、swagger、api-docs、doc.html 等）是高价值侦察：
                # 这是 SRC 里找未授权接口的主要手段，不是低价值目录爆破。
                # 实测 worker 枚举 20 个 /api/v1/... 含 swagger-resources/api-docs/doc.html
                # 被这条规则挡掉，恰好挡掉了最该做的事。
                high_value_api = sum(
                    1 for x in items
                    if _API_PATH_HINT.search(x)
                ) >= max(3, len(items) // 2)
                if len(items) > 10 and rnd >= 8 and not looks_like_payload and not high_value_api:
                    return "禁止中后期大列表路径/子域枚举：请聚焦已确认入口，或无洞收尾。"

        # 注意：这里必须是 [^/\s"'] 而不是 [^/\\s"']。
        # raw string 里 "\\s" 是「字面反斜杠 + 字母 s」，会被当成排除字符集里的成员，
        # 导致 $sub.other.edu.cn 这种含字母 s 的 host 被截断成 "$"，所有 host 提取全失效。
        # 这个 bug 让「跨校探测」判定一直漏判（历史遗留，不是本次引入）。
        url_hosts = re.findall(r"https?://([^/\s\"']+)", lower)

        def _same_site(h: str) -> bool:
            """h 是否属于当前目标的同一站点（含同注册域的子域）。

            一个学校/企业常有多个子域（employ./rsres./auth. 等同属 shupl.edu.cn），
            它们共享同一攻击面，属于同一 target 该打的资产。按字面 host 严格比对会把
            这些真实横向资产判成「偏离目标」——实测 rsres.shupl.edu.cn、
            employ.shupl.edu.cn 都被拦过，正是 SRC 最需要的同级横向突破。
            """
            if not h or not target_host:
                return True
            if h == target_host:
                return True
            try:
                from app.agents.target_cluster import root_domain
                rh, rt = root_domain(h), root_domain(target_host)
                return bool(rh) and rh == rt
            except Exception:
                return False

        if rnd >= 6 and target_host:
            off_site = [h for h in url_hosts if h.endswith(".edu.cn") and not _same_site(h)]
            if off_site:
                return "禁止中后期离开当前站点请求其它单位域名：本 worker 只负责当前 target。"

        # 只针对「批量探测**其它** Edu 子域」。曾经只要命令里同时出现 .edu.cn / curl / for
        # 就拦，结果把「遍历当前站点自己的接口」也挡掉了：实测 worker 用 for 循环 + curl
        # 带 Cookie 验证同站登录态被误拦 6 次，导致凭据类漏洞拼不出 PoC、复现验证输出为空、
        # 高危被误降级成 deepen。
        #
        # 二次修正：不再用「for + curl + 出现 edu.cn」这种字符组合猜意图。Worker 会把
        # 127.0.0.1 拆成 A/B/C/D 拼回来绕检测，说明按字面匹配只会逼模型做变形，不能真正
        # 约束行为。改为只看**确凿的跨目标迹象**：
        #   ① 命令里出现了另一个 edu.cn 主机（非当前目标）
        #   ② 明确写了子域枚举循环变量（for sub in / for host in）
        # 同站遍历（含指向自己的 IP/域名变形）一律放行。
        if rnd >= 10 and "curl" in lower and "for " in lower:
            other_edu = [h for h in url_hosts if h.endswith(".edu.cn") and not _same_site(h)]
            has_enum_loop = any(m in lower for m in ("for sub in", "for host in"))
            if other_edu or has_enum_loop:
                return "禁止偏离当前站点批量探测其它单位域名：本 worker 只负责当前 target。"

        return ""

    def _candidate_pool(self) -> list[dict]:
        pool = list(self.duplicate_history)
        for f in self.findings:
            pool.append(f.model_dump(mode="json"))
        return pool

    def _dup_matches(self, candidate: dict) -> tuple[bool, list[dict]]:
        return dedup.is_duplicate(candidate, self._candidate_pool(), target_ref=self.target)

    def _check_duplicate(self, args: dict) -> dict:
        duplicate, matches = self._dup_matches(args)
        self._emit("duplicate_checked", duplicate=duplicate, matches=len(matches),
                   title=(args.get("title") or "")[:120])
        return {
            "ok": True,
            "duplicate": duplicate,
            "matches": matches,
            "guidance": (
                "这是重复/已驳回/通杀库已覆盖的漏洞，不要 submit_finding；继续挖其它入口或 finish。"
                if duplicate else
                "未发现明显重复；若已取得真实证据，可继续 submit_finding。"
            ),
        }

    def _report_intel(self, args: dict) -> dict:
        """worker 主动上报可复用情报（纯内存收集，编排层 async 统一落全局情报库）。

        kind: cred / endpoint / profile / fact（fingerprint 由系统自动识别，不让 worker 报）
        - cred:     {username, password}  —— 仅上报【验证过能登录】的凭证
        - endpoint: {path, vuln_type}     —— 验证有效的未授权/敏感端点
        - profile:  {key, value}          —— 技术栈/WAF/突破口等画像
        - fact:     {scope, polarity, detail, evidence} —— 探索事实/结论，**含否定结论**
                     polarity=positive(证实有什么) / negative(试过没有/不可利用)
        fact 走独立工具 record_fact，这里只保留其余三类以维持旧调用兼容。
        """
        kind = (args.get("kind") or "").strip().lower()
        if kind not in ("cred", "endpoint", "profile"):
            if kind == "fact":
                return {"ok": False, "error": "记录探索事实请用 record_fact 工具，不要用 report_intel。"}
            return {"ok": False, "error": "kind 必须是 cred/endpoint/profile 之一。"}
        payload = args.get("payload")
        if not isinstance(payload, dict) or not payload:
            return {"ok": False, "error": "payload 必须是非空对象，按 kind 提供对应字段。"}
        if len(self._reported_intel) >= 20:
            return {"ok": True, "message": "本轮情报已上报足够，无需再报。"}
        def _safe_text(value: Any, limit: int) -> str:
            if isinstance(value, (dict, list)):
                try:
                    text = json.dumps(value, ensure_ascii=False)
                except Exception:
                    text = str(value)
            else:
                text = str(value or "")
            return text[:limit]

        item = {
            "kind": kind,
            "payload": {str(k)[:50]: _safe_text(v, 300) for k, v in payload.items() if v not in (None, "")},
            "summary": _safe_text(args.get("summary"), 300),
            "confidence": "verified" if args.get("verified") else "likely",
        }
        if not item["payload"]:
            return {"ok": False, "error": "payload 内容为空。"}
        self._reported_intel.append(item)
        self._emit("intel_reported", intel_kind=kind)
        return {"ok": True, "message": "情报已记录，将沉淀到全局情报库供后续 worker 复用。继续挖洞或 finish。"}

    def _record_fact(self, args: dict) -> dict:
        """记录一条探索事实/结论（含否定结论），沉淀到全局情报库。

        设计移植自 ARTEX 的 record_fact：与 report_intel 的区别是——
        report_intel 只收「可复用情报」（凭证/端点/画像），本工具收「观察结论」，
        明确允许「端口关闭」「参数不可注入」「未发现登录入口」这类否定结论。
        目的是让后续派到同域的 worker 知道哪些方向已被试过，不必从零重试。
        """
        if len(self._reported_intel) >= 20:
            return {"ok": True, "message": "本轮已记录足够多的事实/情报，无需再记。"}
        scope = str(args.get("scope") or "").strip()
        detail = str(args.get("detail") or "").strip()
        evidence = str(args.get("evidence") or "").strip()
        polarity = str(args.get("polarity") or "positive").strip().lower()
        confidence = str(args.get("confidence") or "inferred").strip().lower()

        if polarity not in ("positive", "negative"):
            return {"ok": False, "error": "polarity 只能是 positive（证实有）或 negative（试过没有）。"}
        if confidence not in ("observed", "inferred"):
            return {"ok": False, "error": "confidence 只能是 observed（输出里直接看到）或 inferred（据现象推断）。"}
        if not scope or len(scope) < 3:
            return {"ok": False, "error": "scope 必填：说清是这个结论属于哪个攻击面（哪个参数/哪个端口/哪个入口）。"}
        if not detail or len(detail) < 6:
            return {"ok": False, "error": "detail 必填：写清结论本身，太短没有复用价值。"}
        if not evidence:
            return {"ok": False, "error": "evidence 必填：贴出你实际看到的那一行输出，没有证据的事实会污染情报库。"}

        item = {
            "kind": "fact",
            "payload": {
                "scope": scope[:200],
                "polarity": polarity,
                "detail": detail[:500],
                "evidence": evidence[:400],
            },
            "summary": f"{scope}：{detail}"[:300],
            # observed/inferred 直接映射到情报库的 confidence 语义
            "confidence": "observed" if confidence == "observed" else "inferred",
        }
        self._reported_intel.append(item)
        self._emit("intel_reported", intel_kind="fact")
        kind_cn = "否定结论" if polarity == "negative" else "正向事实"
        return {
            "ok": True,
            "message": f"已记录一条{kind_cn}（{confidence}）。同域后续 worker 会看到它。继续挖或 finish。",
        }

    def _report_coverage(self, args: dict) -> dict:
        """单站协作覆盖记录：记录已验证 API/入口，供后续 worker 复用。"""
        if len(self._reported_coverage) >= 12:
            return {"ok": True, "message": "本轮覆盖记录已足够，收尾时汇总即可。"}

        def _safe_text(value: Any, limit: int) -> str:
            if isinstance(value, (dict, list)):
                try:
                    text = json.dumps(value, ensure_ascii=False)
                except Exception:
                    text = str(value)
            else:
                text = str(value or "")
            return text[:limit]

        route = (args.get("route") or "").strip()
        if not route:
            route = str((self.target_meta.get("site_collab_route") or {}).get("source") or "")
        summary = _safe_text(args.get("summary"), 400).strip()
        if not summary:
            return {"ok": False, "error": "summary 不能为空：请概括已覆盖的 API/入口和结论。"}
        endpoints_in = args.get("endpoints") or []
        endpoints: list[dict] = []
        if isinstance(endpoints_in, list):
            for item in endpoints_in[:20]:
                if not isinstance(item, dict):
                    continue
                endpoints.append({
                    "method": _safe_text(item.get("method") or "GET", 12).upper(),
                    "path": _safe_text(item.get("path") or item.get("url"), 220),
                    "status": _safe_text(item.get("status"), 40),
                    "checks": _safe_text(item.get("checks"), 120),
                    "result": _safe_text(item.get("result") or item.get("note"), 180),
                })
        record = {
            "route": route or "site",
            "summary": summary,
            "endpoints": endpoints,
            "remaining": _safe_text(args.get("remaining"), 400),
        }
        self._reported_coverage.append(record)
        self._emit("coverage_reported", route=record["route"], summary=summary[:180], endpoints=len(endpoints))
        return {"ok": True, "message": "覆盖记录已记下，后续同站 worker 会看到摘要。继续补盲区或 finish。"}

    def _vuln_class_of(self, finding: Finding) -> str:
        """取该漏洞的语义大类，用于同类产量熔断。

        必须走 semantic_class（关键词子串匹配），不能用 normalize_vuln_type：
        后者是精确匹配，LLM 只要多写一句话就变新桶。实测 155 条真实数据里
        「越权访问/功能级授权失效 (BFLA)」这类长描述各自成桶（10+ 个），
        「弱口令导致后台管理员接管 + 客户PII泄露」也自成一桶，熔断完全不生效。
        关键词匹配能把它们都收进 idor / weak_cred / auth_bypass。

        title 与 vuln_type 一起喂进去，命中率更高（标题常带"SQL注入""弱口令"等）。
        """
        from app.cluster import semantic_class
        try:
            sem = semantic_class(finding.title or "", finding.vuln_type or "")
        except Exception:
            sem = ""
        if sem and sem != "other":
            return sem
        # 语义没命中时再退回精确归一，至少同写法还能相等比较
        return dedup.normalize_vuln_type(finding.vuln_type or "") or "other"

    def _report_deepen_suggestion(self, finding: Finding, cls: str, hits: int) -> None:
        """把「该类已够量、建议人工深挖」标记到 finding 的 evidence 上，供 UI 渲染深挖按钮。"""
        try:
            ev = dict(finding.evidence or {})
            ev["deepen_suggested"] = True
            ev["deepen_reason"] = (
                f"同类（{cls}）已命中 {hits} 条，已停止继续枚举；"
                "如需扩大战果可点「深挖」派生定向 worker。"
            )
            ev["deepen_class"] = cls
            ev["deepen_hits"] = hits
            finding.evidence = ev
        except Exception:
            pass
        self._emit("deepen_suggested", title=finding.title, vuln_class=cls, hits=hits)

    def _submit_finding(self, args: dict) -> dict:
        """Pydantic 兜底校验（双保险），失败返回错误让模型修正。"""
        try:
            finding = Finding(**args)
        except ValidationError as e:
            self._emit("finding_invalid", errors=str(e))
            return {"ok": False, "error": f"Finding 校验失败，请修正后重新提交: {e}"}

        if not self._enterprise:
            bomb_block = edu_bombing_block_reason(finding)
            if bomb_block:
                self._emit("finding_out_of_scope", title=finding.title, reason=bomb_block[:200])
                return {
                    "ok": False,
                    "kind": "out_of_scope",
                    "submitted": False,
                    "error": bomb_block,
                }

        backdoor_block = weak_backdoor_block_reason(finding)
        if backdoor_block:
            self._emit("finding_out_of_scope", title=finding.title, reason=backdoor_block[:200])
            return {
                "ok": False,
                "kind": "out_of_scope",
                "submitted": False,
                "error": backdoor_block,
            }

        evidence_block = self._weak_write_evidence_reason(finding)
        if evidence_block:
            self._emit("finding_needs_more_evidence", title=finding.title, reason=evidence_block[:200])
            return {
                "ok": False,
                "kind": "needs_more_evidence",
                "submitted": False,
                "error": evidence_block,
                "guidance": (
                    "不要把这条半成品提交给 reviewer。" + HARMLESS_PROTOCOL
                ),
            }

        duplicate, matches = self._dup_matches(finding.model_dump(mode="json"))
        if duplicate:
            self._emit("finding_duplicate", title=finding.title, matches=len(matches))
            return {
                "ok": False,
                "duplicate": True,
                "matches": matches,
                "error": "该漏洞命中统一查重库（历史提交/已驳回/通杀明细），已拦截。不要再次提交同一漏洞，继续挖其它点或 finish。",
            }

        self.findings.append(finding)
        # 携带完整 finding 供 orchestrator 实时落库（进程被打断时不丢洞）。
        self._emit(
            "finding_submitted",
            title=finding.title,
            severity=finding.severity_claimed.value,
            vuln_type=finding.vuln_type,
            finding=finding.model_dump(mode="json"),
        )

        # 同类产量熔断：命中 quota 后不再继续枚举同类接口，只写报告 + 标记可深挖。
        # 这样 worker 把剩余轮次让给别的漏洞类型，而不是在同一类上刷变体烧 token。
        cls = self._vuln_class_of(finding)
        self._class_hits[cls] = self._class_hits.get(cls, 0) + 1
        hits = self._class_hits[cls]
        if hits >= VULN_CLASS_QUOTA:
            self._report_deepen_suggestion(finding, cls, hits)
            already = cls in self._class_capped
            self._class_capped.add(cls)
            if not already:
                self._emit("vuln_class_capped", vuln_class=cls, hits=hits, quota=VULN_CLASS_QUOTA)
            return {
                "ok": True,
                "message": (
                    f"已收录漏洞「{finding.title}」（{finding.severity_claimed.value}）。"
                    f"【产量已达上限】同类（{cls}）已命中 {hits} 条，禁止继续枚举同一类接口/参数；"
                    "本条已标记为「可深挖」，人工可点深挖派生定向 worker。"
                    "请把剩余轮次用于其它漏洞类型；没有其它方向就直接 finish。"
                ),
                "vuln_class": cls,
                "class_hits": hits,
                "class_capped": True,
                "deepen_suggested": True,
            }

        return {
            "ok": True,
            "message": (
                f"已收录漏洞「{finding.title}」（{finding.severity_claimed.value}）。"
                f"同类（{cls}）已累计 {hits}/{VULN_CLASS_QUOTA} 条，"
                "再命中同类即触发产量上限，请优先换其它漏洞类型。"
            ),
            "vuln_class": cls,
            "class_hits": hits,
        }

    def _weak_write_evidence_reason(self, finding: Finding) -> str:
        """拦截 EduSRC 最常见半成品：写接口返回成功但影响 0 行。

        无害证法（哨兵闭环 / 鉴权对照 / 幂等回写 / 旁路回读）放行；
        只拦「成功文案 + 零影响」且没有任何无害证据的半成品。
        """
        if self._enterprise:
            return ""
        return weak_write_block_reason(finding)
