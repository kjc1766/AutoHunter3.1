# HackerOne 实战案例：untrusted-search-path

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Node.js - DLL Hijacking on Windows
- 等级：High | 项目：Internet | 披露：2022-07-25 | CVE：-
- 原文：https://hackerone.com/reports/1636566

- - - - - - - - 
Full Node.js Security Releases  - summarizing the issue is here:https://nodejs.org/en/blog/vulnerability/july-2022-security-releases/
The original Node.js HackerOne report is here: https://hackerone.com/bugs?report_id=1447455
-----
Node.js versions earlier than 16.16.0 (LTS) and 14.20.0 are vulnerable to dynamic link library (DLL) hijacking.
Attackers can exploit this vulnerability to escalate their privileges and establish persistence in a target environment.
The vulnerability can also provide another way to embed malicious code into packages.
This vulnerability can be exploited if the victim has the following dependencies on Windows machine:
* OpenSSL has been installed or

