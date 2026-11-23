# HackerOne 实战案例：missing-authentication-for-critical-function

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Authentication bypass  for  ███  leads to  take over any users account.
- 等级：Critical | 项目：Krisp | 披露：2022-10-31 | CVE：-
- 原文：https://hackerone.com/reports/1608151

- - - - - - - - 
@n0_m3rcy has identified and reported an account takeover issue which required no user interaction.
We would like to thank @n0_m3rcy for reporting it responsibly to our bug bounty program !
---


## Token leak in security challenge flow allows retrieving victim's PayPal email and plain text password
- 等级：High | 项目：PayPal | 披露：2020-01-08 | CVE：-
- 原文：https://hackerone.com/reports/739737

- - - - - - - - 
A bug was identified whereby sensitive, unique tokens were being leaked in a JS file used by the recaptcha implementation. In certain cases, a user must solve a CAPTCHA challenge after authenticating. When the security challenge is completed, the authentication request is replayed to log in. The exposed tokens were used in the POST request to solve the CAPTCHA.
The researcher identified a method by which a user, starting from a malicious site, could expose the security challenge token to a third party via a cross-site script inclusion (XSSI) attack. If the user then followed a login link from the malicious site and entered their credentials, the malicious third party could c

