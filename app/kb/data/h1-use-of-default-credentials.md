# HackerOne 实战案例：use-of-default-credentials

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Default Credentials on Kinetic Core System Console - https://█████/kinetic/app/
- 等级：Critical | 项目：U.S. | 披露：2023-05-15 | CVE：-
- 原文：https://hackerone.com/reports/1938693

- - - - - - - - 
**Description:**
The Kinetic Core System Console application has weak credentials of **admin/admin**.
## References
[https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials](https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/04-Authentication_Testing/02-Testing_for_Default_Credentials)
## Impact
Potential attackers could identify technologies being used underneath. This would allow for them to find potential exploits.
In addition, the application is disclosing server logs, users in the database with their emails and names, sy

