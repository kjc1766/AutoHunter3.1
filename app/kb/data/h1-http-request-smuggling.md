# HackerOne 实战案例：http-request-smuggling

_27 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## HTTP request smuggling with Origin Rules using newlines in the host_header action parameter
- 等级：Critical | 项目：Cloudflare | 披露：2022-06-27 | CVE：-
- 原文：https://hackerone.com/reports/1575912

- - - - - - - - 
The `host_header` action parameter available to rulesets in the [Origin Rules API](https://developers.cloudflare.com/rules/origin-rules/) lacked sufficient input validation i.e., allowing CRLF characters. Because of this, it was possible to inject arbitrary headers and, as a consequence, smuggle HTTP requests. This vulnerability enabled bypassing security products such as Cloudflare Access and viewing the content of internal origin servers.
The issue was fixed by Cloudflare engineers and an Internal investigation proved that no Cloudflare customers were affected by exploitation of this vulnerability.
As a recommendation, we advise Cloudflare Access customers  to always verif


## HTTP Request Smuggling in Transform Rules using hexadecimal escape sequences in the concat() function
- 等级：Critical | 项目：Cloudflare | 披露：2022-05-16 | CVE：-
- 原文：https://hackerone.com/reports/1478633

- - - - - - - - 
The Edge Rules engine used by Cloudflare Transform Rules features string modifying functions like lower() and concat(), which accepted hexadecimal-encoded characters such as ”\x0a\x0d“. This allowed for manipulation of request headers (e.g. injecting an additional header) and, as a consequence, made HTTP smuggling attack (TE.CL) possible. This vulnerability enabled an attacker to bypass security products such as Cloudflare Access and view the content of internal origin servers. 
This bug in hexadecimal parsing was fixed by the relevant engineering team. We rewarded this finding as critical as well as a bonus for a high quality, detailed report. 
Internal investigation confir


## HTTP Request Smuggling via HTTP/2
- 等级：Critical | 项目：Basecamp | 披露：2021-08-27 | CVE：-
- 原文：https://hackerone.com/reports/1211724

- - - - - - - - 
HTTP Request Smuggling via HTTP/2
---


## HTTP request smuggling on Basecamp 2 allows web cache poisoning
- 等级：Critical | 项目：Basecamp | 披露：2020-10-28 | CVE：-
- 原文：https://hackerone.com/reports/919175

- - - - - - - - 
It is found that an authenticated Basecamp 2 user can desync front and backend servers and poison the socket with harmful response for the next visitor.  During redirect probe, It also appears that front-end infrastructure performs caching of content. Using HTTP request smuggling attack, It is possible to poison the cache with the off-site redirect response using `X-Forwarded-Host` request header in smuggled request. This will make the attack persistent, affecting any user who subsequently requests the affected URL.
## Validation steps
**1.**  Open https://requestbin.com/r/enjv2g5042bg in your browser for request capturing.
**2.** Paste the following request in Burp repeater


## Unauthenticated request smuggling on launchpad.37signals.com
- 等级：Critical | 项目：Basecamp | 披露：2020-10-28 | CVE：-
- 原文：https://hackerone.com/reports/867577

- - - - - - - - 
## Description
By sending an ambiguous request on the rails application on `launchpad.37signals.com`, an attacker can desynchronise frontend and backend servers, leaving the socket to the backend server poisoned with a harmful response. This response will then be served up to the next visitor.
The desync occurs when sending a request with a `Content-Length` header and a valid `Transfer-Encoding` header followed by an invalid `Transfer-Encoding` header. The frontend server only examines the second `Transfer-Encoding` which is invalid, so it uses the `Content-Length` instead. However the backend server prioritises the valid `Transfer-Encoding` header and therefore ignores the 


## Stealing Zomato X-Access-Token: in Bulk using HTTP Request Smuggling on api.zomato.com
- 等级：Critical | 项目：Eternal | 披露：2020-07-09 | CVE：-
- 原文：https://hackerone.com/reports/771666

- - - - - - - - 
# Intro
Hi Zomato Security Team!
My name is Evan Custodio and this is my first time evaluating your platform. I specialize in looking for server-side vulnerabilities. Recently I've taken a deep look at HTTP Request Smuggling issues. I have custom tools to evaluate over 150 types of HTTP Smuggling Payloads. When evaluating your platform I've found one asset that falls victim to HTTP Smuggling Attacks that result in: PII/Information Leakage, Session Takeover, Victim Request Hijacking/Forging and Forced Victim Redirection to Attacker Endpoint. this is a serious bug that should be dealt with immediately as any bad Actor could use these issues to stage attacks that could cause se


## Mass account takeovers using HTTP Request Smuggling on https://slackb.com/ to steal session cookies
- 等级：Critical | 项目：Slack | 披露：2020-03-12 | CVE：-
- 原文：https://hackerone.com/reports/737140

- - - - - - - - 
Hi Slack Security Team!
My name is Evan and I'm a first time bug hunter to your platform :) Because you guys were running a month long bounty promotion I decided to take a little of my time and gently perform recon on your platform. Specifically the area of interest I focus in is HTTP Request Smuggling. I developed tooling to actively target some advanced HTTP Smuggling exploits and ran it on your in-scope assets. In my research I stumbled across a finding that I consider extremely critical not only for Slack but for all customers and organizations which share their privatedata/channels/conversations on Slack.
The bug chain is as follows:
1) HTTP Request Smuggling CTLE to Ar


## HTTP request smuggling using malformed Transfer-Encoding header
- 等级：Critical | 项目：Node.js | 披露：2020-03-07 | CVE：CVE-2019-15605
- 原文：https://hackerone.com/reports/735748

- - - - - - - - 
Please see the attached PDF for a writeup of this vulnerability.
## Impact
Please see the attached PDF for a writeup of this vulnerability.
---


## Multiple HTTP Smuggling reports
- 等级：Critical | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-7658,
- 原文：https://hackerone.com/reports/648434

- - - - - - - - 
Theses reports spreads other several years and are all about **HTTP Smuggling issues**
(HTTP Requests or Responses splitting, Cache Poisoning, Security filter bypass).
I've made reports on a wide range of open source projects, explaining
the (not always easy) problems to the various security maintainers and testing the fixs.
The starting point for this work was the 2005 work published by Amit Klein and some others:
 * 2004 - Amit Klein : "Divide and Conquer: HTTP Response Splitting, Web Cache Poisoning Attacks, and Related Topics" https://packetstormsecurity.com/papers/general/whitepaper_httpresponse.pdf
 * 2005 - Chaim Linhart, Amit Klein, Ronen Heled, Steve Orrin: "HTTP Re


## HTTP Request Smuggling and SSRF via CRLF Injection in Curl_add_custom_headers
- 等级：High | 项目：curl | 披露：2026-01-02 | CVE：-
- 原文：https://hackerone.com/reports/3484431

- - - - - - - - 
## Summary:
A lack of CRLF validation in `Curl_add_custom_headers` at `lib/http.c:1761` allows users to inject arbitrary HTTP headers. This violation of RFC 7230 §3.2.4 leads to HTTP Request Smuggling and potential SSRF bypass. **AI Disclosure:** I utilized an AI assistant to aid in the initial code analysis and patch generation, but I have manually verified all claims using hex dumps and proxy simulations to ensure technical accuracy.
## Affected version
* **curl/libcurl version:** 8.18.0-DEV and 8.15.0
* **Platform:** Linux (Kali Linux)
* **curl -V output:** `curl 8.18.0-DEV (x86_64-pc-linux-gnu) libcurl/8.18.0-DEV OpenSSL/3.5.4`
## Steps To Reproduce:
1. Start a listener 


## Request Smuggling in Apache Tomcat (Important, CVE-2023-45648)
- 等级：High | 项目：Internet | 披露：2024-02-07 | CVE：CVE-2023-45648
- 原文：https://hackerone.com/reports/2299692

- - - - - - - - 
Apache Tomcat supports Trailer Section. However, we found that in version prior than 11.0.0-M11, 10.1.13, 9.0.80, 8.5.93, Apache Tomcat cannot properly parse the trailer section if there's no colon in the trailer header's line. It will skip the following lines until the last line with a valid colon-separated key-value header pair, which can be leveraged to perform HTTP request smuggling.
If we send the following payload, the headers of the second request **(Line 12-15)** will be regarded as the trailer section of the first request, while the content of the second request **(Line 17-19)** is processed as the second request. When sending this payload to other HTTP implementati


## CVE-2024-21733 Apache Tomcat HTTP Request Smuggling (Client- Side Desync) (CWE: 444)
- 等级：High | 项目：Internet | 披露：2024-01-29 | CVE：CVE-2024-21733
- 原文：https://hackerone.com/reports/2327341

- - - - - - - - 
Apache Tomcat from 8.5.7 through 8.5.63, from 9.0.0-M11 through 9.0.43 are vulnerable to client-side de-sync attacks. 
Client-side de-sync (CSD) vulnerabilities occur when a web server fails to correctly process the Content-Length of POST requests. By exploiting this behavior, an attacker can force a victim's browser to de-synchronize its connection with the website, causing sensitive data to be smuggled from the server and/or client connections.
Users are recommended to upgrade to version 8.5.64 onwards or 9.0.44 onwards, which contain a fix for the issue.
PoC:
~~~~~~~~~~~~~~~~~~
POST / HTTP/1.1
Host: hostname
Sec-Ch-Ua: "Chromium";v="119", "Not?A_Brand";v="24"
Sec-Ch-Ua-Mo


## Possibility of Request smuggling attack
- 等级：High | 项目：Internet | 披露：2023-12-22 | CVE：-
- 原文：https://hackerone.com/reports/2280391

- - - - - - - - 
Request smuggling was possible by throwing an IOException with the upper size limit of the trailer header.
Confirmed with tomcat version 9.0.82.
* example
~~~~~~~~~~~~~~~~~~
POST /examples/test.jsp HTTP/1.1
Host: www.example.co.jp
Content-Type: application/x-www-form-urlencoded
Transfer-Encoding: chunked
Connection: KeepAlive
5
foo=b
2
ar
0
testtrailer: aaaaa...(large size)
a: GET /examples/?this_is_attack HTTP/1.1
Host: attack
~~~~~~~~~~~~~~~~~~
* Reproduce with the following steps:
[code omitted]
The result of curl is two HTTP responses("/examples/test.jsp" and "/examples/?this_is_attack").
Two requests are recorded in the Tomcat access log.
[code omitted]
## Impact
A trai


## HTTP Request Smuggling (CL.0) leads to mass redirect users to attacker server without user interaction
- 等级：High | 项目：LinkedIn | 披露：2023-09-25 | CVE：-
- 原文：https://hackerone.com/reports/1943608

- - - - - - - - 
- Reporter detected HTTP Request Smuggling on a 3rd party CDN
- Because the issue was with a specific 3rd party CDN, the impact on LinkedIn was limited because we use numerous different CDNs and it didn't affect our main site 
- LinkedIn worked with the specific CDN provider to get this resolved quickly
---


## Pause-based desync in Apache HTTPD
- 等级：High | 项目：Internet | 披露：2022-08-25 | CVE：-
- 原文：https://hackerone.com/reports/1667974

- - - - - - - - 
Apache was vulnerable to a pause-based desync. This vulnerability is described in detail in my whitepaper here: https://portswigger.net/research/browser-powered-desync-attacks#pause
## Impact
This enables server-side HTTP Request Smuggling when Apache is deployed as a back-end server, and it also enables MITM attackers to inject arbitrary JavaScript in spite of TLS.
important: HTTP request smuggling vulnerability in Apache HTTP Server 2.4.52 and earlier (CVE-2022-22720)
Apache HTTP Server 2.4.52 and earlier fails to close inbound connection when errors are encountered discarding the request body, exposing the server to HTTP Request Smuggling
Acknowledgements: James Kettle <j


## HTTP Request Smuggling
- 等级：High | 项目：U.S. | 披露：2021-04-20 | CVE：-
- 原文：https://hackerone.com/reports/1120982

- - - - - - - - 
hello dear support 
I have found HTTP Request Smuggling on www.████████
Issue description
==============
HTTP request smuggling vulnerabilities arise when websites route HTTP requests through webservers with inconsistent HTTP parsing.
By supplying a request that gets interpreted as being different lengths by different servers, an attacker can poison the back-end TCP/TLS socket and prepend arbitrary data to the next request. Depending on the website's functionality, this can be used to bypass front-end security rules, access internal systems, poison web caches, and launch assorted attacks on users who are actively browsing the site.
## Impact
Impact
an attacker can poison the


## http request smuggling in  twitter.com
- 等级：High | 项目：X | 披露：2020-11-18 | CVE：-
- 原文：https://hackerone.com/reports/715996

- - - - - - - - 
**Summary:**
the same vulnerability reported in other domain , see this report [here](https://hackerone.com/reports/713285) 
**Description:** 
the Description of HTTP request smuggling attacks : [here](https://portswigger.net/web-security/request-smuggling)
##Detect HTTP request smuggling attack (subdomains vulnerable):
-to detect HTTP request smuggling attack with add header `Transfer-Encoding: chunked` 
and encode the body of request with chunked encode.
1. send request with a valid chunked encode and you will get response means that the **back-end server accept chunked encode**
2. send a large value in hex of chunked encode , if get ** delay of response**  means its vulne


## HTTP Request Smuggling due to CR-to-Hyphen conversion
- 等级：High | 项目：Node.js | 披露：2020-10-17 | CVE：CVE-2020-8201
- 原文：https://hackerone.com/reports/922597

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
**Summary:** [add summary of the vulnerability]
Apparently, node.js converts CR in HTTP request headers to hyphen before parsing. This can lead to HTTP Request Smuggling as it is a non-standard interpretation of the header.
**Description:** [add more details about this vulnerability]
Consider an HTTP request with Content[CR]Length header . Suppose a proxy in front of node.js ignores the Content[CR]Length header (and


## http request smuggling in pscp.tv and periscope.tv
- 等级：High | 项目：X | 披露：2020-09-10 | CVE：-
- 原文：https://hackerone.com/reports/713285

- - - - - - - - 
**Description:** 
the Description of HTTP request smuggling attacks : [here](https://portswigger.net/web-security/request-smuggling)
seems that many subdomains in pscp.tv and periscope.tv vulenrable
##1-Detect HTTP request smuggling attack [504 response with delay (30 s, 60s)] "DoS"
POC & Steps To Reproduce: in this video F606648
Resource: [https://portswigger.net/web-security/request-smuggling/finding] 
##2- [exploit HTTP request smuggling attack ] send two request as one request get two response as one response [low impact]
POC & Steps To Reproduce & impact : in this video F606663
**ps:**
-add the two CRLFs in the end of the second request in GET REQUEST.
-use the valid va


## HTTP request Smuggling
- 等级：High | 项目：Helium | 披露：2020-07-02 | CVE：-
- 原文：https://hackerone.com/reports/867952

- - - - - - - - 
When malformed or abnormal HTTP requests are interpreted by one or more entities in the data flow between the user and the web server, such as a proxy or firewall, they can be interpreted inconsistently, allowing the attacker to "smuggle" a request to one device without the other device being aware of it. 
console.helium.com s vulnerable to CL TE ( Front end server uses Content-Length , Back-end Server uses Transfer-encoding ) HTTP request smuggling attack.
##Products affected:
Helium console Website. :  console.helium.com
##Steps To Reproduce:
1. Run the burp suite turbo intruder on the following request
[code omitted]
2. Script for tubro Intruder is attached. Word list can


## HTTP Request Smuggling
- 等级：High | 项目：Brave | 披露：2020-06-04 | CVE：-
- 原文：https://hackerone.com/reports/866382

- - - - - - - - 
When malformed or abnormal HTTP requests are interpreted by one or more entities in the data flow between the user and the web server, such as a proxy or firewall, they can be interpreted inconsistently, allowing the attacker to "smuggle" a request to one device without the other device being aware of it. 
 publishers.basicattentiontoken.org is vulnerable to CL TE ( Front end server uses Content-Length , Back-end Server uses Transfer-encoding ) HTTP request smuggling attack.
## Products affected: 
Brave Website. : publishers.basicattentiontoken.org
## Steps To Reproduce:
1.  Run the burp suite turbo intruder on the following request
[code omitted]
2. Script for tubro Intrude


## Request smuggling on admin-official.line.me could lead to account takeover
- 等级：High | 项目：LY | 披露：2020-05-19 | CVE：-
- 原文：https://hackerone.com/reports/740037

- - - - - - - - 
The reporter identified a request smuggling issue on admin-official.line.me [(TE.CL-type).](https://portswigger.net/research/http-desync-attacks-request-smuggling-reborn) The reporter clearly illustrated the impact without putting our users at risk or affecting the stability of our service. For this we would like to thank @shaolin_tw!
This issue was the result of how our load balancers were forwarding requests to the backend services. It had widespread influence and the report allowed us to resolve the issue internally, as well as make the vendor of the load balancers aware of this possible issue when using their product. The contents of the report allowed us to identify and


## HTTP Request Smuggling on https://labs.data.gov
- 等级：High | 项目：GSA | 披露：2020-05-13 | CVE：-
- 原文：https://hackerone.com/reports/726773

- - - - - - - - 
Greetings,
The application appears to be vulnerable to HTTP request smuggling due to a disagreement between the front-end and back-end server, where the front-end server uses the Transfer-Encoding header to determine content in the HTTP body, but back-end server uses the Content-Length header, which causes a desync. The following steps outline how to reproduce this vulnerability:
The purpose of the following Turbo Intruder script is to send a desync request followed by 14 requests in quick succession to increase the chances of catching the desync-ed request such that it would not poison the request of another user who happens to be browsing the page.
[code omitted]
The follo


## Request smuggling on ████████
- 等级：High | 项目：U.S. | 披露：2019-10-08 | CVE：-
- 原文：https://hackerone.com/reports/526880

- - - - - - - - 
**Summary:**
**Description:**
The sites at █████████ and ww.██████████ are vulnerable to backend socket poisoning which enables attackers to hijack responses to other users.
This vulnerability occurs because the backend server regards` \n` as a valid header ending, whereas the backend only thinks `\r\n` is valid. This means it's possible to send requests that are interpreted differently by the two servers, leading to backend socket poisoning.
## Impact
Unauthenticated, remote attackers can randomly redirect active users to malicious websites, with no user-interaction required.
## Step-by-step Reproduction Instructions
To replicate this with minimal risk of affecting legitima


## Bypass for #488147 enables stored XSS on https://paypal.com/signin again
- 等级：High | 项目：PayPal | 披露：2019-08-07 | CVE：-
- 原文：https://hackerone.com/reports/510152

- - - - - - - - 
Due to a configuration in frontend, caching servers, it was possible for a researcher to use request smuggling to convert a page request into a cached redirect. If the cached redirect were accessed by a legitimate user, an attacker's content would be rendered instead of the requested page. While this would not impact any back-end data, this could interfere with the integrity of certain pages, including potential interference with the sign-in page. PayPal worked with the researcher and our technical teams to remediate the issue and confirm there was no evidence of real-world attacks.
**Summary (researcher):**
I've posted a full writeup over at https://portswigger.net/blog/htt


## Stored XSS on https://paypal.com/signin via cache poisoning
- 等级：High | 项目：PayPal | 披露：2019-08-07 | CVE：-
- 原文：https://hackerone.com/reports/488147

- - - - - - - - 
Due to a configuration in frontend, caching servers, it was possible for a researcher to use request smuggling to convert a page request into a cached redirect. If the cached redirect were accessed by a legitimate user, an attacker's content would be rendered instead of the requested page. While this would not impact any back-end data, this could interfere with the integrity of certain pages, including potential interference with the sign-in page. PayPal worked with the researcher and our technical teams to remediate the issue and confirm there was no evidence of real-world attacks.
**Summary (researcher):**
I've posted a full writeup over at https://portswigger.net/blog/htt


## Hackerone1
- 等级：High | 项目：RATELIMITED | 披露：2018-12-21 | CVE：-
- 原文：https://hackerone.com/reports/471087

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
**Summary:** [add summary of the vulnerability]
**Description:** [add more details about this vulnerability]
## Steps To Reproduce:
(Add details for how we can reproduce the issue)
  1. [add step]
  1. [add step]
  1. [add step]
## Supporting Material/References:
  * List any additional material (e.g. screenshots, logs, etc.)
## Impact
Kkx
---

