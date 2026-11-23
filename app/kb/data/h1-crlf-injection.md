# HackerOne 实战案例：crlf-injection

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## CRLF Injection / Protocol Smuggling in libcurl via CURLOPT_USERNAME (IMAP)
- 等级：Critical | 项目：curl | 披露：2025-12-28 | CVE：-
- 原文：https://hackerone.com/reports/3479984

- - - - - - - - 
## Summary:
I have discovered a CRLF injection vulnerability in the IMAP protocol implementation of libcurl. The vulnerability exists because the `imap_atom` function in `lib/imap.c` fails to properly sanitize or quote Carriage Return (`\r`) and Line Feed (`\n`) characters when processing the `CURLOPT_USERNAME` option.
This allows an attacker to inject arbitrary IMAP commands by inserting `\r\n` sequences into the username field. When these characters are sent to the server, they terminate the current command and allow the subsequent data to be interpreted as a new, separate command (Protocol Smuggling).
## Affected version
I successfully reproduced this on the latest master


## HTTP/3 Protocol Smuggling and Header Injection via CRLF in QPACK value conversion
- 等级：Critical | 项目：curl | 披露：2025-12-27 | CVE：-
- 原文：https://hackerone.com/reports/3479203

- - - - - - - - 
A fundamental design flaw exists in how libcurl handles HTTP/3 (QUIC) response headers across all supported backends (ngtcp2, quiche, openssl-quic). The vulnerability stems from the unsafe transcoding of binary QPACK headers (HTTP/3) into the textual HTTP/1.1 format used internally by
  curl's pipeline.
  Specifically, libcurl fails to validate or sanitize header values received from the QUIC stack. If a malicious HTTP/3 server sends a header value containing Carriage Return (\r, 0x0D) and Line Feed (\n, 0x0A) characters, libcurl blindly concatenates them into its internal buffer. This
  buffer is then passed downstream to the client application as a single "header line", wh


## Grafana RCE via SMTP server parameter injection
- 等级：Critical | 项目：Aiven | 披露：2022-11-08 | CVE：-
- 原文：https://hackerone.com/reports/1200647

- - - - - - - - 
## Summary:
This report is similar to [#1180653](https://hackerone.com/reports/1180653), except with different parameter injection entrypoint.
SMTP server password configuration setting accepts new line characters. This can be used to set non-exported configuration variables. Using this CRLF-injection, the `rendering_args` of grafana image renderer can be modified which leads to code execution on the Grafana server.
## Steps To Reproduce:
1.Create Aiven Grafana instance
2.Setup netcat listener on your server: `nc -n -lvp 4444`
3.Send the following request to the grafana instance, replace place holders. The aivenv1 token can be retrieved by inspecting the browser traffic.
4. 


## Protocol Smuggling / CRLF Injection via Gopher Protocol allows Arbitrary Command Injection
- 等级：High | 项目：curl | 披露：2025-12-25 | CVE：-
- 原文：https://hackerone.com/reports/3477023

- - - - - - - - 
Summary:
I have discovered that the Gopher protocol implementation in curl fails to properly sanitize newline characters (%0d%0) in the selector path. This allows an attacker to inject arbitrary TCP commands when curl connects to a target server via gopher://. This vulnerability enables Protocol Smuggling attacks, turning a curl request into a weapon to interact with internal services like Redis, Memcached, or SMTP.
Affected version:
Master branch (Compiled from source on Dec 24, 2025).
Steps To Reproduce:
1. Setup a dummy listener (simulating a victim service like Redis or SMTP):
   $ nc -lvnp 11211
2. Execute the attack using a crafted Gopher URL containing URL-encoded CRL


## 'net/http': HTTP Header Injection in the set_content_type method
- 等级：High | 项目：Ruby | 披露：2022-02-04 | CVE：-
- 原文：https://hackerone.com/reports/1168205

- - - - - - - - 
The set\_content\_type's parameter is not filtered to prevent the injection from altering the entire request.
The vulnerable code:
[code omitted]
# PoC
1.
[code omitted]
2.
[code omitted]
I set the same severity as [CVE-2020-26116](https://nvd.nist.gov/vuln/detail/CVE-2020-26116) has.
## Impact
In web applications a CRLF injection can have severe impacts, depending on what the application does with single items. Impacts can range from information disclosure to code execution, a direct impact web application security vulnerability.
---

