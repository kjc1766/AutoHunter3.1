# HackerOne 实战案例：cleartext-storage-of-sensitive-information

_19 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Unauthorized Account Access via Leaked Credentials in URL Format (Account Takeover )
- 等级：Critical | 项目：Khan | 披露：2025-05-07 | CVE：-
- 原文：https://hackerone.com/reports/3080597

- - - - - - - - 
I discovered a critical vulnerability that allows attackers to access user accounts on khanAcademy.com using credentials publicly available on VirusTotal., an attacker can directly authenticate into a user’s account without any secondary verification or alert to the user.
i have reported a similar issue , here's the report ( 2981324 ) 
this time the email and password of the victim is archived in clear text ( https://en.khanacademy.org/login,██████,,█████████,,,█████████,██████████,Personal )
by entering the mail ( ██████████ ) and password ( ███████ ) in the login , the attacker can easily perform account takeover
Please Enforce 2FA: Make two-factor authentication mandatory


## ███ leaking PII of tour visitors (names, email addresses, phone numbers) via misconfigured record permissions
- 等级：Critical | 项目：U.S. | 披露：2024-03-22 | CVE：-
- 原文：https://hackerone.com/reports/2294930

- - - - - - - - 
Dear DoD team,
The ████████ is leaking a large amount of sensitive data, including **full names, email addresses and phone numbers**. These are accessible by any registered user, as there is no additional verification. 
Any registered user of the portal is able to gain access to records other users (most likely visitors using the platform to complete security checks).
The specific vulnerable objects presenting a risk are:
Contact
Account
AccountContactRelation
As the website states that over ████████ every year, the extent of this leak may be affecting hundreds of thousands of users.
████
Hope you find this report helpful - look forward to your feedback.
## Impact
Large-scal


## Mozilla Employee's Token for sql.telemetry.mozilla.org Exposed in Git Commit
- 等级：Critical | 项目：Mozilla | 披露：2023-12-18 | CVE：-
- 原文：https://hackerone.com/reports/2193815

- - - - - - - - 
A Mozilla employee's API token for https://sql.telemetry.mozilla.org was leaked in one of our Github repos. The token provided access to the service dashboard which contained confidential data. The API token was rotated and removed from the service.  
Note that this asset is out of scope of our program, however, we accepted the report since the reported issue is critical.
---


## Mozilla FuzzManager API Token Exposed in Git Commit
- 等级：Critical | 项目：Mozilla | 披露：2023-11-29 | CVE：-
- 原文：https://hackerone.com/reports/2030076

- - - - - - - - 
The researcher has discovered that an API token for the FuzzManager of Mozilla (https://fuzzmanager.fuzzing.mozilla.org) was leaked in one of our GitHub repositories. The API token provides access to our internal fuzzing data and results. The token was accidentally configured with read-write access, we rotated the tokens and made sure to use write-only tokens in our workers
---


## Cleartext storage of sensitive information at https://staging.status.ai-apps-comms.ibm.com/env can lead to account takeover  of several IBM employees
- 等级：Critical | 项目：IBM | 披露：2022-09-09 | CVE：-
- 原文：https://hackerone.com/reports/1670586

- - - - - - - - 
Cleartext storage of sensitive information was reported to IBM, analyzed and has been remediated. Thank you to zere.
---


## Critical || Unrestricted access to private Github repos and properties of Elastic through leaked token of Elastic employee
- 等级：Critical | 项目：Elastic | 披露：2021-09-01 | CVE：-
- 原文：https://hackerone.com/reports/1266188

- - - - - - - - 
@prateek_0490 was able to gain access to private Github repositories through a leaked Github token on bitbucket. We confirmed this token was valid, and have rotated.
---


## SSN is exposed on slides, previous critical report was not fixed in an appropriate way
- 等级：Critical | 项目：U.S. | 披露：2020-06-11 | CVE：-
- 原文：https://hackerone.com/reports/874017

- - - - - - - - 
**Summary:**
SSN is exposed on slides, previous critical report was not fixed in an appropriate way
**Description:**
1. SSN is exposed on a screenshot. Slide 13th. SSN is covered by an olive/green rectangle which is moveable. The image itself was not updated. 
██████wp-content/uploads/2018/12/████████
2. The issue was previously submitted and was not fixed in an appropriate way.
https://hackerone.com/reports/█████████
3. The file is easy to find by the file name.
https://duckduckgo.com/?q=%22███%22&t=hj&ia=web
## Impact
Critical
███████ is a real person (officer) according to  ██████████
## Step-by-step Reproduction Instructions
1. Download the file ████████wp-content/upload


## Github Token Leaked publicly for https://github.sc-corp.net
- 等级：Critical | 项目：Snapchat | 披露：2018-10-08 | CVE：-
- 原文：https://hackerone.com/reports/396467

- - - - - - - - 
###Description :
GitHub is a truly awesome service but it is unwise to put any sensitive data in code that is hosted on GitHub and similar services as i was able to find github token indexed ***7 hours Ago*** by user ***██████ - Software Engineer - Snap Inc***


## Critical PII Data Exposure in ORDER_ERROR_LOG
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/3242830

- - - - - - - - 
A critical security vulnerability has been identified in the application's error logging system where the ORDER_ERROR_LOG file contains complete database insertion statements that expose Personally Identifiable Information (PII) of customers in plain text format.
#### Root Cause
The application's error handling mechanism is logging full SQL INSERT statements when database operations fail. These statements contain complete customer records including sensitive personal information that should never be stored in log files.
What Data is ExposedThe logs contain complete customer records including:
Full names
Email addresses
Phone numbers
Home addresses
Customer IDs
Transaction am


## Leaked reused password for a few Khan Academy users
- 等级：High | 项目：Khan | 披露：2025-07-12 | CVE：-
- 原文：https://hackerone.com/reports/3099978

- - - - - - - - 
I found A lot of credentials for your domain
on the Telegram bot: ███
While the exact sources of the leaked data are unknown, the volume of exposed information is substantial. This report is submitted for your review to assess and mitigate the exposure of user credentials, including emails and passwords.
Steps To Reproduce:
1-access this chatbot ===> ██████
2-start the chatbot
3 - add  www.khanacademy.org/login
4-u will get the passwords and emails just download them ███████
try
(username or email : password)
 ██████ : ███
████ : ██████
███ : ████████
## Impact
Impact
Exposure of user emails and passwords, leading to credential compromise.
Increased risk of account takeover 


## debug.log File Exposure that exposes (user/████) username and password at █████████
- 等级：High | 项目：Mars | 披露：2023-11-15 | CVE：-
- 原文：https://hackerone.com/reports/2122938

- - - - - - - - 
Summary:
Hello Team,
I have discovered a debug.log file exposure vulnerability at █████████ . This vulnerability allows an attacker to view potentially sensitive information, including (user/██████) username and password.
Details:
The vulnerability is present at █████ of the application. When a user accesses the debug.log file, the application displays detailed information about the server , error messages and debugging information. In this case, the debug.log file contains (user/██████) username and password, which can be used by an attacker to gain unauthorised access to the application.
Steps To Reproduce:
Access the debug.log file by navigating to ███████ .
Observe that 


## Sensitive Information Disclosure Through Config File
- 等级：High | 项目：MTN | 披露：2022-09-01 | CVE：-
- 原文：https://hackerone.com/reports/1397788

- - - - - - - - 
## Summary:
An attacker could gain access to sensitive information about usernames, encrypted passwords, internal IP addresses and configuration data of internal services.
## Steps To Reproduce:
- Go to https://zik.mtncameroon.net/common/queryconfig.action
## Remediation
Configure the application to not reveal sensitive information to client.
## References
https://cwe.mitre.org/data/definitions/200.html
## Impact
A malicious user is able to gain sensitive information usernames, encrypted passwords, internal IP addresses and configuration data of internal services.
---


## ████ api key exposed in github.com/███/███
- 等级：High | 项目：8x8 | 披露：2022-02-22 | CVE：-
- 原文：https://hackerone.com/reports/1454965

- - - - - - - - 
@adnanmalikinfo identified a committed API key of a 3rd party SaaS platform for social marketing.
We swiftly escalated to the repository owner, who restricted access.
---


## Leaking Rockset API key on Github
- 等级：High | 项目：Rockset | 披露：2021-03-02 | CVE：-
- 原文：https://hackerone.com/reports/1094151

- - - - - - - - 
## Summary:
We all know that Github is great, but it runs the risk of some credentials being revealed by mistake. In this case I found a Rockset API key, This API key is not in the current code, but it is visible in an old commit.
## Steps To Reproduce:
You can find the leak in this link : https://github.com/rockset/recipes/pull/19/files
[code omitted]
Then I visited the documentation of Rockset ( https://docs.rockset.com/rest-api/ ) and I found this way to check if the API key is revoke or not
[code omitted]
and I got this answer:
[code omitted]
So I could verify that it was not revoked
## Impact
I just checked that the key was not revoked. I didn't try anything with the to


## Development Application Credentials + Information Exposed
- 等级：High | 项目：Kubernetes | 披露：2020-12-03 | CVE：-
- 原文：https://hackerone.com/reports/1018413

- - - - - - - - 
**Issue Description**
When I browsed through all the JS files on prow.k8s.io I came across a link called **/config** which contains a configuration disclosure for the development files
**URL Vulnerabilities**
https://prow.k8s.io/config
**Proof On Concept**
[code omitted]
## Impact
Information Exposed + File Configuration Disclosure
---


## Sensitive information about a ██████
- 等级：High | 项目：U.S. | 披露：2020-09-21 | CVE：-
- 原文：https://hackerone.com/reports/893970

- - - - - - - - 
**Summary:**
https://████████/ is an U.S. Government (USG) Information System (IS) that is provided for USG-authorized use only.Due to some reason a document  which contains the information about a special ███ for the ████  █████ which possibly is ███████or █████.The pdf file is located at https://██████/spi/█████████.pdf and also contains some drawings for the packaging of the machine.
To confirm that it indeed was a confidential document it was found that a basic search related to this pdf returns a meta info containing a label about criminal penalties for foreign export:
"WARNING – This document contains technical data whose export is restricted by the Arms Export Control


## PII/PHI data available on web https://████████Portals/22/Documents/Meetings
- 等级：High | 项目：U.S. | 披露：2020-06-25 | CVE：-
- 原文：https://hackerone.com/reports/877598

- - - - - - - - 
**Summary:**
https://███Portals/22/Documents/Meetings contains many internal documents which likely were reviewed on meeting/meetings preparations which should not be available for public but searchable via google/bing.  Documents include: resumes, bio data form, emails (including history of medical conditions), mails, letters. 
PII/PHI exposed: name, emails, phones, medical history/condition.
**Description:**
https://███████Portals/22/Documents/Meetings contains many internal documents which likely were reviewed on meeting/meetings preparations which should not be available for public but searchable via google/bing.  Documents include: resumes, bio data form, emails (includ


## AppLovin API Key hardcoded in a Github repo
- 等级：High | 项目：X | 披露：2019-09-18 | CVE：-
- 原文：https://hackerone.com/reports/674774

- - - - - - - - 
Hello,
I found a Sensitive Data Exposure in github/mopub-android-mediation project, the AppLovin UI API key is hardcoded in source code. 
And in the comment it's mentioned that 
##"This is a unique SDK Key from AppLovin. Get yours from the AppLovin UI".
Github Link:- https://github.com/mopub/mopub-android-mediation/blob/72804166ec9f3b79cc0dcfa96bd8c813f3252794/Testing/src/main/AndroidManifest.xml#L60
Google Ads SDK reference link:- https://developers.google.com/admob/android/mediation/applovin
Thanks
Anshuman Pattnaik
## Impact
So if it's a production API key then it shouldn't be shown publicly in Github repo otherwise it can be used by other developers as it's a company pro


## Production secret key leak in config/secrets.yml
- 等级：High | 项目：Grab | 披露：2019-01-08 | CVE：-
- 原文：https://hackerone.com/reports/456997

- - - - - - - - 
**Summary:** 
Production secret key leak in config/secrets.yml
**Description:** 
In Github, http://engineering.grab.com/ secret_key_base is leaked which is present in the config/secrets.yml
## Steps To Reproduce:
  1. Go to the below GitHub URL and we can verify that secret_key_base is present.
[code omitted]
Mitigation:-
[code omitted]
## Impact
Proper Impact is explained here:-
https://stackoverflow.com/questions/44220691/rails-what-are-the-consequences-of-a-leaked-secret-key-base
We have recently received a lot of duplicate reports related to keys specified in the following URL:
`https://github.com/grab/blogs/blob/master/2017-01-29-deep-dive-into-database-timeouts-in-rail

