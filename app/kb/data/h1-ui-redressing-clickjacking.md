# HackerOne 实战案例：ui-redressing-clickjacking

_8 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Clickjacking In https://demo.nextcloud.com
- 等级：Critical | 项目：Nextcloud | 披露：2017-05-20 | CVE：-
- 原文：https://hackerone.com/reports/222762

- - - - - - - - 
Hi Nextcloud,
Clickjacking In https://demo.nextcloud.com
This Is Zeeshan,An Ethical Hacker, I Have Found A Security Issue In Your Site
Clickjacking In nextcloud https://demo.nextcloud.com Page
<html>
<head>
<body>
<p>Website is vulnerable to clickjacking!</p>
<iframe src="https://demo.nextcloud.com" width="500" height="500"></iframe>
</body>
</html>
Please Fix It As Soon As Possible
Best Regards,
Zeeshan Waheed
xsszeeshan@gmail.com
---


## Clickjacking at  app.lemlist.com
- 等级：High | 项目：lemlist | 披露：2022-05-20 | CVE：-
- 原文：https://hackerone.com/reports/1574017

- - - - - - - - 
Hi team,
While performing security testing of your website i have found the vulnerability called Clickjacking.
Many URLS are in scope and vulnerable to Clickjacking.
What is Clickjacking ?
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
The server didn't return an X-Frame-Options header which means that this website could be at risk of a clickjacking attack. The X-Frame-Option


## Clickjacking to change email address
- 等级：High | 项目：Gener8 | 披露：2022-01-12 | CVE：-
- 原文：https://hackerone.com/reports/783191

- - - - - - - - 
##Summary
Clickjacking (User Interface redress attack, UI redress attack, UI redressing) is a malicious technique of tricking a Web user into clicking on something different from what the user perceives they are clicking on, thus potentially revealing confidential information or taking control of their computer while clicking on seemingly innocuous web pages.
It allows remote attackers to do some clickjacking which can be used for adding arbitrary tasks . Why? Almost all of your page has missing X-FRAME-OPTIONS header.
Websites are at risk of a clickjacking attack when they allow content to be embedded within a frame.
##Proof of concept code :- 
Copy the above code and paste


## ClickJacking
- 等级：High | 项目：Acronis | 披露：2021-03-16 | CVE：-
- 原文：https://hackerone.com/reports/947690

- - - - - - - - 
I have found the vulnerability called Clickjacking.
Please find the details below:
Description     
Clickjacking is an exploit in which malicious coding is hidden beneath apparently legitimate buttons or other clickable content on a website.
  OWASP Benchmark   A6- Security Misconfiguration  
Steps to Reproduce   
1.Craft an HTML page and add the following 
( https://www.acronis.com/en-in/ ) of the application within an iframe.
2.Save the file as *.html and run the file.
3.Open the HTML page in a browser.
4.The following attached screenshot shows webiste is in frame.
Please find the attached screenshot for your reference. 
High Level Fix Recommendation
Clickjacking attacks c


## Cross-site Scripting (XSS) - Stored in RDoc wiki pages
- 等级：High | 项目：GitLab | 披露：2019-12-16 | CVE：-
- 原文：https://hackerone.com/reports/662287

- - - - - - - -


## Viral Direct Message Clickjacking via link truncation leading to capture of both Google credentials & installation of malicious 3rd party Twitter App
- 等级：High | 项目：X | 披露：2019-10-31 | CVE：-
- 原文：https://hackerone.com/reports/643274

- - - - - - - - 
**Summary:** [Viral Direct Message Clickjacking via link truncation leading to capture of both Google credentials & installation of malicious 3rd party Twitter App]
**Description:** [Because very long links in direct messages are truncated after 38 characters the malicious actors were able to provide a malicious link in a direct message that appeared as though it was to an authenticated YouTube video and caused a clickjacking scenario to occur. The link caused any users that were already logged into a Google account to be first logged out and then asked to log back in. A malicious Google app captured the account credentials and then redirected the user to the website getmore


## Account takeover vulnerability by editor role privileged users/attackers via clickjacking
- 等级：High | 项目：WordPress | 披露：2018-09-03 | CVE：-
- 原文：https://hackerone.com/reports/388254

- - - - - - - - 
####Vulnerability -
Editor role privileged users are able to hack into other's account by exploiting clickjacking vulnerability.
####Version-
4.9.7
####Issue-
https://make.wordpress.org/core/handbook/testing/reporting-security-vulnerabilities/#why-are-some-users-allowed-to-post-unfiltered-html
As mentioned per the above link, the editor and admin roles are given permissions to inject arbitary javascript in the posts. Though its a severe vulnerability we can't report about injecting javascript to steal cookies.
**But only the admin roles/users have the permissions to change the details of other users. Due to this vulnerability editor privileged users are even able to do accou


## Clickjacking on Mixmax.com
- 等级：High | 项目：Mixmax | 披露：2017-06-13 | CVE：-
- 原文：https://hackerone.com/reports/234713

- - - - - - - - 
mixmax.com was vulnerable to clickjacking.
---

