# HackerOne 实战案例：stack-overflow

_12 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Buffer Overflow in cURL Internal printf Function
- 等级：Critical | 项目：curl | 披露：2025-12-12 | CVE：-
- 原文：https://hackerone.com/reports/3462525

- - - - - - - - 
A critical buffer overflow vulnerability exists in the `curl_msprintf()` function in cURL's internal printf implementation. The function writes formatted output to a user-provided buffer without performing any bounds checking, allowing attackers to overflow arbitrary memory and potentially achieve arbitrary code execution.
## Affected Version
Current master branch (commit 141ce4be64) and potentially earlier versions
## CVSS Score Breakdown
**Base Score: 9.8 (Critical)**
- **Attack Vector (AV):** Network (N)
- **Attack Complexity (AC):** Low (L)
- **Privileges Required (PR):** None (N)
- **User Interaction (UI):** None (N)
- **Scope (S):** Unchanged (U)
- **Confidentiality (C


## GoldSrc: Buffer Overflow in DELTA_ParseDelta function leads to RCE
- 等级：Critical | 项目：Valve | 披露：2021-05-04 | CVE：-
- 原文：https://hackerone.com/reports/484745

- - - - - - - - 
## Description
The bug is triggered by 2 packets.
First one is `svc_deltadescription` which describes memory layout of such structures as `event_t`, `weapon_data_t`, ...
It is sent as a list of fields' descriptions: type, offset and others.
Next, `DELTA_ParseDelta` fills these structures when corresponding delta packets are received. The problem is that this function doesn't check if `field_offset + field_size` doesn't exceed bounds of allocated memory for these structures which can lead to buffer overflow.
To actually trigger this overflow we need to send specially crafted delta information. I found that `svc_event` packet is parsed in `ParseEvent` function that allocates `


## Stack Buffer Overflow in cURL Cookie Parsing Leads to RCE
- 等级：High | 项目：curl | 披露：2025-09-16 | CVE：-
- 原文：https://hackerone.com/reports/3340109

- - - - - - - - 
## Summary
I discovered a critical stack-based buffer overflow vulnerability in cURL's cookie parsing mechanism that can lead to remote code execution. The vulnerability occurs when processing maliciously crafted HTTP cookies, affecting all applications that use libcurl for HTTP requests.
## Description
During security research on cURL's cookie handling implementation, I identified a stack buffer overflow in the cookie parsing logic. The vulnerability allows remote attackers to trigger memory corruption by sending oversized cookie data through HTTP responses.


## Stack-based Buffer Overflow in TELNET NEW_ENV Option Handling
- 等级：High | 项目：curl | 披露：2025-06-30 | CVE：-
- 原文：https://hackerone.com/reports/3230082

- - - - - - - - 
**Title:**
Stack-based Buffer Overflow in TELNET NEW_ENV Option Handling
**Vulnerability Description:**
**Summary:**
A stack-based buffer overflow vulnerability exists in the `libcurl` TELNET handler. When `libcurl` connects to a malicious TELNET server, the server can trigger an overflow by sending a `NEW_ENVIRON SEND` request. This causes the client to construct a response that overwrites a fixed-size stack buffer, leading to a crash and potential remote code execution (RCE). The vulnerability can be triggered by a user connecting to a malicious URL using the `curl` command-line tool or any application that uses `libcurl`.
**Root Cause Analysis:**
The vulnerability is loca


## mb_strtolower (UTF-32LE): stack-buffer-overflow at php_unicode_tolower_full (CVE-2020-7065)
- 等级：High | 项目：Internet | 披露：2020-10-21 | CVE：CVE-2020-7065
- 原文：https://hackerone.com/reports/838127

- - - - - - - - 
PHP bug report (made public by the maintainers at the time of writing): https://bugs.php.net/bug.php?id=79371
Mitre CVE page: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-7065
Link to the release notes: https://www.php.net/ChangeLog-7.php#7.4.4
## Impact
One of impacts is that the issue allows an attacker to straightforwardly crash the PHP interpreter provided a specific UTF character can be passed to `mb_strtolower` function dealing with UTF-32LE encoding. 
Original summary from the bug report:
> A call to `mb_strtolower` allows overwriting of a stack-allocated buffer with an overflown array from .rodata.
Description as provided by CVE database entry:
> In PHP ve


## Buffer overflow In hl.exe's launch -game argument allows an attacker to execute arbitrary code locally or from browser
- 等级：High | 项目：Valve | 披露：2020-08-19 | CVE：-
- 原文：https://hackerone.com/reports/832750

- - - - - - - - 
Half Life 1 allows users to set various launch arguments when running the game from the command line, one of them is "**-game**" which specifies the game/mod to be launched. [Documented here](https://developer.valvesoftware.com/wiki/Command_Line_Options#Command-line_parameters_2)
[code omitted]
The contents of this argument is copied via a call to strcpy() onto the stack without any size checking, this results in adjacent memory being overwritten including the stored return address.
This can be tested by parsing an overly long argument to **hl.exe -game <argument>** and easily viewed in **Immunity Debugger** by opening hl.exe and setting the arguments field to -game <overly 


## VLC 4.0.0 - Stack Buffer Overflow (SEH)
- 等级：High | 项目：VLC | 披露：2020-02-10 | CVE：-
- 原文：https://hackerone.com/reports/489102

- - - - - - - - 
**Summary:**
Incorrect calculation of Buffer Size in rist module for VLC leading to Stack Overflow with SEH chain overwrite.
The modules/access/rist module has an incorrect calculation of buffer size giving an attacker the possibility to set the buffer size of a local variable by sending a maliciously crafted RTSP packet and overflowing the variable in a proceeding memcpy operation. 
**Description:**
In the static void rtcp_input(...) function a variable new_sender_name is defined with a maximum size of MAX_CNAME (128 bytes). When reading a RTCP_PT_SDES package the length for the memcpy operation is set by the rtcp_sdes_get_name_length(buf) which is taking the 9-10th bit of 


## Perl $ENV Key Stack Buffer Overflow
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-12814
- 原文：https://hackerone.com/reports/272497

- - - - - - - - 
The CPerlHost::Add method in win32\perlhost.h is vulnerable to a stack buffer overflow.
void
CPerlHost::Add(LPCSTR lpStr)
{
    char szBuffer[1024];
    LPSTR *lpPtr;
    int index, length = strlen(lpStr)+1;
    for(index = 0; lpStr[index] != '\0' && lpStr[index] != '='; ++index)
    szBuffer[index] = lpStr[index];
    szBuffer[index] = '\0';
    [...]
}
The issue exists because the size of lpStr, the key passed in when indexing into $ENV, is not checked before it is copied into szBuffer, a fixed size stack buffer.
The issue can be reproduced on a win32 build with the following script.
print "Starting\r\n";
$ENV{"A" x (0x1000)} = 0;
print "Done\r\n";
In cases where the $ENV 


## Malformed playlist.txt in GoldSrc games leads to Access Violation & arbitrary code execution
- 等级：High | 项目：Valve | 披露：2019-09-17 | CVE：-
- 原文：https://hackerone.com/reports/504951

- - - - - - - - 
A crafted `playlist.txt` can be used to exploit a stack overflow vulnerability in `GameUI.dll` that can lead to arbitrary code execution.
# Reproduction
Place attached `playlist.txt` in game directory (`valve`, `cstrike`, etc.). The game will crash when it tries to play `Splash` track.
# Exploitability
The file can be sent from server with `precache_generic` function (custom `mp.dll`, amxx plugins, etc.). I don't know ant way to force reload the playlist, so for the exploit to trigger, the client must be restarted. In my opinion, it's still dangerous. And this method won't work if the client already had `playlist.txt` in the game directory.
## Impact
The attacker can use thi


## Stack overflow in XML Parsing
- 等级：High | 项目：Notepad++ | 披露：2019-08-25 | CVE：-
- 原文：https://hackerone.com/reports/480883

- - - - - - - - 
**Summary:** 
A stack buffer overflow vulnerability has been detected in XML parsing functionality  on Notepad++.
That's due to the fact that _invisibleEditView.getText function doesn't check buffer boundaries.
**Description:** 
Vulnerability src file: notepad-plus-plus/PowerEditor/src/Notepad_plus.cpp
Vulnerability line: line 1008
Variable affected: char encodingStr[128];
Function that overflows buffer: _invisibleEditView.getText
## Steps To Reproduce:
  1. Create a .xml file with a correct XML format
  2. Introduce a big XML field that overflows "encodingStr" buffer.
  3. Open the file with Notepad++ and application should crash.
## Supporting Material/References:
  * BoF_


## Stack overflow in UnbindFromTree (browser can be crashed remotely)
- 等级：High | 项目：Tor | 披露：2017-10-02 | CVE：-
- 原文：https://hackerone.com/reports/264481

- - - - - - - - 
I reported this bug to Mozilla approximately [9 months ago](https://bugzilla.mozilla.org/show_bug.cgi?id=1322307) and all versions of Firefox back to at least ESR45 and including current Nightly 57 builds are still vulnerable to this unpatched flaw. I've tested on Fedora 26, Debian 8, Windows 8 and Windows 10. Mozilla declined to award a bounty. 
Code:
[code omitted]
The caveat to this is that if scripts are disabled on the page where this code is located, the Tor browser won't crash. [This link](https://bugzilla.mozilla.org/attachment.cgi?id=8817075) will probably crash your Firefox. A WinDBG stack trace is located [here](https://bugzilla.mozilla.org/attachment.cgi?id=88171


## mirb only: stack-buffer-overflow (OOB write) in main()
- 等级：High | 项目：shopify-scripts | 披露：2017-05-09 | CVE：-
- 原文：https://hackerone.com/reports/219870

- - - - - - - - 
Triggered in `7e28510` (7 April 2017) with `mirb` only.
`cat test013.rb | mirb`
[code omitted]
---

