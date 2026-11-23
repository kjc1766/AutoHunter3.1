"""任务级可选红线（用户勾选生效）。

与内置自身红线的区别：
- 内置红线（禁止全量脱库 / 禁止扫描器心智 / 禁自毁环境）写死在 guard 与
  prompts 里，**不受开关影响，永远生效**。
- 这里的 REDLINE_CATALOG 是**可供用户按项目勾选**的行为边界：不同 SRC 项目
  对「能不能拿凭据去登录」「能不能探内网」的要求不一样，交给用户决定。

勾选后拼进 worker 系统提示词末尾，作为该任务不可逾越的硬约束；
同时供前端渲染勾选框。
"""

from __future__ import annotations

# id -> (标题, 完整规则文本)
REDLINE_CATALOG: list[dict] = [
    {
        "id": "src_common",
        "title": "通用 SRC 红线",
        "desc": "翻找敏感凭据、增删改等操作均属禁止测试行为；拿凭据后直接交报告",
        "rule": (
            "【通用 SRC 红线】翻找敏感凭据、增删改等操作均属于禁止测试行为，"
            "可在报告中说明详细利用思路，人工复审将进行验证。"
            "如获取 AK/SK、kubernetes 集群凭证（如 kube-config、ServiceAccount）后"
            "请直接提交报告，将由审核验证和确认影响范围及等级，**严禁自行深入业务验证危害**。"
        ),
    },
    {
        "id": "rce",
        "title": "RCE 红线",
        "desc": "禁止反弹 Shell、WebShell、提权、横向移动、读取敏感文件",
        "rule": (
            "【RCE 红线】禁止反弹 Shell、禁止落地 WebShell、禁止提权、"
            "禁止横向移动、禁止读取敏感文件。只证明到「命令可执行」即可，"
            "在报告中说明后续可利用思路，由人工复审验证。"
        ),
    },
    {
        "id": "ssrf",
        "title": "SSRF 红线",
        "desc": "禁止探测内网、访问云元数据、获取凭据或继续打内网",
        "rule": (
            "【SSRF 红线】禁止探测内网、禁止访问云元数据地址（如 169.254.169.254）、"
            "禁止借 SSRF 获取凭据或继续向内网横向打击。"
            "证明「服务端可被驱使发起请求」即止，在报告中说明内网可达性推断。"
        ),
    },
    {
        "id": "container_escape",
        "title": "容器逃逸红线",
        "desc": "禁止操作宿主机、读取宿主机凭据、访问其他容器",
        "rule": (
            "【容器逃逸红线】禁止操作宿主机、禁止读取宿主机凭据、禁止访问其他容器。"
            "证明逃逸可行性（如挂载点可写、特权容器）即止，不做实际落地操作。"
        ),
    },
    {
        "id": "file_upload",
        "title": "文件上传红线",
        "desc": "禁止上传 WebShell、恶意脚本、后门文件，或覆盖业务文件",
        "rule": (
            "【文件上传红线】禁止上传 WebShell、恶意脚本、后门文件，"
            "禁止覆盖任何业务文件。只验证「可上传类型/路径可控」或上传无害标记文件并立即清理，"
            "不得造成业务影响。"
        ),
    },
    {
        "id": "credential",
        "title": "凭据泄露红线",
        "desc": "禁止使用凭据登录、查询资源、进入集群或继续验证危害",
        "rule": (
            "【凭据泄露红线】禁止使用泄露的凭据登录、查询资源、进入集群或继续验证危害。"
            "证明「凭据真实有效（如能换取 token 的前置返回）」即止，"
            "在报告中说明影响范围，由人工验证。"
        ),
    },
]

_BY_ID = {x["id"]: x for x in REDLINE_CATALOG}


def normalize_redline_checks(raw) -> list[str]:
    """过滤非法 id、去重、保持目录顺序。"""
    if not raw:
        return []
    if isinstance(raw, str):
        try:
            import json
            raw = json.loads(raw)
        except Exception:
            raw = [raw]
    if not isinstance(raw, (list, tuple, set)):
        return []
    picked = {str(x).strip() for x in raw if x}
    return [x["id"] for x in REDLINE_CATALOG if x["id"] in picked]


def render_redline_prompt(checks) -> str:
    """把勾选的红线渲染成提示词片段。未勾选返回空串。"""
    ids = normalize_redline_checks(checks)
    if not ids:
        return ""
    lines = ["# 本任务附加红线（用户勾选，硬约束，违反即无效）"]
    for i, rid in enumerate(ids, 1):
        lines.append(f"{i}. {_BY_ID[rid]['rule']}")
    lines.append(
        "以上红线优先于「打穿门限」：当打穿需要跨越某条红线时，"
        "**停在红线前，把已得证据交报告并写清后续利用思路**，由人工复审验证。"
    )
    return "\n".join(lines)
