# HackerOne 实战案例：information-exposure-through-sent-data

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Alt-Svc bypasses credential leak protection (CVE-2018-1000007)
- 等级：High | 项目：curl | 披露：2026-01-04 | CVE：CVE-2018-1000007
- 原文：https://hackerone.com/reports/3485826

- - - - - - - - 
## Summary
I found a bug where curl's Alt-Svc implementation fails to strip sensitive authentication headers (Authorization and Cookies) when remapping a connection to a different host or port. This essentially bypasses the security fix for CVE-2018-1000007.
While auditing the code, I noticed that Alt-Svc remappings in `lib/url.c` update `conn->conn_to_host.name` and `conn->conn_to_port`, but the authentication guard in `lib/vauth/vauth.c` (the `Curl_auth_allowed_to_host` function) only checks the original `conn->host.name` and `conn->remote_port`.
Additionally, Alt-Svc remappings do not set the `data->state.this_is_a_follow` flag. Since the auth guard only activates when th


## Proxy-Authorization header is leaked to origin server after redirect from proxied to direct connection
- 等级：High | 项目：curl | 披露：2025-12-30 | CVE：-
- 原文：https://hackerone.com/reports/3480713

- - - - - - - - 
## Summary
curl leaks the Proxy-Authorization header to the origin server after following an HTTP redirect that transitions from a proxied connection to a direct connection (e.g. when using --noproxy or when proxy is bypassed after redirect). This causes proxy credentials (which are hop-by-hop) to be sent to unintended servers.
## Affected version
Tested with:
curl 8.17.0 on Linux x86_64
curl -V:
[PASTE curl -V OUTPUT HERE]
## Steps To Reproduce
1. Start a fake origin server:
   nc -l -p 8080
2. Start a fake proxy that redirects to the origin:
   printf "HTTP/1.1 302 Found\r\nLocation: http://127.0.0.1:8080/\r\nContent-Length: 0\r\n\r\n" | nc -l -p 3128
3. Run curl:
   curl 


## Authorization Header Leak via --location-trusted in Curl
- 等级：High | 项目：curl | 披露：2025-07-03 | CVE：-
- 原文：https://hackerone.com/reports/2946924

- - - - - - - - 
Curl's --location-trusted Option Leaks Authorization Header Across Domains
The `--location-trusted` option in Curl forwards the Authorization header when following cross-origin redirects, exposing Basic Authentication credentials to untrusted hosts.
- If an attacker controls a redirecting endpoint, they can steal credentials from any requests using Basic Auth.
- Unlike `--location`, which strips authentication headers for security, `--location-trusted` forwards them without warning, leading to unintended  
credential leakage.
This violates authentication best practices and introduces a serious security risk
---
Affected Versions
Run:
curl -V
 **Example Output:**
curl 8.5.0 (


## Remote memory disclosure vulnerability in libcurl on 64 Bit Windows
- 等级：High | 项目：curl | 披露：2022-02-21 | CVE：-
- 原文：https://hackerone.com/reports/1444539

- - - - - - - - 
# Remote memory disclosure vulnerability in libcurl on 64 Bit Windows
## Summary:
`libcurl` (latest) contains a vulnerability that enables attackers to
remotely read memory beyond the bounds of a buffer in the style of the
infamous "heartbleed" vulnerability. Luckily, however, this is only
possible when `libcurl` runs on 64 bit Windows and it requires an
attacker capable of influencing the size of a file upload part.
The core of the problem is the following: while on 64 Linux and BSD
systems, `sizeof(long)` is 8, on 64 bit Windows, it
is 4. Consequently, the function `AddHttpPost` carries out an integer
truncation and sign conversion on these systems, as the parameter
`buffe

