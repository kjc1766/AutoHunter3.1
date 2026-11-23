# HackerOne 实战案例：reflected-xss

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Reflected XSS on Amazon EC2 Instance
- 等级：High | 项目：AWS | 披露：2024-12-24 | CVE：CVE-2022-29548
- 原文：https://hackerone.com/reports/2787650

- - - - - - - - 
Product: Amazon Elastic Compute Cloud (Amazon EC2)
Vulnerability Type:  Reflected Cross-Site Scripting (XSS)
CVE: CVE-2022-29548
Severity:  Medium
Description:
 A reflected XSS vulnerability was discovered on the Amazon EC2 instance, allowing an attacker to inject malicious JavaScript code, potentially leading to unauthorized access to sensitive data or system compromise.
Proof of Concept:
URL: ███████);alert(document.domain)//
## Impact
## The payload is injected into the errorCode parameter, which is reflected back to the user without proper validation or sanitization. This allows an attacker to execute arbitrary JavaScript code in the context of the vulnerable page
---

