# HackerOne 实战案例：off-by-one-error

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Exim off-by-one RCE vulnerability
- 等级：Critical | 项目：Internet | 披露：2019-09-26 | CVE：CVE-2018-6789
- 原文：https://hackerone.com/reports/322935

- - - - - - - - 
Hi, 
I found an off-by-one in Exim MTA utility function. It was reported to exim and official patch has been released, assigned CVE-2018-6789. This bug affects all versions of exim.
This bug is simple, but can be leverage to gain remote code execution, using skillful heap exploitation. Details are here: https://devco.re/blog/2018/03/06/exim-off-by-one-RCE-exploiting-CVE-2018-6789-en/
I believe exim is widespread enough and it seems to fit all criteria. I wonder if this finding worths a bounty, or the reason why it is not included. Thanks!
## Impact
Pre-auth remote code execution on all versions of exim mail server
---


## urlapi: off-by-one in custom scheme validation skips last character
- 等级：High | 项目：curl | 披露：2026-03-12 | CVE：-
- 原文：https://hackerone.com/reports/3598358

- - - - - - - - 
## Summary
In `lib/urlapi.c`, the `set_url_scheme()` function has an off-by-one error when validating custom scheme names. The validation loop checks `scheme[0]` twice (once by `ISALPHA`, once in the loop) and never checks the last character. This allows schemes ending with any arbitrary byte (e.g., `foo!`, `bar{`, `bad/`) to pass validation when set via `curl_url_set(url, CURLUPART_SCHEME, ..., CURLU_NON_SUPPORT_SCHEME)`, violating RFC 3986 Section 3.1.
## Affected version
curl 8.19.1-DEV (Darwin) libcurl/8.19.1-DEV OpenSSL/3.6.1 zlib/1.2.12 brotli/1.2.0 zstd/1.5.7 libidn2/2.3.8
Protocols: dict file ftp ftps gopher gophers http https imap imaps ipfs ipns mqtt mqtts pop3 pop

