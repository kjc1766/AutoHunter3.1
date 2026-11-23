# HackerOne 实战案例：improper-input-validation

_18 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Remote code execution due to unvalidated file upload
- 等级：Critical | 项目：MTN | 披露：2022-09-01 | CVE：-
- 原文：https://hackerone.com/reports/1164452

- - - - - - - - 
## Summary:
Hello 
I found a critical vunerability in one of your site, where user can upload any file type as a profile picture (including php file)
## Steps To Reproduce:
1. Visit https://careers.mtn.cm and register as a user.
2. After successful registration, login and update your data.
3. When uploading profile photo, select any file type.
 4. When its updated, view the source code of the page, you will see your file with complete path.
5. Copy the file path and paste into your browser.
6. Boom your file will be executed
## Supporting Material/References:
Here i upload non-harmful file as a poc 
[code omitted]
https://careers.mtn.cm/en/user/images/users/-13-04-2021-20-15


## Economic Harm through Twitter's Cropping Algorithm
- 等级：Critical | 项目：Twitter | 披露：2021-09-08 | CVE：-
- 原文：https://hackerone.com/reports/1290872

- - - - - - - - 
## Bounty Hunter Name:
CyberQueenMeg
## About You:
Megan, also known as CyberQueenMeg, is a passionate rising cybersecurity professional who is interested in programming, cybersecurity, and web development. Megan is a high school senior in a rigorous computer science program at her high school where she has to take an advanced CS course every year and complete a 200-hour internship. Megan founded the Computer Science Club at her school, which is committed to providing CS education to all in a safe learning environment. Megan works as a freelance bug bounty hunter for HackerOne and Bugcrowd and is particularly focused on hunting for web security vulnerabilities. Megan is a na


## Underrepresentation Bias through Twitter's Cropping Algorithm #2: Favoring Animals over Black People
- 等级：Critical | 项目：Twitter | 披露：2021-09-08 | CVE：-
- 原文：https://hackerone.com/reports/1294242

- - - - - - - - 
Bounty Hunter Name:
CyberQueenMeg
About You:
Megan, also known as CyberQueenMeg, is a passionate rising cybersecurity professional who is interested in programming, cybersecurity, and web development. Megan is a high school senior in a rigorous computer science program at her high school where she has to take an advanced CS course every year and complete a 200-hour internship. Megan founded the Computer Science Club at her school, which is committed to providing CS education to all in a safe learning environment. Megan works as a freelance bug bounty hunter for HackerOne and Bugcrowd and is particularly focused on hunting for web security vulnerabilities. Megan is a national


## Underrepresentation Bias through Twitter's Cropping Algorithm
- 等级：Critical | 项目：Twitter | 披露：2021-09-08 | CVE：-
- 原文：https://hackerone.com/reports/1294062

- - - - - - - - 
Bounty Hunter Name:
CyberQueenMeg
About You:
Megan, also known as CyberQueenMeg, is a passionate rising cybersecurity professional who is interested in programming, cybersecurity, and web development. Megan is a high school senior in a rigorous computer science program at her high school where she has to take an advanced CS course every year and complete a 200-hour internship. Megan founded the Computer Science Club at her school, which is committed to providing CS education to all in a safe learning environment. Megan works as a freelance bug bounty hunter for HackerOne and Bugcrowd and is particularly focused on hunting for web security vulnerabilities. Megan is a national


## Steal ALL collateral during liquidation by exploiting lack of validation in `flip.kick`
- 等级：Critical | 项目：BlockDev | 披露：2019-10-01 | CVE：-
- 原文：https://hackerone.com/reports/684092

- - - - - - - - 
## Summary:
The `flip` contract allows for the MCD system to auction collateral in exchange for DAI.
A lack of validation in the method `flip.kick` allows an attacker to create an auction with a fake
bid value. Since the `end` contract trusts that value, it can be exploited to issue any amount of free
DAI during liquidation. That DAI can then be immediately used to obtain all collateral stored in the
`end` contract.
## Detailed Description:
The `flipper` contract (`flip.sol`) is intended to offer a way for the MCD contracts to obtain DAI by auctioning gems. An auction is initiated by calling the `flip.kick` method, which is normally done by the `cat` contract when it grabs c


## Bypass of GitLab CI runner slash fix in YAML validation
- 等级：Critical | 项目：GitLab | 披露：2019-04-10 | CVE：-
- 原文：https://hackerone.com/reports/409395

- - - - - - - - 
Hi Gitlab Security,
I notice the bug #301432 that Jobert reported earlier is could be bypassed by setting variable in environment.
The reason is that the fix in place preventing url normalization is performed by doing the YAML  validation, however this could be bypassed by setting the environment variable in `https://gitlab.com/{project_id}/settings/ci_cd`
By setting the key ONE and variable value to `../1/key`, it is possible to replicate what jobert did in #301432.
And in `.gitlab-ci.yml`
[code omitted]
Then make any change to `.gitlab-ci.yml` will trigger the bug once again.
Download from cache
{F345819}
Setting environment variable
{F345820}
Upload to cache
{F345821}
## 


## HTTP/2 server push accepts a non-authoritative :scheme=https over cleartext h2c, enabling HTTPS cache-key poisoning
- 等级：High | 项目：curl | 披露：2026-03-29 | CVE：-
- 原文：https://hackerone.com/reports/3630310

- - - - - - - - 
## Summary:
I found that libcurl 8.19.0 accepts an HTTP/2 pushed stream on a cleartext h2c connection even when the server sends `:scheme=https` in `PUSH_PROMISE`. In `lib/http2.c`, `set_transfer_url()` builds the pushed handle URL from the server-supplied `:scheme`, `:authority`, and `:path`, but `PUSH_PROMISE` validation only checks `:authority` and does not reject a non-authoritative pushed `https` origin. The accepted pushed handle is then exposed to the application and processed on the existing connection, and `CURLINFO_EFFECTIVE_URL` later returns the pushed URL from `data->state.url`. As a result, a cleartext h2c server can cause a pushed transfer to appear as `https:


## Unsafe Global IFS Modification in OS400 Shell Script Enables Command Injection and Parsing Flaws (CWE-78/CWE-20)
- 等级：High | 项目：curl | 披露：2025-08-12 | CVE：-
- 原文：https://hackerone.com/reports/3295656

- - - - - - - - 
In the curl source repository, the OS400 initialization script (packages/OS400/make-incs.sh) modifies the global shell variable IFS (Internal Field Separator) without local scoping or restoration. This pattern exposes users and CI/CD systems to unintended parsing, command injection, and logic errors if the environment or invoker is attacker-controlled or untrusted. Shell scripts that alter process-wide environment variables in this way are vulnerable to privilege escalation and unpredictable execution, especially where user input or automated tooling is involved.
This issue and its report were identified and compiled with the assistance of an AI security agent to ensure a th


## Arbitrary File Deletion Vulnerability in curl Source Code via os.unlink()
- 等级：High | 项目：curl | 披露：2025-07-07 | CVE：-
- 原文：https://hackerone.com/reports/2864414

- - - - - - - - 
## Summary:
The curl source code's testing scripts contain instances where the os.unlink() function is used to delete files without validating the input file paths. This introduces a risk of arbitrary file deletion when these scripts are executed with malicious or manipulated inputs. Although the vulnerability is present in test scripts, it could lead to unintended consequences if these scripts are used in shared or automated environments.
## Steps To Reproduce:
  1.Clone the curl repository using (https://github.com/curl/curl.git)
  2.move to tests directory.
  3.Identify the affected scripts:
      The following scripts and lines contain vulnerabilities: 
             test


## HTTP/3 Stream Dependency Cycle Exploit
- 等级：High | 项目：curl | 披露：2025-05-04 | CVE：-
- 原文：https://hackerone.com/reports/3125832

- - - - - - - - 
**Penetration Testing Report: HTTP/3 Stream Dependency Cycle Exploit**
---
# **0x00 Overview**
A novel exploit leveraging stream dependency cycles in the HTTP/3 protocol stack was discovered, resulting in memory corruption and potential denial-of-service or remote code execution scenarios when used against HTTP/3-capable clients such as `curl` (tested on version 8.13.0). This report details a practical proof of concept, required environment setup, attack execution, and crash analysis.
---
# **0x01 Environment Setup**
## **1. Malicious Server Setup (aioquic modified)**
[code omitted]
---
# **0x02 Proof-of-Concept Code**
## **1. Malicious HTTP/3 Server (exploit\_server.py)**
[


## important: Apache HTTP Server weakness with encoded question marks in backreferences (CVE-2024-38474)
- 等级：High | 项目：Internet | 披露：2024-07-13 | CVE：CVE-2024-38474
- 原文：https://hackerone.com/reports/2585381

- - - - - - - - 
I reported this vulnerability through the official Apache HTTP Server security email on April 1, 2024, and received a fix along with a CVE number on July 1, 2024. You can check detailed information from there:
> https://httpd.apache.org/security/vulnerabilities_24.html
## Impact
Substitution encoding issue in mod_rewrite in Apache HTTP Server 2.4.59 and earlier allows attacker to execute scripts in
directories permitted by the configuration but not directly reachable by any URL or source disclosure of scripts meant to only to be executed as CGI.
Users are recommended to upgrade to version 2.4.60, which fixes this issue.
Some RewriteRules that capture and substitute unsafely 


## important: Apache HTTP Server weakness in mod_rewrite when first segment of substitution matches filesystem path. (CVE-2024-38475)
- 等级：High | 项目：Internet | 披露：2024-07-13 | CVE：CVE-2024-38475
- 原文：https://hackerone.com/reports/2585378

- - - - - - - - 
I reported this vulnerability through the official Apache HTTP Server security email on April 1, 2024, and received a fix along with a CVE number on July 1, 2024. You can check detailed information from there:
> https://httpd.apache.org/security/vulnerabilities_24.html
## Impact
Improper escaping of output in mod_rewrite in Apache HTTP Server 2.4.59 and earlier allows an attacker to map URLs to filesystem locations that are permitted to be served by the server but are not intentionally/directly reachable by any URL, resulting in code execution or source code disclosure.
Substitutions in server context that use a backreferences or variables as the first segment of the substit


## CVE-2021-22924: Bad connection reuse due to flawed path name checks
- 等级：High | 项目：curl | 披露：2021-07-21 | CVE：CVE-2021-22924
- 原文：https://hackerone.com/reports/1223565

- - - - - - - - 
## Summary:
`Curl_ssl_config_matches` attempts to compare whether two SSL connections have identical SSL security options or not. The idea is to avoid reusing a connection that uses less secure, or completely different security options such as capath, cainfo or certificate/issuer pinning.
Unfortunately this function has several flaws in it:
1. It completely fails to take into account "BLOB" type certificate values, such as set by `CURLOPT_CAINFO_BLOB` and  `CURLOPT_ISSUERCERT_BLOB`. If the application can be made to initiate connection to a user specified location (where these BLOB options are not used) before the "more secure" connection using these options is made, the att


## 2FA Disable With Wrong Password - Response Tampering.
- 等级：High | 项目：8x8 | 披露：2020-10-21 | CVE：-
- 原文：https://hackerone.com/reports/893085

- - - - - - - - 
The application contained a business logic flaw that resulted in missing validation when removing 2FA on the authenticated account.
---


## Send Phishing/Spam email from support@sameroom.io to any email address.
- 等级：High | 项目：8x8 | 披露：2020-08-05 | CVE：-
- 原文：https://hackerone.com/reports/840688

- - - - - - - - 
The Sameroom API contained an endpoint to generate an email to notify the user that the account had been updated. This API request utilized a JSON body that specified the email address and DisplayName of the user without validating the format or characters of the DisplayName. An attacker could have utilized the endpoint to craft convincing spam emails that originated from the Sameroom server.
---


## HTTP header values do not have trailing OWS trimmed
- 等级：High | 项目：Node.js | 披露：2020-02-24 | CVE：CVE-2019-15606
- 原文：https://hackerone.com/reports/730779

- - - - - - - - 
[I suspect I may have tagged the wrong vulnerability type -I'm failing to find "insufficient validation of user input"]
According to the HTTP-spec, http values are
       field-value    = *( field-content | LWS )
http_parser does not appear to trim trailing LWS. This means if a user sends "Host: foo\r\n" the string literal "foo" is passed up, but if the user sends "Host: foo \r\n" the string literal "foo " is passed up, complete with trailing LWS.
## Steps To Reproduce:
(Add details for how we can reproduce the issue)
If one hands "GET / HTTP/1.1\r\nHost: foo.com \r\nHello: World\r\n\r\n"
to http_parser, http_parser sends on_header_value "foo.com " instead of "foo.com"
## Im


## Steal all MKR from `flap` during liquidation by exploiting lack of validation in `flap.kick`
- 等级：High | 项目：BlockDev | 披露：2019-09-26 | CVE：-
- 原文：https://hackerone.com/reports/684152

- - - - - - - - 
## Summary:
The `flap` contract provides the ability to auction DAI for MKR. That's a fundamental functionality of the MCD system, invoked usually from the `vow` contract.
A flaw in the validation of calls to `flap.kick`, however, allows a malicious user to create "fake' auctions that can be later used to steal MKR from `flap` during the liquidation (`end`) phase.
## Detailed description
The method `flap.kick`, used to start an auction of DAI (for MKR) in the `flap` contract, lacks any validation of the `bid` parameter. Since the method is public, a malicious user can directly invoke it, passing an arbitrary `bid` parameter -- affecting other contracts that assume this value


## Improper UUID validation results in bypass of #419896
- 等级：High | 项目：HackerOne | 披露：2018-10-25 | CVE：-
- 原文：https://hackerone.com/reports/423073

- - - - - - - - 
This was found while evaluating the vulnerability and patch identified in #419896.  I determined the deployed patch to be effective.  However, I noticed tracer values could be sent which didn't conform to the UUID specification as characters outside of the a-f and 0-9 ranges could be used.  For example, a value such as "zzzzzzzz-zzzz-zzzz-zzzz-zzzzzzzzzzzzzz" was accepted by the server as valid.  Likely this indicates a problem with a regex filter that needs to be slightly changed.  
Steps
1. Navigate to a program which allows anonymous submissions.
2. Open the report submission form and add an attachment.
3. Observe the request sent to /attachments includes a client side ge

