# HackerOne 实战案例：server-side-request-forgery-ssrf

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## DNS Rebinding Attack
- 等级：Critical | 项目：arkadiyt-projects | 披露：2025-10-19 | CVE：-
- 原文：https://hackerone.com/reports/3383095

- - - - - - - - 
Hi, there is a  DNS rebinding vulnerability in your SSRF filter. 
{F4891755}
You validate the hostname's IP address, but then pass the hostname to Net::HTTP.start(), which does its own DNS lookup. An attacker can control a DNS server that returns a safe public IP during validation, then returns 127.0.0.1 when Net::HTTP resolves it shortly later...
[code omitted]
Example POC: 
Attacker sets up evil.com DNS to alternate responses. First query (your validation) returns 8.8.8.8. Second query (Net::HTTP's internal lookup) returns 127.0.0.1. As a result: SsrfFilter.get('http://evil.com:6379') bypasses all protection and hits some internal service on localhost..
Suggested fix: 
Con


## Server-Side Request Forgery (SSRF) via Game Export API
- 等级：Critical | 项目：Lichess | 披露：2025-06-03 | CVE：-
- 原文：https://hackerone.com/reports/3165242

- - - - - - - - 
# Summary
Hello Lichess Team,
I found a Server-Side Request Forgery vulnerability in the game export functionality. An attacker can make the Lichess server send HTTP requests to arbitrary URLs by manipulating the `players` parameter. This works on public endpoints that don't require any authentication
# Description:
The issue is in the game export API endpoints that accept a `players` parameter. When I looked at the code, I noticed that this parameter gets passed directly to `RealPlayerApi.apply()` without any URL validation
Here's the problematic flow I found:
In `app/controllers/Game.scala`:
[code omitted]
Then in `modules/api/src/main/GameApiV2.scala`:
[code omitted]
And 


## SSRF in Autodesk Rendering leading to account takeover
- 等级：Critical | 项目：Autodesk | 披露：2025-03-18 | CVE：-
- 原文：https://hackerone.com/reports/3024673

- - - - - - - - 
A server side request forgery (SSRF) vulnerability was found in Autodesk Rendering, which could have allowed an attacker to send a malicious link to a victim and gain control of their account while logged in. Autodesk has fixed the vulnerability and we thank @metereorpreter for reporting this issue.
**Summary (researcher):**
SSRF enables 1-click account takeover / exposes AWS metadata
---


## Server Side Request Forgery (SSRF) via Analytics Reports
- 等级：Critical | 项目：HackerOne | 披露：2023-12-08 | CVE：-
- 原文：https://hackerone.com/reports/2262382

- - - - - - - - 
Hello Gents, I would like to report an issue where attackers are able to read internal files via an SSRF vulnerability.
## Proof of concept
+ ███
## Impact
SSRF.
Thanks and have a nice day!
We recently received a critical server-side request forgery (SSRF) vulnerability report through our bug bounty program. The issue allowed attackers to make internal requests from our application servers by exploiting a lack of output sanitization in an error message. By crafting malicious requests, an attacker could have accessed internal AWS services and obtained temporary credentials. 
Upon receiving the report, we were able to reproduce and verify the issue. We have implemented a fix t


## mail.acronis.com is vulnerable to zero day vulnerability CVE-2022-41040
- 等级：Critical | 项目：Acronis | 披露：2022-10-13 | CVE：CVE-2022-41040
- 原文：https://hackerone.com/reports/1719719

- - - - - - - - 
Hello Acronis team,
Please run
curl -ksL -m5  -o /dev/null -I -w "%{http_code}" "https://mail.acronis.com/autodiscover/autodiscover.json?Email=autodiscover/autodiscover.json@outlook.com&Protocol=ActiveSync"
curl -ksL -m5 "https://mail.acronis.com/autodiscover/autodiscover.json?Email=autodiscover/autodiscover.json@outlook.com&Protocol=ActiveSync" | grep Protocol
and get following output
404 and {"Protocol":"ActiveSync","Url":"https://eas.outlook.com/Microsoft-Server-ActiveSync"}
Proving that  mail.acronis.com is vulnerable to CVE-2022-41040
Poc video attached
## Impact
SSRF can be used to for unauthorized actions or access to confidential data.
mail.acronis.com was vulnerable


## SSRF on http://www.███████/crossdomain.php via url parameter
- 等级：Critical | 项目：Sony | 披露：2022-10-06 | CVE：-
- 原文：https://hackerone.com/reports/971590

- - - - - - - - 
The researcher reported that a Sony endpoint was vulnerable to Local File Inclusion (LFI) and Server-Side Request Forgery (SSRF) vulnerabilities. The researcher used the LFI vulnerability to read sensitive files such as /etc/passwd from the web server. The researcher also demonstrated using the SSRF vulnerability to view EC2 instance metadata, and to retrieve an externally hosted .svg file to execute a reflected Cross-Site Scripting (XSS) attack.
---


## Full read SSRF via Lark Docs `import as docs` feature
- 等级：Critical | 项目：Lark | 披露：2022-01-28 | CVE：-
- 原文：https://hackerone.com/reports/1409727

- - - - - - - - 
A SSRF (server side request forgery) vulnerability was found in the LarkDocs using the "import as docs" feature, which could have potentially been used to access services running on the internal network. We thank @sirleeroyjenkins for reporting this to our team and confirming the resolution.
---


## Full read SSRF in www.evernote.com that can leak aws metadata and local file inclusion
- 等级：Critical | 项目：Evernote | 披露：2021-12-06 | CVE：-
- 原文：https://hackerone.com/reports/1189367

- - - - - - - - 
## Summary:
The following endpoint was found to be vulnerable to SSRF :  `https://www.evernote.com/ro/aHR0cDovLzE2OS4yNTQuMTY5LjI1NC8jdGVzdC5qcw==/-1430533899.js`
The endpoint take a path in url and retrieve its content. it is supposed to be use on path but it can be used on URL to get access to internal network :SSRF
And It can also be used with file uri : Local file inclusion.
## Steps To Reproduce:


## SSRF to AWS file read
- 等级：Critical | 项目：Lab45 | 披露：2021-09-16 | CVE：-
- 原文：https://hackerone.com/reports/978823

- - - - - - - - 
## Summary:
after seeing the disclosure it looks like the bug was not fixed properly
## Steps To Reproduce:
copy and paste the request below and paste it into Burpsuite repeater
`GET /community-app-assets/api/proxy-post?url=http%3A%2F%2F169.254.169.254%2F/latest/meta-data/iam/security-credentials/ecsInstanceRole%3Fu%3D65bd5a1857b73643aad556093%26amp%3Bid%3D934e9ffdc5 HTTP/1.1
Host: cognitive.topcoder.com
Content-Length: 108
Authorization: ApiKey 130edef6-2289-4407-bfcf-3eedacebb860
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36
Content-Type: application/x-www-form-urlencoded
Accept: */*
Origin: 


## Server Side Request Forgery
- 等级：Critical | 项目：Lark | 披露：2021-03-29 | CVE：-
- 原文：https://hackerone.com/reports/644238

- - - - - - - - 
A SSRF (server side request forgery) vulnerability was found in the chat feature of Lark Suite on MacOS, which could have potentially been used to access services and web applications running on the internal network. We thank @jin0ne for reporting this to our team and confirming the resolution.
**Summary (researcher):**
Details
https://jinone.github.io/bugbounty-a-simple-ssrf/
---


## CVE-2021-26855 on ████████ resulting in SSRF
- 等级：Critical | 项目：U.S. | 披露：2021-03-24 | CVE：CVE-2021-26855
- 原文：https://hackerone.com/reports/1119228

- - - - - - - - 
**Description:**
***CVE-2021-26855*** exists on ***███████ resulting*** in SSRF
## References
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-26855
https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26855
## Impact
Server Side Request Frogery
## System Host(s)
███████
## Affected Product(s) and Version(s)
## CVE Numbers
CVE-2021-26855
## Steps to Reproduce
[code omitted]
OUTPUT:
██████████
## Suggested Mitigation/Remediation Actions
---


## SSRF due to CVE-2021-26855 on ████████
- 等级：Critical | 项目：U.S. | 披露：2021-03-24 | CVE：CVE-2021-26855
- 原文：https://hackerone.com/reports/1119224

- - - - - - - - 
**Description:**
There exists a Server Side Request Frogery (SSRF) on ***█████████*** due to ***CVE-2021-26855***
## References
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-26855
https://portal.msrc.microsoft.com/en-US/security-guidance/advisory/CVE-2021-26855
## Impact
Server Side Request Frogery
## System Host(s)
██████
## Affected Product(s) and Version(s)
## CVE Numbers
CVE-2021-26855
## Steps to Reproduce
[code omitted]
Output:
█████████
## Suggested Mitigation/Remediation Actions
---


## Stored XSS & SSRF in Lark Docs
- 等级：Critical | 项目：Lark | 披露：2021-02-05 | CVE：-
- 原文：https://hackerone.com/reports/892049

- - - - - - - - 
A stored XSS (cross site scripting) vulnerability was discovered in Lark Docs that could be escalated into a Server Side Request Forgery (SSRF) vulnerability if opened in a headless browser on the Lark server. The vulnerability has been resolved. We thank @mike12 for reporting this to our team and confirming the resolution.
---


## Hacky Holidays CTF Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1066801

- - - - - - - - 
Greetings team
Yay! Finally I made it to the end, thank you very much for launching this fantastic event, I had to review topics that I thought I knew, learned a lot and I am sure that I will continue learning with the community :)
{F1130889}
Hacky Holidays!
P.S. I will put my writeup in my next comment.
## Impact
---
---


## Infiltrating into Grinch-Networks and saving Christmas!
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1069141

- - - - - - - - 
#
**Summary (researcher):**
Hi, you can find the write-up for this CTF here : https://castilho101.github.io/posts/hackerone-ctf-christmas
---


## 12 Days of CTF Walkthroughs
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1068433

- - - - - - - - 
# h1-ctf: 12 Days of Hacky Holidays
This is my writeup for 12 Days of Hacky Holidays. The report is written such that beginners to CTFs will be able to learn the tricks of the trade.
## The Mission:
> The Grinch has gone hi-tech this year with the intention of ruining the holidays 😱We need you to infiltrate his network and take him down! Check out all the details on https://hackerone.com/h1-ctf  to learn more!
## Contents
I laid out all the days here with their title and vulnerability. For more information about the vulnerability types, https://portswigger.net/web-security/all-materials is a great resource.
Day | Title | Vulnerability
--- | --- | ---
__1__ | robots.txt | Inf


## SSRF via maliciously crafted URL due to host confusion
- 等级：Critical | 项目：curl | 披露：2021-01-08 | CVE：CVE-2018-3774
- 原文：https://hackerone.com/reports/704621

- - - - - - - - 
## Summary:
Curl is vulnerable to SSRF due to improperly parsing the host component of the URL compared to other URL parsers and the [URL living standard](https://url.spec.whatwg.org/).
## POC
`curl -sD - -o /dev/null "http://google.com:80\\@yahoo.com/"`
Curl makes a request to `yahoo.com` instead of `google.com`.
## Supporting Material/References:
  * [Exact question to URL standards body](https://github.com/jsdom/whatwg-url/issues/137#issuecomment-536797948)
  * [CVE-2018-3774](https://nvd.nist.gov/vuln/detail/CVE-2018-3774) similar vulnerability in an NPM lib
    * See also: https://hackerone.com/reports/384029
To quote the standards body issue:
> Specifically the authori


## Full Read SSRF on Gitlab's Internal Grafana
- 等级：Critical | 项目：GitLab | 披露：2020-08-07 | CVE：-
- 原文：https://hackerone.com/reports/878779

- - - - - - - - 
Apparently, Grafana is bundled with Gitlab by default. So the grafana instance that is accessible via `/-/grafana/`is vulnerable to the SSRF outlined below.
## Summary
By chaining together some redirects and a URL decoding bug, it is possible to achieve a full-read, unauthenticated, SSRF from your Grafana instance. It is possible to recreate this bug on `dev.gitlab.org/-/grafana`. 
## Details
In the grafana source code, the following route is defined:
[code omitted]
This route takes the hash from under `/avatar/:hash` and routes it to `secure.grafana.com` in order to access a user's gravatar image. The code that does this looks like this:
[code omitted]
The `this.hash` refer


## Blind SSRF at https://chat.makerdao.com/account/profile
- 等级：Critical | 项目：BlockDev | 披露：2020-04-14 | CVE：-
- 原文：https://hackerone.com/reports/846184

- - - - - - - - 
Blind SSRF at https://chat.makerdao.com/account/profile
---


## SSRF in the Custom Integration Webhook discloses AWS metadata
- 等级：Critical | 项目：Dynatrace | 披露：2020-03-23 | CVE：-
- 原文：https://hackerone.com/reports/643278

- - - - - - - - 
Dynatrace allows customers to set up a webhook integration in order to automatically send updates to a specific endpoint of choice. This submission identified a way how the setup made it possible to accidentally obtain AWS metadata. Dynatrace remediated the vulnerability and found no evidence of abuse associated with it. 
This is also mentionend in https://www.dynatrace.com/support/help/whats-new/release-notes/managed/sprint-186/.
---


## TURN server allows TCP and UDP proxying to internal network, localhost and meta-data services
- 等级：Critical | 项目：Slack | 披露：2020-03-12 | CVE：-
- 原文：https://hackerone.com/reports/333419

- - - - - - - - 
The TURN servers used by Slack allow TCP connections and UDP packets to be proxied to the internal network. This gives an attacker the ability to scan and interact with internal systems.
The attacker may proxy TCP connections to the internal network by setting the `XOR-PEER-ADDRESS` of the TURN connect message (method `0x000A`, <https://tools.ietf.org/html/rfc6062#section-4.3>) to a private IPv4 address.
UDP packets may be proxied by setting the `XOR-PEER-ADDRESS` to a private IP in the TURN send message indication (method `0x0006`, <https://tools.ietf.org/html/rfc5766#section-10>).
Please check the attached report for additional details.
## Impact
By abusing this feature an


## SSRF & unrestricted file upload on https://my.stripo.email/
- 等级：Critical | 项目：Stripo | 披露：2020-02-19 | CVE：-
- 原文：https://hackerone.com/reports/771382

- - - - - - - - 
The researcher discovered an SSRF & unrestricted file upload (Remote code execution ) vulnerabilities .
---


## https://████████ Impacted by DNN ImageHandler SSRF
- 等级：Critical | 项目：U.S. | 披露：2019-10-08 | CVE：-
- 原文：https://hackerone.com/reports/482634

- - - - - - - - 
Summary:
https://███████ runs DNN 8.0.0 to 9.1.1 and is impacted by CVE 2017-0929 allowing for a SSRF through the DNN ImageHandler. Origin servers will request any image file supplied by the attacker. This allows for internal NIPR sites to be mapped and accessed through a vulnerable host. The attack is limited by file extension.
Impact
Vulnerable site allows interaction with internal NIPR sites. Pulling default image files from internal NIPR sites verifies the site is online and responsive. Discloses origin IP addresses, and could be manipulated further.  This could also be used as a defacement technique making the sight display images of radical ideologies or pornography.  


## SSRF in https://www.zomato.com████ allows reading local files and website source code
- 等级：Critical | 项目：Eternal | 披露：2018-02-28 | CVE：-
- 原文：https://hackerone.com/reports/271224

- - - - - - - - 
@nbsp found a SSRF vulnerability which leads to read local files from the web server (source code & system files). 
We have resolved the issue quickly and rewarded the researcher.
---


## SSRF Filter Bypass via Unblocked NAT64 Local-Use IPv6 Prefix (64:ff9b:1::/48)
- 等级：High | 项目：arkadiyt-projects | 披露：2026-03-31 | CVE：-
- 原文：https://hackerone.com/reports/3634400

- - - - - - - - 
## Summary:
`ssrf_filter` v1.3.0 blocks `64:ff9b::/96`, but doesnt block the NAT64 local-use prefix `64:ff9b:1::/48`, allowing those addresses to be treated as public. This enables SSRF requests through `/fetch` to internal-equivalent targets encoded under that prefix when routable in the deployment environment.
## Steps To Reproduce:
1. Like previous report, start our lab first :) (I'm using the library in Docker)
2. Start a second app container with `NET_ADMIN` so we can add a test IPv6 route/address.
[code omitted]
3. Install `iproute2` in that container and add NAT64 local-use address `64:ff9b:1::7f00:1` to loopback.
[code omitted]
4. Start a local HTTP service bound to 


## Gopher Protocol Command Injection (SSRF Smuggling)
- 等级：High | 项目：curl | 披露：2026-01-14 | CVE：-
- 原文：https://hackerone.com/reports/3508785

- - - - - - - - 
## Summary
The `curl` Gopher protocol handler is vulnerable to command injection through URL-encoded CRLF sequences in the path. This allows an attacker to "smuggle" additional Gopher selectors or arbitrary commands into a single Gopher request. By using `%0d%0a` in the URL, an attacker can break the line-delimited Gopher protocol and force `curl` to send multiple distinct request lines to the server.
## Affected Component
- **File:** `lib/gopher.c`
- **Function:** `gopher_do`
- **Line:** 101
- **Vulnerable Code:** `Curl_urldecode` call with `REJECT_ZERO` flag
## Vulnerability Details


## External service interaction (HTTP)
- 等级：High | 项目：AWS | 披露：2024-10-04 | CVE：-
- 原文：https://hackerone.com/reports/2731133

- - - - - - - - 
There is External service interaction ( DNS and HTTP ) vulnerability in
url :  ████ in this video 
██████████
## Impact
The External Service Interaction arise when it is possible for a attacker to induce application to interact with the arbitrary external service such as DNS HTTP etc.
The External Service Interaction can is not limited to HTTP,HTTPS or DNS, you can lead to FTP, SMTP etc. Such weakness can lead to DDoS attack.
The External Service Interaction can lead to OS Command Injection, DOS Attack, DDOS Attack or Code Manipulation
Thank you for bringing this issue to our attention. Upon review, we identified that the related infrastructure was previously deprecated, and


## SSRF and secret key disclosure found on Turbonomic endpoint
- 等级：High | 项目：IBM | 披露：2024-09-19 | CVE：-
- 原文：https://hackerone.com/reports/2697592

- - - - - - - - 
SSRF and secret key disclosure found on Turbonomic endpoint were reported to IBM, analyzed and have been remediated. Thank you to our external researcher, mersa-v6.
---


## SSRF and secret key disclosure found on Turbonomic endpoint
- 等级：High | 项目：IBM | 披露：2024-09-19 | CVE：-
- 原文：https://hackerone.com/reports/2697601

- - - - - - - - 
SSRF and secret key disclosure found on Turbonomic endpoint were reported to IBM, analyzed and have been remediated. Thank you to our external researcher, mersa-v6.
---


## Unauthenticated full-read SSRF via Twilio integration
- 等级：High | 项目：Rocket.Chat | 披露：2024-08-04 | CVE：CVE-2024-39713
- 原文：https://hackerone.com/reports/1886954

- - - - - - - - 
A Server-Side Request Forgery (SSRF) affects Rocket.Chat's Twilio webhook endpoint before version 6.10.1.
---


## /applications/dpc_(get|post) provide full access to api.steampowered.com with the Dota2 API key
- 等级：High | 项目：Valve | 披露：2024-07-30 | CVE：-
- 原文：https://hackerone.com/reports/674800

- - - - - - - - 
Insufficient validation of parameters enabled using path traversal to call arbitrary API methods using an API key that had elevated privileges for Dota2.
**Summary (researcher):**
.
---


## important: Apache HTTP Server on WIndows UNC SSRF (CVE-2024-38472)
- 等级：High | 项目：Internet | 披露：2024-07-13 | CVE：CVE-2024-38472
- 原文：https://hackerone.com/reports/2585385

- - - - - - - - 
I reported this vulnerability through the official Apache HTTP Server security email on April 1, 2024, and received a fix along with a CVE number on July 1, 2024. You can check detailed information from there:
> https://httpd.apache.org/security/vulnerabilities_24.html
## Impact
SSRF in Apache HTTP Server on Windows allows to potentially leak NTML hashes to a malicious server via SSRF and malicious requests or content
Users are recommended to upgrade to version 2.4.60 which fixes this issue. Note: Existing configurations that access UNC paths will have to configure new directive "UNCList" to allow access during request processing.
###important: Apache HTTP Server on WIndows 


## Libuv: Improper Domain Lookup that potentially leads to SSRF attacks
- 等级：High | 项目：Internet | 披露：2024-03-29 | CVE：CVE-2024-24806
- 原文：https://hackerone.com/reports/2429894

- - - - - - - - 
I recently encountered a challenge in a CTF competition that led me to discover a vulnerability within Node.js, present in all versions after v10. Upon further investigation and code debugging, it became apparent that the vulnerability originated from its direct dependency, `libuv`.
I submitted a report to the Node.js team via HackerOne, and they subsequently connected me with the libuv team. This collaboration resulted in the identification and resolution of the vulnerability, now recorded as CVE-2024-24806.
## Impact
This vulnerability could allow an attacker to craft payloads that results in **SSRF** attacks and **Internal API Access**. Full explanation of vulnerability, 


## Lack of sanitization of the billing address in pdf invoice
- 等级：High | 项目：Semrush | 披露：2024-03-06 | CVE：-
- 原文：https://hackerone.com/reports/2077985

- - - - - - - - 
Adam identified a vulnerability that allowed the HTML code injection into payment invoice PDFs. This vulnerability arose from insufficient content sanitization during the interaction between services, where considered trustworthy content from the user service was transferred to the invoice generation system without proper validation.
It's important to note that the PDF generation backend operates in isolation from the payment infrastructure. As a result, it does not have the capability to access sensitive information.
The subsequent internal review revealed no evidence of this vulnerability being exploited by unauthorized parties.
---


## SSRF in https://couriers.indrive.com/api/file-storage
- 等级：High | 项目：inDrive | 披露：2024-01-16 | CVE：-
- 原文：https://hackerone.com/reports/2300358

- - - - - - - - 
## Summary:
SSRF in  ` url ` parameter in https://couriers.indrive.com/api/file-storage
## Steps To Reproduce:
I will try to demonstrate it using burp collaborator 
  1. Request https://couriers.indrive.com/api/file-storage?url=http://va99zfc0lxpm75ogmcjhz8xij9pzdo.oastify.com  ( replace ` url ` value with your burp collaporator )
  1. Notice the contnet being displayed in the response and also the Interaction in your burp collaborator
* The Request 
[code omitted]
* The Response 
[code omitted]
## Supporting Material/References:
████
██████████
████████
## Note
If you request any website like for example ` www.google.com `,  ` https://couriers.indrive.com/api/file-storage?u


## External service interaction ( DNS and HTTP ) in www.████████
- 等级：High | 项目：U.S. | 披露：2023-06-23 | CVE：-
- 原文：https://hackerone.com/reports/1704024

- - - - - - - - 
There is External service interaction ( DNS and HTTP ) vulnerability in www.█████████
Here is an example request :
[code omitted]
And the Burp Collaborator recived this information :
DNS request recived from : ████████
HTTP request recived from : ███
███
█████████
## Impact
The External Service Interaction arise when it is possible for a attacker to induce application to interact with the arbitrary external service such as DNS HTTP etc.
The External Service Interaction can is not limited to HTTP,HTTPS or DNS, you can lead to FTP, SMTP etc. Such weakness can lead to DDoS attack.
The External Service Interaction can lead to OS Command Injection, DOS Attack, DDOS Attack or Code


## Blind SSRF to internal services in matrix preview_link API
- 等级：High | 项目：Reddit | 披露：2023-04-26 | CVE：-
- 原文：https://hackerone.com/reports/1960765

- - - - - - - - 
## Summary:
Reddit' new chat is based on Matrix software which has preview_link functionality which doesn't filter the URL before sending the request
## Impact:
Attacker can enumerate services by grabbing og:title and port scanning, also possible RCE escalation (Asking for permission on this one)
## Steps To Reproduce:
  1. Visit the https://matrix.redditspace.com/_matrix/media/r0/preview_url/?url=*
  2. Replace * with http://██████ to get og:title ███████
  3. Replace * with http://█████████ to get og:title ███████
 4. Replace * with http://██████████to get og:title ██████
 5. Replace * with ████████ to get og:title █████████
Note: If the request is stuck and not responding


## Unauthenticated Blind SSRF at https://█████ via xmlrpc.php file
- 等级：High | 项目：U.S. | 披露：2023-04-14 | CVE：-
- 原文：https://hackerone.com/reports/1890719

- - - - - - - - 
**Description:**
Hi team,
I would like to report a security vulnerability I discovered on your website. I was able to perform Server-Side Request Forgery (SSRF) attacks via the xmlrpc.php file at https://████████ endpoint.
Using a simple POST request to the xmlrpc.php endpoint, I was able to bypass input validation and send a request to an external URL.
I have attached a proof of concept (PoC) script that demonstrates this vulnerability. It sends a request to my VPS server using interact.sh client (https://github.com/projectdiscovery/interactsh), but an attacker could use this technique to send requests to any URL of their choosing.
## References
https://www.sonarsource.com/


## Blind SSRF via image upload URL downloader on https://██████/
- 等级：High | 项目：U.S. | 披露：2022-10-14 | CVE：-
- 原文：https://hackerone.com/reports/1691501

- - - - - - - - 
**Description:**
Dear DoD,
I found Blind SSRF on one domain from Hack US program.  Original domain is https://█████/ but when you make account and login it redirects you to https://███/my/. Here's the video PoC:
██████
Thank you!
## Impact
In a typical SSRF attack, the attacker might cause the server to make a connection to internal-only services within the organization's infrastructure. In other cases, they may be able to force the server to connect to arbitrary external systems, potentially leaking sensitive data such as authorization credentials. The attack can often result in unauthorized actions or access to data within the organization, either in the vulnerable applica


## Blind SSRF External Interaction on ████████
- 等级：High | 项目：MTN | 披露：2022-08-21 | CVE：-
- 原文：https://hackerone.com/reports/1220688

- - - - - - - - 
Hii Security Team,
I am S █████(Metaxone Certified Ethical Hacker) and a Security Researcher I just checked your website and found Blind SSRF External Interaction on ██████████
What is SSRF?
Server-side request forgery (also known as SSRF) is a web security vulnerability that allows an attacker to induce the server-side application to make HTTP requests to an arbitrary domain of the attacker's choosing.
In typical SSRF examples, the attacker might cause the server to make a connection back to itself, or to other web-based services within the organization's infrastructure, or to external third-party systems.
SSRF attacks often exploit trust relationships to escalate an attack

