# HackerOne 实战案例：information-disclosure

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## ASBS viewing other soldiers PII/Board/Board Voters/ETC
- 等级：Critical | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/2954320

- - - - - - - - 
**Description:**
An authenticated user, could run GraphQL queries that return sensitive information on other users. 
**Steps to reproduce it**
Please see below.
## References
Using burp suite, an authenticated user is able to do a full introspection against the target. After the introspection, a user can use Burp Suite Repeater to create custom GraphQL Queries based on information they are trying to find. 
CWE-200, CWE-284, CWE-359
## Impact
This would allow an attacker to capture data of soldiers by DoDID, to then look up other soldier data to gather board information, SSN, Clearance information, Branch information.  If a user was able to grab their own information, they co


## Netlify Authentication Token Exposed in Public Mozilla CI Logs
- 等级：Critical | 项目：Mozilla | 披露：2025-05-13 | CVE：-
- 原文：https://hackerone.com/reports/2915647

- - - - - - - - 
A critical vulnerability was discovered involving the exposure of a Netlify authentication token within publicly accessible logs. This token provided full access to the `Mozilla IT Web SRE` Netlify account, bypassing all restrictions. The token’s permissions encompassed roles such as Owner, Developer, Billing Admin, Reviewer, Publisher, and Content Editor, granting complete control over site management, deployments, billing, and content configurations. This exposed API key posed significant security risks, enabling unauthorized users to manipulate the account and its associated assets freely.
---


## The /reports/:id.json endpoint discloses potentially sensitive user attributes when reporter summary is present
- 等级：Critical | 项目：HackerOne | 披露：2025-04-01 | CVE：-
- 原文：https://hackerone.com/reports/3000510

- - - - - - - - 
Hi
The.json endpoint of any disclosed report is leaking reporter's email, OTP backup codes, reporter's phone number, "graphql_secret_token", tshirt size all the reporter account's internal details etc. 
[code omitted]`
* I was checking Hackerone's disclosed report ██████████ and suddenly during check found .json point is leaking too much data of reporter [code omitted] . I immediately reported it to you.
█████
* PoC:- Leakage of data of reporter
█████
█████
## Impact
Reporter H1 account private data disclosed
---


## Wordpress users Disclosure
- 等级：Critical | 项目：Autodesk | 披露：2025-02-12 | CVE：-
- 原文：https://hackerone.com/reports/2981756

- - - - - - - - 
we can see all the WordPress users/author with some of their information. Which can even be Personal information of employees/author. The file author-sitemap.xml at:https://www.payapps.com/author-sitemap.xml is enabled and this give the attacker many users names and emails like:
{F4036174}
## Impact
Malicious people could collect the usernames disclosed (and the admin user) and be focused throughout BF attack (as the usernames are now known), making it less harder to penetrate your systems.
---


## Public google drive link Exposes Military Orders Containing PII (Name, SSN etc..) and Operational Details
- 等级：Critical | 项目：U.S. | 披露：2025-01-24 | CVE：-
- 原文：https://hackerone.com/reports/2926447

- - - - - - - - 
**Description:**
I found google drive link `https://drive.google.com/drive/folders/█████████`  at `https://████████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55` contains pdfs at '/████ Internal/Orders' that discloses the following PII:
Full Name: ███████
Social Security Number (SSN): ███████
Home Address: ████, ██████
Marital Status: Married, 3 dependents (M03 in January 2021 orders; S00 in earlier orders)
Security Clearance Level: ███
## How to reproduce 
1. Navigate to `https://██████.aspx?Mode=ReadOnly&Id=90dd0d3b-0ed1-e76b-128f-11ebc799ba55`.
2. Below the page you will find `https://drive.google.com/drive/folders/█████████`.
3. Go to `https://drive.google.


## Pull Any Automated Record Brief
- 等级：Critical | 项目：U.S. | 披露：2024-10-25 | CVE：-
- 原文：https://hackerone.com/reports/1541740

- - - - - - - - 
**Description:** With some simple URL manipulation, an authenticated user is able to request other soldiers ARB/ORBs. 
## References
I am able to pull my own "Current Automated Record Brief", "Selection Board Record Brief", and all validated ones, then manipulate numbers in the request URL, and then pull any other valid number to pull a soldier. URL ID: "SRBHeaderID=#######"
## Impact
After pulling an ARB/ORB, someone would have access to view their last 4 SSN, Date of Birth, Place of birth, Clearance information, Mailing Address, and DODID. With most recent breaches of SSNs, one attacker would have enough information to verify and impersonate another soldier for malicious p


## two aws access key and secret key and database username and password exposed
- 等级：Critical | 项目：Mozilla | 披露：2024-10-18 | CVE：-
- 原文：https://hackerone.com/reports/2401648

- - - - - - - - 
## Summary:
hello mozilla security team i found two aws access key and secret key and database username and password exposed  in dockerhub image 
## Steps To Reproduce:
go to https://hub.docker.com/r/mozilla/commonvoice
and do pull for this image
you will find them in 
/code/scripts/test/config.json
███████
poc of  the asw keys 
████
and also 
████
reference 
{F3097699}
and the enum for it 
████████
## Supporting Material/References
  *https://hackerone.com/reports/1720278
  * https://hackerone.com/reports/1580567
## Impact
## Summary:
exposure of sensitive data lead to many serious attacks and access
A security vulnerability is identified in a Docker image hosted on Docker 


## Jira Credential Disclosure within Mozilla Slack
- 等级：Critical | 项目：Mozilla | 披露：2024-04-23 | CVE：-
- 原文：https://hackerone.com/reports/2467999

- - - - - - - - 
## Summary:
I was able to find Jira Admin API Keys disclosed within Mozilla's #███ Slack channel which was posted by a staff member of Mozilla.
## Steps To Reproduce:
  1.Navigate to the following file -█████
  2.Observe the exposed credentials on line 310-312 of the Python Script.
  3. Verify Groups with the following CURL request - `curl -u "██████:ATATT3xFfGF0V99l_█████████551CCC5D" -H "Content-Type: application/json" https://mozilla-hub.atlassian.net/rest/api/3/user/groups?accountId=████████`
 
4. Observe the following output which shows that the user is a Jira Administrator, Administrator and  Jira Service Desk user etc.
[{"name":"jira-servicedesk-users","groupId":"███"


## View any user email using the Team's audit log section
- 等级：Critical | 项目：HackerOne | 披露：2024-03-26 | CVE：-
- 原文：https://hackerone.com/reports/2404415

- - - - - - - - 
**Summary:**
Hello team, I decided to do some further testing, and I came across another endpoint that can be used to reveal user emails.


## Creation of bounties through Customer API leads to private email disclosure
- 等级：Critical | 项目：HackerOne | 披露：2024-03-26 | CVE：-
- 原文：https://hackerone.com/reports/2382120

- - - - - - - - 
**Summary:**
Hello team,
It is possible to reveal any user email using the `BountiesHistoryQuery` request.
To demonstrate this, I will make use of both the API and the graphql requests.


## Full Access to sonarQube and Docker
- 等级：Critical | 项目：U.S. | 披露：2024-03-22 | CVE：-
- 原文：https://hackerone.com/reports/2312609

- - - - - - - - 
This vulnerability involves the exposure of sensitive credentials and IP addresses in a JavaScript file. I gained access to your Hub Docker account and Sonar projects, allowing me to identify and assess the extent of the issue. The vulnerability stems from a JS file within your application that contains hard-coded sensitive credentials, such as usernames, passwords, and potentially API keys. Additionally, it exposes IP addresses associated with your infrastructure. This sensitive information is readily accessible to anyone with access to the file, making it susceptible to unauthorized access and potential misuse.
---


## Datadog api keys exposed can be used to do all the read and write access to the instance
- 等级：Critical | 项目：Mars | 披露：2024-01-25 | CVE：-
- 原文：https://hackerone.com/reports/2307933

- - - - - - - - 
The researcher identified DatadogHQ API keys and application keys embedded in a JavaScript (JS) file on the site █████. These keys could potentially provide unauthorized access to DatadogHQ services. The researcher responsibly reported the issue, providing a proof-of-concept (PoC) to demonstrate the vulnerability without exploiting it further.
---


## Access to resumes applied through LinkedIn Jobs
- 等级：Critical | 项目：LinkedIn | 披露：2023-09-22 | CVE：-
- 原文：https://hackerone.com/reports/560668

- - - - - - - - 
The security issue identified by the researcher allowed LinkedIn Recruiter seat holders to view data about job applicants that exceeded permissions. After validating the vulnerability report, a fix was deployed to production within 24 hours.
---


## Full access to InDrive jira panel via exposed API token
- 等级：Critical | 项目：inDrive | 披露：2023-06-28 | CVE：-
- 原文：https://hackerone.com/reports/1785145

- - - - - - - - 
**Description**
Hello!
Browsing through GitHub I found the following repository:
███
Looking for interesting keywords, the following file popped up:
███████
[code omitted]
The repository wasn't updated in a while, but I still decided to give it a change and try to make an API call with the auth token:
curl -i -s -k -X $'GET' \
    -H $'Host: indriver.atlassian.net' -H $'Cache-Control: max-age=0' -H $'Authorization: Basic ████' -H $'Content-Type: application/json' -H $'Sec-Ch-Ua: \"Google Chrome\";v=\"107\", \"Chromium\";v=\"107\", \"Not=A?Brand\";v=\"24\"' -H $'Sec-Ch-Ua-Mobile: ?0' -H $'Sec-Ch-Ua-Platform: \"macOS\"' -H $'Upgrade-Insecure-Requests: 1' -H $'User-Agent: Mozil


## Sensitive Data Exposure via wp-config.php file
- 等级：Critical | 项目：U.S. | 披露：2023-05-15 | CVE：-
- 原文：https://hackerone.com/reports/1912671

- - - - - - - - 
**Description:**
Hi team,
A copy of the WordPress config file wp-config.php has been found at  █████████ endpoint. It contains sensitive information, such as MySQL and AWS credentials, and various keys.
## References
https://codex.wordpress.org/WordPress_Files
## Impact
The page provides information to users who do not need it.
## System Host(s)
████████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
1. Go to: ███/wp-config.php_
2. See the information.
## Suggested Mitigation/Remediation Actions
Implement access control.
---


## HEIC image preview can be used to invoke Imagick
- 等级：Critical | 项目：Nextcloud | 披露：2023-01-07 | CVE：CVE-2021-32802
- 原文：https://hackerone.com/reports/1261413

- - - - - - - - 
The HEIC image preview provider calls into Imagick at https://github.com/nextcloud/server/blob/5d097ddb4b99673f57b8c085dedd93880ee2539d/lib/private/Preview/HEIC.php#L98-L109. This is bad as Imagick processes all kind of image types.
One can use this for example to exfiltrate arbitrary files by passing a SVG file that contains a `xlink:href` to a locally existing file. There are also other concerns with regard to SSRF and XML parsing done by Imagick.
A super naive example, uploading a file such as "test.heic" with this content will render the file "nextcloud20.png" inside it. (but you can also reference PDFs, or use it for SSRF, etc etc.
`test.heic`:
[code omitted]
Preview:
{


## springboot actuator is leaking internals at ██████████
- 等级：Critical | 项目：U.S. | 披露：2022-09-14 | CVE：-
- 原文：https://hackerone.com/reports/1662474

- - - - - - - -


## The dashboard is exposed in https://███
- 等级：Critical | 项目：U.S. | 披露：2022-09-06 | CVE：CVE-2020-7130
- 原文：https://hackerone.com/reports/1566758

- - - - - - - - 
**Description:**
At first, hello, after searching in sub-domains, the dashboard was accessed by Google Dorking Which is supposed to be protected
https://█████████l/arsys/forms/arpcp/ARPC%3AWeb%3AHier%3ADashboard/Default+Admin+View/?F536871388=1&mode=Submit&cacheid=c66791da
## References
https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure
## Impact
CWE-200
https://cwe.mitre.org/data/definitions/200.html
## System Host(s)
█████████l
## Affected Product(s) and Version(s)
website
## CVE Numbers
CVE-2020-7130
## Steps to Reproduce
After searching in Google dorking on a file extension or endpoint jspDashboard found in the URL
https://████████l/arsys/forms/ar


## SSRF via Office file thumbnails
- 等级：Critical | 项目：Slack | 披露：2022-07-05 | CVE：-
- 原文：https://hackerone.com/reports/671935

- - - - - - - - 
On August 12, 2019, a group of researchers reported an exploit path for a vulnerability in LibreOffice. Slack uses LibreOffice to process certain file types for preview. A specially crafted file uploaded to Slack could permit local file access and expose an internal Slack AWS credential for the container used to process these files. This was categorized as Critical, in our internal rubric, which is aligned with CVSSv3.
We fixed the bug on August 13th, 2019. Following a thorough investigation, Slack concluded the this vulnerability was not exploited except by the security researcher who reported this issue, and that this researcher did not gain access customer data.
The vulne


## Identify the mobile number of a twitter user
- 等级：Critical | 项目：X | 披露：2022-03-29 | CVE：-
- 原文：https://hackerone.com/reports/1225164

- - - - - - - - 
**Summary:** 
By exploiting this security vulnerability we can detect the mobile number of a twitter user.
**Description:**
This security vulnerability is of type "Information disclosure" it allows to exploit Flawed behavior of the twitter system to obtain distinct responses when different error states occur.
This security vulnerability allows to identify the mobile number of a twitter user from its USER_NAME.
## Steps To Reproduce:
We explain how to get the mobile number which is (██████████) from the following twitter user "███"==> USER_NAME = ████
1.access the following url: "████" and enter user name "██████" and click search. (see screenshot "1.PNG")
2. At this step twi


## default ████ creds on https://████████
- 等级：Critical | 项目：U.S. | 披露：2022-02-14 | CVE：-
- 原文：https://hackerone.com/reports/711662

- - - - - - - - 
**Description:**
I can log into `https://███ using` `█████` as credentials
## Impact
Can do anything an ██████████ can do in this application, Server Now 
## Step-by-step Reproduction Instructions
1. go to `https://███████`
2. log in using `██████████`
## Suggested Mitigation/Remediation Actions
use proper authentication, this might be a test account but it should still not use `███` as the creds
## Impact
logged in as ████ ██████ as shown in the screenshot
---


## The Return of the Grinch
- 等级：Critical | 项目：h1-ctf | 披露：2022-02-01 | CVE：-
- 原文：https://hackerone.com/reports/1433581

- - - - - - - - 
Read the full writeup here: https://github.com/tarifas90/CTF-Writeups-2021/blob/main/hackyholidasy2021.md
---


## Endpoint without access control leads to order informations and status changes
- 等级：Critical | 项目：Azbuka | 披露：2021-12-09 | CVE：-
- 原文：https://hackerone.com/reports/1050753

- - - - - - - - 
Closed.
---


## Improper data update process on UpdatePhabricatorIntegration mutation leads to leak of Phabricator Conduit API token.
- 等级：Critical | 项目：HackerOne | 披露：2021-04-30 | CVE：-
- 原文：https://hackerone.com/reports/1161141

- - - - - - - - 
## Details
**Title**: Improper data update process on `UpdatePhabricatorIntegration` mutation leads to leak of Phabricator Conduit API token.
**Risk**: High
**Impact**: High
**Exploitability**: High
**Target**: `base_url` parameter on `UpdatePhabricatorIntegration` mutation at `/graphql` endpoint.
## Introduction
Sensitive data exposure occurs when an application, company, or other entity inadvertently exposes personal data. Sensitive data exposure differs from a data breach, in which an attacker accesses and steals information.
## Synopsis
**Phabricator Conduit API** is using simple verification system and requires a valid api token for system bots, integrations etc to get 


## Critical Information disclosure of rtapi token for any user via https://video-support-staging.uber.com/video/api/getPopulousUser
- 等级：Critical | 项目：Uber | 披露：2021-03-29 | CVE：-
- 原文：https://hackerone.com/reports/953649

- - - - - - - - 
The researcher has identified that the API endpoint  can be leveraged to return a sensitivetoken that can be leveraged for access to rtapi endpoints. As example change x-uber-token value with the following found code:
---


## Duplicate Entry of email leads to 500 Server Error which disclosing the SQL Database table information
- 等级：Critical | 项目：Kartpay | 披露：2021-03-14 | CVE：-
- 原文：https://hackerone.com/reports/1082891

- - - - - - - - 
The Issue was with the process of Deletion of the merchant data from the admin Dashboard. The Admin has rights to delete the merchant email ID and further, it gets deleted as Soft delete, not the full delete but there was no Validation to the codes which can detect the re-registration of the same Email ID which leads to the Critical error. 
Secondly, it was found that while pushing the codes in the production, The Debug was enabled and show the data only needed for internal use.
---


## critical information disclosure
- 等级：Critical | 项目：U.S. | 披露：2021-03-11 | CVE：-
- 原文：https://hackerone.com/reports/1106009

- - - - - - - - 
##Description:
hey all ,
I have found critical information through this endpoint /██████;
this endpoint contains all env vars used in a  www.██████ such as server credentials, db ,mail , twitter client_id and client_secret , facebook client_id and client_secret, etc...
## Impact
full access control on  every services on website
## System Host(s)
www.█████████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Go to
https://www.█████████/████████; 
you need to put ; to bypass 401 error
## Suggested Mitigation/Remediation Actions
---


## critical information disclosure
- 等级：Critical | 项目：U.S. | 披露：2021-03-11 | CVE：-
- 原文：https://hackerone.com/reports/1106505

- - - - - - - - 
##Description:
hey all ,
I have found critical information through this endpoint ████
on ███████  DB credentials such as DB_NAME,DB_USER,DB_PASSWORD,DB_HOST, etc..
## Impact
full access control on DB service on website
## System Host(s)
███
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Go to 
██████/████████?aam-media=1
you nedd to put ?aam-media=1  to bypass blank page
## Suggested Mitigation/Remediation Actions
---


## Information Disclosure(PHPINFO/Credentials) on DoD Asset
- 等级：Critical | 项目：U.S. | 披露：2021-03-11 | CVE：-
- 原文：https://hackerone.com/reports/883693

- - - - - - - - 
**Summary:**
A DoD leaks credentials on a phpinfo() page.
**Description:**
https://███ publicly displays a phpinfo() page that leaks system information and credentials.
## Impact
The impact is medium not only due to information leakage of numerous different details such as system information but also the leakage of domain credentials.
USERDOMAIN	███████
USERNAME	██████
█████████PASSWORD']	████████
## Step-by-step Reproduction Instructions
1. Visit: https://████/████
2. Information Disclosed
## Suggested Mitigation/Remediation Actions
████████ BAT  suggests removing the ███ page or requiring authentication before making it accessible.
## Impact
The impact is medium not only d


## Disclosure of Merchant_id into the source code without entered OTP code leads to Victims MID takeover.
- 等级：Critical | 项目：Kartpay | 披露：2021-03-08 | CVE：-
- 原文：https://hackerone.com/reports/1082288

- - - - - - - - 
The System Encryption for the merchant registration was revealing the details which can be further exploitable for the Registration of the merchant. After sharing the details by the @bugera it was fixed by the team.
---


## h1-ctf : 12 days of hack holiday writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-14 | CVE：-
- 原文：https://hackerone.com/reports/1069175

- - - - - - - - 
# Summary
This was a real fun CTF and I really enjoyed solving the challenges. Great job on creating the challenges. 
This is my writeup for the "12 Days of Hacky Holidays CTF". I hope you enjoy reading it, and I hope others reading it will pick up a trick or two.
# Flags:
This is all the flags found during the CTF
* Flag 1: flag{48104912-28b0-494a-9995-a203d1e261e7}
* Flag 2: flag{b7ebcb75-9100-4f91-8454-cfb9574459f7}
* Flag 3: flag{b705fb11-fb55-442f-847f-0931be82ed9a}
* Flag 4: flag{972e7072-b1b6-4bf7-b825-a912d3fd38d6}
* Flag 5: flag{2e6f9bf8-fdbd-483b-8c18-bdf371b2b004}
* Flag 6: flag{18b130a7-3a79-4c70-b73b-7f23fa95d395}
* Flag 7: flag{5bee8cf2-acf2-4a08-a35f-b48d5e979


## HackyHolidays 2020 Full Write-up: Information Disclosure of 12 Flags
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1068434

- - - - - - - - 
## Intro
This is my report for the 2020 Hacky Holidays HackerOne CTF. I managed to find all 12 flags with the assistance of my little helper, Jake. He specialises in brute-forcing via a unique keyboard mashing technique:
{F1134543}
Anywho, let's get started...
## Flag 1: Robots
The first one was a nice easy find as a result of some basic enumeration.
Looking in [/robots.txt](https://hackyholidays.h1ctf.com/robots.txt), I immediately spotted the flag:
[code omitted]
Flag: `flag{48104912-28b0-494a-9995-a203d1e261e7}`
## Flag 2: Moved
The content of the `robots.txt` file also contained a clue about the second flag:
[code omitted]
There was a [/s3cr3t-ar3a](https://hackyholidays


## How The Hackers Saved Christmas
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1069335

- - - - - - - - 
{F1139789}
# Challenge I 🤖
"What are you doing?" I asked myself. I was about to trespass a clear warning to **keep out**.
{F1139744}
"Have you lost your mind?" But I couldn't help it. I was born for this. And I wasn't going to back down. There are 12 more days until Christmas Eve, and I wasn't going to let a green furry dude destroy everything.
Let me backtrack a few days earlier. I minded my own business, prepping the Christmas tree on an old Elvis Presley album. I had planned holidays for my family and me, for a much-deserved getaway together.
Somehow I ended up on Twitter, just checking up on things from all my favorite hackers.
Suddenly my mood changed when I saw this tw


## Admin Reseller Account Disclosure
- 等级：Critical | 项目：8x8 | 披露：2020-12-15 | CVE：-
- 原文：https://hackerone.com/reports/879562

- - - - - - - - 
The vendor that handles 8x8 Resellers had inadvertently exposed account credentials. The information was removed and credentials changed.
**Summary (researcher):**
Leaked admin account of third party reseller in github with full access to all files.
---


## Leaked DB credentials on https://██████████.mil/███
- 等级：Critical | 项目：U.S. | 披露：2020-12-03 | CVE：-
- 原文：https://hackerone.com/reports/761790

- - - - - - - - 
**Summary:**
Information disclosure with login credentials for ms-sql database exposed. 
**Description:**
I've found a PHP info file disclosed on https://█████.mil/██████ containing login credentials for a database cloud server (███████) as well as information on the host system such as hostname, username and full paths. The database server is up, but I have not tried connecting to it with the credentials, as I feel that would be going too far. 
## Impact
Possible access to database as well as disclosure of sensitive host information. 
## Step-by-step Reproduction Instructions
1. Go to https://██████████.mil/████████
2. Search for 'password', you should see this: 
    `Data 


## Open SonarQube instance leaking internal source code
- 等级：Critical | 项目：Equifax-vdp | 披露：2020-09-03 | CVE：-
- 原文：https://hackerone.com/reports/947946

- - - - - - - - 
# Summary
I came across an open SonarQube instance which can be found here: http://34.238.92.229:9000/
In this, there are 10 projects with a total of around 100k lines of code
To identify the owner, I went to the Issues tab and expanded the list of authors. There were 29 people there, and many of them were Equifax employees (I reached this conclusion because they have @equifax.com email id). 
Some of the projects there in the instance are related to authentication and APIs. One of the largest projects there is called zoomv2
Owing to the sensitive nature of the leakage, I did not dig deeper through the source code, however, I believe that this much information is enough for a


## Sensitive Information Disclosure
- 等级：Critical | 项目：Dropcontact | 披露：2020-08-21 | CVE：-
- 原文：https://hackerone.com/reports/963352

- - - - - - - - 
we were displaying sensitive information.
**Summary (researcher):**
While testing the site i was able to disclose sensitive information such as username, passwords, api keys, etc due to DEBUG = True .This bug arose due to default configuration at the backend. Now the bug is fixed. Thanks to  the team for the quick fix!
---


## h1-ctf writeup , finally paid the payments by chaining multiple bugs
- 等级：Critical | 项目：h1-ctf | 披露：2020-06-18 | CVE：-
- 原文：https://hackerone.com/reports/894110

- - - - - - - - 
# Summary:
Ultimate aim is to pay the payments of hackerone using bounty pay with no use privileges at starting.
Given scope is : *.bountypay.h1ctf.com
**Enumerated subdomains are :**
  1. www.bountypay.h1ctf.com
  2. app.bountypay.h1ctf.com
  3. staff.bountypay.h1ctf.com
  4. api.bountypay.h1ctf.com
  5. software.bountypay.h1ctf.com (cant access gloabally)
The overall CTF can be divided into levels, at each level we work with one subdomain.
**Lets make the road map to the CTF:**
  1. Login into the **app.bountypay.h1ctf.com** (using **git repo files**, 2FA bypass)
  2. **SSRF** in **load transactions** to access **software.bountypay.h1ctf.com** and getting **BountyPay.apk**


## gitlab-workhorse bypass in Gitlab::Middleware::Multipart allowing files in `allowed_paths` to be read
- 等级：Critical | 项目：GitLab | 披露：2020-06-08 | CVE：-
- 原文：https://hackerone.com/reports/850447

- - - - - - - -


## China – Limited Partner PII Regarding Work Scheduling via Unauthenticated API Endpoint
- 等级：Critical | 项目：Starbucks | 披露：2020-04-01 | CVE：-
- 原文：https://hackerone.com/reports/659248

- - - - - - - - 
0xpatrik discovered an unauthenticated API endpoint that allowed retrieval of specified work leave dates of designated Starbucks employees in China.
@0xpatrik — thank you for reporting the original vulnerability and for confirming the resolution.
---

