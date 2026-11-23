# HackerOne 实战案例：improper-restriction-of-authentication-attempts

_16 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Improper Restriction of Authentication Attempts in cURL
- 等级：Critical | 项目：curl | 披露：2025-06-28 | CVE：-
- 原文：https://hackerone.com/reports/3030158

- - - - - - - - 
## Summary:
The authentication mechanism in cURL does not properly restrict the number of failed authentication attempts, allowing an attacker to brute-force credentials. This issue affects authentication-based requests and could lead to unauthorized access if an attacker successfully guesses a valid password.
## Affected Version:
cURL version: [Specify version]
Platform: [Specify OS and environment]
(curl -V output: [Attach output])
## Steps To Reproduce:
Use a valid username but an incorrect password to make an authentication request via cURL:
curl -u valid_user:wrong_password http://target-url.com
Observe that there is no lockout or delay after multiple failed attempts.
A


## weak protection against brute-forcing on login api leads to account takeover
- 等级：Critical | 项目：Palo | 披露：2022-08-29 | CVE：-
- 原文：https://hackerone.com/reports/766875

- - - - - - - - 
## Summary:
Weak protection against brute-forcing on login API: https://api.outpost.co/api/v1/login leads to account takeover on https://www.teamoutpost.com/
## Steps To Reproduce:
* Sign in on https://www.teamoutpost.com/
███
* redirect to https://app.outpost.co/sign-in to login
█████████
* test any login credentials and review the request to https://api.outpost.co/api/v1/login
███████
* Notice the difference between the wrong user "Username does not exist" and wrong password " Password does not match username" 
████
* first we need to brute-force on username to get some valid usernames 
█████████
* We can grep on "Username does not exist" 
██████
* Here is valid usernames 


## Grinchs website takendown with various other exploits
- 等级：Critical | 项目：h1-ctf | 披露：2021-03-02 | CVE：-
- 原文：https://hackerone.com/reports/1069034

- - - - - - - - 
# The HackyHolidays
This is my first HackerOne CTF challenge writeup.
Contents:
(flag1): Day 1 (Check the files, robots.txt)
(flag2): Day 2 (one more :) jquery.min.js)
(flag3): Day 3 (People Rater)
(flag4): Day 4 (Brute Force, Swag Shop)
(flag5): Day 5 (Brute Force, Secure Login)
(flag6): Day 6 (Brute Force, My Diary)
(flag7): Day 7 (Brute Force, Hate Mail Generator)
(flag8): Day 8 (Brute Force, Forum)
(flag9): Day 9 (Brute Force, Evil Quiz)
(flag10): Day 10 (Brute Force, Signup Manager)
(flag11): Day 11 (Day 17th for me ;( ) (Brute Force, Follow the Link in Signup-Manager) Sheesh!!!
(flag12): Day 12 (TAKE DOWN GRINCH! Follow the Link provided in 11)
## Flag 1 
This was a fa


## Grinch-Networks taken down - hacky holidays CTF
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1069189

- - - - - - - - 
## Summary:
CTF Submission
[code omitted]
{F1139188}
## Steps To Reproduce:
- Day 1: /robots.txt
- Day 2: /s3cr3t-ar3a
  - inspect html
  - the flag is dynamically built
- Day 3: /people-rater
  - [https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=](https://hackyholidays.h1ctf.com/people-rater/entry?id=eyJpZCI6MX0=)
- Day 4: /swag-shop
  - [https://hackyholidays.h1ctf.com/swag-shop/api/sessions](https://hackyholidays.h1ctf.com/swag-shop/api/sessions)
  - One of the sessions has a user value `C7DCCE-0E0DAB-B20226-FC92EA-1B9043` 
  - [https://hackyholidays.h1ctf.com/swag-shop/api/user?uuid=C7DCCE-0E0DAB-B20226-FC92EA-1B9043](https://hackyholidays.h1ctf.com/swag


## A specially crafted value for the 'Cache-Digest' header causing crash in  chat.makerdao.com
- 等级：Critical | 项目：BlockDev | 披露：2020-11-02 | CVE：CVE-2020-9490
- 原文：https://hackerone.com/reports/972936

- - - - - - - - 
A specially crafted value for the 'Cache-Digest' header causing crash
---


## Password reset endpoint is not brute force protected
- 等级：High | 项目：Nextcloud | 披露：2023-07-21 | CVE：CVE-2023-35172
- 原文：https://hackerone.com/reports/1987062

- - - - - - - - 
Oversight of https://github.com/nextcloud/security-advisories/security/advisories/GHSA-v243-x6jc-42mp (https://hackerone.com/reports/1841665, but I can't judge the content there as it is not yet public).
In any case. The whole lostpassword flow is now annotated with bruteforce protection. Except the endpoint that actually matters. https://github.com/nextcloud/server/blob/master/core/Controller/LostController.php#L226-L229
An attacker can still happily try to brute force the token. Without getting throttled.
## Impact
The lostpassword flow is without actual bruteforce protection.
Security advisory at https://github.com/nextcloud/security-advisories/security/advisories/GHSA-mj


## Basic auth header on WebDAV requests is not bruteforce protected
- 等级：High | 项目：Nextcloud | 披露：2023-06-02 | CVE：CVE-2023-32319
- 原文：https://hackerone.com/reports/1879549

- - - - - - - - 
Hi Team,
I hope you are doing well.
Vulnerability Name :- Basic Authentication Bypass due to Lack of Rate Limit
Vulnerable URL :- https://efss.qloud.my/remote.php/dav/calendars/ha.ckitbharat3@gmail.com/app-generated--deck--board-5269/
Steps to Reproduce :- 1. Login --> Go to Tasks.
2. Copy private Link.
3. It looks like :- https://efss.qloud.my/remote.php/dav/calendars/ha.ckitbharat3@gmail.com/app-generated--deck--board-5269/
4. Open it in other browser .
5. It asks for username and password .
6. Username/email is in URL , enter same and for password enter random password.
7. Capture this request in burp suite.
8. There is an Auth header --> copy there value and see it's b64


## Brute Force of fabric-ca server admin account
- 等级：High | 项目：Linux | 披露：2022-08-06 | CVE：-
- 原文：https://hackerone.com/reports/411364

- - - - - - - - 
## fabric-ca server
- Default configuration maxenrollments value -1(enable outside enrollment)
- Listening 0.0.0.0:7054(easily discoved and can be reached)
- No limit to wrong password try
Above conditions result in brute force to CA server admin account
## Impact
## Attack gain a high-level permissioned account to permissioned network and can add\delete\update\query
---


## Full account takeover in ███████ due lack of rate limiting in forgot password
- 等级：High | 项目：U.S. | 披露：2022-04-20 | CVE：-
- 原文：https://hackerone.com/reports/1059758

- - - - - - - - 
##Steps:
1. Visit the link https://www.██████/██████████and enter the valid ████████.
2. You will be redirect to the page where it will ask you to fill your ████████ and ████████ that you get in your mail.
3. Enter the wrong ███ and intercept the request.
4. Then bruteforce the ███.(You can use burp intruder)
5. After valid ████████ it will aks you to create new password
##Request that I intercept
POST ███ HTTP/1.1
Host: www.███████
Connection: close
Content-Length: 197
Cache-Control: max-age=0
sec-ch-ua: "Google Chrome";v="87", " Not;A Brand";v="99", "Chromium";v="87"
sec-ch-ua-mobile: ?0
Origin: https://www.███████
Upgrade-Insecure-Requests: 1
DNT: 1
Content-Type: applicat


## No rate limit lead to otp brute forcing
- 等级：High | 项目：MTN | 披露：2021-08-16 | CVE：-
- 原文：https://hackerone.com/reports/1060541

- - - - - - - - 
## Summary:
Hello.
There is no rate limit protection in the endpoint https://mtnonline.com/nim/submit , Which could lead to brute force otp code.
## How To Reproduce:
Visit https://mtnonline.com/nim and complete all the required field and submit.
when next page load, user will be ask otp code.
Enter any five digit number and intercept the request using burp suit.
Send the request to intruder and clear all the payload except for otp.
Select brute forcer in payload type and clear the alphabetic character in character set and leave only digit.
In the min. length and max. length enter 5.
Click on attact button.
In the attached image, all the response code where  303 which means 


## Lack of rate limitation on careers site allows the attacker to brute force the verification code
- 等级：High | 项目：TikTok | 披露：2021-02-11 | CVE：-
- 原文：https://hackerone.com/reports/1075827

- - - - - - - - 
An attacker could have potentially attempted to brute force the verification code needed to reset a candidate's password by leveraging a lack of rate limiting on the TikTok careers portal. We thank @iambouali for reporting this to our team and confirming the resolution.
---


## load scripts DOS vulnerability
- 等级：High | 项目：BlockDev | 披露：2020-04-02 | CVE：CVE-2018-6389
- 原文：https://hackerone.com/reports/826238

- - - - - - - - 
load scripts DOS vulnerability
---


## Authorization for wp-admin directory are vulnerable to brute force.
- 等级：High | 项目：Stripo | 披露：2020-02-05 | CVE：-
- 原文：https://hackerone.com/reports/788420

- - - - - - - - 
The domain https://my.stripo.email in the directory /wp-admin are not blocking amount of request in the authorization form, this leads to bruteforce attack. Where the attacker are able to guess tons of passwords without getting blocked or the password field gets locked.
This attack make it possible to gain access as an admin extremely easy and quick to get a successfully login.
To test this security issue you need to visit the link https://my.stripo.email in the directory /wp-admin
Install a bruteforce tool like: Burp intruder, Wfuzz, Hydra, Ncrack
I personality use Wfuzz and Burp.
Wfuzz command in Linux terminal: wfuzz -c -w /usr/share/seclists/Passwords/Common-Credentials/


## Bruteforce in admin panel
- 等级：High | 项目：Nextcloud | 披露：2020-01-31 | CVE：-
- 原文：https://hackerone.com/reports/341074

- - - - - - - - 
Hello there,
Admin panel of your website (https://nextcloud.com/wp-login.php) is vulnerable to bruteforce attacks as their is no rate-limiting.
## Impact
Can gain access to admin panel.
To fix this, Just add rate limiting.
---


## The login of Hotor Not is Vulnerable to bruteforce.
- 等级：High | 项目：Bumble | 披露：2020-01-23 | CVE：-
- 原文：https://hackerone.com/reports/744692

- - - - - - - - 
I was able to validate that The Login of HotorNot is Vulnerable to BruteForcing .
Steps to reproduce:
1. https://hotornot.com/signin
2.Use Burp intruder attack for BruteForcing 
3.Send as many requests you want.
Fix:
Proper mitigation of BruteForcing should be done using Ratelimitng etc implementation.
## Impact
If attacker successfully Bruteforces the he/she might takeover it.Which might lead in users Privacy Violation
---


## The Uber Promo Customer Endpoint Does Not Implement Multifactor Authentication, Blacklisting or Rate Limiting
- 等级：High | 项目：Uber | 披露：2017-12-24 | CVE：-
- 原文：https://hackerone.com/reports/293359

- - - - - - - - 
## Summary
The https://cn-sjc1.uber.com/rt/users/apply-clients-promotions customer endpoint used to apply Uber promotions does not implement multifactor authentication, IP address blacklisting for multiple failed attempts, or IP address-based rate limiting to prevent brute force bearer token enumeration.
## Security Impact
Issued x-uber-tokens are able to be enumerated at rates only limited by an attacker's available bandwidth.
## Reproduction Steps
A massively parallel Golang application was configured to spawn thousands of concurrent HTTP request workers, each with a PRNG-derived  token. Unlike other endpoints within the Uber architecture, https://cn-sjc1.uber.com/rt/users

