# HackerOne 实战案例：business-logic-errors

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Change phone number OTP flaw leads to any phone number takeover
- 等级：Critical | 项目：inDrive | 披露：2024-10-09 | CVE：-
- 原文：https://hackerone.com/reports/2588329

- - - - - - - - 
## Summary:
Dear Indrive,
Ive found another valid report, the app allows any user to change the app phone number, but a flaw within the otp allows any number to be added into the account!
When an user requests a phone number change inside the app, it will send a 4 digit code but if you place 0000, it will accept any number and update it into the app!!
## Steps To Reproduce:
  1. Click setting in the account
  2. Click into the phone number and change for a new one
  3. Input 0000 as the otp code
  Phone number added!!
VIDEO POC
████████
At the end you can see  i was trying to pick a number from my contacts but instead i  just use a random phone number and works!!
Remediation


## Unauthorized access to PII leads to MASS account Takeover
- 等级：Critical | 项目：U.S. | 披露：2022-02-14 | CVE：-
- 原文：https://hackerone.com/reports/1061736

- - - - - - - - 
Hi, I hope you doing well
I found a critical endpoint which disclosed the personal information which can use to takeover any account present on https://██████████
#Steps:
1. Visit the link https://www.████████/███████    you will get my details,  including first name and last name, mobile number and email_address related to the account.
2. Go to the forgot password link present at https://www.███████/ click on it.
3. Enter the mail address later you will be taken to another page which will ask you to enter mail address and pin
4. After entering mail address enter the pin as "████" as █████████ is at the endpoint.
5. It will validate and will ask you to change the password of


## Multiple vulnerability leading to account takeover in TikTok SMB subdomain.
- 等级：Critical | 项目：TikTok | 披露：2022-02-02 | CVE：-
- 原文：https://hackerone.com/reports/1404612

- - - - - - - - 
Multiple vulnerabilities like Insecure Direct Object Reference (IDOR), Cross-Site Request Forgery (CSRF), XSS were found that could have resulted in account takeover on the TikTok SMB subdomain. First, an Insecure Direct Object Reference (IDOR) was found, where a missing authorization check could allow an attacker to modify the details of another user. Second, a Cross-Site Request Forgery (CSRF) was found in which an attacker could takeover an account by sending a malicious link, which if clicked by another user could be used to modify that user's account's email address. We thank @lu3ky-13 for reporting this to our team and confirming its resolution.
**Summary (researcher):


## Modify in-flight data to payment provider Smart2Pay
- 等级：Critical | 项目：Valve | 披露：2021-08-10 | CVE：-
- 原文：https://hackerone.com/reports/1295844

- - - - - - - - 
I have found vulnerability which allows attacker to generate steam wallet balance.
Firstly you will have to change yours steam account email to something like (I will explain why in next steps, amount100 is the important part): 
brixamount100abc@█████
Then go to https://store.steampowered.com/steamaccount/addfunds and click add add funds.
Proceed to payment and select any payment which uses Smart2Pay payment method (przelewy24 in my country).
Click next steps as you would do with normal transaction.
Intercept POST request to https://globalapi.smart2pay.com/
You should see request like that
[code omitted]
We cant change parameters as there is Hash field with signature, howeve


## An attacker can run pipeline jobs as arbitrary user
- 等级：Critical | 项目：GitLab | 披露：2020-08-26 | CVE：-
- 原文：https://hackerone.com/reports/894569

- - - - - - - -


## Availing Zomato gold by using a random third-party `wallet_id`
- 等级：Critical | 项目：Eternal | 披露：2020-08-07 | CVE：-
- 原文：https://hackerone.com/reports/938021

- - - - - - - - 
We received a report from @pandaaaa wherein he demonstrated a way to avail Zomato Gold membership using random Zomato User's wallet. The report was triaged and rewarded with critical severity with a `CVSS score of 9.3`. 
It was considered critical since a random user's wallet could have been used for unauthorized membership purchases. This was only possible on third party wallets with `status - active` flag.
| Timeline | Action |
|---|---|
| Thu, 23 July 2020, 15:54 IST | @pandaaaa submitted a report with high severity |
| Thu, 23 July 2020, 16:08 IST | Investigation started, the team started analysing the issue |
| Thu, 23 July 2020, 16:47 IST | First contact on Report |
| 


## Unrestricted File Upload Leading to Remote Code Execution
- 等级：Critical | 项目：Central | 披露：2019-10-30 | CVE：CVE-2019-15893
- 原文：https://hackerone.com/reports/683965

- - - - - - - -


## Ability to perform actions (Tweet, Retweet, DM) and other actions, unauthenticated, on any account with SMS enabled.
- 等级：Critical | 项目：X | 披露：2019-09-26 | CVE：-
- 原文：https://hackerone.com/reports/470749

- - - - - - - - 
**Summary:** By knowing the mobile phone number associated with a Twitter account, or by using random mobile phone numbers! It is possible to perform the following actions against a target without their knowledge or interaction. With no account takeover scenario.
It's a case of, if I know the mobile number... I can control basic functions of the account.
I can do everything that is listed here: https://help.twitter.com/en/using-twitter/sms-commands on an account, completely unauthenticated.
## Steps To Reproduce:
(Add details for how we can reproduce the issue)
  1. Spoof target number, send an SMS to a special short code for the geographical location, as seen here: https://


## OLO Total price manipulation using negative quantities
- 等级：Critical | 项目：Upserve | 披露：2019-07-06 | CVE：-
- 原文：https://hackerone.com/reports/364843

- - - - - - - - 
Manipulating an order request JSON object, containing an additional item with a negative quantity directly manipulates the total amount of the order.
In the following JSON request, an order is submitted for 2 ChickenBurgers ($12 each), as well as -1 BreadPuddings ($9 each).
The total price after tax calculates as $18.70 and is accepted by the system. The attached screenshots show the previous orders, indicating that only $18.70 was charged for the transaction.
[code omitted]
## Impact
The attacker can reduce the price of the order.
The total amount of an order could be modified by including an item with a negative quantity.
---


## Opportunity to post hidden comments
- 等级：Critical | 项目：X | 披露：2018-12-11 | CVE：-
- 原文：https://hackerone.com/reports/434202

- - - - - - - - 
Twitter allows to comment on anyone's tweet. While testing this feature, observed that one can post comment on tweet which will be invisible to the victim whom the reply was posted and would be visible to any other twitter user.
This can allow an Attacker to abuse victim on a tweet. The catch here is victim cannot even know that attacker posted on his tweet but any other twitter user can see that tweet.
**Steps to reproduce**
1. Attacker login to Twitter
2. Attacker blocks victim using Block@victim button at https://twitter.com/<victim>
3. Attacker opens any popular tweet of victim
4. Attacker abuses victim in the tweet reply
5. Victim cannot see the tweet reply posted by At


## Global defaming of any twitter user
- 等级：Critical | 项目：X | 披露：2018-12-06 | CVE：-
- 原文：https://hackerone.com/reports/434689

- - - - - - - - 
Private tweets can be used to keep any user's tweet secret from rest of twitter world. Once the user changes his setting from private tweets to public tweets, all his secret tweets become visible. This can become a major issue causing global distributed attacks
**Steps to Reproduce**
1. Assume the attacker is targeting certain president XYZ for the next election
2. Attacker goes to settings and enable private tweet
3. Attacker find famous tweets from 10000+ celebrity profiles
4. Attacker replies on all those 10000+ celebrity profile tweets mentioning "XYZ is the worst candidate. See what he did <some video or something>"
5. None of the twitter user can see that reply from At


## A bug in the Monero wallet balance can enable theft from exchanges
- 等级：Critical | 项目：Monero | 披露：2018-08-02 | CVE：-
- 原文：https://hackerone.com/reports/377592

- - - - - - - - 
**Summary:**
A Monero bug (already fixed in master) allows theft from exchanges.  This has been exploited again a Monero-derived coin, so the exploit may be underway currently.
**Description:**
(fluffypony: Also please mention you spoke to me and I recommended you put it on HackerOne)
PR #3985 fixed a wallet balance display bug, which seems innocuous enough, but this bug also extends to exchanges: a transfer of, e.g., 1 XMR to an exchange with a duplicated TX pub key will show up on an exchange as a 2 XMR deposit, which then allows the attacker to withdraw 2 XMR from the exchange's wallet.  An attacker could exploit this repeatedly to siphon of all of the exchange's balance.


## Double Payout via PayPal
- 等级：Critical | 项目：Coinbase | 披露：2018-04-04 | CVE：-
- 原文：https://hackerone.com/reports/307239

- - - - - - - - 
An issue with the handling of the PayPal transaction states resulted in a user being able to both withdraw money from PayPal, but not have the funds deducted from their account.
---


## ETH contract handling errors
- 等级：Critical | 项目：Coinbase | 披露：2018-04-04 | CVE：-
- 原文：https://hackerone.com/reports/328526

- - - - - - - - 
A business logic error in the ETH contract handling code allowed for a nested `revert` call in contract execution to improperly credit a user account though funds had not been transferred. In addition, the code did not appropriately handle `delegatecall` within a contract.
Sample contract for the first issue:
[code omitted]
Attacking call of the first issue:
[code omitted]
Sample contract for the second issue:
[code omitted]
We would like to thank @ambisafe for the prompt disclosure and assistance with both issues. Our normal bounties are $10,000 per instance of account balance manipulation. In this case, since two separate issues were reported within one report and provided


## Ethereum account balance manipulation
- 等级：Critical | 项目：Coinbase | 披露：2018-03-21 | CVE：-
- 原文：https://hackerone.com/reports/300748

- - - - - - - - 
The researchers noticed an issue with our ETH receiving code when receiving from a contract. This allowed sending of ETH to Coinbase to be credited even if the underlying contract execution failed. The issue was fixed by changing the contract handling logic. Analysis of the issue indicated only accidental loss for Coinbase, and no exploitation attempts.
The Security team thanks @vicompany for the quick disclosure, and also the internal team for pushing a fix within hours. We do appreciate @vicompany's patience as the full communication loop back to HackerOne took significantly longer than the fix deployment cycle.
**Summary (researcher):**
**Short Summary:** 
By using a smar


## Non-premium user can disable Ads in japanese version of dic.pixiv.net
- 等级：High | 项目：pixiv | 披露：2026-04-27 | CVE：-
- 原文：https://hackerone.com/reports/3183520

- - - - - - - - 
## Summary
A vulnerability is identified in the Japanese version of the pixiv dictionary website (`dic.pixiv.net`) where non-premium users can disable advertisements. Normally, the ability to disable ads is restricted to premium users only, as indicated by the "P" icon next to the ad display settings in the user profile. However, due to improper access control at the API endpoint `/_api/update_user_setting`, any authenticated user can modify their ad display preferences without verification of premium status.
## Steps to Reproduce
1. Disable any ad-blocker plugins in your browser and login as a non-premium Pixiv user
2. Browse to `https://dic.pixiv.net` (the Japanese version


## PROTOCOL-LEVEL: Persistent UDP Amplification and Cache Poisoning via Alt-Svc Logic Flaw
- 等级：High | 项目：curl | 披露：2026-01-02 | CVE：-
- 原文：https://hackerone.com/reports/3483902

- - - - - - - - 
## Summary
A structural logic flaw in the `libcurl` `Alt-Svc` header parser allows attack attributes (specifically `persist` and `max-age`) to "leak" from one service definition to another.
We have successfully chained this logic bug with `curl`'s HTTP/3 (QUIC) support to demonstrate a **Persistent UDP Amplification** attack. An attacker can force a victim's client to cache a malicious UDP route for up to 30 days (`persist=1`), turning the client into an unwilling participant in a distributed denial-of-service (DDoS) attack against arbitrary targets.
## Affected version
Reproduced on: **curl 8.17.0** (and `libcurl` master branch)
Platform: **Linux/Generic** (Issue is cross-p


## Business Logic error leads to bypass 2FA requirement
- 等级：High | 项目：HackerOne | 披露：2024-07-11 | CVE：-
- 原文：https://hackerone.com/reports/2571981

- - - - - - - - 
Hi team,
##Summary
I have identified a business logic issue in the 2FA requirement. I noticed that the organization enables the 2FA requirement so that only reporters who have set up 2FA can report, due to security reasons. This is because the report contains sensitive information, and if a hacker's credentials are compromised, the 2FA protection should be in place. This ensures that the vulnerability reported by the hacker remains secure. However, if the hacker adds another hacker as a collaborator, the hackerone does not check whether the invited hacker has set up 2FA or not. The invited hacker can join the report without any 2FA requirement, which contains the same sensit


## Attackers can *Upgrade and claim offer* on the Premium Trial Subscription with a total price of *IDR0.00* from the original *IDR7,022,061.82*
- 等级：High | 项目：LinkedIn | 披露：2024-06-18 | CVE：-
- 原文：https://hackerone.com/reports/2131224

- - - - - - - - 
Reporter found a method to tamper with the premium pricing flow where an attacker could subscribe to LinkedIn Sales Navigator Core offering for free. This issue has been fixed and is now resolved.
**Summary (researcher):**
##WriteUp:
https://aidilarf.medium.com/part-2-anyone-can-use-unlimited-trial-premium-on-accounts-that-have-used-trial-premium-before-b1ac65c9a2d6
---


## Any user could upload attachments to pentest scoping form they don't have access to
- 等级：High | 项目：HackerOne | 披露：2024-05-15 | CVE：-
- 原文：https://hackerone.com/reports/2450215

- - - - - - - - 
hello team
in my recent testing i found that any users could upload attachments to any users pentest scoping form without having access to it as long as they have the scope id.
note: before you start you will require two account to test for this bug.
steps to reproduce:
1. create a sandbox
2. go to pentest an start an pentest form
3.copy the pentest form id from the url
4. log in to your second account
5. send the following request
==================================================================================================================
POST /attachments HTTP/2
Host: hackerone.com
Cookie: your cookies
-----------------------------22121373215470710503552942440
Content


## CSP Bypass and escalation of https://hackerone.com/reports/2279346
- 等级：High | 项目：PortSwigger | 披露：2024-02-23 | CVE：-
- 原文：https://hackerone.com/reports/2387458

- - - - - - - - 
Hello Team , 
I have gone through this report https://hackerone.com/reports/2279346 and their is CSP bypass where website has implemented security in that but after this i can escalate Again CSP bypass with using different Script .
As shown in https://hackerone.com/reports/2279346 report website rectify the scripts like: 
document.getElementsByTagName("div")[0].innerHTML=`<iframe srcdoc="<div lang=en ng-app=application ng-csp class=ng-scope>
<script src='https://www.google.com/recaptcha/about/js/main.min.js'></script>
<img src=x ng-on-error='w=$event.target.ownerDocument;a=w.defaultView.top.document.querySelector(&quot;[nonce]&quot;);b=w.createElement(&quot;script&quot;);b.s


## the domain is truck-admin.eu-east-1.indriverapp.com and Enter the management system of the blasting mobile phone verification code
- 等级：High | 项目：inDrive | 披露：2023-09-11 | CVE：-
- 原文：https://hackerone.com/reports/1991376

- - - - - - - - 
## Summary:
Find the mobile phone number of the administrator through the WHOIS information, and then send the verification code. Assuming that the verification code expires for 30 seconds or 1 minute, we can only explode the correct verification code in a short time to log in to the management system, so I choose to blast The verification code between 6000 and 7000, and sends the verification code every time it blasts, knows that the correct verification code is found, and I only exploded 8 times to find the correct verification code
## Steps To Reproduce:
  1. Find the management address through the directory scanning:https://truck-admin.eu-east-1.indriverapp.com/admin/aut


## User scoped external storage can be used to gather credentials of other users
- 等级：High | 项目：Nextcloud | 披露：2023-06-27 | CVE：CVE-2023-35928
- 原文：https://hackerone.com/reports/1978882

- - - - - - - - 
Security advisory at https://github.com/nextcloud/security-advisories/security/advisories/GHSA-637g-xp2c-qh5h
---


## Able to approve admin approval and change effective status without adding payment details .
- 等级：High | 项目：Reddit | 披露：2022-06-22 | CVE：-
- 原文：https://hackerone.com/reports/1543159

- - - - - - - - 
## Summary:
In https://ads.reddit.com/ you can create campaign under which you can create ads , once you create new campaign , it is on pending stage and will not be delivered unless you add payment details and is reviewed by admin and approved according to what it says here https://advertising.reddithelp.com/en/categories/ad-review/about-reddits-ad-review-process . But changing the value of admin_approval to APPROVED and effective_status to ACTIVE , the ads is approved and thus we receive the confirmation email from reddit ads that our ads is approved .
## Impact:
Can bypass the review process and change the ads status to approve and active without payment process .
## Step


## Ability to use premium templates as free user via https://stripo.email/templates/?utm_source=viewstripo&utm_medium=referral
- 等级：High | 项目：Stripo | 披露：2022-03-30 | CVE：-
- 原文：https://hackerone.com/reports/1166993

- - - - - - - - 
## Summary:
Hello, I found security vulnerability in your web application, another business logic.
## Steps To Reproduce
  1. Go to https://stripo.email/templates/?utm_source=viewstripo&utm_medium=referral
  2. Choose any premium template and click [code omitted]
  3. Then sign in to save and it is in your templates
## Supporting Material/References:
Down there is video showing everything
  * [attachment / reference]
## Impact
Lose of business
---


## Add upto 10K rupees to a wallet by paying an arbitrary amount
- 等级：High | 项目：Eternal | 披露：2022-02-23 | CVE：-
- 原文：https://hackerone.com/reports/1408782

- - - - - - - - 
| TimeStamp   |      Action      |
|----------|:-------------:|
| Wed, 24 Nov 2021, 11:24 IST | Received the report |
| Wed, 24 Nov 2021, 11:25 IST | Validation and analysis of issue initiated |
| Wed, 24 Nov 2021, 11:28 IST | Vulnerability reported to the respective Internal Team |
| Wed, 24 Nov 2021, 11:36 IST | The authenticity of the issue is verified by the Security Team |
| Wed, 24 Nov 2021, 11:41 IST | Report Triaged |
| Wed, 24 Nov 2021, 14:47 IST | Fix Deployed on Production |
| Wed, 24 Nov 2021, 14:48 IST | Severity adjusted to High (7.5 CVSS) by Security Team |
| Wed, 24 Nov 2021, 15:47 IST | Fix verified by the Security Team |
| Wed, 24 Nov 2021, 16:00 IST | Fix 


## Subdomain takeover of images.crossinstall.com
- 等级：High | 项目：X | 披露：2022-01-05 | CVE：-
- 原文：https://hackerone.com/reports/1406335

- - - - - - - - 
## Summary
images.crossinstall.com points to an AWS S3 bucket that no longer exists. I was able to take control of this bucket and put my own content onto it. I can now serve content on this domain, obtain a TLS certificate for this domain, etc.
If any customers or servers are pointing to anything within this domain, I could serve them arbitrary/malicious content. I could also use this in case your domain whitelists your own domain for OAuth, or if there are cookies scoped to the entire domain. Usually this can have a high impact.
## PoC
Visit images.crossinstall.com/index.html; an HTML comment with my username is present.
[code omitted]
## Impact
Subdomain takeover
---


## s3 bucket takeover presented in https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/full-build-macos.sh
- 等级：High | 项目：Reddit | 披露：2021-10-21 | CVE：-
- 原文：https://hackerone.com/reports/1285598

- - - - - - - - 
Hey team,
## Summary:
 I have found that in the code of full-build-macos.sh in rpanstudio on github(https://github.com/reddit/rpan-studio/blob/e1782332c75ecb2f774343258ff509788feab7ce/CI/install-dependencies-osx.sh) contains a  s3 bucket which was unclaimed i.e (https://obs-nightly.s3-us-west-2.amazonaws.com)
## Steps To Reproduce:
1. Create a s3 bucket with name obs-nightly and us west 2 region
2. Upload files  with the name same as given in the code  (e.g. cef_binary_${1}_macosx64.tar.bz2)
3. Make the settings and change it as a static website 
4. You have successfully taken the s3 bucket and now when any user runs the code the url with s3 get executed and an attacker can 


## Unix time unlock_time values have dangerous validation rules enabling a number of exploits
- 等级：High | 项目：Monero | 披露：2021-09-12 | CVE：-
- 原文：https://hackerone.com/reports/854726

- - - - - - - - 
*Initially found by TheCharlatan, discussed with and expanded on by Isthmus, impacts all releases of monero and monero wallets*
## Description
The unlock_time field in monero transaction dictates when a transaction's outputs can be spent again. This rule is enforced by the consensus code in https://github.com/monero-project/monero/blob/master/src/cryptonote_core/blockchain.cpp#L3478 . The rule has two parts. If the unlock_time is below 500000000, it is interpreted as a block height and compared with the current block height. If the unlock_time in a used transaction input's previous output is below the current block height, a transaction using that output is valid. Otherwise 


## Payment method token being sent to 3rd party analytics service
- 等级：High | 项目：Upserve | 披露：2021-09-03 | CVE：-
- 原文：https://hackerone.com/reports/637267

- - - - - - - - 
Vulnerability Details:
Payment Tokens can be re-used to link the Credit Card to Another Users Account.
When Linking a Credit Card, a url with Payment_method_token will be generated and then the user will be redirected to the generated url
{F523794}
Then, a Request will be Made to [code omitted] to Finally Link the Credit Card using the payment_method_token
{F523795}
##Reproduction Steps
1.) Create 2 Accounts on https://app.upserve.com/s/upserve-lounge-test-providence-2
 * juandelacruz@gmail.com
 * juandoe@gmail.com
2.) Add a Credit Card
 * 4834422077410033|01|2023|730  - for juandelacruz@gmail.com
 * 4834422073330870|06|2024|582 - juandoe@gmail.com
3.) While Adding the Credi


## CVE-2018-6389 exploitation - using scripts loader
- 等级：High | 项目：MTN | 披露：2021-08-18 | CVE：CVE-2018-6389
- 原文：https://hackerone.com/reports/925425

- - - - - - - - 
**Issue Description**
Unauthenticated attackers can cause a denial of service (resource consumption) by using the large list of registered .js files (from wp-includes/script-loader.php) to construct a series of requests to load every file many times. 
The vulnerability is registered as [CVE-2018-6389] #761722 #752010 #753491 #335177 
**CVE ID Risk Score**
[CVE-2018-6389 7.5](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6389)
Platform(s) Affected: [website]
*.[https://www.mtn.zm/wp-admin/load-scripts.php?load=](https://www.mtn.zm/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp


## Complete destruction of the Grinch server
- 等级：High | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1065885

- - - - - - - - 
# Hackyholidays
# flag 1
First flag is just a matter of reading `/robots.txt` file:
[code omitted]
# flag 2
Visiting `/s3cr3t-ar3a` and opening it with developer tools gets the second flag:
	flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
It is inserted in the DOM via some obfuscated javascript code buried in `/assets/js/jquery.min.js`
[code omitted]
# flag3 /people-rater
The people rater app references entries via something like
	https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6Mn0=
where the id parameter is base64 encoding of  `{"id":NUMBER}`
Setting `NUMBER=1` immediatly gives the flag:
[code omitted]
# flag4 /swag-shop
The swag shop sells some itmes but in order 


## Host Header injection in oslo.io (using X-Forwarded-For header) leading to email spoofing
- 等级：High | 项目：Logitech | 披露：2021-01-07 | CVE：-
- 原文：https://hackerone.com/reports/1072277

- - - - - - - - 
#Hello team
##I hope it will be a happy year for you and for me 😇 
## Summary:
I found Host Header injection in oslo.io  
I tried to use it to show the security effect on users And I found this
## Steps To Reproduce:
 1. Well, first of all, enter your project 
2.Make an invitation by email 
3.Now through the burpsuite 
If we try to change the host, 403 will appear
  {F1145857}
So we will use  [code omitted]
 
PoC : 
{F1145858}
## Impact
Many things can be done, including deceiving the user and referring to something else or a login page and stealing their account
>>There is a lot of information about it here : 
 https://portswigger.net/web-security/host-header
---


## Named pipe connection inteception
- 等级：High | 项目：MariaDB | 披露：2020-12-17 | CVE：-
- 原文：https://hackerone.com/reports/1019891

- - - - - - - - 
With MariaDB running on Windows, when local clients connect to the server over named pipes, it's possible for an unprivileged user with an ability to run code on the server machine to intercept the named pipe connection and act as a man-in-the-middle, gaining access to all the data passed between the client and the server, and getting the ability to run arbitrary SQL commands on behalf of the connected user.
On Windows, MariaDB allows local clients to connect to the server over named pipes. Unfortunately, when creating the named pipe server, the security descriptor is not set correctly, and as a result every user on the system can create pipe server instances. This allows fo


## Attachments may be hijacked via AppCache+CookieBombing trick (bc3_production_blobs bucket)
- 等级：High | 项目：Basecamp | 披露：2020-11-26 | CVE：-
- 原文：https://hackerone.com/reports/403602

- - - - - - - - 
Basecamp attachments are stored in the `bc3_production_blobs` bucket in the root directory and can be served with `text/html` content-type. 
https://storage.googleapis.com/bc3_production_blobs/*key*?GoogleAccessId=bc3-production-storage%40bc3-production.iam.gserviceaccount.com&Expires=1535826443&Signature=*sign*&response-content-type=text/html
So with AppCache+CookieBombing trick an attacker can upload html file and if the user visit url of this file then all further uploads to this bucket and downloads from it will be hijacked by an attacker. 
To know more about this trick refer to https://labs.detectify.com/2018/08/02/bypassing-exploiting-bucket-upload-policies-signed-urls


## Manipulate Uneditable Messages in Support
- 等级：High | 项目：CS | 披露：2020-10-27 | CVE：-
- 原文：https://hackerone.com/reports/995969

- - - - - - - - 
## Summary:
Hello,
The support section has a validation on all the posted messages where it doesn't allow you to edit your messages after some minutes from posting them.
I was able to bypass this protection and edit successfully the previous messages that can't be edited.
After further investigation, I found that whenever you create/send a message, there is a date value made of numbers generated in the response which indicates the timestamp or the date that the message was created.
And when you edit that message, the same value is used as a date parameter in the edit request.
The bug is that the date parameter is still active for the unedited messages, so when you perform an


## Bypass hide download Nextcloud Share
- 等级：High | 项目：Nextcloud | 披露：2020-10-05 | CVE：-
- 原文：https://hackerone.com/reports/865777

- - - - - - - - 
## Summary
Hello everyone, accidentally browsing through nextcloud, I have found a small vulnerability on nextcloud server. This vulnerability allow download the file when the download function has been hidden
Here is the error details.
If anything is wrong please respond to me. Thanks you.
## Description
I sharing folder for another ( download not hide)
{F814529}
{F814531}
Of course, the download function is still enabled, I will have the download request as below
{F814536}
I then disabled download on the entire file folder  
{F814542}
{F814546}
But the download link created on the server does not change or change the permissions, I can completely download the file to conti


## An attacker can buy marketplace articles for lower prices as it allows for negative quantity values leading to business loss
- 等级：High | 项目：Semrush | 披露：2020-04-02 | CVE：-
- 原文：https://hackerone.com/reports/771694

- - - - - - - - 
Hi there,
When we
**Summary:** 
When someone goes to https://www.semrush.com/marketplace/offers/ and orders for articles, an attacker can pay for less than intended due to  negative quantities being allowed. 
## Steps To Reproduce:
- Go to https://www.semrush.com/marketplace/offers/
- Click on 500 Words($40) Order Now button.
- Select any two articles.
- Intercept the request:
[code omitted]
- The actual price should be $110 for two articles.
Change the JSON body to :
[code omitted]
- The cost will become $20 for two articles:
4 * $40- 2 * $70= $160 - $140 = $20
████
I even tried with my Virtual Card. Here is the failed payment. This is the proof that it actually charges the


## Race Condition allows to redeem multiple times gift cards which leads to free "money"
- 等级：High | 项目：Reverb.com | 披露：2020-01-25 | CVE：-
- 原文：https://hackerone.com/reports/759247

- - - - - - - - 
Hello team!
I've found a Race Condition vulnerability which allows to redeem gift cards multiple times. This how a s/he can easily buy stuff just bying one gift card and redeem it over and over again.
## Steps to reproduce


## Improper handling of payment callback allows topping up a Swiss Starbucks Card bypassing actual payment via a crafted success message
- 等级：High | 项目：Starbucks | 披露：2019-11-18 | CVE：-
- 原文：https://hackerone.com/reports/682617

- - - - - - - - 
khovansky uncovered that an attacker could register on https://xtras.starbucks.ch and utilizing that registration, subsequently generate a reset password email via https://card.starbucks.ch 
After resetting the password for the account, khovansky noticed this process auto generates a virtual Swiss Starbucks card. khovansky could then top up this virtual card without completing a transaction by forging a "payment successful" callback.
@khovansky — thank you for reporting this vulnerability and your assistance confirming the resolution.
---

