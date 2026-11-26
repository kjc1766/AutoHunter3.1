"""核心数据结构 (Pydantic)。

Finding 是 worker 挖到漏洞后的标准输出格式，对应设计文档 §6。
SelfCheck 强制 worker 先对照当前 SRC 模式的忽略清单做一遍自检。
"""
from __future__ import annotations

from enum import Enum
from typing import Optional

from pydantic import BaseModel, Field


class Severity(str, Enum):
    critical = "严重"
    high = "高危"
    medium = "中危"
    low = "低危"


class Verdict(str, Enum):
    """worker 对单个目标的结论。

    ★ 六分法（移植自 clown-src-6k 的 research-runtime contract）：
    「完成语义混用」是长程跑偏的头号根因——原来 no_vuln 同时装了三种完全不同的东西，
    导致「被 WAF 挡住没试成」被记成「确认没洞」，目标进 dead 永不重开，搜索空间被静默收窄。

      found                     挖到了（有 findings）
      no_vuln                   真的挖透了，确认该面没有可利用漏洞
      inconclusive              做了但说不清（响应异常、证据不足、无法判定）
      blocked                   受阻（被 WAF/登录墙/频率限制/依赖不可用挡住，没试成）
      invalid_precondition      前提不成立（目标环境不满足，如需要内网、需要特定角色）
      cancelled                 被取消（用户停止、预算耗尽、外部中断）
      error                     执行出错（LLM 失败、工具崩溃等系统性问题）

    派发语义区别：
      - blocked  → status=waiting，**不消耗重试次数、不进 dead**，等 unblock 条件满足后唤醒
      - inconclusive → 按普通重试处理（换角度再来一次）
      - invalid_precondition → 进 dead 但记录原因，便于人工复核
    """
    found = "found"                      # 挖到漏洞
    no_vuln = "no_vuln"                  # 确认无漏洞
    inconclusive = "inconclusive"        # 无法判定
    blocked = "blocked"                  # 受阻（不是没洞）
    invalid_precondition = "invalid_precondition"  # 前提不成立
    cancelled = "cancelled"              # 被取消
    error = "error"                      # 出错


class SelfCheck(BaseModel):
    """worker 提交漏洞前的垃圾洞自检，对照当前 SRC 模式忽略清单。"""
    is_reflected_xss: bool = Field(False, description="是否为反射型 XSS（按当前 SRC 规则判断是否忽略/降级）")
    needs_admin_login: bool = Field(False, description="是否需要登录管理员后台才能触发（会被忽略）")
    needs_mitm: bool = Field(False, description="是否需要中间人攻击（会被忽略）")
    is_pure_info_leak: bool = Field(False, description="是否为无实际利用的信息泄露，如 phpinfo/内网IP/源码（会被忽略）")
    scanner_only_no_poc: bool = Field(False, description="是否仅扫描器出结果但无法给出利用方法（会被忽略）")
    is_public_interface: bool = Field(False, description="该接口是否本就是面向公众的公开接口（若是，访问它通常不构成漏洞）")
    info_leak_hits_strict_list: bool = Field(False, description="若属信息泄露类：泄露数据是否命中当前 SRC 模式的高价值敏感数据口径")


class Evidence(BaseModel):
    extracted_data_sample: Optional[str] = Field(None, description="脱敏后的数据样本，证明能拿到数据")
    tool_output: Optional[str] = Field(None, description="关键工具输出片段")
    notes: Optional[str] = Field(None, description="其它证据说明")


class ChainStep(BaseModel):
    """攻击链路中的一步：用了什么方法 + 这步得到了什么。"""
    method: str = Field(..., description="这一步用的方法/动作，如『审计前端JS』『提取API端点』『测试越权』")
    detail: str = Field("", description="这步具体做了什么、发现/得到了什么")


class Finding(BaseModel):
    """worker 标准漏洞输出。缺关键字段审核会直接打回。"""
    vuln_type: str = Field(..., description="漏洞类型，如 sql_injection / rce / captcha_bypass / idor / unauthorized_access")
    title: str = Field(..., description="漏洞标题，格式：[目标] - [模块] - [简述]")
    severity_claimed: Severity = Field(..., description="worker 自评等级")
    target_url: str = Field(..., description="漏洞所在 URL")
    owner: str = Field("", description="归属单位/业务系统 + 确认依据。EduSRC 写学校；企业模式写企业/集团/系统")
    description: str = Field(..., description="漏洞类型、触发条件、影响范围")
    steps: list[str] = Field(..., description="复现步骤，逐条")
    poc: str = Field(..., description="可执行的 PoC，curl 命令 / payload")
    raw_request: str = Field("", description="原始请求包")
    raw_response: str = Field("", description="原始响应包（含证明漏洞的关键差异）")
    evidence: Evidence = Field(default_factory=Evidence)
    affected_scope: str = Field("", description="影响面，如可获取的数据量/权限")
    impact: str = Field(
        "",
        description=(
            "漏洞危害：只写最终能造成哪些伤害（人/号/钱/内部正文/能改能删），每种伤害单独一行。"
            "有例子的必须举例（姓名/手机号/证件实值，或改成了什么）；没真打过的权限面照写能力但不要编具体受害者。"
            "不是步骤，不写「第一层/第二层」，不用「不限于」「等敏感信息」这类模糊表述。"
        ),
    )
    fix_suggestion: str = Field(
        "",
        description="修复建议：贴合本洞的精准整改方案，简短直白可落地",
    )
    kill_chain: list[ChainStep] = Field(default_factory=list, description="攻击链路：按时间顺序记录怎么一步步打下来的（侦察→定位→利用→取证）")
    self_check: SelfCheck = Field(default_factory=SelfCheck)


class WorkerResult(BaseModel):
    """worker 对单个目标的最终结论。"""
    target: str
    verdict: Verdict
    findings: list[Finding] = Field(default_factory=list)
    summary: str = Field("", description="worker 对本次挖掘的总结")
    rounds: int = 0
    error: Optional[str] = None
    failure_kind: str = Field("", description="结构化失败类型，供编排层决定是否回队")
    retry_after_seconds: int = Field(0, ge=0, description="建议等待秒数；0 表示无需延迟")
    deepen_lead: str = Field("", description="突破入口但未打穿时的定向深挖线索，触发自动回火再派一轮")
    block_reason: str = Field(
        "",
        description=(
            "verdict=blocked 时必填：具体被什么挡住（WAF 拦截页 / 需要短信验证码 / 接口 429 限流 / 目标 502）"
        ),
    )
    unblock_condition: str = Field(
        "",
        description=(
            "verdict=blocked 时必填：**满足什么条件就能重开**（如「换新出口 IP」「拿到有效会话」"
            "「该接口恢复 200」）。写不出解锁条件说明这不是 blocked，而是 no_vuln 或 inconclusive"
        ),
    )
    reported_intel: list[dict] = Field(default_factory=list, description="worker 主动上报的可复用情报，编排层落全局情报库")
    reported_coverage: list[dict] = Field(default_factory=list, description="单站协作覆盖记录，编排层写事件流供后续 worker 复用")
    # LLM 中断回队时携带：工作笔记 / 会话 cookie·头 / 已挖轮次，避免重开后进度归零
    resume_context: dict = Field(default_factory=dict, description="LLM 中断后回队续挖用的进度快照")


class ReviewVerdict(str, Enum):
    accepted = "accepted"  # 进最终列表
    ignored = "ignored"    # 垃圾洞/不收，丢弃
    deepen = "deepen"      # 线索有价值但利用没打穿，打回定向深挖


class Confidence(str, Enum):
    confirmed = "confirmed"  # 证据完整(+复现成功)，可直接提交
    likely = "likely"        # 证据合理但未完全复现
    uncertain = "uncertain"  # 合理但有疑点，交用户裁决


class Review(BaseModel):
    """审核 agent 对单个 Finding 的结论，对应设计文档 §5 Review 表。"""
    verdict: ReviewVerdict = Field(..., description="accepted=进最终列表 / ignored=丢弃 / deepen=打回深挖")
    confidence: Confidence = Field(..., description="信度分档")
    severity_final: Optional[Severity] = Field(None, description="审核后的最终等级（accepted 时必填）")
    score: float = Field(..., ge=0, le=10, description="0-10 评分")
    # CVSS 3.1 基础向量（如 CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:U/C:H/I:H/A:H）。
    # 由 reviewer 按 NVD 公式计算后回填，让定级可复算、可审计，而不是纯主观打分。
    cvss_vector: str = Field("", description="CVSS 3.1 基础向量（系统按 NVD 公式回填）")
    in_scope: bool = Field(..., description="是否在当前任务 SRC 范围内")
    is_duplicate: bool = Field(False, description="是否与已有漏洞重复")
    ignore_reasons: list[str] = Field(default_factory=list, description="忽略理由（ignored 时必填）")
    downgrade_reasons: list[str] = Field(default_factory=list, description="降级理由")
    reproduced: bool = Field(False, description="是否复现验证过")
    reviewer_notes: str = Field("", description="审核备注：判断依据")
    # deepen 时必填：明确告诉 worker 这一轮要把什么利用链打穿
    deepen_directive: str = Field("", description="深挖指令（verdict=deepen 时必填）：具体要证明/打穿什么")
    # 同一漏洞被「未证实」打回的累计次数（跨轮次计入 DB，这里只作运行时载体）。
    # reviewer 在熔断逻辑里会读写这个字段；Pydantic BaseModel 默认禁止赋值未声明字段，
    # 不声明会抛 `"Review" object has no field "uncertain_attempts"`。
    # 实测该异常导致 8888-8963 任务累计 2612 次审核失败、所有 finding 卡在 pending_review。
    uncertain_attempts: int = Field(0, description="未证实累计次数（熔断用，运行时字段）")
