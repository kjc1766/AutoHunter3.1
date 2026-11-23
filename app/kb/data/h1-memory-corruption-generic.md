# HackerOne 实战案例：memory-corruption-generic

_26 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Buffer Overflow in curl MQTT Test Server (tests/server/mqttd.c) via Malicious CONNECT Packet
- 等级：Critical | 项目：curl | 披露：2025-06-28 | CVE：-
- 原文：https://hackerone.com/reports/3101127

- - - - - - - - 
# Title: Buffer Overflow in curl MQTT Test Server (mqttd.c) via Malicious CONNECT Packet
## Description
The MQTT test server (`mqttd.c`) in the curl project contains a buffer overflow vulnerability due to improper validation of password length fields in MQTT `CONNECT` packets. An attacker can craft a malicious packet with an excessive password length value to trigger a denial of service (server crash) or potentially execute arbitrary code.
---
## Summary
The vulnerability occurs when parsing the password length field in MQTT `CONNECT` packets:
- No bounds checking is performed when reading the 2-byte password length
- Subsequent memory operations use this unvalidated length,


## LZMADecompressor.decompress Use After Free
- 等级：Critical | 项目：Internet | 披露：2016-12-05 | CVE：-
- 原文：https://hackerone.com/reports/172562

- - - - - - - - 
I have submitted a vulnerability that has now been fixed. The report includes a proof of concept that demonstrates code execution. The submitted patch was accepted with minor changes.
https://bugs.python.org/issue28275
---
Python 3.5.2 suffers from a use after free vulnerability caused by the behavior of the LZMADecompressor.decompress method. The problem exists due to a dangling pointer created by an incomplete error path in the _lzma!decompress function.
static PyObject *
decompress(Decompressor *d, uint8_t *data, size_t len, Py_ssize_t max_length)
{
    char input_buffer_in_use;
    PyObject *result;
    lzma_stream *lzs = &d->lzs;
    /* Prepend unconsumed input if neces


## imagecolormatch Out Of Bounds Write on Heap
- 等级：High | 项目：Internet | 披露：2020-10-10 | CVE：CVE-2019-6977
- 原文：https://hackerone.com/reports/478368

- - - - - - - - 
The link to the PHP bug: https://bugs.php.net/bug.php?id=77270
This is possible to exploit in PHP 7.0.33 and 5.6.39. I used this vulnerability to write a local safe mode bypass exploit.
It is possible to write up to 1200 bytes over the boundaries of a buffer allocated in the imagecolormatch function, which then calls gdImageColorMatch()
The function takes two gdImagePtr as arguments and wants to compare both of them. It then allocates a dynamic buffer with the following calculation:
`buf = (unsigned long *)safe_emalloc(sizeof(unsigned long), 5 * im2->colorsTotal, 0);`
im2->colorsTotal is under the control of an attacker. By simply allocating only one color to the second imag


## napi_get_value_string_X allow various kinds of memory corruption
- 等级：High | 项目：Node.js | 披露：2020-07-02 | CVE：CVE-2020-8174
- 原文：https://hackerone.com/reports/784186

- - - - - - - - 
**Summary:**
`napi_get_value_string_latin1`, `napi_get_value_string_utf8`, `napi_get_value_string_utf16` are vulnerable to buffer overflows, partially due to an integer underflow.
**Description:**
`napi_get_value_string_latin1`, `napi_get_value_string_utf8`, and `napi_get_value_string_utf16` behave like this:
1. If the output pointer is `NULL`, return.
2. Write `min(string_length, bufsize - 1)` bytes to the output buffer. Note that `bufsize` is an unsigned type, so this leads to an integer underflow for `bufsize == 0`. Since this is a `size_t`, the underflow will cause the entire string to be written to memory, no matter how long the string is.
3. Finally, write to `buf[copi


## HTTP/2 Denial of Service Vulnerability
- 等级：High | 项目：Node.js | 披露：2020-02-13 | CVE：-
- 原文：https://hackerone.com/reports/335533

- - - - - - - - 
**Summary:** Malformed HTTP/2 frames cause NodeJS http2 module to perform an uninitialized read. This results in a segmentation fault of the node process, causing a denial of service for all users of the instance.
**Description:** I have already worked extensively with the nodejs core security team on this issue. The issue has already been acknowledged by James Snell so this report is to officially get the issue on the books. All necessary details for this bug report have already been provided via security mailing list for nodejs. This issue is known to be present in v9 and v10 of nodejs.
## Steps To Reproduce:
Again, all the necessary repro instructions, core file, and stac


## Stack Buffer Overflow in GD dynamicGetbuf
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：-
- 原文：https://hackerone.com/reports/175587

- - - - - - - - 
#Stack-based buffer over flow in GD dynamicGetbuf#
- Vulnerable function: imagecreatefromstring()
- Bug has been reported: https://bugs.php.net/bug.php?id=73280
- Submitted a patch and accepted: https://github.com/php/php-src/commit/cc08cbc84d46933c1e9e0149633f1ed5d19e45e9
- Impact: Remotely Exploitable. Given the nature of the function, it is not uncommon to see programmers passing user inputs to the vulnerable function imagecreatefromstring(). Real life examples:
  * https://github.com/rbloone/sslv-scraper/blob/305c79e24421795abdae8106ad686cb9c6742e94/img.php
  * https://github.com/hick/utl/blob/a573f04ac0a6db2cfe56e2785dfab7b1534c04f3/pasteimage/file.php
Description:
----


## Malformed .MDL triggers an Access Violation on GoldSRC (hl.exe)
- 等级：High | 项目：Valve | 披露：2019-10-09 | CVE：-
- 原文：https://hackerone.com/reports/495793

- - - - - - - - 
A malformed player .MDL triggers an exploitable Access Violation on GoldSRC engine games (Half-Life) upon invocation, which could lead to remote code execution on a client.
###Crash Information
FAILURE_ID_HASH_STRING:  um:invalid_pointer_write_exploitable_c0000005_hw.dll!createinterface
Event Type: Exception
Exception Faulting Address: 0x4c01000
First Chance Exception Type: STATUS_ACCESS_VIOLATION (0xC0000005)
Exception Sub-Type: Write Access Violation
FOLLOWUP_IP: 
hw!CreateInterface+282aa
03a554ea d95efc          fstp    dword ptr [esi-4]
PROBLEM_CLASSES: 
    ID:     [0n309]
    Type:   [@ACCESS_VIOLATION]
    Class:  Addendum
    Scope:  BUCKET_ID
    Name:   Omit
    Da


## CVE-2017-5482 The Q.933 parser in tcpdump before 4.9.0 has a buffer overflow in print-fr.c:q933_print().
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-5482,
- 原文：https://hackerone.com/reports/202969

- - - - - - - - 
Reported to the project maintainers in 2016. Regardless of CVE-2016-8575 q933_print()
still could overread the buffer trying to parse a short packet. Fixed by https://github.com/the-tcpdump-group/tcpdump/commit/c39c1d99ac3b6d5d9519b39da6717180651650d3.
---


## CVE-2017-5342 In tcpdump before 4.9.0 a bug in multiple protocol parsers could cause a buffer overflow in print-ether.c:ether_print()
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-5342
- 原文：https://hackerone.com/reports/202968

- - - - - - - - 
Reported to the project maintainers in 2016. gre_print_0() and the functions modelled after it passed the value of "length" instead of the value of "caplen", this could make ether_print() access beyond the memory allocated for the captured packet. Fixed by https://github.com/the-tcpdump-group/tcpdump/commit/0db4dcafe5ae38201d3869c96a96cb714d82ff35.
---


## CVE-2017-5484 The ATM parser in tcpdump before 4.9.0 has a buffer overflow in print-atm.c:sig_print()
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-5484
- 原文：https://hackerone.com/reports/202967

- - - - - - - - 
Reported to the project maintainers in 2016. The function sig_print() did receive a correct caplen parameter value but didn't use it correctly which could result in a read outside of buffer. Fixed by https://github.com/the-tcpdump-group/tcpdump/commit/5d214e36eed3565fbdc0f9b527bbc33a6bb63972.
---


## CVE-2017-5341 The OTV parser in tcpdump before 4.9.0 has a buffer overflow in print-otv.c:otv_print()
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-5341
- 原文：https://hackerone.com/reports/202965

- - - - - - - - 
Reported to the project maintainers in 2016. The function sig_print() did receive a correct caplen parameter value but didn't use it correctly which could cause a read outside of buffer. Fixed by https://github.com/the-tcpdump-group/tcpdump/commit/409ffe94529df3d8bb8258bf99586f821756cb29.
---


## CVE-2017-5204: The IPv6 parser in tcpdump before 4.9.0 has a buffer overflow in print-ip6.c:ip6_print()
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-5204
- 原文：https://hackerone.com/reports/202960

- - - - - - - - 
Reported to the project maintainer in October 2016. A specially crafted IPv6 packet could trigger a read outside of buffer in tcpdump.
[code omitted]
Fixed by https://github.com/the-tcpdump-group/tcpdump/commit/d6913f7e3fc6d3084ab64d179853468e58cdca4b.
---


## ZeroMQ libzmq remote code execution
- 等级：High | 项目：Internet | 披露：2019-09-12 | CVE：CVE-2019-6250
- 原文：https://hackerone.com/reports/477073

- - - - - - - - 
Bug report and exploit: https://github.com/zeromq/libzmq/issues/3351
Fix by me: https://github.com/zeromq/libzmq/pull/3353
My motive for full disclosure is as follows:
[code omitted]
Source: http://zeromq.org/area:faq
The issue reporting page (http://zeromq.org/docs:issue-tracking) instructs to open a Github issue, with no special procedure for security issues, so I went ahead and did just that.
libzmq appears to be widely used and has wrapper implementations for Go, Python, Java, Node.js, etc.
## Impact
Running arbitrary code on the victim's system.
---


## Linux kernel: CVE-2017-1000112: a memory corruption due to UFO to non-UFO path switch
- 等级：High | 项目：Internet | 披露：2019-09-11 | CVE：CVE-2017-1000112
- 原文：https://hackerone.com/reports/684573

- - - - - - - - 
Hi!
[CVE-2017-1000112](https://nvd.nist.gov/vuln/detail/CVE-2017-1000112) is a vulnerability I found in the Linux kernel caused by a UFO to non-UFO path switch for UFO packets. It can be exploited to gain kernel code execution from an unprivileged process.
This vulnerability was reported to security@kernel.org and linux-distros@ following the coordinated disclosure process and then [announced](https://www.openwall.com/lists/oss-security/2017/08/13/1) on oss-security@. The fix was [committed](https://git.kernel.org/pub/scm/linux/kernel/git/davem/net.git/commit/?id=85f1bd9a7b5a79d5baa8bf44af19658f7bf77bfa) on Aug 10, 2017.
I wrote a proof-of-concept exploit for a range of Ubun


## Linux kernel: CVE-2017-7308: a signedness issue in AF_PACKET sockets
- 等级：High | 项目：Internet | 披露：2019-09-11 | CVE：CVE-2017-7308
- 原文：https://hackerone.com/reports/684567

- - - - - - - - 
Hi!
[CVE-2017-7308](https://nvd.nist.gov/vuln/detail/CVE-2017-7308) is a vulnerability I found in the Linux kernel caused by a signedness issue in AF_PACKET sockets. It can be exploited to gain kernel code execution from an unprivileged process. The kernel has to be built with CONFIG_PACKET for the vulnerability to be present. A lot of modern distributions enable this option by default.
I initially reported this vulnerability to security@kernel.org following the coordinated disclosure process. As advised by them I've developed a fix for this vulnerability and sent it upstream. The fix was [committed](https://git.kernel.org/cgit/linux/kernel/git/torvalds/linux.git/commit/?id=


## heap-buffer-overflow (buffer read overrun) in curl: ourWriteOut() src/tool_writeout.c:115
- 等级：High | 项目：Internet | 披露：2018-05-16 | CVE：-
- 原文：https://hackerone.com/reports/212931

- - - - - - - - 
Curl is a ubiquitous tool in use by millions of people around the world. I reported this flaw to the curl security mailing list on 10 March 2017:
[code omitted]
Fixed by the developers on 12 March 2017:
https://github.com/curl/curl/commit/1890d59905414ab84a35892b2e45833654aa5c13
From the git commit:
[code omitted]
From the curl security mailing list:
[code omitted]
---


## Memory corrouption in mrb_gc_mark
- 等级：High | 项目：shopify-scripts | 披露：2017-04-17 | CVE：-
- 原文：https://hackerone.com/reports/208363

- - - - - - - - 
The memory corruption in mrb_gc_mark function can lead to code execution or at least DoS on mruby.
PoC attached.


## Certain inputs cause tight C-level recursion leading to process stack overflow
- 等级：High | 项目：shopify-scripts | 披露：2017-03-14 | CVE：-
- 原文：https://hackerone.com/reports/189633

- - - - - - - - 
Introduction
============
Certain legal Ruby programs can cause a tight recursion on the C-level (without using `eval`) while spending very little of the Ruby-level stack. This precludes triggering a Ruby stack overflow exception and eventually leads to a process stack overflow and a segfault. Both vanilla mruby and mruby running inside mruby-engine are vulnerable.
Proof of concept
================
recursive_to_i.rb:
------------------
    def to_i
        '' * self
    end
    to_i
1. Save the above code as `recursive_to_i.rb`.
2. Run either:
   a) `mruby recursive_to_i.rb`
   b) `sandbox recursive_to_i.rb`
3. Both cause a segfault due to a process stack overflow.
Discussio


## Crash: Overwriting NoMethodError with a builtin class crashes/corrupts memory
- 等级：High | 项目：shopify-scripts | 披露：2017-03-01 | CVE：-
- 原文：https://hackerone.com/reports/186723

- - - - - - - - 
Uhm, while testing this I seem to have broken `https://mruby.science`.. Ooops, sorry about that!
Anyway, here's the bug:
Overwriting (at least, not sure about other triggers) `NoMethodError` with a builtin class like `Fixnum` or `Integer` leads to a rather interesting behavior. `https://mruby.science` didn't crash all the times (reads: it sometimes does report a `MRubyEngine::EngineTimeQuotaError`), but sometimes it does report the 'Application Error' page after a long time. My local sandbox behaves somewhat like this: it prints the `MRubyEngine::EngineTimeQuotaError` error but crashes anyway.
The root cause is that triggering the `NoMethodError` triggers another `NoMethodEr


## attempting double-free using the mruby compiler `mrbc`
- 等级：High | 项目：shopify-scripts | 披露：2017-02-07 | CVE：-
- 原文：https://hackerone.com/reports/193517

- - - - - - - - 
I cloned the mruby git 4 days ago, started fuzzing with American Fuzzy Lop. This is the 1st crash. 
./mrbc test000
[code omitted]
---


## SIGSEGV on mruby's mark_tbl() (Invalid memory access)
- 等级：High | 项目：shopify-scripts | 披露：2016-12-17 | CVE：-
- 原文：https://hackerone.com/reports/183239

- - - - - - - - 
There is an invalid memory access on mruby when calling to `mark_tbl()` which causes a SIGSEGV and leads to denial of service.
## Sample
The following code triggers the bug (attached as mark_tbl.min2.rb):
[code omitted]
## Crash
Here we can see the crash (full crash output attached)
[code omitted]
## Crash debug
[code omitted]
Backtrace
[code omitted]
## Impact
Its impact seems to be limited to DoS of the service running the ruby sandbox. The invalid address can be controlled by the user but in a really limited way, so I doubut this chould be turned into a write-what-where type vuln.
---


## Crash: mrb_any_to_s can't handle NilClass, Symbol and Fixnum
- 等级：High | 项目：shopify-scripts | 披露：2016-12-16 | CVE：-
- 原文：https://hackerone.com/reports/185794

- - - - - - - - 
When using `boxing_word.h` (haven't tested other boxing methods yet), `mrb_any_to_s` is unable to handle `NilClass`, `Symbol` and `Fixnum`. This can be achieved by just deleting `:to_s` from the class and let `mrb_any_to_s` crash.
I tried to come up with a fix but I'm not 100% sure where this should be fixed. The boxing schemas all work slightly different so fixing `mrb_any_to_s` in a way that it respects the boxing schema is not my preferred choice (as implementation details shouldn't bleed through to that method). I guess it's either the right call to make `mrb_any_to_s` always safe or pull part of the functionality into the specific boxing header.
#PoC
Works with `Symbol`


## mruby-time: Crash host with uninitialized Time obj
- 等级：High | 项目：shopify-scripts | 披露：2016-12-16 | CVE：-
- 原文：https://hackerone.com/reports/184661

- - - - - - - - 
So once again, another try ;) (As always hopefully unknown and valid ;))
`Time::initialize_copy` performs its copy action even on `Time` objects on which `initialize` never ran, leading to a crash. 
The PoC crashes https://www.mruby.science/runs - didn't try Shopify production servers for the usual reasons.
As a sidenote: Matz has patched a memory leak in the `mruby-time` here: https://github.com/mruby/mruby/commit/d97a37eb7b4fe52bb1b16bb6f7410fbae85e3809 You probably want to pull this into your copy of mruby-time as this has the potential (not tested) to slowly eat up memory if this condition is hit on purpose. I didn't want to create its own bugreport for this as it's kind


## Crash: calling Proc::initialize_copy with a Proc instance where initialize never ran leads to a crash
- 等级：High | 项目：shopify-scripts | 披露：2016-12-16 | CVE：-
- 原文：https://hackerone.com/reports/184857

- - - - - - - - 
Using the same trick from #184661 with `Proc` leads to another crash, this time in `Proc` related functions.
Again, haven't looked into it besides validity testing and an initial code lookup (more detailed investigation + possible patches when there's more time on my side). Again, to give you guys the possibility to get this fixed ASAP without being limited by the time I got to spare.
# Impact
I didn't look too close but as it's accessing a 0+OFFSET this might be usable to gain code execution. Otherwise it's just a DoS, further investigation is needed.
# PoC
The PoC below crashes the `https://www.mruby.science/runs` sandbox, `mruby` master tip and `mruby-engine` reliably.
[c


## Memory disclosure in mruby String#lines method
- 等级：High | 项目：shopify-scripts | 披露：2016-12-16 | CVE：-
- 原文：https://hackerone.com/reports/181319

- - - - - - - - 
This bug was found with `jmlb337`.
Hey again,
while reviewing mruby for vulnerabilities, I stumble onto a case that allow an attacker to leak heap content including pointer that can be used along another vulnerability to craft a complete exploit.
## Reproduction Step
1. Allocate a string with a few lines.
2. Call String#lines and free or reallocate the string.
3. Allocate a few objects.
4. The next lines will now contains the value of the newly allocated data, including pointer used by `mrb_value`s.
## PoC
[code omitted]
Look at `@a` to get the "UUUU..." `mrb_value` object and strings.
## Explaination
The bug is triggered due to the caching of `p` at [string.c:310](https://g


## JSBeautifier BApp: Race condition leads to memory disclosure
- 等级：High | 项目：PortSwigger | 披露：2016-12-07 | CVE：-
- 原文：https://hackerone.com/reports/187134

- - - - - - - - 
Description
====================
If an attacker builds up multiple connections which will be released at the same time having a response Content-Length of 0, leaving out the response Content-Length header or having a higher Content-Length than the actual response while insinuating starting a doc-type then the stacked up connections will interfere with each other and, besides other weird behavior, will scramble the response buffers through each other.
The following behaviors have been observed.
 - Burp strips the content completely and comes back with only the headers
 - Buffers between the requests get scrambled up leading to content leaking between them
 - The original byte

