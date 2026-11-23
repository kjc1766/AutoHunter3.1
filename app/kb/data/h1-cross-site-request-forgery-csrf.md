# HackerOne 实战案例：cross-site-request-forgery-csrf

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Revocation API Token by Bypassing The XSRF Token
- 等级：Critical | 项目：Enjin | 披露：2024-01-19 | CVE：-
- 原文：https://hackerone.com/reports/2312217

- - - - - - - - 
@alpernae was able to demonstrate that the [Enjin Platform](https://platform.enjin.io)'s GraphQL interface was missing the appropriate CSRF protection when using a session token.
**Summary (researcher):**
The attack is performed by crafting a malicious HTML form that, when submitted, sends a request to the Enjin platform to revoke the API token. The form is designed to bypass the Cross-Site Request Forgery (CSRF) protection mechanisms in place, such as the XSRF token. This allows the attacker to force the victim's browser to make a request to the Enjin platform on their behalf, leading to the revocation of the API token
---


## CSRF to change password
- 等级：Critical | 项目：Nord | 披露：2022-01-12 | CVE：-
- 原文：https://hackerone.com/reports/204703

- - - - - - - - 
Description 
Cross-Site Request Forgery (CSRF) is a type of attack that occurs when a malicious web site, email, blog, instant message, or program causes a user's web browser to perform an unwanted action on a trusted site for which the user is currently authenticated.
I have found CSRF to change password , 
POC 
<html>
  <body>
    <form action="https://nordvpn.com/profile/" method="POST">
      <input type="hidden" name="tmpl" value="settings" />
      <input type="hidden" name="password" value="password" />
      <input type="hidden" name="password&#95;confirmation" value="password" />
      <input type="submit" value="Submit request" />
    </form>
  </body>
</html>
Than


## CSRF на установку своей почты к аккаунту.
- 等级：Critical | 项目：VK.com | 披露：2021-05-23 | CVE：-
- 原文：https://hackerone.com/reports/301586

- - - - - - - - 
CSRF при привязке почты к странице.
**Summary (researcher):**
ВНИМАНИЕ ВКОНТАКТЕ КИНУЛИ МЕНЯ НА ВЫПЛАТУ И СКАЗАЛИ ЧТО Я ЭКСПЛУАТИРОВАЛ!! КОГДА Я ПОПРОСИЛ ДОКАЗАТЬ ЭТО ОНИ ЗАИГНОРИЛИ И ПРУФОВ С ИХ СТОРОНЫ НЕ ПОСЛЕДОВАЛО..............................
---


## CSRF to account takeover in https://█████/
- 等级：Critical | 项目：U.S. | 披露：2020-11-09 | CVE：-
- 原文：https://hackerone.com/reports/1018270

- - - - - - - - 
Hi DoD team,
I found a CSRF to account takeover in https://███████/
## NOTE:
Try to open the site in firefox because chrome sometimes is not allowing to open the site.
## Summary:
There is no protection against CSRF in changing email which lead to CSRF to account takeover on  https://██████/.
## Step-by-step Reproduction Instructions
## I have made a video POC in which I have shown the account takeover clearly Please do watch for better understanding
1. Login as victim and check your infos in the account details
2. Open the CSRF malicious file which I have attached (csrf_POC.html)
3. Now the email is different (you can also change your name and other fields as well)
4. Now y


## CSRF to account takeover in https://███████.mil/
- 等级：Critical | 项目：U.S. | 披露：2020-10-16 | CVE：-
- 原文：https://hackerone.com/reports/987751

- - - - - - - - 
**Summary:**
Hello 
**Description:**
## Impact
## Step-by-step Reproduction Instructions
1. Go to  https://███.mil/ and login using your credintials
2. Now Click on change password
3. First turn the intercept of burp to on and enter your secondary email id and password and click on register password.
[code omitted]
4: Now send the link to the victims
## Product, Version, and Configuration (If applicable)
██████
## Impact
It is a critical issue as i was able to takeover anyone account using this attack..
---


## Отсутствие CSRF ключа на функции Закрытый Профиль.
- 等级：Critical | 项目：ok.ru | 披露：2020-05-15 | CVE：-
- 原文：https://hackerone.com/reports/448928

- - - - - - - - 
"Friends only" account mode could be toggled on and off with a CSRF attack.
Настройка Закрытый профиль могла быть включена или выключена через CSRF.
---


## CSRF - Modify Project Settings
- 等级：Critical | 项目：Stripo | 披露：2020-02-03 | CVE：-
- 原文：https://hackerone.com/reports/766533

- - - - - - - - 
**Target Url/Endpoint**
https://my.stripo.email/cabinet/stripeapi/v1/projects/{Project_Id}
**Note**
Attacker just need to know victim project Id.
## Summary:
This CSRF Vulnerability leads to change user's project settings including General Information, Contacts, Social Networks and Other Options.
## Steps To Reproduce:
This POC is a simple example on exploiting this bug. Attacker can exploit it with more advanced techniques and can really lead to critical issues.
1. Navigate to Project Settings -> Modify any data and intercept the request, send it to repeater, and do the following.
2. Take the HTML code format from burp suite -> Engagement Tools -> Generate CSRF POC.
3. Put 


## Take over of accounts created using Google or Facebook
- 等级：Critical | 项目：Khan | 披露：2019-05-17 | CVE：-
- 原文：https://hackerone.com/reports/442901

- - - - - - - - 
When a user creates an account using Google or Facebook and does not set an additional password, it is possible to set their passwords via CSRF.
Since the account is created using a social media account, no existing password check is needed and the CSRF check on the endpoint is broken. 
To reproduce, create an account with Google or Facebook and make account load the attached HTML file. You should now be able to login to the account with password=ATTACKER_PASS.
## Impact
An attacker can take over of accounts created using Google or Facebook.
---


## Account takeover by changing email
- 等级：Critical | 项目：Khan | 披露：2019-05-17 | CVE：-
- 原文：https://hackerone.com/reports/538800

- - - - - - - - 
The endpoint `/signup/email` allows users to change their email before they confirm their account email. This endpoint is not protected from CSRF. Thus, any account that is not yet "confirmed" is vulnerable to account takeover using the following steps:
1. Attacker obtains new email address not associated with a KA account.
2. Attacker then lures a new KA user to visit a URL linking to a page that sends a `POST` request to `/signup/email` with the POST body : `casing=camel&email=ATTACKER_EMAIL`.
3. The email change will go through and the attacker would then be able to take over the unconfirmed account using password reset.
4. The original user would not be able to reclaim a


## <- Critical IDOR vulnerability in socialclub allow to insert and delete comments as another user and it discloses sensitive information ->
- 等级：Critical | 项目：Rockstar | 披露：2017-05-24 | CVE：-
- 原文：https://hackerone.com/reports/204292

- - - - - - - - 
In this report, the researcher found an insecure direct object reference that allowed a malicious user to impersonate another user in the comment section under Newswire articles. This meant that an attacker could leave abusive comments that appeared to have been made by another user, or delete a particular victim's previous comments.
This vulnerability had other adverse side effects as well, including information leakage and CSRF.
---


## CSRF leads to Account takeover
- 等级：High | 项目：U.S. | 披露：2024-12-18 | CVE：-
- 原文：https://hackerone.com/reports/2699029

- - - - - - - - 
**Description:**
During my search in this domain I found it vulnerable to CSRF so I tried to escalate it Account takeover and I succeed
## Impact
Account takeover via CSRF
## System Host(s)
███████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Vulnerable domain and endpoint : https://██████████/account/profile/edit
1. Click on this URL: https://█████████/account/register and fill in the required fields.
2. You will be instructed to check your inbox for a verification email, but you can avoid this step and log in using the username and password you created on the registration page.
3. Navigate to this endpoint https://███████/account/profile/edit 


## CSRF leads to Account takeover
- 等级：High | 项目：U.S. | 披露：2024-12-18 | CVE：-
- 原文：https://hackerone.com/reports/2712857

- - - - - - - - 
**Description:**
During my search in this domain I found it vulnerable to CSRF so I tried to escalate it Account takeover and I succeed
## Impact
Account takeover via CSRF
## System Host(s)
█████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Vulnerable domain and endpoint : https://██████/account/profile/edit
1. Click on this URL: https://███/account/register and fill in the required fields.
2. You will be instructed to check your inbox for a verification email, but you can avoid this step and log in using the username and password you created on the registration page.
3. Navigate to this endpoint https://█████/account/profile/edit and attempt to


## CSRF Attack on changing security questions leads to full Account TakeOver
- 等级：High | 项目：U.S. | 披露：2024-12-18 | CVE：-
- 原文：https://hackerone.com/reports/2652603

- - - - - - - - 
**Description:**
Hii, 
While researching https://www.████/, I discovered that an attacker could exploit a CSRF vulnerability to perform a password reset and gain full control of any user's account.
There is a feature in the user profile that allows users to change their security questions and answers. However, when the user changes this information, the application does not verify the CSRF token, resulting in a CSRF vulnerability in that functionality.
Additionally, there is another functionality on the reset password. Users can change their password via the security questions. However, exploiting the previously mentioned vulnerability will lead to bypassing this feature and


## Argo CD CSRF leads to Kubernetes cluster compromise
- 等级：High | 项目：Internet | 披露：2024-01-29 | CVE：-
- 原文：https://hackerone.com/reports/2326194

- - - - - - - - 
GHSA: https://github.com/argoproj/argo-cd/security/advisories/GHSA-92mw-q256-5vwg
It's been publicly known for years that all of Argo CD API is vulnerable to Cross-Site Request Forgery (CSRF). We assume the team haven't made it a priority because of the lack of evidence to support it's a severe vulnerability.
Modern browsers implement the Lax SameSite cookie attribute to prevent CSRF, but it is not foolproof. The samesite attribute is rendered useless if the origin is on the same parent domain as the target.
We spin up a sample environment with Argo CD v2.8.2 to test this. An attacker controls contents of ​​marketing.victim.com (via Stored XSS, for example) and wants to targ


## Cross-Site Request Forgery
- 等级：High | 项目：ownCloud | 披露：2023-11-05 | CVE：-
- 原文：https://hackerone.com/reports/2041007

- - - - - - - - 
The application does not throw a CrossSiteRequestForgeryException, if the request does not contain the requesttoken header.
Steps to reproduce 
- run the docker image "owncloud/server:10.12.2" , redis and mariadb with docker-compose
-  log in the application as an admin user
- insert your cookies in
[code omitted]
and run it.
- Login in the application with the username `new_admin` and the passwort `a`
To add an admin user is only an example. Most if not all requests does not require an CSRF token.
I think the cause of this vulnerability is the second condition of https://github.com/owncloud/core/blob/master/lib/private/AppFramework/Middleware/Security/SecurityMiddleware.php


## Improper CSRF token validation allows attackers to access victim's accounts linked to Hackerone
- 等级：High | 项目：HackerOne | 披露：2023-06-19 | CVE：-
- 原文：https://hackerone.com/reports/1727221

- - - - - - - -


## CSRF Account Takeover
- 等级：High | 项目：TikTok | 披露：2022-08-16 | CVE：-
- 原文：https://hackerone.com/reports/1253462

- - - - - - - - 
A Cross-Site Request Forgery (CSRF) vulnerability was found on a TikTok endpoint which could have resulted in a full account takeover. We thank @s3c for reporting this to our team and confirming its resolution.
---


## CSRF protection bypass in GitHub Enterprise management console
- 等级：High | 项目：GitHub | 披露：2022-04-13 | CVE：CVE-2022-23732
- 原文：https://hackerone.com/reports/1497169

- - - - - - - - 
A path traversal vulnerability was identified in GitHub Enterprise Server management console that allowed the bypass of CSRF protections. This could potentially lead to privilege escalation. To exploit this vulnerability, an attacker would need to target a user that was actively logged into the management console. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.5 and was fixed in versions 3.1.19, 3.2.11, 3.3.6, 3.4.1.
[CVE-2022-23732](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-23732)
---


## 0-day Cross Origin Request Forgery vulnerability in Grafana 8.x .
- 等级：High | 项目：Aiven | 披露：2022-03-16 | CVE：CVE-2022-21703
- 原文：https://hackerone.com/reports/1458236

- - - - - - - - 
## Disclaimer
To triage, please note that this is still a 0-day that was alerted to Grafana already, in order to make sure the client is safe I report this issue now, please make sure to not spread it further or leak it, as the best interest is to let you be aware and safer from any potential attacks in the meantime.
## Description
@jub0bs and I have found a cross-origin request forgery attack issue in the Grafana instances hosted on the Aiven platforms (CVE-2022-21703, which is still a 0-Day CVE on Grafana) . 
With the cross-origin request forgery attack it's possible for an attacker to successfully mount cross-origin request forgery attack against authenticated victims of 


## Widespread CSRF on authenticated POST endpoints
- 等级：High | 项目：UPchieve | 披露：2022-02-13 | CVE：-
- 原文：https://hackerone.com/reports/1309435

- - - - - - - - 
## Summary:
Cross-Site Request Forgery (CSRF) is possible on most, if not all, authenticated POST endpoints.
While CORS is configured such that the Access-Control-Allow-Origin header is set to `Access-Control-Allow-Origin: hackers.upchieve.org`, CORS does **not** prevent CSRF - it only prevents the attacker from reading the response. This does not stop the attacker from performing any arbitrary actions on behalf of the user.
This is possible through a simple HTML form with hidden inputs, submitted with JavaScript. While POST requests are made using JSON data by default, `application/x-www-form-urlencoded` is accepted as well. Because the user's session cookie does not have t


## CSRF in Account Deletion feature (https://www.flickr.com/account/delete)
- 等级：High | 项目：Flickr | 披露：2021-09-14 | CVE：-
- 原文：https://hackerone.com/reports/615448

- - - - - - - - 
CSRF was missing in Account Deletion form due to switching login providers. @asad0x01_ found the vulnerability and reported it concisely, even with a video POC.
The issue was fixed with 60 days, but we were slow to resolve the ticket and disclose.
**Summary (researcher):**
Sometimes you just get lucky. When Flickr was owned by Yahoo, they used to use **Yahoo Authentication system** (https://login.yahoo.com) . When Flickr got sold to  SmugMug, they introduced new login flow (https://identity.flickr.com). Basically in their previous login flow, they used to use the **Yahoo** authentication code as CSRF token while deleting account. While testing the account deletion feature, I


## CSRF on /api/graphql allows executing mutations through GET requests
- 等级：High | 项目：GitLab | 披露：2021-08-02 | CVE：-
- 原文：https://hackerone.com/reports/1122408

- - - - - - - - 
Mutations are `edit` or `create`  queries used in Graphql. Gitlab prevents CSRF in this functionality by sending a POST request with a X-CSRF-Token header. The bug I found here was that, when we send a GET request, the backend does not expect the X-CSRF-Token header. Using this, an attacker could leverage this to bypass the existing CSRF protection


## Slack integration setup lacks CSRF protection
- 等级：High | 项目：HackerOne | 披露：2021-07-07 | CVE：-
- 原文：https://hackerone.com/reports/170552

- - - - - - - - 
Details:
**Summary:**
Cross-site Request Forgery in the `Integrations` (https://hackerone.com/[YOUR_TEAM]/integrations) feature for teams.
**Description (Include Impact):**
The `Integrations` flow is insecure, because it can be abused by CSRF.
PoC:
Request
[code omitted]
Response
[code omitted]
How can it be bad since you are using `state` parameter?
You are trusting in third-party security that is not under your control.
All the attacker needs is an XSS or Login CSRF or Clickjacking in the third-party system and he can compromise your system. With one of the previous mentioned vulnerabilities in the third-party system, the attacker can control the entire OAuth flow and conn


## Japan - CSRF in webapp.starbucks.co.jp with user interaction could leak an access token if the user was not using Chrome
- 等级：High | 项目：Starbucks | 披露：2021-05-18 | CVE：-
- 原文：https://hackerone.com/reports/1113559

- - - - - - - - 
elber discovered a CSRF in webapp.starbucks.co.jp leaked an access token if an authenticated user opened a crafted HTML file in a browser other than Chrome which has Same Site Attribute for the cookie set by default.
elber also demonstrated the ability to add a Starbucks card to the account with the potential for a single account takeover at login.starbucks.co.jp, if the attacker could trick the user into executing another crafted HTML file.
elber — thank you for reporting this vulnerability and for confirming the resolution.
---


## SocialClub Account Take Over Through Import Friends feature
- 等级：High | 项目：Rockstar | 披露：2021-04-01 | CVE：-
- 原文：https://hackerone.com/reports/901728

- - - - - - - - 
In this report, the researcher identified a vulnerability in a Social Club feature intended to allow users to import their friends list from Facebook and other social media sites. However, if a targeted victim were to visit a crafted site containing a specific malicious script that exploited this feature, it would become possible for an attacker to gain control of the victim's Social Club account. This would work by forcibly linking a Facebook account under the attacker's control to the victim's Social Club account via CSRF, giving the attacker the ability to log into the victim's Social Club account via Facebook Sign-in. This issue has been resolved and is no longer exploit


## ███████mill is vulnerable to cross site request forgery that leads to full account take over.
- 等级：High | 项目：U.S. | 披露：2021-01-25 | CVE：-
- 原文：https://hackerone.com/reports/1066083

- - - - - - - - 
**Summary:**
The form within the "My Account" page in ███████mil fails to verify the CSRF token used when an user makes changes such as changing the password and other details. For example, an attacker can change the user's email address, full name, phone number, etc. In this way the attacker can gain full control over the user's account. 
**Note**
In order to get a valid CSRF token you will need to create an account and make any change in "My account" after this you can grab the value of the ██████████ token and use it in your CSRF attack.
**Description:**
Cross-site request forgery (also known as CSRF) is a web security vulnerability that allows an attacker to induce users


## CSRF on launchpad.37signals.com OAuth2 authorization endpoint
- 等级：High | 项目：Basecamp | 披露：2020-10-30 | CVE：-
- 原文：https://hackerone.com/reports/850022

- - - - - - - - 
Hi,
I found a CSRF in the OAuth2 authorization endpoint on launchpad.37signals.com. That allows a malicious 3rd party application to gain full API access to  victim's  account in 37signals products  that uses OAuth2 authorization.
I found that when making a post request to [code omitted]  endpoint it does not check the "authenticity token" if you add " .json or .xml " like this "authorization.json" .
##post request:
[code omitted]
After a 3rd party application gets the authorization code from redirect_uri, it can then exchange it for an access token. and get full access to the api.
## request to get the access token:
[code omitted]
## PoC:
1- you will need to register on the


## CSRF Vulnerabiliy on Facebook Linkage Page Allows Full Account takerover of Socialclub Accounts.
- 等级：High | 项目：Rockstar | 披露：2020-06-24 | CVE：-
- 原文：https://hackerone.com/reports/653254

- - - - - - - - 
In this report, the researcher identified a CSRF vulnerability in the account linking process that could have allowed attackers to link their Facebook account to the victim's Social Club account, giving the attacker access to the victim's Social Club account. This attack would have required a degree of deception and certain preconditions to be in place, otherwise it would fail. However, the impact was severe enough to be worth fixing despite it being a CSRF issue. We implemented an anti-CSRF token that is now required to complete the linking process, and as a result this attack is no longer possible.
---


## Account takeover through CSRF in http://███████/██████████/default.asp
- 等级：High | 项目：U.S. | 披露：2020-06-11 | CVE：-
- 原文：https://hackerone.com/reports/670924

- - - - - - - - 
**Summary:**
Hi team,
I have found a CSRF vulnerability in http://██████/████/default.asp that leads to account takeover.
## Step-by-step Reproduction Instructions
1. Go to http://██████████/████████/default.asp and login
2. Copy the below HTML code
3. Submit the request and see your profile
4. Try to login again with your username and password
5. Use the password `██████████`. You will be logged in with `████` as a password.
**HTML code:**
[code omitted]
## Impact
Complete account takeover
---


## Firmware download/install vulnerable to CSRF
- 等级：High | 项目：Ubiquiti | 披露：2020-05-29 | CVE：CVE-2020-8168
- 原文：https://hackerone.com/reports/323852

- - - - - - - - 
Attackers can abuse multiple end-points not protected against cross-site request forgery (CSRF), as a result authenticated users can be persuaded to visit malicious web pages, which allows attackers to perform arbitrary actions, such as downgrade the  device's firmware to older versions, modify configuration, upload arbitrary firmware, exfiltrate files and tokens.
These vulnerabilities were found on AirMax AirMax AirOS v6.2.0 and prior versions for TI, XW and XM boards.
The fix for these vulnerabilities were included in the new version of AirMax AirOS firmware v6.3.0 for TI, XW and XM boards.
For more details please visit:
https://community.ui.com/releases/airMAX-M-v6-3-0/c8


## H1514 CSRF in Domain transfer allows adding your domain to other user's account
- 等级：High | 项目：Shopify | 披露：2020-03-30 | CVE：-
- 原文：https://hackerone.com/reports/416978

- - - - - - - - 
**Summary:**
Shopify allows users to buy their own domain from the Shopify system. One of the facility on this is that if you buy the domain through Shopify, you can do an inter-store transfers. This means:
> You can only transfer your domain to a Shopify store owned by you. It can take up to 24 hours to complete the transfer.
I ended up finding a CSRF that allows adding my domain to user X's store granted I know their *.myshopify.com.
**Description:**
When you request for a transfer of your domain to another store, an email is sent to you with the transfer link. This link looks like this: 
`https://www.shopify.com/login?redirect=settings/domains/initiate_inter_shop_domain_t


## Norway - store.starbucks.no - CSRF on email change
- 等级：High | 项目：Starbucks | 披露：2020-01-23 | CVE：-
- 原文：https://hackerone.com/reports/718852

- - - - - - - - 
moonlight323 discovered a Cross-Site Request Forgery (CSRF) vulnerability on store.starbucks.no. This vulnerability affected the functionality that allows a customer to change the email address associated with their account. By abusing this functionality, an attacker could potentially change the victim's email on the account if they were successfully able to lure the victim to trigger the CSRF payload while they were logged in.
@moonlight323— thank you for reporting this vulnerability and confirming the resolution.
---


## Cross-Site Request Forgery (CSRF) vulnerability on API endpoint allows account takeovers
- 等级：High | 项目：Khan | 披露：2019-06-22 | CVE：-
- 原文：https://hackerone.com/reports/419891

- - - - - - - - 
## Summary
The `/signup/email` API endpoint at [khanacademy.org](https://khanacademy.org) is vulnerable to Cross-Site Request Forgery (CSRF) attacks, allowing takeovers of accounts associated with unconfirmed email addresses.
## Description
The vulnerable endpoint allows an authenticated user to change the email address associated with their account if they have not yet confirmed the current address. However, it does not sufficiently verify that requests were intentionally performed by the user (e.g. by checking the values of HTTP headers and using an anti-CSRF token).
## Proof-of-Concept (PoC)
This is the code used for the demonstration video attached to this report (ka-sig


## CSRF to HTML Injection in Comments
- 等级：High | 项目：WordPress | 披露：2019-05-13 | CVE：-
- 原文：https://hackerone.com/reports/428019

- - - - - - - - 
Simon discovered a CSRF vulnerability that led to RCE. More [details are available on the RIPS blog](https://blog.ripstech.com/2019/wordpress-csrf-to-rce/).
---


## UniFi Video Server web interface Configuration Restore CSRF leading to full application compromise
- 等级：High | 项目：Ubiquiti | 披露：2019-04-28 | CVE：CVE-2019-5430
- 原文：https://hackerone.com/reports/329749

- - - - - - - - 
In UniFi Video 3.10.0, due to the lack of CSRF protection, it is possible to abuse the Web API to make changes on the server configuration without the user consent, requiring the attacker to lure an authenticated user to access on attacker controlled page.
---


## CSRF in Inviting users
- 等级：High | 项目：Ping | 披露：2019-03-26 | CVE：-
- 原文：https://hackerone.com/reports/323975

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
**Summary:** [add summary of the vulnerability]
When a user is invited, a GET request is made. This can be used with a CSRF attack. 
**Description:** [add more details about this vulnerability]
User invitations usually should be done through a POST request. In this case the app uses a GET request. For example: https://ort-admin.pingone.com/web-portal/ajax/user/directory/inviteuser/?alternate_email=rojan@netsecurity.


## Issue:Form does not contain an anti-CSRF token
- 等级：High | 项目：Phabricator | 披露：2019-03-22 | CVE：-
- 原文：https://hackerone.com/reports/513134

- - - - - - - - 
=============================
#Form does not contain an anti-CSRF token
=============================
--------------------------------------------------------------------------------------------------------------------
There are 15 instances of this issue ==>
/
/Z1336
/applications/
/auth/start/
/auth/start/
/book/phabricator/article/installation_guide/
/dashboard/
/dashboard/arrange/8/
/differential/
/diffusion/
/diffusion/commit/
/diffusion/commit/query/E1D1uHPOvfuP/
/feed/query/all/
/home/menu/view/245/
/maniphest/
--------------------------------------------------------------------------------------------------------------------
Issue Details ==>
Cross-site Request Forge


## Request vulnerable to CSRF
- 等级：High | 项目：Phabricator | 披露：2019-03-22 | CVE：-
- 原文：https://hackerone.com/reports/513137

- - - - - - - - 
There are 4 instances of this issue:
[+] /dashboard/panel/render/12/
[+] /dashboard/panel/render/22/
[+] /dashboard/panel/render/4/
[+] /dashboard/panel/render/6/
Issue background ==>
Cross-site Request Forgery (CSRF) is an attack which forces an end user to execute unwanted actions on a web application to which he/she is currently authenticated. With a little help of social engineering (like sending a link via email / chat), an attacker may trick the users of a web application into executing actions of the attacker's choosing. A successful CSRF exploit can compromise end user data and may allow an attacker to perform an account hijack. If the targeted end user is the admini


## Account Takeover using Linked Accounts due to lack of CSRF protection
- 等级：High | 项目：Rockstar | 披露：2019-02-20 | CVE：-
- 原文：https://hackerone.com/reports/463330

- - - - - - - - 
In this report, the researcher found a weakness in our third-party account linking process. They were able to create a malicious link that, if clicked by the victim, would under certain conditions give the attacker access to the victim's Social Club account. This issue has now been fixed.
---


## Проверяем принадлеженость email и номера телефона к определенному юзеру / CSRF на смену номера для некоторых пользователей
- 等级：High | 项目：VK.com | 披露：2019-01-28 | CVE：-
- 原文：https://hackerone.com/reports/388236

- - - - - - - - 
Проблема генерации хеша.
**Summary (researcher):**
CSRF на смену номера имея фамилию и логин юзера, возможность сопоставить номер и email на принадлежность к одной и той же странице
---

