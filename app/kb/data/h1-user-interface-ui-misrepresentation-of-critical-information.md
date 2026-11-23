# HackerOne 实战案例：user-interface-ui-misrepresentation-of-critical-information

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Incorrect security UI of files' download source on brave MacOS
- 等级：High | 项目：Brave | 披露：2025-01-16 | CVE：CVE-2025-23086
- 原文：https://hackerone.com/reports/2888770

- - - - - - - - 
## Summary:
This vulnerability involves the incorrect display of the download source in the Brave download alert. Instead of displaying the actual source of the downloaded file, the browser displays the referrer header value, which may mislead the user into believing that the file is from a trusted source. This behavior creates a potential security risk as it could allow attackers to trick users into downloading malicious files.
## Products affected: 
Brave is up to date
Version 1.73.97 Chromium: 131.0.6778.108 (Official Build) (arm64)
## Steps To Reproduce:
1. Victim visit: https://ybt01.github.io/upload/google.html#
2. Victim click `click me to download google apk` and wil


## Mailsploit: a sender spoofing bug in over 30 email clients
- 等级：High | 项目：Internet | 披露：2019-09-19 | CVE：-
- 原文：https://hackerone.com/reports/295339

- - - - - - - - 
Mailsploit is a collection of bugs in email clients that allow effective sender spoofing and code injection attacks. The spoofing is not detected by Mail Transfer Agents (MTA) aka email servers, therefore circumventing spoofing protection mechanisms such as DMARC (DKIM/SPF) or spam filters.
Bugs were found in over 30 applications, including prominent ones like Apple Mail (macOS, iOS and watchOS), Mozilla Thunderbird, various Microsoft email clients, Yahoo! Mail, ProtonMail and others.
In addition to the spoofing vulnerability, some of the tested applications also proved to be vulnerable to XSS and code injection attacks.
More informations are available on mailsploit.com
## I

