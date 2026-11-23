# HackerOne 实战案例：cross-site-scripting-xss-reflected

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Reflected XSS in https://nin.mtn.ng/nin/success?message=lol&nin=<VULNERABLE>
- 等级：Critical | 项目：MTN | 披露：2024-10-05 | CVE：-
- 原文：https://hackerone.com/reports/2039384

- - - - - - - - 
###Summary:
Hello team,
Found a reflected XSS on one your domains i believe https://nin.mtn.ng/nin/success?message=msg&nin= as the nin parameter is vulnerable.
Please check the following PoC:
Run the following command from a terminal:
curl -ski "https://nin.mtn.ng/nin/success?message=lol&nin=<script>alert(1)</script>"  | grep "alert"
{F2446627}
I reported this before in report #1737682 but it was closed as resolved while still vulnerable.
## Impact
Attacker could execute js in the victim's browser.
---


## Reflected XSS
- 等级：Critical | 项目：Bumble | 披露：2019-11-21 | CVE：-
- 原文：https://hackerone.com/reports/739601

- - - - - - - - 
The researcher has found an XSS when sending messages through our service.
---


## muber-id Query Parameter Can Generate SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint
- 等级：Critical | 项目：Uber | 披露：2017-12-26 | CVE：-
- 原文：https://hackerone.com/reports/300102

- - - - - - - - 
## Summary
The muber-id request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker control


## lite:sess Query Parameter Can Generate SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint
- 等级：Critical | 项目：Uber | 披露：2017-12-26 | CVE：-
- 原文：https://hackerone.com/reports/300101

- - - - - - - - 
## Summary
The lite:sess request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker contro


## udi-id Query Parameter Can Generate SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint
- 等级：Critical | 项目：Uber | 披露：2017-12-26 | CVE：-
- 原文：https://hackerone.com/reports/300103

- - - - - - - - 
## Summary
The udi-id request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker controlle


## SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint
- 等级：Critical | 项目：Uber | 披露：2017-12-26 | CVE：-
- 原文：https://hackerone.com/reports/300081

- - - - - - - - 
## Summary
The _ga request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker controlled d


## SSL-protected Reflected XSS in m.uber.com
- 等级：Critical | 项目：Uber | 披露：2017-12-26 | CVE：-
- 原文：https://hackerone.com/reports/296701

- - - - - - - - 
## Summary
m.uber.com is susceptible to reflected XSS
## Security Impact
A malformed URL can be used to render arbitrary SSL-protected web pages from m.uber.com
## Reproduction Steps
https://m.uber.com/?bjbxm%3c%2fscript%3e%3cscript%3ealert(1)%3c%2fscript%3exrii5=1
## Specifics
From the rendered web page:
[code omitted]
No further efforts were made to render a more believable webpage as the vulnerability and reflected code above is sufficient to trigger Chromium Browser's XSS _Auditor protections.
## Impact
An attacker could render arbitrary SSL-protected web pages from m.uber.com, to capture user login credentials and passwords, credit card numbers and related payment infor


## SSL-protected Reflected XSS in https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js Endpoint
- 等级：Critical | 项目：Uber | 披露：2017-12-26 | CVE：-
- 原文：https://hackerone.com/reports/300080

- - - - - - - - 
## Summary
The _cc request parameter at the https://m.uber.com/0-dfffb25d2cf6ceeb0a27.js mobile endpoint is copied into a javascript string encapsulated in double quotation marks, resulting in SSL-protected payloads being reflected unmodified in the application's response. The script-src whitelist at the endpoint includes a wildcard *.cloudfront.net host, which could be used by any attacker with an Amazon Web Services account to provision an arbitrary cloudfront.net host to serve trusted files from. The endpoint also has a missing base-uri, which allows the injection of base tags. They can be used to set the base URL for all relative (script) URLs to an attacker controlled d


## XSS on Amazon Aquisition:  elemental
- 等级：High | 项目：AWS | 披露：2025-07-22 | CVE：-
- 原文：https://hackerone.com/reports/3205667

- - - - - - - - 
Hi Kasim, thank you for submitting this report and for validating that it was fully addressed.
---


## Reflected - XSS
- 等级：High | 项目：MTN | 披露：2024-10-21 | CVE：-
- 原文：https://hackerone.com/reports/1779447

- - - - - - - - 
## Summary:
Hi, Team I'm Found Reflected XSS
## Steps To Reproduce:
1.Nave to https://www.mtn.bj/
2.Go to Messages 
3. Enter XSS Payload :
    * <h1 onauxclick=confirm(document.domain)>RIGHT CLICK HERE
4. Reflected the popup
## Impact
Cross site scripting attacks can have devastating consequences. Code injected into a vulnerable application can exfiltrate data or install malware on the user's machine. Attackers can masquerade as authorized users via session cookies, allowing them to perform any action allowed by the user account.
**Summary (researcher):**
POC Video :- https://youtu.be/HLshcsX1GwU?si=BM0VLLNjbM8ZwBbi
* https://youtu.be/gT-0RwW0mRM?si=yUhC-N1Hk33pcBwj
---


## Reflected XSS on Pangle Endpoint
- 等级：High | 项目：TikTok | 披露：2024-04-05 | CVE：-
- 原文：https://hackerone.com/reports/2352968

- - - - - - - - 
A cross-site scripting (XSS) vulnerability was found at the Pangle endpoint via the 'redirect' parameter. This was caused by the reflection of user-supplied data without appropriate HTML escaping or output encoding. As a result, a JavaScript payload could have been returned by the above endpoint and executed within a user's browser. We saw no evidence of exploitation before the vulnerability was fixed and additional mitigations applied. We thank @m7x for reporting this to our team and confirming its remediation.
---


## CRLF to XSS & Open Redirection
- 等级：High | 项目：TikTok | 披露：2023-08-16 | CVE：-
- 原文：https://hackerone.com/reports/2012519

- - - - - - - - 
Due to inadequate input validation, it could have been possible to inject CRLF (HTTP Response Splitting) into the parameter "__hack_redirect_now__ " on a TikTok seller endpoint. This could have led to Reflective XSS (Cross-Site Scripting) to gain access to a user's cookies, or the ability to send users to unauthorized webpages ending in "tiktok.com" via an open redirect. This vulnerability has been resolved. We thank @ashrafabdelrazik for reporting this to our team.
---


## Reflected Cross-Site Scripting(CVE-2022-32770 )
- 等级：High | 项目：Rocket.Chat | 披露：2023-06-22 | CVE：CVE-2022-32770
- 原文：https://hackerone.com/reports/1844777

- - - - - - - - 
The researcher has found a XSS  vulnerability  inside our https://video.rocket.chat.
---


## Reflected Cross-site Scripting (XSS) at https://www.tiktok.com/
- 等级：High | 项目：TikTok | 披露：2023-06-02 | CVE：-
- 原文：https://hackerone.com/reports/1915808

- - - - - - - - 
A Cross-Site Scripting (XSS) vulnerability was found on a TikTok.com endpoint via the 'link' parameter, which could have resulted in the ability to execute JavaScript code within a user's browser. We thank @mrhavit for reporting this to the team.
---


## XSS at TikTok Ads Endpoint
- 等级：High | 项目：TikTok | 披露：2023-01-27 | CVE：-
- 原文：https://hackerone.com/reports/1683129

- - - - - - - - 
A Cross-Site Scripting (XSS) vulnerability was found on a TikTok Ads endpoint, due to a lack of appropriate HTML escaping or output encoding on the reflection of user-supplied data, which was resolved on September 7, 2022. This could have resulted in a JavaScript payload injected into the endpoint causing it to be executed within the context of the victim's browser. We thank @s3c for reporting this to our team.
**Summary (researcher):**
I found a Cross-site scripting (XSS) and bypassed the WAF (akamai) on one of the TikTok ads endpoints and could lead it to takeover any account on ads.tiktok.com
---


## XSS Reflected on reddit.com via url path
- 等级：High | 项目：Reddit | 披露：2022-09-27 | CVE：-
- 原文：https://hackerone.com/reports/1051373

- - - - - - - - 
Hi I found a XSS-R
To reproduce the issue please click the poc link and then press the "verify email" button
PoC:
https://www.reddit.com/verification/asd',%20alert(document.location),%20%27
## Impact
With the help of XSS an attacker can steal your cookies, in many cases steal sessions, download malware onto your system and send a custom request.
Users can be socially engineered by the attacker by redirecting them from the real website to a fake one and there are many more attack scenarios that an expert attacker can perform with XSS.
It is also possible to inject html thus modifying the original page
---


## Reflected xss on videostore.mtnonline.com
- 等级：High | 项目：MTN | 披露：2022-09-25 | CVE：-
- 原文：https://hackerone.com/reports/1646248

- - - - - - - - 
## Summary:
Hi,
I found reflected xss vuln on videostore.mtnonline.com
## Steps To Reproduce:
  1. Open browser
  2. Go to ``https://videostore.mtnonline.com/GL/Default.aspx?PId=126&CId=5&OprId=11&Ctg=OF25MTNNGVS_LapsInTime%22%27testxxx%3E%3Ciframe%20src=%22data:text/html,%3C%73%63%72%69%70%74%3E%61%6C%65%72%74%28%31%29%3C%2F%73%63%72%69%70%74%3E%22%3E%3C/iframe%3E`` url
 3. Browser show alert popup
## Impact
We can run javascript code
---


## Shop - Reflected  XSS  With  Clickjacking Leads to Steal User's Cookie  In Two Domain
- 等级：High | 项目：Meredith | 披露：2022-09-14 | CVE：-
- 原文：https://hackerone.com/reports/1221942

- - - - - - - - 
Hii  Security Team ,
I am S Rahul MCEH(Metaxone Certified Ethical Hacker) and a Security Researcher I just checked your website and found Reflected XSS to Good XSS Clickjacking In Two Domain
Description:- As the search parameter is vulnerable to XSS and but the plus point is there is  no X-Frame-Header or Click-jacking Protection.So by combing this two methods the Attack Easier And Converted it to Well Working XSS on Other User’s . 
Vulnerable Urls:- https://marthastewart.com/shop/all.html?s=
                            https://bhg.com/shop/all.html?s=
		
Steps to reproduce :-
1. Navigate to  Vulnerable URLS and As we know that ?s= parameter is vulnerable to XSS 
2.As Reflec


## cross site scripting in : mtn.bj
- 等级：High | 项目：MTN | 披露：2022-08-06 | CVE：-
- 原文：https://hackerone.com/reports/1264834

- - - - - - - - 
## Summary:
Xss vulnerability in mtn.bj  in file name 
## Steps To Reproduce:
  1.Go to : 
https://www.mtn.bj/business/ressources/formulaires/plan-de-localisation-de-compte/?next=https://www.mtn.bj/business/ressources/formulaires/formulaire-de-souscription/
  2 - fill all inputs with any data 
3 - in file upload upload a file with payload file name such as : "><img src=x onerror=alert(document.cookie);.jpg
4-the payload will executed in the page .
## Supporting Material/References:
1 - video showing poc 
2 - screen shot
## Impact
execute malicious java script in user browser
---


## Corsa Site Scripting Vulnerability (XSS)
- 等级：High | 项目：Linux | 披露：2022-07-30 | CVE：-
- 原文：https://hackerone.com/reports/1650210

- - - - - - - - 
An XSS was found in Cactus, a project that is not part of the bounty program.
---


## fix(cmd-socketio-server): mitigate cross site scripting attack #2068
- 等级：High | 项目：Linux | 披露：2022-07-21 | CVE：-
- 原文：https://hackerone.com/reports/1638984

- - - - - - - - 
Please refer this fix and approve Bounty.
See this In Github [Security Fix](https://github.com/hyperledger/cactus/pull/2068)
@ryjones
(https://github.com/hyperledger/cactus/pull/2068#issuecomment-1186157206)
## Impact
fix(cmd-socketio-server): mitigate cross site scripting attack
---


## POST BASED REFLECTED XSS IN dailydeals.mtn.co.za
- 等级：High | 项目：MTN | 披露：2022-07-15 | CVE：-
- 原文：https://hackerone.com/reports/1451394

- - - - - - - - 
## Summary:
Dear Team ,
I have found a post based reflected XSS in https://dailydeals.mtn.co.za/ .
## Steps To Reproduce:
1.Create a html file with following content .
<form action="https://dailydeals.mtn.co.za/index.cfm?GO=CRAVE_ESTABLISHMENTS_LIST" method="POST"><input type="hidden" name="location_id" value="0"><input type="hidden" name="suburb" value="0"><input type="hidden" name="search_phrase" value=""><input type="hidden" name="submit_search" value="Search"><input type="hidden" name="m" value=""><input type="hidden" name="cpID" value=""><input type="hidden" name="CFID" value="a611fd5d-822a-4c08-a032-bcac1551f032'&quot;<!--><Svg OnLoad=(confirm)(1)-->"><input type="hidd


## Reflected xss in https://sh.reddit.com
- 等级：High | 项目：Reddit | 披露：2022-05-08 | CVE：-
- 原文：https://hackerone.com/reports/1549206

- - - - - - - - 
## Summary:
Reflected cross-site scripting (or XSS) arises when an application receives data in an HTTP request and includes that data within the immediate response in an unsafe way.
## Impact:
attacker can execute malicious java script and steal cookies 
## Steps To Reproduce:
[add details for how we can reproduce the issue]
Hi team ,
Navigate to below url 
scroll to page end find a option see more
Move mouse over there and observe the execution of javascript 
## Supporting Material/References:
[list any additional material (e.g. screenshots, logs, etc.)]
  * [attachment / reference]
## Impact
attacker can execute malicious java script and steal cookies
---


## Reflected xss on ads.tiktok.com using `from` parameter.
- 等级：High | 项目：TikTok | 披露：2022-02-09 | CVE：-
- 原文：https://hackerone.com/reports/1452375

- - - - - - - - 
A XSS (cross-site scripting) vulnerability was found on a TikTok ads endpoint using the "from" parameter. We thank @imran_nisar for reporting this to our team and confirming its resolution.
---


## Reflected xss в m.vk.com/chatjoin
- 等级：High | 项目：VK.com | 披露：2021-11-05 | CVE：-
- 原文：https://hackerone.com/reports/316475

- - - - - - - - 
XSS в мобильных сообщениях.
---


## Reflected Cross-Site scripting in : mtn.bj
- 等级：High | 项目：MTN | 披露：2021-09-26 | CVE：-
- 原文：https://hackerone.com/reports/1264832

- - - - - - - - 
Hello Team 
I have found a Reflected XSS vulnerability in mtn.jb by file name 
## Steps To Reproduce:
[add details for how we can reproduce the issue]
  1. go to : 
████
  2. enter any email and press  Suivant
  3. fill all the inputs by any data .
  4. in file upload upload any photo with payload file name : "><img src=x onerror=alert(document.cookie);.jpg
  5 . the payload executed in the page  
Supporting Material/References:
1 - video showing poc 
2 - screenshot
## Impact
An attacker can use XSS to send a malicious script to an unsuspecting user. The end user’s browser has no way to know that the script should not be trusted, and will execute the script. Because it think


## Mattermost Server OAuth Flow Cross-Site Scripting
- 等级：High | 项目：Mattermost | 披露：2021-08-06 | CVE：CVE-2021-37859
- 原文：https://hackerone.com/reports/1216203

- - - - - - - - 
## Summary:
The vulnerability is a reflected Cross-Site Scripting (XSS) via the OAuth flow. A victim clicking a malicious link pointing to the target Mattermost host will trigger the XSS. If the victim is a regular user, it is possible to obtain all of their Mattermost chat contents; if it’s an administrator, it is possible to create a new administrator.
## Root Cause Analysis:
The application fails to sanitize an HTTP query parameter before reflecting it within the HTML response during the OAuth flow.
[code omitted]
The file "/web/oauth.go" (https://github.com/mattermost/mattermost-server/blob/master/web/oauth.go) contains the function "completeOAuth" which on line 284 valu


## Cross site scripting
- 等级：High | 项目：Informatica | 披露：2021-05-17 | CVE：-
- 原文：https://hackerone.com/reports/1095797

- - - - - - - - 
Researcher identified a XSS vulnerability in a service used by Informatica. Informatica worked with the vendor to patch their service for us and all other customers of the vendor. 
Thanks rawezh_ali for your responsible disclosure.
---


## Reflected/Stored XSS on duckduckgo.com
- 等级：High | 项目：DuckDuckGo | 披露：2021-04-10 | CVE：-
- 原文：https://hackerone.com/reports/1110229

- - - - - - - - 
Hi DuckDuckGo,
While browsing normally (since I use DuckDuckGo on a daily basis), I discovered an interesting stored XSS on the duckduckgo main search engine. A payload that somebody had left on urbandictionary.com had triggered a HTML injection, and a stored XSS as a result. 
**Steps to Reproduce**
1. Search the following in the searchbar of DuckDuckGo: `urban dictionary "><img src=x<`
2. A payload left by someone else will render itself and fire in the main DuckDuckGo page.
3. It is also possible to visit the page via the DuckDuckGo URL as [such](https://duckduckgo.com/?q=urban+dictionary+%22%3E%3Cimg+src%3Dx%3C&t=ffab&atb=v1-1&ia=web) and the XSS will trigger.
**POC**
- T


## Reflected XSS on transact.playstation.com using postMessage from the opening window
- 等级：High | 项目：PlayStation | 披露：2021-03-30 | CVE：-
- 原文：https://hackerone.com/reports/900619

- - - - - - - - 
## Report Summary:
When `transact.playstation.com` loads it handles messages received from `postMessage` in the `_receiveMessageFromTransactClientService` method. The only validation that is performed is to ensure that the referrer and origin match:
[code omitted]
These checks can be passed by using `win = window.open("https://transact.playstation.com/")` to launch a new window, then send messages with `win.postMessage`.  This allows a few functions to be called, including `replaceRoute` which allows the current ember route and model to be set:
[code omitted] 
After looking at a few of the routes, `voucher.multi-product-details` has a `sku.longDescription` on the model that 


## Download full backup and Cross site scripting
- 等级：High | 项目：ImpressCMS | 披露：2020-12-06 | CVE：-
- 原文：https://hackerone.com/reports/1049040

- - - - - - - - 
A backup zip file was still left on the server, which was removed. Moreover, an old unused content editor was still left and could be used by a malicious user. The unused editor has been removed as well.
---


## Cross-Site-Scripting on www.tiktok.com and m.tiktok.com leading to Data Exfiltration
- 等级：High | 项目：TikTok | 披露：2020-11-19 | CVE：-
- 原文：https://hackerone.com/reports/968082

- - - - - - - - 
The researcher discovered a URL parameter reflecting its value without being properly sanitized and was able to achieve reflected XSS. In addition, researcher found an endpoint which was vulnerable to CSRF.
The endpoint allowed to set a new password on accounts which had used third-party apps to sign-up. Researcher combined both vulnerabilities to achieve a "one click account takeover".
**Summary (researcher):**
While fuzzing, I discovered a URL parameter reflecting its value without being properly sanitized. Thus, I was able to achieve **reflected XSS**. In addition, I found an endpoint which was **vulnerable to CSRF**.
The endpoint enabled me to set a new password on accou


## Reflected XSS on a Atavist theme at external_import.php
- 等级：High | 项目：Automattic | 披露：2020-11-18 | CVE：-
- 原文：https://hackerone.com/reports/976657

- - - - - - - - 
## Summary:
Hi team,
I found this php file https://magazine.atavist.com/static/external_import.php , and there is a parameter called `scripts` on this php file. 
Basically, the endpoint prints value of `scripts` parameter to `<script src='$Value'>`.
So we can import any script file like that : https://magazine.atavist.com/static/external_import.php?scripts=//15.rs
Or we can write HTML tags too, there is no encoding : https://magazine.atavist.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscript%3Ealert(1)%3C/script%3E
This endpoint is also available on other websites. Like :
https://docs.atavist.com/static/external_import.php?scripts=%27%3E%3C/script%3E%3Cscrip


## SafeParamsHelper::safe_params is not so safe
- 等级：High | 项目：GitLab | 披露：2020-11-02 | CVE：-
- 原文：https://hackerone.com/reports/946728

- - - - - - - -


## Cross-site Scripting (XSS) - Reflected
- 等级：High | 项目：8x8 | 披露：2020-07-07 | CVE：-
- 原文：https://hackerone.com/reports/503988

- - - - - - - - 
The password reset page of the managers portal of VCC reflected input of the **tenant** parameter without proper encoding considerations.
**Summary (researcher):**
Just wanted to disclose as it's my first ever report on h1.
---


## Reflected cross-site scripting vulnerability on a DoD website
- 等级：High | 项目：U.S. | 披露：2020-05-14 | CVE：-
- 原文：https://hackerone.com/reports/774792

- - - - - - - - 
Hello there !
I'd like to report a 'XSS' vulnerability on a DoD website *https://███/unit/███ ,
Here in the search engine of the website please enter the following payloads <script>alert(document.domain)</script> & you can even use this payload to steal cookies <script>alert(document.cookie)</script> and hit enter and just scroll you're mouse below the Term: <script>alert(document.domain)</script> to the three icons and as soon as you scroll you're mouse over that three icons you will notice the " pop-up "
FOR CLEAR DEMONSTRATION OF THE VULNERABILITY PLEASE REFER TO THE PROOF-OF-CONCEPT ATTACHED TO THIS REPORT.
Thanks,
████
## Impact
XSS vulnerabilities can be used to trick 


## The URL in "Choose a data source'' at "https://bi.owox.com/ui/settings/connected-services/setup/" is not filtered => reflected XSS.
- 等级：High | 项目：OWOX, | 披露：2019-12-09 | CVE：-
- 原文：https://hackerone.com/reports/733051

- - - - - - - - 
Hi team,
This is another report with #732987. Because it is completely independent
Detail
--
In the process of selecting the data source at https://bi.owox.com/ui/settings/connected-services/setup/, I found a reflected XSS.
Specifically, when you click on ``Google Analytics``, a page will appear for you to enter ``Gmail``. After completing the steps, an error link will appear during the redirect (Screenshot)
███
Vulnerable area:
----
``/analytics/``
The URL will now be: https://bi.owox.com/ui/callbacks/google-supervisors/analytics%3Cimg%20src=xss%20onerror=prompt(1)%3E/?state=d159b8264eef78b11afdd016531b128c&code=4/tAFEdKitWAD6NCxUfXRT4NMTLMnzMwHeDlac-un9ecDEce9Ts2EZ6_pN-giK


## Reflected XSS
- 等级：High | 项目：OWOX, | 披露：2019-12-09 | CVE：-
- 原文：https://hackerone.com/reports/732987

- - - - - - - - 
Hi team,
I have found an XSS at https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28/dashboard/?trial=activated
Because the input is not properly filtered, resulting in XSS being executed
Vulnerable area: 
-----
``6177527534dc114eb07fa829e4ce4d28``
The URL will now be: https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated
PoC
---
1, go to https://bi.owox.com/ui/6177527534dc114eb07fa829e4ce4d28%3Cimg%20src=xss%20onerror=prompt('XSS')%3E/dashboard/?trial=activated
2, Log in and ``XSS`` will execute
██████████
Tested browser
---
Firefox 
Chrome
## Impact
This vulnerability is aimed at all victims and the


## Reflective Cross-site Scripting via Newsletter Form
- 等级：High | 项目：Shopify | 披露：2019-10-11 | CVE：-
- 原文：https://hackerone.com/reports/709336

- - - - - - - - 
*.myshopify.com is vulnerable to a reflective cross-site scripting attack in the newsletter form. This can be crafted to trigger on a page load without any further user interaction.
The following example url shows this vulnerability:
[code omitted]
This was tested on a newly registered store "testbuguser.myshopify.com"
If you require any additional details, please do not hesitate to bump.
## Impact
This attack could be leveraged to compromise administrative sessions or perform actions on behalf of users with the same level of privilege as the user.
**Summary (researcher):**
This is a reflective cross-site scripting in the newsletter signup feature of *.myshopify.com websites


## Reflected XSS on https://make.wordpress.org via 'channel' parameter
- 等级：High | 项目：WordPress | 披露：2019-08-26 | CVE：-
- 原文：https://hackerone.com/reports/659419

- - - - - - - - 
Hi there,
I just found a reflected XSS on make.wordpress.org domain.
steps to reproduce : 
1. visit this link :
https://make.wordpress.org/chat/logs?channel=16%22%3E%3Cimg%20src=x%20onerror=alert(document.domain)%3E&date=2019-07-21&no_bots=1
2. xss pop up will occurs
POC:
see:wp reflected xss.png
Note: it works on the latest version of firefox
## Impact
some of xss impact like stealing cookies, session hijacking, etc ..
---

