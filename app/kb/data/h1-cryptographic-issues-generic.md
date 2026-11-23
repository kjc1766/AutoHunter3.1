# HackerOne 实战案例：cryptographic-issues-generic

_16 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## RCE (Remote code execution) in one of DoD's websites
- 等级：Critical | 项目：U.S. | 披露：2020-07-30 | CVE：CVE-2017-1000486
- 原文：https://hackerone.com/reports/874924

- - - - - - - - 
**Summary:**
The targeted website is vulnerable to CVE-2017-1000486, by only running command was (whoami) to prove that the RCE exist has been run successfully on the target
**Description:**
The target uses a vulnerable version of primefaces : Primetek Primefaces 5.x, that is vulnerable to a weak encryption flaw resulting in remote code execution
## Impact
Critical
## Step-by-step Reproduction Instructions
Using the following exploit : https://github.com/pimps/CVE-2017-1000486
1. python primefaces.py████████/
## Product, Version, and Configuration (If applicable)
Primefaces 5.3.6
## Suggested Mitigation/Remediation Actions
Primefaces has to be updated to a newer version
## I


## █████████ - Insecure download cookie generation allows bypass of CAC authentication, access to deleted and locked files
- 等级：Critical | 项目：U.S. | 披露：2020-05-11 | CVE：-
- 原文：https://hackerone.com/reports/496326

- - - - - - - - 
**Summary:**
To download a file, ████ directs users to `/██████████/Download.aspx` and sets a cookie authenticating the download. The cookie looks like this:
[code omitted]
If an attacker can generate this cookie, this allows downloading a file. As it turns out, the generation of the cookie is fairly straightforward and requires no server-side key, only a file ID and its associated password. The components are:
1. The file ID, base 64 encoded, followed by a dash
2. The SHA512 hash of the plaintext file ID, base 64 encoded
3. The secret key of the package (as sent in the email), base 64 encoded, followed by a dash
4. The SHA2512 hash of the secret key, base 64 encoded
By gene


## RCE on https://█████/ Using CVE-2017-9248
- 等级：Critical | 项目：U.S. | 披露：2019-10-10 | CVE：CVE-2017-9248
- 原文：https://hackerone.com/reports/491668

- - - - - - - - 
Summary:
https://█████████/ is hosting an unpatched version of the Telerik DialogHandler Telerik.Web.UI.DialogHandler.aspx allowing for the machine key to be brute forced. The machine key can be used to access the DNN file manager to upload arbitrary files including ASPX giving a web shell and RCE.
Description:
Telerik has a known cryptographic weakness in older versions of the Dialog Handler which when exploited can be used to brute force the machine key and gain access to the DNN file manager. The file manager allows for ASPX shell upload and RCE.
Step-by-step Reproduction Instructions
Hit https://███/Providers/HtmlEditorProviders/Telerik/Telerik.Web.UI.DialogHandler.aspx 


## elections.k8s.io uses weak session secret key, may place elections at risk
- 等级：High | 项目：Kubernetes | 披露：2025-09-19 | CVE：-
- 原文：https://hackerone.com/reports/1387366

- - - - - - - - 
## Summary
Hi there, I have been working on a new tool to detect misconfigured session signing across bug bounty programs, called CookieMonster. Many applications use stateless cookies to preserve session information (i.e. who has logged in), but many applications do not properly secure this. @nagli and I discovered that `elections.k8s.io` uses a weak Flask SECRET_KEY, literally the string `N/A`, to sign authentication cookies.
In many applications, this allows the complete compromise of the application, as you can manipulate who you are logged in as. This would be especially problematic for an election voting system. It seems, in the case of Elekto, this may not be the case


## HashDoS in V8
- 等级：High | 项目：Node.js | 披露：2025-07-15 | CVE：CVE-2025-27209
- 原文：https://hackerone.com/reports/3131758

- - - - - - - - 
The V8 release used in Node.js v24.0.0 has changed how string hashes are computed using rapidhash. This implementation re-introduces the HashDoS vulnerability as an attacker who can control the strings to be hashed can generate many hash collisions - an attacker can generate collisions even without knowing the hash-seed.
* This vulnerability affects Node.js v24.x users.
---


## Improper error handling in async cryptographic operations crashes process
- 等级：High | 项目：Node.js | 披露：2025-05-14 | CVE：CVE-2025-23166
- 原文：https://hackerone.com/reports/2817648

- - - - - - - - 
The C++ method SignTraits::DeriveBits() may incorrectly call ThrowException() based on user-supplied inputs when executing in a background thread, crashing the Node.js process. Such cryptographic operations are commonly applied to untrusted inputs. Thus, this mechanism potentially allows an adversary to remotely crash a Node.js runtime.
---


## Signature Verification /// golang.org/x/crypto/ssh
- 等级：High | 项目：Sifchain | 披露：2021-12-09 | CVE：-
- 原文：https://hackerone.com/reports/1276384

- - - - - - - - 
## Summary:
Crypto package are vulnerable to Improper Signature Verification "
An attacker can craft an ssh-ed25519 or sk-ssh-...@openssh.com public key, such that the library will panic when trying to verify a signature with it. Clients can deliver such a public key and signature to any golang.org/x/crypto/ssh server with a PublicKeyCallback, and servers can deliver them to any golang.org/x/crypto/ssh client "
Introduced through: github.com/Sifchain/sifnode@0.0.0 › golang.org/x/crypto@v0.0.0-20201016220609-9e8e0b390897
Introduced through: github.com/Sifchain/sifnode@0.0.0 › github.com/tyler-smith/go-bip39@v1.1.0 › golang.org/x/crypto@v0.0.0-20200622213623-75b288015ac9
and f


## Apple Pay cryptogram replay and amount tampering
- 等级：High | 项目：RBKmoney | 披露：2021-03-10 | CVE：-
- 原文：https://hackerone.com/reports/996540

- - - - - - - - 
During Apple Pay in-app or on-site payments the device generates a payment cryptogram, which contains a transaction ID, encrypted payment data, etc.
This is an example of the cryptogram which the phone passes to the internet acquiring service on api.transferwise.com:
[code omitted]
                
Data field contains encrypted onlinePaymentCryptogram which represents "Online payment cryptogram, as defined by 3-D Secure."
Apple also requires to "Inspect the CMS signing time of the signature, as defined by section 11.3 of RFC 5652. If the time signature and the transaction time differ by more than a few minutes, it's possible that the token is a replay attack."
This is all de


## Some build dependencies are downloaded over an insecure channel (without subsequent integrity checks)
- 等级：High | 项目：Internet | 披露：2020-12-04 | CVE：-
- 原文：https://hackerone.com/reports/1039504

- - - - - - - - 
## Summary:
Build jobs [`mingw64 | openssl-1.1.1d`](https://github.com/OpenVPN/openvpn/blob/master/.travis.yml#L87) and [`mingw32 | openssl-1.0.2u`](https://github.com/OpenVPN/openvpn/blob/master/.travis.yml#L91) download dependencies from `build.openvpn.net` and `www.oberhumer.com`over an insecure channel (`http`, _not_ `https`) and do not check their integrity in any way.
This opens the door to person-in-the-middle attacks, whereby an attacker controlling an intermediate node on the network path between Travis CI's build servers and those two servers could manipulate traffic and inject his own malicious code into the artifacts produced by the two jobs in question.
## Steps


## Critical vulnerability in JSON Web Encryption (JWE) - RFC 7516 Invalid Curve attack
- 等级：High | 项目：Internet | 披露：2019-11-12 | CVE：-
- 原文：https://hackerone.com/reports/213437

- - - - - - - - 
We found an issue in the JWE specification where it fails to warn the implementers about Invalid Curve attack.
We found several libraries to be vulnerable :   node-jose, jose2go, Nimbus JOSE+JWT and jose4j and in the process of filing an errata for the RFC.
We report the vulnerabilities to the maintainers that promptly fixed the issue.
We also wrote a blog post about it in order to reach the highest number of people potentially vulnerable. You can find the write up in [0,1,2].
[0] http://blog.intothesymmetry.com/2017/03/critical-vulnerability-in-json-web.html
[1] http://blogs.adobe.com/security/2017/03/critical-vulnerability-uncovered-in-json-encryption.html
[2] https://auth


## WordPress Automatic Update Protocol Does Not Authenticate Updates Provided by the Server
- 等级：High | 项目：WordPress | 披露：2019-07-22 | CVE：-
- 原文：https://hackerone.com/reports/228854

- - - - - - - - 
When the WordPress automatic update process is initiated (likely via `wp-cron.php`), this is the path the code takes:
* https://github.com/WordPress/WordPress/blob/4a6f90db58a935abb688cfb91b391dffeda7b35c/wp-admin/includes/class-wp-upgrader.php#L242-L283
* https://github.com/WordPress/WordPress/blob/38347d7c580be4cdd8476e4bbc653d5c79ed9b67/wp-admin/includes/file.php#L482-L525
* https://github.com/WordPress/WordPress/blob/9f4bbcdb7896a7baba9eb88add281f3fbcdec0ef/wp-includes/http.php#L67-L71
* https://github.com/WordPress/WordPress/blob/76d77e927bb4d0f87c7262a50e28d84e01fd2b11/wp-includes/class-http.php#L597-L613
* https://github.com/WordPress/WordPress/blob/76d77e927bb4d0f87c


## Samlify is vulnerable to signature wrapping
- 等级：High | 项目：Node.js | 披露：2018-10-23 | CVE：-
- 原文：https://hackerone.com/reports/356284

- - - - - - - - 
I would like to report a signature wrapping weakness in samlify
It allows an attacker to modify a SAML token received from the IdP before validating it with the service provider
# Module
**module name:** samlify
**version:** 2.3.7
**npm page:** `https://www.npmjs.com/package/samlify`
## Module Description
Highly configuarable Node.js SAML 2.0 library for Single Sign On
## Module Stats
> Replace stats below with numbers from npm’s module page:
1084 downloads in the last week
# Vulnerability
## Vulnerability Description
It's possible to wrap the signature of a SAML response, and insert a new username in the original token, thus make it appear as though a different user was aut


## Timing Attack in Google Authenticator - Per User Prompt
- 等级：High | 项目：Ian | 披露：2017-10-29 | CVE：-
- 原文：https://hackerone.com/reports/277534

- - - - - - - - 
*Google Authenticator - Per User Prompt* contains a timing attack vulnerability in how it validates the application password for a user account.
[code omitted]
__wp-content/plugins/google-authenticator-per-user-prompt/google-authenticator-per-user-prompt.php__
As the above code runs on the `authenticate` hook, and uses a strict equality check, it's possible to brute force an application password using a timing attack and gain access to the account, without needing the real password or even a valid OTP token.
The plugin adds two `authenticate` hooks, one for the above app password check, then a second that does the OTP validation stuff, but *only* if the not using an app pass


## NexTable: Credentials exposure
- 等级：High | 项目：Eternal | 披露：2017-06-30 | CVE：-
- 原文：https://hackerone.com/reports/120941

- - - - - - - - 
There was an issue with how the NexTable was storing passwords for merchants. This was fixed by the NexTable Team.
Thanks @mrtuxracer for reporting this.
---


## SSL/TLS Vulnerability at khanacademy.org
- 等级：High | 项目：Khan | 披露：2017-02-22 | CVE：CVE-2016-2183
- 原文：https://hackerone.com/reports/207457

- - - - - - - - 
CVE - 2011 - 3389
Description : 
The SSL protocol, as used in certain configurations in Microsoft Windows and Microsoft Internet Explorer, Mozilla Firefox, Google Chrome, Opera, and other products, encrypts data by using CBC mode with chained initialization vectors, which allows man-in-the-middle attackers to obtain plaintext HTTP headers via a blockwise chosen-boundary attack (BCBA) on an HTTPS session, in conjunction with JavaScript code that uses (1) the HTML5 WebSocket API, (2) the Java URLConnection API, or (3) the Silverlight WebClient API, aka a "BEAST" attack.
Problem Location : 
https://www.khanacademy.org/
Mitigation : 
The Upgrade TLS version on the server to late


## Twitter iOS fails to validate server certificate and sends oauth token
- 等级：High | 项目：X | 披露：2016-12-23 | CVE：CVE-2016-10511
- 原文：https://hackerone.com/reports/168538

- - - - - - - - 
Twitter on iOS newest two versions (6.62 and 6.62.1) are affected, other versions not tested. Tested independently on two different iPhone 6 with iOS version 9.3.3 and 9.3.5 without Jailbreak. The iPhone were without any mobileconfig profiles installed - *no* we did not install any CA certificate in the CA store of the device. Really stock iPhones. The Twitter app does not check the SSL/TLS certificate of https://api.twitter.com . A transparent proxy setup (eg. burp suite in transparent mode) is sufficient to exploit. Steps to reproduce:
1. Start Burp or other Proxy software in transparent mode. Setting "Generate CA-signed per-host certificates", which means the CA cert of B

