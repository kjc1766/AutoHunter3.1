# HackerOne 实战案例：unverified-password-change

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Password authentication when changing information bypass. Bypass of report #721341
- 等级：High | 项目：Khan | 披露：2021-02-11 | CVE：-
- 原文：https://hackerone.com/reports/1040373

- - - - - - - - 
#SUMMARY
When reading the disclosed reports of your program, i see this one report #721341 . The reporter reported a lack of password confirmation when linking accounts. A fix was applied, adding password confirmation when linking account to other services. But i found a way to bypass this, The password confirmation is only done in the client side. This is bad because such methods are vulnerable to response manipulation. I will add a video poc 
#STEPS TO REPRODUCE
1. Open a browser in which a user has previously logged into an account, but hasn't logged out.
2. Open another browser and login using your account
3. Try to link gmail using your account, it will prompt for a pas


## Information can be changed without a password
- 等级：High | 项目：Khan | 披露：2020-03-14 | CVE：-
- 原文：https://hackerone.com/reports/721341

- - - - - - - - 
If a user has access to a logged in session on Khan Academy, they are able to conduct a full account takeover. This is due to the fact that a new email address can be added to an account without a method of re-authentication. Once this email address has been added, the attacker can simply logout and follow the "Forgot Password" dialogue on the login page to send a password reset email to the email address they added. This allows them to change the password and completely take over the account. While this could arguably be the user's fault for not logging out, Khan Academy specifically targets an audience of students and educators, many of whom may use their accounts on share

