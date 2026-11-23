# HackerOne 实战案例：cross-site-scripting-xss-generic

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## New XSS vector in ReaderMode with %READER-TITLE-NONCE%
- 等级：Critical | 项目：Brave | 披露：2023-06-22 | CVE：-
- 原文：https://hackerone.com/reports/1436142

- - - - - - - - 
## Summary:
Previously, script execution in ReaderMode pages was prohibited by CSP. However, three months ago, [this commit](https://github.com/brave/brave-ios/pull/4209/files#diff-eaeef15a290e9e5e9bcaae784f18d874f8c932dfa3de416a5820eccd6b2d8cfbR54) partially relaxed the CSP and scripts with `nonce-%READER-TITLE-NONCE%` are now allowed to be executed. This relaxation of the CSP rule can be exploited for XSS attacks on ReaderMode pages.
Here, the attack vector is `%READER-CREDITS%` which is also [included in the ReaderMode HTML template](https://github.com/brave/brave-ios/blob/6f667506228eeff77daf4df7c9dddae22eb0ad1b/Client/Frontend/Reader/Reader.html#L18). The `%READER-CREDI


## Subdomain takeover due to an unclaimed Amazon S3 bucket on ███
- 等级：Critical | 项目：U.S. | 披露：2020-09-03 | CVE：-
- 原文：https://hackerone.com/reports/918946

- - - - - - - - 
**Summary:**
An unclaimed Amazon S3 bucket on █████████ gives an attacker the possibility to gain full control over this subdomain.
**Description:**
`███████` pointed to an S3 bucket that did no longer exists. The bucket points to an Amazon S3 website bucket in the US East region. I claimed this bucket and successfully took over this subdomain. 
Note:
I am reporting this issue to DoD since: "████████ ██████" The ████████ is linked to ███, so I believe this belongs here. I discovered this domain initially from the DoD websites list. Please excuse if this is a misconception. 
## Impact
This is extremely vulnerable to attacks as a malicious user could create any web page with a


## Html Injection and Possible XSS via MathML
- 等级：Critical | 项目：X | 披露：2019-09-03 | CVE：-
- 原文：https://hackerone.com/reports/502926

- - - - - - - - 
Hi,
I would like to report HTML Injection and possible cross site scripting (XSS) vulnerability using the MathML on Firefox.
Account title of field is vulnerable to Html Injection which can lead an attacker to store javascript using the MathML in Firefox.
Modern Firefox versions allow usage of inline MathML. While other user agents don't support the href attribute for MathML elements (yet), Firefox does and thereby enables passive JavaScript execution. Note that supporting href for MathML elements is a feature - introduced with MathML 3. The same effect can be observed by using xlink:href. The statusline action further enables obfuscation of the actual link target - and in t


## The react-marked-markdown module allows XSS injection in href values.
- 等级：Critical | 项目：Node.js | 披露：2018-05-13 | CVE：-
- 原文：https://hackerone.com/reports/344069

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to triage and respond quickly, so be sure to take your time filling out the report!
I would like to report XSS in react-marked-markdown.
The react-marked-markdown module incorrectly sanitizes href values and allows arbitrary code injection (XSS) via user provided Markdown.
# Module
**module name:** react-marked-markdown
**version:** 1.4.6
**npm page:** `https://www.npmjs.com/package/1.4.6`
## Module Description
A react components package that helps you use Markdown easily.
## Module Stats
> Replace


## Cross-site Scripting (XSS) in /updates-pro/archive/
- 等级：Critical | 项目：MapsMarker.com | 披露：2017-07-02 | CVE：-
- 原文：https://hackerone.com/reports/235866

- - - - - - - - 
Hey guys.
The dir parameter on /updates-pro/archive/ seems to be vulnerable to Cross-site Scripting.
Steps to reproduce:
1- Navigate to: https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1
2- Add this to the url: <svG onLoad=prompt(9)>
3- Result in attached printsceen.
Or quite simple visit:
https://www.mapsmarker.com/updates-pro/archive/?dir=v3.0.1%3CsvG%20onLoad=prompt(1)%3E
---


## Potential XSS Vulnerability in Acronis Login Callback URL
- 等级：High | 项目：Acronis | 披露：2024-11-06 | CVE：-
- 原文：https://hackerone.com/reports/2611305

- - - - - - - - 
## Summary
The login callback URL, https://learn.acronis.com/portal/, is vulnerable to Cross-Site Scripting (XSS) attacks. When a user logs in and is redirected to this URL, the redirectUrl parameter is not properly sanitized, allowing an attacker to inject arbitrary JavaScript code. This code could be used to steal the user's session cookie, perform phishing attacks, or deface the website.
## Steps To Reproduce
I was able to exploit this vulnerability by crafting a URL that included malicious JavaScript code in the redirectUrl parameter. When a user clicks on this URL and logs in, the injected code is executed in the user's browser.
For example, the following URL would disp


## XSS from Mastodon embeds
- 等级：High | 项目：IRCCloud | 披露：2023-10-09 | CVE：-
- 原文：https://hackerone.com/reports/1887917

- - - - - - - - 
By default, the IRCCloud web client embeds Mastodon toots when a link to one is sent. Anyone can run a Mastodon server, and so the server from which toot data is fetched might be malicious. It is possible for an attacker to cause a web client user to execute arbitrary JavaScript in the context of the IRCCloud web client by tricking the web client into embedding a `javascript:` URL.
**POC**:
1. Ensure "Embed social media links" is enabled in settings under "Chat & embeds" (I think this is on by default)
2. Send a message with a link to https://sm4.ca/@a/123456789012345678 (the link itself 404s but IRCCloud only tries to use Mastodon API so it doesn't matter)
3. Wait a few sec


## yelp.com XSS ATO (via login keylogger, link Google account)
- 等级：High | 项目：Yelp | 披露：2023-08-15 | CVE：-
- 原文：https://hackerone.com/reports/2010530

- - - - - - - - 
# Summary:
yelp.com reflects the content of the cookie `guvo` in the html returned to the user. In some cases this value is not properly escaped, leading to XSS. This can be combined with another issue where the backend does not properly parse the user supplied cookies and allows us to smuggle a `guvo` cookie inside a cookie named `yelpmainpaastacanary`. The `yelpmainpaastacanary` cookie can be set by including a URL query parameter `?canary=[Cookie value]`  in any request to `*.yelp.com`.
This report shows how chaining this cookie XSS with a cookie parsing issue leads to persistent XSS in a victims browser. To demonstrate impact I'll show how this can be used to inject a ke


## XSS on rockstargames.com
- 等级：High | 项目：Rockstar | 披露：2023-07-25 | CVE：-
- 原文：https://hackerone.com/reports/212700

- - - - - - - - 
In this report, the researcher reported a reflected Cross-Site Scripting (XSS) vulnerability on the Max Payne 3 sub-site on rockstargames.com. The vulnerability has since been resolved.
---


## Universal XSS through FIDO U2F register from subframe
- 等级：High | 项目：Brave | 披露：2023-06-22 | CVE：-
- 原文：https://hackerone.com/reports/993670

- - - - - - - - 
## Summary:
There are three weaknesses in Brave's FIDO U2F implementation.
* `u2f.register()` can be executed from cross-origin subframe by invoking [U2F.postMessage](https://github.com/brave/brave-ios/blob/e52c52495aa654584abe8172d689977756e6549d/Client/Frontend/UserContent/UserScripts/U2F.js#L264) directly
* Then, FIDO related modals show the name of top frame origin (but not caller subframe)
* The `version` parameter sent from the above `postMessage` is embedded in an [evaluateJavaScript](https://github.com/brave/brave-ios/blob/d01b8c07b8a6244af48798efe4afeccd266707e2/Client/WebAuthN/U2FExtensions.swift#L1003) without escape
The combination of these weaknesses allows cros


## XSS on internal: privileged origin through reader mode
- 等级：High | 项目：Brave | 披露：2023-06-22 | CVE：-
- 原文：https://hackerone.com/reports/1438028

- - - - - - - - 
## Summary:
Brave iOS has two weaknesses described below. By combining them, XSS can be achieved on the privileged origin `internal://local`.
1. Exposure of uuidKey through REFERER header
Reader mode in Brave has two HTML templates, [Reader.html](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html) and [ReaderViewLoading.html](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/ReaderViewLoading.html). The former template defines [<meta name="referrer" content="never">](https://github.com/brave/brave-ios/blob/development/Client/Frontend/Reader/Reader.html#L10) header for preventing referrer leakage, but the latter tem


## UXss on brave browser via scan QR Code
- 等级：High | 项目：Brave | 披露：2023-04-11 | CVE：CVE-2022-23258
- 原文：https://hackerone.com/reports/1884042

- - - - - - - - 
## Summary:
I found UXss in your browser, and executed Xss on all open domains.
before that I want to tell you a little, that I've found a vulnerability like this in Microsoft Edge :
https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2022-23258
Oppo browser : (Private/no disclosure)
and now i found it in your application
## Products affected: 
 * Android 13, Brave browser version 1.48.164,  Brave Nightly browser version 1.50.53, Brave Beta Browser version 1.49.106, Chromium 110.5481.100
Payload : {F2191688}
This is a QR Code containing the url : javascript:alert(document.domain);
which the attacker will use to attack the victim
## Steps To Reproduce:
- Open Brav


## CSP-bypass XSS in project settings page
- 等级：High | 项目：GitLab | 披露：2022-11-16 | CVE：-
- 原文：https://hackerone.com/reports/1588732

- - - - - - - -


## XSS: `v-safe-html` is not safe enough
- 等级：High | 项目：GitLab | 披露：2022-11-16 | CVE：-
- 原文：https://hackerone.com/reports/1579645

- - - - - - - - 
`v-safe-html` directive uses Dompurify [to remove](https://gitlab.com/gitlab-org/gitlab-ui/-/blob/9f1bcb1f7392d4d6d072f10197c2aab2c29c3287/src/directives/safe_html/constants.js#L3)  `data-remote', 'data-url', 'data-type', 'data-method'` attributes from HTML tags. Rails-js relies on another attribute, [`data-disable-with`](https://github.com/rails/rails/blob/v6.1.4.7/actionview/app/assets/javascripts/rails-ujs.coffee#L10) to [show a HTML content](https://github.com/rails/rails/blob/v6.1.4.7/actionview/app/assets/javascripts/rails-ujs/features/disable.coffee#L41) when an user clicks on a disabled link.
For example, the following text will bypass the sanitization and popup an a


## XSS in ZenTao integration affecting self hosted instances without strict CSP
- 等级：High | 项目：GitLab | 披露：2022-09-22 | CVE：-
- 原文：https://hackerone.com/reports/1542510

- - - - - - - -


## Blind XSS in app.pullrequest.com/████████ via /reviews/ratings/{uuid}
- 等级：High | 项目：HackerOne | 披露：2022-05-25 | CVE：-
- 原文：https://hackerone.com/reports/1558010

- - - - - - - - 
**Summary:**
Hi,
While researching PullRequest yesterday, I saw some "review" endpoints in web archive of "app.pullrequest.com". (http://web.archive.org/cdx/search/cdx?url=app.pullrequest.com/*&output=text&fl=original&collapse=urlkey)
One of them was https://app.pullrequest.com/reviews/ratings/6eaa6b75-b958-4530-ba46-0d00cbe74e0b/false , I went to that endpoint and filled the all fields with my blind XSS payload.
`'"><img src=x id=█████ onerror=eval(atob(this.id))>`
This payload sends an alert to my blind XSS application in `██████`
Today (May 3, 2022, 6:09 pm UTC+3), I got a lot of alerts from https://app.pullrequest.com/███. I checked the report and I see it came from an P


## Email templates XSS by filterXSS bypass
- 等级：High | 项目：Judge.me | 披露：2022-05-25 | CVE：-
- 原文：https://hackerone.com/reports/1404804

- - - - - - - - 
## Summary:
`js-xss` is used to prevent XSS on email templates previews but the custom `onIgnoreTag` function can be used to bypass this filter. This leads to a Self-XSS scenario that can be used to achieve Account Takeover in 1-click.
[code omitted]
## XSS
The way how `js-xss` parse tags starting with `<![` differ from how browser parse it, so it's possible to abuse this in this way:
[code omitted]
Sending this as the HTML email template will trigger an XSS when the email is previewed. Since email templates are private and only the owner of the template can preview it, this can be considered a Self-XSS. But there is a way to do another user preview it, leading to an account


## Universal Cross-Site Scripting vulnerability
- 等级：High | 项目：Proctorio | 披露：2021-12-14 | CVE：-
- 原文：https://hackerone.com/reports/1326264

- - - - - - - - 
Sector7.nl notified Proctorio that there was a universal cross-site scripting vulnerability within the browser extension on June 17th, 2021. This vulnerability was patched on June 24th, 2021. Sector7.nl and other researchers were notified on June 25th. On August 3rd, 2021 Sector7.nl confirmed the vulnerability was successfully patched.
---


## Android WebViews in Twitter app are vulnerable to UXSS due to configuration and CVE-2020-6506
- 等级：High | 项目：X | 披露：2020-09-24 | CVE：CVE-2020-6506
- 原文：https://hackerone.com/reports/906433

- - - - - - - - 
## Summary:
CVSS score: 8.1 / High / CVSS:3.0/AV:N/AC:L/PR:N/UI:R/S:U/C:H/I:H/A:N
**Embargo notice: Do Not Disclose publicly until https://crbug.com/1083819 is disclosed.**
Twitter for Android is affected by a UXSS vulnerability due to its configuration of Android WebView and CVE-2020-6506.
Vendor mitigation is recommended to protect unpatched WebView users, due to its impact and ease of exploitation. Mitigation options which minimize breaking changes are provided for various use cases.
Android WebView is the system component which allows Android apps to display web pages. Apps typically use Android WebView directly or via frameworks/libraries.
CVE-2020-6506 is a universal c


## Cross-Site Scripting (XSS) on www.starbucks.com | .co.uk login pages
- 等级：High | 项目：Starbucks | 披露：2020-06-30 | CVE：-
- 原文：https://hackerone.com/reports/881115

- - - - - - - - 
Hi team,
**Summary:** 
There is a cross-site scripting vulnerability on the login page of  www.starbucks.com and various regions, due to improper escaping on the URL path.
**Description:**
The login page at https://www.starbucks.com/account/signin builds several links by the relative URL path. An attacker can actually control the relative path: 
{F839656}
Furthermore, the application does not escape certain characters –  allowing us to break out of the tags and inject a malicious event handler.
**Platform(s) Affected:** 
- https://www.starbucks.com/account/signin
- https://www.starbucks.co.uk/account/signin
## Steps To Reproduce:
  1. Open Chrome or Firefox
  2. Visit `https


## URL Advisor component in KIS products family is vulnerable to Universal XSS
- 等级：High | 项目：Kaspersky | 披露：2019-08-28 | CVE：-
- 原文：https://hackerone.com/reports/463915

- - - - - - - - 
**Summary**
In Microsoft Edge, URL Advisor UI is served as first-party content on every domain. So the XSS vulnerability I found in this UI automatically applies to all websites, it allows running code in the context of *any* domain.
**Description**
URL Advisor frame is located under https://www.google.com/<INJECT_ID>/ua/url_advisor_balloon.html and https://www.yahoocom/<INJECT_ID>/ua/url_advisor_balloon.html in Microsoft Edge (always the same INJECT_ID value). It gets its content from a message sent via `window.postMessage()` without validating message origin. Under some circumstances it will assign that data as link target, so a malicious website can make that link point t


## Account Takeover in Periscope TV
- 等级：High | 项目：X | 披露：2018-09-06 | CVE：-
- 原文：https://hackerone.com/reports/317476

- - - - - - - - 
**Summary:** 
When you login periscope.tv using twitter, and change the host header from `www.periscope.tv` to `attacker.com/www.periscope.tv`, the oauth redirect destination will be `attacker.com/www.periscope.tv`, thus allowing attacker to send the oauth authorize link to victim, and takeover their account after auto redirect.
## Steps To Reproduce:
Visit https://www.periscope.tv/ and click login with twitter, a request should appear
[code omitted]
Change the host header to 
`Host: hackerone.com/www.periscope.tv`
Full request
[code omitted]
Response should be something like 
[code omitted]
Send this link to victim, after authorizing, victim's twitter oauth token and verifi


## XSS on https://www.starbucks.co.uk (can lead to credit card theft) (/shop/paymentmethod)
- 等级：High | 项目：Starbucks | 披露：2018-05-22 | CVE：-
- 原文：https://hackerone.com/reports/227486

- - - - - - - - 
Hi,
**Steps to reproduce:**
0. Run Firefox (these steps *require* Firefox).
1. Log in on https://www.starbucks.co.uk/account/signin
2. Go to https://www.starbucks.co.uk/shop/card/egift and add any card to your basket.
3. Go to https://www.starbucks.co.uk/shop/paymentmethod?==%u0022a%20onclick=confirm(/-/g+this.ownerDocument.domain)%20id=%u0022checkoutButton
4. After the page finishes loading click the "Checkout" title.
5. A confirmation prompt is shown showing the current domain.
**Note** that these steps can be automated due to missing CSRF protection on the "Add to Basket" option. Effectively, all a user has to do is to load a page which is under attacker's control. I set 


## Html injection mycrypto.com
- 等级：High | 项目：MyCrypto | 披露：2018-03-16 | CVE：-
- 原文：https://hackerone.com/reports/324548

- - - - - - - - 
Hello. I remembered that a couple of months ago I found an HTML injection vulnerability on myetherwallet.com, I sent it, but my message was ignored.
Since you have the same interface, I decided to check this vulnerability on your site and it was reproduced. The vulnerability works both on www.mycrypto.com and on mycrypto.com.
Html injection is in a pop-up message
 <div class = "alert-message ng-binding" ng-bind-html = "alert.message"> You are successfully connected
<br> URL: <strong> https://www.mycrypto.com/?txHash=qwqwq%3C%20SRC=%22jav
ascript: alert (0); "& gt; <a href="https://securityz.net"> <img src =" https://securityz.net/mycrypto.jpeg "> </a> qwqw # check- tx-status


## Stored XSS / Bypassing .htaccess protection in http://nodebb.ubnt.com/
- 等级：High | 项目：Ubiquiti | 披露：2017-09-28 | CVE：-
- 原文：https://hackerone.com/reports/202354

- - - - - - - - 
Hello,
While I was looking at your renewn SSL certificated, I have noticed the following link : http://nodebb.ubnt.com/
I have seen that this link was protected by htaccess password, but I have decided to run a nmap scan. By running the following :
[code omitted]
one of the open ports was this : `4567/tcp open   tram?`
And, to my surprise the ip `104.131.159.88:4567`, as well as `http://nodebb.ubnt.com:4567/` were available from internet and unprotected.
Here, I have found a nodeBB instance and I have managed to create a persisted XSS by using the  upload API, that does not properly sanitize the file names and automatically sets wrong mime types. 
Normally, it seems that the


## Store XSS on Informatica University via transcript (informatica.csod.com)
- 等级：High | 项目：Informatica | 披露：2017-09-09 | CVE：-
- 原文：https://hackerone.com/reports/219509

- - - - - - - - 
Hi,
Vulnerable field: Training Description
Steps to reproduce:
1. Login to your account and go Informatica University.
2. You can either click on "My Training" or "Universal Profile" at the upper right hand corner of the page.
3. You will then be redirected to the Universal profile bio page, click on the "Transcript tab"
4. Select options on the upper right side then select "Add external training: on the drop down option.
5. Fill out the needed information but for the Training Description use the following payload:
'"><img src=x onerror=alert(document.cookie);>
6. Complete the rest of the form and click on Submit.
7. You will then be redirected to your training transcript.
8


## Stored XSS on Admin Access Page - Email field
- 等级：High | 项目：Revive | 披露：2017-08-02 | CVE：-
- 原文：https://hackerone.com/reports/173501

- - - - - - - - 
"Cricetinae" :)
###Short Description
The **Email** field is not sanitized on **Inventory > Admin Access** page resulting in to Stored Cross-Site Scripting vulnerability.
###Vulnerability Details
Cross-Site Scripting issue let's one to run a javascript of choice. It helps most of the client side risks including but not limited to phishing, temporary deface, browser key-logger and others. Exploitation frameworks like BeEF eases the offensive attack.
Stored XSS is more risky than the reflected ones because of the fact that the malicious script is persisted across. It can affect all the time and all the users who has the access to the page.


## Wordpress 4.7.2 - Two XSS in Media Upload when file too large.
- 等级：High | 项目：WordPress | 披露：2017-07-17 | CVE：-
- 原文：https://hackerone.com/reports/203515

- - - - - - - - 
Description
-------------------
An attacker can inject a malicious script in to the filename which a victim tries to upload leading to XSS inside the administrators control panel.
Two different "file to large" cases end up in interpolating the file name and appending it into DOM unsanitized leading to XSS.
I have attached pictures of one of the cases, in the attached case the file was 12.4 MB, in a freshly installed environment. For reproduction note that any file type can be used (.jar whatever) as the vuln happens before the type is validated.
PoC
-------------------
Create a 20MB file called 
`Dinosaurs secret life<img src=x  onerror=alert(1)>.png`
Goto your wordpress sit


## MailPoet Newsletters <= 2.7.2 - Authenticated Reflected Cross-Site Scripting (XSS)
- 等级：High | 项目：Eternal | 披露：2017-06-17 | CVE：-
- 原文：https://hackerone.com/reports/200355

- - - - - - - - 
Hello __Team__
__Abstract__:-
A Cross-Site Scripting vulnerability was found in the MailPoet Newsletters plugin. This issue allows an attacker to perform a wide variety of actions, such as stealing Administrators' session tokens, or performing arbitrary actions on their behalf. In order to exploit this issue, the attacker has to lure/force a logged on WordPress Administrator into opening a URL provided by an attacker.
__Introduction__:-
The MailPoet Newsletters plugin allows a WordPress administrator to create newsletters, automated emails, post notifications and autoresponders. A Cross-Site Scripting vulnerability was found in the MailPoet Newsletters plugin. This issue all


## XSS in $shop$.myshopify.com/admin/ via twine template injection in "Shopify.API.Modal.input" method when using a malicious app
- 等级：High | 项目：Shopify | 披露：2017-06-01 | CVE：-
- 原文：https://hackerone.com/reports/217790

- - - - - - - - 
#Description
The Shopify [Embedded App SDK](https://help.shopify.com/api/sdks/merchant-apps/embedded-app-sdk) is used to facilitate limited interactions with parent page (`/admin/apps/$id`) from an embedded app within the shop admin interface. The SDK has multiple methods which allow an app to interact with the user which execute in the context of the admin domain and pass information back to the app. These UI elements are rendered from predefined templates using [lodash](https://lodash.com)'s [_.template](https://lodash.com/docs/4.17.4#template) method. While the method automatically provides input escaping the "input" template (used by the `Shopify.API.Modal.input` method)


## XSS in $shop$.myshopify.com/admin/ via "Button Objects" in malicious app
- 等级：High | 项目：Shopify | 披露：2017-05-22 | CVE：-
- 原文：https://hackerone.com/reports/217745

- - - - - - - - 
This report is similar in impact, exploitability and root-cause as report #205701 requiring an additional step of user-interaction. 
#Description
The Shopify [Embedded App SDK](https://help.shopify.com/api/sdks/merchant-apps/embedded-app-sdk) is used to facilitate limited interactions with parent page (`/admin/apps/$id`) from an embedded app within the shop admin interface. The SDK has multiple methods which accept a `buttons` parameter which is defined under the [button objects](https://help.shopify.com/api/sdks/shopify-apps/embedded-app-sdk/methods#button-objects) section of the SDK documentation. Buttons can define a `href` parameter which will open when the button is cli


## Stored XSS in community.ubnt.com
- 等级：High | 项目：Ubiquiti | 披露：2017-04-28 | CVE：-
- 原文：https://hackerone.com/reports/179164

- - - - - - - - 
I have created two accounts
one attacker account: vibhuti123_i
other victim account: John_victim
 attacker account:vibhuti123_i who will create a malicious link after uploading svg file embeded with script and doing stored xss.Now attacker vibhuti123_i will send this  stored xss malicious link to victim:john_victim by posts,message,reply of ubnt community features or anyother way of communication.After this John_victim will believe this link as it is saved on community.ubnt.com server.It's no way look dangerous so john_victim will click this link and xss gets executed.
This stored xss link created by attacker will execute in every account and also it is accessible without lo


## Bypass to postMessage origin validation via FTP
- 等级：High | 项目：Slack | 披露：2017-04-21 | CVE：-
- 原文：https://hackerone.com/reports/210654

- - - - - - - - 
@a1kmm- discovered a bypass to our postMessage origin check, wherein an attacker with existing MITM capabilities could use FTP to bypass validation and view XOXS tokens of victims on the local network. This was related to, and investigated at the same time as, a previous report. This issue is now resolved and was not exploited. Thanks @a1kmm-!
---


## upgrade Aspen on inside.gratipay.com to pick up CR injection fix
- 等级：High | 项目：Gratipay | 披露：2017-03-22 | CVE：-
- 原文：https://hackerone.com/reports/143139

- - - - - - - - 
1) Using IE11, open DevTools and start network capture
2) visit the following URL:
http://inside.gratipay.com/assets/%0dSet-Cookie:%20qwe=qwe%0dq
3) find a 'qwe' cookie set in the response
There is a 0x0d character injected, which can be used as a header
delimiter in IE.
To see this behaviour using Curl, you can use the following command:
curl -s -v 'http://inside.gratipay.com/assets/%0dSet-Cookie:%20qwe=qwe%0dq' 2>&1|less
Screenshots of Curl output and DevTools are attached.
---


## Reflected XSS in U2F plugin by shipping the example endpoints
- 等级：High | 项目：Nextcloud | 披露：2017-03-22 | CVE：-
- 原文：https://hackerone.com/reports/192786

- - - - - - - - 
While running a [RIPS scan](https://www.ripstech.com/) against our [instrumentalized source code](https://github.com/nextcloud/php-static-scanner-instrumentalization) it noticed that the file `/apps/twofactor_u2f/vendor/yubico/u2flib-server/examples/localstorage/index.php` echoes on user input:
{F145451}
I was first a tad confused because [the examples have been removed from our Git repository](https://github.com/nextcloud/twofactor_u2f/tree/3321e0dc84208adb623b6843f72e81782d9f2b6e/vendor/yubico/u2flib-server), but the release from apps.nextcloud.com ships with that file. So I suppose the Makefile is downloading the dependencies again.
While exploiting this is not entirely t


## Stored cross-site scripting (XSS) on a DoD website
- 等级：High | 项目：U.S. | 披露：2017-03-16 | CVE：-
- 原文：https://hackerone.com/reports/183971

- - - - - - - - 
A stored cross-site scripting vulnerability was found on a Department of Defense website which may trick a web user into executing a malicious script, potentially revealing a user's web session information or modify web content. @jon_bottarini was able to demonstrate this vulnerability by crafting a specially formatted URL. Thanks @jon_bottarini!
---


## Subdomain Takeover (moderator.ubnt.com)
- 等级：High | 项目：Ubiquiti | 披露：2017-02-06 | CVE：-
- 原文：https://hackerone.com/reports/181665

- - - - - - - - 
Hello __Team__
This report is same as #179110
One of your subdomain http://moderator.ubnt.com is pointing towards
[code omitted]
{F134183}
And it is unclaimed
When I open it 
it is showing 
{F134184}
__Impact__ :-
An attacker can claim this subdomain by requesting a process of registering this abandoned subdomain to his name.
And attacker can fully take over this subdomain and do whatever he wants. this can cause huge damage to the website's main domain as well as to the company.
I Recommend removing  the Cname and DNS connecting to it.
You can read about this sort of attacks here : https://www.siteground.com/tutorials/googleapps/google_calendar.htm
To clarify your doughs I 


## Stored XSS in topics because of whitelisted_generic engine vulnerability
- 等级：High | 项目：Discourse | 披露：2017-01-20 | CVE：-
- 原文：https://hackerone.com/reports/197902

- - - - - - - - 
Hello!
**Steps to reproduce:**
1. Paste this payload URL in the topic: http://89.223.28.48/og_image.html?uncache1234
2. Save the post and you will see the XSS will fire
{F151911}
Though you now escape the OpenGraph data, the whitelisted_generic onebox engine decodes variables values back at lines: [202](https://github.com/discourse/onebox/blob/master/lib/onebox/engine/whitelisted_generic_onebox.rb#L202) and [207](https://github.com/discourse/onebox/blob/master/lib/onebox/engine/whitelisted_generic_onebox.rb#L207).
Then these decoded values are injected in the raw HTML [here](https://github.com/discourse/onebox/blob/master/lib/onebox/engine/whitelisted_generic_onebox.rb#L284)


## XSS in topics because of bandcamp preview engine vulnerability
- 等级：High | 项目：Discourse | 披露：2017-01-20 | CVE：-
- 原文：https://hackerone.com/reports/197443

- - - - - - - - 
1. Load http://try.discourse.org
2. Click "New topic"
3. Enter this payload https://89.223.28.48/bandcamp.com/album/index.html?XSSa2 to field with placeholder "Type title or paste a link here"
4. Wait for the preview engine to parse the link
4. XSS will fire
{F151439}
You should sanitize external data in this engine and replace *matches_regexp* from
`^https?:\/\/.*bandcamp\.com\/album\/`
to
`^https?:\/\/.*\.bandcamp\.com\/album\/`
to fix the issue.
---


## Stored XSS in posts because of absence of oembed variables values escaping
- 等级：High | 项目：Discourse | 披露：2017-01-20 | CVE：-
- 原文：https://hackerone.com/reports/197914

- - - - - - - - 
Hello!
**Steps to reproduce:**
1. Paste this payload URL in the post: http://89.223.28.48/oembed_video.html?uncache
2. Save the post and you will see the XSS will fire.
{F151922}
The vulnerability exists because of absence of oembed variables values escaping.
There is the oembed link in the payload page:
[code omitted]
As you can see the onebox parser goes to this oembed URL to get the data:
[code omitted]
The content of *oembed.json* is:
[code omitted]
So the unescaped data is injected in the raw HTML at [this line](https://github.com/discourse/onebox/blob/master/lib/onebox/engine/whitelisted_generic_onebox.rb#L284) of generic_whitelisted onebox engine that leads to XSS vul

