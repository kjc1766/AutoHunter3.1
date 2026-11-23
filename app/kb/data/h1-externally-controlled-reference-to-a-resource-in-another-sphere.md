# HackerOne 实战案例：externally-controlled-reference-to-a-resource-in-another-sphere

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Subdomain takeover of v.zego.com
- 等级：High | 项目：Zego | 披露：2021-06-26 | CVE：-
- 原文：https://hackerone.com/reports/1180697

- - - - - - - - 
## Summary
v.zego.com points to an AWS EC2 instance at 52.214.138.192 that no longer exists. I was able to take control of this IP address and run my own EC2 instance. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.
If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.


## Subdomain takeover of mydailydev.starbucks.com
- 等级：High | 项目：Starbucks | 披露：2019-05-22 | CVE：-
- 原文：https://hackerone.com/reports/570651

- - - - - - - - 
A subdomain of `starbucks.com` had a CNAME record pointing to an Azure Traffic Manager profile that @0xpatrik was able to claim.
---

