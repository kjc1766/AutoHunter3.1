# HackerOne 实战案例：file-and-directory-information-exposure

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://████
- 等级：Critical | 项目：U.S. | 披露：2021-07-29 | CVE：CVE-2019-11510,
- 原文：https://hackerone.com/reports/695005

- - - - - - - - 
##Description
Hello. Some time ago, researcher Orange Tsai from DEVCORE team had a talk on Defcon/BlackHat regarding Pulse Secure SSL VPN vulnerabilities fixed on 2019/4/25:
**CVE-2019-11510 - Pre-auth Arbitrary File Reading**
CVE-2019-11542 - Post-auth Stack Buffer Overflow
**CVE-2019-11539 - Post-auth Command Injection**
CVE-2019-11538 - Post-auth Arbitrary File Reading
**CVE-2019-11508 - Post-auth Arbitrary File Writing**
CVE-2019-11540 - Post-auth Session Hijacking
Link to the slides: https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf
I discovered that `https://██████████` instance is vulnerable to described vulnerabilities.
#


## Open FTP server on a DoD system
- 等级：High | 项目：U.S. | 披露：2019-10-08 | CVE：-
- 原文：https://hackerone.com/reports/192321

- - - - - - - - 
**Summary:**
I don't know if this qualifies but during my search I discovered an open FTP panel that I was able to successfully log into.   
Using any FTP program,  I used File zilla and then entered ████  as my host then connected. Then I was able to look through any of the files. I noticed the last modified file was  quite recent leading me to believe it's still in us
**Summary (researcher):**
An open FTP panel was discovered which allowed any attackers to connect and upload their files. Initial probing discovered it was still being used by multiple people confirming this was still in use.
---

