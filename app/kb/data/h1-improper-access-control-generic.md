# HackerOne 实战案例：improper-access-control-generic

_40 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Air Force candidate PII + recruitment chat logs accessible via BAC/IDOR on █████████ (very large/significant exposure)
- 等级：Critical | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/2968391

- - - - - - - - 
Greetings DoD team,
I've uncovered another serious IDOR on a DoD-owned Salesforce asset (█████████).
Broken record-level configuration the Document object of this Salesforce instance allows  an attacker to retrieve a huge number of sensitive Air Force candidate records.
It is likely that these records are related to the Air Force recruiter live chat:█████. 
This is very problematic, as each log file contains a wealth of highly private personal information.
**Database fields include:**
Private chat logs between candidate/recruiter,
Full name,
Address,
Phone number,
Email address,
Medical data,
Drug use history,
Felony/Criminal history,
Academic data,
The contents of the chat 


## Unauthorized coins transfer from locking account(s)
- 等级：Critical | 项目：Cosmos | 披露：2025-06-29 | CVE：-
- 原文：https://hackerone.com/reports/2976481

- - - - - - - -


## unauthorized access and add user and change personal information all users
- 等级：Critical | 项目：Mars | 披露：2025-05-27 | CVE：-
- 原文：https://hackerone.com/reports/2828641

- - - - - - - - 
The report describes a vulnerability in the ██████████  website, where unauthorized access to an API endpoint allows attackers to add new users and modify personal information of existing users. The vulnerability is classified as Improper Access Control. The issue stems from the absence of proper authentication and authorization mechanisms on the ██████████  endpoint, which handles user registration and profile updates. This vulnerability allows anyone to create new user accounts or modify existing user information without requiring any authentication. Additionally, the vulnerability is compounded by a predictable user identifier system (4-digit codes) that can be easily enu


## change part of personal information all users
- 等级：Critical | 项目：Mars | 披露：2025-05-12 | CVE：-
- 原文：https://hackerone.com/reports/2828693

- - - - - - - - 
The report describes a vulnerability in the ██████████  website, where unauthorized access to an API endpoint allows attackers to add new users and modify personal information of existing users. The vulnerability is classified as Improper Access Control. The issue stems from the absence of proper authentication and authorization mechanisms on the ██████████  endpoint, which handles user registration and profile updates. This vulnerability allows anyone to create new user accounts or modify existing user information without requiring any authentication. Additionally, the vulnerability is compounded by a predictable user identifier system (4-digit codes) that can be easily enu


## Admin Dashboard Access Leads to Updating Merchant Info
- 等级：Critical | 项目：MTN | 披露：2025-03-02 | CVE：-
- 原文：https://hackerone.com/reports/2801787

- - - - - - - - 
## Summary:
The ███████ application provides access to 3(Merchant, Supervisor, Admin) classes of users. Looking at the Admin side, its clear only permitted admins can login to the portal since nothing on the UI indicates a register feature. However I was able to find a registration endpoint to sign up. Now I have access to the Admin dashboard. Based on the functionalities there, it's evident an outsider shouldn't have access to this.
## Steps To Reproduce:
[add details for how we can reproduce the issue]
  1. Visit ████████ and signup
  2. Login at ██████ and you will be redirected to the admin dashboard where you can approve or decline transactions.
██████   
  3. At ██████


## Account Takeover via Password Reset without user interactions
- 等级：Critical | 项目：GitLab | 披露：2025-02-26 | CVE：-
- 原文：https://hackerone.com/reports/2293343

- - - - - - - - 
@asterion04 submitted a report to GitLab.
Summary
I found a way to change the password of a GitLab account via the password reset form and successfully retrieve the final reset link without user interactions, using just its email address.
Steps to reproduce
Go to "Forgot Your Password?" link
Enter the victim's email and intercept the submit request via Burp Suite .
Then right-click on the HTTP Editor inside Burp Suite and select Extensions -> Content-Type Converter -> Convert to JSON (make sure to have the Content-Type Converter plugin installed from the BApp Store)
Now replace this converted JSON line `` "user[email]":"victim@gmail.com"``, to
[code omitted]
Forward the requ


## Applicant security exam Attachments/Documents accessible through an IDOR/BAC on the custom Apex controller on https://█████.mil
- 等级：Critical | 项目：U.S. | 披露：2025-02-12 | CVE：-
- 原文：https://hackerone.com/reports/2950536

- - - - - - - - 
Greetings DoD team,
I've uncovered a highly dangerous IDOR on the ██████████ portal.
An attacker can switch the ownership of any Attachment record submitted through the portal and access the files. These contain highly sensitive information as they include all materials/documentation submitted as part of the vetting procedures prior to visiting the █████, e.g. personal medical records. Potentially this might include internal attachments as well.
An attacker is able to exploit the following chain:
1. Generate/enumerate a list of Salesforce Attachment Id's. These are highly predictable: example methodology/script here: https://blog.hypn.za.net/2022/11/12/Hacking-Salesforce-bac


## OTP code Leaked in API Response
- 等级：Critical | 项目：MTN | 披露：2025-01-08 | CVE：-
- 原文：https://hackerone.com/reports/2633888

- - - - - - - - 
## Summary:
The application https://corporate.admyntec.co.za allows users to sign up for device insurance. When you Get a Quote, it requires authentication via phone number. An OTP is sent to the phone number to further validate the action was initiated by the legit user. Except this same OTP code is returned in the OTP response.
## Steps To Reproduce:
  1.Vist https://corporate.admyntec.co.za/customerInsurance and get a quote. 
  2. Have a proxy interceptor tool like burpsuite running. Now enter any valid MTN number.
   3. Notice the OTP code is also returned in the API's response
{F3484295}
## Impact
It's possible to sign up with other users accounts. It's possible to log 


## SAML Signature verification bypass allows logging into any user (with specific conditions)
- 等级：Critical | 项目：GitHub | 披露：2024-10-10 | CVE：CVE-2024-6800
- 原文：https://hackerone.com/reports/2579939

- - - - - - - - 
An XML signature wrapping vulnerability was present in GitHub Enterprise Server (GHES) when using SAML authentication with specific identity providers utilizing publicly exposed signed federation metadata XML. This vulnerability allowed an attacker with direct network access to GitHub Enterprise Server to forge a SAML response to provision and/or gain access to a user with site administrator privileges. Exploitation of this vulnerability would allow unauthorized access to the instance without requiring prior authentication. This vulnerability affected all versions of GitHub Enterprise Server prior to 3.14 and was fixed in versions 3.13.3, 3.12.8, 3.11.14, and 3.10.16.
[CVE-2


## DoD workstation exposed to internet via TinyPilot KVM with no authentication
- 等级：Critical | 项目：U.S. | 披露：2024-08-16 | CVE：-
- 原文：https://hackerone.com/reports/2633988

- - - - - - - - 
**Description:**
There appears to be a workstation belonging to ███████ (███) that is completely exposed to the internet via IP web interface by way of a TinyPilot KVM device.
TinyPilot KVMs are hardware devices that enable you to remotely access computers via IP address. This device in question is available over the internet without authentication and is connected to a workstation that appears to belong to ███. There is an "UNCLASSIFIED" green banner at the top. In the top right corner appears to be the initials "SA", which may identify the user.
Please see attached screenshot. Of note: I did **not** interact with the device at all. I immediately closed the connection after


## Guest Privilege Escalation to admin group
- 等级：Critical | 项目：Rocket.Chat | 披露：2024-08-10 | CVE：-
- 原文：https://hackerone.com/reports/501081

- - - - - - - - 
Due to improper ACLs it was found possible to escalate privileges from a guest user to admin.
As first step the guest user adds itself to the `bot` group that holds the `manage-own-integrations` permission. With this permission it is possible to create a custom Integration with a script that, if triggered, adds the user to the `admin` group.
The `insertOrUpdateUser` method improperly validates a users permissions to change its groups. Because an explicit check prevents from adding itself to the `admin` group directly, the privileges of the `bot` group need to be used to further escalate to global admin.
## Releases Affected:
  * [develop@5f0180d](https://github.com/RocketCha


## Automatic Admin Access
- 等级：Critical | 项目：U.S. | 披露：2024-07-19 | CVE：-
- 原文：https://hackerone.com/reports/1991214

- - - - - - - - 
URL: https://█████████.mil/apexcrrel/f?p=150:1:23467499301323::NO:::
When visiting the following URL, the user is automatically signed into a user with administrative access. 
███
This user is allowed to:
1. Create new submissions, allowing file uploads
████████
2. See all submissions going back to 2012
██████████
3. Manage users - add, delete, and link users. This user could also add the Administrator role to a user. 
███
████
4. Send spam emails to all users
█████████
5. Access admin tools like publishing data and removing publications
██████████
I did not test all functionality provided by this access as I did not want to damage the integrity of the data on the web applic


## Endpoint Redirects to Admin Page and Provides Admin role
- 等级：Critical | 项目：U.S. | 披露：2024-07-19 | CVE：-
- 原文：https://hackerone.com/reports/1991290

- - - - - - - - 
**Summary:**
By navigating to https://████████.mil/apexcrrel/f?p=165:56, the user will automatically be redirected to the web application admin portal with Admin access.
**Description:**
There is a web application running at the following URL:
https://█████.mil/apexcrrel/f?p=165:1::::::
████
For context, this is a web application running on a Oracle Apex Express platform. The '165' in the 'p' parameter in the URL is a unique identifier for the web application. The '1' following the '165' represents the page that the user is viewing. 
The page '56' can be used to automatically obtain administrator access to this application. 
Here we can see that we can't access the 45th page


## Subdomain takeover ████████.mil
- 等级：Critical | 项目：U.S. | 披露：2024-06-27 | CVE：-
- 原文：https://hackerone.com/reports/2499178

- - - - - - - - 
**Description:**
The subdomain `█████.mil` is pointing to `peosol-lg.███████.`, the domain `██████` is currently available for registration as can be seen at https://www.godaddy.com/nl-nl/domainsearch/find?domainToCheck=█████
Given the rules, residency of the US, of the `us`-tld I decided not to register the domain, also I do believe the output to be enough.
## References
## Impact
Using this vulnerability an attacker can:
- host unwanted/malicious content under your domain
- receive email on subdomains mentioned above
- effectively execute cross-site scripting attacks
- in some cases, steal cookie data
- in some cases, trick password managers into filling passwords
## Syste


## Lack of Tenant Scoping Enables Limited Cross-Tenant Data Querying and Mutation
- 等级：Critical | 项目：Enjin | 披露：2024-01-25 | CVE：-
- 原文：https://hackerone.com/reports/2327238

- - - - - - - - 
@tushar_rec0n was able to demonstrate on the [Enjin Platform](https://platform.enjin.io) that it was possible, for certain queries and mutations, to query and mutate data cross-tenant (ie. to query or mutate someone else's data).
It's worth noting that the Enjin Platform does have a plethora of queries and mutations that are intended to work cross-tenant, although this report specifically highlighted ones that were not intended to do so.
A full assessment of the vulnerability was conducted and, outside of the three duplicate reports, we identified this vulnerability had not been used by anyone else.
---


## Default Admin Username and Password on ███
- 等级：Critical | 项目：U.S. | 披露：2023-12-21 | CVE：-
- 原文：https://hackerone.com/reports/2262365

- - - - - - - - 
It is possible to access the application is using the default username and password 
Steps To Reproduce:
1-Go to https://███/geoportal/ and login with credentials:
user and password: admin
user and password: gptadmin
Poc video attached
## Impact
A Department of Defense website was misconfigured in a manner that may have allowed a malicious user to login with administrator for the default organization account credentials and delete posts , edit website
## System Host(s)
███
## Affected Product(s) and Version(s)
## CVE Numbers
## Steps to Reproduce
POC video
## Suggested Mitigation/Remediation Actions
---


## Unauthenticated Remote Access to Testing Endpoint
- 等级：Critical | 项目：IBM | 披露：2023-12-04 | CVE：-
- 原文：https://hackerone.com/reports/2192984

- - - - - - - - 
Unauthenticated remote access to a testing endpoint was reported to IBM, analyzed and has been remediated. Thank you to our external researcher @sajidraza.
---


## User automatically logged in as Sys Admin user on https://███/Administration/Administration.aspx
- 等级：Critical | 项目：U.S. | 披露：2023-11-03 | CVE：-
- 原文：https://hackerone.com/reports/2190808

- - - - - - - - 
**Description:**
Any user can access the Administration section of the following URL: https://███
When the user goes to the following domain they are automatically logged in as "████████" which is a sys admin user on the application, this allows any user to upload files, add users, change permissions for users and delete users.
## References
## Impact
A malicious actor can modify other user's privileges on the application, add users, upload files, delete users. They can also add false information to the application which will jeopardize the integrity of the application. With administrator privileges they have no restrictions on the application.
## System Host(s)
https://████


## ' Full Account Takeover ' at █████
- 等级：Critical | 项目：Mars | 披露：2023-06-23 | CVE：-
- 原文：https://hackerone.com/reports/1959540

- - - - - - - - 
A severe vulnerability is identified in the login functionality of a website belonging to Mars. An unauthorized actor can manipulate the server's response from the █████████████ endpoint to gain unauthorized access to any user account on the platform, leading to a full account takeover. The attacker can achieve this by intercepting the login request, modifying the server's response to indicate a successful login, and setting a cookie with the target user's ID. This exploit does not require knowledge of the victim's email address or password.
---


## access nagios dashboard using default credentials in ** omon1.fpki.gov, 3.220.248.203**
- 等级：Critical | 项目：U.S. | 披露：2022-10-21 | CVE：-
- 原文：https://hackerone.com/reports/1700896

- - - - - - - - 
## Summary:
when i performing recon on fpki.gov i found nagios dashboard in ** omon1.fpki.gov, 3.220.248.203**  and i accessed it using default credentials
username:  ** nagiosadmin **
password :  ** nagiosadmin **
## Steps To Reproduce:
  1. visit these urls : 
        **  https://omon1.fpki.gov/nagios/side.php **
        ** https://3.220.248.203/nagios/side.php **
  2. he will ask to put your credentials in basic authentication enter these credentials 
       
         username:  ** nagiosadmin **
         password :  ** nagiosadmin **
##POC:
look at poc pic
## Impact
attacker can make any action like an admin he has full control on your panal.
thanks , have a nice day :)



## Default Login Credentials on https://broadbandmaps.mtn.com.gh/
- 等级：Critical | 项目：MTN | 披露：2022-08-25 | CVE：-
- 原文：https://hackerone.com/reports/1297480

- - - - - - - - 
## Summary:
Hello Team,
I just found out that `broadbandmaps.mtn.com.gh` requires logging in when you visit it, but it turned out that you can actually login as an Admin and do anything on the specific site.
when you visit the mentioned site you will get this   
{F1405776}
it will require to be logged in to perform any action, to bypass this you have to Login with the default credentials `Username`= admin `password`= admin , and for some reasons you can't login with Firefox it only works on Google chrome and  chromium web browser.
## Supporting Material:
-Check this Video >
{F1405806}
## Impact
Access admin Panel due to Default credentials
---


## One-click account hijack for anyone using Apple sign-in with Reddit, due to response-type switch + leaking href to XSS on www.redditmedia.com
- 等级：Critical | 项目：Reddit | 披露：2022-08-02 | CVE：-
- 原文：https://hackerone.com/reports/1567186

- - - - - - - - 
Hi,
# Description
I've been researching new ways to steal OAuth codes and access-tokens using postMessage, and I found a way for me to steal the code and/or access-token from Apple-sign-in on reddit.com allowing a full account hijack of the account in Reddit.
The way it works is this:
1. Attacker prepares a `state`-parameter in its own browser from the regular Apple sign-in flow in Reddit. This is an important part on how we get the code.
2. Attacker makes a page for the victim with the attacker's state attached to it. The page loads an iframe with `www.redditmedia.com`, which is an intentional sandbox but with a fun quirk, it uses `window.name` of the frame to pass over que


## Public Jenkins instance with /script enabled
- 等级：Critical | 项目：IBM | 披露：2022-03-11 | CVE：-
- 原文：https://hackerone.com/reports/1492447

- - - - - - - - 
An RCE/LFI due to Public Jenkins instance with /script enabled was reported to IBM February 26th, analyzed and has been remediated since March 3rd, 2022. Thank you to Sanjok Karki (thesanjok) for the finding.
**Summary (researcher):**
RCE/LFI due to Public Jenkins instance with /script enabled.
---


## Critically Sensitive Spring Boot Endpoints Exposed
- 等级：Critical | 项目：Semrush | 披露：2022-02-10 | CVE：-
- 原文：https://hackerone.com/reports/1022048

- - - - - - - - 
Spring Boot includes a number of additional features to help you monitor and manage your application when you push it to production. 
Hacker found that actuator endpoints containing potentially sensitive data (such as internal tokens and service data) were left public.
**Summary (researcher):**
Semrush has a microservices architecture, there is an API gateway which routes to the server corresponding to the service in the internal network. Some Semrush services use spring boot with actuator endpoints enabled, some services left these endpoints publicly accessible. It was therefore possible to access it as follow: https://semrush.com/service-xyz/actuator/ . Some endpoints leak


## Unauthenticated Access to Admin Panel Functions at https://███████/███
- 等级：Critical | 项目：U.S. | 披露：2021-11-29 | CVE：-
- 原文：https://hackerone.com/reports/1397564

- - - - - - - - 
**Description:**
The admin panel at https://██████████/████████ and all its functions can be accessed without authentication. This is basically the same vulnerability as in #1394910, just on another system.
## Impact
An attacker is able to use the administrative functions in order to upload, delete or modify files.
## System Host(s)
███
## Affected Product(s) and Version(s)
██████████
## CVE Numbers
## Steps to Reproduce
* Navigate to https://███/ and click on the "Authenticate ██████████" button
* Notice how the application first sends an HTTP POST request to https://███████/████████ which should redirect to https://██████/██████████ (`Location: █████`). Navigating to  http


## Unauthenticated Access to Admin Panel Functions at https://██████████/████████
- 等级：Critical | 项目：U.S. | 披露：2021-11-29 | CVE：-
- 原文：https://hackerone.com/reports/1394910

- - - - - - - - 
**Description:**
I discovered that the admin panel at https://████/█████ and all its functions can be accessed without authentication.
## Impact
An attacker is able to use the administrative functions in order to upload, delete or modify files.
## System Host(s)
████████
## Affected Product(s) and Version(s)
██████'s ████████ (███) Management
## CVE Numbers
## Steps to Reproduce
* Navigate to https://█████/ and click on the "█████████" button
* Notice how the application first sends an HTTP POST request to https://█████████/█████ which gets answered with a redirect to https://█████/█████ which again redirects to https://███████/█████████
* Looking at the response to https://


## Access to microtransaction sales data for lots of apps from 2014 to present at /valvefinance/sanity/
- 等级：Critical | 项目：Valve | 披露：2021-09-21 | CVE：-
- 原文：https://hackerone.com/reports/975212

- - - - - - - - 
The Steamworks Product Data web site had an URL route with insufficient access controls, which would allow an authenticated partner to view data for games which they might not otherwise have permissions to view. After mitigation, an audit of accesses to this URL route showed no accesses by parties other than Valve or the reporter of this issue.
---


## Access to alerta.khanacademy.org leak sensitive data
- 等级：Critical | 项目：Khan | 披露：2021-09-08 | CVE：-
- 原文：https://hackerone.com/reports/1061664

- - - - - - - - 
Hi ,
I found to access https://alerta.khanacademy.org/ using signup bypass.That leak access to sensitive data of khanacademy.org
Step To Reproduce:
1. Go to https://alerta.khanacademy.org/#/signup
2. Inspect Q and remove ng-hide
{F1121291}
3. You got Signup Form. Signup account using anythings@khanacademy.org mail.
{F1121292}
4. When you successfully signup,You access alerta.khanacademy.org without confirm email.
{F1121297}
If you not login direct .
1. Go to alerta.khanacademy.org/#/login.
2. Inspect Q and remove ng-hide
{F1121293}
3. Login with your register info.
{F1121294}
## Impact
Attacker can access alerta dashboard
Thanks,
@nightmare_msf
---


## URN Request bypass ACL Checks
- 等级：Critical | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-12523
- 原文：https://hackerone.com/reports/824802

- - - - - - - - 
## Summary:
Attacker can bypass ACL checks gaining access to restricted HTTP servers such as those running on localhost. Attacker could also gain access to CacheManager if VIA
header is turned off. Only lines with : will be readable though, and the response must be less than 4096 bytes or it'll trigger the Heap Overflow I reported earlier. 
This is due to URN request being transformed into HTTP request, and not going through the ACL checks that incoming HTTP request go through. 
<= Squid-4.8 Vulnerable
Fixed in Squid-4.9
Squid Announce: http://www.squid-cache.org/Advisories/SQUID-2019_8.txt
Assigned  CVE-2019-12523 
## Steps To Reproduce:
Enable URN by adding the following e


## Publicly accessible Continuous Integration Tool
- 等级：Critical | 项目：Snapchat | 披露：2021-07-29 | CVE：-
- 原文：https://hackerone.com/reports/313457

- - - - - - - - 
@apfeifer27 found an internal Continuous-Integration instance, which disclosed internal source code and credentials for some of our instances.
---


## Unauthorized access to admin panel of the Questionmark Perception system at https://██████████
- 等级：Critical | 项目：U.S. | 披露：2021-06-30 | CVE：-
- 原文：https://hackerone.com/reports/1026146

- - - - - - - - 
**Summary:**
Due to the lack of access control, an anonymous attacker can compromise the administrator account on the Questionmark Perception system.
**Description:**
By using the service description which publicly accessible on the internet, and by bypassing the access control, an anonymous attacker can (ab)use the method provided by the system and get the administrator access on the Questionmark Perception system.
## Step-by-step Reproduction Instructions
- Visit https://██████/█████████ to get all the Questionmark Web Integration Services' description.
████
- The method **GetAdministratorList** returns a list giving the full details of all the administrators in the databa


## Default Admin Username and Password on █████ Server at █████████mil
- 等级：Critical | 项目：U.S. | 披露：2021-06-15 | CVE：-
- 原文：https://hackerone.com/reports/1195325

- - - - - - - - 
**Description:**
A ██████ Server is running at https://███mil you can access the login at https://████mil/█████████ the application is using the default "Administrator for the default organization" credentials 
#POC 
Go to  https://███mil/████████ and login with *█████*
██████████
████
████
## How to remediate the vulnerability
Change the password of the user or disable the account 
## References
█████
https://cwe.mitre.org/data/definitions/521.html
##EXTRA
If you have any questions or concerns regarding the above let me know!
Cheers,
## Impact
A Department of Defense website was misconfigured in a manner that may have allowed a malicious user to login with administrator for


## No Valid SPF Records/don't have DMARC record
- 等级：Critical | 项目：UPchieve | 披露：2021-05-18 | CVE：-
- 原文：https://hackerone.com/reports/1198439

- - - - - - - - 
I have already reported this isssue through email and the company has accepted my report.
Hiii,
There is any issue No valid SPF Records on 
https://app.upchieve.org
Desciprition :
There is a email spoofing vulnerability.Email spoofing is the forgery of an email header so that the message appears to have originated from someone or somewhere other than the actual source. Email spoofing is a tactic used in phishing and spam campaigns because people are more likely to open an email when they think it has been sent by a legitimate source. The goal of email spoofing is to get recipients to open, and possibly even respond to, a solicitation.
I found :
SPF record lookup and validati


## Zero click account Takeover due to Api misconfiguration 🏂🎩
- 等级：Critical | 项目：UPchieve | 披露：2021-05-14 | CVE：-
- 原文：https://hackerone.com/reports/1166500

- - - - - - - - 
Hacker reported that full account takeover was possible through exploitation of one our forms. Hacker provided sufficient information to prove capability and how to remediate. Our team remediated the issue so that the takeover is no longer possible.
**Summary (researcher):**
i was able to take over any account without any action from the user
---


## Full account takeover of any user through reset password
- 等级：Critical | 项目：UPchieve | 披露：2021-05-14 | CVE：-
- 原文：https://hackerone.com/reports/1175081

- - - - - - - - 
## Summary:
Hi Security team members,
Usually, If we reset our password on https://app.upchieve.org that time we got a password reset link on the email. And through that password reset link, we can reset our password.
But, I noticed that if we add another email in the request of forgot password through Burpsuite then both person will get the same password reset token in their email. So, an attacker can takeover any account without the user's interaction.
## Steps To Reproduce:
1. Navigate to: https://app.upchieve.org/resetpassword 
2. Then, enter the victim's email address 
3. Intercept this request
4. Now, add your email also in the JSON body. like this:
[code omitted]
5. F


## CVE-2020-6287  https://redapi2.acronis.com
- 等级：Critical | 项目：Acronis | 披露：2021-02-16 | CVE：CVE-2020-6287
- 原文：https://hackerone.com/reports/1028392

- - - - - - - - 
Hi team.
## Summary
CVE-2020-6287  https://redapi2.acronis.com
https://nvd.nist.gov/vuln/detail/CVE-2020-6287
>SAP NetWeaver AS JAVA (LM Configuration Wizard), versions - 7.30, 7.31, 7.40, 7.50, does not perform an authentication check which allows an attacker without prior authentication to execute configuration tasks to perform critical actions against the SAP Java system, including the ability to create an administrative user, and therefore compromising Confidentiality, Integrity and Availability of the system, leading to Missing Authentication Check.
You can check. I created user with role 'Administrator'
[code omitted]
## Steps To Reproduce
  1. clone https://github.com


## Full account takeover on https://████████.mil
- 等级：Critical | 项目：U.S. | 披露：2021-01-25 | CVE：-
- 原文：https://hackerone.com/reports/1058015

- - - - - - - - 
###Description
The flow in application is to sign up and wait for an email containing a one-time password, as soon as you login using that password, it asks you to change it. I took that password change request and applied on any email changing their password and it worked
###Steps to produce:
1- Copy the following request: (note `txtEMail` and `txtNewPassword` parameters)
[code omitted]
2- Now, log in using any victim email with a random password and intercept the request at `https://█████.mil/Login.aspx`
3- Paste the request you copied above and change the `txtEMail` (to victim email) and `txtNewPassword` parameters and send it.
## Impact
Full account takeover on any user.


## A Visit from The Grinch ~ 'Twas the night before Hackmas...
- 等级：Critical | 项目：h1-ctf | 披露：2021-01-11 | CVE：-
- 原文：https://hackerone.com/reports/1067912

- - - - - - - - 
##Foreword
This was an amazing CTF! The first from Hackerone that I've finished and one that I have enjoyed the most. Huge shout out to @adamtlangley for creating this downright poetic challenge. My whopping 20+ invitations are already being put to good use. Hacky Holidays and Merry Hackmas!
##Flag #1 - robots.txt
>'Twas the night before Hackmas, when all through the net
>Not a feature was deployed, not even password reset
>The flag was placed in robots.txt with care
>In hopes that hackers might first look there
A classic! The first flag was nestled in robots.txt, the first place any good hacker or CTFer might look for clues. 
{F1132033}
##Flag #2 - s3cr3t-ar3a
>The flag was


## SAML authentication bypass through unauthenticated `addSamlProvider` Meteor Call
- 等级：Critical | 项目：Rocket.Chat | 披露：2021-01-08 | CVE：CVE-2020-29594
- 原文：https://hackerone.com/reports/1049375

- - - - - - - - 
**Summary:** Rocket.Chat exposes an unauthenticated Meteor method `addSamlProvider`, which allows disabling SAML signature verification.
**Description:**
The `addSamlProvider` Meteor method sets a number of settings, among them a boolean flag that defaults to `false`:
[code omitted]
The provider `name` is entirely user-controlled in this case.
Secondly, if a SAML authentication provider does not have a certificate set, or the setting is falsy, no validation is performed:
[code omitted]
## Releases Affected:
  * all versions including `meteor-accounts-saml`, i.e. 0.8.0 and later.
## Steps To Reproduce (from initial installation to vulnerability):
On the login page of a Rocket


## Unrestricted File Upload Leads to RCE on mobile.starbucks.com.sg
- 等级：Critical | 项目：Starbucks | 披露：2020-12-09 | CVE：-
- 原文：https://hackerone.com/reports/1027822

- - - - - - - - 
ko2sec discovered an .ashx endpoint on mobile.starbucks.com.sg intended for image files permitted unrestricted file type uploads which could lead to a potential RCE. ko2sec's thorough analysis provided additional endpoints on other out of scope domains that shared this vulnerability.
@ko2sec  — thank you for reporting this vulnerability and for confirming the resolution.
---

