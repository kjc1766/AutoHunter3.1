# HackerOne 实战案例：allocation-of-resources-without-limits-or-throttling

_3 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## HTTP/2 CONTINUATION Flood Vulnerability
- 等级：High | 项目：curl | 披露：2025-06-28 | CVE：CVE-2023-44487
- 原文：https://hackerone.com/reports/3125820

- - - - - - - - 
# **0x00 Vulnerability Overview: Fatal Flaw in HTTP/2 Protocol Stack**
## **1. HTTP/2 Header Block Fragmentation Mechanism**
* **RFC 7540 Specification**:
  * Header blocks are transmitted using a HEADERS frame followed by one or more CONTINUATION frames.
  * All frames must belong to the **same stream** and be sent **sequentially**.
## **2. libcurl Vulnerability**
[code omitted]


## Memory Leak in libcurl via Location Header Handling (CWE-770)
- 等级：High | 项目：curl | 披露：2025-05-22 | CVE：-
- 原文：https://hackerone.com/reports/3158093

- - - - - - - - 
## Summary:
This report details a memory leak vulnerability in libcurl that occurs when processing HTTP 3xx redirect responses containing a `Location:` header. Specifically, the memory allocated for the `Location:` header's value is not properly deallocated when the `Curl_easy` handle is reused for subsequent requests (e.g., when following redirects or in long-running applications that frequently reuse handles). This leads to a gradual increase in memory consumption, potentially resulting in a Denial of Service (DoS) due to resource exhaustion.


## Prototype pollution attack (lodash)
- 等级：High | 项目：Node.js | 披露：2020-04-27 | CVE：CVE-2020-8203
- 原文：https://hackerone.com/reports/712065

- - - - - - - - 
I would like to report a prototype pollution vulnerability in lodash.
It allows an attacker to inject properties on Object.prototype
Module
module name: lodash
version: 4.17.15
npm page: https://www.npmjs.com/package/lodash
Module Description
The Lodash library exported as Node.js modules.
Module Stats
25,228,177 downloads in the last week
Vulnerability
Vulnerability Description
This is a similar with this vulnerability: https://hackerone.com/reports/380873
The functions merge, mergeWith, and defaultsDeep can be tricked into adding or modifying properties of the Object prototype. These properties will be present on all objects.
Steps To Reproduce:
Craft an object by "zipObje

