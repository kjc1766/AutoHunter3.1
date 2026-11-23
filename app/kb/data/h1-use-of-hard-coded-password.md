# HackerOne 实战案例：use-of-hard-coded-password

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## hardcoded password stored in javascript of https://████.mil
- 等级：High | 项目：U.S. | 披露：2020-11-02 | CVE：-
- 原文：https://hackerone.com/reports/991718

- - - - - - - - 
**Summary:**
I have discovered a cleartext password stored within a javascript. This password allows me to authentication to https://█████.mil.
**Description:**
I have discovered a cleartext password stored within a javascript. This password allows me to authentication to https://███████.mil.
To confirm this vulnerability we will first navigate to https://███████.mil, you are now prompted to type a password. We will provide an incorrect password such as 'Password'.
██████████
███
We can confirm the password is invalid. However, reviewing the javascript data for '██████.chunk.js' we can confirm the authentication is validated based on a hardcoded password '█████████!'.
██████

