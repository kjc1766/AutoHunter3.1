# HackerOne 实战案例：array-index-underflow

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Signedness issue in ClassInfo message handler leads to RCE on CS:GO client
- 等级：Critical | 项目：Valve | 披露：2021-05-27 | CVE：-
- 原文：https://hackerone.com/reports/876719

- - - - - - - - 
Title:         Signedness issue in ClassInfo message handler leads to RCE on CS:GO client
Scope:         csgo.exe
Weakness:      Array Index Underflow
Severity:      Critical (9.6)
Link:          https://hackerone.com/reports/876719
Date:          2020-05-17 20:31:35 +0000
By:            @chaynik
Details:
Vulnerability
-------------
`CSVCMsg_ClassInfo` message is used by Source Engine to pass information about entity classes. It is described by the following Protobuf:
[code omitted]
The bug is present in `CSVCMsg_ClassInfo` message handler on client. The pseudocode of function that handles this message:
[code omitted]
An array of appropriate size is allocated to hold the rec


## https://██████ vulnerable to CVE-2020-3187 - Unauthenticated arbitrary file deletion in Cisco ASA/FTD
- 等级：Critical | 项目：U.S. | 披露：2020-10-16 | CVE：CVE-2020-3187
- 原文：https://hackerone.com/reports/987090

- - - - - - - - 
Hi team , while testing i found a host ip https://█████████ which belong to DoD (██████████.mil) running web services interface of Cisco ASA/FTD and it is vulnerable to CVE-2020-3187 - Unauthenticated arbitrary file deletion in Cisco ASA/FTD. An attacker could exploit this vulnerability by sending a crafted HTTP request containing directory traversal character sequences. An exploit could allow the attacker to view or delete arbitrary files on the targeted system. When the device is reloaded after exploitation of this vulnerability, any files that were deleted are restored. The attacker can only view and delete files within the web services file system.
Vulnerable IP : https:


## Unchecked weapon id in WeaponList message parser on client leads to RCE
- 等级：Critical | 项目：Valve | 披露：2019-09-17 | CVE：-
- 原文：https://hackerone.com/reports/513154

- - - - - - - - 
Let's look at WeaponList message parser code in the HLSDK:
[code omitted]
And `WeaponResource::AddWeapon`:
[code omitted]
There are no boundary check, and the range of `iId` is `[-128, 128)`, so I can modify many things in the data section.
In `client.dll`, there's an object called `gEngfuncs`, it is a function table that has various functions of the engine. After some calculations on latest CS 1.6 `client.dll`, I concluded that this function table could be overwritten using the above bug.
I have attached a PoC that will pop `calc.exe` on latest CS 1.6 client when connected to malicious server. The AMXX plugin will catch `InitHUD` message, and send crafted `WeaponList` messa


## Your page has 2 blocking CSS resources. This causes a delay in rendering your page.
- 等级：Critical | 项目：Node.js | 披露：2018-07-15 | CVE：-
- 原文：https://hackerone.com/reports/365968

- - - - - - - - 
This report was not deemed to be a security vulnerability and the reporter was asked to open an issue upstream to fix publicly.
---


## Array Index Underflow--http rpc
- 等级：High | 项目：Monero | 披露：2021-10-11 | CVE：-
- 原文：https://hackerone.com/reports/825091

- - - - - - - - 
## Summary:
parserse_base_utils.h:197
const unsigned char tmp = isx[(int)*++it];
Int type will cause the array subscript to appear negative and read wrong data, 
Solution:
const unsigned char tmp = isx[(unsigned char)*++it];
## Releases Affected:
  * up to date version on github
## Steps To Reproduce:
[add details for how we can reproduce the issue]
\#include <iostream>
\#include "serialization/keyvalue_serialization.h"
\#include "storages/portable_storage_template_helper.h"
\#include "storages/portable_storage_base.h"
\#ifdef __cplusplus
extern "C"
\#endif
int LLVMFuzzerTestOneInput(const char *data, size_t size) {
  std::string s(data,size);
  try
  {
    epee::serializati

