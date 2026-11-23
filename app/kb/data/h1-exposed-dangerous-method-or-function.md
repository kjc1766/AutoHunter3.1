# HackerOne 实战案例：exposed-dangerous-method-or-function

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Open memory dump method leaking customer information ,secret keys , password , source code & admin accounts
- 等级：Critical | 项目：Stripo | 披露：2020-01-31 | CVE：-
- 原文：https://hackerone.com/reports/783360

- - - - - - - - 
## Summary:
Stripo uses Spring boot for the backend API development , and misconfigured the application to open actuator APIs to the public.
This issue is found in 3 domains , don't know if I need to publish 3 reports for that, or just one report , but the domains are :
https://my.stripo.email/cabinet/stripeapi/actuator
https://plugins.stripo.email/actuator
https://plugin.stripo.email/actuator
it might be available in other micro services as well
## Steps To Reproduce:
  1. Go to the following URL : https://my.stripo.email/cabinet/stripeapi/actuator/heapdump
  1. This url will download the heap dump of the server 
  1. using a memory analyzer such as Eclipse memory analyzer 

