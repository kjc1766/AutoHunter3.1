# HackerOne 实战案例：null-pointer-dereference

_6 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## NULL Pointer dereference in idn.c
- 等级：Critical | 项目：curl | 披露：2023-09-20 | CVE：-
- 原文：https://hackerone.com/reports/2171309

- - - - - - - - 
## Summary:
A NULL Pointer dereference vulnerability is present in idn.c source code.
This module is responsible of handling international domain name.
This issue was found performing manual source code review of Curl which took >20 hours.
## Steps To Reproduce:
Find below a detailed and commented execution flow / code snippet explanation.
## Impact 
In some circumstances writing or reading memory is possible, which may lead to code execution.


## Denial of Service: nghttp2 use of uninitialized pointer
- 等级：Critical | 项目：Node.js | 披露：2020-02-13 | CVE：-
- 原文：https://hackerone.com/reports/335608

- - - - - - - - 
While investigating https://hackerone.com/reports/335533 and while following the same reproduction steps, I uncovered a bug in nghttp2 that causes use of an uninitialized pointer for an altsvc frameresulting in crash. The error can be easily triggered by a remote attacker by sending malformed ALTSVC and GOAWAY frames to the server, or by a malicious server sending same to the client. For Node.js, the result is a crashed process. The report has been submitted to the nghttp2 author who is working on a fix and is working on a fixed release.
## Impact
Crashing the Node.js process causing a Denial of Service
---


## important: Apache HTTP Server: Crash resulting in Denial of Service in mod_proxy via a malicious request (CVE-2024-38477)
- 等级：High | 项目：Internet | 披露：2024-07-13 | CVE：CVE-2024-38477
- 原文：https://hackerone.com/reports/2585375

- - - - - - - - 
I reported this vulnerability through the official Apache HTTP Server security email on April 1, 2024, and received a fix along with a CVE number on July 1, 2024. You can check detailed information from there:
> https://httpd.apache.org/security/vulnerabilities_24.html
## Impact
null pointer dereference in mod_proxy in Apache HTTP Server 2.4.59 and earlier allows an attacker to crash the server via a malicious request.
Users are recommended to upgrade to version 2.4.60, which fixes this issue.
###important: Apache HTTP Server: Crash resulting in Denial of Service in mod_proxy via a malicious request (CVE-2024-38477)
null pointer dereference in mod_proxy in Apache HTTP Server


## CVE-2017-10965: Null pointer dereference in Irssi <1.0.4
- 等级：High | 项目：Internet | 披露：2019-10-04 | CVE：CVE-2017-10965
- 原文：https://hackerone.com/reports/247027

- - - - - - - - 
34 days after reading https://irssi.org/2017/05/12/fuzzing-irssi/, I was finally able to trigger a null pointer dereference in irssi 1.0.2. 
Timeline:
Report to vendor: 15 June 2017
Acknowledge by vendor: 15 June 2017
Fixed by vendor: 7 July 2017
Advisory: 
http://seclists.org/oss-sec/2017/q3/80
Patch:
https://github.com/irssi/irssi/commit/5e26325317c72a04c1610ad952974e206
[code omitted]
---


## null pointer dereference and segfault in tile-count-merge
- 等级：High | 项目：Mapbox | 披露：2017-07-11 | CVE：-
- 原文：https://hackerone.com/reports/245221

- - - - - - - - 
This crash was triggered with `642f773 ` while fuzzing `tile-count-merge` with AFL on Debian 8 x64.
`./tile-count-merge -o /dev/null test000`
[code omitted]
---


## null pointer dereference in Sass::Eval::operator()(Sass::Map*)
- 等级：High | 项目：LibSass | 披露：2017-06-08 | CVE：-
- 原文：https://hackerone.com/reports/221287

- - - - - - - - 
Feeding `@P#{(200000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000 0:0)}` to `./sassc -s` triggers this null pointer dereference.
[code omitted]
---

