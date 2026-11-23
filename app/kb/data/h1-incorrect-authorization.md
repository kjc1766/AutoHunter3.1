# HackerOne 实战案例：incorrect-authorization

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## IDOR Leads To  User Profile Modification https://mtnmobad.mtnbusiness.com.ng/app/updateUser
- 等级：Critical | 项目：MTN | 披露：2024-09-18 | CVE：-
- 原文：https://hackerone.com/reports/1714638

- - - - - - - - 
## Summary:
Hello Team,
https://mtnmobad.mtnbusiness.com.ng/app/updateUser allows authenticated users to alter their account profile. But, however, there is no authorization check when updating another user's profile thus, allowing attacker to modify  anyone's profile info such as `Username, Address,  Mobile Number,  Company Name and Company Size`
## Steps To Reproduce:
## Requirements:
Create two Test Accounts (Attacker & Victim)
Login into attacker's account In Mozilla Firefox at https://mtnmobad.mtnbusiness.com.ng/#/login1.   
1. Visit https://mtnmobad.mtnbusiness.com.ng/#/userProfile 
2. Goto to Burp and turn Intercept is on to capture request.
3. Locate this endpoint `P


## Any meeting chat history can be read and modified by an arbitrary user
- 等级：Critical | 项目：8x8 | 披露：2021-04-29 | CVE：-
- 原文：https://hackerone.com/reports/1038658

- - - - - - - - 
A vulnerability existed where a `JaaS` user could read & modify the chat history of an `8x8 Meet` conference. It was limited by the fact that the meeting UUID was required to be known. The fix was promptly deployed to production.
**Summary (researcher):**
A vulnerability in an API accessible through the `jaas.8x8.vc` white-label frontend of the Jitsi platform allowed a user to view, edit, and overwrite / delete the conversation (chat) history or transcript of any `8x8.vc` conference due to a lack of authorization checks to validate that the meeting being edited belonged to the white-label customer.
---


## Full access to internal Gitlab instances at redash.gitlab.com, dashboards.gitlab.com, prometheus.gitlab.com
- 等级：Critical | 项目：GitLab | 披露：2019-04-19 | CVE：-
- 原文：https://hackerone.com/reports/498964

- - - - - - - - 
**Summary:**
Lack of proper ticket trick security leads to internal access on Gitlab instances. **I did not use support.gitlab.com instead just using support@gitlab.com email was suffice. 
**Description:**
*Getting a support@gitlab.com Google Account*
After the Ticket Trick attack that Inti reported and disclosed, many companies including Gitlab added proper security measures to prevent this kind of attack. What companies did not realize is that Zendesk has a feature that can be exploited by attackers other than the CC feature. 
In this case, Gitlab has blocked sending emails to support+*@gitlab.com which prevents Ticket Trick that Inti came up with. However, the CC feature 


## Email verification bypasa
- 等级：High | 项目：Stripo | 披露：2020-03-24 | CVE：-
- 原文：https://hackerone.com/reports/763458

- - - - - - - - 
Email verification bypass:
after finishing the registration user need to verify the email address, this can be bypased while loggin in to the account.
---

