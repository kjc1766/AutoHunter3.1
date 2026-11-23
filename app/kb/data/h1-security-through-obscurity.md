# HackerOne 实战案例：security-through-obscurity

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Subdomain takeover of █████████
- 等级：Critical | 项目：U.S. | 披露：2022-09-06 | CVE：-
- 原文：https://hackerone.com/reports/1457928

- - - - - - - - 
I have found a subdomain of `███████` to be vulnerable to takeovers via a CNAME to unclaimed domain. I have claimed this domain and redirected them to a blank page to prevent a bad actor from doing so in the meantime, and hosted a POC file at obscure URLs. These are the following domains I discovered and the outdated endpoints on Azure to which they point:
█████ --> ████
...and the proof-of-concept file is at the following location:
https://████████/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
I have not hosted any other file nor attempted any other vector of attack.
## Impact
You're probably familiar with takeovers like this by now, but through this vulnerability, it woul

