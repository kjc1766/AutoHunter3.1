# HackerOne 实战案例：command-injection-generic

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Argument Injection via curl Short-Flag Grouping
- 等级：Critical | 项目：curl | 披露：2026-04-13 | CVE：-
- 原文：https://hackerone.com/reports/3669305

- - - - - - - - 
This report details how the curl -os command facilitates an Argument Injection vulnerability in applications that wrap the curl command-line tool.
The specific command curl -os /etc/passwd --url http://example.com demonstrates a subtle but dangerous behavior. Because -s (silent) follows -o (output), curl expects the very next string to be the filename.In this scenario:The -o flag consumes the next argument (/etc/passwd).The -s flag tells curl to suppress the progress meter and error messages.The --url flag specifies the source of the data.This effectively turns a "downloader" into a "file overwriter."
 Root Cause Analysis
The root cause is insufficient input validation and t


## Middleware Authentication Bypass on IBM Portal
- 等级：Critical | 项目：IBM | 披露：2025-05-02 | CVE：CVE-2025-29927
- 原文：https://hackerone.com/reports/3088290

- - - - - - - - 
Middleware authentication bypass on IBM portal endpoint  was reported to IBM, analyzed and has been remediated. Thank you to our external researcher @muhammadwaseem3.
---


## Cisco IOS XE instance at ████ vulnerable to CVE-██████
- 等级：Critical | 项目：MTN | 披露：2025-02-19 | CVE：CVE-2023-20198,
- 原文：https://hackerone.com/reports/2778350

- - - - - - - - 
## Summary:
CVE-███████ is characterized by improper path validation to bypass Nginx filtering to reach the webui_wsma_http web endpoint without requiring authentication. By bypassing authentication to the endpoint, an attacker can execute arbitrary Cisco IOS commands or issue configuration changes with Privilege 15 privileges. Further attacks involved exploitation of CVE-2023-20273 to escalate to the underlying Linux OS root user to facilitate implantation.
This PoC exploits CVE-█████████ to leverage two different XML SOAP endpoints:
The vulnerability check, config, and command execution options all target the `cisco:wsma-exec` SOAP endpoint to insert commands into the `exe


## Remote Code Execution and AWS IAM Credentials Exfiltration in https://████████/
- 等级：Critical | 项目：U.S. | 披露：2024-12-18 | CVE：-
- 原文：https://hackerone.com/reports/2083771

- - - - - - - - 
**Description:**
The host https://██████/ has /jenkins/script directory enabled that allows user to execute system command in the host.
## References
https://hackerone.com/reports/768266
## Impact
Attacker can use the IAM credentials to manage various AWS resources, create and delete resources, read and write data in AWS services,  create and manage other IAM users and roles, access the AWS Management Console, use the AWS Command Line Interface (CLI). In addition, attacker can obtain a reverse shell and takeover the vulnerable server.
## System Host(s)
█████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
1. Go to https://███/jenkins/script and ent


## Shell command injection in https://partner.steamgames.com/apps/communityitems/ via file extension of item_image_small and item_image_large
- 等级：Critical | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/840243

- - - - - - - - 
Shell injection was achieved on a publishing gateway through metacharacter injection in an item-upload path.
**Summary (researcher):**
.
---


## WG call injection in /economy/contextcommand
- 等级：Critical | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/652649

- - - - - - - - 
Context-specific commands to a web-facing gateway had insufficient parameter validation. Some economy queries could be run outside the actual requesters' capability by confusing the type system. Some bypasses for initial fixes were also provided.
**Summary (researcher):**
Insufficient validation of parameters allowed making arbitrary calls to an internal data service.
---


## RCE on partner.steampowered.com
- 等级：Critical | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/518348

- - - - - - - - 
Insufficient validation of parameters allowed an attacker to specify the name of a PHP function to call with parameter types (array, array, string). This could be changed to a call with parameter types (string string) using array_diff_uassoc. This enabled calling assert, which at the time invoked eval, enabling arbitrary code execution.
**Summary (researcher):**
-
---


## RCE via File Upload  with a Null Byte Truncated File Extension at https://██████/
- 等级：Critical | 项目：U.S. | 披露：2023-12-21 | CVE：-
- 原文：https://hackerone.com/reports/2054184

- - - - - - - - 
Hi,
I found "repos" at `https://███/` and `https://c█████████/` and this one (which doesn't have the file upload functionality appearing on the DOM, but it still may be there) `https://███████`.  There may be more, I had to fuzz a lot to find these. 
These repos contain file upload functionality. I found that if you place a null byte between file extensions, you can upload files with malicious extensions. 
Running the `dir` command at the uploaded file `https://████████/savefiles/poc.asp?cmd=dir`  - the shell has been deleted for security purposes. Let me know if you want me to reupload it. 
██████████
The request from burp - note the null byte: 
█████
*** Reproduction ***
1


## Rocket.Chat Server RCE
- 等级：Critical | 项目：Rocket.Chat | 披露：2023-03-04 | CVE：CVE-2023-23917
- 原文：https://hackerone.com/reports/1631258

- - - - - - - - 
Rocket.Chat server (https://github.com/RocketChat/Rocket.Chat) has a Prototype Pollution vulnerability that leads to RCE under the admin account. Any user can create their own server in your cloud and become an admin so this vulnerability could affect the cloud infrastructure. This attack vector also may increase the impact of XSS to RCE which is dangerous for self-hosted users as well.
---


## Apache Flink RCE via GET jar/plan API Endpoint
- 等级：Critical | 项目：Aiven | 披露：2022-11-08 | CVE：-
- 原文：https://hackerone.com/reports/1418891

- - - - - - - - 
## Summary:
Aiven has not restricted access to the GET `jars/{jar_id}/plan` API. This endpoint can be used to load java class files with the specified arguments that are in the java classpath on the server. This can be abused to gain RCE on the Apache Flink Server.
## Steps To Reproduce:
The video below shows how to setup the Apache Flink instance and run the PoC. Feel free to use my VPS which will make triaging somewhat easier (`ssh ████████`, password: `██████`):
█████████
  1. Login to my aiven account: `████`, password: `██████`
  1. Run the SQL job as demonstrated in the video
  1. Open the Flink Web UI and verify that there is a new job in the jobs panel.
  1. Setup ne


## POOL_UPGRADE request handler may allow an unauthenticated attacker to remotely execute code on every node in the network.
- 等级：Critical | 项目：Linux | 披露：2022-10-20 | CVE：CVE-2022-31020
- 原文：https://hackerone.com/reports/1705717

- - - - - - - - 
This issue is related to the https://github.com/hyperledger/indy-node. 
The issue was found in the `indy-node` code that handles the write request of type ****`POOL_UPGRADE` (in file** `indy-node/indy_node/server/request_handlers/config_req_handlers/pool_upgrade_handler.py`****).**** 
The `additional_dynamic_validation` function handles an undocumented field called `package` that can contain the name of the package to be upgraded. I case that this field is not empty, it is passed as is to the following functions `self.upgrader.check_upgrade_possible -> NodeControlUtil.curr_pkg_info -> cls._get_curr_info`.
[code omitted]
As seen in the code snippet above, the user supplied na


## Remote Command Execution via Github import
- 等级：Critical | 项目：GitLab | 披露：2022-10-06 | CVE：CVE-2022-2884
- 原文：https://hackerone.com/reports/1679624

- - - - - - - -


## RCE via the DecompressedArchiveSizeValidator and Project BulkImports (behind feature flag)
- 等级：Critical | 项目：GitLab | 披露：2022-09-13 | CVE：CVE-2022-2185
- 原文：https://hackerone.com/reports/1609965

- - - - - - - -


## Remote Code Execution at https://169.38.86.185/ (edst.ibm.com)
- 等级：Critical | 项目：IBM | 披露：2021-11-04 | CVE：-
- 原文：https://hackerone.com/reports/1379130

- - - - - - - - 
A discovered Gitlab server was running an old version affected by RCE. This vulnerability could have allowed an unauthenticated attackers to compromise the server by public exploit in ExifTool. The issue was reported to IBM and remediated.
---


## Pre-auth Remote Code Execution on multiple Uber SSL VPN servers
- 等级：Critical | 项目：Uber | 披露：2021-02-24 | CVE：-
- 原文：https://hackerone.com/reports/540242

- - - - - - - - 
format string vulnerability on /sslmgr with no authentication required
**Summary (researcher):**
Details:
> http://blog.orange.tw/2019/07/attacking-ssl-vpn-part-1-preauth-rce-on-palo-alto.html
---


## Remote code execution on Basecamp.com
- 等级：Critical | 项目：Basecamp | 披露：2020-11-26 | CVE：CVE-2017-8291
- 原文：https://hackerone.com/reports/365271

- - - - - - - - 
A critical flaw in Basecamp's profile image upload function leads to remote command execution. Images are converted on the server side, but not only image files but also PostScript/EPS files are accepted (if renamed to .gif). This is probably due to ImageMagick / GraphicsMagick being used for image conversion, which calls a PostScript interpreter (Ghostscript) if the input file starts with '%!'. The used Ghostscript version however has a security bug (CVE-2017-8291) leading to remote command execution.
/Proof of concept/: Upload the attached rce.gif file as profile image (change the `ping -c1 attacker.com' to some other shell command).
/Mitigation/: Upgrade Ghostscript; also


## Test-scripts for postgis in mason-repository using unsafe unzip of content from unclaimed bucket creates potential RCE-issues
- 等级：Critical | 项目：Mapbox | 披露：2020-07-28 | CVE：-
- 原文：https://hackerone.com/reports/329689

- - - - - - - - 
On March 25, 2018 @fransrosen reported a vulnerability to Mapbox. An AWS S3 bucket previously owned by Mapbox was reclaimed by this researcher, which is possible due to the global namespacing of S3 buckets. This bucket was still actively referenced in a test script. The bucket takeover therefore posed a possibility for remote code execution via this S3 bucket. 
Mapbox responded within a day and worked with the researcher to reclaim this bucket, as well as multiple other S3 buckets that had been claimed by the researcher and were still referenced in public Github repositories. 
The incident was fully resolved, including bounty payout, by April 27 2018 when all affected S3 buc


## OS Command Injection in Nexus Repository Manager 2.x -- Bypass for Nexus Repository Manage 2.14.15-01 Command Injection fix
- 等级：Critical | 项目：Central | 披露：2020-06-29 | CVE：-
- 原文：https://hackerone.com/reports/724599

- - - - - - - - 
https://support.sonatype.com/hc/en-us/articles/360033490774
An OS command injection vulnerability has been discovered in Nexus Repository Manager requiring immediate action. The vulnerability allows for an attacker with administrative access to nxrm to execute arbitrary commands on the system. We have mitigated the issue by not allowing the server to do this. This advisory provides the pertinent information needed to properly address this vulnerability, along with the details on how to reach us if you have any further questions or concerns.
This vulnerability was identified by an external researcher and has been verified by our security team. We are not aware of any active e


## Command Injection (via CVE-2019-11510 and CVE-2019-11539)
- 等级：Critical | 项目：U.S. | 披露：2020-05-07 | CVE：CVE-2019-11510,
- 原文：https://hackerone.com/reports/680480

- - - - - - - - 
**Summary:**
The Navy has a Pulse Secure SSL VPN (https://████████/dana-na/auth/url_default/welcome.cgi) that is vulnerable to:
CVE-2019-11510 - Pre-auth Arbitrary File Reading
CVE-2019-11539 - Post-auth Command Injection
vulnerable hostname from ssl certificate: ██████████.navy.mil
The pre-auth arbitrary file reading vulnerability (CVE-2019-11510) enables an un-authenicated user to read the file /data/runtime/mtmp/lmdb/dataa/data.mdb from the Pulse VPN device. This files contains admin and other users credentials in plain-text format. This information can be used to log into the pulse device as an administrator.
Once logged in as an administrator, the post-auth command inje


## Git flag injection - local file overwrite to remote code execution
- 等级：Critical | 项目：GitLab | 披露：2019-12-19 | CVE：-
- 原文：https://hackerone.com/reports/658013

- - - - - - - -


## Git flag injection leading to file overwrite and potential remote code execution
- 等级：Critical | 项目：GitLab | 披露：2019-12-19 | CVE：-
- 原文：https://hackerone.com/reports/653125

- - - - - - - -


## RCE on default Ubuntu Desktop >= 12.10 Quantal
- 等级：Critical | 项目：Internet | 披露：2019-11-12 | CVE：-
- 原文：https://hackerone.com/reports/192512

- - - - - - - - 
I recently reported a number of vulnerabilities in Canonical's Apport crash report software. These bugs provided RCE on a default install of Ubuntu Desktop >= 12.10 upon opening a malicious file. I reported the issues to the Apport maintainers and we coordinate the disclosure of these issues. 
Is the Internet Bug Bounty interested in providing bounties for RCE bugs affecting default Ubuntu installations? I have included a link to the Launchpad ticket and my blog post describing the issues in detail. Please let me know if this is something that you are interested in. I am happy to provide any further information that you require. 
https://bugs.launchpad.net/bugs/1648806
https


## Privilege Escalation From user to SYSTEM via unauthenticated command execution
- 等级：Critical | 项目：Ubiquiti | 披露：2019-11-08 | CVE：CVE-2019-15595
- 原文：https://hackerone.com/reports/544928

- - - - - - - - 
The vulnerability, or feature depending how you look at it, is the ability to execute commands using the 
evostream API interface that is exposed on localhost:7440. Since the evostream service is running as SYSTEM a user can use the launchprocess command,  http://docs.evostream.com/2.0/launchProcess.html, to execute any binary with supplied arguments. The only thing that is keeping this "feature" from allowing remote code execution is the fact that it listens on localhost only. However, if it were couple with an SSRF, an attacker could achieve full remote code execution.
## Impact
The ability to run arbitrary commands as SYSTEM from any user.
---


## OS Command Injection in Nexus Repository Manager 2.x(bypass CVE-2019-5475)
- 等级：Critical | 项目：Central | 披露：2019-10-29 | CVE：CVE-2019-15588,
- 原文：https://hackerone.com/reports/688270

- - - - - - - - 
## OS Command Injection in Nexus Repository Manager 2.x(bypass CVE-2019-5475)
# Maven artifact
**groupId:** org.sonatype.nexus.plugins
**artifactId:** nexus-yum-repository-plugin
**version:** 2.14.14-01
# Vulnerability
## Vulnerability Description
The Nexus Yum Repository Plugin is vulnerable to Remote Code Execution. All instances using CommandLineExecutor.java with user-supplied data is vulnerable, such as the Yum Configuration Capability.
## Additional Details
Take a look at the patch for CVE-2019-5475
 https://github.com/sonatype/nexus-public/commit/7b9939e71693422d3e09adc3744fa2e9b3a62a63#diff-4ab0523de106ac7a38808f0231fc8a23R84
![](1.png)
The `getCleanCommand` method i


## Mercurial git subrepo lead to arbritary command injection
- 等级：Critical | 项目：Internet | 披露：2019-09-26 | CVE：CVE-2017-17458
- 原文：https://hackerone.com/reports/294147

- - - - - - - - 
Hi IBB,
I'd like to submit a issue exist in Mercurial.
[code omitted]
Further details of my original report can be found at:
https://bz.mercurial-scm.org/show_bug.cgi?id=5730
And the Mercurial security advisory
https://www.mercurial-scm.org/wiki/WhatsNew#Mercurial_4.4.1_.282017-11-07.29
Thanks,
Terry
## Impact
A crafted mercurial repo with an evil git subrepo can lead to execute arbritary command on user's OS. And other web applications or clients support mercurial repo management or invoke hg related command also have a risk affected by this vulnerability.
---


## Local files could be overwritten in GitLab, leading to remote command execution
- 等级：Critical | 项目：GitLab | 披露：2019-07-17 | CVE：-
- 原文：https://hackerone.com/reports/587854

- - - - - - - -


## Remote Code Execution on www.semrush.com/my_reports on Logo upload
- 等级：Critical | 项目：Semrush | 披露：2019-06-24 | CVE：-
- 原文：https://hackerone.com/reports/403417

- - - - - - - - 
The Logo upload in the report constructor at: https://www.semrush.com/my_reports/constructor
{F340480}
is passed through a not properly patched version of ImageMagick. You can use Postscript to get Ghostscript to run which in return allows to trigger arbitrary commands on the server, leading to Remote Code Execution. Tavis Ormandy has also mentioned recently that the policy.xml needs to disable EPS,PS,PDF and XPS since all these have ways to trigger Ghostscript: http://openwall.com/lists/oss-security/2018/08/21/2
The following PoC-payload was used to get a reverse shell when issuing the upload:
Save it as `test.jpg` and upload it as an image for the logo:
[code omitted]
(`██


## h1-5411-CTF report: LFI / Deserialization / XXE vulnerability,
- 等级：Critical | 项目：h1-5411-CTF | 披露：2018-10-22 | CVE：-
- 原文：https://hackerone.com/reports/415233

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
**Summary:** 
h1-5411-ctf write-up
The CTF contained a Local File inclusion that enabled the attacker to read .php files (among others) from the server and by doing so, it helped to find out PHP serialization bug and the XXE vulnerability that was used as SSRF to exploit the hidden maintenance pages.
Flag: [code omitted]
**Description:** 
See attached .pdf file.
## Steps To Reproduce:
See attached .pdf file.
## Supp


## Cisco RCE
- 等级：Critical | 项目：Informatica | 披露：2018-09-21 | CVE：-
- 原文：https://hackerone.com/reports/411270

- - - - - - - - 
The researcher was able to complete RCE attack and download sensitive files. We have mitigated it by hardening the machine and port.
**Summary (researcher):**
There are opened classical cisco smart install service, which was successfully exploited.
Informatica is a fAsTeSt!!! bug fixer in my life.
Closing vulnerability in a 3-5 hours..!
And closing report in a day!
Gratz!
---


## Sending arbitrary IPC messages via overriding Function.prototype.apply
- 等级：Critical | 项目：Brave | 披露：2018-09-18 | CVE：-
- 原文：https://hackerone.com/reports/188086

- - - - - - - - 
## Summary:
Brave Browser allows to overwrite the internal js code from the user js code.
Using this behavior, an attacker can send arbitrary IPC messages and do UXSS, address bar spoofing, changing browser settings and so on. This bug is similar to #187542.
## Tested on: 
Brave	0.12.11
## Steps To Reproduce:
1. Go to this page: https://vulnerabledoma.in/brave/settings_change2.html 
[code omitted]
2. See `about:preferences`. You can confirm that your home page is changed to `http://attacker.example.com/`.
Also an attacker can do UXSS and address bar spoofing using this bug. Please see #187542's PoC .
#Technical Details
This `apply` in the `ipc_utils.js` is overwritten: 
[cod


## Sending arbitrary IPC messages via overriding Array.prototype.push
- 等级：Critical | 项目：Brave | 披露：2018-09-18 | CVE：-
- 原文：https://hackerone.com/reports/188561

- - - - - - - - 
## Summary:
This bug is similar to #187542 and #188086.
I found that also `Array.prototype.push` is exploitable.
## Tested on: 
Brave	0.12.12
## Steps To Reproduce:
1. Go to this page: https://vulnerabledoma.in/brave/settings_change3.html 
[code omitted]
2. See `about:preferences`. You can confirm that your home page is changed to `http://attacker.example.com/`.
Also an attacker can do UXSS and address bar spoofing using this bug. Please see #187542's PoC .
#Technical Details
This `push` in the `event_emitter.js` is overwritten: 
[code omitted]
Could you confirm this bug?
Thanks!
---


## Brave Browser unexpectedly allows to send arbitrary IPC messages
- 等级：Critical | 项目：Brave | 披露：2018-09-18 | CVE：-
- 原文：https://hackerone.com/reports/187542

- - - - - - - - 
## Summary:
I found that Brave Browser allows to overwrite the internal js code from the user js code.
Using this behavior, an attacker can send arbitrary IPC messages and do UXSS, address bar spoofing, changing browser settings and so on. 
## Steps to Reproduce:
1 .  An attacker overwrites `Function.prototype.call`, like this:
[code omitted]
2 .  An attacker calls `alert()`.
3 .  Brave's `alert()` function calls `Function.prototype.call` in the internal code. At this time, the overwritten `Function.prototype.call` is used in the `alert` internal code.
4 .  `Function.prototype.call` receives IPC messages as arguments. This arguments are replaced to arbitrary messages by step


## Vulnerability in project import leads to arbitrary command execution
- 等级：Critical | 项目：GitLab | 披露：2018-08-22 | CVE：-
- 原文：https://hackerone.com/reports/378148

- - - - - - - - 
**Summary:** 
A filename regular expression could be bypassed and enable the attacker to create a symbolic link in Gitlab upload directory by importing a specially crafted Gitlab export. Further more, Gitlab is designed to not delete project upload directory currently. So, the attacker could delete the imported project and then upload another specially crafted Gitlab export to a project with the same name, which leads to path traversal/arbitrary file upload and finally enables the attacker to be able to get a shell with the permission of the system gitlab user.
**Description:**
1. how to create a symbolic link in the upload directory
code in `file_importer.rb` uses `%r{.*/\.


## Malware in `active-support` gem
- 等级：Critical | 项目：RubyGems | 披露：2018-08-09 | CVE：CVE-2018-3779
- 原文：https://hackerone.com/reports/392311

- - - - - - - - 
This was sent to RubySec:
The gem duplicates official `activesupport` (no hyphen) code, but adds a compiled extension. The extension attempts to resolve a base64 encoded domain (`29faea63.planfhntage.de`), downloads a payload, and executes.
active-support-5.2.0.gem/data/ext/trellislike/unflaming/waffling/extconf.rb
[code omitted]
## Impact
Run arbitrary code on a victim's machine.
---


## Remote Command Execution vulnerability in pullit
- 等级：Critical | 项目：Node.js | 披露：2018-06-14 | CVE：-
- 原文：https://hackerone.com/reports/315773

- - - - - - - - 
I would like to report Remote Command Execution vulnerability in pullit
It allows remote command execution such as reading or writing to the file system, and executing other programs under the current user running the pullit node executable.
## Module
pullit
https://www.npmjs.com/package/pullit
version: 1.3.0


## `macaddress` concatenates unsanitized input into exec() command
- 等级：Critical | 项目：Node.js | 披露：2018-05-11 | CVE：-
- 原文：https://hackerone.com/reports/319467

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
I would like to report code injection in `macaddress`
It allows to inject arbitrary shell commands if the user input can influence the `iface` argument.
# Module
**module name:** macaddress
**version:** 0.2.8
**npm page:** `https://www.npmjs.com/package/macaddress`
## Module Description
> Retrieve MAC addresses in Linux, OS X, and Windows.
## Module Stats
81 238 downloads in the last day
1 632 083 downloads in the l


## `command-exists` concatenates unsanitized input into exec()/execSync() commands
- 等级：Critical | 项目：Node.js | 披露：2018-05-11 | CVE：-
- 原文：https://hackerone.com/reports/324453

- - - - - - - - 
I would like to report command injection in `command-exists`.
It allows to inject and execute arbitrary shell commands while trying to determine if a crafted command exists.
# Module
**module name:** `command-exists`
**version:** 1.2.2
**npm page:** `https://www.npmjs.com/package/command-exists`
## Module Description
> node module to check if a command-line command exists
## Module Stats
5 480 downloads in the last day
74 405 downloads in the last week
294 869 downloads in the last month
# Vulnerability
## Vulnerability Description
`commandName` argument is not properly escaped before being concatenated into the command that is passed to `exec()`/`execSync()`.
See https://gi


## `fs-path` concatenates unsanitized input into exec()/execSync() commands
- 等级：Critical | 项目：Node.js | 披露：2018-05-11 | CVE：CVE-2020-8298
- 原文：https://hackerone.com/reports/324491

- - - - - - - - 
I would like to report command injection in `fs-path`.
It allows to inject and execute arbitrary shell commands while performing various operations from `fs-path` API like copying files.
# Module
**module name:** `fs-path`
**version:** 0.0.24
**npm page:** `https://www.npmjs.com/package/fs-path`
## Module Description
> Useful file utitiles.
## Module Stats
108 downloads in the last day
2 916 downloads in the last week
13 186 downloads in the last month
# Vulnerability
## Vulnerability Description
Arguments are not properly escaped before being concatenated into the command that is passed to `exec()`/`execSync()`.
 See https://github.com/pillys/fs-path/blob/master/lib/index.j


## Command injection by overwriting authorized_keys file through GitLab import
- 等级：Critical | 项目：GitLab | 披露：2018-04-27 | CVE：CVE-2017-0915
- 原文：https://hackerone.com/reports/298873

- - - - - - - - 
The `Projects::GitlabProjectsImportService` contains a vulnerability that allows an attacker to write files to arbitrary directories on the server. This leads to an arbitrary command execution vulnerability by overwriting the `authorized_keys` file. To reproduce, sign in to a GitLab instance that has GitLab import enabled. This is enabled by default, so I'd assume that this vulnerability applies to most GitLab instances. I've installed my GitLab instance through Omnibus.
Next up, intercept your network traffic and upload a GitLab import file. Observe the following request being made to the server:
**Request**
[code omitted]
Now take a closer look at the code that is being ex


## `whereis` concatenates unsanitized input into exec() command
- 等级：Critical | 项目：Node.js | 披露：2018-03-28 | CVE：CVE-2018-3772
- 原文：https://hackerone.com/reports/319476

- - - - - - - - 
I would like to report command injection in `whereis`
It allows to inject arbitrary shell commands by trying to locate crafted filenames.
# Module
**module name:** whereis
**version:** 0.4.0
**npm page:** `https://www.npmjs.com/package/whereis`
## Module Description
> Simply get the first path to a bin on any system.
## Module Stats
Stats
101 downloads in the last day
5 403 downloads in the last week
18 945 downloads in the last month
~227 340 estimated downloads per year [JUST FOR REFERENCE,  ~DOWNLOADS PER MONTH*12]
# Vulnerability
## Vulnerability Description
File name argument is not properly escaped before being concatenated into the command that is passed to `exec()`.


