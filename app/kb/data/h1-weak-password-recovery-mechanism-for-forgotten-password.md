# HackerOne 实战案例：weak-password-recovery-mechanism-for-forgotten-password

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Cookie steal through content Uri
- 等级：Critical | 项目：Brave | 披露：2021-04-22 | CVE：-
- 原文：https://hackerone.com/reports/876192

- - - - - - - - 
## Summary
A misconfiguration in a content provider is allowing Brave for Android to download internal files to Downloads folder, making them accessible to other apps. A malicious app could order Brave to download the cookies database and retrieve it afterwards.
## Environment
- **Device:** HTC M8
- **OS version:** Android 9
- **Package name:** com.brave.browser
- **App version:** 1.8.93 (`versionCode` 410809320)
## Proof of concept


## (Possible) staff account takeover via reset token bruteforce at helpdesk.bistudio.com
- 等级：Critical | 项目：BOHEMIA | 披露：2018-09-19 | CVE：-
- 原文：https://hackerone.com/reports/332632

- - - - - - - - 
As stated in a brief exchange with @rvn in my other report ##312433, I might have found a logic flaw in the way https://helpdesk.bistudio.com handles the reset flow and tokens.
I've asked if it was possible to obtain a test account, but I fully understand that it's something that cannot be done; as such I'll submit a "blind" report based on my black-box analysis and wait for your team to verify it. Also note that this flaw seems to also be present in the "Set out of office email response" flow, albeit less critical.


## Reset any password
- 等级：High | 项目：pixiv | 披露：2021-03-31 | CVE：-
- 原文：https://hackerone.com/reports/703972

- - - - - - - - 
## Summary:
When I try to reset the password, the verification code of the mailbox is 6 digits, and there is no limit on the number of submissions, so I can reset the password of any user.
## Steps To Reproduce:
1.input the email  [reset password url](https://www.pixiv.net/reminder.php).
{F595146}
click  the "submit" button
{F595147}
input the email verification code and try to guess the verification code, but I won’t be able to continue using it after I try it a few times.
{F595148}
2.After trying, I found that there was no such submission restriction when the password was reset in the third step.
Repeat the above steps, the only difference is that you need to enter the cor


## Password Reset Token Not Expired
- 等级：High | 项目：Infogram | 披露：2017-10-30 | CVE：-
- 原文：https://hackerone.com/reports/283550

- - - - - - - - 
Hello Team,
Here in this scenario, I've found that the there's a kind of server side invalidation of Password Reset tokens. Like if I've requested for password reset token (token1) and I don't use it, after I will make another request for password reset token (token2). This time I'll use the token2 means the link that I requested for the second time, so the first token (token1) should explicitly expire by the server. But here I can use the token1 also after password change by token2, this is unusual behavior of web application.
Exploit Scenario:
If victim's email account is still logged into his/her Office Computers or any public Internet Cafe. Then any external attacker can

