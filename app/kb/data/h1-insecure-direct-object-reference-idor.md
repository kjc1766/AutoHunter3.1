# HackerOne 实战案例：insecure-direct-object-reference-idor

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Authentication Bypass in Subscription Management Endpoint
- 等级：Critical | 项目：lemlist | 披露：2025-11-17 | CVE：-
- 原文：https://hackerone.com/reports/3417162

- - - - - - - - 
A vulnerability was identified in the subscription management functionality that allows unauthorized access to customer billing information. The issue stems from insufficient authentication and authorization controls on an API endpoint, which could potentially be exploited to access sensitive customer data.
## Technical Details:
The vulnerability affects the subscription management API endpoint
Missing authentication requirements allow unauthorized access
The issue is classified as an Insecure Direct Object Reference (IDOR) vulnerability
Customer identifiers can be manipulated to access other users' data
## Resolution:
The vulnerability has been promptly addressed and fixed 


## Sale cancellations from other sellers without restrictions
- 等级：Critical | 项目：MercadoLibre | 披露：2025-03-06 | CVE：-
- 原文：https://hackerone.com/reports/2495989

- - - - - - - - 
We thank @capablanca0 for the report and for providing clear reproduction steps with a proof-of-concept code demonstrating the vulnerability. MercadoLibre acknowledged the issue and worked on a fix internally.
**Summary (researcher):**
An attacker was able to cancel all MercadoLibre sales. I think I saved a few million 😉😎
---


## █████████ when adding branches to your account
- 等级：Critical | 项目：Mars | 披露：2024-11-26 | CVE：-
- 原文：https://hackerone.com/reports/2756402

- - - - - - - - 
A vulnerability has been identified in the branch addition functionality of the Royal Canin specialized channel website ██████████. The issue is classified as an Insecure Direct Object Reference (IDOR) vulnerability, which allows unauthorized users to add branches to any account by manipulating the customer's routing number (RUT) in the request parameter.
---


## IDOR at mtnmobad.mtnbusiness.com.ng leads to PII leakage.
- 等级：Critical | 项目：MTN | 披露：2024-10-05 | CVE：-
- 原文：https://hackerone.com/reports/1773609

- - - - - - - - 
## Summary:
Hello team, i found an IDOR at `https://mtnmobad.mtnbusiness.com.ng/` that allows an attacker to enumerate data such as personal phone number and and account information justt from knowing the email.
The vulnerable request is the following:
[code omitted]
Simply replace the place holder `<PUT_VICTIM_EMAIL_HERE>` with the victim's email and you can see private data about his account such as phone number and account information, as you can see that's PII information being leaked.
## Impact
PII leakage.
---


## Insecure Direct Object Reference (IDOR) Allows Viewing Private Report Details via /bugs.json Endpoint
- 等级：Critical | 项目：HackerOne | 披露：2024-05-23 | CVE：-
- 原文：https://hackerone.com/reports/2487889

- - - - - - - -


## Insecure Direct Object Reference Protection bypass by changing HTTP method in IBM Your Learning endpoint.
- 等级：Critical | 项目：IBM | 披露：2024-05-01 | CVE：-
- 原文：https://hackerone.com/reports/2456603

- - - - - - - - 
Insecure Direct Object Reference vulnerability was reported to IBM, analyzed and has been remediated. Thank you to our external researcher.
---


## Attachment disclosure via summary report
- 等级：Critical | 项目：HackerOne | 披露：2024-04-29 | CVE：-
- 原文：https://hackerone.com/reports/2442008

- - - - - - - - 
**Summary:**
Hackerone provides a form for reporting vulnerabilities to various programs. where the form supports uploading files & previews (images or videos) but is not allowed to use file ids belonging to other accounts. but with the sumary report feature I as a hacker can reveal files belonging to other users just changing the id. this is very severe.
**Description:**
I have tried to call files belonging to other accounts through the submit report, edit report form but it doesn't work it always gets the response [code omitted]. but fortunately I can find another endpoint that is able to read files belonging to other accounts, namely in the sumary report feature.


## IDOR vulnerability reveals additional information
- 等级：Critical | 项目：Semrush | 披露：2024-03-07 | CVE：-
- 原文：https://hackerone.com/reports/1770858

- - - - - - - - 
An issue was identified in the Content Outline Builder product. Changing a user ID in a GraphQL request could reveal additional information about users of Content Outline builder. The subsequent internal review revealed no evidence of this vulnerability being exploited by unauthorized parties.
---


## IDOR to account takeover on POST to █████████ by changing member_id parameter
- 等级：Critical | 项目：Mars | 披露：2024-01-30 | CVE：-
- 原文：https://hackerone.com/reports/2132183

- - - - - - - - 
The website endpoint "██████" is exposed to multiple identifier vulnerabilities, which could potentially result in a complete takeover of user accounts. If exploited, malicious actors could gain full control over the victim's account, posing a significant security risk.
---


## IDOR in upload videos of a Channel on https://video.ibm.com
- 等级：Critical | 项目：IBM | 披露：2023-08-31 | CVE：-
- 原文：https://hackerone.com/reports/2085185

- - - - - - - - 
IDOR in uploading videos to channels on https://video.ibm.com was reported to IBM, analyzed and has been remediated. Thank you to our external researcher.
---


## read and message other user's messages
- 等级：Critical | 项目：Reddit | 披露：2023-05-18 | CVE：-
- 原文：https://hackerone.com/reports/1744264

- - - - - - - - 
go to your account's chat page, stop the request and change the reddit session parameter, now leave the request and you will be able to access the test account's chat screen
send the request to the repeater change the reddit session parameter and send it then you will see the return result is 200
show reply in browser and copy and paste the address into your browser you will access the chat page of your test account
## Impact
other users' chat screen can be accessed
and message can be sent
---


## Remove Every User, Admin, And Owner Out Of Their Teams on developers.mtn.com via IDOR + Information Disclosure
- 等级：Critical | 项目：MTN | 披露：2022-12-01 | CVE：-
- 原文：https://hackerone.com/reports/1448550

- - - - - - - - 
Hello world,
This vulnerability is too involved with regular users, in order for us to prevent any damage, we need 3 different user accounts we own. 
This gives us specific "user_id" and "team_id" to work with.
There's an Information Disclosure as a side effect of this vulnerability. User and team names are disclosed in the response from the server.
## Steps To Reproduce(POC)
==First, let's paint a mental picture of this vulnerability and the required conditions using accounts with imaginary user_id & team_id.
The vulnerability and conditions are realistic, the only imaginary thing is the user_id and team_id.==
 1. Create 3 accounts on developers.mtn.com(Account A, B, and C)


## Unprotected Direct Object Reference
- 等级：Critical | 项目：MTN | 披露：2022-12-01 | CVE：-
- 原文：https://hackerone.com/reports/1536936

- - - - - - - - 
Hello MTN Security Team,
During my hunting,
I discovered that there's an Insecure Direct Object Reference  on https://nin.mtnonline.com 
Vulnerable Path:  https://nin.mtnonline.com/nin/success?message=1
Steps To Reproduce:
You may not even require to submit any NIN before accessing this unprotected page,
Just visit https://nin.mtnonline.com/nin/success?message=1 
I discovered that, to  see other user's NIN, it only require 2 difference , example
https://nin.mtnonline.com/nin/success?message=3
https://nin.mtnonline.com/nin/success?message=5
https://nin.mtnonline.com/nin/success?message=7
https://nin.mtnonline.com/nin/success?message=9
https://nin.mtnonline.com/nin/success?mes


## IDOR in API applications (able to see any API token, leads to account takeover)
- 等级：Critical | 项目：Automattic | 披露：2022-11-01 | CVE：-
- 原文：https://hackerone.com/reports/1695454

- - - - - - - - 
## Summary:
Hi,
@ehtis, thank you for the test account. Here is a critical report. :)
On Pressable, we can create API applications at https://my.pressable.com/api/applications, and we can access many things using the API token via following the [API docs](https://my.pressable.com/documentation/api/v1)
I created an API application and tried to update it, I saw this request :
████████
As you can see there is an `application[id]` parameter that contains the application ID. I changed it to my second account's application ID and that API app moved to my account. So, there is an IDOR but it doesn't have a great impact because it just removes the API application from the victim's a


## IDOR Leads To Account Takeover Without User Interaction
- 等级：Critical | 项目：MTN | 披露：2022-09-04 | CVE：-
- 原文：https://hackerone.com/reports/1272478

- - - - - - - - 
## Summary:
Hello Team,
There's IDOR Bug on this subdomain `mtnmobad.mtnbusiness.com.ng` leads to account takeover, More details check the Poc. 
## Steps To Reproduce:
  1. Create two accounts on `mtnmobad.mtnbusiness.com.ng` and both accounts verify the emails from your email inbox
  2. Login to attacker account on Browser A Go to update Profile Try to update the address for example and Capture the Request with burp send it to `Repeater`
{F1384484}
3. Login to Victim account on browser B do the same to get the victim `ID` you can Grab his ID without sending this request to `Repeater`
4. Go to the Attacker Request You sent to `Repeater` Change `/ID` with the Victim's `ID` yo


## Steal private objects of other projects via project import
- 等级：Critical | 项目：GitLab | 披露：2022-06-07 | CVE：-
- 原文：https://hackerone.com/reports/743953

- - - - - - - -


## Private objects exposed through project import
- 等级：Critical | 项目：GitLab | 披露：2022-06-07 | CVE：-
- 原文：https://hackerone.com/reports/767770

- - - - - - - -


## Email change or personal data change on the account.
- 等级：Critical | 项目：Stripe | 披露：2022-01-21 | CVE：-
- 原文：https://hackerone.com/reports/1250037

- - - - - - - - 
@dk82hg found the email change flow on indiehackers.com was vulnerable to an insecure direct object reference (IDOR) which allowed an attacker to change the email associated with a user account to one they owned and ultimately take over a victim’s account in certain situations. A fix was shipped to confirm authentication on account actions.
Note: This bug was accepted and received before our minimum bounty amounts were increased on August 25, 2021.
---


## Ability to add arbitrary images/descriptions/titles to ohter people's issues via IDOR on getrevue.co
- 等级：Critical | 项目：X | 披露：2021-05-26 | CVE：-
- 原文：https://hackerone.com/reports/1096560

- - - - - - - - 
**Summary:** 
Hi team,
I discovered a vulnerability that allows an attacker to add arbitrary images/descriptions/titles to other people's issues via IDOR
**Description:**
It's possible to perform a IDOR attacker on `getrevue.co`when adding a image to your issue it's also possible to add descriptions and more to other people's issue
## Steps To Reproduce:
   1. Go to `getrevue.co` and Sign In
   2. Click on Issues then Click on Add new issue
   3. Go to the Issue that you created and from the bottom of the page Click on Media
   4. Turn on the Intercept and Upload image
   5. On the request change the ID to your other account's issue ID
Request:
[code omitted]
POC video:
{F11


## █████████ IDOR leads to disclosure of PHI/PII
- 等级：Critical | 项目：U.S. | 披露：2021-02-18 | CVE：-
- 原文：https://hackerone.com/reports/1085782

- - - - - - - - 
**Summary:**
████ is designed in a way where there is a vulnerable endpoint that allows a non-medical user to view the ██████████ records of people who are not ████████s of the sponsor. 
**Description:**
I am currently an Active Duty Airman and this vulnerability does require CAC authentication. When browsing the ██████ website with a proxy I noticed that there is a function that allows sponsors (in this case me) to view their █████s shot records in PDF form. After viewing my ██████████'s shot records, I noticed this functionality lives on the following endpoint `https://████=[id]`.  If you increment or decrement the `██████` parameter by 1 the application will throw an HTTP


## IDOR when editing users leads to Account Takeover without User Interaction at CrowdSignal
- 等级：Critical | 项目：Automattic | 披露：2020-11-18 | CVE：-
- 原文：https://hackerone.com/reports/915114

- - - - - - - - 
## Summary:
Hi team,
If you click `Edit` button on any user of your team at https://app.crowdsignal.com/users/list-users.php, you will send a GET request to `https://app.crowdsignal.com/users/invite-user.php?id=(userid)&popup=1`
In this endpoint, `id` parameter is vulnerable for IDOR. When you change the user ID, you will see victim's email in response like that :
{F893392}
And if you click `Update Permissions` button, you will log-in to victim's account directly.
Also, user IDs are sequential. And they have a simple range with `00010006` to `19920500+`
## Steps To Reproduce:
  1. Log-in to your team account at CrowdSignal
  1. Go to https://app.crowdsignal.com/users/invite-


## IDOR when editing email leads to Account Takeover on Atavist
- 等级：Critical | 项目：Automattic | 披露：2020-11-18 | CVE：-
- 原文：https://hackerone.com/reports/950881

- - - - - - - - 
## Summary:
Hi team,
I created an account on Atavist and checked my settings page.
I can change my email at https://magazine.atavist.com/cms/reader/account with this request :
{F936117}
And as you can see, there is a `id` parameter on request data. It's our user ID, and it's vulnerable for IDOR. So we can change any user's email address.
Also user IDs are sequential so an attacker can change all accounts' email.
## Steps To Reproduce:
  1.Go to https://magazine.atavist.com/login and Login to your account
  1. Go to https://magazine.atavist.com/cms/reader/account and open your proxy program 
  1. Change the email and click `Save`
  1. In request, change the ID to your test ac


## IDOR to Account Takeover on https://████/index.html
- 等级：Critical | 项目：U.S. | 披露：2020-09-29 | CVE：-
- 原文：https://hackerone.com/reports/969223

- - - - - - - - 
Hello Team!
**Summary:**
I found when you wish to update your profile on https://███████/ after your login through https://██████████/signIn/signIn.html website due to an IDOR.
This IDOR gives you the opportunity to change the origin email for the registered account by changing the ID parameter on the following request, i assume that if i would do it on the id=1 i would takeover the admin account, this is due to not requiring the OLD password to make an email change, aswell as no restriction to make POST actions on different account IDS.
**Description:**
IDOR chained to full Account Takeover on ██████ domain.
Account
## Step-by-step Reproduction Instructions
1. Register an a


## I.D.O.R To Order,Book,Buy,reserve On YELP FOR FREE (UNAUTHORIZED USE OF OTHER USER'S CREDIT CARD)
- 等级：Critical | 项目：Yelp | 披露：2020-08-19 | CVE：-
- 原文：https://hackerone.com/reports/391092

- - - - - - - - 
@hk755a found an Insecure Direct Object Reference (IDOR) Vulnerability that allowed an attacker to pay with someone else's registered credit card, while ordering food with Grubhub through the `/checkout/transaction_platform` endpoint. No credit card information was disclosed as a result of this vulnerability.
This is yet another vulnerability in @hk755a's collection of IDOR reports, and we appreciate their diligent effort in working with the Yelp Security team to prevent others from obtaining free food through our system!
**Summary (researcher):**
There was an Insecure Direct Object Reference Vulnerability that allowed the attacker to pay from someone else's credit card whil


## Singapore - Account Takeover via IDOR
- 等级：Critical | 项目：Starbucks | 披露：2020-07-28 | CVE：-
- 原文：https://hackerone.com/reports/876300

- - - - - - - - 
ko2sec discovered that an alternate site shared database and cookie credentials with card.starbucks.com.sg. By exploiting an endpoint on the alternate site, ko2sec was able to copy a PHPSESSID cookie value from that site over to card.starbucks.com.sg and then see user information, update the password and perform an account takeover. ko2sec was awarded a bounty multiplier for this report as they had also submitted a 2nd report for another site that mimicked this behavior.
@ko2sec — thank you for reporting this vulnerability and for confirming the resolution.
---


## account takeover on 3.0.1 version
- 等级：Critical | 项目：Rocket.Chat | 披露：2020-06-14 | CVE：-
- 原文：https://hackerone.com/reports/842625

- - - - - - - - 
I find user reset password hash info and other security info on "/api/v1/[users.info](http://users.info)"  
note : I login on rocketchat with ldap account (my role : user)  
note: in request "[https://target/api/v1/users.info?username=[x]](https://target/api/v1/users.info?username=%5Bx%5D)" you should change usrname to userId
1- please login with user ldap account (role user)  
2- send a request to&nbsp;[https://target/api/v1/users.list](https://target/api/v1/users.list)&nbsp;and copy \_id value  
3- send a request to&nbsp;[https://target/api/v1/users.info?userId=[userId]](https://target/api/v1/users.info?userId=%5BuserId%5D)&nbsp;and copy email value (in response you can se


## IDOR on update user preferences
- 等级：Critical | 项目：Palo | 披露：2020-05-13 | CVE：-
- 原文：https://hackerone.com/reports/854290

- - - - - - - - 
## Summary:
Team member with role USER can change data of any user in the team, or steal his cookies, or steal the account of victim via forget password function.
## Steps To Reproduce:
  1. Login in as user1 (the user with role `admin`) and invite user2 (set his role to `user`).
  2. Login in as user2, open Mail tab and select user1 from `Conversation assignment` dropdown (see F796149 attachment).
  3. Open network tools in the browser devTools or open local proxy and copy `UserUuid` (`da4f313f-e21e-4b5f-b2da-42d9864716f6` in my case) of the user1 from the following request: https://api.outpost.co/api/v1/conversation/assigned?assignedToUserUuid=da4f313f-e21e-4b5f-b2da-42d98


## ████ █████ exposes highly sensitive information to public
- 等级：Critical | 项目：U.S. | 披露：2020-05-11 | CVE：-
- 原文：https://hackerone.com/reports/388554

- - - - - - - - 
**Summary:**
www.██████ is a system used by ██████ for vendors to upload details of their technology for review by ███. Due to an insecure direct object reference vulnerability, all vendor uploads are accessible to the public, without authentication. This includes `Unclass//FOUO` documents, documents labeled `ITAR RESTRICTED / EXPORT CONTROLLED DATA`, and confidential / proprietary data of the respective vendors. These documents include detailed specifications on military technology, including weapons systems, surveillance systems, missiles and ballistics, and other confidential technology.
For instance, several documents contained had labeled criminal penalties for foreign 


## Access to all █████████ files, including CAC authentication bypass
- 等级：Critical | 项目：U.S. | 披露：2019-04-08 | CVE：-
- 原文：https://hackerone.com/reports/429000

- - - - - - - - 
**Summary:**
Due to an Insecure Direct Object Reference (IDOR) in adding recipients to a shared package on ██████████, an unauthenticated attacker can access all files uploaded to ████. As described on ██████████ website, this includes documents with classifications up to FOUO, including PII / PHI Privacy Act data, and documents classified `FOUO//CLOSE HOLD`, `FOUO//SENSITIVE`, and `FOUO//LIMITED DISTRIBUTION DOCUMENT`.
Additionally, █████ enforces CAC pickup requirements to require users to first authorize via CAC. This too, can be bypassed, allowing an attacker to download any file sent over ████.
Note that in addition to this vulnerability, other IDORs exist in sensitive 


## ███████ Site Exposes █████████ forms
- 等级：Critical | 项目：U.S. | 披露：2019-04-05 | CVE：-
- 原文：https://hackerone.com/reports/395246

- - - - - - - - 
## Summary
The █████ site (https://██████.mil/) allows authenticated users to submit ██████ e-forms. Due to a vulnerability in this system, any authenticated user can access the full █████████ e-form of any other user.
## Steps to reproduce
1. Intercept an authenticated request on █████████ containing an Authorization header.
2. Replace the url with `█████████`. Observe that the id in the url can be incremented/decremented to view recently generated OMPFs.
3. Upon submitting the request, the user's full ███████ form JSON response will be sent.
## Impact
Access to ████ is possible through either a Department of Defense Self-Service logon, CAC card, or █████████password. Thus,


## 'cnvID' parameter vulnerable to Insecure Direct Object References
- 等级：Critical | 项目：Concrete | 披露：2018-04-15 | CVE：-
- 原文：https://hackerone.com/reports/265284

- - - - - - - - 
Installation Information
===
IIS 8, PHP 5.5, Concrete5 (5.7.5.7) [Default install]


## Missing Access Control in MigrationFile allows attacker to upload files to any Migration
- 等级：High | 项目：GitHub | 披露：2026-03-05 | CVE：CVE-2026-1355
- 原文：https://hackerone.com/reports/3506183

- - - - - - - - 
A Missing Authorization vulnerability was identified in GitHub Enterprise Server that allowed an attacker to upload unauthorized content to another user’s repository migration export due to a missing authorization check in the repository migration upload endpoint. By supplying the migration identifier, an attacker could overwrite or replace a victim’s migration archive, potentially causing victims to download attacker-controlled repository data during migration restores or automated imports. An attacker would require authentication to the victim's GitHub Enterprise Server instance
---


## Unauthenticated Users Can Access Other Users’ Bug Report Attachments via Broken Access Control
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/3259610

- - - - - - - - 
The `/BugReport/Admin/Attachment/{id}` endpoint exposes attachments linked to private bug reports.
By manipulating the numeric ID in the URL, it’s possible to access attachments belonging to other users, including sensitive bug reports, without proper authorization checks.
This vulnerability works **even when unauthenticated**, meaning anyone who knows or guesses valid IDs can retrieve attachments.
This is a classic **Insecure Direct Object Reference (IDOR)**, where the application fails to enforce access control on a direct object reference (the ID).
## References
- [OWASP Top Ten 2021 – A01:2021 Broken Access Control](https://owasp.org/Top10/A01_2021-Broken_Access_Control/


## IDOR Exposes PII of Tens of Thousands of Users and Supervisors
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/2967032

- - - - - - - - 
**Description:**
While using the system as intended (submitting a SAAR), I noticed there is an insure direct object Reference vulnerability in the application. Users can modify the URL parameter `saarnId` to view and possibly edit other user's SAARs.
**CAC Required**
## References
https://cwe.mitre.org/data/definitions/639.html
https://cwe.mitre.org/data/definitions/284.html
## Impact
This vulnerability leaks the following information on tens of thousands of users:
* Address
* Full Name
* Email
* Phone Number
* DoB
* Supervisor
* DODID Number
* Controlled Unclassified Information
* Clearance Level
* User ID
## System Host(s)
███████
## Affected Product(s) and Version(s)
N/A



## IDOR Vulnerability in Banner Deletion
- 等级：High | 项目：Revive | 披露：2025-11-19 | CVE：CVE-2025-52670
- 原文：https://hackerone.com/reports/3401612

- - - - - - - - 
## Summary
I found an IDOR vulnerability in Revive Adserver's banner deletion endpoint that lets any Manager delete banners belonging to other Managers. The code validates access to the parent campaign but doesn't check if the user owns the specific banner being deleted. This means Manager A can sabotage Manager B's ad campaigns by deleting their banners.
---
## Description
The `/www/admin/banner-delete.php` endpoint is vulnerable to Insecure Direct Object Reference (IDOR). When I tested it, I could delete another manager's banners by manipulating the `bannerid` parameter while keeping my own valid `clientid` and `campaignid`.
Here's what happens: The endpoint checks if I ha


## Arbitrary Read of Another Users private repository without Authorization
- 等级：High | 项目：GitHub | 披露：2025-09-23 | CVE：CVE-2025-8447
- 原文：https://hackerone.com/reports/3124517

- - - - - - - - 
An improper access control vulnerability was identified in GitHub Enterprise Server that allowed users with access to any repository to retrieve limited code content from another repository by creating a diff between the repositories. To exploit this vulnerability, an attacker needed to know the name of a private repository along with its branches, tags, or commit SHAs that they could use to trigger compare/diff functionality and retrieve limited code without proper authorization. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.18, and was fixed in versions 3.14.17, 3.15.12, 3.16.8 and 3.17.5.
[CVE-2025-8447](https://www.cve.org/cverecord?id=C


## Broken Access Control (IDOR) in Booking Detail and Bids Could Leads to Sensitive Information Disclosure
- 等级：High | 项目：Bykea | 披露：2025-06-13 | CVE：-
- 原文：https://hackerone.com/reports/2374730

- - - - - - - - 
## Summary:
Dear Security Team,
I hope this report finds you well,
I would like to report an issue where a malicious user could see other users booking detail, bids information & bids config. The vulnerable URL endpoint are:
[code omitted]
In this case, the `booking_id` in the request URL is vulnerable to IDOR.
## Steps To Reproduce:
1. Create 2 users `attacker` and `victim`, in this case, the `attacker` is a passenger with username `█████████` & the `victim` is a passenger with username `██████████`.
2. As `victim`, perform authentication to get `user_id` & `access_token`.
3. As `victim`, create a new trip.
    Request:
    [code omitted]
    Response:
    [code omitted]
  


## IDOR: Account Deletion via Session Misbinding – Attacker Can Delete Victim Account
- 等级：High | 项目：Mozilla | 披露：2025-06-03 | CVE：-
- 原文：https://hackerone.com/reports/3154983

- - - - - - - - 
## Summary:
A critical vulnerability in the Firefox Accounts API allows an authenticated attacker to permanently delete any user's account by sending a `POST /v1/account/destroy` request using attacker session, but including the victim’s `email` and `authPW` (password hash) in the JSON payload. The server fails to verify that the session making the request belongs to the account being deleted.
## Steps To Reproduce:
1. Login to the victim's account.
{F4367852}
2. Use Burp Suite to intercept a request to the endpoint https://api.accounts.firefox.com/v1/account/destroy when deleting the account. Capture the JSON body, for example:
[code omitted]
███████
3. Then cancel the requ


## Insecure Direct Object Reference (IDOR) in GraphQL deleteProfileImages Mutation
- 等级：High | 项目：Autodesk | 披露：2025-02-21 | CVE：-
- 原文：https://hackerone.com/reports/2968039

- - - - - - - - 
An IDOR (Insecure Direct Object Reference) vulnerability was found on Autodesk User Profile, through the "id" parameter which could have allowed an attacker to delete another user's photo. Autodesk has fixed the vulnerability and we thank @alphahacks for reporting this issue.
---


## Unauthorized Reservation Cancellation Through IDOR Vulnerability
- 等级：High | 项目：Yelp | 披露：2025-01-29 | CVE：-
- 原文：https://hackerone.com/reports/2944357

- - - - - - - - 
It is possible to cancel a reservation by knowing the reservation id, this is because the reservation feature does not require users to login. We were already aware of this issue.
**Summary (researcher):**
It is possible to cancel a reservation just by knowing the reservation id
This was closed as a duplicate of an issue from 2019. Furthermore, knowing the reservation ID is not difficult since it is present in the URLs that people share on social media when they share their reservations. We fundamentally disagree on the conclusion of this report but nonetheless, I appreciate Yelp disclosing the issue
---

