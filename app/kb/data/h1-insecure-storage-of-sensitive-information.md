# HackerOne 实战案例：insecure-storage-of-sensitive-information

_19 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Exposed Extremely Sensitive Information in Public ZIP File
- 等级：Critical | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/2857082

- - - - - - - - 
An unprotected ZIP file (█████.zip) containing sensitive information is publicly accessible at http://██████/data/█████.zip. This file contains highly sensitive data, including SMTP credentials, database connection details, and AWS secret keys for the us-gov-west-1 region.
Steps to Reproduce:
    Download the ZIP file from the publicly accessible URL:
        URL: http://██████/data/████.zip
        You can download the file via the browser or using curl:
    curl -O http://██████/data/███.zip
Extract the contents of the ZIP file using any standard extraction tool:
unzip ███.zip
Review the extracted files for sensitive information. The files include:
    SMTP credentials (us


## Local File Disclosure on the █████ (https://████████.edu/) leads to the full source code disclosure and credentials leak
- 等级：Critical | 项目：U.S. | 披露：2024-06-27 | CVE：-
- 原文：https://hackerone.com/reports/684836

- - - - - - - - 
##Description
During poking around `██████.00/24` range -  ██████████ looking for the Cisco devices, I came across `███` which resolved to the https://███████.edu/
While it's a not `.mil` host, it's likely related to the DoD since it hosted in the DoD-controlled ASN.
I discovered few critical vulnerabilities here, one of them is LFD (local file disclosure).
##POC
https://██████.edu/file.ashx?path=web.config
will download the website configuration file.
It exposes the DB credentials:
███
Similarly, attacker able to get content of any server-side resource, such as source code of application:
https://███.edu/file.ashx?path=UserAccountJSON.aspx.cs
## Impact
Source code & DB cred


## Exposure Of Admin Username & Password
- 等级：Critical | 项目：MTN | 披露：2022-12-25 | CVE：-
- 原文：https://hackerone.com/reports/1703733

- - - - - - - - 
Hello Team, 
Ther an exposure of your username and password on this    subdomain █████
    uid: "mtnng",
        passwd: "██████████",
Steps To Reproduce:
Visit ███ 
Now, press CTRL+U to view the source code of this page,
Look for this code
       console.log(message);
    }
}
    (function (){
    const plid = 73;
    const mtnContainer = document.getElementById("mtn20238");
    const mtnUri = mtnContainer.childNodes[0].getAttribute("href");
    mtnContainer.addEventListener("click", ()=>fetch(mtnUri).catch(()=>{}));
    window.mobucksApi.placeAd({
        containerElementId: "mtn20238",
        uid: "mtnng",
        passwd: "███████",
        plid:plid,
        }, () => { 


## Firebase Database Takeover in https://pulseradio.mtn.co.ug/
- 等级：Critical | 项目：MTN | 披露：2022-12-01 | CVE：-
- 原文：https://hackerone.com/reports/1447751

- - - - - - - - 
## Summary:
During my test , in one of the subdomain of mtn.co.ug I found firebase configuration disclosed in the source code along with apiKey and database URL . 
Exploiting this vulnerability attacker is able to upload malicious data in the firebase account of pulseradio.mtn.co.ug and see database over there .
## Steps To Reproduce:
POC :  https://mtn-pulse-uganda.firebaseio.com/poc.json
1. Go to URL below and view the source code of website .
view-source:https://pulseradio.mtn.co.ug/wp-content/themes/mtn-pulse-reskin/zero-rate/firebase-config.js
There you will see following sensitive data .
$(document).ready(function() {
			// Your web app's Firebase configuration
			var 


## Able to view hackerone reports attachments
- 等级：Critical | 项目：GitLab | 披露：2022-07-11 | CVE：-
- 原文：https://hackerone.com/reports/979787

- - - - - - - -


## Insecure Storage of Sensitive Information on lonestarcell.com server
- 等级：Critical | 项目：MTN | 披露：2022-04-09 | CVE：-
- 原文：https://hackerone.com/reports/1482830

- - - - - - - - 
Hello , i hope your doing well 
i found some sensitive information disclosure at those endpoint
it is disclosure server status and some other stuff 
https://simregistration.lonestarcell.com//monitoring/DB02/DB02.html#System
https://simregistration.lonestarcell.com//monitoring/DB01/index.html
https://simregistration.lonestarcell.com//monitoring
## Impact
Sensitive Information disclosure on lonestarcell server
---


## Military  name,email,phone,address,certdata Disclosure
- 等级：Critical | 项目：U.S. | 披露：2022-03-18 | CVE：-
- 原文：https://hackerone.com/reports/1490133

- - - - - - - - 
A DoD public facing asset Military was misconfigured and disclosed name, email ,phone address , and certdata of users.
---


## Directory Indexing on the ████ (https://████/) leads to the backups disclosure and credentials leak
- 等级：Critical | 项目：U.S. | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/684838

- - - - - - - - 
##Description
During poking around `█████████/24` range -  █████ looking for the Cisco devices, I came across `█████` which resolved to the https://██████/
While it's a not `.mil` host, it's likely related to the DoD since it hosted in the DoD-controlled ASN.
I discovered few critical vulnerabilities here, one of them is exposed backup files via directory listing.
##POC
https://███/obj/Debug/
█████
The source code can be found here:
https://█████████/obj/Debug/Package/GLOSS2.zip
It's zipped backup.
The DB credentials exposed here:
https://█████/obj/Debug/Package/GLOSS2.SetParameters.xml
███
##Suggested fix
Disable directory indexing, restrict access to the sensitive files, a


## PulseSSL VPN Site with Compromised Creds @ ████
- 等级：Critical | 项目：U.S. | 披露：2020-07-30 | CVE：-
- 原文：https://hackerone.com/reports/854049

- - - - - - - - 
Dear US DoD,
Back in 2019, I had reported that a pulseSSL VPN server owned by US DoD can be compromised by a publicly available exploit. The report is████████. As a result, the userid and passwd db was also compromised. I found that at least 1 userid and password combination from that compromised db can still be used.
##PoC
Here is a screenshot of me accessing a US DoD owned website using a compromised credentials found back in 2019. I am still able to login to https://████/dana-na/auth/url_3/welcome.cgi with:
l: █████████
p:  █████
█████
Here is the screenshot of the credentials that was dump back in 2019:
████
## Impact
It is widely reported in the media that blackhat hack


## Previously Compromised PulseSSL VPN Hosts
- 等级：Critical | 项目：U.S. | 披露：2020-05-27 | CVE：-
- 原文：https://hackerone.com/reports/852713

- - - - - - - - 
Hi again!!
Back in 2019, I had reported that a pulseSSL VPN server owned by US DoD can be compromised by a publicly available exploit. The report is #681249. As a result, the userid and passwd db was also compromised. I  found  that at least 1 userid and password combination from that compromised db can still be used. 
##PoC
Here is a screenshot of me accessing a US DoD owned website using a compromised credentials found back in 2019. I am still able to login to https://████/dana-na/auth/url_46/welcome.cgi with:
l: ███
p: █████████
███████
███████
Here is the creds from  Sep, 2019.
█████
## Impact
It is widely reported in the media that blackhat hackers around the world are 


## SSN leak due to editable slides
- 等级：Critical | 项目：U.S. | 披露：2020-05-14 | CVE：-
- 原文：https://hackerone.com/reports/693943

- - - - - - - - 
**Summary:**
A presentation slide contains a screenshot of a records brief which contains an SSN
**Description:**
The slides try to redact the PII of the records with a blue block but we can remove it by editing the slides to remove the offending blue block
## Impact
Critical 
## Step-by-step Reproduction Instructions
We can see an officer record brief, but the area with the SSN is blocked. We can make a copy of the file and edit it to remove the blue block thus allowing us to see the SSN
https://█████████/wp-content/uploads/2018/03/███████
Slide 84
███████
█████████
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Purge 


## PII Leak via https://████████
- 等级：Critical | 项目：U.S. | 披露：2020-05-11 | CVE：-
- 原文：https://hackerone.com/reports/808338

- - - - - - - - 
**Summary:**
An attacker can create an account on https://████ and gain access to a wealth of PII for practically every member that is registered on the website. This includes e-mail addresses, physical addresses, telephone numbers, and other information about a vast majority of the US Air Force, as this portal is where ████████ support is hosted.
**Description:**
## Impact
An adversary can sign up for an account on https://█████████ to gather a vast amount of PII related to a large portion of the USAF. This can be used for many purposes and should not be accessible by a regular user.
## Step-by-step Reproduction Instructions
1. Browse to https://██████████
███████
2. Create


## PII leakage-Full SSN on ███
- 等级：Critical | 项目：U.S. | 披露：2019-10-10 | CVE：-
- 原文：https://hackerone.com/reports/644358

- - - - - - - - 
**Summary:**
I discovered a pdf file on ████████ that outlines various information corresponding to military members. It reveals information on date of birth, where they were born, marriage status, race, children/dependents, etc
**Description:**
I discovered what looks to be an internal file that outlines sensitive information on various service member and looks to be publicly accessible
## Impact
High
## Step-by-step Reproduction Instructions
Visit: https://█████/wp-content/uploads/2018/12/██████████
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Remove immedietly
## Impact
An attacker can gleam highly personal informa


## CVE-2010-1429 JBoss Insecure Storage of Sensitive Information on ips.mtn.co.ug
- 等级：High | 项目：MTN | 披露：2024-08-30 | CVE：CVE-2008-3273,
- 原文：https://hackerone.com/reports/2375659

- - - - - - - - 
## Summary:
Red Hat JBoss Enterprise Application Platform (aka JBoss EAP or JBEAP) 4.2 before 4.2.0.CP09 and 4.3 before 4.3.0.CP08 allows remote attackers to obtain sensitive information about "deployed web contexts" via a request to the status servlet, as demonstrated by a full=true query string. this issue exists because of a CVE-2008-3273 regression. by requesting the Status param and sitting its value to true, Jobss will print a sensitive information such as Memory used/Total Memory / Client IP address. 
## Proof of concept
  1. Navigate intercept / visit hostserver on https://h30f.n1.ips.mtn.co.ug/status?full=true
  1. You can see on the page is sensitive has exposed
  


## Mozilla Mastodon Staging Instance Admin API Key Disclosure Through Slack
- 等级：High | 项目：Mozilla | 披露：2023-09-11 | CVE：-
- 原文：https://hackerone.com/reports/2137154

- - - - - - - - 
## Summary:
I was able to find Admin Maston API Keys disclosed within Mozilla's #trust-and-safety-eng channel which was posted by a staff member of Mozilla.
## Steps To Reproduce:
  1. Authenticate to mozilla.slack.com as an NDA or Mozillla Staff Member (https://wiki.mozilla.org/NDA)
  2. Search the #trust-and-safety-eng channel for █████████  (Exposed token)
  3. Validate that the token through the following command:
tok=███
ep=https://stage.moztodon.nonprod.webservices.mozgcp.net
curl -H "Authorization: Bearer $tok" "$ep/api/v1/admin/accounts/" 
4. Observe the following output (I've redacted some as it shows the output of all Mastodon accounts):
████████
5. Please note tha


## sensitive data exposure
- 等级：High | 项目：Reddit | 披露：2022-11-10 | CVE：-
- 原文：https://hackerone.com/reports/1716249

- - - - - - - - 
## Summary:
[A Password hash entry was found in /etc/passwd. This is a major vulnerability since /etc/passwd is a world-readable file by default. Once the password hash is found, an attacker may extract the password using a program like crack.]
## Impact:
it is high impact vulnerability .once hacker found password hash it may be leads to develop a program like crack
## Steps To Reproduce:
[https://www.reddit.com/etc%2fpasswd]
  1. [add step]
  1. [add step]
  1. [add step]
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
  * [attachment / reference]
## Impact
A Password hash entry was found in /etc/passwd. This is a major vulne


## Partial SSN exposed through Presentation slides on ██████████
- 等级：High | 项目：U.S. | 披露：2019-10-10 | CVE：-
- 原文：https://hackerone.com/reports/665144

- - - - - - - - 
**Summary:**
During a search of ████████ I discovered that one of the slides ina presentation contained a screen shot of live data. 
**Description:**
The slides describe testing and using military application to organize and aggregate data on users. On one of the slides it does show a screen shot of actual data. I'm assuming it's live due to the fact that part of it was blocked out like the previous report where it showed XXXX and 4 digits.
## Impact
Critical
## Step-by-step Reproduction Instructions
████
## Product, Version, and Configuration (If applicable)
N/A
## Suggested Mitigation/Remediation Actions
Purge the file
## Impact
Last 4  digits of an SSN can be used on vari


## Online training material disclosing username and password
- 等级：High | 项目：U.S. | 披露：2019-10-08 | CVE：-
- 原文：https://hackerone.com/reports/672629

- - - - - - - - 
**Summary:**
A training document is revealing username and password details for what appears to be a DoD training system
**Description:**
Using the google dork ``site:*.mil ext:ppt intext:password``, I was able to find a number of powerpoint documents on .mil websites that include username and passwords.
This document appears to be some old training materials
Slide 39 of www.███████/█████████ 
See: █████████
In this instance, the document relates to an online training platform at https://████████/, so if the credentials are still valid, anyone who reads that presentation could potentially access that system and any data it holds. Training databases often have elements of sen


## Leaking sensitive information lead to compromise employer API keys
- 等级：High | 项目：Yelp | 披露：2017-11-09 | CVE：-
- 原文：https://hackerone.com/reports/273630

- - - - - - - - 
The configuration file of an internal IRC bot (which included credentials to internal services and some external services used by Yelp developers) was inadvertently included by an employee in a personal public GitHub repository. The repository was taken down and the affected credentials rotated.
---

