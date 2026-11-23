# HackerOne 实战案例：buffer-over-read

_25 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## h1 hacky holidays CTF solution
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1065517

- - - - - - - - 
Simple script to print all the flags. Full solution to follow (want to spend more time writing this, but am racing to be first 10 submissions):
[code omitted]
output:
[code omitted]
## Impact
critical, we must stop the Grinch!
---


## Out of Bounds Memory Read in php_jpg_get16
- 等级：Critical | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-11040
- 原文：https://hackerone.com/reports/665330

- - - - - - - - 
I have found and reported an out of bounds memory read in PHP [php_jpg_get16]
When PHP EXIF extension is parsing EXIF information from an image, e.g. via exif_read_data() function, in PHP versions 7.1.x below 7.1.30, 7.2.x below 7.2.19 and 7.3.x below 7.3.6 it is possible to supply it with data what will cause it to read past the allocated buffer.
This has been fixed and assigned CVE-2019-11040
The bug report is here: https://bugs.php.net/bug.php?id=77988
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-11040
https://nvd.nist.gov/vuln/detail/CVE-2019-11040
## Impact
This may lead to information disclosure or crash.
---


## heap buffer overflow in phar_detect_phar_fname_ext
- 等级：Critical | 项目：Internet | 披露：2020-10-10 | CVE：CVE-2019-9021
- 原文：https://hackerone.com/reports/475499

- - - - - - - - 
The original report is here  https://bugs.php.net/bug.php?id=77247
[code omitted]
[code omitted]
## Impact
Heap buffer over read
---


## Heap Buffer Over-read in lib/http2.c (on_header) handling PUSH_PROMISE frames
- 等级：High | 项目：curl | 披露：2025-12-28 | CVE：-
- 原文：https://hackerone.com/reports/3480078

- - - - - - - - 
## Summary:
I have discovered a Heap Buffer Over-read vulnerability in `lib/http2.c` within the `on_header` callback function. When processing HTTP/2 `PUSH_PROMISE` frames, the code incorrectly uses the `%s` format specifier on raw pointers provided by `nghttp2`.
According to `nghttp2` documentation, the `name` and `value` pointers in the `on_header` callback are **not null-terminated**. By using `%s` without precision specifiers, `curl_maprintf` reads past the bounds of the allocated buffer into adjacent heap memory until it encounters a null byte. This leads to a Denial of Service (crash via OOM or invalid read) or potentially leaks sensitive heap memory.
## Vulnerability 


## Out-of-bounds read in HTTP method handling causes undefined behavior and potential crash This is sharp, Gaurav. We’ve got a real memory-safety bug ins
- 等级：High | 项目：curl | 披露：2025-11-20 | CVE：-
- 原文：https://hackerone.com/reports/3434510

- - - - - - - - 
Summary
-​‍​‌‍​‍‌​‍​‌‍​‍‌ Component: libcurl core HTTP handling (HTTP/2 request translation and CONNECT detection)
- Type: out-of-bounds read resulting from missing null-termination
- Impact: Behavior not defined by the specification, the program can crash (DoS) and CONNECT requests can be misclassified
- Root cause: The method string was copied without a null ​‍​‌‍​‍‌​‍​‌‍​‍‌termin
Affected​‍​‌‍​‍‌​‍​‌‍​‍‌ code paths
- Struct layout:
- struct httpreq { ... char method[1]; }
- Allocation and copy (no NUL):
- req = calloc(1, sizeof(*req) + m_len);
- memcpy(req->method, method, m_len);
- Unsafe uses:
- strcmp("CONNECT", req->method) — assumes null-terminated string
- strlen(re


## Heap Buffer Overflow in Curl_memdup0() via CURLOPT_COPYPOSTFIELDS/CURLOPT_POSTFIELDSIZE Mismatch
- 等级：High | 项目：curl | 披露：2025-08-09 | CVE：-
- 原文：https://hackerone.com/reports/3292590

- - - - - - - - 
## Summary
A heap buffer overflow vulnerability exists in libcurl's `Curl_memdup0()` function when handling `CURLOPT_COPYPOSTFIELDS` operations. The vulnerability occurs when libcurl internally processes POST data where the specified `CURLOPT_POSTFIELDSIZE` exceeds the actual buffer size of data set via `CURLOPT_COPYPOSTFIELDS`. This is a legitimate use case that libcurl should handle safely, but currently results in out-of-bounds memory access.
## POC


## Squid leaks previous content from reusable buffer
- 等级：High | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-12528
- 原文：https://hackerone.com/reports/824163

- - - - - - - - 
## Summary:
A malicious response to a FTP request can cause Squid to miscalculate the length of a string copying data past the terminating NULL. Due to Squid's memory pool the contents that is exposed could range from internal data, to other user's private Request/Response to Squid. 
This exist in Squid-4.9 and Below and was fixed in Squid-4.10
This vulnerability was assigned CVE-2019-12528.
## Steps To Reproduce:
A custom config is should not be needed. 
I've attached a python script that returns the needed response to trigger this.
1) Start Squid 
[code omitted]
2) Start your malicious FTP Server
[code omitted]
3) Make a request to the FTP server via Squid.
[code omitted]



## The VTP parser in tcpdump before 4.9.2 has a buffer over-read in print-vtp.c:vtp_print()
- 等级：High | 项目：Internet | 披露：2021-08-22 | CVE：CVE-2017-13033
- 原文：https://hackerone.com/reports/802846

- - - - - - - - 
Hello,
The vulnerable code portion is linked below. The linked function is responsible for printing VTP packet payload information to the terminal (e.g., stdout)
https://github.com/the-tcpdump-group/tcpdump/commit/ae83295915d08a854de27a88efac5dd7353e6d3f#diff-8c6895b252e6da31d60a7866973d5787L262-L268
The issue may be reproduced as follows
Check out vulnerable tcpdump commit (< 4.9.2) as follows
[code omitted]
Run tcpdump against linked payload (link: https://github.com/the-tcpdump-group/tcpdump/blob/ae83295915d08a854de27a88efac5dd7353e6d3f/tests/vtp_asan-3.pcap?raw=true)
[code omitted]
It is acknowledged here(link: https://github.com/the-tcpdump-group/tcpdump/commit/ae832959


## CVE-2017-13050: The RPKI-Router parser in tcpdump before 4.9.2 has a buffer over-read in print-rpki-rtr.c:rpki_rtr_pdu_print()
- 等级：High | 项目：Internet | 披露：2021-08-22 | CVE：CVE-2017-13050
- 原文：https://hackerone.com/reports/802863

- - - - - - - - 
Hello,
The vulnerable code portion is linked below. The linked function is responsible for printing RPKI-Router packet payload information to the terminal (e.g., stdout)
https://github.com/the-tcpdump-group/tcpdump/commit/83c64fce3a5226b080e535f5131a8a318f30e79b
The issue may be reproduced as follows
Check out vulnerable tcpdump commit (< 4.9.2) as follows
[code omitted]
Build it with afl and AddressSanitizer as follows (please install libpcap before this step)
[code omitted]
Run tcpdump against linked payload (link: https://github.com/the-tcpdump-group/tcpdump/blob/83c64fce3a5226b080e535f5131a8a318f30e79b/tests/rpki-rtr-oob.pcap?raw=true)
[code omitted]
It is acknowledged h


## CVE-2017-13019:  The PGM parser in tcpdump before 4.9.2 has a buffer over-read in print-pgm.c:pgm_print()
- 等级：High | 项目：Internet | 披露：2021-08-22 | CVE：CVE-2017-13019
- 原文：https://hackerone.com/reports/802896

- - - - - - - - 
Hello,
The vulnerable code portion is linked below. The linked function is responsible for printing PGM packet payload information to the terminal (e.g., stdout)
https://github.com/the-tcpdump-group/tcpdump/commit/4601c685e7fd19c3724d5e499c69b8d3ec49933e
The issue may be reproduced as follows
Check out vulnerable tcpdump commit (< 4.9.2) as follows
[code omitted]
Build it with afl and AddressSanitizer as follows (please install libpcap before this step)
[code omitted]
Run tcpdump against linked payload (link: https://github.com/the-tcpdump-group/tcpdump/blob/4601c685e7fd19c3724d5e499c69b8d3ec49933e/tests/pgm_opts_asan_2.pcap?raw=true)
[code omitted]
It is acknowledged here(l


## CVE-2020-9383 Floppy OOB read
- 等级：High | 项目：Internet | 披露：2021-08-22 | CVE：CVE-2020-9383
- 原文：https://hackerone.com/reports/891846

- - - - - - - - 
A vulnerability was found in Linux Kernel up to 5.5.6 (Operating System) and classified as critical. Affected by this issue is the function `set_fdc` of the file `drivers/block/floppy.c`. The manipulation with an unknown input leads to a memory corruption vulnerability (Out-of-Bounds). Using CWE to declare the problem leads to CWE-125. Impacted is confidentiality, integrity, and availability.
The weakness was disclosed 02/25/2020 by Jordy Zomer (GitHub Repository). The advisory is shared for download at github.com. This vulnerability is handled as CVE-2020-9383 since 02/24/2020. The attack needs to be approached locally. 
References:
http://lists.opensuse.org/opensuse-securi


## CVE-2017-13040 The MPTCP parser in tcpdump before 4.9.2 has a buffer over-read in print-mptcp.c, several functions.
- 等级：High | 项目：Internet | 披露：2021-07-09 | CVE：CVE-2017-13040
- 原文：https://hackerone.com/reports/964582

- - - - - - - - 
## Description:
Versions of tcpdump before 4.9.2 are vulnerable to a buffer over-read in print-mptcp.c. This vulnerability was disclosed to the tcpdump maintainers and was recently patched in version 4.9.2 and disclosed as (CVE-2017-13040).
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/4c3aee4bb0294c232d56b6d34e9eeb74f630fe8c
This vulnerability can be exploited in two ways. The first is to produce a .pcap file with crafted packet(s) for the protocol(s) concerned and make the target system try to decode the file using tcpdump. The second is to send specially crafted packet(s) to the network segment where the target system is running a tcpdump process that is deco


## CVE-2017-13041 The ICMPv6 parser in tcpdump before 4.9.2 has a buffer over-read in print-icmp6.c:icmp6_nodeinfo_print().
- 等级：High | 项目：Internet | 披露：2021-07-09 | CVE：CVE-2017-13041
- 原文：https://hackerone.com/reports/964583

- - - - - - - - 
## Description:
Versions of tcpdump before 4.9.2 are vulnerable to a buffer over-read in print-icmp6.c. This vulnerability was disclosed to the tcpdump maintainers and was recently patched in version 4.9.2 and disclosed as (CVE-2017-13041).
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/f4b9e24c7384d882a7f434cc7413925bf871d63e
This vulnerability can be exploited in two ways. The first is to produce a .pcap file with crafted packet(s) for the protocol(s) concerned and make the target system try to decode the file using tcpdump. The second is to send specially crafted packet(s) to the network segment where the target system is running a tcpdump process that is deco


## Out-of-bounds read in iconv.c:_php_iconv_mime_decode() due to integer overflow
- 等级：High | 项目：Internet | 披露：2020-10-12 | CVE：CVE-2019-11039
- 原文：https://hackerone.com/reports/593229

- - - - - - - - 
PHP upstream bug report: https://bugs.php.net/bug.php?id=78069
*Description:*
In _php_iconv_mime_decode() function in iconv.c, there's an out-of-bounds read due to an integer overflow vulnerability. MIME encoded string is being parsed and decoded in for loop with following condition:
[code omitted]
Inside this for loop, it's possible for str_left to be decreased and p1 to be increased at the same time when scan_stat is equal to 2 (i.e. case 2 branch of the switch) and the given character set is unrecognized and ICONV_MIME_DECODE_CONTINUE_ON_ERROR is specified, so it continues to parse the message. It will then try to skip the encoded word by searching for the other two '?' c


## Invalid Read on exif_process_SOFn
- 等级：High | 项目：Internet | 披露：2020-10-10 | CVE：CVE-2019-9640
- 原文：https://hackerone.com/reports/510025

- - - - - - - - 
This  bug is present in exif_scan_thumbnail method of ext/exif/exif.c file.
Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77540
PHP version : 7.1.26
CVE-ID : 2019-9640
## Impact
This bug may allow an attacker to read unintended data from memory.
---


## Heap Buffer Overflow (READ: 4) in phar_parse_pharfile
- 等级：High | 项目：Internet | 披露：2020-10-10 | CVE：CVE-2018-20783
- 原文：https://hackerone.com/reports/477344

- - - - - - - - 
Phar files with __HALT_COMPILER(); in unexpected places can lead to a buffer overrun. This is something I found while fuzzing with AFL using an ASAN instrumented PHP.
The issue can be observed by disabling the ZEND allocator and using ASAN (or valgrind/etc?) with a crafted phar as input. I have prepared an example PHAR file *php-oob4.phar*
[code omitted]
Base64 encoding of *php-oob4.phar* is as follows:
[code omitted]
OUTPUT
====
The following ASAN report was generated from this test case:
[code omitted]
## Impact
A context dependent attacker can trigger unsafe memory access. This may reveal information, affect availability, or be used as part of an exploit chain.
This was t


## GarlicRust - heartbleed style vulnerability in major I2P C++ router implementations
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-17066
- 原文：https://hackerone.com/reports/295740

- - - - - - - - 
Brief
-----
I2pd and kovri are both C++ I2P routers that share the same code base, as kovri was forked from i2pd several years ago. The vulnerability lies in a common code piece, making both implementations vulnerable, as was acknowledged by orignal, the main developer of i2pd.
The vulnerability is that there is lack of sanitation checks when handling Garlic messages in the both routers: by sending a specially crafted Garlic message, an attacker can cause the router to send onward an I2P message containing leaked RAM data, triggering a massive (up to ~16KB) information leakage.
Technical Details:
===========
Code Version: Taken from Kovri Github on the 18th of November 2017



## Heap-buffer-overflow in Perl__byte_dump_string (utf8.c) could lead to memory leak
- 等级：High | 项目：Internet | 披露：2019-10-24 | CVE：CVE-2018-6798,
- 原文：https://hackerone.com/reports/480778

- - - - - - - - 
With crafted regex match, I have found a heap-over-flow in function Perl__byte_dump_string, which would lead to memory leak.
* Reported to the [Perl security mailing list](https://rt.perl.org/Public/Bug/Display.html?id=132063) on 11 Sep 2017.
* Confirmed as a security flaw by TonyC on 24 Feb 2018
* CVE-2018-6797 assigned to this flaw on 7 Feb 2018
* [Public security advisory](https://github.com/Perl/perl5/blob/blead/pod/perl5262delta.pod) released on 14 April 2018
[code omitted]
## Impact
Depending on the heap implementation a remote attacker could leak heap information to bypass ASLR.
---


## CVE-2017-13008 The IEEE 802.11 parser in tcpdump before 4.9.2 has a buffer over-read in print-802_11.c:parse_elements().
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-13008
- 原文：https://hackerone.com/reports/268805

- - - - - - - - 
Reported to the devs on 6 March 2017.
Tcpdump 4.9.2 released on 8 September 2017.
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/5edf405d7ed9fc92f4f43e8a3d44baa4c6387562
`The IEEE 802.11 parser in tcpdump before 4.9.2 has a buffer over-read in print-802_11.c:parse_elements().`
[code omitted]
---


## CVE-2017-12986 The IPv6 routing header parser in tcpdump before 4.9.2 has a buffer over-read in print-rt6.c:rt6_print().
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-12986
- 原文：https://hackerone.com/reports/268804

- - - - - - - - 
Reported to the devs on 4 February 2017.
Tcpdump 4.9.2 released on 8 September 2017.
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/7ac73d6cd41e9d4ac0ca7e6830ca390e195bb21c
`The IPv6 routing header parser in tcpdump before 4.9.2 has a buffer over-read in print-rt6.c:rt6_print().`
[code omitted]
---


## CVE-2017-13038 The PPP parser in tcpdump before 4.9.2 has a buffer over-read in print-ppp.c:handle_mlppp().
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-13038
- 原文：https://hackerone.com/reports/268808

- - - - - - - - 
Reported to the devs on 11 June 2017.
Tcpdump 4.9.2 released on 8 September 2017.
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/7335163a6ef82d46ff18f3e6099a157747241629
`The PPP parser in tcpdump before 4.9.2 has a buffer over-read in print-ppp.c:handle_mlppp().`
[code omitted]
---


## CVE-2017-13010 The BEEP parser in tcpdump before 4.9.2 has a buffer over-read in print-beep.c:l_strnstart().
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-13010
- 原文：https://hackerone.com/reports/268807

- - - - - - - - 
Reported to the devs on 6 March 2017.
Tcpdump 4.9.2 released on 8 September 2017.
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/877b66b398518d9501513e0860c9f3a8acc70892
`The BEEP parser in tcpdump before 4.9.2 has a buffer over-read in print-beep.c:l_strnstart().`
[code omitted]
---


## CVE-2017-13009 The IPv6 mobility parser in tcpdump before 4.9.2 has a buffer over-read in print-mobility.c:mobility_print().
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-13009
- 原文：https://hackerone.com/reports/268806

- - - - - - - - 
Reported to the devs on 6 March 2017.
Tcpdump 4.9.2 released on 8 September 2017.
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/db8c799f6dfc68765c9451fcbfca06e662f5bd5f
`The IPv6 mobility parser in tcpdump before 4.9.2 has a buffer over-read in print-mobility.c:mobility_print().`
[code omitted]
---


## CVE-2017-12985: The IPv6 parser in tcpdump before 4.9.2 has a buffer over-read in ip6_print()
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-12985
- 原文：https://hackerone.com/reports/268803

- - - - - - - - 
Reported to the devs on 4 February 2017.
Tcpdump 4.9.2 released on 8 September 2017.
Patch: https://github.com/the-tcpdump-group/tcpdump/commit/66df248b49095c261138b5a5e34d341a6bf9ac7f
`The IPv6 parser in tcpdump before 4.9.2 has a buffer over-read in print-ip6.c.`
[code omitted]
---


## A specifically malformed MQTT Subscribe packet crashes MQTT Brokers using the mqtt-packet module for decoding
- 等级：High | 项目：Node.js | 披露：2019-04-28 | CVE：CVE-2019-5432
- 原文：https://hackerone.com/reports/541354

- - - - - - - - 
I would like to report a buffer over-read in mqtt-packet respectively BufferList module.
It allows triggering an out of range read on a buffer which throws a RangeError. MQTT Brokers like mosca and aedes using this module can be forced to crash by sending a specifically malformed MQTT Subscribe packet. 
# Module
**module name:** mqtt-packet
**version:** 6.1.1
**npm page:** `https://www.npmjs.com/package/mqtt-packet`
## Module Description
Encode and Decode MQTT 3.1.1, 5.0 packets the node way.
## Module Stats
114,635 weekly downloads
# Vulnerability
## Vulnerability Description
From the original E-Mail to the Author:
*Hey Matteo,
while playing around with mosca/aedes and our 

