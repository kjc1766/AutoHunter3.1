# HackerOne 实战案例：authentication-bypass

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Account Takeover in Password Reset Function
- 等级：Critical | 项目：Mars | 披露：2025-09-02 | CVE：-
- 原文：https://hackerone.com/reports/3228888

- - - - - - - - 
A critical authentication bypass vulnerability was present in the password reset functionality of the ███████ website at ███████. The vulnerability allowed attackers to take over any user account without requiring access to the victim's phone number or the one-time password (OTP) sent via SMS. The security flaw existed in the implementation of the "Forgot Password" feature, where the system was designed to send an OTP to a user's registered phone number for verification before allowing password reset. However, the vulnerability arose from inadequate server-side validation that relied on client-side responses to determine the success of OTP verification. An attacker could int


## Stealing SSO Login Tokens (snappublisher.snapchat.com)
- 等级：High | 项目：Snapchat | 披露：2021-07-29 | CVE：-
- 原文：https://hackerone.com/reports/265943

- - - - - - - - 
# Description
Attacker can steal SSO login tokens for snappublisher.snapchat.com by chaining different flaws in SSO and Snapchat’s Snappublisher tool. Detailed attack flow is as follows.
# Attack Flow
1.. Snapchat fetches a `SSO LOGIN TOKEN` from `accounts.snapchat.com` to login into different products of Snapchat i.e. SnapPublisher, Ads Manager, Business Manager, etc. provided that user is logged into `accounts.snapchat.com`.
eg. To login into SnapPublisher following requests are made …
1] https://accounts.snapchat.com/accounts/login?client_id=creativesuite-prod&referrer=https://snappublisher.snapchat.com/sso_continue
2] 302 redirect to
https://accounts.snapchat.com/account

