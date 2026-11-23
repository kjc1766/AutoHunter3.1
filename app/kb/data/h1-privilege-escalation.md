# HackerOne 实战案例：privilege-escalation

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Unauthorized access to PII leads to Administrator account Takeover
- 等级：Critical | 项目：MTN | 披露：2025-02-22 | CVE：-
- 原文：https://hackerone.com/reports/2450685

- - - - - - - - 
## Summary:
This vulnerability is present in the `wp-json/wp/v2/users/15` file located in the wordpress directory endpoints. This flaw arises from insufficient restrictions placed on the list of post authors, which can be exploited by remote attackers to obtain sensitive information through wp/v2/users/15 requests attackers can obtain sensitive information in the form of email addresses (PII Leaks) and will be used in `wp-login` to send forget password or brute-force password requests.
**Descriptions:**
An cross-origin resource sharing (CORS) policy controls whether and how content running on other domains can perform two-way interaction with the domain that publishes the po


## Ad Account Takeover
- 等级：Critical | 项目：LinkedIn | 披露：2023-07-20 | CVE：-
- 原文：https://hackerone.com/reports/1791720

- - - - - - - - 
The researcher found an authorization issue in LinkedIn Marketing Solutions - Business Manager, which allowed an attacker to bind an unrelated Campaign Manager Account via the attacker's Business Manager. This could have led to unauthorized access to the target's LinkedIn Campaign Manager. We addressed and resolved the issue within 24 hours.
**Summary (researcher):**
‎
---


## Main Domain Takeover at  https://www.marketo.net/
- 等级：Critical | 项目：Adobe | 披露：2022-09-26 | CVE：-
- 原文：https://hackerone.com/reports/1661914

- - - - - - - - 
Resolved valid subdomain takeover report on Marketo. We appreciate the collaboration with the researcher.
---


## Upload Profile Photo in any folder you want with any extension you want
- 等级：Critical | 项目：Stripo | 披露：2022-03-30 | CVE：-
- 原文：https://hackerone.com/reports/753375

- - - - - - - - 
The vulnerability has been fixed
**Summary (researcher):**
Using this vulnerability, a Stripo user becomes able to upload his/her profile photo in any folder (including that of other users), with any file extension as per his/her wish.
---


## EC2 subdomain takeover at http://████████/
- 等级：Critical | 项目：U.S. | 披露：2022-02-14 | CVE：-
- 原文：https://hackerone.com/reports/1296366

- - - - - - - - 
There is a dangling DNS A record that points to an EC2 instance that no longer exists, I was able to claim the EC2 instance and host content on http://███████/.
## Steps To Reproduce:
  1. Visit http://█████████/██████████.html and view the PoC:  ██████
## Suggested Remediation Steps
  Remove the A record pointing to the current ec2 instance. 
## Impact
Hosting content on http://█████/ and potentionally fully bypassing web protections like CORS (in cases of `████████`) or redirecting users to malicious pages.
## Impact
Hosting content on http://██████/ and potentionally fully bypassing web protections like CORS (in cases of `██████████`) or redirecting users to malicious pag


## Attacker is able to join any tenant on larksuite and view personal files/chats.
- 等级：Critical | 项目：Lark | 披露：2021-11-03 | CVE：-
- 原文：https://hackerone.com/reports/1363185

- - - - - - - - 
A privilege escalation issue was found in Open.larksuite.com, which could have potentially allowed attackers to join any tenant, and view files and communications that are shared by team members. We thank @imran_nisar for reporting this to our team and confirming the resolution.
---


## Subdomain takeover of ███
- 等级：Critical | 项目：U.S. | 披露：2021-09-09 | CVE：-
- 原文：https://hackerone.com/reports/892667

- - - - - - - - 
#Summary:
The subdomain ██████ had an CNAME record pointing to an unclaimed ███████ webservice. This is a high severity security issue because an attacker can register the subdomain on ███ and therefore can own the subdomain  █████████.
#Description:
The dangling CNAME record of █████████  is pointing to █████.███████ which was not claimed by you. I registered a service with this name and therefore was able to takeover the subdomain. Every attacker doing this has afterwards full control over the contents served on this subdomain.
#Subdomain Affected: 
██████████
#Proof Of Concept:
I have uploaded a simple subdomain takeover PoC on http://███████/████████
# Step-by-step Repro


## RCE hazard in reporting (via Chromium)
- 等级：Critical | 项目：Elastic | 披露：2021-05-26 | CVE：-
- 原文：https://hackerone.com/reports/1168765

- - - - - - - - 
**Summary:** Reporting embeds a Chromium that is susceptible to RCEs
**Description:**
Reporting uses a headless Chromium to generate PNGs and PDFs. This is invoked (at least on Elastic Cloud, ECE and ECK) with `--no-sandbox` to work at all.
There are RCEs readily available for Chrome, and at least the versions shipped with 7.11 and 7.12 are susceptible to the attached example.
Attached is an adaptation of this exploit: https://github.com/rapid7/metasploit-framework/pull/15007/files#diff-42ae645fcacbd90d93296471ac57e1d734544af7fb082efd607db0a29d197ac4R53
I have not been able to devise a complete chain yet (thus the "hazard"), but anything that enables pointing reporting at at


## Remote Code Execution in coming Kibana 7.7.0
- 等级：Critical | 项目：Elastic | 披露：2021-04-19 | CVE：-
- 原文：https://hackerone.com/reports/861744

- - - - - - - - 
**Summary:**
Kibana 7.7.0 as per commit [c5f682cb](https://github.com/elastic/kibana/commits/c5f682cb) is vulnerable to a remote code execution vulnerability that is similar to the one reported in https://hackerone.com/reports/852613
Kibana 7.7.0 is not released, so this is an experiment. I know that getting these reports is more valuable to Elastic prior to a release, as the amount of work growing out of a critical vulnerability like this is a lot more _after_ release. It could possibly be more valuable for me to wait until Cloud actually has the release and clearly is in scope, but I have faith in you wanting to encourage people to actually look at code whose release is im


## Password Reset link hijacking via Host Header Poisoning leads to account takeover
- 等级：Critical | 项目：U.S. | 披露：2021-04-02 | CVE：-
- 原文：https://hackerone.com/reports/1108874

- - - - - - - - 
**Description:**
████████ uses the Host header when sending out password reset links. This allows an attacker to insert a malicious host header, leading to password reset link / token leakage.
## References
http://www.skeletonscribe.net/2013/05/practical-http-host-header-attacks.html
https://hackerone.com/reports/226659
## Impact
The victim will receive the malicious link in their email, and, when clicked, will leak the user's password reset link / token to the attacker, leading to full account takeover.
## System Host(s)
███
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
1.) Open up Firefox and Burp Suite.
2.) Visit the forgot password page (http


## Email Confirmation Bypass in your-store.myshopify.com which leads to privilege escalation
- 等级：Critical | 项目：Shopify | 披露：2020-09-15 | CVE：-
- 原文：https://hackerone.com/reports/910300

- - - - - - - - 
Hello Shopify, I have found a bug by which I can verify any email on .myshopify.com, the bug is very strange but it works. Also I can take over the accounts but only the ones which do not have SSO.
To reproduce please follow the steps exactly as I written otherwise you will not be able to reproduce it.
Steps to reproduce: 
1. Go to your partners account and make a store
{F886149}
2. Go to your new store and don't verify email, then go to admin/settings/account/youraccountnumber
{F886151}
3. Change your email to victims email(in my case say_ch33se+111@wearehackerone.com)
{F886138}
4. Go to burps match and replace and replace your email with the email you want to takeover(in m


## Privilege escalation from any user (including external) to gitlab admin when admin impersonates you
- 等级：Critical | 项目：GitLab | 披露：2020-08-26 | CVE：-
- 原文：https://hackerone.com/reports/493324

- - - - - - - - 
**Summary:**
Hey team,
I have discovered a way for any logged in user (attacker) to escalate his privileges to gitlab administrator if the real gitlab administrator impersonates attacker's account.
**Description:**
When the gitlab admin impersonates some user, he gets new `_gitlab_session` cookie and then clicking at `Stop impersonating` he gets his own admin's cookie back. The vulnerability is that the impersonated user (attacker in our case) can see impersonated session at the `Active sessions` so he can switch to it (manually setting it in cookie) and click `Stop impersonating` by himself. This is a way how he can become gitlab administrator.
## Steps To Reproduce:
1. Sig


## Remote Code Execution on Cloud via latest Kibana 7.6.2
- 等级：Critical | 项目：Elastic | 披露：2020-07-28 | CVE：-
- 原文：https://hackerone.com/reports/852613

- - - - - - - - 
**Summary:** A prototype pollution in Kibana can be used to gain remote code execution.
**Description:**
There is a prototype pollution bug in the upgrade assistant's telemetry collector, via a dangerous usage of `_.set`: https://github.com/elastic/kibana/blob/master/x-pack/plugins/upgrade_assistant/server/lib/telemetry/usage_collector.ts#L93
We can pollute the prototype by providing a specially crafted "upgrade-assistant-telemetry" "saved object".
The attached video provides a walkthrough. There is a bit of waiting involved at one point, I included the entire thing for completeness with a hint of when you can fast forward :) 
## Steps To Reproduce:
The following assumes an 


## Subdomain takeover of ████
- 等级：Critical | 项目：U.S. | 披露：2020-07-08 | CVE：-
- 原文：https://hackerone.com/reports/900062

- - - - - - - - 
**Summary:**
I was able to claim the subdomain: ████ using Microsoft Azure ( CDN profiles)
**Description:**
## Impact
Platform(s) Affected:
Subdomain
Azure CDN
## Step-by-step Reproduction Instructions
1. Using dig, I was able to determine that the subdomain '███████' was vulnerable to takeover. The record showed status: NXDOMAIN and was pointing to the CNAME: █████.
2. Using this information, I was able to create a new Azure CDN Profile with the name '██████████'. This would resolve to the CNAME record mentioned above.
3. I then created a Web App domain through Azure  where I uploaded a small proof html file through FTP, I then set the CDN's origin type to WebApp and select


## Able to Become Admin for Any LINE Official Account
- 等级：Critical | 项目：LY | 披露：2020-03-25 | CVE：-
- 原文：https://hackerone.com/reports/698579

- - - - - - - - 
The reporter found an issue where abusing an IDOR would allow for an attacker to become an administrator of any LINE Official Account. This was due to an issue where the group ID could be extracted and/or easily guessed, combined with lack of authentication, leading to being able to craft a request that resulted in being given administration rights to that LINE Official Account.
---


## Project Template functionality can be used to copy private project data, such as repository, confidential issues, snippets, and merge requests
- 等级：Critical | 项目：GitLab | 披露：2019-11-27 | CVE：-
- 原文：https://hackerone.com/reports/689314

- - - - - - - - 
I've found a three minor vulnerabilities which, when combined, allow an attacker to copy private repositories, confidential issues, private snippets, and then some. I'll go through the code path to explain the vulnerabilities and how they are combined. See the **Proof of Concept** section if you want to reproduce it immediately.
Let's start at the `ProjectsController` of EE, which is prepended to `app/controllers/projects_controller.rb` in an EE instance. 
**ee/app/controllers/ee/projects_controller.rb**
[code omitted]
This method defines what parameters can be passed by the user. The two notable parameters here are `use_custom_template` and `group_with_project_templates_id`


## Worker container escape lead to arbitrary file reading in host machine
- 等级：Critical | 项目：Semmle | 披露：2019-10-16 | CVE：-
- 原文：https://hackerone.com/reports/694181

- - - - - - - - 
## Summary:
Because lack of security, attacker will be able to remove original log file and replace it will a symlink to other file, 
After finishing job, host machine copy file from docker container.
Because the original log file has been removed, the host machine will copy the symlink file.
But the problem is it doesn't copy the linked file in container, it copys the linked file in the HOST MACHINE.
## Steps To Reproduce:
The attack is very simple, just remove the original build.log file and replace with a symlink file,
I used this configuration to read the ``/etc/passwd``:
[code omitted]
## PoC
Content of ``/etc/passwd`` is attached below
## Impact
Give attacker ability t


## Privilege Escalation удаляем все созданные ссылки с okl.lt
- 等级：Critical | 项目：ok.ru | 披露：2019-07-23 | CVE：-
- 原文：https://hackerone.com/reports/478621

- - - - - - - - 
IDOR at okl.lt allowed to hide links in another user's dashboard. The short link itself remained functional.
**Summary (researcher):**
Уязвимость позволяла скрывать все созданные ссылки другими пользователями в их панеле, но ссылка продолжала работать
IDOR at okl.lt allowed to hide links in another user's dashboard. The short link itself remained functional.
---


## Subdomain takeover on svcgatewaydevus.starbucks.com and svcgatewayloadus.starbucks.com
- 等级：Critical | 项目：Starbucks | 披露：2018-07-23 | CVE：-
- 原文：https://hackerone.com/reports/383564

- - - - - - - - 
Hello,
This is fairly close to [this report](https://hackerone.com/reports/325336) however these are different subdomains than the one in the report.
This can be pretty serious since I can server virtually anything I want. In the 45 minutes I've held the domain I have served to 341 unique IP addresses. 
Two starbucks.com subdomains are pointed to Azure with an unclaimed CNAME record. Anyone would be able to serve content on these subdomains.
##svcgatewayloadus.starbucks.com
[code omitted]
##svcgatewaydevus.starbucks.com
[code omitted]
#PoC:
http://svcgatewayloadus.starbucks.com/
http://svcgatewaydevus.starbucks.com/
##Mitigation:
Remove the CNAME record from the starbucks.co


## Privilege escalation allows any user to add an administrator
- 等级：Critical | 项目：Node.js | 披露：2018-07-12 | CVE：CVE-2018-16483
- 原文：https://hackerone.com/reports/343626

- - - - - - - - 
I would like to report privilege escalation in the npm module express-cart.
It allows a normal user to add another user with administrator privileges.
# Module
**module name:** express-cart
**version:** 1.1.5
**npm page:** `https://www.npmjs.com/package/express-cart`
## Module Description
expressCart is a fully functional shopping cart built in Node.js (Express, MongoDB) with Stripe, PayPal and Authorize.net payments.
## Module Stats
[10] weekly downloads
# Vulnerability
## Vulnerability Description
A deficiency in the access control allows normal users from expressCart to add new users to the application. This behavior by itself might be considered a privilege escalation. H


## Subdomain takeover on svcgatewayus.starbucks.com
- 等级：Critical | 项目：Starbucks | 披露：2018-06-25 | CVE：-
- 原文：https://hackerone.com/reports/325336

- - - - - - - - 
Hello,
this is pretty serious security issue in some context, so please act as fast as possible.


## ACME TLS-SNI-01/02 challenge vulnerable when combined with shared hosting providers
- 等级：Critical | 项目：Internet | 披露：2018-05-19 | CVE：-
- 原文：https://hackerone.com/reports/304378

- - - - - - - - 
The [ACME TLS-SNI-01](https://tools.ietf.org/html/draft-ietf-acme-acme-01#section-7.3) (and [TLS-SNI-02](https://tools.ietf.org/html/draft-ietf-acme-acme-09#section-8.4)) specification assumed wrong in terms of how current major cloud providers routed and validated domains. This was reported earlier this week to Let's Encrypt, and they decided to disable the method. Today Let's Encrypt decided to sunset both TLS-SNI-01 and TLS-SNI-02 due to the vulnerability I found. 
A full writeup of the finding and my side of the timeline can be found here:
* [How I exploited ACME TLS-SNI-01 issuing Let's Encrypt SSL-certs for any domain using shared hosting](https://labs.detectify.com/20


## Privilege Escalation using API->Feature
- 等级：Critical | 项目：Ubiquiti | 披露：2017-11-24 | CVE：CVE-2017-0932
- 原文：https://hackerone.com/reports/239719

- - - - - - - - 
EdgeOS version `1.9.1.1` and prior, consequence of the lack of validation on the input of the `Feature` functionality, an attacker with access to an `operator` (read-only) account and ssh connection to the devices, can escalate privileges to `admin` (root) access in the system.
**Summary (researcher):**
The **EdgeRouter X** (firmware `v1.9.1.1`) is susceptible to a local **privilege escalation** due a **Path Traversal** vulnerability in the `Feature` API. This vulnerability allows an attacker with non-privileged access (read-only) to execute commands on the device with the root rights. The attack consists in sending a maliciously crafted file (using `scp` with a non-privileg


## all private tokens are leaked to an unauthenticated attacker
- 等级：Critical | 项目：GitLab | 披露：2017-09-21 | CVE：-
- 原文：https://hackerone.com/reports/268794

- - - - - - - - 
Using the api, one can obtain the authentication token for any user on gitlab:
[code omitted]
We can then use this token to impersonate any user to perform any action they can perform:
[code omitted]
[code omitted]
---


## Access of Android protected components via embedded intent
- 等级：Critical | 项目：Slack | 披露：2017-07-17 | CVE：-
- 原文：https://hackerone.com/reports/200427

- - - - - - - - 
@bagipro found a vulnerability wherein a malicious and unprivileged app on the victim's phone could interact with any activity in the Slack Android app, allowing manipulation of the app in unintended ways. Thanks for the finding @bagipro!
**Summary (researcher):**
I found the following code inside [code omitted] (exported activity, it means that any third-party app installed on the device/instant app can access it)
[code omitted]
So we get that ANY protected/not exported activity can be reached.
Here is an example how it can be used against [code omitted], ***opening arbitrary link inside WebView***
[code omitted]
It could be used with [code omitted] scheme to trigger XSS, o


## Возможность взлома любого пользователя, не использующего двухфакторной аутентификации, через получения кода восстановления на чужой номер.
- 等级：Critical | 项目：VK.com | 披露：2017-05-20 | CVE：-
- 原文：https://hackerone.com/reports/219171

- - - - - - - - 
Уязвимость в библиотеке приложения VK на Android, позволяющая получить на свой номер код для восстановления некоторых страниц.
**Summary (researcher):**
Из-за уязвимости можно было отправить код восстановления любой страницы на чужой номер, спасала только двухфакторная аутентификация.
---


## Subdomain takeover in many subdomains
- 等级：Critical | 项目：OWOX, | 披露：2017-03-24 | CVE：-
- 原文：https://hackerone.com/reports/205949

- - - - - - - - 
Subdomain takeover was possible in some of the subdomains. Though you cant claim it and host your page but it compromises them of using certain google services like GMAIL,Calendar,G-Drive,etc on those susbdomains.
**Summary (researcher):**
Subdomain takeover was possible in some of the subdomains. Though you cant claim it and host your page but it compromises them of using certain google services like GMAIL,Calendar,G-Drive,etc on those susbdomains.
---


## Privilege Escalation on a DoD Website
- 等级：Critical | 项目：U.S. | 披露：2017-02-15 | CVE：-
- 原文：https://hackerone.com/reports/199644

- - - - - - - - 
A Department of Defense website was exposed to a privilege escalation vulnerability, which could have allowed remote administrator access to the website. Thanks to @vag_mour for discovering this vulnerability!
---


## Subdomain Takeover at http://gameday.websummit.net
- 等级：Critical | 项目：WebSummit | 披露：2017-01-30 | CVE：-
- 原文：https://hackerone.com/reports/193056

- - - - - - - - 
As i said in the title i found a subdomain takeover vulnerability on the url http://gameday.websummit.net
The url was trying to find a bucket that didn't exist from a probably forgotten dns entry that was at
gameday.websummit.net.s3-website-eu-west-1.amazonaws.com
So i created a bucket with the specified name and uploaded a poc.
POC in the pictures
For more infos please ask...
---


## Ability to access all user authentication tokens, leads to RCE
- 等级：Critical | 项目：GitLab | 披露：2016-11-03 | CVE：-
- 原文：https://hackerone.com/reports/158330

- - - - - - - - 
# Vulnerability details
The project export feature serializes the user objects of team members and stores it in the `project.json` file. This object contains the `authentication_token` for every user, meaning that an attacker can simply go ahead and create a project on GitLab.com, add one of the admins of GitLab.com, create an export, and obtain the authentication token for that user.
# Proof of concept
Follow these steps to reproduce the issue:
 - create a test account on a GitLab instance and create a temporary repository
 - invite an admin of the GitLab instance as a team member to the repository
 - go to the repository settings and create an export
 - wait a few minutes 


## Pending invites remain valid even after the inviter is removed.
- 等级：High | 项目：Omise | 披露：2025-10-08 | CVE：-
- 原文：https://hackerone.com/reports/3303136

- - - - - - - - 
## Summary:
When an admin (A) invites another user (B) with admin privileges, removing the inviter (A) does not invalidate the pending invite for B. Furthermore, if B has already accepted the invite, B remains in the team with admin privileges. This could allow unauthorized admin access even after the original inviter is removed.
##  Steps to Reproduce
1. Invite a user (A) to the team with **admin privileges**.  
2. A accepts the invitation and becomes an admin.  
3. A invites another user (B) to the team with **admin privileges**.  
4. Remove user A from the team.  
5. Observe:  
   - If B has not accepted the invite, the invite **remains valid**.  
   - If B has already ac


## Bug Report #23JAN136 (subdomain takeover via shopify )
- 等级：High | 项目：Mars | 披露：2025-09-02 | CVE：-
- 原文：https://hackerone.com/reports/1851895

- - - - - - - - 
A subdomain takeover vulnerability was identified on the domain █████████, where the subdomain pointed to an unclaimed Shopify instance. The researcher discovered that the subdomain was vulnerable to takeover because the DNS record pointed to a Shopify service that was no longer being used by the organization. The vulnerability was successfully exploited by the researcher, who created a Shopify account, added the custom domain █████████, and demonstrated control over the subdomain by setting up a password-protected page. This type of vulnerability occurred when DNS records continued to point to external services (in this case, Shopify) that were no longer actively managed by


## Bug Report #23JAN135 (subdomain takeover via shopify )
- 等级：High | 项目：Mars | 披露：2025-09-02 | CVE：-
- 原文：https://hackerone.com/reports/1851886

- - - - - - - - 
The researcher kuriyama discovered a subdomain takeover vulnerability affecting ██████████, which was pointing to an unclaimed Shopify instance. The researcher successfully demonstrated the takeover by claiming the subdomain and setting up a proof-of-concept storefront.
---


## Elevation of Privileges (EoP) vulnerabilities related to the some easy_options on Windows
- 等级：High | 项目：curl | 披露：2025-07-03 | CVE：-
- 原文：https://hackerone.com/reports/2941920

- - - - - - - - 
## Summary
An Elevation of Privileges (EoP) vulnerability can occur in a Windows privileged process that uses CURLOPT_COOKIEJAR, CURLOPT_HSTS, or CURLOPT_ALTSVC.
This vulnerability arises due to the differences in the implementation of the unlink function between Windows and Linux, as well as the behavior of MoveFileEx, which follows specially crafted links.
Given that many components, such as program updaters, frequently use curl with elevated privileges, this issue must be considered a serious concern.
## Affected version
libcurl latest version (8.11.1)
## Description
libcurl provides easy options such as `CURLOPT_COOKIEJAR`, `CURLOPT_HSTS`, and `CURLOPT_ALTSVC`. For examp


## Non Org Admin/Group Manager can create groups in an organization
- 等级：High | 项目：HackerOne | 披露：2024-07-23 | CVE：-
- 原文：https://hackerone.com/reports/2372018

- - - - - - - - 
This report describes a privilege escalation vulnerability that allows a user with only "Program Admin" permissions, to escalate their privileges to higher levels like "Report Manager" or even full administrator privileges under certain circumstances. 
The vulnerability exists due to a mutation in the GraphQL API that lets a low privileged attacker assign themselves to the default admin groups created when a new program is set up. By assigning themselves to these groups, the attacker gains elevated permissions like the ability to modify reports, award bounties, manage users and groups, etc.
The issue is amplified if the organization admin later modifies the permissions for t


## setuid() does not drop all privileges due to io_uring
- 等级：High | 项目：Node.js | 披露：2024-03-16 | CVE：CVE-2024-22017
- 原文：https://hackerone.com/reports/2170226

- - - - - - - - 
`setuid()` does not affect libuv's internal io_uring operations if initialized before the call to `setuid()`.
This allows the process to perform privileged operations despite presumably having dropped such privileges through a call to `setuid()`.
This vulnerability affects all users using version greater or equal than Node.js 18.18.0, Node.js 20.4.0 and Node.js 21.
---


## Code injection and privilege escalation through Linux capabilities
- 等级：High | 项目：Node.js | 披露：2024-02-15 | CVE：CVE-2024-21892
- 原文：https://hackerone.com/reports/2237545

- - - - - - - - 
On Linux, Node.js ignores certain environment variables if those may have been set by an unprivileged user while the process is running with elevated privileges with the only exception of `CAP_NET_BIND_SERVICE`.
Due to a bug in the implementation of this exception,  Node.js incorrectly applies this exception even when certain other capabilities have been set.
This allows unprivileged users to inject code that inherits the process's elevated privileges.
---


## Permissions policies can be bypassed via Module._load.
- 等级：High | 项目：Node.js | 披露：2023-08-16 | CVE：CVE-2023-32002
- 原文：https://hackerone.com/reports/1960870

- - - - - - - - 
The use of `Module._load()` can bypass the policy mechanism and require modules outside of the policy.json definition for a given module.
This vulnerability affects all users using the experimental policy mechanism in all active release lines: 16.x, 18.x and, 20.x.
Please note that at the time this CVE was issued, the policy is an experimental feature of Node.js.
---


## Privilege Escalation in kOps using GCE/GCP Provider
- 等级：High | 项目：Kubernetes | 披露：2023-08-04 | CVE：-
- 原文：https://hackerone.com/reports/1842829

- - - - - - - - 
## Summary:
When using kOps with the GCP provider, it is possible for a user with shell access to any pod, to escalate their privileges to cluster admin. During provisioning of the cluster, kOps gives all nodes access to the state storage bucket through the service account associated with the instance. Any user with shell access can request the service account credentials, and read sensitive information from the state store. Using this information, the user can privesc to cluster admin, compromising the entire cluster. It is further possible to compromise a privileged GCP service account associated with the control-plane nodes and takeover other resources in the GCP project.


## The use of __proto__ in process.mainModule.__proto__.require() bypasses the permission system in Node v19.6.1
- 等级：High | 项目：Node.js | 披露：2023-07-20 | CVE：CVE-2023-30581
- 原文：https://hackerone.com/reports/1877919

- - - - - - - - 
process.mainModule.require() correctly works with permission system in Node v19.6.1. 
But the use of \_\_proto\_\_  in process.mainModule.\_\_proto\_\_.require() can bypass the check.
# Description and STR
Consider the following policy.json:
[code omitted]``
The policy only allows proc.js file to be loaded without any dependencies.
However with the following proc.js
[code omitted]``
We get the output:
[code omitted]``
Therefore os dependency can be loaded and os.version executed even if unspecified in permission system.
## Impact
Bypass the permission system
---

