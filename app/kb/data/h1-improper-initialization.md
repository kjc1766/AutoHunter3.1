# HackerOne 实战案例：improper-initialization

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Timeout-based race conditions make Uint8Array/Buffer.alloc non-zerofilled
- 等级：High | 项目：Node.js | 披露：2026-02-12 | CVE：CVE-2025-55131
- 原文：https://hackerone.com/reports/3405778

- - - - - - - - 
A flaw in Node.js's buffer allocation logic can expose uninitialized memory when allocations are interrupted, when using the `vm` module with the timeout option. Under specific timing conditions, buffers allocated with `Buffer.alloc` and other `TypedArray` instances like `Uint8Array` may contain leftover data from previous operations, allowing in-process secrets like tokens or passwords to leak or causing data corruption. While exploitation typically requires precise timing or in-process code execution, it can become remotely exploitable when untrusted input influences workload and timeouts, leading to potential confidentiality and integrity impact.
---

