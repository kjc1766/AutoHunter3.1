# HackerOne 实战案例：external-control-of-file-name-or-path

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Arbitrary Configuration File Inclusion: via External Control of File Name or Path
- 等级：Critical | 项目：curl | 披露：2025-11-10 | CVE：-
- 原文：https://hackerone.com/reports/3418646

- - - - - - - - 
## Summary:
The Arbitrary Configuration File Inclusion (ACFI) vulnerability was identified in the curl utility via the --config <file> option. This flaw is a form of External Control of File Name or Path (CWE-73), occurring due to the lack of adequate validation on the user-supplied configuration file path.
An attacker can leverage this weakness to:
Trick a user into executing curl with a malicious configuration file located at an arbitrary path (e.g., /tmp/malicious.curlrc).
Significantly control curl's behavior, including setting dangerous options such as url = "file:///" and output = "...".
The impact is Critical, potentially allowing the attacker to perform a Local File 

