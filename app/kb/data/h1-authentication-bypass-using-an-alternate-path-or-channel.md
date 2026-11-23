# HackerOne 实战案例：authentication-bypass-using-an-alternate-path-or-channel

_12 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Ability to Add and Verify Uncontrolled Mobile Numbers Leading to Account Takeover (ATO)
- 等级：Critical | 项目：MTN | 披露：2025-03-04 | CVE：-
- 原文：https://hackerone.com/reports/2762462

- - - - - - - - 
## Summary
A critical vulnerability was identified in the OTP verification process on the shop.mtn.ng platform, which allows attackers to add and verify mobile numbers that they do not control. By tampering with the OTP verification request, an attacker can link a victim's mobile number to their account. This leads to an Account Takeover (ATO) scenario where the attacker gains full access to the victim's account without owning or controlling the victim's phone number.
## Steps to Reproduce


## Authentication Bypass Leads To  Complete Account TakeveOver on ██████████
- 等级：Critical | 项目：MTN | 披露：2024-09-14 | CVE：-
- 原文：https://hackerone.com/reports/1709881

- - - - - - - - 
## Summary:
Hello Team,
When an invalid email address/password is entered, the Web Application will not authenticate the user. But nevertheless, it is conceivable for an attacker to get around authentication and log in as anyone else, leading to Complete Account Takeover.
## Steps To Reproduce:
Create Two Test Account (Attacker & Victim)
Using attacker's account, login at ███████ 
1. Capture request with Burp. 
2. Without sending request to "Burp Repeater",  modify attacker's email to victim's email. For example REDACTED+██████ to  REDACTED+█████. 
3. Change the param `value:false`, to  `value:true,` and click send. 
4. Notice, attacker has successfully bypassed the authenti


## Account Takeover via Authentication Bypass in TikTok Account Recovery
- 等级：Critical | 项目：TikTok | 披露：2024-07-13 | CVE：-
- 原文：https://hackerone.com/reports/2443228

- - - - - - - - 
An improper authentication mechanism in TikTok's account recovery process could have been used for account takeovers on Android devices. There was no evidence of exploitation and this vulnerability has now been completely fixed. We thank @xtt0k for reporting this to our team and confirming its remediation.
**Summary (researcher):**
I identified a critical vulnerability in one of TikTok's endpoints that permitted unauthorized changes to user accounts due to improper parameter handling. This flaw could have allowed a TikTok account to be taken over by knowing the account username. I appreciate TikTok's swift action in resolving this issue and their generous bounty.
---


## Authentication bypass in ████████
- 等级：Critical | 项目：MTN | 披露：2022-12-02 | CVE：-
- 原文：https://hackerone.com/reports/1747146

- - - - - - - - 
## Summary:
In a nutshell, an authentication bypass exploits weak authentication mechanisms to allow a hacker to access your systems and data.In a nutshell, an authentication bypass exploits weak authentication mechanisms to allow a hacker to access your systems and data
## Steps To Reproduce:
  1.I was going to the site: █████ and on the home page I clicked on personal and the site redirected me to another site which is: ██████████ and on this site on which I was redirected I saw "link your NIN" and I went to this site and after listing I found an impressive thing which is the Tiny filemanager and to authenticate myself I bypass it with default credentials to access it.
The


## Mass Account Takeover at https://app.taxjar.com/ - No user Interaction
- 等级：Critical | 项目：Stripe | 披露：2022-07-11 | CVE：-
- 原文：https://hackerone.com/reports/1581240

- - - - - - - - 
@beerboy_ankit discovered an IDOR in the user invite link in Taxjar. This could have allowed an attacker to take over a user's account. The vulnerability was caused by a leaked token in the delete invitation request feature and resolved by using the invitation ID instead of the token to look up the user’s invite when deleting an invitation. Validation was added to ensure the ID belongs to the user’s organization.
---


## Cache Manager ACL Bypass
- 等级：Critical | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-12524
- 原文：https://hackerone.com/reports/824203

- - - - - - - - 
## Summary:
ACL Manager can be bypassed giving non authorized users to squid-internal-mgr.
Possible to bypass other url_regex, but only focused on manager. 
<= Squid-4.7 vulnerable
Silently Fixed in Squid-4.8 
Announce page was allocated, but never made http://www.squid-cache.org/Advisories/SQUID-2019_4.txt As another issue similar to this wasn't fixed 
Patch: http://www.squid-cache.org/Versions/v4/changesets/squid-4-e1e861eb9a04137fe81decd1c9370b13c6f18a18.patch
Assigned: CVE-2019-12524
## Steps To Reproduce:
1) Start squid-4.7
[code omitted]
2) Issue the following request replacing <hostname> with the hostname of the server running squid
[code omitted]
[code omitted]
You s


## Other misconfiguration on Slack Server
- 等级：Critical | 项目：ImpressCMS | 披露：2021-01-04 | CVE：-
- 原文：https://hackerone.com/reports/1039325

- - - - - - - - 
Other misconfiguration on Slack Server
---


## Two-factor authentication (2FA) Bypass
- 等级：Critical | 项目：BlockDev | 披露：2020-01-15 | CVE：-
- 原文：https://hackerone.com/reports/708303

- - - - - - - - 
Bypassing 2FA after activating it on the company forum.
---


## Admin panel take over | User info leakage | Mass Comprimise
- 等级：Critical | 项目：U.S. | 披露：2019-10-08 | CVE：-
- 原文：https://hackerone.com/reports/428757

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
**Summary:** [add summary of the vulnerability]
I'm able to take over the admin panel, allowing me to viewing the entire ticket database's PII (DOD ID, email, name by changing the URL and bypassing authentication
**Description:** [add more details about this vulnerability]
## Steps To Reproduce:
1: Go to
████████?x-app=itsm&x-urlpath=/arsys/shared/login.jsp&x-redir=%2Farsys%2Fforms%2Fedgelb-itsm-ar%2FRKM%253AKnowled


## Mass Accounts Takeover Without any user Interaction  at https://app.taxjar.com/
- 等级：High | 项目：Stripe | 披露：2022-10-19 | CVE：-
- 原文：https://hackerone.com/reports/1685970

- - - - - - - - 
@mr_asg discovered an improper access control issue in TaxJar. This could have allowed for account takeover using the email change functionality. The vulnerability was caused by not correctly validating whether or not the reset password token was connected to the user being reset and was resolved by relying on the user fetched from the reset password token itself instead of the account ID provided in the URL.
**Summary (researcher):**
I discovered an IDOR in the Accountant Access form in Taxjar. This could have allowed an attacker to take over any user's account. The vulnerability was caused by  manipulating the user's number in the POST request to `/accounts/<ACCOUNT_NUMBER


## Unauthorized access to employee panel with default credentials.
- 等级：High | 项目：U.S. | 披露：2021-11-13 | CVE：-
- 原文：https://hackerone.com/reports/1063298

- - - - - - - - 
## Summary:
Hello, 
When hunting for your web application.
I have managed to go https://cars.fas.gsa.gov/cars/cars and get displayed with a form.
I have already tried to login to Cars and without success.
However i've noticed the loginChk() function and change the value of the form hence bypassing it and logging in succesfuly.
## Steps To Reproduce:
  1. go to https://cars.fas.gsa.gov/cars/cars
  2. type loginChk()  function in console. 
  3. It would return false. 
  4. Now  type in console ( can be opened using F12). 
       document.forms[0].scSelCen.value = "admin"
  5. Now try to login by clicking on CARS button.
## Supporting Material/References:
Navigator used : googl


## Ability to bypass email verification for OAuth grants results in accounts takeovers on 3rd parties
- 等级：High | 项目：GitLab | 披露：2020-10-01 | CVE：-
- 原文：https://hackerone.com/reports/922456

- - - - - - - -

