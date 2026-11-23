# HackerOne 实战案例：heap-overflow

_22 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Heap Buffer Overflow in TFTP
- 等级：Critical | 项目：curl | 披露：2025-12-01 | CVE：-
- 原文：https://hackerone.com/reports/3444904

- - - - - - - - 
# Summary:
A heap buffer overflow vulnerability exists in the TFTP implementation of libcurl. The vulnerability is triggered when a malicious TFTP server sends an OACK (Option  acknowledgment) packet with a blksize option that is larger than the default block size (512 bytes). libcurl updates its internal block size variable but fails to reallocate the receive and send buffers (rpacket and spacket). When the application subsequently receives data (in tftp_rx) or sends data (in tftp_tx) using the larger block size, it writes past the end of the allocated buffer, leading to a heap buffer overflow.
# Affected version
**curl 8.18.0-DEV** (based on LIBCURL_VERSION in  include/cur


## CVE-2020-10938-buffer overflow/out-of-bounds write in compress.c:HuffmanDecodeImage()
- 等级：Critical | 项目：Internet | 披露：2021-08-22 | CVE：CVE-2020-10938
- 原文：https://hackerone.com/reports/816637

- - - - - - - - 
Hello,
  
 There is an out-of-bounds write that is likely exploitable while performing Huffman decoding of Fax images.
 The technical details are as follows.
  
 # Type: integer underflow produces out of bounds heap/etc write
 # Platform: 32-bit
 # Details:
  
[code omitted]
 Basic initialization; of specific note are that the variables 'x' and 'count' are signed. On a 64-bit
 platform, assuming GCC or similar, it is 8 bytes in length and of course 4 bytes in length on 32-bit. There
 is nothing inherently restricting this to 32-bit other than practicalities of the file size as there is a
 need to have backing data to trigger the vulnerability. On 64-bit platforms this equate


## Heap overflow in utf32be_mbc_to_code
- 等级：Critical | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-9023
- 原文：https://hackerone.com/reports/476168

- - - - - - - - 
https://bugs.php.net/bug.php?id=77418
Buffer overflow in mbc_to_code functions for UTF32BE, UTF32LE, UTF16BE, and UTF16LE due to incorrect length assumptions of a buffer. Provided a patch that was adapted to check the length of the buffer prior to using it.
## Impact
Memory leakage and/or corruption
---


## PHP mbstring / Oniguruma multiple remote heap/stack corruptions
- 等级：Critical | 项目：Internet | 披露：2019-10-14 | CVE：CVE-2017-9224,
- 原文：https://hackerone.com/reports/237915

- - - - - - - - 
Oniguruma [1] by K. Kosako is a BSD licensed regular expression library that supports a variety of character encodings. The Ruby programming language, in version 1.9, as well as PHP's multi-byte string module (since PHP5), use Oniguruma as their regular expression engine. It is also used in products such as Atom, Take Command Console, Tera Term, TextMate, Sublime Text and SubEthaEdit.
We've identified six remote memory corruption issues in Oniguruma that affect the latest stable release v6.2.0 and the develop branch, they have received upstream patch in the latest stable version v6.3.0; PHP upstream has now included 5 of the patches (CVE-2017-9224, CVE-2017-9226, CVE-2017-92


## Heap Buffer Overflow in libcurl curl_slist_append via Unterminated String
- 等级：High | 项目：curl | 披露：2025-06-30 | CVE：-
- 原文：https://hackerone.com/reports/3229490

- - - - - - - - 
#Summary
A heap buffer overflow vulnerability exists in libcurl's `curl_slist_append()` function in `lib/slist.c:94`. When the function is called with a non-null-terminated string, the internal `strdup()` call triggers `strlen()` to read beyond allocated buffer boundaries, leading to a heap buffer overflow. This vulnerability can be triggered through various libcurl APIs that process user-controlled string data without proper null termination validation.
#Steps to Reproduce (STR/POC):
  1. Allocate a buffer of any size (e.g., 256 bytes)
  2. Fill the buffer completely with non-null bytes (no null terminator)
  3. Call curl_slist_append(NULL, buffer)
  4. The strlen() call wi


## Heap‑based buffer overflow in curl -K <config_file> allows arbitrary write .
- 等级：High | 项目：curl | 披露：2025-04-27 | CVE：-
- 原文：https://hackerone.com/reports/3094406

- - - - - - - - 
## Summary:
  A heap‑based buffer overflow in curl’s config‑file parser (`parseconfig()` --> `getparameter()`) allows an attacker supplying a crafted config file to overwrite internal pointers (via `cleanarg()`), leading to a write‑what‑where primitive and potential remote code execution.
## Affected version
  -curl 8.13.0 (x86_64-pc-linux-gnu) libcurl/8.13.0 OpenSSL/3.0.13 libpsl/0.21.2
    Release-Date: 2025-04-02
  - or any Version after  version 8.13.0 (dev-versions) that include `cleanarg()` and have writable argv support
## Steps To Reproduce:
 - tested on both Ubuntu 24.04.1 [Linux bobo-pc-1701 6.11.0-21-generic #21~24.04.1-Ubuntu ] AND 
                  Kali 6.11.2-


## Buffer Overflow Vulnerability in WebSocket Handling
- 等级：High | 项目：curl | 披露：2024-01-02 | CVE：-
- 原文：https://hackerone.com/reports/2298307

- - - - - - - - 
## Summary:
Hello security team,
Hope you are doing well :)
I would like to report a potential security vulnerability in the WebSocket handling code of the curl library. The issue is related to the usage of the `strcpy` function, which can lead to a buffer overflow if the length of the input is not properly checked. The vulnerable code snippet is located at [this link](https://github.com/curl/curl/blob/e251e858b941e29bb95a6c0d26bb45981a872585/lib/ws.c#L581).
## Steps To Reproduce:
1. Trigger the WebSocket functionality with a crafted request.
2. Provide a base64-encoded nonce value that exceeds the buffer size.
3. Observe that the `strcpy` function is used without proper bou


## CVE-2023-38545: socks5 heap buffer overflow
- 等级：High | 项目：curl | 披露：2023-10-11 | CVE：CVE-2023-38545
- 原文：https://hackerone.com/reports/2187833

- - - - - - - - 
# Summary:
The SOCKS5 state machine can be manipulated by a remote attacker to overflow heap memory if four conditions are met:
1. The request is made via socks5h.
2. The state machine's negotiation buffer is smaller than ~65k.
3. The SOCKS server's "hello" reply is delayed.
4. The attacker sets a final destination hostname larger than the negotiation
buffer.
libcurl is supposed to disable SOCKS5 remote hostname resolution for hostnames larger than 255 but will not due to a state machine bug.
For example tor user running libcurl app with follow location that connects to rogue onion server that replies with payload in `Location:` header which causes crash or worse.
# Walkthro


## Remote kernel heap overflow
- 等级：High | 项目：PlayStation | 披露：2022-05-11 | CVE：CVE-2022-29867
- 原文：https://hackerone.com/reports/1350653

- - - - - - - - 
# Summary
The PlayStation has a kernel PPPoE driver, that originates from NetBSD. This driver has a kernel heap overflow vulnerability, that an attacker can remotely trigger over the LAN, with the ability to control both the contents that are overflown and their sizes.
# Technical Details
## PPPoE Protocol
In short, the PlayStation (PS) will:
 1. Send a PADI packet.
 2. Expect to receive a PADO packet.
 3. Send a PADR packet.
 4. Expect to receive a PADS packet.
## The Vulnerability
I determined that the PS' PPPoE driver originates from NetBSD. In that PPPoE driver, there is a vulnerability in the way PADR packets are allocated:
[code omitted]
The flow is:
 - `pppoe_send_pad


## Read and write beyond bounds in mod_sed
- 等级：High | 项目：Internet | 披露：2022-04-14 | CVE：CVE-2022-23943
- 原文：https://hackerone.com/reports/1511619

- - - - - - - - 
This CVE consists of several bugs in mod_sed, where overflows, truncation, uses after free and a logic error can allow a remote, unauthenticated attacker to read and/or write heap locations beyond bounds. See https://github.com/apache/httpd/commit/943f57b336f264d77e5b780c82ab73daf3d14deb and https://github.com/apache/httpd/commit/e266bd09c313a668d7cca17a8b096d189148be49 for the commits that fixed the bugs. Attached are my reports to the httpd team; email me if you need additional information.
----
1. Use-after-free and truncation/overflows causing read/write beyond bounds:
[code omitted]
----
2. Update to 1, above, using an expansion ratio that is more likely to be commonly 


## Buffer overflow in req_parsebody method in lua_request.c
- 等级：High | 项目：Internet | 披露：2022-01-04 | CVE：CVE-2021-44790
- 原文：https://hackerone.com/reports/1434056

- - - - - - - - 
Software Versions
-------------------
Ubuntu - 18.04 (32-bit)
Apache 2.4.51 (32-bit)
Description
-------------
This bug is present in "req_parsebody" method of modules/lua/lua_request.c file.
Below mentioned lines of code cause this bug.
[code omitted]
Above code does not check whether the result of (end - crlf) is greater than or equal to 8.
So it is possible to make the result of (end - crlf - 8), negative.
Sending this HTTP request causes the result to be -1.
   `curl -v -X POST -H 'content-type: multipart/form-data; boundary=-' --data-binary $'-\r\n\r\naaa-' http://127.0.0.1/test.lua`
Since "vlen" is of type "size_t", -1 will become 4294967295. This is the maximum value 


## Basic Authentication Heap Overflow
- 等级：High | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-12527
- 原文：https://hackerone.com/reports/641240

- - - - - - - - 
## Summary:
An attacker can get arbitrary data overflowed in the heap via Basic Authorization base64 blob. Even when basic auth isn't configured.
## Report sent to developers
When calling HttpHeader::getAuth the field value will be base64 decoded. The call to the decode method doesn't ensure that the buffer decodedAuthToken is large enough for the decoded string leading to a heap overflow. 
[code omitted]
[code omitted]
 In my repo steps I make an FTP request to squid-internal-mgr. Any user can reach this code since the Manager regex doesn't check for FTP protocol. A user can't access any real actions from cache manager though, just are able to reach the part of the code tha


## Heap buffer overflow vulnerability while processing a malformed TIFF file.
- 等级：High | 项目：Internet | 披露：2021-07-09 | CVE：CVE-2020-27829
- 原文：https://hackerone.com/reports/1047086

- - - - - - - - 
A heap buffer overflow vulnerability occurs in magick while processing of a malformed TIFF file.Following is the version/build details:
[code omitted]
Replication details:
1. run following command with attached poc.tif file:
[code omitted]
note: zip file password is infected.
you should see the crash as mentioned below.
Following is the crash details:
[code omitted]
## Impact
can crash the software, may be remote code execution but i haven't checked the exploitability part of it.
---


## libcurl: SMTP end-of-response out-of-bounds read - CVE-2019-3823
- 等级：High | 项目：curl | 披露：2021-01-08 | CVE：CVE-2019-3823
- 原文：https://hackerone.com/reports/518097

- - - - - - - - 
[code omitted]
The issue was reported to the project on 18 January 2019.
A patch was sent to me on 19 January 2019. 
curl 7.64.0 was released on 6 January 2019.
https://curl.haxx.se/docs/CVE-2019-3823.html
## Impact
If the buffer passed to `smtp_endofresp()` isn't NUL terminated and contains no character ending the parsed number, and `len` is set to 5, then the `strtol()` call reads beyond the allocated buffer.
---


## Buffer over-write in finfo_open with malformed magic file.
- 等级：High | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2015-8865
- 原文：https://hackerone.com/reports/476179

- - - - - - - - 
https://bugs.php.net/bug.php?id=71527
This bug causes a segfault when running with environment variable USE_ZEND_ALLOC set to 0, and also when compiled with ASAN with USE_ZEND_ALLOC set and unset.
To reproduce, run the following PHP file, with the example magic file below.
$ cat magic-open.php
<?php
$finfo = finfo_open(FILEINFO_NONE, $argv[1]);
$info = finfo_file($finfo, $argv[2]);
var_dump($info);
?>
Magic file is (used without ASAN):
$ xxd -g 1 magic.crash-noasan
0000000: 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e  >>>>>>>>>>>>>>>>
0000010: 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e 3e     >>>>>>>>>>>>>>>
$ cat magic.crash-noasan
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Magic f


## Out of order TLS handshake / application data messages lead to segmentation fault
- 等级：High | 项目：Node.js | 披露：2020-02-13 | CVE：-
- 原文：https://hackerone.com/reports/335495

- - - - - - - - 
**Summary:** 
IMPORTANT NOTE: I have already been working with the NodeJS core security team on this issue and have provided core files, POC and many other pieces of information. I was told by James Snell to report via Hackerone to make it official however all the relevant details on this issue have already been provided to NodeJS team. This report will be minimal since all details are already with the team which needs them.
**Description:** Sending interleaved handshake messages in the TLS handshake OR sending TLS handshake messages AFTER the handshake has completed (after finished msg) causes a segmentation fault of the NodeJS process. This is present in v9 and v10, using 


## heap-buffer-overflow (read outside of buffer) in Sass::Prelexer::exactly<(char)92>(char const*) - libsass/src/lexer.hpp:92
- 等级：High | 项目：LibSass | 披露：2019-10-05 | CVE：-
- 原文：https://hackerone.com/reports/221163

- - - - - - - - 
Built with afl-clang-fast from git source `5909ba5`.
Feeding a file that contains nothing but `'\` to sassc triggers this flaw.
[code omitted]
---


## Heap overflow happen when receiving short length key from ssh server using ssh protocol 1
- 等级：High | 项目：PuTTY | 披露：2019-09-20 | CVE：-
- 原文：https://hackerone.com/reports/630462

- - - - - - - - 
## Summary:
There's no check in `ssh1_login_process_queue` function when read `servkey` and `hostkey` length from packet which may cause heap overflow. 
Remote code execution may be possible.
## Steps To Reproduce:
  1. To test this issue, I downloaded openssl6.8 to compile to craft packets, using below command to download openssl6.8p1 source code
`# wget https://openbsd.hk/pub/OpenBSD/OpenSSH/portable/openssh-6.8p1.tar.gz`
 
  2. After download openssl6.8p1 source code, patch `ssh-keygen.c` and `sshd.c` according with `ssh-keygen.c.diff` and `sshd.c.diff` attached accordingly.
  3. Compile patched openssl6.8p1 to get `sshd` which used to act as ssh1 server and `ssh-keygen` 


## CVE-2018-6797:  A crafted regular expression can cause a heap buffer write overflow in Perl 5 giving a remote attacker control over bytes written
- 等级：High | 项目：Internet | 披露：2018-05-19 | CVE：CVE-2018-6797
- 原文：https://hackerone.com/reports/337986

- - - - - - - - 
An attacker supplies a regular expression containing one or more `\xDF` characters after an escape putting the regexp into unicode matching mode, such as a `\N{}` escape.  Each `\xDF` character adds one byte of overflow, and any other text in the regular expression is written in order, providing the attacker control over the bytes written to the overflowed region.
* Reported to the [Perl security mailing list](https://rt.perl.org/Ticket/Display.html?id=132227) on 6 Oct 2017.
* Confirmed as a security flaw by TonyC on 31 Jan 2018
* CVE-2018-6797 assigned to this flaw on 6 Feb 2018
* Patch released to the security mailing list for Perl 5.24 and Perl 5.26 on 09 Feb 2018
* Patch


## Heap Overflow in fiber_switch triggered from Fiber.transfer
- 等级：High | 项目：shopify-scripts | 披露：2017-05-30 | CVE：-
- 原文：https://hackerone.com/reports/227762

- - - - - - - - 
It appears as if my recommendations were ignored in the GitHub issue, so I've repeated the issue here.
# PoC
	Fiber.new{}.transfer(
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0,0,0,0,0,0,
		0,0,0,0,0)
# Explanation
The cause of this is that in mrbgems/mruby-fiber/src/fiber.c the stack Fiber stack is initialized lines 90-96 to a default of 64 (FIBER_STACK_INIT_SIZE), however in fiber_switch lines 191-198, if the Fiber's status is currently MRB_FIBER_CREATED, then it will copy the arguments provided from fiber_transfer irregardless of whether or not there are more arguments than 64 (the PoC doesn


## heap-buffer-overflow (read outside of buffer) in mrb_vm_exec()
- 等级：High | 项目：shopify-scripts | 披露：2017-05-09 | CVE：-
- 原文：https://hackerone.com/reports/221251

- - - - - - - - 
Triggered in `3231219` (14 April 2017). Compiled with afl-gcc + asan.
`./mirb < test000`
[code omitted]
---


## Content-Length restriction bypass to heap overflow in gip.rocks.
- 等级：High | 项目：Gratipay | 披露：2017-03-20 | CVE：-
- 原文：https://hackerone.com/reports/214449

- - - - - - - - 
I started playing around with a0xnirudh's [Content-Length restriction bypass](https://hackerone.com/reports/203388) and noticed that when combined with a different vulnerability  this could be leveraged to do a bit more than DoS.
We decided to open a new ticket to address this issue, since [we were already aware of the bypass](https://github.com/gratipay/gip.rocks/issues/2). a0xnirudh wrote such a good report that we decided to not close their report as a `Duplicate`.
# Summary
---
I noticed that `gip.rocks` was using an outdated version (2.9.0) of the Pillow framework which is vulnerable to heap overflows. The test playoad is 788480 bytes. So the bypass allowed me to pass t

