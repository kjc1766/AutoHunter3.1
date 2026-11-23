# HackerOne 实战案例：misconfiguration

_17 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Мисконфигурация Cisco Smart Install
- 等级：Critical | 项目：Azbuka | 披露：2021-11-16 | CVE：-
- 原文：https://hackerone.com/reports/1398662

- - - - - - - - 
Closed.
---


## Weak password policy leading to exposure of administrator account access
- 等级：Critical | 项目：U.S. | 披露：2021-05-20 | CVE：-
- 原文：https://hackerone.com/reports/1168104

- - - - - - - - 
Hi,
The login endpoint https://mysmartplans.gsa.gov/Marathon/Default.aspx is having weak password policy.
During the recon, I came across a mysmartplans overview document http://www.accentimaging.com/accent/pdfs/Accent%20MySmartPlans.pdf
. In this document few users are mentioned like - rick, ban, tim etc.I tried to login user password combination of these user-names & rick wass found a valid administrator username & password.
username- rick
password -rick
This user appears to be administrator user.
Hope GSA takes necessary measures to improve user account policies.
PoC
1) Open url https://mysmartplans.gsa.gov/Marathon/Default.aspx
2) Enter username  rick password rick
3) Yo


## Spring Actuator endpoints publicly available and broken authentication
- 等级：Critical | 项目：LY | 披露：2020-08-06 | CVE：-
- 原文：https://hackerone.com/reports/838635

- - - - - - - - 
Due to insufficient access control, it was possible to access the Spring Boot Actuator endpoints /heapdump and /env. @kazan71p identified two highly sensitive applications leaking information through these endpoints.
The LINE Security team shutdown the secondary endpoints just as it was discovered by the reporter, as part of our incident response process. After further investigation, we also found that both applications had the same issue with their authentication functionality, due to using the same library. The issue was that old tokens were not expiring and being properly invalidated, allowing for replay attacks that should not have been possible.
The applications were hi


## Spring Actuator endpoints publicly available, leading to account takeover
- 等级：Critical | 项目：LY | 披露：2020-08-04 | CVE：-
- 原文：https://hackerone.com/reports/862589

- - - - - - - - 
Due to insufficient access controls, it was possible to access the Spring Boot Actuator endpoints /heapdump and /env. The /heapdump endpoint leaks data from the Java Virtual Machine, leading to disclosure of admin credentials, user tokens and a combination of other data.
This endpoint was not discovered by the internal security team due to being put on a custom path, avoiding detection through our usual means. The reporter accessing this endpoint also triggered a warning for our CSIRT team, allowing us to take quick and coordinated action. After quickly restricting access to this endpoint, we investigated and found no activity except that of the reporter.
The maximum impact 


## Session Cookie Leakage via Static Header Field in WebViewerFragment
- 等级：High | 项目：LinkedIn | 披露：2026-03-17 | CVE：-
- 原文：https://hackerone.com/reports/3475626

- - - - - - - - 
Hello LinkedIn Security Team,
I was able to identify a vulnerability in the `WebViewerFragment` that can lead to leaking the user's cookies to a threat actor. Below, I will explain the finding and provide a PoC.
## Summary
A static field (`CUSTOM_HEADERS`) in `WebViewerFragment` persists cookies across different URL loads, allowing an attacker to chain multiple weaknesses to exfiltrate a victim's LinkedIn session cookies to an attacker-controlled server.
## Root Cause
While the exploitation is complex, the root cause is simple. In the `loadUrl` method of the vulnerable fragment:
[code omitted]
The method retrieves cookies for the URL. If cookies exist, they are added to `Web


## Internal Access to Hackerone confluence Docs
- 等级：High | 项目：HackerOne | 披露：2025-08-15 | CVE：-
- 原文：https://hackerone.com/reports/3113398

- - - - - - - - 
This vulnerability allowed external access to HackerOne's internal Confluence documentation through a support system misconfiguration. The impact included:
- Access to internal documentation that wasn't intended for public viewing
- The ability to view and modify limited content within the Confluence instance
This configuration issue demonstrated how support system workflows could be leveraged to gain unauthorized access to internal resources.
---


## subdomain takeover at █████████
- 等级：High | 项目：Mars | 披露：2023-11-15 | CVE：-
- 原文：https://hackerone.com/reports/2106886

- - - - - - - - 
Summary:
I discovered a subdomain takeover vulnerability at ██████████. The subdomain was pointing to an inactive or non-existent resource, allowing an attacker to claim the resource and take control of the subdomain.
Details:
While performing reconnaissance on █████, I noticed that the ███████ subdomain was pointing to a resource on a third-party service. However, upon further investigation, I found that the resource was either inactive or non-existent.
This allowed me to claim the resource on the third-party service and take control of the ██████████ subdomain. As a result, I was able to serve arbitrary content on the subdomain
Steps To Reproduce:
I wanted to share with yo


## Mass account takeover!
- 等级：High | 项目：Stripe | 披露：2022-12-21 | CVE：-
- 原文：https://hackerone.com/reports/1634165

- - - - - - - - 
@akashhamal0x01 discovered an Organization Owner could update the email address of a member of their organization in TaxJar. This could have allowed an attacker to take over a victim’s account if the victim belonged to the attacker’s organization. The vulnerability was caused by the ability to edit another member’s email address and was resolved by restricting Organization Owners from editing a member’s email address.
**Summary (researcher):**
A misconfiguration was found by which other users mail can be changed resulting in account takeover!
---


## Subdomain takeover on 'de-headless.staging.gymshark.com'
- 等级：High | 项目：Gymshark | 披露：2022-10-27 | CVE：-
- 原文：https://hackerone.com/reports/1711890

- - - - - - - - 
The Gymshark subdomain https://de-headless.staging.gymshark.com/ was pointing to an unclaimed Shopify site. Because of this an attacker could claim this subdomain, via Shopify, and serve their own content.
This is extremely dangerous as an attacker could serve any malicious content on this domain such as malware, domain defacement, phishing campaigns etc. 
Also, phishing victims wouldn't be able to identify the maliciousness of a potential phishing campaign because it would be from a valid Gymshark subdomain.
**Note:** *I have temporarily claimed this domain for PoC and have password protected the site to reduce unnecessary impact to others. I am happy to remove this protect


## Security misconfiguration
- 等级：High | 项目：lemlist | 披露：2022-05-16 | CVE：-
- 原文：https://hackerone.com/reports/1486327

- - - - - - - - 
## Description :
When we request a magic link to login into the application, and use that same link in multiple browsers, it working there isn't any limit on use of link.
Steps to reproduce :
1. go to app.lemilist.com
2. create a magic link 
3. use it to login 
4. now open another browser or incognito window
5. use that same magic link
And You'll be logged in in your account.
## Impact
If Attacker gets the magic link of user he can login into victim's account.
Account takeover.
Mitigation :
1. Add a limit to magic link and remove the magic link from database after 1 use.
2. only allow the Requester IP to login using the magic link.
---


## Subdomain Takeover on proxies.sifchain.finance pointing to vercel
- 等级：High | 项目：Sifchain | 披露：2022-04-01 | CVE：-
- 原文：https://hackerone.com/reports/1487793

- - - - - - - - 
Hello Team,
Subdomain takeover vulnerabilities occur when a subdomain (subdomain.example.com) is pointing to a service (e.g. GitHub pages, Heroku, etc.) that has been removed or deleted. This allows an attacker to set up a page on the service that was being used and point their page to that subdomain. For example, if subdomain.example.com was pointing to a GitHub page and the user decided to delete their GitHub page, an attacker can now create a GitHub page, add a CNAME file containing subdomain.example.com, and claim subdomain.example.com.
Here there is a Sifchain domain  (proxies.sifchain.finance) which is pointing towards vercel pages so  this domain can be taken over can


## Password reset token leakage
- 等级：High | 项目：UPchieve | 披露：2022-03-26 | CVE：-
- 原文：https://hackerone.com/reports/1354437

- - - - - - - - 
Reset Password link : http://hackers.upchieve.org/setpassword?token=a3c448b1eb9b982f93ec39a7181ec1a2
1.Open Password reset page from email.
2.Intercept the request(I have used burp suite)
3.You can see the link for reset password in below requests
POST /j/collect?v=1&_v=j93&a=1038273919&t=pageview&_s=1&dl=https%3A%2F%2Fhackers.upchieve.org%2Fsetpassword%3Ftoken%3Da3c448b1eb9b982f93ec39a7181ec1a2&dp=%2Fsetpassword&ul=en-us&de=UTF-8&dt=UPchieve&sd=24-bit&sr=1366x768&vp=1366x657&je=0&_u=wCCAAUABAAAAAC~&jid=185704536&gjid=1537782490&cid=83313712.1632910097&tid=UA-133171872-1&_gid=1095396647.1632910097&_r=1&gtm=2ou9r0&z=1390812166 HTTP/2
Host: www.google-analytics.com
Content-Len


## Ability To Delete User(s) Account Without User Interaction
- 等级：High | 项目：GitLab | 披露：2021-03-17 | CVE：-
- 原文：https://hackerone.com/reports/928255

- - - - - - - -


## Route53 Subdomain Takeover on test-cncf-aws.canary.k8s.io
- 等级：High | 项目：Kubernetes | 披露：2021-01-16 | CVE：-
- 原文：https://hackerone.com/reports/794382

- - - - - - - - 
## Summary:
I discovered that it was possible to takeover ` test-cncf-aws.canary.k8s.io` by assigning a zone to that name with one of the following nameservers in Route53:
[code omitted]
Once the zone was claimed, I was able to create DNS records under this host. Consider the following record:
[code omitted]
##Steps To Reproduce:
1. See above domain
##Remediation Instructions
Remove the NS record delegation NS privs on a subdomain before you delete the zone
## Impact
With this vulnerability, an attacker can host arbitrary content under your domain. This can allow an attacker to host brand-damaging materials, steal sensitive * scoped session cookies, and even escalate other v


## Subdomain Takeover due to unclaimed domain pointing to Acquia Cloud
- 等级：High | 项目：Insulet | 披露：2021-01-14 | CVE：-
- 原文：https://hackerone.com/reports/874482

- - - - - - - - 
ssue Details
The consultant identified that subdomain http:// or https://qa.myomnipod.com 
Web Site Not Found
Sorry, we could not find any content for this web address. Please check the URL.
If you are an Acquia Cloud customer and expect to see your site at this address, you'll need to add this domain name to your site via the Acquia Network management console.
Error Is displayed.
How did you come across this bug ?
Using enumeration, I was able to discover this domain and determined it
NOTE: The hostname was not claimed by me also because i need to pay certain amount to host a website.
## Impact
Sub-domain take over attacks can happen when a company creates a dns entry that 


## Django DEBUG mode enabled and leaked system information.
- 等级：High | 项目：Dropcontact | 披露：2020-08-21 | CVE：-
- 原文：https://hackerone.com/reports/963542

- - - - - - - - 
We were leaking / showing system information.
**Summary (researcher):**
Django DEBUG mode was enabled and showing some information on some errors.I just follow the errors and finally got some sensitive system information such as configuation ,API keys ,Database users ,System Directories,etc..
---


## misconfigured CORS let to HPP and SOP bypass
- 等级：High | 项目：BTFS | 披露：2020-05-07 | CVE：-
- 原文：https://hackerone.com/reports/867436

- - - - - - - - 
Hello team,
I found a bug on your website that let me bypass the SOP policy.
Hope you fix it, everything is in the video
https://www.youtube.com/watch?v=PYsU350S-s4
## Impact
The attacker my direct a victim to a phishing page of www.bitterrent.com/login and he/she will be convince to enter their email and password or even hijack csrf-token and sending him a password or email reset link.
I also found a link that expose the csrf-token on the URL and you should check this link in the black.svg host header URL
---

