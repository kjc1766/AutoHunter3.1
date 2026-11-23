# HackerOne 实战案例：phishing

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Address Bar Spoofing on TOR Browser
- 等级：High | 项目：Tor | 披露：2023-01-02 | CVE：-
- 原文：https://hackerone.com/reports/275960

- - - - - - - - 
Hi TOR team,
I would like to report a security bug in your browser:
Step 1: Goto http://www.ոokia.com/(http://jsbin.com/wuyikedaxi/1/edit?html,output)
Step 2: Observe that address bar points to http://www.ոokia.com/ which actually to be pointing to http://xn--okia-zgf.com, however browser displays www.ոokia.com/
Actual results:
Address bar points to a spoofed domain http://www.ոokia.com/. Address bar fails to parse character "ո"(U+0578 Armenian Small Letter). Several other characters from Armenian family lead to the same effect. 
Expected results:
TORbrowser should have resolved the domain to real http://xn--okia-zgf.com.  On chrome, internet explorer and firefox it resolves


## Github Account hijack through broken link in developer.twitter.com
- 等级：High | 项目：X | 披露：2021-02-04 | CVE：-
- 原文：https://hackerone.com/reports/1031321

- - - - - - - - 
Description
A link in    https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries   was broken and anyone could create that account which leads to account impersonate
Steps To Reproduce
1) Visit https://developer.twitter.com/en/docs/twitter-api/tools-and-libraries
2) Scroll down to Javascript/Node.js and click on by @HunterLarco (v2)
3)  Create github username HunterLarcol
4) When someone visits and scroll down to  javascript/Node.js and click on @HunterLarco (v2). They are redirected to my account
similar report
https://hackerone.com/reports/265696
To solve this issue 
put this link https://github.com/HunterLarco
Please let me know if you have any questions. I 


## Subdomain Takeover on demo.greenhouse.io pointing to unbouncepages
- 等级：High | 项目：Greenhouse.io | 披露：2020-03-05 | CVE：-
- 原文：https://hackerone.com/reports/407355

- - - - - - - - 
Actuall this report is same as of this one:- https://hackerone.com/reports/38007  
Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.
Here there is a greenhouse domain  (demo.greenhouse.io) which is 


## npm packages that overlap with core node packages
- 等级：High | 项目：Node.js | 披露：2018-06-16 | CVE：-
- 原文：https://hackerone.com/reports/333459

- - - - - - - - 
Hi,
  
I have [posted here](https://github.com/npm/registry/issues/306), but I wanted to make you aware of this easy social engineering trick. I do not want to claim any of these are currently malicious, but it they easily could be.
  
Thanks,
Marc
## Impact
The attacker could do anything...use the postinstall as the user, work the same as steal data, etc.
---

