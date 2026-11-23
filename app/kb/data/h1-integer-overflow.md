# HackerOne 实战案例：integer-overflow

_7 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Cookie Max-Age Integer Overflow Vulnerability
- 等级：Critical | 项目：curl | 披露：2026-01-19 | CVE：-
- 原文：https://hackerone.com/reports/3516186

- - - - - - - - 
## Summary:
The cookie parsing code in `lib/cookie.c` contains an integer overflow vulnerability when processing the `Max-Age` attribute of HTTP cookies. The vulnerable code attempts to add the max-age value to the current timestamp without adequate overflow protection
While the code includes an overflow check (`CURL_OFF_T_MAX - now < co->expires`), this check itself can experience integer overflow in edge cases where:
1. The `max-age` value is extremely large (near `CURL_OFF_T_MAX`)
2. The current time (`now`) is large enough that the subtraction `CURL_OFF_T_MAX - now` produces unexpected results
3. The addition `co->expires += now` occurs without proper bounds checking
An 


## Integer overflow vulnerability
- 等级：Critical | 项目：Glovo | 披露：2022-05-17 | CVE：-
- 原文：https://hackerone.com/reports/1562515

- - - - - - - - 
## Summary:
In one of my previous reports i send parameter tampering report vulnerability. Then you asked me to send PoC and you just closed it, that's why i'm sending you this new report with exactly name of vulnerability. Integer Overflows are closely related to other conditions that occur when manipulating integers. An Integer Overflow is the condition that occurs when the result of an arithmetic operation, such as multiplication or addition, exceeds the maximum size of the integer type used to store it. When an integer overflow occurs, the interpreted value will appear to have “wrapped around” the maximum value and started again at the minimum value. For example, an 8-bi


## Integer overflow leading to buffer overflow
- 等级：Critical | 项目：Internet | 披露：2019-09-25 | CVE：CVE-2018-18311
- 原文：https://hackerone.com/reports/424447

- - - - - - - - 
There exists an integer overflow in Perl_my_setenv @ util.c : 2070
2070: void Perl_my_setenv(pTHX_ const char *nam, const char *val) {
...
2166:         const int nlen = strlen(nam);
...
2171:         vlen = strlen(val);
2172:         new_env = (char*)safesysmalloc((nlen + vlen + 2) * sizeof(char));
Here in a 64 bit version of Perl, since the arguments `nam` and `val` are user controlled, the 32 bit integers `nlen` and `vlen` are also under the control of the attacker. Therefore, if `nam` and `val` are two very long strings (for example, 2147483647 bytes long), the addition at line 2172 would result in an integer overflow.
The `new_env` would therefore be a chunk of a size w


## integer Overflow in MQTT Protocol Handling Allows Bypassing Message Size Limit
- 等级：High | 项目：curl | 披露：2026-01-13 | CVE：-
- 原文：https://hackerone.com/reports/3508500

- - - - - - - - 
## Summary:
A logic error involving an integer overflow (specifically, an unsigned integer underflow) exists in the lib/mqtt.c file within the mqtt_publish function. This vulnerability allows an attacker (or a malicious user configuration) to bypass the explicit MAX_MQTT_MESSAGE_SIZE check.
The vulnerability occurs when curl calculates whether an MQTT packet exceeds the maximum allowed size ( 0xFFFFFFF or ~268 MB). The validation logic performs a subtraction operation using the payload length before verifying if the payload is already too large. If the payload length exceeds the maximum size, the subtraction wraps around (underflows) to a large positive value, causing the sa


## MQTT Protocol Violation & Integer Overflow in libcurl
- 等级：High | 项目：curl | 披露：2026-01-01 | CVE：-
- 原文：https://hackerone.com/reports/3484319

- - - - - - - - 
## Executive Summary
**Vulnerability Type:** CWE-190
**Component:** lib/mqtt.c  
**Function:** mqtt_decode_len  
**Affected Architectures:**
- **All architectures:** Protocol non-compliance leading to stream desynchronization
- **32-bit architectures:** Deterministic integer overflow in length decoding
libcurl does not correctly enforce the MQTT v3.1.1 specification limit for the “Remaining Length” field when decoding incoming packets. This allows malformed MQTT packets to be parsed incorrectly, leading to protocol desynchronization and potential denial of service. On 32-bit systems, the decoding logic additionally allows a deterministic integer overflow.
---
## Root Cause: 


## Integer overflow in CipherUpdate
- 等级：High | 项目：Internet | 披露：2021-04-08 | CVE：CVE-2021-23840,
- 原文：https://hackerone.com/reports/1113025

- - - - - - - - 
## Summary:
I reported an integer overflow to the OpenSSL security list on Dec 13, 2020 and it was fixed in OpenSSL 1.1.1j. Reporting it here for the bounty. It was assigned CVE-2021-23840 (https://nvd.nist.gov/vuln/detail/CVE-2021-23840) which NVD rated CVSS 7.5. Amusingly, the same bug (worked around by my library pyca/cryptography before 1.1.1j was released) was assigned CVE-2020-36242 (https://nvd.nist.gov/vuln/detail/CVE-2020-36242), which received a 9.1 CVSS from NVD.
## Steps To Reproduce:
The below is a reproducer for prior to 1.1.1j.
[code omitted]
## Impact
This returned negative output length, which, when combined with common use of pointer arithmetic in buffers r


## CVE-2017-8798 - miniupnp getHTTPResponse chunked encoding integer signedness error
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-8798
- 原文：https://hackerone.com/reports/227344

- - - - - - - -

