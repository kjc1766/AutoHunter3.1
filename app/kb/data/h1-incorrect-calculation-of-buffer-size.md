# HackerOne 实战案例：incorrect-calculation-of-buffer-size

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Zip bomb
- 等级：Critical | 项目：Tor | 披露：2023-11-28 | CVE：-
- 原文：https://hackerone.com/reports/263663

- - - - - - - - 
Hi, if you go to this site https://blog.haschek.at/tools/bomb.php
 from Tor Browser, the Tor browser hangs along with the system.
---


## size_t-to-int vulnerability in exFAT leads to memory corruption via malformed USB flash drives
- 等级：High | 项目：PlayStation | 披露：2022-09-21 | CVE：-
- 原文：https://hackerone.com/reports/1340942

- - - - - - - - 
## Summary
A heap-based buffer overflow can be triggered by a malformed exFAT USB flash drive. 
## Vulnerability
The vulnerability is in Sony's exFAT implementation where there is an integer truncation from 64bit to 32bit on a size variable that is used to allocate the up-case table:
[code omitted]
Namely, `dataLength` and `size` are both 64bit wide, however the `size` argument of `sceFatfsCreateHeapVl()` is 32bit wide:
[code omitted]
When using a big size for `dataLength`, this function will therefore only allocate a small buffer, and as a result overflow and corrupt subsequent objects on the heap when calling `UVFAT_ReadDevice()`.
For example, using `sectorSize=0x200` and 

