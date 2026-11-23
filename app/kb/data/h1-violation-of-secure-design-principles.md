# HackerOne 实战案例：violation-of-secure-design-principles

_28 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Cross‑Layer State Confusion in libcurl: Credential & Key‑Material Persistence Across Redirect / Connection Reuse Boundaries
- 等级：Critical | 项目：curl | 披露：2025-12-28 | CVE：-
- 原文：https://hackerone.com/reports/3480641

- - - - - - - - 
## Summary:
This report describes a state‑level security invariant violation in libcurl where credential‑ or key‑related state may persist or be re‑applied across logical trust boundaries (redirects, connection reuse, or scheme transitions) without a formal invariant enforcing reset semantics.
The issue is not a parsing bug, not an HTTP smuggling issue, and not a broken cryptographic primitive. It is a cross‑layer state confusion between transport/session state and security intent, observable under realistic client workflows.
## Affected Component
libcurl (client‑side HTTP stack)
Redirect handling
Connection reuse / pooling
Credential / key‑material attachment to requests
##


## Exposure of Private Personal Information to an Unauthorized Actor - PII  and soldier data (mos, schools, and speciality training)
- 等级：Critical | 项目：U.S. | 披露：2025-01-24 | CVE：-
- 原文：https://hackerone.com/reports/1556950

- - - - - - - - 
**Description:**
Authenticated users on `https://█████████/SelfService/home/selfservice` can view other ████████'s data by following the page site for `My ███ Data` and start manipulating URL requests to view the following tabs: 
* Personnel
* Active Duty Tours
* ADOS
* Assignments
* ATRRS
* Data Discrepancies
* DJMS-RC Pay File Records
* DJMS-RC Pay Voucher
* Drill Attendance
* Education/Training
* Gains/Losses
* GI Bill Programs
Tester primarily focused on Personnel, ATRRS, and Education/Training tabs. 
## References
* CWE-359: Exposure of Private Personal Information to an Unauthorized Actor
* CWE-200 - Information Disclosure
* CWE-284 - Improper Access Control
## Contrib


## Subdomain takeover ██████
- 等级：Critical | 项目：U.S. | 披露：2024-07-26 | CVE：-
- 原文：https://hackerone.com/reports/2552243

- - - - - - - - 
The subdomain `█████` is pointing to `open-elb-prod-277276106.us-east-1.elb-amazonaws.com.`, the domain `elb-amazonaws.com` was available for registration
## Impact
Using this vulnerability an attacker can:
- host unwanted/malicious content under your domain
- receive email on subdomains mentioned above
- effectively execute cross-site scripting attacks
- in some cases, steal cookie data
- in some cases, trick password managers into filling in passwords
## System Host(s)
█████████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Visit http://████████/proof.e7437329-ab61-4f22-a049-df5b3685313a.txt
## Suggested Mitigation/Remediation Actions
Remove CN


## Subdomain Takeover via Host Header Injection on www.█████
- 等级：Critical | 项目：U.S. | 披露：2024-06-18 | CVE：-
- 原文：https://hackerone.com/reports/2188240

- - - - - - - - 
## Vulnerability Overview
**_Reported By_**: Ezequiel \[@ezequielpuig\]
**_Reported Date_**: 01/October/2023
**_Reported To_**: U.S. Department Of Defense
**_Vulnerability Type_**: Subdomain Takeover
**_Affected URL_**: www\.███████
Hello U.S. Department Of Defense Security Team, I hope this report finds you well. 
I want to bring to your attention a serious security issue that poses a significant risk to www\.████████. This is related to a subdomain takeover vulnerability, which could allow malicious individuals to gain control over the subdomain and potentially misuse it for malicious purposes.
_Overview:
The affected subdomain is www\.███, which currently points to an unc


## Flaw in Change Email https://youtu.be/MMvlcHIGs2A
- 等级：Critical | 项目：Staging.every.org | 披露：2020-03-24 | CVE：-
- 原文：https://hackerone.com/reports/825643

- - - - - - - - 
See https://youtu.be/MMvlcHIGs2A
---


## out of date disqus shortname usage in the web app source code
- 等级：Critical | 项目：Starbucks | 披露：2017-08-12 | CVE：-
- 原文：https://hackerone.com/reports/172780

- - - - - - - - 
**Short definition of bug**: Misusage of an third-party web service in http://www.starbucks.com/
Hi Starbucks Bug Bounty Team, I found a vulnerability on your global website. I think you migrate your blog from http://www.starbucks.com/blog/archive/starbucks to https://1912pike.com/ and the blog path is also active and in-service still. Also the old blog posts are listed from the search in the main page of your website.
If we inspect the page source of any blog post page under the path http://www.starbucks.com/blog/ , we will see the disqus embedding codes still active.  
i.e. checkout the page source of this page:
http://www.starbucks.com/blog/starbucks-digital-network-conte


## FS Permissions Bypass
- 等级：High | 项目：Node.js | 披露：2026-02-12 | CVE：CVE-2025-55130
- 原文：https://hackerone.com/reports/3417819

- - - - - - - - 
A flaw in Node.js’s Permissions model allows attackers to bypass `--allow-fs-read` and `--allow-fs-write` restrictions using crafted relative symlink paths. By chaining directories and symlinks, a script granted access only to the current directory can escape the allowed path and read sensitive files. This breaks the expected isolation guarantees and enables arbitrary file read/write, leading to potential system compromise.
This vulnerability affects users of the permission model on Node.js v20,  v22,  v24, and v25.
---


## Account Takeover via Unverified Email Change and Improper Session Handling
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/3324823

- - - - - - - - 
Hi team,
During testing on ███
, I noticed an issue with session handling after changing the account email. When I update the email to an unregistered one, the system accepts it without proper verification. If the victim later registers on the website using that email, my existing session does not expire. Instead, I am able to access the victim’s newly created account data.
I also attempted to end the session and log in again, but the system still redirected me into the victim’s account, indicating improper session invalidation and account takeover risk.
## Steps to Reproduce
##steps_Reproduce
1.Register a new account using Google authentication.
2.Change the account email t


## Unauthenticated arbitrary file upload on the https://█████/ (█████████)
- 等级：High | 项目：U.S. | 披露：2024-08-16 | CVE：-
- 原文：https://hackerone.com/reports/698789

- - - - - - - - 
##Description
I was able to identify unsafe upload endpoint on the https://█████/upload.php
##POC
1) Go to the https://█████████/upload.php
2) Upload some test file.
You will see success message:
████
3) Visit `https://███/delete.me` and you will see your uploaded file there
I uploaded example test file with string `test file`
█████████
## Impact
Arbitrary file upload, may lead to the Stored XSS, hosting attacker's content and code execution.
---


## Unauthenticated arbitrary file upload on the https://█████/ (█████.mil)
- 等级：High | 项目：U.S. | 披露：2024-07-19 | CVE：-
- 原文：https://hackerone.com/reports/698793

- - - - - - - - 
##Description
I was able to identify unsafe upload endpoint on the https://██████/upload.php
##POC
1) Go to the https://██████/upload.php
2) Upload some test file.
You will see success message, leaking some internal paths
3) Visit `https://██████████/delete.me` and you will see your uploaded file there
I uploaded example image file there:
█████
## Impact
Arbitrary file upload, may lead to the Stored XSS, hosting attacker's content and code execution.
---


## Onion-Location header allows to open arbitrary URLs including chrome:
- 等级：High | 项目：Brave | 披露：2023-06-22 | CVE：-
- 原文：https://hackerone.com/reports/1089995

- - - - - - - - 
## Summary:
This [PR](https://github.com/brave/brave-core/pull/6762) introduced "Open in Tor" feature that can open .onion URLs offered through `Onion-Location` response header, but `Onion-Location` header allows to open arbitrary URLs such as `javascript:` and `chrome:`.
This behavior can be exploited as a way to bypass SOP and gain access to privileged URLs.
## Products affected: 
* Brave Nightly for OSX (1.21.28 Chromium: 88.0.4324.96 (Official Build) nightly (x86_64))
## Steps To Reproduce:
* Open https://csrf.jp/brave/onion.php
* Click "Open in Tor" button shown in the Brave's address bar
* Privileged URL `chrome://restart/` is opened, and Brave is restarted.
If a user 


## String length restriction byepass at https://callerfeel.mtnonline.com/profile/feedback.html
- 等级：High | 项目：MTN | 披露：2022-09-07 | CVE：-
- 原文：https://hackerone.com/reports/1638347

- - - - - - - - 
## Summary:
Hi, hope you are well :)
I found that the attacker can bye pass the lenght restriction of user name at the feedback form
## Steps To Reproduce:
{F1823237}
## Impact
Attacker can make the receiver page to delay and can cause application level dos
##Mitigation:
Restrict the lenght of the string in backend too not only front end 
Best regards
@aliyugombe
---


## Web Cache Poisoning on  █████
- 等级：High | 项目：U.S. | 披露：2021-06-03 | CVE：-
- 原文：https://hackerone.com/reports/1183263

- - - - - - - - 
**Description:**
The web application `https://████████` uses a web cache to more efficiently serve its pages to the users. An attacker can send a malformed request which the server caches the response of and sends it to the users.
## Impact
An attacker can alter the web cache, making the web application unavailable for as long as they wish.
## System Host(s)
█████████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
* Send the following request to the server:
[code omitted]
* The server will return a 400 status code response and cache the response.
* Now, send the request below. Normally, it should return a 404 response.
[code omitted]
* However it 


## Arbitrary file upload and stored XSS via ███ support request
- 等级：High | 项目：U.S. | 披露：2021-02-18 | CVE：-
- 原文：https://hackerone.com/reports/865354

- - - - - - - - 
**Summary:**
A malicious user can upload files of any type when submitting a support request. 
## Impact
This would allow the attacker to upload malicious executable files as well as `.html` or `.svg` files which would allow the attacker to execute malicious code on behalf of the ████ customer support representative.
## Step-by-step Reproduction Instructions
1. Browse to████████ and create an account or sign in if you already have an account.
2. Click `█████ Faculty/Staff IT Support`.
█████████
3. Click `██████ Support`
██████████
4. Complete the form and upload a file of your choice. Click Submit.
█████████
5. You will see that your request has been created, and your files 


## Access Token Smuggling from my.playstation.com via Referer Header
- 等级：High | 项目：PlayStation | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/835437

- - - - - - - - 
I discovered a way to smuggle an access token from my.playstation.com via Referer header through chain of open redirection vulnerability.  
On my investigation of authentication flow I found this endpoint with potential site for open redirect vulnerability
https://my.playstation.com/auth/response.html
Let's look at some part of the code on this endpoint.
[code omitted]
This is a switch statement checking on variable named requestID
The interesting part for this report is the last condition where requestID is equal to "external".  
This condition basically says that if requestID is equal to "external" then construct URL from query parameters and redirect to that URL.  
There 


## Email Verification bypass on signup
- 等级：High | 项目：Automattic | 披露：2020-12-03 | CVE：-
- 原文：https://hackerone.com/reports/1040047

- - - - - - - - 
## Summary:
This bug is related to wordpress.com. There is feature in wordpress.com which allow users to invite people. We have to enter email address to invite that particular person but the invite link and invite key is also available to the person who invited. This allow attackers to create the profile without having access to the email address and they can make account on behalf of any people who  is not already signed up in wordpress.com
## Platform(s) Affected:
wordpress.com
public-api.wordpress.com
## Steps To Reproduce:
This issue can be reproduced by following these easy steps: 
* Login to your account on wordpress.com
* Setup burpsuite proxy with browser.
* Select 


## On Singing up with a Phone number , The 4 digit OTP does not expires for a long time leading to an easy attack and make a verified account easilty
- 等级：High | 项目：Bumble | 披露：2020-11-25 | CVE：-
- 原文：https://hackerone.com/reports/792295

- - - - - - - - 
Hello there how are you doing ?
Go to sign up page and enter a new phone number and you will be redirected to https://bumble.com/registration/confirm-phone .
You will receive a easy breakable 4 digit OTP Code .
I waited for about 4 hours and the OTP did not expired , This shows that the OTP can be easily bruteforced even having the rate limiting , assuming rate limiting is implemented as this is an old program .
The OTP can be bruteforced , by changing IP via VPN and as the OTP does not expires for a long time it gives sufficient time , to get the actual OTP Code also the OTP is only of 4 digits , So it only requires 10,000 requests .
For Solving of this issue , Captcha Impl


## Authorization Token on PlayStation Network Leaks via postMessage function
- 等级：High | 项目：PlayStation | 披露：2020-11-21 | CVE：-
- 原文：https://hackerone.com/reports/826394

- - - - - - - - 
# Description
After some analysis on how playstation network authentication work, I came across a certain pattern of how authorization tokens are handled.
The web application utilizes postMessage function to exchange authorization tokens between windows/frames.
To simplify this, let's follow on one of authorization flows.
When you enter, https://my.playstation.com
There is a request to
https://auth.api.sonyentertainmentnetwork.com/2.0/oauth/authorize?response_type=token&scope=capone%3Areport_submission%2Ckamaji%3Agame_list%2Ckamaji%3Aget_account_hash%2Cuser%3Aaccount.get%2Cuser%3Aaccount.profile.get%2Ckamaji%3Asocial_get_graph%2Ckamaji%3Augc%3Adistributor%2Cuser%3Aaccount.id


## Unrestricted File Upload to ███████SubmitRequest/Index.cfm?fwa=wizardform
- 等级：High | 项目：U.S. | 披露：2020-06-11 | CVE：-
- 原文：https://hackerone.com/reports/813395

- - - - - - - - 
**Summary:**
An attacker is able to upload files of any type to `███SubmitRequest/Index.cfm?fwa=wizardform` as long as they are less than 5 MB.
**Description:**
The █████ ████ Request System allows a user to submit requests to the ██████████ ███ for event support. An attacker can exploit this request form by uploading malicious files due to an unrestricted file upload feature.
## Impact
An attacker is able to upload malicious files onto the server. These files are attached to a request for support from the ██████ █████████. If a member of the ██████ ████ were to open the malicious file, the attacker could gain remote code execution on ████ information systems. Alternatively,


## Cache poisoning DoS to various TTS assets
- 等级：High | 项目：GSA | 披露：2020-03-12 | CVE：-
- 原文：https://hackerone.com/reports/728664

- - - - - - - - 
I have recently come across a technique to force a Cloudfoundry app to return a HTTP 404 error when requesting any resource, which contains cache friendly headers. What this means is, if the Cloudfoundry app in question is behind a web cache like Cloudfront or Cloudflare etc, it will possibly store a copy of the 404 error response as the cache for the resource being requested, which is served to other users. This describes a cache poisoning Denial of Service, and the concept for this is detailed at https://cpdos.org.
The technique to achieve CPDoS against a Cloudfoundry and hence TTS app is to send a request with the following header:
[code omitted]
This header is designed t


## Bypass Email Verification using Salesforce -- Reproducible in gitlab.com
- 等级：High | 项目：GitLab | 披露：2019-12-13 | CVE：CVE-2019-5486
- 原文：https://hackerone.com/reports/617896

- - - - - - - -


## Missing Protection Mechanism in Mail Servers allows malicious user to use staff.ratelimited.me email could lead to identity theft.
- 等级：High | 项目：RATELIMITED | 披露：2019-02-02 | CVE：-
- 原文：https://hackerone.com/reports/486667

- - - - - - - - 
Hello ratelimited,
I'm not really sure how your mail servers being configured but i guess there is a mis-configuration or missing protection mechanism that fails to verify if the email that is going to be sent are only made by authorized ratelimited staff only. From this point of view a malicious user could sent an email to a victim by using valid and email owned by staffs of ratelimited and to be specific one of them are `gtsatsis@staff.ratelimited.me` and i can surely tell it is based on #369581 wherein a team member acknowledge the hacker that is will be given a reward for efforts.


## SSLv3 Poodle Vulnerability
- 等级：High | 项目：FormAssembly | 披露：2018-11-24 | CVE：-
- 原文：https://hackerone.com/reports/220116

- - - - - - - - 
Hey there,
I tested against POODLE MITM and enterprisedemo.formassembly.com is vulnerable, I simply went into terminal and used this command 
    "openssl s_client -connect enterprisedemo.formassembly.com:443 -ssl3"
POC
How to fix: Disable SSLv3
---


## Private program email forwarding response invitation not expire after first use.
- 等级：High | 项目：HackerOne | 披露：2018-05-30 | CVE：-
- 原文：https://hackerone.com/reports/209140

- - - - - - - - 
**Summary:**
Hi Hackerone Team,
Before i reported that email forwarding of private can be enumerated and any user join to private program here #201369 , __but this seems by design__, but now it i found a related issue which can cause a security impact on private program because the email forwarding response of `HackerOne` did not expire after first use.
**Description (Include Impact):**
If a user __Quits__ to a private program, this user can rejoined without the knowledge of private program owners, also you can check further if the user become Banned it seems that the linked on email still not expire and this can cause security implication if the banned user can rejoined to 


## Access to local file system using javascript
- 等级：High | 项目：Tor | 披露：2017-11-18 | CVE：-
- 原文：https://hackerone.com/reports/258630

- - - - - - - - 
Issue :
Access to local file system using javascript(slightly xss on server side )
The browser can access the local files using iframes with a local html file. this is very normal and often used for local web development but javascript shouldn't be able to get the content of that iframe because this can be used to post the contents to the attackers server. something else I noticed is that it's not limited to the same directory.
Steps to Reproduce :
save a html file from here and open in tor browser .
<html>
<body>
<div id='div1'>
</div>
<script>
current_href = document.location.href
frame = document.createElement('iframe'); frame.src = current_href.replace('file:///home/jnsj


## Exposed API-key allows to control nightly builds of firmwares (█████████ & ████████)
- 等级：High | 项目：Ubiquiti | 披露：2017-10-09 | CVE：-
- 原文：https://hackerone.com/reports/179986

- - - - - - - - 
The researcher found a public API token that was mistakenly granted full-access permission, which allowed the creation/overwrite of nightly builds of UniFi Firmware.
**Summary (researcher):**
Publicly available api-key granted full access permissions to API that controls nightly builds of Ubiquiti firmwares, i.e. it was possible to upload new builds and modify existing ones.
---


## {REDACTED}.data.gov subdomain takeover.
- 等级：High | 项目：GSA | 披露：2017-09-06 | CVE：-
- 原文：https://hackerone.com/reports/263902

- - - - - - - - 
@edio discovered a number of related subdomain takeover attacks against some subdomains of data.gov. 
 
Technically, these domains are out of scope for our [Vulnerability Disclosure Policy](https://github.com/18F/vulnerability-disclosure-policy/blob/master/vulnerability-disclosure-policy.md). We want to remind hackers to please limit their testing to domains explicitly listed in that scope (which is repeated on [our HackerOne program page](https://hackerone.com/tts) for convenience). This is for your own safety: we want to be sure that everyone's on the same page about your activities being authorized.
That said, this was a legitimate vulnerability, which we fixed, and we're


## An unsafe design practice in the Passphrase may result in Secret being accidentally changed.
- 等级：High | 项目：Phabricator | 披露：2017-04-04 | CVE：-
- 原文：https://hackerone.com/reports/218324

- - - - - - - - 
Summary:
An unsafe design practice in the Passphrase may result in Secret being accidentally changed.
Preface:
If a user wants to share his/hers secrets, he/she may use the Passphrase. But when he/she created the credential and setted who can view it and who can edit it, they will soon discover that if they not set the edit permission to the one they want to share secret with, it is impossible success. Naturally, they would give the edit permission to everyone they want to share the secret with. So, here is the problem. It means they can change the secret. If someone ignores the edit records, he/she may under attack inadvertently. Because the secret has been modified.
Reprod

