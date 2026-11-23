# HackerOne 实战案例：improper-authorization

_11 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Email verification bypass via request  to endpoint "accounts.insightly.com/signup/provisionuser"
- 等级：Critical | 项目：Insightly | 披露：2025-08-18 | CVE：-
- 原文：https://hackerone.com/reports/2718253

- - - - - - - - 
# Summary:
The vulnerability occurs in the "EmailAddress" parameter in the member creation area and affects all users.
##Steps To Reproduce:
Before proceeding with the steps of the vulnerability, have a previously created account or open it now to scenario the attack against existing accounts.
  1-to become a member 
First, go to the address below and type a different e-mail address, then go to the link and fill in the name, surname and password fields. 
*https://accounts.insightly.com/signup*
2. And before you sign up, catch the outgoing requests on burp and change the "EmailAddress" parameter in the request, which I will leave below as image poc.
3.If we are trying to open


## Hijack all emails sent to any domain that uses Cloudflare Email Forwarding
- 等级：Critical | 项目：Cloudflare | 披露：2022-07-28 | CVE：-
- 原文：https://hackerone.com/reports/1419341

- - - - - - - - 
The Email Routing feature enables Cloudflare users to create any number of custom email addresses and route all incoming messages to the user's preferred inboxes.
Due to a bug in zone ownership verification, it was possible to configure Email Routing to redirect e-mail messages for an unverified zone (with Email Routing enabled) to a different mailbox. In addition, the vulnerability allowed the e-mail forwarding configuration created by the zone owner to be overwritten.
The issue has since been fixed by the Engineering team and zone ownership verification is working as expected when setting up Email forwarding rules. We investigated the exploit and validated it had only been


## Claiming the listing of a non-delivery restaurant through OTP manipulation
- 等级：Critical | 项目：Eternal | 披露：2022-02-22 | CVE：-
- 原文：https://hackerone.com/reports/1330529

- - - - - - - - 
**Summary:** Am able to claim any restaurant which is not claimed before.
**Description:** An endpoint `POST /restaurant-onboard-diy/v2/send-auto-claim-otp HTTP/2` sends OTP to the restaurant mobile no.
##Request (Request:1) is - 
[code omitted]
which responses -
[code omitted]
###Here Attacker gains OTP on his own mobile no by changing the `number` & `resId` to his own restaurant.
By using the following request (Request:2) attacker is able to map his e-mail Id as `Owner / Manager` to Victim restaurant.
##Request:2
[code omitted]
###Here by changing the `verificationCode`  -  (Otp received on Attacker Mobile in response of Request :1 )& `requestId`  (Response of request:1) a


## Account Takeover via billing
- 等级：Critical | 项目：Chaturbate | 披露：2018-09-19 | CVE：-
- 原文：https://hackerone.com/reports/394329

- - - - - - - - 
The hacker found that when subscribing to a fanclub the parameters could be manipulated to purchase a fanclub subscription for another user. This will set the email of the target account if they had no email on file. This could then be used to reset the password for the target user.
The purchasing logic was fixed to not allow modifying of these parameters. The attack could only target accounts with no email on file, and required a purchase.
---


## Shopify admin authentication bypass using partners.shopify.com
- 等级：Critical | 项目：Shopify | 披露：2017-09-28 | CVE：-
- 原文：https://hackerone.com/reports/270981

- - - - - - - - 
@uzsunny reported that by creating two partner accounts sharing the same business email, it was possible to be granted "collaborator" access to any store without any merchant interaction.
We tracked down the bug to incorrect logic in a piece of code that was meant to automatically convert an existing normal user account into a collaborator account. The intention was that, when a partner already had a valid user account on the store, their collaborator account request could be accepted automatically, with the user account converted into a collaborator account.
The code did not properly check what type the existing account was, and therefore an existing collaborator account in


## Subscription check bypass of NordVPN service
- 等级：High | 项目：Nord | 披露：2023-07-17 | CVE：-
- 原文：https://hackerone.com/reports/2012443

- - - - - - - - 
The reporter identified an issue in one of the NordVPN's infrastructure backend services responsible for checking if the user has a valid subscription. Successful exploitation of this issue does not permanently grant lifetime access to the VPN services, nor does it affect the confidentiality or integrity of other users. To abuse this service a user would have to perform the exploitation steps each time they wish to connect to the VPN service.
We are aware that the exploitation of this service is a bit different on mobile applications this is based on minor distinctions between applications' architectural decisions. Nonetheless, the root cause and impact- users can access Nor


## Stealing Users OAuth authorization code via redirect_uri
- 等级：High | 项目：pixiv | 披露：2023-03-22 | CVE：-
- 原文：https://hackerone.com/reports/1861974

- - - - - - - - 
## Summary:
Path traversal in OAuth `redirect_uri` which can lead to users authorization code being leaked to any malicious user.
The following authorization code flow request is generated at booth login.
[code omitted]
Path traversal vulnerability in this `redirect_uri` parameter allows the attacker to direct the user to the product page created by the attacker.
[code omitted]
-> redirected to https://booth.pm/ja/items/4503924
If the attacker had Google Analytics enabled, the query string could be exposed when the victim is redirected to the product page, so the unused authorization code is leaked.
## Steps To Reproduce:
  1. The attacker makes his shop public. Register his


## Account takeover - improper validation of jwt signature (with regards  to experiation date claim)
- 等级：High | 项目：Linktree | 披露：2022-12-26 | CVE：-
- 原文：https://hackerone.com/reports/1760403

- - - - - - - - 
Some backend services did not properly validate JWTs. As a result JWT validation could be bypassed by setting the expiration date claim to a unix timestamp in the past, and abusing this for account takeover.
**Summary (researcher):**
The expiration date claim of the JWT token was not properly handled. I was able to bypass validation by changing the expiration date to a date in the past.
---


## Improper authorization allows disclosing users' notification data in Notification channel server
- 等级：High | 项目：LY | 披露：2021-12-31 | CVE：-
- 原文：https://hackerone.com/reports/1314162

- - - - - - - - 
LINE Channel authentication provides separate authentication tokens for each LINE Channel. Due to the bug in the authentication process in the Notifications Channel service, it could be possible for an attacker to get the Notifications Channel data of another user by using their valid authentication token from another channel, for example, if an attacker creates their own channel and makes victim account to join it.
---


## Email address of any user can be queried on Report Invitation GraphQL type when username is known
- 等级：High | 项目：HackerOne | 披露：2020-02-20 | CVE：-
- 原文：https://hackerone.com/reports/792927

- - - - - - - - 
**Summary:**
Email  id  of all hackerone users disclosure
**Description:**
There is an flaw , with that i can get all hackerone users email id


## Improper Authorization
- 等级：High | 项目：Stripo | 披露：2020-02-03 | CVE：-
- 原文：https://hackerone.com/reports/751299

- - - - - - - - 
hi there ,
i found an vulnerability on  https://my.stripo.email/cabinet/#/users/orog_id ,
generally every user have an organisation and the organisation contain projects , 
lets suppose : test@gmail.com is the owner of the project
and test2@gmail.com was invited to his project as admin , in normal situation the owner can not be removed even if second account is admin
the issue is i can removed the owned from hi position to admin , and the big problem once the owner is removed he can not login again to his account
## Steps To Reproduce:
[add details for how we can reproduce the issue]
  1. you must have 2 account , one owner , the second got invited as admin
  2. log in with 

