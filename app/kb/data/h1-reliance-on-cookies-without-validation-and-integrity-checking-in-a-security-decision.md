# HackerOne 实战案例：reliance-on-cookies-without-validation-and-integrity-checking-in-a-security-decision

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Отправка писем с произвольным текстом/кликабельными ссылками любому зарегистрированному пользователю с указанной почтой, зная только steamid
- 等级：Critical | 项目：CS | 披露：2020-12-20 | CVE：-
- 原文：https://hackerone.com/reports/993711

- - - - - - - - 
Using a third-party service `GetResponse` used on the project and the 2FA deactivation functionality combined, a hacker found a way to send **arbitrary text** to **any** user, knowing only the victim's SteamID.
*The vulnerability relied on:*
1. Invalid cookie management in request;
1. No additional validation for email ownership.
---


## Ruby CVE-2021-41819: Cookie Prefix Spoofing in CGI::Cookie.parse
- 等级：High | 项目：Internet | 披露：2022-02-03 | CVE：CVE-2021-41819,
- 原文：https://hackerone.com/reports/1464396

- - - - - - - - 
Release note: https://www.ruby-lang.org/en/news/2021/11/24/cookie-prefix-spoofing-in-cgi-cookie-parse-cve-2021-41819/
> The old versions of CGI::Cookie.parse applied URL decoding to cookie names. An attacker could exploit this vulnerability to spoof security prefixes in cookie names, which may be able to trick a vulnerable application.
> By this fix, CGI::Cookie.parse no longer decodes cookie names. Note that this is an incompatibility if cookie names that you are using include non-alphanumeric characters that are URL-encoded.
> This is the same issue of CVE-2020-8184.
---
The following is copied from hackerone's report. https://hackerone.com/reports/910552
I found the same 

