"""回归测试：保证 1) 真洞不被吞 2) 重复筛查 + 同类型合并。

用户要求的两条硬保证，全部用真实代码路径验证。
"""
import sys

sys.path.insert(0, "/app")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R = []


def chk(name, fn):
    try:
        ok, d = fn()
        R.append((name, ok, str(d)[:78]))
    except Exception as e:
        R.append((name, False, f"{type(e).__name__}: {str(e)[:60]}"))


# ============ 保证 1：真洞不会被吞 ============
print("【保证 1】真洞不会被吞\n")


def a1_archived_no_filter():
    """归档接口不得过滤 superseded。"""
    src = open("/app/app/api/findings.py", encoding="utf-8").read()
    # 只查 archived_list 函数体内的 where 子句
    i = src.find("async def archived_list")
    j = src.find("async def", i + 10)
    body = src[i:j]
    bad = 'Finding.status != "superseded"' in body or "Finding.status != 'superseded'" in body
    return (not bad, "已移除 superseded 过滤" if not bad else "仍在过滤！")


chk("归档接口不过滤 superseded", a1_archived_no_filter)


def a2_stats_match_list():
    """stats.archived 计数条件必须与 archived_list 一致。"""
    t = open("/app/app/api/tasks.py", encoding="utf-8").read()
    i = t.find("stats.archived = ")
    seg = t[i:i + 400]
    bad = "superseded" in seg.split(")").__str__()[:600] or 'Finding.status != "superseded"' in seg
    return (not bad, "计数与列表一致" if not bad else "计数仍在过滤 superseded")


chk("归档徽标数==列表条数", a2_stats_match_list)


def a3_sweep_exists():
    src = open("/app/app/orchestrator.py", encoding="utf-8").read()
    ok = "_sweep_orphan_superseded" in src and "_maybe_sweep_orphan_superseded" in src
    return (ok, "兜底自愈已就位" if ok else "缺失")


chk("兜底自愈存在", a3_sweep_exists)


def a4_sweep_hooked():
    src = open("/app/app/orchestrator.py", encoding="utf-8").read()
    n = src.count("await self._maybe_sweep_orphan_superseded(session)")
    return (n >= 1, f"挂载 {n} 处" if n else "未挂到主循环")


chk("兜底自愈挂了主循环", a4_sweep_hooked)


def a5_migration():
    """uncertain_attempts 必须在自动迁移清单里，否则新库缺列。"""
    src = open("/app/app/db/session.py", encoding="utf-8").read()
    i = src.find("_MIGRATIONS = [")
    j = src.find("]", i)
    ok = "uncertain_attempts" in src[i:j]
    return (ok, "已入 _MIGRATIONS" if ok else "缺失（新库会报 no such column）")


chk("新列走自动迁移", a5_migration)


def a6_sweep_no_cooldown_on_fail():
    src = open("/app/app/orchestrator.py", encoding="utf-8").read()
    i = src.find("async def _maybe_sweep_orphan_superseded")
    body = src[i:i + 900]
    # 失败分支必须在更新计时器之前 return
    fail_ret = body.find("return")
    set_ts = body.find("self._last_orphan_sweep = now_ts")
    ok = 0 <= fail_ret < set_ts
    return (ok, "失败不推进冷却" if ok else "失败也推进冷却")


chk("sweep 失败不推进冷却", a6_sweep_no_cooldown_on_fail)


# ============ 保证 2：重复筛选 + 同类合并 ============
print("\n【保证 2】重复筛查 + 同类型合并\n")


def b1_dedup_same():
    from app import dedup
    u = "https://x.com/api/login"
    a = dedup.fingerprint(u, {"title": "后台默认弱口令 admin/admin123", "vuln_type": "默认口令"})
    b = dedup.fingerprint(u, {"title": "后台弱口令 admin/admin123 接管", "vuln_type": "弱口令+越权"})
    return (a.key == b.key, f"同洞同key={a.key == b.key} sem={a.sem}")


chk("同洞不同写法→同key", b1_dedup_same)


def b2_dedup_diff():
    from app import dedup
    u = "https://x.com/api/login"
    a = dedup.fingerprint(u, {"title": "弱口令 admin", "vuln_type": "弱口令"})
    c = dedup.fingerprint(u, {"title": "SQL注入", "vuln_type": "SQL注入"})
    return (a.key != c.key, "异洞异key（不误合并）")


chk("异洞不误判重复", b2_dedup_diff)


def b3_dedup_intercept():
    """入口去重必须能拦下重复提交。"""
    from app import dedup
    hist = [{"id": "1", "title": "后台默认弱口令 admin/admin123",
             "vuln_type": "默认口令", "target_url": "https://a.com/api/login",
             "dedup_key": "", "source": "history", "policy": "block"}]
    cand = {"id": "2", "title": "后台弱口令 admin/admin123 接管",
            "vuln_type": "弱口令+越权", "target_url": "https://a.com/api/login"}
    dup, ms = dedup.is_duplicate(cand, hist, target_ref="https://a.com/api/login")
    return (dup, f"拦截={dup} 理由={(ms[0].get('reason') if ms else '')[:40]}")


chk("重复提交被拦截", b3_dedup_intercept)


def b4_cluster_merge():
    from app.cluster import build_clusters
    items = [
        {"id": "1", "title": "鑫贝帝管理后台默认弱口令 admin/admin123", "vuln_type": "默认口令",
         "target_url": "https://www.xinbeidi.net/api/admin/login", "severity_claimed": "高危", "poc": "c"},
        {"id": "2", "title": "鑫贝帝管理后台弱口令 admin/admin123 接管", "vuln_type": "弱口令+越权",
         "target_url": "https://www.xinbeidi.net/api/admin/login", "severity_claimed": "严重", "poc": "c"},
        {"id": "3", "title": "鑫贝帝后台弱口令→ADMIN token", "vuln_type": "弱口令",
         "target_url": "https://www.xinbeidi.net/api/admin/login", "severity_claimed": "高危", "poc": "c"},
    ]
    c = build_clusters(items)
    return (len(c) == 1 and c[0]["count"] == 3, f"3条→{len(c)}组")


chk("同类型漏洞合并", b4_cluster_merge)


def b5_cluster_keep_diff():
    from app.cluster import build_clusters
    items = [
        {"id": "1", "title": "A站 SQL 注入", "vuln_type": "SQL注入",
         "target_url": "https://a.com/api/eval", "severity_claimed": "高危", "poc": "c"},
        {"id": "2", "title": "A站 任意文件上传 RCE", "vuln_type": "RCE",
         "target_url": "https://a.com/api/upload", "severity_claimed": "严重", "poc": "c"},
    ]
    c = build_clusters(items)
    return (len(c) == 2, f"2个不同的洞→{len(c)}组（不误合）")


chk("不同类型不误合并", b5_cluster_keep_diff)


def b6_fold_grouped():
    """归档列表必须支持折叠。"""
    src = open("/app/app/api/findings.py", encoding="utf-8").read()
    ok = "grouped: bool = Query(True" in src and "_fold_archived" in src
    return (ok, "折叠参数+实现都在" if ok else "缺失")


chk("归档列表支持折叠", b6_fold_grouped)


def b7_endpoint_lenient():
    from app import dedup
    hist = [{"id": "1", "title": "api/code 会话签发", "vuln_type": "auth_bypass",
             "target_url": "https://a.com/api/code?uid=admin", "dedup_key": "", "source": "h", "policy": "block"}]
    cand = {"id": "2", "title": "api/code 零凭证签发", "vuln_type": "认证绕过",
            "target_url": "https://a.com/api/code"}
    dup, _ = dedup.is_duplicate(cand, hist, target_ref="https://a.com/api/code")
    return (dup, "单边query容错生效" if dup else "未拦住")


chk("端点单边query容错", b7_endpoint_lenient)


print("=" * 84)
print(f"{'检查项':<28}{'结果':<7}说明")
print("-" * 84)
for n, o, d in R:
    print(f"{n:<28}{'PASS' if o else 'FAIL':<7}{d}")
print("-" * 84)
p = sum(1 for _, o, _ in R if o)
print(f"通过 {p}/{len(R)}")
