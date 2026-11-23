"""task_events 归档：只删日志，不碰任何业务数据。

安全边界（重要）：
- 只操作 `task_events` 一张表。漏洞在 `findings` / `reviews`，目标在 `targets`，
  情报在 `intel`，通杀在 `killsweeps` —— 这些表**一行都不动**。
- task_events 是纯审计日志（谁在什么时候发起了什么事件），删掉不影响任何
  漏洞数据、复审状态、通杀结果、报告内容。
- 保守策略：只删「老于保留天数」且「非 error/warn 级」的 info 事件；
  error/warn 是排障依据，保留更久（ERROR_WARN_EXTRA_DAYS）。
- 先在日志里报告将删多少行，再删；可 dry-run。
"""

from __future__ import annotations

import asyncio
import logging
import os
from datetime import timedelta

from sqlalchemy import delete, func, select

from app.db.models import TaskEvent, _now
from app.db.session import SessionLocal

logger = logging.getLogger(__name__)

# 普通 info 事件的保留天数（默认 7 天，控制库体积：一天约 6k 行，7 天约 4.5 万行）
EVENT_RETENTION_DAYS = int(os.environ.get("EVENT_RETENTION_DAYS", "7"))
# error/warn 事件额外多保留的天数（默认再多 23 天，共 30 天，留足排障窗口）
EVENT_ERROR_WARN_EXTRA_DAYS = int(os.environ.get("EVENT_ERROR_WARN_EXTRA_DAYS", "23"))
# 清理间隔（小时）。保留窗口只有 7 天，用 6h 跑一次，过期数据最多滞留 6 小时。
EVENT_CLEANUP_INTERVAL_HOURS = int(os.environ.get("EVENT_CLEANUP_INTERVAL_HOURS", "6"))
# 单次最多删多少行，避免大事务长时间锁库（影响挖掘）
EVENT_CLEANUP_BATCH = int(os.environ.get("EVENT_CLEANUP_BATCH", "5000"))


async def prune_task_events(dry_run: bool = False) -> dict:
    """按保留策略删除过期 task_events。返回统计。

    只删 task_events，不触碰 findings/reviews/targets/intel/killsweeps。
    """
    now = _now()
    info_cutoff = now - timedelta(days=max(1, EVENT_RETENTION_DAYS))
    err_cutoff = now - timedelta(days=max(1, EVENT_RETENTION_DAYS + EVENT_ERROR_WARN_EXTRA_DAYS))

    async with SessionLocal() as session:
        total = (await session.execute(select(func.count()).select_from(TaskEvent))).scalar() or 0

        # 待删条件：要么是 info 且早于 info_cutoff，要么是 error/warn 且早于 err_cutoff
        n_info = (await session.execute(
            select(func.count()).select_from(TaskEvent).where(
                TaskEvent.level.not_in(["error", "warn"]),
                TaskEvent.ts < info_cutoff,
            )
        )).scalar() or 0
        n_err = (await session.execute(
            select(func.count()).select_from(TaskEvent).where(
                TaskEvent.level.in_(["error", "warn"]),
                TaskEvent.ts < err_cutoff,
            )
        )).scalar() or 0
        to_delete = n_info + n_err

        result = {
            "total": total,
            "info_expired": n_info,
            "error_warn_expired": n_err,
            "to_delete": to_delete,
            "deleted": 0,
            "dry_run": dry_run,
        }
        if dry_run or to_delete == 0:
            return result

        # 分批删，避免长时间持有写锁影响挖掘
        deleted = 0
        while deleted < to_delete:
            ids = (await session.execute(
                select(TaskEvent.id).where(
                    (TaskEvent.level.not_in(["error", "warn"]) & (TaskEvent.ts < info_cutoff))
                    | (TaskEvent.level.in_(["error", "warn"]) & (TaskEvent.ts < err_cutoff))
                ).limit(EVENT_CLEANUP_BATCH)
            )).scalars().all()
            if not ids:
                break
            await session.execute(delete(TaskEvent).where(TaskEvent.id.in_(ids)))
            await session.commit()
            deleted += len(ids)
            await asyncio.sleep(0.05)  # 让出写锁，别憋死正在写事件的 worker
        result["deleted"] = deleted
        return result


async def run_periodic_event_cleanup() -> None:
    """定时归档任务事件日志。与工作目录清理独立。"""
    interval = max(1, EVENT_CLEANUP_INTERVAL_HOURS) * 3600
    logger.info(
        "事件日志归档已启动: 间隔 %dh, info 保留 %dd, error/warn 保留 %dd",
        EVENT_CLEANUP_INTERVAL_HOURS,
        EVENT_RETENTION_DAYS,
        EVENT_RETENTION_DAYS + EVENT_ERROR_WARN_EXTRA_DAYS,
    )
    while True:
        try:
            await asyncio.sleep(interval)
            r = await prune_task_events()
            if r["deleted"]:
                logger.info(
                    "事件日志归档完成: 删 %d 行（原 %d 行，info 过期 %d，error/warn 过期 %d）",
                    r["deleted"], r["total"], r["info_expired"], r["error_warn_expired"],
                )
        except asyncio.CancelledError:
            logger.info("事件日志归档已停止")
            break
        except Exception:
            logger.exception("事件日志归档异常")
