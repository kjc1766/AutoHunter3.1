"""产量熔断 + 原有两条保证 的联合回归。"""
import sys

sys.path.insert(0, "/app")
sys.stdout.reconfigure(encoding="utf-8", errors="replace")

R = []


def chk(n, fn):
    try:
        ok, d = fn()
        R.append((n, ok, str(d)[:72]))
    except Exception as e:
        R.append((n, False, f"{type(e).__name__}: {str(e)[:55]}"))


def t_quota_const():
    from app.agents.worker import VULN_CLASS_QUOTA
    return (VULN_CLASS_QUOTA >= 1, f"VULN_CLASS_QUOTA={VULN_CLASS_QUOTA}")


chk("产量熔断阈值可配", t_quota_const)


def t_class_unified():
    """同义类型必须归同一桶，否则熔断失效。"""
    from app.dedup import normalize_vuln_type as n
    pairs = [("SQL注入", "sqli"), ("默认口令", "弱口令"), ("认证绕过", "unauthorized_access"),
             ("签名绕过", "伪造sign"), ("RCE", "rce")]
    bad = [(a, b) for a, b in pairs if n(a) != n(b)]
    return (not bad, "同义归同桶" if not bad else f"不一致: {bad}")


chk("同义类型归同桶", t_class_unified)


def t_quota_logic():
    from app.agents.worker import VULN_CLASS_QUOTA, Worker

    class F:
        def __init__(self, t, v):
            self.title = t
            self.vuln_type = v
            self.evidence = {}

    w = Worker.__new__(Worker)
    w._class_hits = {}
    hits = []
    for i in range(4):
        f = F(f"sql 变体{i}", "SQL注入")
        cls = w._vuln_class_of(f)
        w._class_hits[cls] = w._class_hits.get(cls, 0) + 1
        hits.append(w._class_hits[cls] >= VULN_CLASS_QUOTA)
    # 前 n-1 条不封顶，第 n 条起封顶
    expect = [False] * (VULN_CLASS_QUOTA - 1) + [True] * (4 - VULN_CLASS_QUOTA + 1)
    return (hits == expect, f"封顶序列={hits}")


chk("第N条起封顶", t_quota_logic)


def t_deepen_flag():
    src = open("/app/app/agents/worker.py", encoding="utf-8").read()
    ok = "deepen_suggested" in src and "_report_deepen_suggestion" in src
    return (ok, "深挖标记已实现" if ok else "缺失")


chk("可深挖标记", t_deepen_flag)


def t_deepen_api():
    src = open("/app/app/api/findings.py", encoding="utf-8").read()
    ok = "/results/{finding_id}/deepen" in src
    return (ok, "深挖接口存在" if ok else "缺失")


chk("深挖接口", t_deepen_api)


def t_archived_exposes():
    src = open("/app/app/api/findings.py", encoding="utf-8").read()
    ok = 'd["deepen_suggested"]' in src
    return (ok, "归档接口暴露标记" if ok else "缺失")


chk("归档接口暴露深挖标记", t_archived_exposes)


# 原有保证不能破
def t_archived_no_super():
    src = open("/app/app/api/findings.py", encoding="utf-8").read()
    i = src.find("async def archived_list")
    j = src.find("async def", i + 10)
    return ('Finding.status != "superseded"' not in src[i:j], "归档未过滤 superseded")


chk("【回归】归档不过滤", t_archived_no_super)


def t_dedup_still():
    from app import dedup
    u = "https://x.com/a"
    a = dedup.fingerprint(u, {"title": "弱口令", "vuln_type": "默认口令"})
    b = dedup.fingerprint(u, {"title": "弱口令接管", "vuln_type": "弱口令"})
    c = dedup.fingerprint(u, {"title": "SQL", "vuln_type": "SQL注入"})
    return (a.key == b.key and a.key != c.key, "去重仍正常")


chk("【回归】去重", t_dedup_still)


def t_cluster_still():
    from app.cluster import build_clusters
    items = [
        {"id": "1", "title": "A 弱口令 admin/admin123", "vuln_type": "默认口令",
         "target_url": "https://a.com/l", "severity_claimed": "高危", "poc": "c"},
        {"id": "2", "title": "A 弱口令接管", "vuln_type": "弱口令",
         "target_url": "https://a.com/l", "severity_claimed": "严重", "poc": "c"},
    ]
    return (len(build_clusters(items)) == 1, "聚类仍正常")


chk("【回归】聚类", t_cluster_still)

print("=" * 80)
for n, o, d in R:
    print(f"{n:<26}{'PASS' if o else 'FAIL':<7}{d}")
print("-" * 80)
print(f"通过 {sum(1 for _, o, _ in R if o)}/{len(R)}")
