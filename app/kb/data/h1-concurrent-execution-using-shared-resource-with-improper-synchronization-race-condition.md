# HackerOne 实战案例：concurrent-execution-using-shared-resource-with-improper-synchronization-race-condition

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Race Condition Enables Bypassing Verification Check
- 等级：High | 项目：Tools | 披露：2024-04-04 | CVE：-
- 原文：https://hackerone.com/reports/2110030

- - - - - - - - 
A race condition was discovered in the WorldID platform that could enable bypassing the verification check limits under certain conditions. The issue resided in the enforcement of maximum allowed verifications, which was not properly synchronized across parallel requests to the cloud backend service.
The fix implemented enforcement of the maximum verifications in the database, making it the source of truth for state. This ensures that only one successful request per nullifier use can occur, even if parallel requests are attempted simultaneously. The vulnerability only affected certain cloud-backed verification flows, not on-chain WorldID applications.
---

