# HackerOne 实战案例：relative-path-traversal

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## CVE-█████-35813 in █████
- 等级：Critical | 项目：Mars | 披露：2026-02-24 | CVE：CVE-2023-35813
- 原文：https://hackerone.com/reports/2200329

- - - - - - - - 
A security researcher discovered a critical remote code execution vulnerability (CVE-██████-35813) affecting multiple Sitecore products through version 10.3. The vulnerability was exploited through the sitecore_xaml.ashx endpoint using ASP.NET TemplateParser injection, allowing attackers to execute arbitrary code by manipulating the ParseControl function with malicious XAML markup. Initial testing demonstrated successful code execution with a CVSS score of 9.8. The organization successfully applied the Sitecore security patch, and subsequent retesting confirmed the vulnerability was fully remediated. We appreciate the thorough documentation and responsible disclosure of this


## Path Traversal in SFTP QUOTE command leads to Arbitrary File Write and potential RCE
- 等级：Critical | 项目：curl | 披露：2025-08-10 | CVE：-
- 原文：https://hackerone.com/reports/3293177

- - - - - - - -

