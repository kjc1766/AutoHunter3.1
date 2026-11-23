# HackerOne 实战案例：information-exposure-through-directory-listing

_6 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Directory listing vulnerability is disclosing names and emails, widespread (thousands of records, publicly accessible without auth)
- 等级：Critical | 项目：curl | 披露：2026-01-14 | CVE：-
- 原文：https://hackerone.com/reports/3509437

- - - - - - - - 
## Summary:
[directory listing vulnerability is disclosing names and emails and so many other sensitive information, that significantly increases the severity because these are considered as PII (Personally Identifiable Information). Thousands of records, publicly accessible without auth also can be referred as sensitive user base. It has very high impact on Confidentiality as (names and emails are being disclosed).]
[Do **not** use an AI to generate the report]
## Affected version
[https://curl.se/dev/inbox/]
## Steps To Reproduce:
[add details for how we can reproduce the issue]
  1. [Navigate to the the normal URL : https://curl.se/]
  2. [Now try to access a directory /d


## Information Disclosure Due To exposed .env file (Directory Listing) at ████████
- 等级：High | 项目：AWS | 披露：2024-10-22 | CVE：-
- 原文：https://hackerone.com/reports/2784712

- - - - - - - - 
A .env file was discovered on the server at ████, exposing sensitive application configurations, including database credentials, email settings, and more. This information could allow an attacker to gain unauthorized access to critical systems and services.
**Steps to Reproduce:**
1. Open a web browser.
2. Navigate to ████████.
3. The .env file content is displayed, revealing sensitive information.
**PoC Video Link:** ██████
## Impact
The exposed .env file could lead to multiple security threats, including but not limited to:
Unauthorized database access using DB_HOST, DB_USERNAME, and DB_PASSWORD.
Compromise of email services via MAIL_USERNAME and MAIL_PASSWORD.
Ability to 


## Information Exposure Through Directory Listing
- 等级：High | 项目：Mars | 披露：2023-06-23 | CVE：-
- 原文：https://hackerone.com/reports/1948562

- - - - - - - - 
## Summary:
Directory listing is a web server function that displays the directory contents when there is no index file in a specific website directory. It is dangerous to leave this function turned on for the web server because it leads to information disclosure.
## Steps To Reproduce:
Go to this URL:  ███
You can see logs files
████
████████
## PoC:
[code omitted]
[code omitted]
## Impact
Information Disclosure
---


## Information Exposure Through Directory Listing
- 等级：High | 项目：Tor | 披露：2021-08-27 | CVE：-
- 原文：https://hackerone.com/reports/1316412

- - - - - - - - 
##Vulnerability description
The web server is configured to display the list of files contained in this directory. This is not recommended because the directory may contain files that are not normally exposed through links on the web site.
##Link as POC:
https://www.torproject.org/static/
https://www.torproject.org/static/css/
https://www.torproject.org/static/findoc/
https://www.torproject.org/static/fonts/
https://www.torproject.org/static/js/
https://www.torproject.org/static/images/
https://www.torproject.org/static/keys/
For obvious reasons, I can not check whether this service is in scope, thats why i haven't searched for any critical informations and haven't check tok


## Source code disclosed via S3 Bucket
- 等级：High | 项目：Ruby | 披露：2020-02-13 | CVE：-
- 原文：https://hackerone.com/reports/778931

- - - - - - - -


## If the developer forgets to remove the built in controller welcome.php it helps the attacker to identify that the site is built with Codeigniter
- 等级：High | 项目：CodeIgniter | 披露：2017-10-18 | CVE：-
- 原文：https://hackerone.com/reports/278225

- - - - - - - - 
The attacker can check the website's backend technology simply by typing site_name/index.php/welcome/index it will display the codeigniter welcome page if the developer dosen't removed the built in controller and view welcome.php and welcome_message.php i attaching a screenshot below as a proof of concept
---

