# HackerOne 实战案例：exposure-of-data-element-to-wrong-session

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## State Isolation Failure in Multiplexed Connections (Shared Auth Context)
- 等级：Critical | 项目：curl | 披露：2026-01-08 | CVE：-
- 原文：https://hackerone.com/reports/3487952

- - - - - - - - 
Vulnerability: State Isolation Failure in Multiplexed Connections (Shared Auth Context) Product: libcurl Affected Versions: v7.43.0 - Current (v8.x) - All versions supporting HTTP/2 Multiplexing Severity: CRITICAL (CVSS: 9.1)
1. Executive Summary
A fundamental design flaw exists in libcurl's state management for HTTP/2 multiplexed connections. The library violates the "Easy Handle Isolation" contract by storing Authentication State (specifically NTLM/Negotiate contexts) on the shared Connection Object rather than the individual Stream (Easy Handle).
This violation allows a secondary, unauthenticated Easy Handle ("Attacker Stream") to effectively "inherit" the authentication 

