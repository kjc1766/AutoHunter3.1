# HackerOne 实战案例：improper-check-or-handling-of-exceptional-conditions

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## curl proceeds with unsafe connections when -K file can't be read
- 等级：High | 项目：curl | 披露：2022-04-21 | CVE：-
- 原文：https://hackerone.com/reports/1542881

- - - - - - - - 
## Summary:
I'm using curl 7.82.0 on Linux. When the file specified by the -K option can't be read, curl sends network traffic as specified by the other options that are explicitly included on the command line (in other words, there's only a warning and I'd like it to be a fatal error). This behavior occurs even if those other options result in an action that's often considered unsafe, such as use of cleartext passwords. It's fine for curl to be capable of sending cleartext passwords, but this shouldn't happen unintentionally.
I feel that this is a vulnerability in curl because curl is able to recognize that the user's intended set of options was not specified correctly, but

