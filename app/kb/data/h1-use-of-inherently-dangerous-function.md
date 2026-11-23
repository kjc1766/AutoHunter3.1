# HackerOne 实战案例：use-of-inherently-dangerous-function

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Unexpected input validation of octal literals in nodejs v15.12.0 and below returns defined values for all undefined octal literals.
- 等级：Critical | 项目：Node.js | 披露：2021-06-14 | CVE：CVE-2021-28918,
- 原文：https://hackerone.com/reports/1141623

- - - - - - - - 
**Summary:**
 Unexpected input validation of octal literals in the nodejs implementation of V8 JavaScript engine V8 9.0.257.13 and below returns defined values for all undefined octal literals where otherwise should return undefined. Input data 08, 09... 078, 079 should return undefined, as evinced by 0o8, 0o9 etc. This affects ALL downstream nodejs software. An attacker could abuse a myriad of downstream software that relies on nodejs, for example any of the 1,570,041 npm packages that expect an undefined response for `eval(08)`;. One such example is netmask npm package: the package is unable to evaluate any octal literal containing an 8 or a 9 leading to SSRF, LFI, RFI.
**


## URL Spoof / Brave Shield Bypass
- 等级：High | 项目：Brave | 披露：2017-08-31 | CVE：-
- 原文：https://hackerone.com/reports/255991

- - - - - - - - 
## Summary:
Improper URL parsing in Brave allows an attacker to spoof the hostname shield settings are applied to.
## POC:
https://youtu.be/yz99T_Trfuc
## Products affected: 
 * Brave (browser-laptop) 0.18.14 rev ad92d02
## Steps To Reproduce:
 1. Browse to http://brave.com
 2. Click on the Shield icon and toggle the shield from "up" to "down"
 3. Browse to http://brave.com%60x.code-fu.org/ and notice the shield is down for this domain as well. 
I believe this could be used enable flash by spoofing one of the "whitelisted" domains. 
The renderer will load the code-fu.org domain, however I believe when the  URL is later parsed in node it uses (non standards compliant?) url.pa

