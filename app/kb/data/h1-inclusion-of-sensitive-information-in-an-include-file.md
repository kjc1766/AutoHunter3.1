# HackerOne 实战案例：inclusion-of-sensitive-information-in-an-include-file

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Critical Information Disclosure via /talos/api/v1/files/upload
- 等级：Critical | 项目：Bykea | 披露：2025-09-17 | CVE：-
- 原文：https://hackerone.com/reports/3228011

- - - - - - - - 
@sameer_ali discovered a vulnerability in the file upload functionality where uploaded files were first stored on the server before being sent to S3. Due to a configuration  flaw, memory chunks from the server were included in some uploaded files. This issue was classified as Critical and was addressed as a priority.
---

