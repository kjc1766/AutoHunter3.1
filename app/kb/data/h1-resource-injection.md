# HackerOne 实战案例：resource-injection

_3 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Zero-amount miner TX + RingCT allows monero wallet to receive arbitrary amount of monero
- 等级：Critical | 项目：Monero | 披露：2019-07-03 | CVE：-
- 原文：https://hackerone.com/reports/501585

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!
**Summary:** 
By mining a specially crafted block, that still passes daemon verification an attacker can create a miner transaction that appears to the wallet to include sum of XMR picked by the attacker. It is our belief that this can be exploited to steal money from exchanges.
**Description:** 
I'm the lead developer of CUT coin (https://github.com/cutcoin/cutcoin), a coin based on Monero codebase.


## Content injection in Jira issue title enabling sending arbitrary POST request as victim
- 等级：High | 项目：GitLab | 披露：2022-09-22 | CVE：CVE-2022-1940
- 原文：https://hackerone.com/reports/1533976

- - - - - - - - 
## Summary
The issue described here leads to the same outcome as my previous report, https://hackerone.com/reports/1409788 . So look into that one for further details on the JavaScript gadgets. Also see my report https://hackerone.com/reports/1481207 for a detailed rundown of injections in GitLab.
This time it is the `title` field of Jira issue pages that renders without proper HTML encoding. Leading to HTML and CSS injection. By abusing a script gadget and a browser quirk (tested on Chrome and Firefox) the injection can be escalated into a highly dangerous arbitrary POST request. Depending on the payload, this POST request can lead to account takeover(of OAuth/SAML accounts


## Arbitrary POST request as victim user from HTML injection in Jupyter notebooks
- 等级：High | 项目：GitLab | 披露：2022-05-20 | CVE：-
- 原文：https://hackerone.com/reports/1409788

- - - - - - - -

