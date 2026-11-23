# HackerOne 实战案例：execution-with-unnecessary-privileges

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## One Click Code Execution via File
- 等级：High | 项目：Evernote | 披露：2020-03-24 | CVE：CVE-2019-17051
- 原文：https://hackerone.com/reports/822609

- - - - - - - - 
This issue was reported to Evernote by @ajdumanhug and fixed in November 2019. This disclosure is a copy of the original, and is for historical purposes only.
## Overview
The Open with Terminal functional is vulnerable to One Click Code Execution. Tested the vulnerability using the Mac Desktop App version Mac 7.13 and below.
It happens because they don't add com.apple.quarantine meta-attribute for downloaded files to avoid the execution of terminal files.
I already reported this to Evernote, and I just wanted to report it here to ask for disclosure.
## Proof of Concept
https://www.youtube.com/watch?v=OG2tKlZX5bg&feature=youtu.be
## Supporting Material/References:
https://dis

