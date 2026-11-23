# HackerOne 实战案例：reliance-on-untrusted-inputs-in-a-security-decision

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Helpdesk Takeover at dmc.datastax.com
- 等级：High | 项目：DataStax | 披露：2020-01-15 | CVE：-
- 原文：https://hackerone.com/reports/759454

- - - - - - - - 
## Summary:
DNS record [dmc.datastax.com](dmc.datastax.com) is pointing to stale [dmc-support.zendesk.com](dmc-support.zendesk.com) domain on Zendesk which is available for takeover.
DNS Stale Records: {F661014}
## Proof of Concept:
There was no helpdesk configured at this address, which means that the address was available and anyone could claim it. I was able to claim dmc-support.zendesk.com.
On this page, https://dmc.datastax.com/hc/en-us I haven't made the page public, I'm attaching a screenshot of the webpage:
{F661004} 
## Supporting Material/References:
Login page:
{F661021}
## Impact
Subdomain takeover
---

