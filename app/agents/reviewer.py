"""Reviewer Agent：极理性审核 + EduSRC 评级 + 垃圾洞过滤。

输入：worker 提交的 Finding（独立审核，不看 worker 挖掘过程）。
流程（对应设计文档 §7）：
  阶段① 规则匹配（快速过滤明显忽略项）— 由 LLM 在提示词内完成
  阶段② 证据链审查（LLM 核心）
  阶段③ 复现验证（仅当评定为 严重/高危 时触发，重新发包）
输出：Review 结论。
"""
from __future__ import annotations

import json
import threading
from typing import Any, Callable, Optional

from pydantic import ValidationError

from app.agents.backdoor_proof import WEAK_BACKDOOR_REASON, looks_like_weak_backdoor
from app.agents.edu_scope import BOMBING_BLOCK_REASON, looks_like_edu_bombing
from app.agents.prompts import normalize_src_type, reviewer_system_prompt
from app.agents.write_proof import (
    HARMLESS_PROTOCOL,
    STRONG_KINDS,
    classify_write_proof,
    has_strong_write_proof,
    should_skip_live_replay,
)
from app.llm.client import LLMClient, LLMError, _is_forced_tool_choice_unsupported
from app.schemas import Confidence, Finding, Review, ReviewVerdict, Severity
from app.tools.executor import ToolExecutor
from app.tools.schemas import REVIEWER_TOOL_SCHEMAS
# CVSS 3.1 基础分：按 NVD 官方公式计算，让定级从「模型主观打分」变成「可复算」
from app.tools.cvss31 import (
    base_score as cvss_base_score,
    metrics_from_args as cvss_from_args,
    nvd_reject_reason,
)

# 触发复现验证的等级
_HIGH_VALUE = {Severity.critical, Severity.high}

# 同一漏洞被「未证实」打回的次数上限。到达后强制归档进「AI 未采纳」并标注，
# 不再无限重审——实测同一个 SQL 注入被反复打回 4 次，每次都是 deepen/uncertain，
# 既进不了复审也进不了未采纳，等于原地空转（用户视角就是"被吞了"）。
UNCERTAIN_ATTEMPT_CAP = 2
_REVIEW_TEXT_LIMITS = {
    "description": 1800,
    "poc": 1800,
    "raw_request": 1800,
    "raw_response": 3200,
    "affected_scope": 1000,
    "owner": 500,
}


def _classify_replay_run(result: dict, output: str) -> tuple[str, str]:
    """判断复现命令到底「跑了没有」。

    返回 (kind, why)：
      kind="not_run"  命令没真正执行成功（被拦/超时/工具缺失/环境不可用）
      kind="ran"      命令执行了，输出可以交给 LLM 判断漏洞是否复现

    为什么需要这一步：原实现直接把 output 塞给 LLM，命令没跑成时 output 是空的，
    LLM 只能回 NO，高危洞被误降成 deepen。实测凭据类漏洞就因此丢过。
    「没跑成」和「跑了但没复现」是两件事，前者不该算证据不足。
    """
    if not isinstance(result, dict):
        return "not_run", "执行器未返回结果"

    if result.get("blocked"):
        return "not_run", "命令被安全策略拦截"

    if result.get("timed_out"):
        return "not_run", "执行超时"

    if result.get("cancelled"):
        return "not_run", "执行被取消"

    err = str(result.get("error") or "").strip()
    if err and not result.get("ok"):
        return "not_run", f"执行异常: {err[:80]}"

    rc = result.get("return_code")
    text = str(output or "").strip()

    # 命令替换失败 / 命令不存在的典型信号：这类是环境问题，不是漏洞结论
    _MISSING = ("command not found", "not found", "No such file", "cannot find",
                "Permission denied", "Network is unreachable", "Could not resolve",
                "Temporary failure in name resolution", "Connection refused")
    # shell 语法错误：PoC 本身写坏了，命令根本没跑起来。
    # 原实现把这类输出交给 LLM 判 NO，导致「高危→deepen」误降级（实测 19 条）。
    _SYNTAX = ("syntax error", "unexpected eof", "unexpected token",
               "unterminated", "command substitution", "bad substitution",
               "unexpected newline", "syntax error near")
    if not text:
        if rc not in (0, None):
            return "not_run", f"无输出且退出码 {rc}"
        return "not_run", "命令无任何输出"

    low = text.lower()
    if any(s in low for s in _SYNTAX):
        return "not_run", f"PoC 语法错误（命令未执行）: {text[:60]}"

    if rc not in (0, None) and len(text) < 120 and any(m.lower() in low for m in _MISSING):
        return "not_run", f"环境错误: {text[:60]}"

    return "ran", ""


_REVIEW_STATIC_PREFIX = (
    "下一条是 Finding JSON。只按真实请求/响应/PoC/证据/自检审核；证据不足但可打穿则 deepen，垃圾 ignored。"
)

_REVIEW_NEVER_DEEPEN_MARKERS = (
    "反射型xss", "反射 xss", "self-xss", "self xss", "用户名枚举",
    "phpinfo", "拒绝服务", "dos",
    "短信轰炸", "邮箱轰炸", "邮件轰炸", "验证码轰炸", "sms bomb", "email bomb",
    "非教育", "不在范围", "钓鱼", "中间人", "mitm", "本就公开", "公开展示", "公开接口",
)
_REVIEW_CAPTCHA_ONLY_IGNORE_MARKERS = ("图形验证码", "算术验证码")


def _review_text(finding: Finding, review: Review) -> str:
    parts: list[str] = [
        finding.vuln_type,
        finding.title,
        finding.target_url,
        finding.description,
        finding.poc,
        finding.raw_request,
        finding.raw_response,
        finding.affected_scope,
        json.dumps(finding.evidence.model_dump(mode="json"), ensure_ascii=False),
        json.dumps([s.model_dump(mode="json") for s in finding.kill_chain], ensure_ascii=False),
        " ".join(review.ignore_reasons or []),
        " ".join(review.downgrade_reasons or []),
        review.reviewer_notes,
    ]
    return "\n".join(str(p or "") for p in parts).lower()


def _has_any(text: str, markers: tuple[str, ...]) -> bool:
    return any(m.lower() in text for m in markers)


def _ignored_deepen_directive(finding: Finding, review: Review, src_type: str) -> str:
    """把少数“真实入口但未打穿”的 ignored 兜底转成 deepen。

    这不是放宽 accepted 口径，只是避免 reviewer 把已有价值线索直接归档；
    真正垃圾/公开展示/图形验证码/反射 XSS 仍保持 ignored。
    """
    if review.verdict != ReviewVerdict.ignored or review.is_duplicate or not review.in_scope:
        return ""

    sc = finding.self_check
    rce_type = (finding.vuln_type or "").strip().lower() in {
        "rce", "command_injection", "command_exec", "code_injection", "ssti", "deserialization",
    }
    if sc.is_reflected_xss or sc.needs_admin_login or sc.needs_mitm:
        return ""
    # 盲打/无回显 RCE 常由扫描器时间盲模板发现、worker 给不出回显 PoC 时会置 scanner_only_no_poc，
    # 正是值得定向深挖坐实的线索，不因这个标记就完全不救（对应问题：无回显 RCE 被丢）。
    if sc.scanner_only_no_poc and not rce_type:
        return ""

    text = _review_text(finding, review)
    register_like = _has_any(text, ("注册", "register", "signup"))
    never_markers = _REVIEW_NEVER_DEEPEN_MARKERS
    if register_like:
        never_markers = tuple(m for m in never_markers if m not in {"本就公开", "公开接口"})
    if (
        _has_any(text, never_markers)
        or (_has_any(text, _REVIEW_CAPTCHA_ONLY_IGNORE_MARKERS) and not register_like)
    ):
        return ""

    auth_signal = _has_any(text, (
        "未授权", "无需登录", "无鉴权", "未鉴权", "unauthorized", "without auth", "no auth",
    ))
    config_signal = _has_any(text, (
        "系统配置", "配置项", "系统参数", "configkey", "initpassword", "init password",
        "sys.user.initpassword", "/config", "appconfig", "setting",
    ))
    register_signal = register_like and _has_any(text, (
        "注册", "批量注册", "无验证码", "免验证码", "register", "signup", "captcha",
    ))
    secret_context = _has_any(text, ("泄露", "硬编码", "暴露", "明文", "返回", "前端", "js", "配置", "config"))
    strong_secret_signal = _has_any(text, (
        "secret", "appsecret", "clientsecret", "api key", "apikey", "accesskey",
        "私钥", "密钥", "签名密钥",
    ))
    bearer_secret_signal = _has_any(text, ("token", "jwt", "session")) and secret_context
    secret_signal = strong_secret_signal or bearer_secret_signal
    upload_signal = _has_any(text, (
        "上传", "upload", "savefile", "fileupload", "multipart/form-data",
    ))
    write_signal = _has_any(text, (
        "修改", "删除", "新增", "保存", "重置", "update", "delete", "remove", "save", "reset",
    ))
    rce_signal = rce_type or _has_any(text, (
        "rce", "命令执行", "命令注入", "command inject", "远程代码", "代码执行", "code execution",
        "ssti", "模板注入", "反序列化", "deserial",
    ))
    side_channel = _has_any(text, (
        "时间盲", "time-based", "time based", "sleep(", "延时", "响应时间", "响应延迟", "延迟",
        "dnslog", "oast", "带外", "ceye", "interactsh", "burpcollaborator", "回连", "外连",
        "落地文件", "写入文件", "结果写入", "outfile", "tee ", "touch ",
    ))

    # 无回显/盲打 RCE：有稳定侧信道证据(时间盲/带外/落地回读)但缺直接回显，不当垃圾丢，回炉坐实。
    if rce_signal and side_channel:
        return (
            "这是疑似盲打/无回显 RCE/命令执行/SSTI/反序列化：已有侧信道线索但缺直接回显。"
            "沿同一注入点把命令结果坐实——用稳定 time-based(sleep 递增验证时间差线性)、"
            "DNS/HTTP 带外回连(dnslog/interactsh/ceye)、或把命令输出写入可回读的业务字段/落地文件后访问，"
            "拿到明确执行结果证据。确认时间差不稳定或无任何侧信道差异才 finish no_vuln。"
        )

    if config_signal and (auth_signal or secret_signal):
        return (
            "不要再把“配置项泄露”当最终成果提交；沿已证实的配置接口继续深挖："
            "枚举更多配置 key/接口地址，提取 token、secret、默认口令或后台路径，并实证能否登录后台、"
            "调用受限 API、读取死规矩敏感数据或执行敏感写操作。只拿到默认值/普通配置则 finish no_vuln。"
        )

    if register_signal:
        return (
            "基于已证实的注册入口继续深挖，不要把“可批量注册”单独当洞："
            "注册低影响测试账号后登录拿 token/session，枚举表单/用户/导出/后台 API，"
            "验证是否能读取或修改他人数据、批量导出、越权访问管理接口，或链到短信/改密/账号接管。"
            "若只能注册空账号且无下游危害，finish no_vuln。"
        )

    if secret_signal:
        return (
            "沿已发现的 key/secret/token 继续深挖：确认它是否可用，尝试伪造签名或携带凭证调用受限 API，"
            "必须打出读取敏感数据、后台权限、配额盗刷或敏感写操作的实证；仅证明字符串存在不要再提交。"
        )

    if upload_signal and auth_signal:
        return (
            "沿未授权上传入口继续深挖：验证可上传的扩展名、落点路径和访问方式，"
            "优先证明脚本可解析执行/可覆盖敏感文件/可读取敏感数据；只能上传并访问 txt 则 finish no_vuln。"
        )

    if write_signal and auth_signal:
        return (
            "沿未授权写接口继续深挖，但禁止删改真实/他人数据。"
            + HARMLESS_PROTOCOL
        )

    if src_type == "enterprise" and auth_signal:
        return (
            "该未授权线索尚未打出企业可收影响；继续验证是否能读取客户/员工/订单/审批/财务等受限数据，"
            "或执行权限、配置、业务状态类敏感写操作。无实际影响则 finish no_vuln。"
        )

    return ""


def _maybe_reject_edu_bombing(finding: Finding, review: Review, src_type: str) -> bool:
    """EduSRC 不收短信/邮箱轰炸；LLM 误收或误打回深挖时改判 ignored。"""
    if normalize_src_type(src_type) != "edusrc":
        return False
    if not looks_like_edu_bombing(finding):
        return False
    review.verdict = ReviewVerdict.ignored
    review.confidence = Confidence.likely
    review.severity_final = None
    review.score = min(float(review.score or 0), 1.5)
    reasons = list(review.ignore_reasons or [])
    if "EduSRC不收短信/邮箱轰炸" not in reasons:
        reasons.append("EduSRC不收短信/邮箱轰炸")
    review.ignore_reasons = reasons
    review.reviewer_notes = (
        (review.reviewer_notes or "").strip()
        + "\n[系统改判] "
        + BOMBING_BLOCK_REASON
    ).strip()
    return True


def _maybe_reject_weak_backdoor(finding: Finding, review: Review) -> bool:
    """图床/CDN/无页面替换实锤的「疑似被黑」改判 ignored。"""
    if not looks_like_weak_backdoor(finding):
        return False
    review.verdict = ReviewVerdict.ignored
    review.confidence = Confidence.likely
    review.severity_final = None
    review.score = min(float(review.score or 0), 1.5)
    reasons = list(review.ignore_reasons or [])
    if "图床/CDN不是被黑" not in reasons:
        reasons.append("图床/CDN不是被黑")
    review.ignore_reasons = reasons
    review.reviewer_notes = (
        (review.reviewer_notes or "").strip()
        + "\n[系统改判] "
        + WEAK_BACKDOOR_REASON
    ).strip()
    return True


def _maybe_accept_write_proof(finding: Finding, review: Review) -> bool:
    """无害写/删证据已经齐时，不允许因「没破坏真实数据」被 ignored/deepen。"""
    if review.verdict not in {ReviewVerdict.ignored, ReviewVerdict.deepen}:
        return False
    if review.is_duplicate or not review.in_scope:
        return False
    kind = classify_write_proof(finding)
    if kind not in STRONG_KINDS:
        return False
    review.verdict = ReviewVerdict.accepted
    review.confidence = Confidence.likely
    if review.severity_final is None:
        review.severity_final = finding.severity_claimed or Severity.medium
    review.score = min(max(review.score, 5.0), 7.4)
    review.ignore_reasons = []
    review.reviewer_notes = (
        (review.reviewer_notes or "").strip()
        + f"\n[系统改判] 写/删证据属于无害证法（{kind}），不得因未破坏真实数据驳回或打回深挖。"
    ).strip()
    return True


def _maybe_deepen_ignored(finding: Finding, review: Review, src_type: str) -> bool:
    directive = _ignored_deepen_directive(finding, review, normalize_src_type(src_type))
    if not directive:
        return False
    review.verdict = ReviewVerdict.deepen
    review.confidence = Confidence.uncertain
    review.severity_final = None
    review.score = min(max(review.score, 2.5), 3.9)
    review.deepen_directive = review.deepen_directive or directive
    review.reviewer_notes = (
        (review.reviewer_notes or "").strip()
        + "\n[系统改判] 该 Finding 不够 accepted，但属于“入口真实、下一步明确”的半成品；已从 ignored 改为 deepen，要求 worker 定向补链。"
    ).strip()
    return True


def _is_thinking_tool_choice_error(err: LLMError) -> bool:
    """强制指定 submit_review 的 tool_choice 不被模型/网关接受时的兜底判定。

    复用 client 层的宽判定：既覆盖 DeepSeek thinking 的明确报错，也覆盖部分代理网关
    (GLM/Qwen/Gemini)对 forced tool_choice 直接返回 400(如 code=1210 "API 调用参数有误")
    的情况——这些模型仍支持 tools+auto，故降级为 auto 重试，仍强制模型必须调用 submit_review。
    """
    return _is_forced_tool_choice_unsupported(err)


def _clip_text(text: str, limit: int) -> str:
    text = str(text or "")
    if len(text) <= limit:
        return text
    head = max(1, int(limit * 0.65))
    tail = max(1, limit - head - 60)
    return f"{text[:head]}\n...[已截断 {len(text) - limit} 字]...\n{text[-tail:]}"


def _clip_jsonish(value: Any, text_limit: int = 900, depth: int = 0) -> Any:
    if depth >= 3:
        return _clip_text(json.dumps(value, ensure_ascii=False) if isinstance(value, (dict, list)) else str(value), text_limit)
    if isinstance(value, str):
        return _clip_text(value, text_limit)
    if isinstance(value, list):
        if len(value) <= 12:
            items = value
        else:
            items = value[:8] + [f"...[已省略 {len(value) - 12} 项]..."] + value[-4:]
        return [_clip_jsonish(v, text_limit, depth + 1) for v in items]
    if isinstance(value, dict):
        out: dict[str, Any] = {}
        for k in sorted(value.keys(), key=str):
            out[str(k)] = _clip_jsonish(value[k], text_limit, depth + 1)
        return out
    return value


def _review_finding_payload(finding: Finding) -> dict[str, Any]:
    """压缩审核输入里的大字段；保留证据头尾和结构，减少 reviewer 输入 token。"""
    data = finding.model_dump(mode="json")
    for key, limit in _REVIEW_TEXT_LIMITS.items():
        if key in data:
            data[key] = _clip_text(data.get(key) or "", limit)
    data["steps"] = [_clip_text(str(s), 500) for s in (data.get("steps") or [])[:10]]
    data["kill_chain"] = _clip_jsonish(data.get("kill_chain") or [], 700)
    data["evidence"] = _clip_jsonish(data.get("evidence") or {}, 900)
    data["self_check"] = data.get("self_check") or {}
    return data


class Reviewer:
    def __init__(
        self,
        llm: Optional[LLMClient] = None,
        on_event: Optional[Callable[[str, dict], None]] = None,
        enable_reproduce: bool = True,
        src_type: str = "edusrc",
        src_rules: str = "",
        redline_note: str = "",
        cancel_event: Optional["threading.Event"] = None,
    ):
        self.llm = llm or LLMClient()
        self.on_event = on_event or (lambda kind, data: None)
        self.enable_reproduce = enable_reproduce
        self.src_type = normalize_src_type(src_type)
        self.src_rules = src_rules or ""
        self.redline_note = redline_note or ""
        self._last_llm_error = ""
        # 复现验证子进程的协作取消（超时/停止时传导杀进程组）
        self.cancel_event = cancel_event or threading.Event()

    def _emit(self, kind: str, **data: Any) -> None:
        self.on_event(kind, data)

    def review(self, finding: Finding) -> Review:
        self._emit("review_start", title=finding.title)

        # 阶段①②：把 Finding 全文喂给 LLM 审核
        review = self._llm_review(finding)
        if review is None:
            detail = f"：{self._last_llm_error}" if self._last_llm_error else ""
            raise RuntimeError(f"审核 LLM 调用异常或结构化输出无效{detail}，保留 pending_review 稍后重试。")

        if _maybe_reject_edu_bombing(finding, review, self.src_type):
            self._emit("review_auto_ignore_bombing", title=finding.title)
        elif _maybe_reject_weak_backdoor(finding, review):
            self._emit("review_auto_ignore_weak_backdoor", title=finding.title)
        elif _maybe_accept_write_proof(finding, review):
            self._emit("review_auto_accept_write", title=finding.title, write_kind=classify_write_proof(finding))
        elif _maybe_deepen_ignored(finding, review, self.src_type):
            self._emit("review_auto_deepen", title=finding.title, directive=review.deepen_directive)

        # 阶段③：仅 accepted 且 严重/高危 才触发复现验证。
        # 写/删 PoC 禁止现场复放：URL 含 delete 不是破坏性 SQL，复放既不安全
        # 也会把已取证的高危洞误降成 deepen，最后埋进「AI 未采纳」。
        if (
            self.enable_reproduce
            and review.verdict == ReviewVerdict.accepted
            and review.severity_final in _HIGH_VALUE
        ):
            skip_replay, skip_why = should_skip_live_replay(finding, finding.poc)
            if skip_replay:
                if has_strong_write_proof(finding):
                    review.reproduced = True
                    review.reviewer_notes += (
                        f"\n[复现验证] SKIPPED({skip_why})：无害写/删证据链已齐，"
                        "不现场复放写接口；视同已复现。"
                    )
                    self._emit("reproduce_done", title=finding.title, reproduced=True, skipped=skip_why)
                else:
                    review.reproduced = False
                    review.verdict = ReviewVerdict.deepen
                    review.confidence = Confidence.uncertain
                    review.severity_final = None
                    review.score = min(review.score, 3.9)
                    review.deepen_directive = review.deepen_directive or HARMLESS_PROTOCOL
                    review.reviewer_notes += (
                        f"\n[自动降级] 高危/严重写删结论不能现场复放（{skip_why}），"
                        "且无害证据不足，改为 deepen，禁止未证实结论进入人工复审。"
                    )
                    self._emit("reproduce_done", title=finding.title, reproduced=False, skipped=skip_why)
            else:
                self._reproduce(finding, review)
                if not review.reproduced:
                    review.verdict = ReviewVerdict.deepen
                    review.confidence = Confidence.uncertain
                    review.severity_final = None
                    review.score = min(review.score, 3.9)
                    if not review.deepen_directive:
                        review.deepen_directive = (
                            "当前高危/严重结论复现未通过，不能进入人工待审核。"
                            "请补充真实成功证据：例如证明密码重置后可用新密码登录，"
                            "或证明接口返回明确成功且状态已真实变化。"
                        )
                    review.reviewer_notes += (
                        "\n[自动降级] 高危/严重漏洞必须有可复现实锤；本次系统复现未通过，"
                        "已改为 deepen，禁止以未证实结论进入人工复审队列。"
                    )

        # 信度约束：未经系统复现的，不允许标 confirmed（最高 likely）
        if not review.reproduced and review.confidence == Confidence.confirmed:
            review.confidence = Confidence.likely

        # 未证实次数熔断：同一个洞反复"未证实"打回，必须收敛到「AI 未采纳」。
        # 只对真·未证实（reproduced=False 且 verdict=deepen）计数；accepted 不计数。
        if review.verdict == ReviewVerdict.deepen and not review.reproduced:
            review.uncertain_attempts = int(getattr(review, "uncertain_attempts", 0) or 0) + 1
            if review.uncertain_attempts >= UNCERTAIN_ATTEMPT_CAP:
                review.verdict = ReviewVerdict.ignored
                review.severity_final = review.severity_final or finding.severity_claimed or Severity.medium
                reasons = list(review.ignore_reasons or [])
                reasons.insert(0, (
                    f"已连续 {review.uncertain_attempts} 次「未证实」（复现未通过），"
                    "按熔断规则归档进 AI 未采纳，供人工判定是否误杀"
                ))
                review.ignore_reasons = reasons
                review.reviewer_notes = (
                    (review.reviewer_notes or "").rstrip()
                    + f"\n[熔断归档] 该洞累计 {review.uncertain_attempts} 次未证实，"
                    "已停止自动重审，转人工判断。"
                ).strip()
                self._emit("review_uncertain_capped",
                           title=finding.title,
                           attempts=review.uncertain_attempts)

        self._emit(
            "review_done",
            verdict=review.verdict.value,
            severity=review.severity_final.value if review.severity_final else None,
            score=review.score,
            confidence=review.confidence.value,
            deepen_directive=review.deepen_directive if review.verdict == ReviewVerdict.deepen else None,
        )
        return review

    def _llm_review(self, finding: Finding) -> Optional[Review]:
        finding_text = json.dumps(_review_finding_payload(finding), ensure_ascii=False, separators=(",", ":"))
        mode_name = "企业 SRC" if self.src_type == "enterprise" else "EduSRC"
        messages = [
            {"role": "system", "content": reviewer_system_prompt(self.src_type, src_rules=self.src_rules, redline_note=self.redline_note)},
            {"role": "user", "content": _REVIEW_STATIC_PREFIX},
            {"role": "user", "content": (
                f"按 {mode_name} 标准审核并调用 submit_review：\n```json\n{finding_text}\n```"
            )},
        ]
        forced_tool_choice = True
        for _ in range(3):  # 最多 3 次让模型修正
            try:
                tool_choice = (
                    {"type": "function", "function": {"name": "submit_review"}}
                    if forced_tool_choice else "auto"
                )
                msg = self.llm.chat(
                    messages, tools=REVIEWER_TOOL_SCHEMAS,
                    tool_choice=tool_choice,
                )
            except LLMError as e:
                if e.kind == "quota":
                    raise
                self._last_llm_error = str(e)
                if forced_tool_choice and _is_thinking_tool_choice_error(e):
                    forced_tool_choice = False
                    self._emit(
                        "review_tool_choice_fallback",
                        error="thinking 模式不支持强制 submit_review，已降级为 auto tool_choice 重试",
                    )
                    messages.append({
                        "role": "user",
                        "content": (
                            "当前模型不支持强制指定工具。请你必须主动调用 submit_review 工具，"
                            "不要只输出自然语言；否则本次审核无法落库。"
                        ),
                    })
                    continue
                self._emit("review_error", error=self._last_llm_error)
                return None
            except Exception as e:
                self._last_llm_error = str(e)
                self._emit("review_error", error=self._last_llm_error)
                return None

            tool_calls = getattr(msg, "tool_calls", None)
            if not tool_calls:
                messages.append({"role": "assistant", "content": msg.content or ""})
                messages.append({"role": "user", "content": "请调用 submit_review 工具输出结构化结论。"})
                continue

            tc = tool_calls[0]
            try:
                args = json.loads(tc.function.arguments or "{}")
                # Review 模型不认识 cvss_* 字段（那是给 CVSS 计算器用的），
                # 必须先剔掉再构造，否则 pydantic 会因 extra field 报校验失败。
                cvss_args = {k: v for k, v in args.items() if k.startswith("cvss_")}
                model_args = {k: v for k, v in args.items() if not k.startswith("cvss_")}
                review = Review(**model_args)
                # reproduced 只能由系统的复现阶段设置，不信任 LLM 自填
                review.reproduced = False
                self._calibrate_cvss(review, cvss_args)
                return review
            except (json.JSONDecodeError, ValidationError) as e:
                messages.append({"role": "assistant", "content": "", "tool_calls": [
                    {"id": tc.id, "type": "function",
                     "function": {"name": tc.function.name, "arguments": tc.function.arguments}}
                ]})
                messages.append({"role": "tool", "tool_call_id": tc.id,
                                 "content": f"校验失败，请修正后重新调用 submit_review: {e}"})
        return None

    def _calibrate_cvss(self, review: Review, args: dict) -> None:
        """用 CVSS 3.1 给分数做二次校验，回填向量。

        设计取舍（重要）：**只用 CVSS 纠「明显虚高」，不强行拉高或覆盖结论**。
        原因：CVSS 衡量的是技术影响，而 SRC 口径还叠了「这类漏洞收不收」的业务规则
        （EduSRC 就明确不收 self-XSS、用户名枚举等）。技术上 6.1 的反射 XSS，
        平台照样拒收。若拿 CVSS 硬改 verdict/severity，会把平台明确不收的东西塞进复审队列。

        所以这里只做两件事：
          1. LLM 给了八项指标 / 向量 → 按 NVD 公式算分并回填 cvss_vector，让报告可复算
          2. LLM 自评分比 CVSS 高出 1.5 以上（明显虚高）→ 压回 CVSS 分，并记降级理由
        反过来「LLM 判低但 CVSS 高」不自动抬升：那通常说明 LLM 已经按平台口径做了业务裁量，
        抬回去等于用技术分对抗业务规则。
        """
        try:
            metrics, attempted = cvss_from_args(args)
        except Exception:
            return
        if not attempted:
            return
        if not metrics:
            review.reviewer_notes += (
                "\n[CVSS] 未给出完整的八项基础指标，本条未做 CVSS 校准（不影响结论）。"
            )
            return
        reject = nvd_reject_reason(metrics)
        if reject:
            review.reviewer_notes += f"\n[CVSS] {reject}"
            return
        scored = cvss_base_score(metrics)
        review.cvss_vector = scored.vector
        review.reviewer_notes += (
            f"\n[CVSS] NVD {scored.vector} = {scored.score:.1f}（{scored.band_zh}）"
        )
        # 只压虚高：高出 1.5 分以上才纠偏
        if review.score - scored.score > 1.5:
            old = review.score
            review.score = scored.score
            review.downgrade_reasons.append(
                f"自评分 {old:.1f} 明显高于 CVSS {scored.score:.1f}，按 NVD 口径校正"
            )
            review.reviewer_notes += f"\n[CVSS] 自评分 {old:.1f} → {scored.score:.1f}（虚高校正）"

        # 等级与 CVSS 定性分档不一致时留痕。
        # 不改 severity_final（那是按平台收洞口径定的），但报告里「等级：高危 / CVSS：9.8 严重」
        # 并列会让复审觉得自相矛盾，所以必须写清为什么：
        #   - CVSS 高、平台定级低 → 通常是业务口径（平台不收这类，或影响面有限）
        #   - CVSS 低、平台定级高 → 通常是危害不在 C/I/A（如纯业务逻辑、破坏信任）
        band_rank = {"低危": 1, "中危": 2, "高危": 3, "严重": 4}
        sev_zh = str(getattr(review.severity_final, "value", review.severity_final) or "")
        if sev_zh in band_rank and scored.band_zh in band_rank:
            gap = band_rank[scored.band_zh] - band_rank[sev_zh]
            if abs(gap) >= 2:
                review.reviewer_notes += (
                    f"\n[CVSS] 注意：CVSS 定性为 {scored.band_zh}，平台定级 {sev_zh}，"
                    "差两档以上。若两者并列展示，请人工确认是技术影响与业务口径的差异，"
                    "而非评分或定级错误。"
                )

    def _reproduce(self, finding: Finding, review: Review) -> None:
        """复现验证：重新执行 PoC（高价值漏洞才做）。"""
        self._emit("reproduce_start", title=finding.title)
        executor = ToolExecutor(f"review_{finding.target_url}", cancel_event=self.cancel_event,
                                enterprise=(self.src_type == "enterprise"))
        # 用 PoC 重新发包（PoC 通常是 curl 命令）
        poc = finding.poc.strip()
        if not poc:
            review.reviewer_notes += "\n[复现] 无 PoC 可执行。"
            self._emit("reproduce_done", title=finding.title, reproduced=False)
            return
        skip_replay, skip_why = should_skip_live_replay(finding, poc)
        if skip_replay:
            review.reviewer_notes += (
                f"\n[复现验证] SKIPPED({skip_why})：不自动执行写/删或破坏性 SQL。"
                "该 PoC 不能作为现场复放实锤，请看无害证据链。"
            )
            self._emit("reproduce_done", title=finding.title, reproduced=False, skipped=skip_why)
            return
        result = executor.run_shell(poc, timeout=60)
        out = (result.get("output") or "")[:1000]

        # 关键前置判断：命令本身没跑成（工具缺失/超时/被拦/非零退出且无输出）
        # ≠ 漏洞复现失败。原逻辑直接把空输出喂给 LLM，LLM 只能判 NO，
        # 高危洞因此被误降成 deepen —— 实测凭据类漏洞就这么丢过。
        run_kind, run_why = _classify_replay_run(result, out)
        if run_kind == "not_run":
            review.reviewer_notes += (
                f"\n[复现验证] NOT_RUN({run_why})：PoC 命令未成功执行，"
                "这不代表漏洞不成立。保留原结论，由人工按证据链复核。"
            )
            # 不设 reproduced=True（那是「已验证」的强含义），但也不降级：
            # 把 verdict 与 severity 原样保留，只在备注里标明「未跑成」。
            self._emit("reproduce_done", title=finding.title, reproduced=False, not_run=run_why)
            return

        # 让 LLM 判断复现输出是否支撑漏洞
        judge_failed = False
        try:
            msg = self.llm.chat([
                {"role": "system", "content": (
                    "你在做漏洞复现验证。根据 PoC 的实际执行输出，判断该漏洞是否被成功复现。\n\n"
                    "分级判定（重要）：\n"
                    "• 完整利用链走通（如登录取到 token → 用 token 读到敏感数据）→ 回 YES\n"
                    "• 关键前置条件已实证（如弱口令登录成功并返回管理员 token、"
                    "上传成功并回读、SQLi 报错回显出库名），但后续步骤因 token 过期/缺 header/"
                    "PoC 少一步而未走完 → 也回 YES，并在理由里注明「部分复现」\n"
                    "• 输出与漏洞无关、或明确证伪（如接口 404 不存在、鉴权正常拦截）→ 回 NO\n\n"
                    "判 NO 的唯一依据是「证据指向漏洞不成立」，"
                    "不能因为「链路没走完」就判 NO —— 那属于部分复现。\n"
                    "只回 YES 或 NO 加一句理由。"
                )},
                {"role": "user", "content": (
                    f"漏洞: {finding.title}\n预期: {finding.description[:500]}\n\n"
                    f"PoC 实际执行输出:\n{out}\n\n该漏洞是否成功复现（含部分复现）？"
                )},
            ], temperature=0.0)
            verdict_text = (msg.content or "").strip()
        except Exception as e:
            judge_failed = True
            verdict_text = f"复现判断异常: {e}"

        if judge_failed:
            # 判官本身挂了，不能推出「漏洞不成立」。保留原结论只做备注，
            # 否则一次 LLM 抖动就能把高危洞打成 deepen。
            review.reviewer_notes += (
                f"\n[复现验证] JUDGE_FAILED：{verdict_text[:80]}。"
                "判官调用失败，不代表漏洞不成立，保留原结论待人工复核。"
            )
            self._emit("reproduce_done", title=finding.title, reproduced=False, judge_failed=True)
            return

        reproduced = verdict_text.upper().startswith("YES")
        review.reproduced = reproduced
        if reproduced:
            review.confidence = Confidence.confirmed
        elif review.confidence == Confidence.confirmed:
            review.confidence = Confidence.likely
        review.reviewer_notes += f"\n[复现验证] {verdict_text}"
        self._emit("reproduce_done", title=finding.title, reproduced=reproduced)
