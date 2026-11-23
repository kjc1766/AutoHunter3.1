# HackerOne 实战案例：password-in-configuration-file

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Git repo on https://██████.mil/ discloses API password
- 等级：High | 项目：U.S. | 披露：2021-03-24 | CVE：-
- 原文：https://hackerone.com/reports/765825

- - - - - - - - 
**Summary:**
I found a .git repository on https://███████.mil/.git which discloses an API password for Yubikey on 2 different domains, together with full source code. 
**Description:**
Fetching the git repository and decompressing the objects results in the ability to read the source code of the server, which includes an API password for the Yubikey hardware authentication software. The API however does not appear to be functional on the main domain, but since the repository is very recent, I cannot be certain that it'll stay non-functional. 
Additionally, the server discloses info.php at https://███████.mil/info.php. I'm uncertain if this should be reported separately, any 


## Insecure Zendesk SSO implementation by generating JWT client-side
- 等级：High | 项目：Trint | 披露：2019-09-08 | CVE：-
- 原文：https://hackerone.com/reports/638635

- - - - - - - - 
## Summary:
app.trint.com implements SSO to Zendesk, it does this by using JWT as described at https://support.zendesk.com/hc/en-us/articles/203663816-Enabling-JWT-JSON-Web-Token-single-sign-on
This functionality has not been implemented securely because the JWT generation happens in the client-side. This is done by the Zendesk secret being hardcoded in the JavaScript code.
The secret is used to create JSON Web Tokens and then you can use the generated token to impersonate any customer in Zendesk. (therefore potentially getting access to their support tickets)
Whilst support.trint.com is marked as out of scope for the program, the described vulnerability isn't caused by Zend

