# HackerOne 实战案例：classic-buffer-overflow

_27 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Buffer Overflow Vulnerability in strcpy() Leading to Remote Code Execution
- 等级：Critical | 项目：curl | 披露：2024-12-02 | CVE：-
- 原文：https://hackerone.com/reports/2871792

- - - - - - - - 
## Summary:
The vulnerability in the program arises from a classic buffer overflow, triggered by the unsafe use of the strcpy() function without bounds checking. The program copies data from a source buffer to a destination buffer, allowing attackers to overflow the buffer if the input string exceeds the buffer's allocated size. This vulnerability can lead to the overwriting of critical memory, such as the return address on the stack, enabling arbitrary code execution and control over the system. The vulnerability is caused by the unsafe use of strcpy(), which does not check the length of the input string before copying it into the buffer. When the input exceeds the buffer s


## Buffer overflow and affected url:-https://github.com/curl/curl/blob/master/docs/examples/hsts-preload.c
- 等级：Critical | 项目：curl | 披露：2023-11-15 | CVE：-
- 原文：https://hackerone.com/reports/2252307

- - - - - - - - 
## Summary:
A buffer overflow, also known as a buffer overrun, occurs when a program or process attempts to write more data to a buffer than the buffer is allocated to hold. This can happen if the program does not properly check the length of the data before writing it to the buffer, or if the program allocates too little space for the buffer.
## Steps To Reproduce:
[add details for how we can reproduce the issue]
1. The hstsread function in the provided code does not properly check the length of the host string before copying it into the e->name buffer. This could lead to a buffer overflow, allowing an attacker to inject arbitrary code into the application.this could exploi


## Buffer overrun in Steam SILK voice decoder
- 等级：Critical | 项目：Valve | 披露：2021-09-13 | CVE：-
- 原文：https://hackerone.com/reports/1180252

- - - - - - - - 
#Vulnerability
The SteamWorks SDK has a function available named [DecompressVoice()](https://partner.steamgames.com/doc/api/ISteamUser#DecompressVoice), which takes as input some compressed voice data, and returns the raw audio data.
The format for the input voice data is as follows:
[code omitted]
There are numerous payload types available, including Opus PLC, Opus, SILK, Raw and Silence. The bug being considered here is specific to the SILK decoder.
The pseudo-code for the SILK decoder is:
[code omitted]
Some important things to note:
 - At `[1]`, a bounds check is performed to ensure we don't read outside the bounds of the input buffer
 - At `[2]`, a bounds check is perfo


## UrnState Heap Overflow
- 等级：Critical | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-12526
- 原文：https://hackerone.com/reports/824771

- - - - - - - - 
## Summary:
When handling a URN Request an attacker controlled response can  cause Squid to overflow a heap buffer. The buffer exist within a struct so not only does it allow an attacker to overflow adjacent memory, but also control a pointer that follows the buffer enabling them to free arbitrary memory. Paired with the Cache Manager bypass that I reported earlier, an attacker will know which addresses are valid. This can lead to RCE and was stated in the serverity of the Squid announce. 
Squid Announce: http://www.squid-cache.org/Advisories/SQUID-2019_7.txt
Assigned CVE-2019-12526
## Steps To Reproduce:
You must add the following to your squid.conf to allow URN request
[co


## Squid as reverse proxy RCE and data leak
- 等级：Critical | 项目：Internet | 披露：2021-08-26 | CVE：-
- 原文：https://hackerone.com/reports/778610

- - - - - - - - 
## Summary:
This was a very difficult experience as Squid maintainers took a long time to answer. I tried getting help from HackerOne support, Dropbox support and the Internet Bug Bounty (never e-mailed me back) to no avail. What could have taken a few days took months.
The vulnerability concerns a stack buffer overflow (write) in parsing of the Host header if Squid acts as a reverse proxy.
The bug is fixed in Squid 4.10 released on 20 Jan 2020 which can be found here: http://www.squid-cache.org/Versions/v4/
## Steps To Reproduce:
[code omitted]
Create a file [code omitted] with this contents. This is based on the instructions at https://wiki.squid-cache.org/ConfigExamples/R


## Several protocol parsers in before 4.9.2 could cause a buffer overflow in util-print.c:bittok2str_internal()
- 等级：Critical | 项目：Internet | 披露：2021-08-22 | CVE：-
- 原文：https://hackerone.com/reports/800324

- - - - - - - - 
Length of a local buffer used to parse network packets was not validated against actual payload size leading to a classic buffer overflow.
P.S. I was not aware of this bounty program at the time of reporting. Is this report in scope? I have a few more reports that were originally sent to the tcpdump security mailing list, I could file a report for each of them here if that qualifies. I may have also helped fix some issues in 4.9.3 as well.
## Impact
I believe remote DoS is possible. Remote code execution remains a possibility but I have not checked this myself.
---


## Specially Crafted Closed Captions File can lead to Remote Code Execution in CS:GO and other Source Games
- 等级：Critical | 项目：Valve | 披露：2021-05-05 | CVE：-
- 原文：https://hackerone.com/reports/463286

- - - - - - - - 
With a specially crafted closed captions file, the parser calls CHudCloseCaption::GetNoRepeatValue which in turn calls CHudCloseCaption::SplitCommand which has no boundary checks allowing the on stack variables cmd and args to be overflowed which in turn allows Remote Code Execution.
**Summary (researcher):**
Buffer overflow via the closed captioning system in the function `CHudCloseCaption::SplitCommand` which can be reached via the function `CHudCloseCaption::GetNoRepeatValue`
[code omitted]
---


## Uninitialized read in exif_process_IFD_in_TIFF
- 等级：Critical | 项目：Internet | 披露：2020-10-10 | CVE：CVE-2019-9641
- 原文：https://hackerone.com/reports/510336

- - - - - - - - 
This bug can be reproduced only in 32 bit PHP builds.
This bug is present in exif_process_IFD_in_TIFF method of ext/exif/exif.c file.
Detailed description and steps to reproduce for this bug is present in bug report submitted to php.net.
Bug Report : https://bugs.php.net/bug.php?id=77509
PHP version : 7.1.26
CVE-ID : 2019-9641
## Impact
Uninitialized variables may leak data from memory.
---


## Malformed NAV file leads to buffer overflow and code execution in Left4Dead2.exe
- 等级：Critical | 项目：Valve | 披露：2020-03-25 | CVE：-
- 原文：https://hackerone.com/reports/542180

- - - - - - - - 
## Summary
In the parsing routines of NAV files (which contain the navigation mesh used by the AI for survivor bots, zombies, and the AI director spawning system) a buffer overflow exists which can be used to control the EIP register and takeover code execution. 
## Proof-of-Concept
1. Download the attached c1m1_hotel.nav
2. Place it in your *<steamapps>/Left 4 Dead 2/left4dead2/maps/* directory
3. Start up Left4Dead 2 and attach a debugger
4. Enter "map c1m1_hotel" into the developer console
5. Observe that EIP becomes 0x41414102, indicating that a buffer overflow has occurred and code execution is possible
## Operating Systems Tested
- Windows 10 1809 Build 17763.437
I hav


## RCE on Steam Client via buffer overflow in Server Info
- 等级：Critical | 项目：Valve | 披露：2019-03-15 | CVE：-
- 原文：https://hackerone.com/reports/470520

- - - - - - - - 
## Introduction
In Steam and other valve games (CSGO, Half-Life, TF2) there is a functionality to find game servers called the server browser. In order to retrieve the information about these servers the server browser communicates with a specific UDP protocol called [server queries](https://developer.valvesoftware.com/wiki/Server_queries). The protocol is well described in the online developers manual of Steam. We implemented a custom python server which only replies with the protocol using the same information available in the documentation. After a successful implementation of the protocol we fuzzed several parameters and noticed that the Steam client crashed when receivi


## Malformed .BSP Access Violation in CS:GO can lead to Remote Code Execution
- 等级：Critical | 项目：Valve | 披露：2018-07-19 | CVE：-
- 原文：https://hackerone.com/reports/351014

- - - - - - - - 
A malformed .BSP can trigger an Access Violation on CS:GO that can lead to arbitrary code execution on a remote computer. I have attached a copy of the malformed .BSP which reliably triggers an Access Violation on CS:GO.
## Impact
An attacker hosting a malicious server could compromise a remote client by having them download a custom map, triggering remote code execution on the victim's computer.
---


## Stack Buffer Overflow in mprintf.c formatting function (fallback path)
- 等级：High | 项目：curl | 披露：2026-01-08 | CVE：-
- 原文：https://hackerone.com/reports/3493602

- - - - - - - -


## Buffer Overflow in WebSocket Handshake (lib/ws.c:1287)
- 等级：High | 项目：curl | 披露：2025-10-21 | CVE：-
- 原文：https://hackerone.com/reports/3392174

- - - - - - - - 
## Summary:
Buffer overflow vulnerability in curl's WebSocket implementation due to unsafe use of strcpy() in the handshake process. The vulnerability is located at lib/ws.c:1287 where strcpy(keyval, randstr) is called without proper bounds checking, despite having a bounds check earlier in the code.
**AI DISCLOSURE**: This vulnerability analysis was conducted with AI assistance. All technical details, code analysis, and exploit development were verified through manual testing and code review. The vulnerability exists in the actual curl source code and has been demonstrated with working proof of concept.
## Affected version
curl version: curl 8.7.1 (x86_64-apple-darwin25.0) 


## Multiple Unsafe strcpy() Function Calls Leading to Potential Buffer Overflow Vulnerabilities in cURL 8.16.1-DEV
- 等级：High | 项目：curl | 披露：2025-09-14 | CVE：-
- 原文：https://hackerone.com/reports/3337561

- - - - - - - - 
## Summary:
During a comprehensive security audit of the cURL codebase, multiple instances of unsafe strcpy() function usage were identified in critical code paths. These implementations violate secure coding practices and represent latent security risks that could lead to buffer overflow vulnerabilities under specific conditions. While existing bounds checking prevents immediate exploitation in standard scenarios, the presence of these unsafe functions creates potential attack vectors that require immediate remediation.
Affected Components:
WebSocket protocol implementation (lib/ws.c:1261)
SSL/TLS backend management (lib/vtls/vtls.c:1066)
WolfSSL error handling (lib/vtls/wo


## Buffer Overflow Risk in Curl_inet_ntop and inet_ntop4
- 等级：High | 项目：curl | 披露：2024-12-08 | CVE：-
- 原文：https://hackerone.com/reports/2887487

- - - - - - - - 
*Curl is a software that I love and is an important tool for the world. *
*If my report doesn't align, I apologize for that.*
The `Curl_inet_ntop` function is designed to convert IP addresses from binary format to human-readable string format, supporting both IPv4 and IPv6. It internally delegates to `inet_ntop4` for IPv4 addresses and `inet_ntop6` for IPv6 addresses. However, insufficient validation of buffer size (`buf`) in these functions exposes the implementation to **buffer overflow risks**, which can lead to undefined behavior, application crashes, or security vulnerabilities.
This report analyzes vulnerabilities in both `Curl_inet_ntop` and `inet_ntop4`, demonstrates


## Remote vulnerabilities in spp
- 等级：High | 项目：PlayStation | 披露：2024-04-25 | CVE：CVE-2006-4304
- 原文：https://hackerone.com/reports/2177925

- - - - - - - - 
## Summary
A malicious PPPoE server can cause denial-of-service or potentially remote code execution in kernel context on the PS4/PS5.
## Heap buffer overwrite and overread in sppp_lcp_RCR and sppp_ipcp_RCR
For some reason, the PS4/PS5 is vulnerable to [CVE-2006-4304](https://www.freebsd.org/security/advisories/FreeBSD-SA-06:18.ppp.asc). By having invalid options, it is possible to cause a heap buffer overwrite and overread.
[code omitted]
Namely, at [1] the length of `p[1]` is not validated to be smaller or equal to `len`. As such, at [2] the call `bcopy()` will copy with a size potentially larger than both the source and the destination.
Furthermore, at [3] the return leng


## Use of Unsafe function || Strcpy
- 等级：High | 项目：curl | 披露：2022-03-09 | CVE：-
- 原文：https://hackerone.com/reports/1485379

- - - - - - - - 
## Summary:
It was observed that application is using strcpy() function which may cause buffer overflow attacks.
#Affected Code
https://github.com/curl/curl
# Affected Lines
1. Line 195 of curl-master\tests\libtest\stub_gssapi.c
2. Line 204,212,216 curl-master\tests\server\socksd.c
## Steps To Reproduce:
Lets first discuss what is the issue with strcpy function. basically it takes 2 arguments 1 dst 2 source. the issue is if the dst size is small and the source size is more without a null terminating value so it will overwrite the memory. so in these case 1 got the several lines about strcpy function. but i'm discussing 1 with you rest with remain the same.
        else if(!s


## CVE-2021-3711: SM2 decrypt  buffer overflow
- 等级：High | 项目：Internet | 披露：2021-09-27 | CVE：CVE-2021-3711
- 原文：https://hackerone.com/reports/1352429

- - - - - - - - 
CVE-2021-3711
In order to decrypt SM2 encrypted data an application is expected to call the API function EVP_PKEY_decrypt(). Typically an application will call this function twice. The first time, on entry, the "out" parameter can be NULL and, on exit, the "outlen" parameter is populated with the buffer size required to hold the decrypted plaintext. The application can then allocate a sufficiently sized buffer and call EVP_PKEY_decrypt() again, but this time passing a non-NULL value for the "out" parameter. A bug in the implementation of the SM2 decryption code means that the calculation of the buffer size required to hold the plaintext returned by the first call to EVP_PKEY


## Buffer overflow in PyCArg_repr in _ctypes/callproc.c for Python 3.x to 3.9.1
- 等级：High | 项目：Internet | 披露：2021-08-25 | CVE：CVE-2021-3177
- 原文：https://hackerone.com/reports/1084342

- - - - - - - - 
**TL;DR Description**
Python 3.x through 3.9.1 has a buffer overflow in PyCArg_repr in _ctypes/callproc.c, which may lead to remote code execution in certain Python applications that accept floating-point numbers as untrusted input, as demonstrated by a 1e300 argument to c_double.from_param. This occurs because sprintf is used unsafely. The CVE number used for this vulnerability is CVE-2021-3177.
**Details**
There's a buffer overflow in the PyCArg_repr() function in _ctypes/callproc.c.
The buffer overflow happens due to not checking the length of th sprintf() function on line: 
    case 'd':
        sprintf(buffer, "<cparam '%c' (%f)>",
            self->tag, self->value.d);


## Buffer Overflow in ext_lm_group_acl helper
- 等级：High | 项目：Internet | 披露：2021-07-28 | CVE：CVE-2020-8517
- 原文：https://hackerone.com/reports/789034

- - - - - - - - 
## Summary
Due to incorrect buffer management ext_lm_group_acl is vulnerable to a denial of service attack when processing NTLM Authentication credentials. This problem is limited to installations using the
ext_lm_group_acl binary.
## Affected Versions
Squid 2.x -> 2.7.STABLE9
Squid 3.x -> 3.5.28
Squid 4.x -> 4.9
## Severity 
Due to incorrect input validation the NTLM authentication credentials parser in ext_lm_group_acl may write to memory outside the credentials buffer. On systems with memory access protections this can result in the helper process being terminated unexpectedly. Resulting in the Squid process also terminating and a denial of service for all clients using t


## Android App Crashes while sending message to users/ on channel
- 等级：High | 项目：Rocket.Chat | 披露：2021-03-18 | CVE：-
- 原文：https://hackerone.com/reports/832217

- - - - - - - - 
## Description
 I found a security vulnerability in Rocket's latest android app by which I was able to remotely crash any  user’s app  instantly just by just sending a simple message in private or in channel. The vulnerability  require the victim open the message. 
## Devices and Versions
Rocket.Chat.Android version: (e.g. 4.5.1)
Mobile device model and OS version: (tested on :+1: -- " **Android 6.0, 8.0, 10.0**"), probably any other android version
## Steps to reproduce
> Create new #test channel
> Send POC Code onto the channel
> Open Mobile App
> App gets crashed
## POC


## phar_tar_writeheaders_int() buffer overflow
- 等级：High | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-9675
- 原文：https://hackerone.com/reports/504761

- - - - - - - - 
A buffer overflow has been found in the phar_tar_writeheaders_int() function.
it does a strncpy to header->linkname from entry->link with the size of entry->link.
As you can see in https://github.com/php/php-src/blob/master/ext/phar/tar.h#L66 , header->linkname is a char of the size 100. Once entry->link contains a value that's bigger than 100 it will overflow the _tar_header structure.
This can be fixed by setting the size argument of strncpy to sizeof(header->linkname) for example:
strncpy(header.linkname, entry->link, strlen(header->linkname);
This has been fixed in the following references:
https://github.com/php/php-src/commit/071e18c6971c4cf64297378b30b945a1b85d682a
ht


## Malformed BSP in GoldSrc Engine may cause shellcode injection
- 等级：High | 项目：Valve | 披露：2020-03-25 | CVE：-
- 原文：https://hackerone.com/reports/458929

- - - - - - - -


## Malformed .BMP file in Counter-Strike 1.6 may cause shellcode injection
- 等级：High | 项目：Valve | 披露：2020-02-27 | CVE：-
- 原文：https://hackerone.com/reports/397545

- - - - - - - - 
With the vulnerability of the GoldSource Engine, the server is able to perform remote code execution on the client, overwriting the stack when reading the BMP file. The problem is in the LoadBMP8 function, which is executed when the player connects to the server, by loading the "overviews\%MAPNAME%.bmp" file. If we send a badly formed file to this function, then we will be able to rewrite the stack of the function by setting the own code in the stack and passing program control to it.
I've wrote a program that compiles file like that. The shellcode, which runs on the stack, starts the "calc.exe" process with the WinExec function.
For the client to execute this file, the serv


## CVE-2017-13089 wget stack smash
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-13089
- 原文：https://hackerone.com/reports/287666

- - - - - - - - 
The http.c:skip_short_body() function is called in some circumstances, such as when processing redirects. When the response is sent chunked in wget before 1.19.2, the chunk parser uses strtol() to read each chunk's length, but doesn't check that the chunk length is a non-negative number. The code then tries to skip the chunk in pieces of 512 bytes by using the MIN() macro, but ends up passing the negative chunk length to connect.c:fd_read(). As fd_read() takes an int argument, the high 32 bits of the chunk length are discarded, leaving fd_read() with a completely attacker controlled length argument.
Reproduction:
To reproduce, use two terminals.  In the first terminal:
$ nc 


## CVE-2017-13090 wget heap smash
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-13090
- 原文：https://hackerone.com/reports/287667

- - - - - - - - 
The retr.c:fd_read_body() function is called when processing OK responses. When the response is sent chunked in wget before 1.19.2, the chunk parser uses strtol() to read each chunk's length, but doesn't check that the chunk length is a non-negative number. The code then tries to read the chunk in pieces of 8192 bytes by using the MIN() macro, but ends up passing the negative chunk length to retr.c:fd_read(). As fd_read() takes an int argument, the high 32 bits of the chunk length are discarded, leaving fd_read() with a completely attacker controlled length argument. The attacker can corrupt malloc metadata after the allocated buffer.
Reproduction
To reproduce, use two termi


## Malformed Skybox .TGA in Half-Life (GoldSRC) leads to Access Violation
- 等级：High | 项目：Valve | 披露：2018-08-28 | CVE：-
- 原文：https://hackerone.com/reports/351016

- - - - - - - - 
A malformed .TGA when loaded as a Skybox on a map in a GoldSRC engine game (Half-Life) can lead to arbitrary code execution on a remote client.
###Reproduction Steps
Load the attached map + resources on a local Half-Life listen server. The game will crash with an Access Violation as soon as the map with the malicious skybox is loaded.
###Exploitability
Since anyone can host a map with custom assets, and the custom assets are loaded onto a remote clients computer, a malicious server can distribute malformed skybox assets (.TGA's) that could cause remote code execution on clients. The inclusion of .DLL's on Steam without ASLR make exploitablility of this bug via ROP quite triv

