# HackerOne 实战案例：file-content-injection

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## DNN - Unrestricted Arbitrary File Upload #████████
- 等级：Critical | 项目：U.S. | 披露：2026-01-12 | CVE：CVE-2025-64095
- 原文：https://hackerone.com/reports/3414079

- - - - - - - - 
**Description:**
DNN (formerly DotNetNuke) \u003C 10.1.1 contains an unrestricted file upload vulnerability caused by the default HTML editor provider allowing unauthenticated file uploads and overwriting existing files, letting unauthenticated attackers deface websites and inject XSS payloads, exploit requires no authentication.
## References
https://nvd.nist.gov/vuln/detail/CVE-2025-64095
## Impact
Unauthenticated attackers can upload and overwrite files, leading to website defacement and cross-site scripting attacks.
## System Host(s)
█████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
#Vulnerable subdomain
https://██████████/Providers/HtmlEdi

