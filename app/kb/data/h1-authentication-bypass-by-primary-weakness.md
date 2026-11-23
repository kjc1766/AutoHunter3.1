# HackerOne 实战案例：authentication-bypass-by-primary-weakness

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Missing server identity policy enforcement in SSH connection reuse allows host key verification bypass via pool poisoning
- 等级：High | 项目：curl | 披露：2026-04-03 | CVE：CVE-2022-27782,
- 原文：https://hackerone.com/reports/3640932

- - - - - - - - 
# Missing server identity policy enforcement in SSH connection reuse allows host key verification bypass via pool poisoning
---
## Summary
`ssh_config_matches()` in `lib/url.c` decides whether an existing SSH connection can be reused by a new transfer handle. It checks client key paths (`rsa`, `rsa_pub`) but never inspects the three options that control server identity verification: `STRING_SSH_KNOWNHOSTS`, `STRING_SSH_HOST_PUBLIC_KEY_MD5`, and `STRING_SSH_HOST_PUBLIC_KEY_SHA256`. A handle configured with strict host key pinning reuses a pooled connection that was established with zero server verification — the pinning check never fires because the SSH handshake is skipped e


## Incorrect Parsing of IPv6 Zone ID in curl
- 等级：High | 项目：curl | 披露：2025-09-01 | CVE：-
- 原文：https://hackerone.com/reports/3319767

- - - - - - - - 
I'm Zehui Miao from NISL@THU. During recent research, our team identified a parsing inconsistency in the curl.

