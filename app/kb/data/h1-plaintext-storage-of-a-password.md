# HackerOne 实战案例：plaintext-storage-of-a-password

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Arbitrary File Reading on Uber SSL VPN
- 等级：High | 项目：Uber | 披露：2021-02-25 | CVE：CVE-2019-11510,
- 原文：https://hackerone.com/reports/617543

- - - - - - - - 
The hacker has found a series of 0 day related to Pulse Secure SSL VPN.
---


## Password of failed (2FA) login attempt is stored in log
- 等级：High | 项目：Nextcloud | 披露：2020-03-01 | CVE：-
- 原文：https://hackerone.com/reports/244092

- - - - - - - - 
If I try to log in on Webdav with my usual Nextcloud password, it doesn't work due to 2FA. I need an application password.
The password of a failed login attempt by any user is stored plain text in the log:
`[...]OCA\\\\DAV\\\\Connector\\\\Sabre\\\\Auth->validateUserPass('matthes', '***THE_PASSWORD***')[...]`
Even though the login attempt failed, the password is the right password. I am using two factor, but still, the password may not be leaked to anyone. It may also be used for other websites or services, like LDAP. And you can disable 2FA and still use the same password. The log is in some cases visible to multiple people, may it be admins (but who shouldn't have access t

