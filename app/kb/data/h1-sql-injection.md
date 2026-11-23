# HackerOne 实战案例：sql-injection

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Complete authentication bypass to admin permissions
- 等级：Critical | 项目：Rocket.Chat | 披露：2026-04-22 | CVE：CVE-2026-29198
- 原文：https://hackerone.com/reports/3564655

- - - - - - - - 
A NoSQL injection vulnerability in Rocket.Chat allows unauthenticated remote attackers to bypass authentication and perform account takeover. By passing a MongoDB operator as the access_token query parameter (e.g., ?access_token[$ne]=null), an attacker can match the first OAuth token in the database without supplying valid credentials. Exploitation requires at least one OAuth token to exist in the database. Affected versions: <8.3.0, <8.2.1, <8.1.2, <8.0.3, <7.13.5, <7.12.6, <7.11.6, and <7.10.9.
---


## SQL Injection vulnerability found on ibm.com endpoint
- 等级：Critical | 项目：IBM | 披露：2026-03-12 | CVE：-
- 原文：https://hackerone.com/reports/3578842

- - - - - - - - 
SQL Injection vulnerability found on ibm.com endpoint was reported to IBM, analyzed and has been remediated. Thank you to our external researcher @cr3ckerxploit.
**Summary (researcher):**
A time-based blind SQL Injection vulnerability was discovered in a legacy CGI script (NEWaptresults.cgi) on an official IBM events subdomain. The learnpaths GET parameter did not properly sanitize user input, allowing an unauthenticated attacker to inject malicious SQL code.
Using both manual testing and automated tools, it was confirmed that the backend database would execute arbitrary queries. The injection was verified via time-based payloads (e.g., SLEEP(5)), which caused a measurable d


## SQLi At `███████` via `theme_name`
- 等级：Critical | 项目：Mars | 披露：2026-02-24 | CVE：-
- 原文：https://hackerone.com/reports/3293803

- - - - - - - - 
A critical SQL injection vulnerability was discovered in a web application's theme selection endpoint through the theme_name parameter. Using SQLMap, the researcher demonstrated both error-based and time-based blind injection attacks against a MySQL database (version 5.1+). The exploitation successfully enumerated thirteen databases, including sensitive repositories for authentication, payment, and security data. The development team promptly implemented fixes using parameterized queries and input validation. Post-remediation testing confirmed the vulnerability was fully resolved. We appreciate the detailed proof-of-concept and responsible disclosure that facilitated swift r


## SQLi at █████ parameter
- 等级：Critical | 项目：Mars | 披露：2026-02-24 | CVE：-
- 原文：https://hackerone.com/reports/3277276

- - - - - - - - 
A critical SQL injection vulnerability was discovered in an items endpoint that accepted unauthenticated POST requests without CSRF validation. The vulnerability allowed attackers to execute arbitrary SQL commands, extract database metadata including PostgreSQL version and user accounts, and perform time-based blind injection attacks. Additional security issues included stored XSS through the description parameter and complete lack of authentication controls. The endpoint was successfully exploited to reveal database schema information and demonstrate data injection capabilities. The vulnerability was promptly remediated by the security team, and we appreciate the thorough r


## SQL injection identified on IBM endpoint.
- 等级：Critical | 项目：IBM | 披露：2026-01-07 | CVE：-
- 原文：https://hackerone.com/reports/2830573

- - - - - - - - 
SQL injection identified on IBM endpoint was reported to IBM, analyzed and has been remediated. Thank you to our external researcher @rakibhqsec7.
---


## SQL Injection in Django ORM via Unvalidated `_connector` in Q Objects
- 等级：Critical | 项目：Django | 披露：2025-11-06 | CVE：-
- 原文：https://hackerone.com/reports/3335709

- - - - - - - -


## SQL Injection when using FilteredRelation
- 等级：Critical | 项目：Django | 披露：2025-09-15 | CVE：-
- 原文：https://hackerone.com/reports/3292573

- - - - - - - - 
Hi Django team :)
Vulnerability location:
https://github.com/django/django/blob/main/tests/filtered_relation/tests.py#L124
You may create my POC function above the "test_select_related_foreign_key" function:
[code omitted]
SQL Query:
`SELECT "filtered_relation_book"."id", "filtered_relation_book"."title", "filtered_relation_book"."author_id", "filtered_relation_book"."editor_id", "filtered_relation_book"."number_editor", "filtered_relation_book"."editor_number", "filtered_relation_book"."state", author_join2"."id", author_join2"."name", author_join2"."content_type_id", author_join2"."object_id" FROM "filtered_relation_book" INNER JOIN "filtered_relation_author" author_join2"


## SQLi | in URL paths
- 等级：Critical | 项目：MTN | 披露：2025-03-06 | CVE：-
- 原文：https://hackerone.com/reports/2958619

- - - - - - - - 
## Summary:
A SQL Injection vulnerability was discovered in the customerId parameter of the URL path:
`███████`
We can observe this by adding a little quote in the customerId:
█████████
which will show the following error, indicating that its vulnerable to SQL Commands Injection:
███████
## Steps To Reproduce:
We can use any SQL Commend here, by just closing the Statement ( putting `')` and then use a command and also we make sure to make the rest as a comment, here is a basic SQL command i used:
███████
or we can use tools like SQLmap to get access to the database, here is the command i used:
[code omitted]
██████
## Impact
## Summary:
An attacker can exploit this to dump a


## SQL injection in URL path leads to Database Access
- 等级：Critical | 项目：MTN | 披露：2025-01-08 | CVE：-
- 原文：https://hackerone.com/reports/2633959

- - - - - - - - 
## Summary:
The application https://corporate.admyntec.co.za/ application has an SQL injection in the URL paths since it takes the ID numbers in there and insert them directly into the backend SQL query without sanitizing them. In the registration, user ID number(Passport or National ID), Organization number are requested, as well as relevant docs. These are all stored in the backend Database.
https://corporate.admyntec.co.za/customerInsurance/newCustomerStep8/userId/868878/customerId/732562'/contactPersonId/0
## Steps To Reproduce:
  1. Using the URL generated when we get displayed the Insurance.   
{F3484515}  
  2. Introduce a single quote next to the customerId number an


## SQL injection in /errors/viewbuild/
- 等级：Critical | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/690349

- - - - - - - - 
A SQL injection vulnerability was found on a partner-facing tool that allowed queries against a legacy backing store.
**Summary (researcher):**
.
---


## Blind SQL Injection on █████ via URI Path
- 等级：Critical | 项目：Mars | 披露：2024-02-14 | CVE：-
- 原文：https://hackerone.com/reports/2266081

- - - - - - - - 
Time-based SQL injection is a hacking technique that capitalizes on vulnerabilities in systems interacting with databases. Unlike traditional SQL injection methods that directly manipulate data, this approach leverages delays in database processing to extract information. Attackers insert malicious SQL statements into input fields of web applications lacking sufficient security measures. If successful, these statements execute against the database, and by intentionally causing delays in processing, the attacker can infer information about the database structure or obtain sensitive data based on the application's response time to specific queries.
---


## SQL Injection on prod.oidc-proxy.prod.webservices.mozgcp.net via invite_code parameter - Mozilla social inscription
- 等级：Critical | 项目：Mozilla | 披露：2024-01-30 | CVE：-
- 原文：https://hackerone.com/reports/2209130

- - - - - - - - 
Hi everyone,
Hope you are well ! 
I wanted to play on [https://mozilla.social](https://mozilla.social), however this requires a user account and an invitation code as it's not open to the public. When entering an invitation code, the user is redirected to `prod.oidc-proxy.prod.webservices.mozgcp.net`.
{F2773206}
Playing around with what's on offer, I've noticed that the `invite_code` parameter is vulnerable to a PostgreSQL injection.
## Steps To Reproduce:
During registration, the following POST request is made : 
[code omitted]
Adding a single quote to the `invite_code` parameter returns a 500 error, and adding a second quote returns a 200. **Red flag**
After a few tests, h


## SQL injection at ███████
- 等级：Critical | 项目：Sony | 披露：2024-01-24 | CVE：-
- 原文：https://hackerone.com/reports/2256032

- - - - - - - - 
The researcher reported that a Sony website was vulnerable to an error-based SQL injection. The researcher was able to demonstrate the vulnerability by using SQLMap to extract data from the database such as database names.
---


## SQL Injection at https://████ via ███ parameter
- 等级：Critical | 项目：Sony | 披露：2023-04-24 | CVE：-
- 原文：https://hackerone.com/reports/1935151

- - - - - - - - 
The researcher reported that a Sony website was vulnerable to a time-based SQL injection. The researcher was able to demonstrate the vulnerability by running a sleep() command on the underlying database. The researcher then used SQLMap to extract data from the database such as table names, the database user name, and the database hostname.
---


## Time Based SQL Injection
- 等级：Critical | 项目：U.S. | 披露：2023-04-20 | CVE：-
- 原文：https://hackerone.com/reports/1878584

- - - - - - - - 
Hello and greetings and respect to you, dear friends
We all know that the sql injection bug is very dangerous, so this bug should be eliminated as soon as possible.
I've identified an SQL injection vulnerability of  type  Time Based on█████████ ██████ 
Below, we see how we found this vulnerability 
If you look carefully, we see that search in the website name Search results The gap has occurred there
as you can see ████████ Method  [██████████████/?███████ ]
now it's time to inject or generate POC with lovely tool sqlmap 
We used a text file here by Name request.txt
and this is our command in sqlmap you can use this command for your own confidence
███ █████████
=============


## SQL Injection through /include/findusers.php
- 等级：Critical | 项目：ImpressCMS | 披露：2022-10-06 | CVE：-
- 原文：https://hackerone.com/reports/1081145

- - - - - - - - 
## Summary:
The vulnerability is located in the `/include/findusers.php` script:
[code omitted]
User input passed through the "groups" POST parameter is not properly sanitized before being passed to the `icms_member_Handler::getUserCountByGroupLink()` and `icms_member_Handler::getUsersByGroupLink()` methods at lines 281 and 294. These methods use the first argument to construct a SQL query without proper validation:
[code omitted]
This can be exploited by remote attackers to e.g. read sensitive data from the "users" database table through boolean-based SQL Injection attacks.
## ImpressCMS branch :
The vulnerability has been tested and confirmed on ImpressCMS version 1.4.2 (t


## Regex account takeover
- 等级：Critical | 项目：Rocket.Chat | 披露：2022-09-22 | CVE：CVE-2022-32211
- 原文：https://hackerone.com/reports/1581059

- - - - - - - - 
**Summary:**
 get admin  reset token with authenticated user
**Description:** 
normal user login can access to  admin reset token and set a new password for admin user
## Releases Affected:
  * 3.18.5
* 3.0.5
## Steps To Reproduce (from initial installation to vulnerability):
(Add details for how we can reproduce the issue)
  1. login with low privilege user 
  2. copy rc_uid and rc_token for script
  3. request for admin email password you can find admin mail with the script 
  4. run python script to get reset token with "blind no SQL injection" ( regex search )
## Supporting Material/References:
  * 
## Suggested mitigation
  * [list any suggested patches or steps to miti


## sql injection via https://setup.p2p.ihost.com/
- 等级：Critical | 项目：IBM | 披露：2022-06-17 | CVE：-
- 原文：https://hackerone.com/reports/1567516

- - - - - - - - 
A SQL Injection against an IBM domain was reported to IBM, analyzed and has been remediated. Thank you to exploitmsf.
.
---


## SQL injection in URL path processing on www.ibm.com
- 等级：Critical | 项目：IBM | 披露：2022-05-06 | CVE：-
- 原文：https://hackerone.com/reports/1527284

- - - - - - - - 
A blind SQL injection in URL path processing on www.ibm.com was reported to IBM, analyzed and has been remediated. Thank you to @asterite.
**Summary (researcher):**
Blind SQL injection was present in URL path processing on www.ibm.com. An interesting thing is that the vulnerability was present in, essentially, any path, one could put a single quote right after the leading slash in path to start exploiting it.
SQL query result was not reflected in server response and server response after exploitation attempt was always erroneous, but it differed depending on whether SQL query failed or not.  If SQL query (influenced by our injection attack vector) did not fail, server respon


## SQL Injection on https://soa-accp.glbx.tva.gov/ via "/api/" path - VI-21-015
- 等级：Critical | 项目：Tennessee | 披露：2022-04-26 | CVE：-
- 原文：https://hackerone.com/reports/1125752

- - - - - - - - 
## Summary:
 
i've found this subdomain [code omitted] also is vulnerable to SQLI through /api/ path
## Steps To Reproduce:
[code omitted] hostname dumped
[code omitted] 
Microsoft SQL Server 2017 (RTM-CU22-GDR) (KB4583457) - 14.0.3370.1 (X64) \n\tNov  6 2020 18:19:52 \n\tCopyright (C) 2017 Microsoft Corporation\n\tEnterprise Edition (64-bit) on Windows Server 2012 R2 Standard 6.3 <X64> (Build 9600: ) (Hypervisor)\n
also you can retest it through time bassed trick
[code omitted]
{F1230364}
## Impact
An attacker can manipulate the SQL statements that are sent to the MySQL database and inject malicious SQL statements. The attacker is able to change the logic of SQL statements 


## SQL Injection in █████
- 等级：Critical | 项目：U.S. | 披露：2022-04-07 | CVE：-
- 原文：https://hackerone.com/reports/1489744

- - - - - - - - 
## References
## Impact
By using SQL injection, an attacker can exfiltrate the whole database, and gain RCE
## System Host(s)
████
## Affected Product(s) and Version(s)
████
## CVE Numbers
## Steps to Reproduce
POC 1 - curl command injecting query, returning database version:
curl https://█████████ -X POST -data="url=%2F████████&███████=AA'+OR(cast(version as date))LIKE'A" -k
POC 2 - curl command injecting query, returning current database:
curl https://███████████████ -X POST -data="url=%2F██████████&███=AA'+OR(cast(current_user as date))LIKE'A" -k
{"msg":"fail","err":"ERROR: invalid input syntax for type timestamp: \"████\""}
POC 3 - curl command injecting query, returning


## Saving Christmas from Grinchy Gods
- 等级：Critical | 项目：h1-ctf | 披露：2022-02-01 | CVE：-
- 原文：https://hackerone.com/reports/1434017

- - - - - - - - 
#
**Summary (researcher):**
It was a fun CTF to play had some good learning on thinking of how to approach real world targets and more things we can try while testing any target , some nudges were good and reminded of scenarios of actual microservices are built where these security issues can be present
huge shoutouts to  Adam and Congon4tor and h1 team for making this CTF live
The writeup is posted at  https://medium.com/@akshanshjaiswal/h1-ctf-hacky-holidays-writeup-20722289be03
---


## SQL Injection leads to retrieve the contents of an entire database.
- 等级：Critical | 项目：BlockDev | 披露：2021-12-29 | CVE：-
- 原文：https://hackerone.com/reports/1002641

- - - - - - - - 
SQL Injection leads to retrieve the contents of an entire database.
---


## SQL Injection in IBM access control panel & Broken access in admin panel
- 等级：Critical | 项目：IBM | 披露：2021-10-18 | CVE：-
- 原文：https://hackerone.com/reports/1355817

- - - - - - - - 
An application endpoint was found to be vulnerable to SQL Injection caused by a lack of sanitation on the client_id parameter. An adversary would eventually be able to read sensitive data from the database, or modify it as well as to execute administration operations. This was reported to IBM and remediated.
---


## Blind SQL Injection
- 等级：Critical | 项目：MTN | 披露：2021-08-14 | CVE：-
- 原文：https://hackerone.com/reports/1069531

- - - - - - - - 
hello dear support
I have found Blind SQL Injection on https://futexpert.mtngbissau.com/signin/
parameters injectable phone_number=0&pin=1&submit=Continuar via post
URL:https://futexpert.mtngbissau.com/signin/
Post: email=0
my payload : phone_number=0'XOR(if(now()=sysdate()%2Csleep(0)%2C0))XOR'Z&pin=1&submit=Continuar
HTTP request
==========
[code omitted]
if you need more info I'm here thank you
## Impact
An attacker can use SQL injection it to bypass a web application's authentication and authorization mechanisms and retrieve the contents of an entire database. SQLi can also be used to add, modify and delete records in a database, affecting data integrity. Under the right 


## SQL Injection on the administrator panel
- 等级：Critical | 项目：MTN | 披露：2021-07-29 | CVE：-
- 原文：https://hackerone.com/reports/865436

- - - - - - - - 
Hello team. The admin panel of the website is mtngbissau.com or is vulnerable to sql attack via https://mtngbissau.com/webadmin/index.php
## Request 
[code omitted]
Confirmation of the vulnerability with sqlmap
[code omitted]
## Impact
Web application is vulnerable to SQL injection, allowing access to data
---


## ccc ctf
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-23 | CVE：-
- 原文：https://hackerone.com/reports/1216085

- - - - - - - - 
██████████
will send  detailed report later
## Impact
can get admin credentials
**Summary (researcher):**
We are given this website 
	https://ccc.h1ctf.com/
We can register a user which is assigned a user hash. In our case we got `8y399q` as user hash. Once logged in the page `/u/8y399q` just says:
	: Remote File list not found
The website points to a twitter account `https://twitter.com/DesignsCcc`. There we find a picture with a browser opened on the website we are attacking. One tab of the browser seems to point to: `/error_-_-_log.txt`
We are able to confirm that this file exists and it contains
	File: https://h1-wfzfi4.s3.eu-west-2.amazonaws.com/files.xml Not Found
	Fil


## 100K CTF's Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-21 | CVE：-
- 原文：https://hackerone.com/reports/1216591

- - - - - - - - 
Limited disclosure based on researcher's request.
**Summary (researcher):**
Hello everyone,
We are one of the winners of 100k CCC CTF and we would like to congratulate all the other winners of the CTF as well.
Here is the link to our write-up https://blog.dexter0us.com/posts/ccc-h1ctf/ hope you guys enjoy reading it and learn something new from it. 
:)
---


## ccc.h1ctf.com CTF
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-18 | CVE：-
- 原文：https://hackerone.com/reports/1215919

- - - - - - - - 
## Summary:
Claiming the flag, writeup to follow.
██████████
██████
## Impact
.
---


## H1-CTF 100k Solution - Congratz on the 100k Rep todayisnew
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-17 | CVE：-
- 原文：https://hackerone.com/reports/1216408

- - - - - - - - 
Sharing the final flag for now. Writeup will come soon 
`██████`
██████████
## Impact
Takeover of admin account :)
---


## Taking Grinch Down To Save Holidays
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-22 | CVE：-
- 原文：https://hackerone.com/reports/1067037

- - - - - - - - 
Hi thank you Hackerone and Adam for organizing the CTF, this had honestly helped me to learn good skills and techniques.
The CTF  began with the scope:  hackyholidays.h1ctf.com and mission to take down grinch
So here's a quick visual summary of all the challenges
{F1131175}  {F1131176}
# 1. Grinch Robots
In this challenge we needed to find grinch robots, opening the robots.txt file destroyed the robots and gave us flags
## Steps to reproduce:
1. Go to https://hackyholidays.h1ctf.com/robots.txt
2. In the page you would find the flag
3. ~~Grinch RobotsDown~~


## CTF Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-14 | CVE：-
- 原文：https://hackerone.com/reports/1066233

- - - - - - - - 
Hi,
First of all, thanks for this amazing CTF!. 
I will post my writeup soon, it is time to sleep now :)
{F1129602}
By the way, the creator of challenge 11 is crazy.
## Impact
Grinch Network is finally down
**Summary (researcher):**
CTF Writeup:
=====================
This CTF was consisted of 12 challenges. Each day a new challenge was released by HackerOne.
Challenge 1 (Robots.txt):
---------------------
__Tools I used:__ Just my browser.
This challenge was really easy, I just checked the [code omitted] file and got the flag.
{F1165514}
Challenge 2 (DOM Flag):
---------------------
__Tools I used:__ Just my browser.
As we can see in the [code omitted] file, there is a "hidd


## First CTF ever!
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1069263

- - - - - - - - 
# Pretext
Started looking into hacking this autumn and then found out HackerOne was doing a Christmas themed CTF. Further investigation showed that the deplorable Grinch might be up to no good again - Christmas is in danger!
# TLDR
Lots of hacking took place, the Grinch was stopped, Christmas saved and all I got for the trouble was these flags (and lots of invites but no Snow Ball Launcher):
[code omitted]
## First look
A first look at the domain in scope (https://hackyholidays.h1ctf.com/) for the CTF reveals the Grinch network's front to the world, a homepage with nothing but a picture.
{F1138471}
Taking a quick look at `https://hackyholidays.h1ctf.com/robots.txt` to see if


## Blind SQL injection at tsftp.informatica.com
- 等级：Critical | 项目：Informatica | 披露：2020-11-16 | CVE：-
- 原文：https://hackerone.com/reports/1034625

- - - - - - - - 
The parameter `refresh_token` sent to the REST path /api/v1/token is vulnerable to blind SQL injection.
Compare the response time of these 2 requests:
[code omitted]
vs
[code omitted]
and notice that the WAITFOR DELAY command is executed.
## Impact
Blind SQL injection can be exploited to exfiltrate data from the FTP server, bypass authentication or for remote code execution.
I stopped my testing at the time-based PoC because I didn't want to risk accessing sensitive data. If you would like to though, I can continue exploiting this vulnerability to present the above impact in practice, eg by getting the database version string.
Researcher identified a time based/blind SQL inj


## SQLi in login form of █████
- 等级：Critical | 项目：U.S. | 披露：2020-09-29 | CVE：-
- 原文：https://hackerone.com/reports/982202

- - - - - - - - 
## Summary
The following is vulnerable to a sqli, due to a limited char set this is t██████████y to demonstrate and not picked up by sqlmap.
[code omitted]
## Description
[code omitted]
returns a 302 with a login error message, while an invalid column name returns a 500 error message. Note that spaces are not accepted, so I must replace them with `/**/`.
To summarize: 
`usr='/**/or/**/lastName!='&pwd=████████` -> 302
`usr='/**/or/**/abc!='&pwd=███` -> 500
case error g██████████get (which could be used to exfil data):
`usr=asdf'/**/and/**/lastName/**/in/**/(select/**/CASE/**/WHEN/**/(SELECT/**/count(*)/**/FROM/**/accounts)>███0000/**/THEN/**/'a'/**/ELSE/**/███/**/END)/**/and/


## Solr Injection in `user_id` parameter at :/v2/leaderboard_v2.json
- 等级：Critical | 项目：Eternal | 披露：2020-08-10 | CVE：-
- 原文：https://hackerone.com/reports/952501

- - - - - - - - 
@zzzhacker13 identified a Solr Injection on the `user_id` parameter at `:/v2/leaderboard_v2.json`. Our team analyzed internally and found that only `fq={injection}` was possible on the `Solr` endpoint, hence the `Solr injection` was of low impact since there was no way to escalate it to exfiltrate data, one could have just changed the filter query but it wasn't possible to update the fields or anything with these methods.
After the report from @zzzhacker13, the team started analyzing the endpoint and discovered an `SQLi` (boolean based blind SQLi) on another parameter in the same codebase. We went ahead and fixed the issue. The `SQL injection`, however, was critical as per o


## SQL Injection or Denial of Service due to a Prototype Pollution
- 等级：Critical | 项目：Node.js | 披露：2020-07-24 | CVE：CVE-2020-8158
- 原文：https://hackerone.com/reports/869574

- - - - - - - - 
I would like to report a prototype pollution vulnerability in the `typeorm` package.
It allows an attacker that is able to save a specially crafted object to pollute the `Object` prototype and cause side effects on the library/application logic, such as denials of service attacks and/or SQL injections, by adding arbitrary properties to any object in the runtime. If the end application depending on the library has dynamic code evaluation or command execution gadgets, the attacker can potentially trigger arbitrary command execution on the target machine.
# Module
**module name:** TypeORM
**version:** v0.2.24, latest
**npm page:** https://www.npmjs.com/package/typeorm
## Module


## SQL Injection Extracts Starbucks Enterprise Accounting, Financial, Payroll Database
- 等级：Critical | 项目：Starbucks | 披露：2019-08-06 | CVE：-
- 原文：https://hackerone.com/reports/531051

- - - - - - - - 
As described in the Hacker Summary, @spaceraccoon discovered a SQL Injection vulnerability in a web service backed by Microsoft Dynamics AX. @spaceraccoon demonstrated that the flaw was exploitable via XML-formatted HTTP payload requests to the server. We appreciate @spaceraccoon's clear and thorough report, which helped us quickly and effectively triage the report and remediate the vulnerability.
**Summary (researcher):**
## False Starts
I first came across the endpoint via typical subdomain enumeration. On the surface, it looked like an extremely promising target: a simple HTML file upload form. I began by testing for unrestricted file uploads with PHP shells and such, but


## Blind SQLi leading to RCE, from Unauthenticated access to a test API Webservice
- 等级：Critical | 项目：Starbucks | 披露：2019-07-22 | CVE：-
- 原文：https://hackerone.com/reports/592400

- - - - - - - - 
@geek_jeremy, at the same time as other hackers who submitted their own reports, discovered a browsable WSDL service on an API endpoint under the starbucks.com.cn domain, running on a non-standard port.
@geek_jeremy demonstrated that the service had several functions that executed without any authentication at all, allowing the listing of users, passwords and other personal information. Fortunately, this was a test service, executing on test data, and as a result, this alone did not constitute a vulnerability worth rewarding.
@geek_jeremy also demonstrated that the service had at least one blind SQLi vulnerability, allowing him to not only access the database behind the serv


## Arbitrary SQL command injection
- 等级：Critical | 项目：Nextcloud | 披露：2019-07-21 | CVE：CVE-2019-5476
- 原文：https://hackerone.com/reports/508487

- - - - - - - - 
When querying for users on the lookup server any unauthenticated user could perform an SQL Injection.
---

