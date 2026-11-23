# HackerOne 实战案例：cross-site-scripting-xss-dom

_26 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## XSS on using the legacy "Graphie To Png" API
- 等级：Critical | 项目：Khan | 披露：2025-02-06 | CVE：-
- 原文：https://hackerone.com/reports/2846011

- - - - - - - - 
An attacker can can upload malicious graphies via (http://graphie-to-png.kasandbox.org/) and (http://graphie-to-png.khanacademy.systems/) that exploit the graphie renderer.
The attack targets any page that has a graphie (`khanacademy.org`!!), as well as `cdn.kastatic.org` and `ka-perseus-graphie.s3.amazonaws.com`
# Proof of concept
## Step 1: Uploading a malicious graphie
consider the following example where https://ka-perseus-graphie.s3.amazonaws.com/2122427aa8dc4ef2a59058bc1a7a934ba6ca6747.svg is used in an article, we will override it by uploading the same JS but with malicious SVG and JSON data (because the hash is a hash of the JS).
1. **Malicious SVG:** The SVG is modi


## xss due to incorrect handling of postmessages
- 等级：Critical | 项目：Khan | 披露：2022-12-23 | CVE：-
- 原文：https://hackerone.com/reports/1758132

- - - - - - - - 
Due to Insecure handling of create link tags (a tags) in a function called `autolink` found in `7Bmt.af733e428f9f986dfc96.js`
[code omitted]
which is ran in the challenges (ex: https://www.khanacademy.org/computing/computer-programming/programming/resizing-with-variables/pc/challenge-brown-bear-eyes). A specially crafted postmessage can abuse this.
[code omitted]
also due to insecure host checking in the `message` event, the mentioned html code above can be run from any webpage.
The payload which the function `autolink` is insecurely creating the tag can look like this
`http://#/"style="width:2000px;height:2000px;position:fixed;top:0;left:0;margin-bottom:2000;z-index:200;"on


## DOM XSS in `fizzy.do` import filename preview enables one-click victim account takeover
- 等级：High | 项目：Basecamp | 披露：2026-04-14 | CVE：-
- 原文：https://hackerone.com/reports/3608199

- - - - - - - - 
## Description
## Summary:
While auditing the latest Fizzy code and validating it end to end in a live Docker deployment of current `main`, I found that the account import page renders the selected local filename with `innerHTML` instead of `textContent`.
In practice, that means a crafted `.zip` filename is not shown as text. It is parsed as live HTML inside the real authenticated import form on `/account/imports/new`. Because that form already contains the victim's session and a valid CSRF token, I was able to inject a second submit control with an attacker-chosen `formaction` and turn the filename preview into an authenticated request gadget.
I pushed this beyond a theoret


## DOM Based Reflected Cross Site Scripting
- 等级：High | 项目：MTN | 披露：2024-12-25 | CVE：-
- 原文：https://hackerone.com/reports/2321874

- - - - - - - - 
## Summary:
I hope you're doing well. I stumbled upon one of your assets. Upon further inspection I realized that the asset was running an outdated version of Swagger. 
The outdated version of Swagger is well-known for Cross-Site Scripting vulnerabilities so I went ahead and attempted to test it in  https://notification-server-v2.sz-my.mtn.com/.  Turns out, it's vulnerable to Cross-Site Scripting. To reproduce it, please follow the steps of reproduction. I have not assessed the full impact of this vulnerability but it is highly probable that a malicious actor could exploit to takeover accounts of applications hosted under *.mtn.com. I hope this gets patched soon. If there's 


## DOM XSS in tiktok.com/login via the redirect_url parameter
- 等级：High | 项目：TikTok | 披露：2024-09-21 | CVE：-
- 原文：https://hackerone.com/reports/2583874

- - - - - - - - 
A DOM Cross-Site Scripting (XSS) vulnerability was found on the redirect_url parameter that could have resulted in account takeover. We thank @sh1yo for reporting this to our team and confirming its resolution.
---


## Lynxview JS interfaces Takeover via deeplink traversal
- 等级：High | 项目：TikTok | 披露：2024-05-24 | CVE：-
- 原文：https://hackerone.com/reports/2417516

- - - - - - - - 
Multiple vulnerabilities could have been chained together resulting in the takeover of Javascript interfaces via the application's exposed Webview. This was only applicable to older versions of the Android application. We thank @fr4via for reporting this to our team and confirming its remediation.
---


## DOM XSS on multiple Automattic domains through postMessages
- 等级：High | 项目：Automattic | 披露：2024-02-26 | CVE：-
- 原文：https://hackerone.com/reports/2371019

- - - - - - - - 
Hi Automattic team,
I have found a 2 flaws that when combined lead to DOM XSS on every website that is using Jetpack with the [Likes](https://jetpack.com/support/likes/) feature enabled. 
The 2 flaws are respectively:
- A DOM XSS vulnerability on https://widgets.wp.com/sharing-buttons-preview/
- The Jetpack plugin creates a postMessage listener allowing messages from the "widgets.wp.com" origin, but will not validate nor encode the `avatar_url` parameter before applying it to the DOM causing XSS.
## Reproduction:
- Navigate to https://0-a.nl/jetpackxssclick.html?url=https://wordpress.com/blog/2024/01/31/http3/ and click the `PoC link`.
## Result
In the newly opened window a 


## com.basecamp.bc3 Webview Javascript Injection and JS bridge takeover
- 等级：High | 项目：Basecamp | 披露：2022-09-23 | CVE：-
- 原文：https://hackerone.com/reports/1343300

- - - - - - - - 
It was identified that the android **com.basecamp.bc3 application**, contains a Webview where the loaded URLs are not sanitised properly. As this webview's functionality is extended via javascript interfaces and has the javascript enabled it is possible to inject arbitrary javascript code which will be executed by the application's webview and provide access to the java native code via the class **a.a.a.s.g** ( which is exposed via the NativeApp).  
##JS Bridge
The following JS Bridges are exposed:
###nativeBridge
{F1452715}
###NativeApp
{F1452717}
###TurboNative
{F1452718}
##Steps to Reproduce
1. Create a valid basecamp account 
2. Create a project 
{F1452720}
3. Open any S


## Dom Xss vulnerability
- 等级：High | 项目：Recorded | 披露：2022-01-19 | CVE：-
- 原文：https://hackerone.com/reports/1448616

- - - - - - - - 
## Summary:
Dom Xss vulnerability
## Steps To Reproduce:
[add details for how we can reproduce the issue]
  1. Go to this link: https://api.recordedfuture.com/index.html
  2. Open chrome devtool and go to console tab
  3. Type: document.write('...<script>alert(1)</script>...');
  4. And boom! Alert 1!
## Impact
XSS can have huge implications for a web application and its users. User accounts can be hijacked, credentials could be stolen, sensitive data could be exfiltrated, and lastly, access to your client computers can be obtained.
---


## Stored XSS in Mermaid when viewing Markdown files
- 等级：High | 项目：GitLab | 披露：2021-10-18 | CVE：-
- 原文：https://hackerone.com/reports/1212822

- - - - - - - -


## Stored XSS in any message (leads to priv esc for all users and file leak + rce via electron app)
- 等级：High | 项目：Rocket.Chat | 披露：2021-03-25 | CVE：CVE-2021-22886
- 原文：https://hackerone.com/reports/1014459

- - - - - - - - 
Persistent XSS flaw using nested markdown tags allows remote attacker to inject arbitrary JavaScript to message. This flaw leads to arbitrary file read and RCE on Rocket.Chat desktop app. Patched on 3.11, 3.10.5, 3.9.7, 3.8.8.
---


## RPC Implementation allows unauthenticated remote calls
- 等级：High | 项目：Lark | 披露：2021-02-10 | CVE：-
- 原文：https://hackerone.com/reports/876022

- - - - - - - - 
It was found that the RPC implementation via postMessage within Lark did not check origin, so an attacker could have potentially performed RPC calls on behalf of a user. We thank @mike12 for reporting this to our team and confirming the resolution.
---


## Possible DOM XSS on app.hey.com
- 等级：High | 项目：Basecamp | 披露：2020-10-27 | CVE：-
- 原文：https://hackerone.com/reports/1010132

- - - - - - - - 
#Summary:
Hello Team,
While testing it was observed that on https://app.hey.com/, on Search box there is a possibility of XSS. Although the payload is reflected in the DOM but the CSP blocks the execution of the script, the XSS can happen if the CSP is somehow bypassed. The Subject parameter is vulnerable.
Apart from XSS, the HTML injection attack is working pretty straight forward.
#Steps To Reproduce:
1. Go to https://app.hey.com
2. Login to your account.
3. Click on 'Write' Mail button.
4. Add the recipient as yourself.
5. In the Subject, add following payload
[code omitted]
6. Send the mail.
7. Go to top left corner Search Box and type "**TestPayload**" 
8. You will see 


## Cross-site Scripting (XSS) - DOM - iqcard.informatica.com
- 等级：High | 项目：Informatica | 披露：2020-10-13 | CVE：-
- 原文：https://hackerone.com/reports/1004833

- - - - - - - - 
Hello all
I found a DOM based XSS at iqcard.informatica.com
# Description
After finding the path **iqcard.informatica.com/pub/fujitsu/fm3v2/player/attach.html**. I noticed that the code inside attach.html was vulnerable to DOM XSS, due to the fact of the javascript *document.location function. search*. The code below illustrates the code contained in the attach.html file
[code omitted]
As can be seen through the code above, the variable * strSearch * receives everything that comes from the URL after the character? and then insert it into the function *document.location.replace ()*. Through this scenario we have some possibilities.
1 - We can direct the user to any page we wa


## DOM BASED XSS ON https://www.rockstargames.com/GTAOnline/features
- 等级：High | 项目：Rockstar | 披露：2020-06-12 | CVE：-
- 原文：https://hackerone.com/reports/479612

- - - - - - - - 
In this report, the researcher identified a DOM-based Cross-Site Scripting vulnerability under the GTAOnline section of the main site. This could have left to theft of cookies if left unresolved. Interestingly, a core factor in this vulnerability was a regression of a previously identified and resolved directory traversal issue. Thanks to this report we were able to close both the regressed directory traversal issue and the cross-site scripting vulnerability at once.
---


## DOM Based xss on https://www.rockstargames.com/ ( 1 )
- 等级：High | 项目：Rockstar | 披露：2020-06-12 | CVE：-
- 原文：https://hackerone.com/reports/475442

- - - - - - - - 
In this report the researcher identified a DOM-based Cross-Site Scripting vulnerability on the main rockstargames.com site. This could have been exploited to steal victim's cookies. The XSS vulnerability was discovered by combining multiple lower-severity vulns, such as directory traversal and an open redirect. By identifying all of the component vulnerabilities, the researcher helped us address this vulnerability faster and more completely. The issue is now resolved.
---


## Warehouse dom based xss may lead to Social Club Account Taker Over.
- 等级：High | 项目：Rockstar | 披露：2020-06-11 | CVE：-
- 原文：https://hackerone.com/reports/663312

- - - - - - - - 
The researcher brought our attention to a DOM-based Cross-Site Scripting vulnerability. Although issues on rockstarwarehouse.com are typically out of scope, this had an explicit impact on Social Club account security, so we decided we needed to act. The vulnerability only affected Internet Explorer and Edge browser users, but with the researcher's help we were able to work with our partners at Rockstar Warehouse and resolve the vulnerability.
---


## DOM-based XSS on mobile.line.me
- 等级：High | 项目：LY | 披露：2020-03-25 | CVE：-
- 原文：https://hackerone.com/reports/736272

- - - - - - - - 
The reporter found a DOM-based XSS affecting mobile.line.me, which could have resulted in an attacker gaining access to information about a user's mobile plans, usage and user details registered as part of their mobile subscription plan.
---


## DOM Based XSS via postMessage at https://inventory.upserve.com/login/
- 等级：High | 项目：Upserve | 披露：2019-06-25 | CVE：-
- 原文：https://hackerone.com/reports/603764

- - - - - - - - 
#Description
DOM based XSS is possible at https://inventory.upserve.com/login/ due to insecure origin checking when receiving a postMessage.
#POC
1. Visit https://hq.upserve.com.████████/upserve_xss.html
2. Click link
3. View alert on https://inventory.upserve.com
#Vulnerable Code
[code omitted]
The origin check simply determines if "https://hq.upserve.com" is anywhere in the origin so an origin like "https://hq.upserve.com.mydomain.com" will pass this check just fine.
## Impact
Due to the page being a login page, login credentials could be logged and stolen when a victim goes to login.
Due to incomplete origin validation, DOM-based XSS was possible at https://inventory.upse


## H1514 DOMXSS on Embedded SDK via Shopify.API.setWindowLocation abusing cookie Stuffing
- 等级：High | 项目：Shopify | 披露：2019-04-17 | CVE：-
- 原文：https://hackerone.com/reports/422043

- - - - - - - - 
Hi Team!
I'm reporting a rather unusual DOMXSS that allows an attacker to perform a XSS attack on any Shopify apps that use the Embedded SDK. To exploit this, several techniques were chained together: Cookie Stuffing -> Login CSRF -> (Not Open) Redirect -> DOMXSS.
#Details
Inspired by #381192, I decided to check all pages to see if there's any broken origin validation. The results were frustrating since they all seemed to be done properly. However I noticed embedded apps did it in a way that it verifies if the coming origin is the logged-in store. Say if I am an admin on foobar.myshopify.com, then an embedded app will check if in-coming messages originate from https://foobar


## DOMXSS in redirect param
- 等级：High | 项目：Semmle | 披露：2019-03-20 | CVE：-
- 原文：https://hackerone.com/reports/361287

- - - - - - - - 
#Summary
The **redirect** param can consist of a ``javascript:`` url, which results in XSS. If a victim visits a malicious URL and logs in, the attacker can perform actions on behalf of the victim.
#Steps to reproduce
1) Logout
2) Visit `` https://lgtm-com.pentesting.semmle.net/?redirect=javascript:prompt(document.domain)%2f%2f
 ``
3) Log in through email
## Impact
If a victim visits a malicious URL and logs in, the attacker can perform actions on behalf of the victim.
---


## DOM XSS on 50x.html page on proxy.duckduckgo.com
- 等级：High | 项目：DuckDuckGo | 披露：2018-11-07 | CVE：-
- 原文：https://hackerone.com/reports/426275

- - - - - - - - 
Hi,
I read the report about DOM XSS on 50x.html page (https://hackerone.com/reports/405191).
I decided to check some other subdomains to be sure.
This link still executes javascript:
https://proxy.duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(%27test%27);%3E
The following subdomains execute javascript as well:
proxy1.duckduckgo.com
proxy2.duckduckgo.com
proxy3.duckduckgo.com
proxy4.duckduckgo.com
@cujanovic: I'm sorry for stealing.
## Impact
The attacker can execute javascript code.
---


## DOM XSS on 50x.html page
- 等级：High | 项目：DuckDuckGo | 披露：2018-10-16 | CVE：-
- 原文：https://hackerone.com/reports/405191

- - - - - - - - 
Hello,
The is a DOM XSS vulnerability on https://duckduckgo.com/50x.html, it seems like the sink is DIV.innerHTML and the source is location.search.
The PoC url is: https://duckduckgo.com/50x.html?e=&atb=test%22/%3E%3Cimg%20src=x%20onerror=alert(document.domain);%3E
The code that is causing this XSS is located in:
https://duckduckgo.com/lib/l110.js
Line 26, Column 60903
Below is the part of the vulnerable code:
`b5.createElement("div"));
cg = (m.exec(b7) || ["", ""])[1].toLowerCase();
b4 = R[cg] || R._default;
ce.innerHTML =  b4[1]  + b7.replace(aB, "<$1></$2>") + b4[2];
cb = b4[0];
while (cb--) {
	ce=ce.lastChild
}
if(!bI.support.leadingWhitespace&&b2.test(b7))`
Screenshot:


## CSS Injection on /embed/ via bgcolor parameter leaks user's CSRF token and allows for XSS
- 等级：High | 项目：Chaturbate | 披露：2018-09-19 | CVE：-
- 原文：https://hackerone.com/reports/386334

- - - - - - - - 
Hi there,
There's a CSS injection here: https://chaturbate.com/embed/admin/?bgcolor=%7D*%7Bbackground:red&tour=nvfS&disable_sound=0&campaign=iNSGX 
[code omitted]
This allows an attacker to enumerate the CSRF token. Once the CSRF token is enumerated, we can 
#POC 
1. Go to `http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR/reset`
2. Now go to `http://d0nut.pythonanywhere.com/demo/token_stealing/7GTt5qD1LD273WYkJyaR` and let it do it's magic :) 
{F324052}
There are numerous endpoints like `POST /choose_broadcaster_chat_color` where it returns `Content-Type: text/html; charset=utf-8` that could potentially allow a hacker to combine the two for XSS (I hav


## XSS в названии сервера
- 等级：High | 项目：VK.com | 披露：2017-09-20 | CVE：-
- 原文：https://hackerone.com/reports/262010

- - - - - - - - 
XSS в поле названия сервера, с ограниченным количеством символов.
**Summary (researcher):**
`Старый админ делает сервер оставляет и продает группу , новый удаляет его но упс срабатывает XSS и старый админ возвращает себе группу . `
но можно вставить `<a href="rg">t` тогда будет ссылка в удалении
Или ВК подгружает страницу `<img src=/rg> `
i die
███████████████████████████
███████▀▀▀░░░░░░░▀▀▀███████
████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██



## XSS в комментариях от имени сообщества
- 等级：High | 项目：VK.com | 披露：2017-09-20 | CVE：-
- 原文：https://hackerone.com/reports/264445

- - - - - - - - 
XSS в дропдауне выбора сообщества при комментировании.
---

