# HackerOne 实战案例：cleartext-transmission-of-sensitive-information

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Insecure WebSocket Usage in curl Documentation and Examples (CWE-319: Cleartext Transmission of Sensitive Information)
- 等级：High | 项目：curl | 披露：2025-08-12 | CVE：-
- 原文：https://hackerone.com/reports/3295652

- - - - - - - - 
The curl source repository contains official documentation and example code that demonstrate WebSocket connections using the insecure ws:// protocol instead of the secure wss://. This misleading guidance may encourage developers to implement cleartext WebSocket endpoints, exposing users and infrastructure to eavesdropping, MITM (Man-in-the-Middle) attacks, and session hijacking. Failing to promote secure defaults in a popular open-source project creates systemic risks for downstream adopters.
This report and its analysis were enhanced and generated using an AI assistant to ensure a comprehensive security review and reproducibility.
Affected version
Verified on the curl maste


## Plaintext leakage of DNS requests in Windows 1.1.1.1 WARP client
- 等级：High | 项目：Cloudflare | 披露：2023-08-03 | CVE：CVE-2023-2754
- 原文：https://hackerone.com/reports/1941390

- - - - - - - - 
The Cloudflare WARP client for Windows assigns loopback IPv4 addresses for the DNS Servers, since WARP acts as local DNS server that performs DNS queries in a secure manner, however, if a user is connected to WARP over an IPv6-capable network, te WARP client did not assign loopback IPv6 addresses but Unique Local Addresses, which under certain conditions could point towards unknown devices in the same local network which enables an Attacker to view DNS queries made by the device.
---


## Leak of Google Sheets API credentials
- 等级：High | 项目：Azbuka | 披露：2021-11-15 | CVE：-
- 原文：https://hackerone.com/reports/965314

- - - - - - - - 
Closed.
---


## Reflected XSS and sensitive data exposure, including payment details, on lioncityrentals.com.sg
- 等级：High | 项目：Uber | 披露：2020-04-30 | CVE：-
- 原文：https://hackerone.com/reports/340431

- - - - - - - - 
lioncityrentals.com.sg employed a Wordpress installation that possessed a vulnerable plugin, Formidable Forms, which was vulnerable to reflected XSS, and exposed sensitive form data. 
Thanks again for the report, @healdb!
**Summary (researcher):**
This was the first bug I ever found that exposed a large amount of PII, thanks for disclosing @uber! 
This bug reinforces to me that hackers should always examine microsites as well as core domains, sometimes bugs on microsites can lead to significant data exposure. In this case, lioncityrentals.com.sg  was collecting data on thousands of Uber Singapore users, which was then exposed by the outdated Wordpress plugin. 
You can read m


## Login form on non-HTTPS page
- 等级：High | 项目：Rockstar | 披露：2017-04-26 | CVE：-
- 原文：https://hackerone.com/reports/214571

- - - - - - - - 
Summary:
=======
A page on a microsite is not fully protected by an SSL certificate. This could allow an attacker in a Man-in-the-Middle position to obtain usernames and passwords of users visiting the site. 
Description:
=======
On the Red Dead Redemption subpage, the comments section on news articles allows registered social club users to post comments. When posting a comment, the user first has to login, which appears as if it is done over a non-secure page:
http://www.rockstargames.com/reddeadredemption/news/article/52645/rockstar-fan-art-gallery-gta-in-a-bottle-8-bit-bully-red.html/#comments
Note the warning in screenshot 1, firefox has identified that this page is not 

