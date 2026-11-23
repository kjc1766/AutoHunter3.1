# HackerOne 实战案例：type-confusion

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Incorrect Type Conversion in interpreting IPv4-mapped IPv6 addresses and below `curl` results in indeterminate SSRF vulnerabilities.
- 等级：Critical | 项目：curl | 披露：2024-05-08 | CVE：CVE-2023-24329,
- 原文：https://hackerone.com/reports/2493548

- - - - - - - - 
## Summary:
Octal Type Handling of Errors in IPv4 Mapped IPv6 Addresses in curl  allows unauthenticated remote attackers to perform indeterminate SSRF, RFI, and LFI attacks on many programs that rely on curl. 
[RFC 4291](https://datatracker.ietf.org/doc/html/rfc4291#section-2-5-5) defines ways to embed an IPv4 address into IPv6 addresses. One of the methods defined in the RFC is to use IPv4-mapped IPv6 addresses, that have the following format:
[code omitted]
In IPv6 notation, the corresponding mapping for `127.0.0.1` is `::ffff:127.0.0.1` ([RFC 4038](https://datatracker.ietf.org/doc/html/rfc4038)). Although curl correctly converts octal numbers starting with 0 in IPv4 forma


## Insufficient Type Check leading to Developer ability to delete Project, Repository, Group, ...
- 等级：High | 项目：GitLab | 披露：2020-11-02 | CVE：-
- 原文：https://hackerone.com/reports/960244

- - - - - - - -

