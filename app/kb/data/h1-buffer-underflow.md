# HackerOne 实战案例：buffer-underflow

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Buffer overflow in strcpy
- 等级：Critical | 项目：curl | 披露：2024-11-07 | CVE：-
- 原文：https://hackerone.com/reports/2823554

- - - - - - - - 
**Buffer Overflow Exploit Analysis**
The vulnerability in the program is a classic case of a buffer overflow, triggered by the unsafe use of the `strcpy()` function, which lacks bounds checking. The following section describes the vulnerability, how the return address is overflowed, and how the exploit works to achieve remote code execution.
**Vulnerable Function:**
The vulnerability occurs due to the use of `strcpy()` in the program, which copies data from a source buffer to a destination buffer without verifying that the destination buffer is large enough to hold the incoming data. If the input string is larger than the allocated buffer size, it results in a buffer overflo


## Negative size parameter in mb_split
- 等级：Critical | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-9025
- 原文：https://hackerone.com/reports/476178

- - - - - - - - 
https://bugs.php.net/bug.php?id=77367
mb_split doesn't correctly detect the length when the $string has an unfinished multibyte character at the end of the string. This causes a crash due to a negative parameter to add_next_index_stringl, which calls zend_string_init and memcpy.
Could reproduce on master.
## Impact
This could be used to cause memory corruption/leakage.
---


## CVE-2019-11043: a buffer underflow in fpm_main.c can lead to RCE in php-fpm
- 等级：Critical | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-11043
- 原文：https://hackerone.com/reports/722327

- - - - - - - - 
The vulnerability exists in php-fpm because of missing bounds check in fpm_main.c. If the FastCGI variable `PATH_INFO` is empty, the underflow happens when the code tries to calculate the value of the `path_info` variable. An invalid pointer in `path_info` leads to a single byte out-of-bounds write, which can be leveraged to code execution.
The php-fpm allows anyone who can connect to its' port to execute code, so an RCE in php-fpm is not interesting by itself. However, this particular issue can be exploited even by a user who has access to the HTTP server (which is Nginx typically). In certain Nginx configurations, it is possible to make it send empty `PATH_INFO` value by b


## tcpdump: CVE-2018-14879 - buffer overflow in tcpdump.c:get_next_file()
- 等级：Critical | 项目：Internet | 披露：2020-02-13 | CVE：CVE-2018-14879
- 原文：https://hackerone.com/reports/724217

- - - - - - - - 
The release of tcpdump 4.9.3 brought many bug fixes, including one I submitted, CVE-2018-14879.
`The command-line argument parser in tcpdump before 4.9.3 has a buffer overflow in tcpdump.c:get_next_file().`
[code omitted]
Reported: 2018 May 14 (via email to security@tcpdump.org)
Fix Released: 2018 September 30
CVE: https://nvd.nist.gov/vuln/detail/CVE-2018-14879
Credit:  https://www.tcpdump.org/public-cve-list.txt
[code omitted]
## Impact
Stack buffer overflow can be caused deliberately as part of an attack known as stack smashing. If the affected program is running with special privileges, or accepts data from untrusted network hosts (e.g. a webserver) then the bug is a pot

