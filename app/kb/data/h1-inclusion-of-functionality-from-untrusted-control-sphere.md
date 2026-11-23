# HackerOne 实战案例：inclusion-of-functionality-from-untrusted-control-sphere

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## important: Apache HTTP Server may use exploitable/malicious backend application output to run local handlers via internal redirect (CVE-2024-38476)
- 等级：High | 项目：Internet | 披露：2024-07-13 | CVE：CVE-2024-38476
- 原文：https://hackerone.com/reports/2585376

- - - - - - - - 
I reported this vulnerability through the official Apache HTTP Server security email on April 1, 2024, and received a fix along with a CVE number on July 1, 2024. You can check detailed information from there:
> https://httpd.apache.org/security/vulnerabilities_24.html
## Impact
Vulnerability in core of Apache HTTP Server 2.4.59 and earlier are vulnerably to information disclosure, SSRF or local script execution via backend applications whose response headers are malicious or exploitable.
Note: Some legacy uses of the 'AddType' directive to connect a request to a handler must be ported to 'SetHandler' after this fix.
Users are recommended to upgrade to version 2.4.60, which 

