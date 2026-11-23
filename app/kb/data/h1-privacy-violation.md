# HackerOne 实战案例：privacy-violation

_14 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Connection informaton is sent to a third-party service
- 等级：Critical | 项目：Nord | 披露：2020-02-23 | CVE：-
- 原文：https://hackerone.com/reports/752402

- - - - - - - - 
Application event data exposed through the reuse of API key
The researcher reported that iOS app usage event information sent to the third party service can be intercepted through the reuse of API key. In order to resolve the issue we have disabled GET requests for API keys, removed the third party SDK and per DPA terms deleted all event data that has ever been sent.
---


## Physical Laptop Takeover
- 等级：Critical | 项目：Ed | 披露：2018-08-12 | CVE：-
- 原文：https://hackerone.com/reports/393615

- - - - - - - - 
At 6:16PM of August 11th of 2018, during H1-702, right before the sand storm beat the shit out of the rooftop party, we managed to perform a critical attack on Ed's infrastructure.
{F332214}
## Report Summary
During our analysis and reconnaissance of how Ed program worked during the h1-702 event, we realized there was a critical flaw on how the program was setup. 
## Report Description
During the process, we realized that the program manager had tendency to leave secrets open in the wild. While analyzing this, we decided to look into hardware hacking. So as we looked around, we found that the owner of the program left their computer open. What was worse is that it allowed us


## ██████ SSN/EDPI
- 等级：High | 项目：U.S. | 披露：2024-10-25 | CVE：-
- 原文：https://hackerone.com/reports/1541817

- - - - - - - - 
**Description:**
With some simple URL manipulation, an authenticated user is able to request other soldiers SSN, perID, EDPI. 
## References
CWE-200 - Information Disclosure
CWE-284 - Improper Access Control
Collaborators: 
theonetruepengu
hxhbrofessor
## Impact
After pulling an perID, someone would have access to view their  SSN, EDPI. With most recent breaches of SSNs, one attacker would have enough information to verify and impersonate another soldier for malicious purposes.
## System Host(s)
████, ██████████
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
Authenticate to https://████████/#/soldierRecord/
Run your browsers developer mode.
Then l


## The Deleted Polls is Still Accessable after 30 Days
- 等级：High | 项目：X | 披露：2023-02-13 | CVE：-
- 原文：https://hackerone.com/reports/1015373

- - - - - - - - 
The researcher demonstrated a vulnerability that makes it possible for Twitter users to access a Poll after it has been deleted by user that originally posted the Poll. Though it was not visible or accessible via the user interface, it could still be accessed for an extended period of time beyond what the Twitter policy states. This behavior made it possible to compromise the privacy of the user's account that originally posted the Poll if the content was not deleted within a specified amount of time.
---


## GPS metadata preserved when converting HEIF to PNG
- 等级：High | 项目：Reddit | 披露：2021-10-21 | CVE：-
- 原文：https://hackerone.com/reports/1069039

- - - - - - - - 
## Summary:
Users who upload HEIC/HEIF files (sometimes called "Live Photos")  to reddit.com or old.reddit.com expect their GPS metadata to be stripped before being displayed publicly. Uploaded HEIC files are converted to PNG, but GPS metadata is incorrectly preserved, in violation of user privacy. The problem is likely device- and browser-agnostic, and mostly affects Safari users on Mac since other devices and browsers either automatically convert to a different format or do not permit HEIC files to be uploaded through the usual user flow.
## Impact:
All users who have submitted HEIC files have their GPS locations exposed publicly, which can be scraped with little detection


## Responsible Disclosure of Privacy Leakage Issue
- 等级：High | 项目：GitLab | 披露：2021-06-29 | CVE：-
- 原文：https://hackerone.com/reports/1089914

- - - - - - - - 
Greetings,
I am Mojtaba Zaheri, a doctoral candidate in Computer Science, affiliated with the [NJIT Cybersecurity Research Center](https://centers.njit.edu/cybersecurity/welcome/). Together with my doctoral dissertation advisor, Prof. Reza Curtmola, we are reaching out to perform responsible disclosure of a vulnerability present on the GitLab website. Please let us know if you have any comments regarding this disclosure.


## Cookie poisoning leads to DOS and Privacy Violation
- 等级：High | 项目：CS | 披露：2021-02-25 | CVE：-
- 原文：https://hackerone.com/reports/1067809

- - - - - - - - 
Summary, submitted by `████████` requires no additions by us and fully expresses impact and reasons behind the vulnerability.
**Summary (researcher):**
# Summary
By change the value of the cookie avatar, a hacker could not only get information of the support agent IP address, but also disconnect all the supports without interaction.
## Vulnerability
The cookie avatar should have the value of a link to the user's steam avatar.
A normal cookie is like that: `https://steamcdn-a.akamaihd.net/steamcommunity/public/images/avatars/ae/ae6680902f4fe18e692ba9ea250bd694b34ad417_medium.jpg`
But in the server, there is a verification like that (pseudocode):
[code omitted]
Now start a cha


## Improper Access Controls Allow PII Leak via ████
- 等级：High | 项目：U.S. | 披露：2021-02-18 | CVE：-
- 原文：https://hackerone.com/reports/819591

- - - - - - - - 
**Summary:**
Dashboards in `██████████` allow a user to add widgets and obtain large amounts of information to include PII and diagnostic information. Additionally, a user is able to make changes to certain catalogs via these widgets.
**Description:**
## Impact
An adversary can gain access to PII to include full names, e-mail addresses, physical addresses, phone numbers, etc., as well as modifying fields within the underlying system. Additionally, the adversary could identify information such as the number/type of incidents, as well as diagnostic information such as memory usage.
## Step-by-step Reproduction Instructions
1. Create an account on `███████/` and browse to `████


## CRITICAL Insecure Direct Object Reference (I.D.O.R) - Link Other User's Credit Card
- 等级：High | 项目：Yelp | 披露：2020-08-19 | CVE：-
- 原文：https://hackerone.com/reports/358143

- - - - - - - - 
@hk755a discovered an Insecure Direct Object Reference Vulnerability that allowed an attacker to associate a randomly added (but subsequently deregistered) credit card with their own account, via the `/rewards/signup` endpoint. While the attacker would not have been able to use this credit card as their own (nor view any primary account numbers (PAN) for said cards), the attacker may have been able to glean the transaction history associated with the card, as well as cash back amounts received.
Yelp was able to quickly validate and fix the vulnerability within two days. Thanks to @hk755a for working with us to fix this bug!
---


## Gateway information leakage
- 等级：High | 项目：U.S. | 披露：2019-07-30 | CVE：-
- 原文：https://hackerone.com/reports/258410

- - - - - - - - 
**Summary:**
Many DoD systems use BlueCoat gateways. These gateways insert unique BlueCoat ids that permit tracking DoD users and gaining insight into the DoD network architecture when DoD users access the Internet.
**Description:**
I run a popular web service (FotoForensics.com -- it's around 150,000 in the Alexa list of top web sites).  My public web site is explicitly for research and gets visitors from all over, including from the DoD.  One of the research project collects non-standard HTTP headers.  The BlueCoat HTTP headers immediately stood out as non-standard.
Someone with a BlueCoat gateway will have headers that look like:
> POST /upload-file.php HTTP/1.1
> Host: w


## Privacy violation для аттачей в сообщениях.
- 等级：High | 项目：ok.ru | 披露：2018-08-21 | CVE：-
- 原文：https://hackerone.com/reports/377115

- - - - - - - - 
The vulnerability allowed unauthorized access to other users' file attachments with no ability to identify senders or recipients.
Уязвимость позволяла получить несанкционированный доступ к приаттаченным файлам без возможности определить отправителя и получателя.
**Summary (researcher):**
Vulnerability allowed downloading other people's files from private messages.
Уязвимость позволяла скачивать чужие файлы из личных сообщений без возможности определить отправителя и получателя.
---


## Получение чужого номера телефона (все цифры) через форму восстановления пароля
- 等级：High | 项目：VK.com | 披露：2018-06-30 | CVE：-
- 原文：https://hackerone.com/reports/350939

- - - - - - - - 
В некоторых случаях можно было получить привязанный к странице номер телефона.
**Summary (researcher):**
Данная уязвимость позволяет злоумышленнику получить личный номер телефона жертвы, который привязан к странице Вконтакте. Для использования данной уязвимости достаточно знать только электронный адрес жертвы.
---


## application/x-brave-tab should not be readable.
- 等级：High | 项目：Brave | 披露：2017-11-07 | CVE：-
- 原文：https://hackerone.com/reports/258578

- - - - - - - - 
## Summary:
It is possible to read a dragged tab object if user is coerced into drag and dropping it into attacker controlled page. This is bad because tab history is mentioned within the object, thus information leaks are possible through a trick.
## Products affected: 
 
Brave: 0.18.14 
rev: ad92d029e184c4cff01b2e9f4916725ba675e3c8 
Muon: 4.3.6 
libchromiumcontent: 60.0.3112.78 
V8: 6.0.286.44 
Node.js: 7.9.0 
Update Channel: dev 
OS Platform: Microsoft Windows 
OS Release: 10.0.14393 
OS Architecture: x64
## Steps To Reproduce:
1. Open PoC and click on button.
2. Popup should appear loading facebook and then should direct to a dummy page
3. Attempt to drag and drop the ne


## Unauthorized Access to Protected Tweets via niche.co API
- 等级：High | 项目：X | 披露：2017-11-02 | CVE：-
- 原文：https://hackerone.com/reports/273698

- - - - - - - - 
Hello,
**Summary:**
Normally If user __(victim)__ set to private / protect their tweets in setting Tweet privacy, other people/user will not able to see their recent or their pass status/twits when they visit his/her __(victim)__ profile. people only can see their __(victim)__ profile images and information about __how many tweet already post by that user__ , __how many followers and following by that account__ and __how many likes__ etc etc. but i found a way to view the protected tweets from other user who protect their tweets.
**Description:** 
in your policy i see there is new domain add as in scope target , and the domain is `niche.co` .
there is some condition needed t

