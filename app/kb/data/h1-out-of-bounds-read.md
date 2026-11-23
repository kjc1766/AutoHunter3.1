# HackerOne 实战案例：out-of-bounds-read

_15 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Adam and the  Deadly  Injections
- 等级：Critical | 项目：h1-ctf | 披露：2021-06-18 | CVE：-
- 原文：https://hackerone.com/reports/1217702

- - - - - - - - 
Hi team adding the  flag here 
[code omitted]
████
I will do the writeup in the below comments before the deadline itself
Thanks 
Akshansh
## Impact
....
---


## RCE on CS:GO client using unsanitized entity ID in EntityMsg message
- 等级：Critical | 项目：Valve | 披露：2021-05-27 | CVE：-
- 原文：https://hackerone.com/reports/584603

- - - - - - - - 
Title:         RCE on CS:GO client using unsanitized entity ID in EntityMsg message
Scope:         csgo.exe
Weakness:      Out-of-bounds Read
Severity:      Critical (9.6)
Link:          https://hackerone.com/reports/584603
Date:          2019-05-19 17:49:21 +0000
By:            @chaynik
Details:
Vulnerability
-------------
`CSVCMsg_EntityMsg` message is used by server to notify client about generic actions regarding entities. The message is described using the following Protocol Buffer:
[code omitted]
The pseudocode of function handling this message:
[code omitted]
Neither handler nor `GetClientNetworkable` check if entity index is valid - an arbitrary integer can be passed


## CS:GO Server -> Client RCE through OOB access in CSVCMsg_SplitScreen + Info leak in HTTP download
- 等级：Critical | 项目：Valve | 披露：2021-05-17 | CVE：-
- 原文：https://hackerone.com/reports/1070835

- - - - - - - - 
Title:         CS:GO Server -> Client RCE through OOB access in CSVCMsg_SplitScreen + Info leak in HTTP download
Scope:         csgo.exe
Weakness:      Out-of-bounds Read
Severity:      Critical (9.6)
Link:          https://hackerone.com/reports/1070835
Date:          2021-01-04 00:22:02 +0000
By:            @simonscannell
Details:
We managed to write an extremely reliable exploit for CS:GO on Windows by chaining  an OOB access that leads to RIP control and an Info leak. This report consists of two  critical bugs. The memory leak was initially reported in #1064367, where the other bug  in the same report was a duplicate and the OOB access in #1064809. Altough #1064809 is sti


## OOB reads in network message handlers leads to RCE
- 等级：Critical | 项目：Valve | 披露：2021-05-04 | CVE：-
- 原文：https://hackerone.com/reports/807772

- - - - - - - - 
# Vulnerability
In Source engine games there are many network messages sent from the server to the client that take an entity index. There is a common pattern among many of these messages for the lower bounds of the entity index to be checked but not the upper bounds. In many cases these out of bound reads get an entity pointer from that index then call a virtual function on it.
As an example, here is the handler for the CS:GO [`GlowPropTurnOff`](https://github.com/SteamDatabase/Protobufs/blob/7c7bc10a1ed346a88cc6b9c13d6642578a9ecd50/csgo/cstrike15_usermessages.proto#L444-L446) message:
[code omitted]
# Exploiting the vulnerability
I will be discussing the `GlowPropTurnOff` 


## Tcpdump before 4.9.3 has a buffer over-read in print-dccp.c:dccp_print_option() (CVE-2018-16229)
- 等级：Critical | 项目：Internet | 披露：2020-02-13 | CVE：CVE-2018-16229
- 原文：https://hackerone.com/reports/724253

- - - - - - - - 
Tcpdump before 4.9.3 has a buffer over-read in print-dccp.c:dccp_print_option(). This vulnerability was disclosed to the tpcdump maintainers and was fixed in version 4.9.3 and disclosed as CVE-2018-16229.
I was credited with finding and disclosing this vulnerability: https://www.tcpdump.org/public-cve-list.txt
[code omitted]
This vulnerability was discovered in version 4.9.2 after compiling tcpdump with Address Sanitizer (ASAN) and fuzzing tcpdump with mutated packets. This vulnerability can be remotely exploited over the network by an attacker with no interaction needed from the victim.
I have attached test-case "fuzzer06:id:000018,sig:11,src:007353,op:havoc,rep:16" as a Pr


## Tcpdump before 4.9.3 has a buffer over-read in print-802_11.c (CVE-2018-16227)
- 等级：Critical | 项目：Internet | 披露：2020-02-13 | CVE：CVE-2018-16227
- 原文：https://hackerone.com/reports/724243

- - - - - - - - 
Versions of tcpdump before 4.9.3 are vulnerable to a buffer over-read in print-802_11.c. This vulnerability was disclosed to the tcpdump maintainers and was recently patched in version 4.9.3 and disclosed as (CVE-2018-16227).
I was credited with finding and disclosing this vulnerability: https://www.tcpdump.org/public-cve-list.txt
[code omitted]
This vulnerability was found and tested on tcpdump 4.9.2 after compiling tcpdump with Address Sanitizer (ASAN) support and fuzzing tcpdump with mutated packets, I have attached a working test-case as a Proof of Concept to this report named "fuzzer06:id:000021,sig:11,src:008627,op:havoc,rep:2". 
This vulnerability can be triggered usi


## Heap-buffer-overflow in `Curl_ssl_push_certinfo_len()` — sole bounds check is `DEBUGASSERT`
- 等级：High | 项目：curl | 披露：2026-04-29 | CVE：-
- 原文：https://hackerone.com/reports/3684614

- - - - - - - - 
## Summary
`Curl_ssl_push_certinfo_len()` in `lib/vtls/vtls.c` uses `DEBUGASSERT(certnum < ci->num_of_certs)` as its **only** bounds check before writing a heap pointer into `ci->certinfo[certnum]`. `DEBUGASSERT` is a no-op in every release/production build (`lib/curl_setup.h:1084`). Any mismatch between the count passed to `Curl_ssl_init_certinfo()` and the certnum values subsequently passed to `Curl_ssl_push_certinfo_len()` results in an unguarded heap out-of-bounds read and write.
This function is the single shared certinfo write path for all five TLS backends (OpenSSL, GnuTLS, mbedTLS, Rustls, Schannel). The `certnum` argument in every backend derives directly from the s


## Heap Out-of-Bounds Read in lib/http2.c via Malformed PUSH_PROMISE Headers
- 等级：High | 项目：curl | 披露：2026-01-10 | CVE：-
- 原文：https://hackerone.com/reports/3506159

- - - - - - - - 
Summary
A heap-based out-of-bounds read vulnerability exists in libcurl's HTTP/2 implementation. The on_header callback in lib/http2.c incorrectly treats header names and values provided by nghttp2 as null-terminated C-strings. Specifically, passing these pointers to curl_maprintf with the %s format specifier triggers an out-of-bounds read via strlen(), as nghttp2 provides raw byte buffers with explicit lengths, not null-terminated strings.
+1
Vulnerability Analysis & Root Cause
1. API Contract Violation: According to the nghttp2 documentation, the nghttp2_on_header_callback provides pointers to the header name and value (name, value) alongside their lengths (namelen, valuel


## Heap Buffer Over-Read via Malicious SMB Server READ_ANDX Response
- 等级：High | 项目：curl | 披露：2025-12-20 | CVE：-
- 原文：https://hackerone.com/reports/3470095

- - - - - - - - 
================================================================================
DESCRIPTION:
================================================================================
## Summary:
I discovered a heap buffer over-read vulnerability in libcurl's SMB protocol 
implementation. A malicious SMB server can send a specially crafted READ_ANDX 
response that causes curl to read and output up to 28KB of uninitialized heap 
memory per request. This results in information disclosure to the attacker.
The vulnerability exists in lib/smb.c within the smb_request_state() function,
specifically in the SMB_DOWNLOAD state handler at lines 1110-1137.
No AI was used to discover this vulner


## Out of Bounds Memory Read in exif_scan_thumbnail
- 等级：High | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-11041
- 原文：https://hackerone.com/reports/675578

- - - - - - - - 
I have found and reported an out of bounds memory read in PHP [exif_scan_thumbnail]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11041
The bug report is here: https://bugs.php.net/bug.php?id=78222
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11041
https://nvd.nist.gov/vuln/detail/CVE-2019-11041
## Impact
This may lead to information disclosure or crash.
---


## Out of Bounds Memory Read in exif_process_user_comment
- 等级：High | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-11042
- 原文：https://hackerone.com/reports/675580

- - - - - - - - 
I have found and reported an out of bounds memory read in PHP [exif_process_user_comment]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.31, 7.2.x below 7.2.21 and 7.3.x below 7.3.8 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11042
The bug report is here: https://bugs.php.net/bug.php?id=78256
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11042
https://nvd.nist.gov/vuln/detail/CVE-2019-11042
## Impact
This may lead to information disclosure or crash.
---


## null pointer dereference in imap_mail
- 等级：High | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2018-19935
- 原文：https://hackerone.com/reports/456727

- - - - - - - - 
in imap_mail if message args is null, in _php_imap_mail no check wheater message  can get, so crash.
[code omitted]
/usr/local/php/bin/php ./craxxx.php 
Warning: imap_mail(): No message string in mail command in /home/fan/github/php-7.2.10/myselffuzz/craxxx.php on line 3
sh: 1: -t: not found
Segmentation fault (core dumped)
../sapi/cli/php ./craxxx.php 
Warning: imap_mail(): No message string in mail command in /home/fan/github/php-7.2.10/myselffuzz/craxxx.php on line 3
ASAN:SIGSEGV
=================================================================
==23766==ERROR: AddressSanitizer: SEGV on unknown address 0x000000000018 (pc 0x7fae925d9cc0 bp 0x7ffcb6b27a10 sp 0x7ffcb6b274a0 T


## `base64-url` below 2.0 allocates uninitialized Buffers when number is passed in input
- 等级：High | 项目：Node.js | 披露：2018-05-12 | CVE：-
- 原文：https://hackerone.com/reports/321692

- - - - - - - - 
I would like to report an uninitialized Buffer allocation issue in `base64-url`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed (e.g. from JSON).
# Module
**module name:** `base64-url`
**version:** 1.3.3
**npm page:** `https://www.npmjs.com/package/base64-url`
## Module Description
> Base64 encode, decode, escape and unescape for URL applications.
## Module Stats
48 047 downloads in the last day
311 047 downloads in the last week
1 374 420 downloads in the last month
# Vulnerability
## Vulnerability Description
The problem arises when a number is passed in, e.g. from


## `npmconf` (and `npm` js api) allocate and write to disk uninitialized memory content when a typed number is passed as input on Node.js 4.x
- 等级：High | 项目：Node.js | 披露：2018-05-12 | CVE：-
- 原文：https://hackerone.com/reports/320269

- - - - - - - - 
I would like to report a Buffer allocation issue in `npmconf` (and `npm` package js api).
It allows to extract sensitive content from uninitialized memory by passing typed input to `setCredentialsByURI`, limited to Node.js 4.x and below.
# Module
**module name:** `npmconf`
**version:** 2.1.2
**npm page:** `https://www.npmjs.com/package/npmconf`
**module name:** `npm`
**version:** 5.6.0
**npm page:** `https://www.npmjs.com/package/npm`
## Module Description
> The config thing npm uses
## Module Stats


## `base64url` allocates uninitialized Buffers when number is passed in input on Node.js 4.x and below
- 等级：High | 项目：Node.js | 披露：2018-05-11 | CVE：-
- 原文：https://hackerone.com/reports/321687

- - - - - - - - 
I would like to report an uninitialized Buffer allocation issue in `base64url`.
It allows to extract sensitive data from uninitialized memory or to cause a DoS by passing in a large number, in setups where typed user input can be passed (e.g. from JSON), on Node.js 4.x and lower.
# Module
**module name:** `base64url`
**version:** 2.0.0
**npm page:** `https://www.npmjs.com/package/base64url`
## Module Description
> Converting to, and from, base64url
## Module Stats
182 924 downloads in the last day
1 097 142 downloads in the last week
4 601 176 downloads in the last month
# Vulnerability
## Vulnerability Description
The problem arises when a number is passed in, e.g. from use

