# HackerOne 实战案例：missing-authorization

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Unrestricted access to quiesce functionality in dss.api.playstation.com REST API leads to unavailability of application
- 等级：High | 项目：PlayStation | 披露：2021-03-30 | CVE：-
- 原文：https://hackerone.com/reports/993722

- - - - - - - - 
## Report Summary
----
Unrestricted access to the quiesce function via a `PUT` request to `https://dss.api.playstation.com/api/application/state` makes the application unreachable for an uncertain amount of time.
## Steps To Reproduce
----
[Reproduction method #1]
+ *Burp Suite is the program required for the following method of reproduction*
+ *Any OS platform can be used to reproduce this bug*
  
1. Using Burp Suite, go to *Proxy* tab -> *Intercept* tab. On this pane, click on **Open Browser** to launch the embedded chromium browser. {F1006879}
1. In the chromium browser address bar, enter: https://dss.api.playstation.com/api/application/state
1. In Burp Suite, go to *Prox


## Access token stealing.
- 等级：High | 项目：PlayStation | 披露：2020-11-21 | CVE：-
- 原文：https://hackerone.com/reports/821896

- - - - - - - - 
# Summary:
`https://my.playstation.com/auth/response.html` suffers from a misconfiguration which leads to access token stealing.
# Description:
The page `https://my.playstation.com/auth/response.html?requestID=iframe_request_ca8b5107-9b8f-4510-9667-15fd7b9327d1&baseUrl=/&targetOrigin=https://my.playstation.com` hosts a javascript which is responsible for transferring OAuth access token from the issuing server to the client.
On analyzing this javascript we found an issue which leads to an access token stealing.
[code omitted]
[code omitted]
To get into the window case we need to start the requestID parameter value from `window` keyword.
a => window.location
c => a.targetOrigi

