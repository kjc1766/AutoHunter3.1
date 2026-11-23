# HackerOne 实战案例：improper-handling-of-url-encoding-hex-encoding

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Cache Poisoning
- 等级：High | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-12520,
- 原文：https://hackerone.com/reports/824753

- - - - - - - - 
## Summary:
An attacker can cause Squid to return to the user attacker controlled data, for any domain. From Squid-4.7 and below both HTTPS and FTP could be poisoned. This is due to Squid URL decoding parts of the Request URL and using that to create a hash. Request that decode to the same URL will retrieve the same cached response even if they're from different domains. 
The fix for  CVE-2019-12524 removed the HTTPS aspect of it, but FTP poisoning was still possible till Squid-4.10. 
<= Squid-4.9 Vulnerable
<= Squid-4.7 Can also poison HTTPS was reduced to just FTP 
Assigned CVE-2019-12520
No Announce was officially made by Squid, and was silently fixed with Squid-4.10. Thi

