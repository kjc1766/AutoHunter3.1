# HackerOne 实战案例：time-of-check-time-of-use-toctou-race-condition

_3 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Ability to bypass partner email confirmation to take over any store given an employee email
- 等级：Critical | 项目：Shopify | 披露：2018-02-07 | CVE：-
- 原文：https://hackerone.com/reports/300305

- - - - - - - - 
I told Pete I would take a look at Spotify, hi Pete.
**Summary**
It's possible to take over any store account through partners given an employee email address. This is possible because I found a way to confirm arbitrary emails. I don't know the Shopify ecosystem well enough to know the other ramifications of such a bug.
On #270981 you wrote:
> The intention was that, when a partner already had a valid user account on the store, their collaborator account request could be accepted automatically, with the user account converted into a collaborator account.
I tested that functionality and confirmed how it works. I realized that if you can somehow create a partner account with a


## TOCTOU Race Condition in HTTP/2 Connection Reuse Leads to Certificate Validation Bypass
- 等级：High | 项目：curl | 披露：2025-09-11 | CVE：-
- 原文：https://hackerone.com/reports/3335085

- - - - - - - - 
I've discovered a Time-of-Check to Time-of-Use (TOCTOU) vulnerability in how `libcurl` handles persistent HTTP/2 connections. During the initial handshake, `libcurl` correctly validates the server's certificate against the user-provided CA bundle. However, it then assumes this trust is permanent for the entire life of the connection.
If an attacker can modify the CA file on disk *after* this initial check, `libcurl` will continue to reuse the now-trusted connection for new HTTP/2 streams without ever re-validating its trust anchor. This allows an attacker to completely bypass certificate validation for all subsequent requests, enabling a full Man-in-the-Middle attack.
**Affe


## Time-of-check to time-of-use vulnerability in the std::fs::remove_dir_all() function of the Rust standard library
- 等级：High | 项目：Internet | 披露：2022-03-24 | CVE：CVE-2022-21658
- 原文：https://hackerone.com/reports/1520931

- - - - - - - - 
The implementation of [`std::fs::remove_dir_all()`](https://doc.rust-lang.org/std/fs/fn.remove_dir_all.html) in the Rust standard library is vulnerable to a time-of-check to time-of-use link replacement attack. This applies to all versions of Rust before 1.58.1.

