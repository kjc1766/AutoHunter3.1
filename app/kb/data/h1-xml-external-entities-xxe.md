# HackerOne 实战案例：xml-external-entities-xxe

_21 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## AEM forms XXE Vulnerability
- 等级：Critical | 项目：Adobe | 披露：2022-01-13 | CVE：-
- 原文：https://hackerone.com/reports/1321070

- - - - - - - - 
AEM Forms Cloud Service offering, as well as version 6.5.10.0 (and below) are affected by an XML External Entity (XXE) injection vulnerability that could be abused by an attacker to achieve RCE. 
CVE: CVE-2021-40722
Ref: https://helpx.adobe.com/security/products/experience-manager/apsb21-103.html
We thank @ismailmuh for reporting this to Adobe!
---


## HackerOne’s 100K CTF Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-21 | CVE：-
- 原文：https://hackerone.com/reports/1218708

- - - - - - - - 
Greetings team
It has been a great challenge, thank you very much for the fun moments and also for the annoying ones :)
██████████
P.S. I will put my writeup in my next comment.
## Impact
---
---


## CCC H1 June 2021 CTF Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-21 | CVE：-
- 原文：https://hackerone.com/reports/1217114

- - - - - - - - 
## CTF Summary
This was my first H1 CTF and I was excited to work with several others to collaborate on the CTF and find the flag. I'll write up the solution process and vulnerabilities involved in the solution:
 * Knowledge (basic) of S3 operations
 * XML External Entities and Local File Exfiltration
 * SQL Injection (+source code review)
 * A very clever use of exfiltration using ICMP ping
The general theme of this CTF involved several out-of-band or blind attacks, which were not obvious on initial review.
## Phase 1: CCC web site and initial recon
The CTF site was located at https://ccc.h1ctf.com and contains a basic login page and registration feature. Registration is op


## XXE in Enterprise Search's App Search web crawler
- 等级：Critical | 项目：Elastic | 披露：2021-04-29 | CVE：-
- 原文：https://hackerone.com/reports/1156748

- - - - - - - - 
## Summary
Hello team! The latest version of Enterprise Search (7.12.0) is vulnerable to XXE when [parsing sitemaps](https://www.elastic.co/guide/en/app-search/current/crawl-web-content.html#crawl-web-content-manage-sitemaps). Up to now I'm only able to read file that contain one line. I'm reporting now to avoid duplicates, but I'll keep working to find a way to extract entire files or HTTP request bodies.
## Description
Enterprise Search has a Web Crawler that crawls websites and ingests data to make it searchable. The crawler will look for `robots.txt` files and in that file it will look for the `sitemap` directive. When the sitemap is present, the crawler will parse it an


## Non-production Open Database In Combination With XXE Leads To SSRF
- 等级：Critical | 项目：Evernote | 披露：2020-10-27 | CVE：-
- 原文：https://hackerone.com/reports/742808

- - - - - - - - 
## Summary:
The Apache Hive database hosted on the IP ██████████ and open on port 10000 is open and vulnerable to XXE.
By "open", I mean that the database can be accessed by anyone.
## Steps To Reproduce:
Chose any database client that supports Apache Hive and also uses a specific client version. "Specific client version" because you will otherwise get an error which looks like this:
[code omitted]
  1. Chose a database client and connect to mentioned IP and port
  2. Execute the following SQL payload:
[code omitted]
The query above will return the associated project id which is "en-development".
## Supporting Material/References:
I will list some interesting information tha


## XXE through injection of a payload in the XMP metadata of a JPEG file
- 等级：Critical | 项目：Informatica | 披露：2020-04-21 | CVE：-
- 原文：https://hackerone.com/reports/836877

- - - - - - - - 
Users are able to change their avatar picture. The avatar picture upload functionality is prone to a XXE attack when parsing the image file. Specifically, the XXE attack is executed through the injection of a payload in the "XMP metadata" of the uploaded JPEG file.
Proof of concept (note the "Burp Collaborator Payload pointing to an External DTD"):
[code omitted]
And I received the following calls (note the User-Agent "Java██████" confirming the vulnerability):
[code omitted]
Similar calls were received from another IP address: 146.112.138.73
Furthermore, the affected host should not be allowed to start a new connection to the Internet.
## Impact
This issue can be abused to 


## XXE at ecjobs.starbucks.com.cn/retail/hxpublic_v6/hxdynamicpage6.aspx
- 等级：Critical | 项目：Starbucks | 披露：2019-11-13 | CVE：-
- 原文：https://hackerone.com/reports/500515

- - - - - - - - 
**Description:**
Hi,guys,when i was visited the jobs of starbucks websites in China(https://ecjobs.starbucks.com.cn), i found a features of uploaded user's photo.Thought the bypass the security restrictions of upload,i can upload html|xhtml|xml|config files etc.The uploaded html file can realize the danger of stored xss,and the uploaded xml file can be  parsed by the server,Through tested, the server does not prohibit the use of doctypes, entities, and access to external dtd files. 
## Steps To Reproduce:
Upload and XXE vulnerability: 
1. Log in to the user, enter the personal information settings page, click Upload Image 
2. Intercept https access information through Burp s


## XXE in DoD website that may lead to RCE
- 等级：Critical | 项目：U.S. | 披露：2019-10-04 | CVE：-
- 原文：https://hackerone.com/reports/227880

- - - - - - - - 
**Summary:**
XXE in https://█████
**Description:**
A malicious user can modify an XML-based request to include XML content that is then parsed locally.
## Impact
An attacker can use an XML external entity vulnerability to send specially crafted unauthorized XML requests, which will be processed by the XML parser. The attacker can use an XML external entity vulnerability for getting unauthorised access to the OS file system.
## PoC
[code omitted]
---


## XXE on https://duckduckgo.com
- 等级：Critical | 项目：DuckDuckGo | 披露：2019-01-31 | CVE：-
- 原文：https://hackerone.com/reports/483774

- - - - - - - - 
An XML External Entity (XXE) injection vulnerability was discovered in the `x.js` endpoint on https://duckduckgo.com via `u` parameter. This was due to improper sanitation of external XML entities. The results was a leak of certain world readable files on the system.
This issue was patched. Additionally, we intend to retire the endpoint in the very near future.
Big thanks to @mik317 for reporting this issue!
---


## Flag WriteUp
- 等级：Critical | 项目：h1-5411-CTF | 披露：2018-10-22 | CVE：-
- 原文：https://hackerone.com/reports/415202

- - - - - - - - 
Hello everyone , here is my writeup :
## Intro
First I decoded the QR Code of the [tweet](https://twitter.com/Hacker0x01/status/1045075889120268289) , decoding to `Here you go: 68747470733a2f2f68312d353431312e68316374662e636f6d` . Decoding the hex value we get the challenge URL : https://h1-5411.h1ctf.com
## Path traversal + local file read
On the website I found two important endpoints : /generate.php and /memes.php . At the generate.php I started doing some "manual fuzzing" trying some command injection, like `;)'";|id`, and template injections like `{{7*7}}` but nothing seemed to work. 
Analyzing the requests I see that the `template` parameter value is a filename , so I 


## LFI and SSRF via XXE in emblem editor
- 等级：Critical | 项目：Rockstar | 披露：2018-08-01 | CVE：-
- 原文：https://hackerone.com/reports/347139

- - - - - - - - 
This summary is provided by the researcher who submitted this report, @alexbirsan . 
___________________________________________________________________________________________________________________________
About one year after I started messing with the emblem editor, I finally found a full SSRF and LFI. I was able to extract text files from the server and HTTP responses by rendering them on my crew emblem.
For those of you who are not familiar with the emblem editor, the interesting part is a SVG to PNG conversion using user supplied input. The main pieces of my exploit were mostly quirks in the ImageMagick version used by Rockstar:
1. Double forward slash to reference a


## XXE in Site Audit function exposing file and directory contents
- 等级：Critical | 项目：Semrush | 披露：2018-03-13 | CVE：-
- 原文：https://hackerone.com/reports/312543

- - - - - - - - 
**Summary:** 
The Project Site Audit function is vulnerable to XXE when parsing sitemap.xml files.
**Description:** 
The Site Audit function spiders a given website and performs analysis on the discovered pages. In order to improve website spidering the URL of a `sitemap.xml` file can be provided. If provided, the `sitemap.xml` file will be downloaded and processed by a Java XML processor.
The Java xml processor used is vulnerable to XXE attacks. By providing an external document type declaration (DTD) the XML processor can be coerced into processing external entities, for example:
**sitemap.xml**
[code omitted]
Will cause the XML processor to process the external entity at 


## XXE on DoD web server
- 等级：Critical | 项目：U.S. | 披露：2017-01-09 | CVE：-
- 原文：https://hackerone.com/reports/188743

- - - - - - - - 
A Department of Defense webserver was vulnerable to an XML External Entity (XXE) processing vulnerability. dawgyg was able to exploit this vulnerability by crafting an XML request that revealed sensitive local system information. Thanks dawgyg!
---


## DMARC  Not found for paragonie.com   URGENT
- 等级：Critical | 项目：Paragon | 披露：2016-11-03 | CVE：-
- 原文：https://hackerone.com/reports/179828

- - - - - - - - 
#Hi sir, ,
I am  new hacker in hackerone platform  I am glad to join paragonie bounty program  ..i  want to report a very critical bug that is i found DMARC   missing for your domain paragonie.com
Add DMARC record as soon as  possible ..
DMARC description 
Background
Email authentication technologies SPF and DKIM were developed over a decade ago in order to provide greater assurance on the identity of the sender of a message. Adoption of these technologies has steadily increased but the problem of fraudulent and deceptive emails has not abated. It would seem that if senders used these technologies, then email receivers would easily be able to differentiate the fraudulent mes


## XML E██████ternal Entity (XXE) Injection in ███
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：CVE-2022-2414
- 原文：https://hackerone.com/reports/2564265

- - - - - - - - 
Description
CVE-2022-2414 describes an XML E██████ternal Entity (XXE) injection vulnerability. XXE vulnerabilities occur when an application parses XML input that contains a reference to an e██████████ternal entity. When the XML parser is improperly configured to process e███████ternal entities, it can allow an attacker to███████
Read arbitrary files on the server.
Perform server-side request forgery (SSRF).
Conduct denial-of-service (DoS) attacks.
E█████████ecute remote code (in rare cases).
Host name█████ ██████████
POC████████
request█████████
[code omitted]
responde████
[code omitted]
## Impact
E███████ploitation of this vulnerability can lead to████████
1-Confidentialit


## XML External Entity (XXE) Injection
- 等级：High | 项目：U.S. | 披露：2024-07-19 | CVE：-
- 原文：https://hackerone.com/reports/2573567

- - - - - - - - 
XML External Entity (XXE) injection vulnerability. XXE vulnerabilities occur when an application parses XML input that contains a reference to an external entity. When the XML parser is improperly configured to process external entities, it can allow an attacker to:
Read arbitrary files on the server.
Perform server-side request forgery (SSRF).
Conduct denial-of-service (DoS) attacks.
Execute remote code (in rare cases).
Host name: 	███████.mil
POC:
[code omitted]
## Impact
Exploitation of this vulnerability can lead to:
1-Confidentiality Breach: Unauthorized access to sensitive information stored on the server.
2-Integrity Violation: Potential manipulation or corruption of 


## XXE with RCE potential on the https://█████████ (CVE-2017-3548)
- 等级：High | 项目：U.S. | 披露：2024-07-19 | CVE：CVE-2017-3548
- 原文：https://hackerone.com/reports/710654

- - - - - - - - 
##Description
Hello. I was able to identify XXE on the https://███████
It is CVE in Oracle PeopleSoft (CVE-2017-3548)
##POC
I determined that instance is available on localhost port 80, so it's possible to access `/pspc/services/AdminService` via XXE:
[code omitted]
where `h1testservice` is test service name I'm trying to create.
The result:
[code omitted]
█████
I created new service on server.
It's possible to go further like other researcher did in the #227880 but I don't think that dropping shell is necessary (since it's already proved that we can create our Apache Axis service.
##Suggested fix
Patch Oracle PeopleSoft instance.
## Impact
Remote code execution, internal ne


## Singapore - XXE at https://www.starbucks.com.sg/RestApi/soap11
- 等级：High | 项目：Starbucks | 披露：2020-07-22 | CVE：-
- 原文：https://hackerone.com/reports/762251

- - - - - - - - 
rugb discovered the endpoint at https://www.starbucks.com.sg/RestApi/* was found vulnerable to XML eXternal Entity (XXE) processing. This permitted arbitrary reading of files on the remote server. This asset is not rated as critical as it does not contain sensitive data.
@rugb — thank you for reporting this vulnerability and for confirming the resolution.
---


## Partial bypass of #483774 with Blind XXE on https://duckduckgo.com
- 等级：High | 项目：DuckDuckGo | 披露：2019-02-25 | CVE：-
- 原文：https://hackerone.com/reports/486732

- - - - - - - - 
**Summary:**
Hi DuckDuckGo team,
I've contacted previously you because in a second time (on the #483774 report), I've seen that was possible bypass the fix. Anyway, I've not got any response, and because I think that this is a bit dangerous issue, I'm opening another report for the bypass. Hope you'll agree.
**Steps for reproduction:**
1. Attacker creates a public server and hosts a file with the following content:
[code omitted]
2. User goes on https://duckduckgo.com/x.js?u=http://attacker_host/xxe.xml
3. The `http://attacker_host/Blind_xxe` resource will be requested by an host {F413045}
I'd like to say that this affects not only `duckduckgo.com`, but also `api.duckduckgo.


## Remote Code Execution (RCE) vulnerability in a DoD website
- 等级：High | 项目：U.S. | 披露：2017-08-15 | CVE：CVE-2017-3548
- 原文：https://hackerone.com/reports/232330

- - - - - - - - 
A remote code execution (RCE) vulnerability was found on a DoD website which could have enabled an attacker to execute remote commands on the web server. Thank you @peuch for notifying us of this vulnerability!
---


## Uploaded XLF files result in External Entity Execution
- 等级：High | 项目：Weblate | 披露：2017-06-02 | CVE：-
- 原文：https://hackerone.com/reports/232614

- - - - - - - - 
Summary:
========
 Weblate users in the Translate group (or those with the ability to upload translation files) can trigger XML External Entity Execution. This is a well known and high/critical vector of attack that often can completely compromise the security of a web application or in some cases lead to Remote Code Execution (although I do not expect it to be an easy RCE in this case).
Description:
========
The XML External Entity Execution allows for arbitrary reading of files on the server using a relatively obscure aspect of the XML language. It is generally considered high or critical severity, most notably Google places it at the same severity as remote code execution

