# HackerOne 实战案例：uncontrolled-resource-consumption

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Critical Deadlock Vulnerability in Monero RPC Leading to Complete Node Paralysis
- 等级：Critical | 项目：Monero | 披露：2026-05-06 | CVE：-
- 原文：https://hackerone.com/reports/3307874

- - - - - - - - 
## Summary:
A deadlock vulnerability in Monero's JSON-RPC interface allows a remote, unauthenticated attacker to completely paralyze any Monero node with a single HTTP request containing specific batch methods, leading to permanent denial of service.
## Releases Affected:
- Monero 'Fluorine Fermi' (v0.18.4.2-2987b7200)
- Likely all previous versions
- All operating systems (Linux, Windows, macOS)
- All run modes (mainnet, testnet, offline, restricted-rpc)
Severity:
CVSS 3.0: 10.0 – Critical:
- CVSS:3.0/AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H
Rationale:
- Remote, network-based attack
- No privileges required
- Immediate node paralysis
Affects availability, integrity, and potentia


## WordPress application vulnerable to DoS attack via wp-cron.php
- 等级：Critical | 项目：U.S. | 披露：2023-04-14 | CVE：-
- 原文：https://hackerone.com/reports/1888723

- - - - - - - - 
**Description:**
Hi team,
The WordPress application is vulnerable to a Denial of Service (DoS) attack via the wp-cron.php script. This script is used by WordPress to perform scheduled tasks, such as publishing scheduled posts, checking for updates, and running plugins.
An attacker can exploit this vulnerability by sending a large number of requests to the wp-cron.php script, causing it to consume excessive resources and overload the server. This can lead to the application becoming unresponsive or crashing, potentially causing data loss and downtime.
I found this vulnerability at https://████████ endpoint.
## References
https://developer.wordpress.org/plugins/cron/
## Impact


## DoS at █████(CVE-2018-6389)
- 等级：Critical | 项目：U.S. | 披露：2023-03-24 | CVE：CVE-2018-6389
- 原文：https://hackerone.com/reports/1887996

- - - - - - - - 
**Description:**
Unauthenticated attackers can cause a denial of service (resource consumption) listing a large number of registered .js files (from wp-includes/script-loader.php)
Vulnerable Url : https://██████████/wp-admin/load-scripts.php?load=eutil,common,wp-a11y,sack,quicktag,colorpicker,editor,wp-fullscreen-stu,wp-ajax-response,wp-api-request,wp-pointer,autosave,heartbeat,wp-auth-check,wp-lists,prototype,scriptaculous-root,scriptaculous-builder,scriptaculous-dragdrop,scriptaculous-effects,scriptaculous-slider,scriptaculous-sound,scriptaculous-controls,scriptaculous,cropper,jquery,jquery-core,jquery-migrate,jquery-ui-core,jquery-effects-core,jquery-effects-blind,jquery-


## DoS at ████████ (CVE-2018-6389)
- 等级：Critical | 项目：U.S. | 披露：2023-02-24 | CVE：CVE-2018-6389
- 原文：https://hackerone.com/reports/1861569

- - - - - - - - 
Hi DoD Team!
##Description
Unauthenticated attackers can cause a denial of service (resource consumption) by using the large list of registered .js files (from wp-includes/script-loader.php) to construct a series of requests to load every file many times.
The vulnerability is registered as [CVE-2018-6389](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2018-6389).
WordPress allows users to load multiple JS files and CSS files through load-scripts.php files at once. However, the number and size of files are not restricted in the process of loading JS files, attackers can use this function to deplete server resources and launch denial of service attacks.
##Vulnerability
htt


## HTTP2 'unknownProtocol' cause Denial of Service by resource exhaustion
- 等级：Critical | 项目：Node.js | 披露：2021-03-15 | CVE：CVE-2021-22883
- 原文：https://hackerone.com/reports/1043360

- - - - - - - - 
**Summary:** 
Node.js http2 server is vulnerable against denial of service attacks when too many connection attempts with an 'unknownProtocol' are established. This leads to a leak of file descriptors. If a file descriptor limit is configured on the system, then the server is unable to accept new connections and prevent the process also from opening, e.g. a file. If no file descriptor limit is configured, then this lead to an excessive memory usage and cause the system to run out of memory.
**Description:**
If an attacker can establish an arbitrary amount of connections to the server and achieves that no session is instantiated by sending data causing the `unknownProtocol` e


## xmlrpc.php FILE IS enabled it will used for Bruteforce attack and Denial of Service(DoS)
- 等级：Critical | 项目：BlockDev | 披露：2021-02-12 | CVE：-
- 原文：https://hackerone.com/reports/1086850

- - - - - - - - 
xmlrpc.php file is visible
---


## Mission completed. Grinch Networks is down and Christmas saved.
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1067090

- - - - - - - - 
Hi, I decided to create a good writeup, but for that I'd need some time, that's why I am submitting this pre-report now, and the actual report I ll submit before the deadline in this thread, right under this one.
Here is some proof that Grinch Networks is down:
hackyholidays.h1ctf.com/attack-box/challenge-completed-a3c589ba2709
flag{ba6586b0-e482-41e6-9a68-caf9941b48a0}
Stay tuned!
## Impact
Critical
---


## Hacky Holidays CTF Writeup
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/1066007

- - - - - - - - 
## Intro:
12 days of challenges - some more challenging than others!  This holiday CTF had all 12 challenges hosted on the website https://hackyholidays.h1ctf.com/
{F1129112}
## Challenge 1:
I started by *significantly* overthinking all of the early challenges in this competition.  When this CTF started the home page did not have the "apps" button as seen in the screenshot above, and simply had the "Keep Out" image and the falling snow.
I checked the HTML source and didn't find anything much.  After checking a couple more obvious things, I started looking into the "falling snow" background, which was a `.mp4` file.  Perhaps there was a single frame with the flag in it?  Exam


## Denial of Service by resource exhaustion CWE-400 due to unfinished HTTP/1.1 requests
- 等级：Critical | 项目：Node.js | 披露：2020-10-17 | CVE：CVE-2020-8251
- 原文：https://hackerone.com/reports/868834

- - - - - - - - 
**Summary:** Node.js is vulnerable to HTTP denial of service (DOS) attacks based on delayed requests submission which can make the server unable to accept new connections.
**Description:**
An attacker can open an arbitrary number of HTTP connections and keep the server busy by never completing the request phase.
Node.js only has two requests timeouts:
1. [server.timeout](https://nodejs.org/docs/latest-v12.x/api/http.html#http_server_timeout) that controls the maximum number of milliseconds the socket can be idle. This also includes the server processing time. 
2. [server.headersTimeout](https://nodejs.org/docs/latest-v13.x/api/http.html#http_server_headerstimeout) (Added in 


## Malformed HTTP/2 SETTINGS frame leads to reachable assert
- 等级：Critical | 项目：Node.js | 披露：2020-07-03 | CVE：-
- 原文：https://hackerone.com/reports/800140

- - - - - - - - 
I do not expect any form of cash bounty for this issue. If we have discovered a unique vulnerability I only ask that Jordan Zebor and Adam Cabrey of F5 Networks be crediting with finding the issue.
**Summary:** A reachable assert in the NodeJS HTTP/2 implementation can result in a denial of service. 
**Description:** Attackers can send a series of malformed HTTP/2 SETTINGS frames to reach an assertion in code, causing the node process to exit with SIGABRT. This has been observed in v13.8.0 and v14.0.0-nightly20200213e23b12e130.
## Steps To Reproduce:
1) Create an example HTTP/2 server. I used the example code from here https://nodejs.org/api/http2.html#http2_http2_createsecu


## Prototype pollution in multipart parsing
- 等级：Critical | 项目：Node.js | 披露：2020-02-28 | CVE：CVE-2020-8136
- 原文：https://hackerone.com/reports/804772

- - - - - - - - 
I would like to report a prototype pollution attack in fastify-multipart it allows to crash a remote server parsing multipart requests by sending a specially crafted request.
# Module
**module name:** fastify-multipart
**version:** all versions before < v1.0.5. v1.0.5 contains the fix. 
**npm page:** `https://www.npmjs.com/package/fastify-multipart`
## Module Description
[Fastify](https://www.fastify.io) plugin to parse the multipart content-type.
Under the hood it uses [busboy](http://npm.im/busboy).
## Module Stats
weekly downloads: 4900
# Vulnerability
## Vulnerability Description
Eran Hammer found this vulnerability for Hapi, he tested Fastify as well and found it vulner


## Lodash "difference" (possibly others) Function Denial of Service Through Unvalidated Input
- 等级：Critical | 项目：Node.js | 披露：2019-12-04 | CVE：-
- 原文：https://hackerone.com/reports/670779

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
I would like to report a denial of service in Lodash.
It allows excessive usage of the NodeJS process's memory, leading to a "JavaScript heap out of memory" crash. The same vulnerability exists in the browser version of Lodash and causes Firefox's tab to crash and restart and causes Chrome's tab to completely freeze and become uncloseable (from my testing at least).
# Module
**module name:** Lodash
**version:** Only


## Prototype pollution attack (extend)
- 等级：Critical | 项目：Node.js | 披露：2018-08-22 | CVE：CVE-2018-16492
- 原文：https://hackerone.com/reports/381185

- - - - - - - - 
I would like to report prototype pollution in extend
It allows an attacker to inject properties on Object.prototype.
# Module
**module name:** extend
**version:** 3.0.1
**npm page:** `https://www.npmjs.com/package/extend`
## Module Description
`node-extend` is a port of the classic extend() method from jQuery. It behaves as you expect. It is simple, tried and true.
> **Note**: The github project is called `node-extend` but the NPM package is just `extend`
## Module Stats
7M downloads in the last week
# Vulnerability
## Vulnerability Description
This is a variant of this vulnerability:
https://hackerone.com/reports/310443
The `extend` function can be tricked into adding or mo


## `memjs` allocates and stores buffers on typed input, resulting in DoS and uninitialized memory usage
- 等级：Critical | 项目：Node.js | 披露：2018-06-27 | CVE：CVE-2018-3767
- 原文：https://hackerone.com/reports/319809

- - - - - - - - 
I would like to report a Buffer allocation vulnerability in `memjs`.
In cases when the attacker is able to pass typed input (e.g. via JSON) to the storage, it allows to cause DoS (on all Node.js versions) and to store (and potentially later extract) chunks of uninitialized server memory containing sensitive data.
# Module
**module name:** `memjs`
**version:** 1.1.0
**npm page:** `https://www.npmjs.com/package/memjs`
## Module Description
> MemJS is a pure Node.js client library for using memcache, in particular, the MemCachier service. It uses the binary protocol and support SASL authentication.
## Module Stats
186 downloads in the last day
2 903 downloads in the last week
1


## Fastify denial-of-service vulnerability with large JSON payloads
- 等级：Critical | 项目：Node.js | 披露：2018-01-25 | CVE：CVE-2018-3711
- 原文：https://hackerone.com/reports/303632

- - - - - - - - 
**Module:**
Fastify - https://www.npmjs.com/package/fastify
Affected versions: <=0.37.0 (all version before 0.38.0)
**Summary:**
A denial-of-service attack can be performed against servers running Fastify by sending a request with "Content-Type: application/json" and a very large payload.
**Description:**
Fastify internally builds up the request payload as a string and then JSON parses the string once the full payload is received. It does not (before v0.38.0) limit the size of the payload before JSON parsing it, meaning that the string can grow large enough to surpass either V8's string length limits and throw an `uncaughtException`, or it can surpass the process's memory li


## DoS: type confusion in mrb_no_method_error
- 等级：Critical | 项目：shopify-scripts | 披露：2017-03-01 | CVE：-
- 原文：https://hackerone.com/reports/181871

- - - - - - - - 
Overwriting the 'new' method of the NoMethodError singleton to not return an exception object leads to memory corruption and possibly arbitrary code execution.
Running the following code under the mruny-engine sandbox script results in a native crash:
    NoMethodError.define_singleton_method(:new) do "waat" end
    Object.q
Attached is a patch to mitigate the issue.
---


## Type confusion in mrb_exc_set leading to memory corruption
- 等级：Critical | 项目：shopify-scripts | 披露：2016-12-16 | CVE：-
- 原文：https://hackerone.com/reports/185041

- - - - - - - - 
Similar to #181871, but the bug is more general. The E_*_ERROR macros are not constants, so the exception types can be redefined to not be exceptions:
    #define E_NOTIMP_ERROR              (mrb_class_get(mrb, "NotImplementedError"))
This means that any code calling mrb_raise on an exception macro can instead get a non-exception object, leading to memory corruption and arbitrary code execution. This snippet causes a native crash in mruby-engine:
    NotImplementedError = String
    Module.constants # mrb_raise(mrb, E_NOTIMP_ERROR, "Module.constants not implemented");
This should be fixed by making mrb_exc_set check that it is an exception type. Attached is a patch to mruby 


## Denial of Service via `__proto__` header name in `req.headersDistinct` (Uncaught `TypeError` crashes Node.js process)
- 等级：High | 项目：Node.js | 披露：2026-03-30 | CVE：CVE-2026-21710
- 原文：https://hackerone.com/reports/3560402

- - - - - - - - 
A flaw in Node.js HTTP request handling causes an uncaught `TypeError` when a request is received with a header named `__proto__` and the application accesses `req.headersDistinct`.
When this occurs, `dest["__proto__"]` resolves to `Object.prototype` rather than `undefined`, causing `.push()` to be called on a non-array. This exception is thrown synchronously inside a property getter and cannot be intercepted by `error` event listeners, meaning it cannot be handled without wrapping every `req.headersDistinct` access in a `try/catch`.
* This vulnerability affects all Node.js HTTP servers on **20.x, 22.x, 24.x, and v25.x**
---


## Economic DoS (Griefing) on IBC Relayers via `memo` Callback Gas Exploitation
- 等级：High | 项目：Cosmos | 披露：2025-12-18 | CVE：-
- 原文：https://hackerone.com/reports/3425308

- - - - - - - - 
**Summary of Impact**
This vulnerability allows an attacker to bypass the relayer's simulation defense and force permissionless relayers to execute computationally expensive, but 'successful', transactions via the `memo` callback feature.
    
This creates an asymmetric economic attack where the relayer's cost (e.g., ~1,000,000 gas) vastly exceeds their profit leading to financial losses.
    
Relayers will be forced to stop servicing the affected IBC channel to avoid bankruptcy, causing a Denial of Service (DoS) for all applications relying on that channel's callbacks.
    
**Steps to Reproduce**
1.   **Identify the Callback Gas Limit:** An attacker first inspects the chain


## Denial of Service (DoS) vulnerability in dedotdotify() URL path normalization
- 等级：High | 项目：curl | 披露：2025-12-13 | CVE：-
- 原文：https://hackerone.com/reports/3463608

- - - - - - - - 
## Summary
A Denial of Service (DoS) vulnerability exists in the `dedotdotify()` function in `lib/urlapi.c` that can cause excessive CPU consumption due to O(n²) time complexity when processing URLs with malicious path patterns containing many `../` sequences.
## Affected Component
- **Component**: libcurl URL API
- **File**: `lib/urlapi.c`
- **Function**: `dedotdotify()` (lines 794-898)
- **Vulnerable Code**: Lines 857-866
## Vulnerability Details
The `dedotdotify()` function normalizes URL paths by removing `../` and `./` sequences according to RFC 3986 Section 5.2.4. However, the implementation has a quadratic time complexity (O(n²)) vulnerability.


## Application Level DoS - Large Markdown Payload in Reply Section Leading to Resource Exhaustion
- 等级：High | 项目：Discourse | 披露：2025-10-18 | CVE：-
- 原文：https://hackerone.com/reports/3058919

- - - - - - - - 
## Summary:
An application level Denial of Service (DoS) vulnerability was identified in the reply section on https://try.discourse.org
By submitting an excessively large markup payload (~800,000 characters), the server takes 30 seconds to respond before returning an HTTP/2 502 Bad Gateway error. This indicates potential resource exhaustion or backend service failure, which could be exploited to degrade or disrupt website availability.
## Attack Scenario:
If an attacker automates this request using multiple parallel requests (e.g., via Burp Intruder, Python scripts, or a botnet), it can cause severe resource exhaustion.
The backend service will be overwhelmed, leading to wid


## WebSocket Fragmentation DoS on Curl Client
- 等级：High | 项目：curl | 披露：2025-08-19 | CVE：-
- 原文：https://hackerone.com/reports/3303765

- - - - - - - -


## Crafted smart contract can take 8 minutes to execute due to bug in modexp precompile.
- 等级：High | 项目：Rootstock | 披露：2025-06-13 | CVE：-
- 原文：https://hackerone.com/reports/2412583

- - - - - - - - 
## Summary:
A bug in the modexp precompile can cause long stalls.
## Steps To Reproduce:
Tested on Linux x64.
[code omitted]
Output:
[code omitted]
## Impact
Stall the network.
---


## DOS of RSKJ server
- 等级：High | 项目：Rootstock | 披露：2025-06-13 | CVE：-
- 原文：https://hackerone.com/reports/2105808

- - - - - - - - 
Due of closing of report (ID #2102315) I will summarize total reproducible report here
## Summary:
DOS of RSKJ server
## Steps To Reproduce:
  1. download https://github.com/rsksmart/rskj/releases/download/FINGERROOT-5.0.0/rskj-core-5.0.0-FINGERROOT-all.jar
  2. at server side run
[code omitted]
it opens `UDPv6` port `5050`
  3. at client side install python3 and library `pip install pysha3`, download  {F2591198},  modify `HOST` inside and run it against server.
  4.the `UDPServer` is going to process *only* one UDP packet forever and it prevents to process other packages received from different nodes. In a while (some minutes left) the application crashes.
## Supporting Mat


## Remote memory exhaustion in Epee RPC stack under zero Receive Window
- 等级：High | 项目：Monero | 披露：2025-04-23 | CVE：-
- 原文：https://hackerone.com/reports/2912194

- - - - - - - - 
## Summary
Memory exhaustion can be triggered in `http_protocol_handler.inl` and `abstract_tcp_server2.inl` under delayed ACK or zero Receive Window advertisement. This can lead with specific RPC methods to remote crash of nodes through restricted RPC endpoints.
## Releases Affected
Every branches of monero(d).
## Details
If a socket delays ACK packets and let TCP receive window diminish (for example, by not reading the response from the server), responses are kept in epee server send queue up until a memory exhaustion happen. The RPC method used heavily influence the rapidity of the memory exhaustion.
monerod had the following arguments: `--prune-blockchain --sync-pruned-bl


## Unauthenticated WordPress Database Repair DoS
- 等级：High | 项目：WordPress | 披露：2024-10-18 | CVE：-
- 原文：https://hackerone.com/reports/2786591

- - - - - - - - 
## Summary:
The WordPress Database Repair feature, accessible via the `/wp-admin/maint/repair.php` endpoint, is vulnerable due to improper access control and insecure design. When `WP_ALLOW_REPAIR` is set to `true` in the `wp-config.php` file, the repair page becomes publicly accessible without requiring any authentication. This vulnerability arises from two main issues: the absence of authentication for accessing the repair endpoint and the insecure nature of the WordPress repair feature, which lacks any limits or restrictions on access frequency or user verification. Consequently, an attacker can repeatedly trigger resource-intensive database repair operations, overwhelmin


## CVE-2024-34750 Apache Tomcat DoS vulnerability in HTTP/2 connector
- 等级：High | 项目：Internet | 披露：2024-07-05 | CVE：CVE-2024-34750
- 原文：https://hackerone.com/reports/2586226

- - - - - - - - 
Hello IBB team, i would like to submit a report about Apache Tomcat DoS vulnerability that i have reported to the Tomcat team, which was assigned to CVE-2024-34750 and disclosed yesterday.
**Details:**
When processing an HTTP/2 stream, Tomcat did not handle some cases of excessive HTTP headers correctly. This led to a miscounting of active HTTP/2 streams which in turn led to the use of an incorrect infinite timeout which allowed connections to remain open which should have been closed.
**Here is the email thread that i contacted the security team:**
██████████
## Impact
Since HTTP/2 connections are left open indefinitely, depending on configuration the DoS is caused either b


## Assertion failed in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash
- 等级：High | 项目：Internet | 披露：2024-04-29 | CVE：CVE-2024-27983
- 原文：https://hackerone.com/reports/2453328

- - - - - - - - 
An attacker can make the Node.js HTTP/2 server completely unavailable by sending a small amount of HTTP/2 frames packets with a few HTTP/2 frames inside. It is possible to leave some data in nghttp2 memory after reset when headers with HTTP/2 CONTINUATION frame are sent to the server and then a TCP connection is abruptly closed by the client triggering the Http2Session destructor while header frames are still being processed (and stored in memory) causing a race condition.
* Advisory: https://nodejs.org/en/blog/vulnerability/april-2024-security-releases
* HackerOne report: 2319584
## Impact
Server crashes instantly after sending a few HTTP/2 frames.
Assertion failed in node:


## Denial of Service caused by HTTP/2 CONTINUATION Flood
- 等级：High | 项目：Internet | 披露：2024-04-22 | CVE：CVE-2024-24549
- 原文：https://hackerone.com/reports/2334401

- - - - - - - - 
I sent the following report to Apache Tomcat Security Team. They confirmed the report and assigned CVE-2024-24549. I'd like to ask if this is eligible for a bounty.
I'd like to report a DoS vulnerability in Tomcat. I tested 10.1.18 and 11.0 (tomcat:latest and tomcat:11.0 docker images respectively) and it seems that both are vulnerable.
An attacker can send headers using HTTP/2 CONTINUATION frames up to the limit of header bytes, header size and connection overhead so that connection is not dropped by a server (GOAWAY/ENHANCE_YOUR_CALM). Once frames are sent a connection is left intact and a new connection starts. After a few connections like these the server crashes with (j


## "Assertion failed" in node::http2::Http2Session::~Http2Session() leads to HTTP/2 server crash
- 等级：High | 项目：Node.js | 披露：2024-04-08 | CVE：CVE-2024-27983
- 原文：https://hackerone.com/reports/2319584

- - - - - - - - 
**Summary:**
I discovered a vulnerability in Node.js HTTP/2 stack (`http2`) package. An attacker can send a very small amount of TCP packets with a few HTTP/2 frames inside. After a few seconds a Node.js (latest: 21.5.0 and latest LTS: v20.11.0) server crash with the following stack:
[code omitted]
The attack is easy to perform so a permanent Denial of Service is possible. It is also hard to debug from server admins (check Impact section).
**Description:**
The `http2` package has an  assertion in the `Http2Session` destructor which check if current memory usage of nghttp2 library (`current_nghttp2_memory_`) has been reset to 0.
[code omitted]
However it is possible to leave 


## http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks
- 等级：High | 项目：Internet | 披露：2024-03-05 | CVE：CVE-2024-22019
- 原文：https://hackerone.com/reports/2375446

- - - - - - - - 
I'd like to report Node.js vulnerability (CVE-2024-22019) that was recently fixed:
- HackerOne report: https://hackerone.com/reports/2233486
- Release notes: https://nodejs.org/en/blog/vulnerability/february-2024-security-releases
## Impact
This is a major issue because it allows unbounded resource (CPU, network bandwidth) consumption of the standard Node.js http server. The standard methods which could help blocking a malicious requests like timeouts and limiting request body size do not seem to work.
Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks (CVE-2024-22019) - (High)
A vulnerability in Node.js HTTP servers allows an attacker to send


## http: Reading unprocessed HTTP request with unbounded chunk extension allows DoS attacks
- 等级：High | 项目：Node.js | 披露：2024-02-15 | CVE：CVE-2024-22019
- 原文：https://hackerone.com/reports/2233486

- - - - - - - - 
A vulnerability in Node.js HTTP servers allows an attacker to send a specially crafted HTTP request with chunked encoding, leading to resource exhaustion and denial of service (DoS). The server reads an unbounded number of bytes from a single connection, exploiting the lack of limitations on chunk extension bytes. The issue can cause CPU and network bandwidth exhaustion, bypassing standard safeguards like timeouts and body size limits.
---


## ReDoS( Ruby, Time)
- 等级：High | 项目：Internet | 披露：2023-04-26 | CVE：CVE-2023-28756
- 原文：https://hackerone.com/reports/1929567

- - - - - - - - 
I reported at https://hackerone.com/reports/1485501
https://www.ruby-lang.org/en/news/2023/03/30/redos-in-time-cve-2023-28756/
> The Time parser mishandles invalid strings that have specific characters. It causes an increase in execution time for parsing strings to Time objects.
> A ReDoS issue was discovered in the Time gem 0.1.0 and 0.2.1 and Time library of Ruby 2.7.7.
## Impact
ReDoS occurs when `Time.rfc2822` accepts user input.
In `Rack::ConditionalGet`, the header value is parsed by `Time.rfc2822`,  it is possible to attack from the request.
Rails uses `::Rack::ConditionalGet` by default, it can be attacked by a request from the client.
CVE-2023-28756: ReDoS vulnerabi


## DOS via issue preview
- 等级：High | 项目：GitLab | 披露：2022-11-04 | CVE：-
- 原文：https://hackerone.com/reports/1543718

- - - - - - - -


## Deny of service via malicious Content-Type
- 等级：High | 项目：Fastify | 披露：2022-10-10 | CVE：CVE-2022-39288
- 原文：https://hackerone.com/reports/1715536

- - - - - - - - 
## Summary:
I found a way to crash a fastify@4.6.0  server with a single query on a minimal setup. 
The function `ContentTypeParser.getParser()` do not check properly if the requested content-type parser exists.
/lib/contentTypeParser.js:94
[code omitted]
If an attacker send `constructor` or any default Object attribute, the function will return something unexpected instead of a parser, here the function returns `[Function: Object]`.
Then the `parser.fn` function is called.
/lib/contentTypeParser.js:94
[code omitted]
Because `parser.fn` is undefined, the application crashes.
## Steps To Reproduce:
I used the code provided in the [documentation](https://www.fastify.io/docs/la


## Lack of Packet Sanitation in Goflow Results in Multiple DoS Attack Vectors and Bugs
- 等级：High | 项目：Cloudflare | 披露：2022-09-30 | CVE：CVE-2022-2529
- 原文：https://hackerone.com/reports/1636320

- - - - - - - - 
sflow decode package of the [Goflow](https://github.com/cloudflare/goflow) application did not implement sufficient packet sanitisation which could lead to a denial of service attack. Attackers could craft malformed packets causing the process to consume large amounts of memory resulting in a denial of service.
The issue has been fixed by Cloudflare Engineering team in the 3.4.4 Goflow release.
---


## DOS validator nodes of blockchain to block external connections
- 等级：High | 项目：Linux | 披露：2022-09-13 | CVE：CVE-2022-31006
- 原文：https://hackerone.com/reports/1695472

- - - - - - - - 
Attack was documented in the in the github repo: https://github.com/hyperledger/indy-node/security/advisories/GHSA-x996-7qh9-7ff7
# Attack:
The attacker sends 500 read requests to each node and opens a new one when
holding 500 parallel connections. Every user is able to send read requests
since it's a public readable registry so setting up an allowlist like it's
done with the nodes' port for the consensus does not work here. To increase
the efficiency:
the custom read request is increased with more bytes (random header or
json values)
the bandwidth of the sender machine is limited
Requirements on the attacker side:
Indy-VDR: comment out the timeouts. Using another tool to se


## Remote denial of service in HyperLedger Fabric
- 等级：High | 项目：Linux | 披露：2022-09-01 | CVE：CVE-2022-36023
- 原文：https://hackerone.com/reports/1635854

- - - - - - - - 
How to reproduce
1.Bring up the test network.(https://hyperledger-fabric.readthedocs.io/en/latest/test_network.html#bring-up-the-test-network)
2.Run the PoC.
[code omitted]
[code omitted]
3.Crash.
[code omitted]
## Impact
It can easily break down as many peers as the attacker wants.
---


## RPC call crashes node
- 等级：High | 项目：Monero | 披露：2022-08-20 | CVE：-
- 原文：https://hackerone.com/reports/1379707

- - - - - - - - 
## Summary:
Passing a large list of amounts to the `get_output_distribution` call crashes a remote node, after maybe 90 seconds of keeping it busy.
## Releases Affected:
  * Probably all
## Steps To Reproduce:
[code omitted]
Reduce the 900000 number a bit and instead of crashing the daemon, it'll do a denial of service, like 90 seconds per call, making it hard for anyone else to use that call.
## Supporting Material/References:
  * Unnecessary. The attack is  straightforward and compelling.
## Housekeeping
Payment address: ████
## Impact
An attacker can crash any remote node that exposes `get_output_distribution` or tie up availability of that function call. I think that's s


## Remote denial of service in  HyperLedger Fabric
- 等级：High | 项目：Linux | 披露：2022-07-07 | CVE：CVE-2022-31121
- 原文：https://hackerone.com/reports/1604951

- - - - - - - - 
This issue was caused by [a missing check of nil](https://github.com/hyperledger/fabric/pull/3494).
> An orderer to orderer consensus message that contains an empty inner message crashes the node because it attempts to figure out its type and the mere action of determining the type of a nil pointer, causes a panic.
Thank you to Haosheng Wang of OPPO ZIWU Security Lab for this disclosure.
---

