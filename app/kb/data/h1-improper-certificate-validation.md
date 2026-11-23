# HackerOne 实战案例：improper-certificate-validation

_12 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Silent TLS Trust Model Hijacking via `CURL_CA_BUNDLE` Environment Variable Leads to MITM
- 等级：Critical | 项目：curl | 披露：2025-11-11 | CVE：-
- 原文：https://hackerone.com/reports/3418776

- - - - - - - - 
## Summary:
curl is vulnerable to silent Man-in-the-Middle (MITM) attacks
due to its design, which implicitly trusts the CA certificate path specified in the CURL_CA_BUNDLE environment variable.
This mechanism allows the entire TLS trust model (chain of trust) of curl to be hijacked without any warning or notification to the user. This fundamentally violates the security promise of HTTPS connections, where users trust that curl will strictly verify server identities. By failing to warn when the system trust store is replaced, curl creates a false sense of security, allowing attackers to decrypt and manipulate HTTPS traffic.
I confirm that I performed the vulnerability discov


## Remotely trigger an assertion on a TLS server with a malformed certificate string
- 等级：Critical | 项目：Node.js | 披露：2020-02-06 | CVE：CVE-2019-15604
- 原文：https://hackerone.com/reports/746733

- - - - - - - - 
**Summary:** 
Connecting to a NodeJS TLS server with a client certificate that has a type 19 string in its subjectAltName will crash the TLS server if it tries to read the peer certificate.
Affected versions include v10.17.0 and v13.1.0.
This is related to issue https://github.com/nodejs/node/issues/30521 but it works the other way around: in that issue, the client crashes; in this example, the server crashes. 
It is likely that the fix for that issue will also fix this.
**Description:** 
Using e.g. node-forge it is possible to create certificates without common name and with any subjectAltName content.  Hence anybody can create a malformed certificate and send it to a node 


## Silent omission of certificate hostname verification in LibreSSL and BoringSSL
- 等级：Critical | 项目：Internet | 披露：2019-09-26 | CVE：CVE-2018-8970
- 原文：https://hackerone.com/reports/329645

- - - - - - - - 
## Abstract
LibreSSL and BoringSSL implemented ``X509_VERIFY_PARAM_set1_host`` differently than OpenSSL. All applications that use the preferred and documented way to configure a TLS connection for hostname validation, silently neglect to perform hostname validation at all. As a consequence, they are vulnerable to MitM attacks.
## Description
OpenSSL 1.0.2 introduced the function [X509_VERIFY_PARAM_set1_host](https://www.openssl.org/docs/man1.0.2/crypto/X509_VERIFY_PARAM_set1_host.html). It sets the expected DNS hostname for a TLS connection. During the handshake, OpenSSL verifies, that the hostname matches one of the DNS names in the subject alternative name extension of th


## The Microsoft Store Uber App Does Not Implement Certificate Pinning
- 等级：Critical | 项目：Uber | 披露：2017-12-24 | CVE：-
- 原文：https://hackerone.com/reports/293358

- - - - - - - - 
## Summary
The Microsoft Store Uber App (Windows Phone Architecture) does not properly implement certificate pinning.
## Security Impact
Layer-2+ network traffic transmitted from and received by the app can be surreptitiously intercepted and transparently modified by an attacker, with no warnings or errors presented to the app user.
## Reproduction Steps
A transparent Layer-2 MITM proxy was configured between a device running the most recent release of the Uber app for Windows Phone Architecture and an Internet gateway. Self-signed certificates were asserted on behalf of the remote systems that the app communicated with. All traffic transmitted and received by the Uber app w


## SameSite restrictions are lifted, and SameSite:Strict cookie are being sent.
- 等级：High | 项目：Brave | 披露：2025-10-15 | CVE：CVE-2018-12402,
- 原文：https://hackerone.com/reports/3253725

- - - - - - - - 
## Summary:
hello, Brave team.
There are cases where the SameSite policy is being bypassed, and I would like to report them.
When a user left-clicks a link in a cross-domain context and selects "Open Link in Split View," all cookies—including those with SameSite=Strict—are sent, even though it is a cross-site navigation.
* For SameSite cookies, only SameSite=Lax cookies should be sent during cross-site navigations.
Before providing a detailed explanation, here is a list of CVEs and issues that were reported as a result of SameSite violations.: 
https://issues.chromium.org/issues/40057062
https://issues.chromium.org/issues/40050641
https://issues.chromium.org/issues/40057831



## Apple SecTrust legacy path accepts untrusted certificates on pre-10.14 macOS/iOS when built with USE_APPLE_SECTRUST
- 等级：High | 项目：curl | 披露：2025-10-09 | CVE：-
- 原文：https://hackerone.com/reports/3374554

- - - - - - - - 
## Summary:
When libcurl is built with USE_APPLE_SECTRUST and runs on Apple OS versions that lack SecTrustEvaluateWithError (macOS <10.14 / iOS <12), the legacy verification path miscompares OSStatus to SecTrustResultType and never checks the SecTrust result. This can cause untrusted certificates to be accepted.
[Statement clarifying if an AI was used to find the issue or generate the report]
This report was prepared with assistance from an AI code analysis tool; the core diagnosis and scope were validated by a combination of classical software, manual inspection of the code, and AI.
## Affected version
Reproduced on current master (as of 2025‑10‑07). Affects builds that ena


## curl allows SSH connection even if host is not in known_hosts
- 等级：High | 项目：curl | 披露：2025-02-05 | CVE：-
- 原文：https://hackerone.com/reports/2961050

- - - - - - - - 
## Summary:
Curl does _not_ fail if the SSH host identity cannot be verified due to the host not being included in the `.ssh/known_hosts` file. This makes using curl to login into an previously unknown ssh host system vulnerable to meddler in the middle attacks. When using key based authentication it will allow a malicious host to spoof the real system, and either return tampered or otherwise malicious content on download, or capture the uploads. When using username + password authentication it will also leak the username and password to the attacker, and thus allow the attacker to connect to the intended target host. 
Curl does have `--insecure` option which is said to:
[co


## Undici does not use CONNECT or otherwise validate upstream HTTPS certificates when using a proxy
- 等级：High | 项目：Node.js | 披露：2022-07-13 | CVE：CVE-2022-32210
- 原文：https://hackerone.com/reports/1583680

- - - - - - - - 
**Summary:** When using Undici with its ProxyAgent, it does not use CONNECT or correctly verify the upstream server's HTTPS certificate.
**Description:**
This affects both Undici itself and global fetch() in Node 18 when used with Undici's ProxyAgent. I've submitted this here for Node as it affects global fetch, and Undici isn't listed in the options (even though Undici's SECURITY.md says to report issues the same way as Node issues: https://github.com/nodejs/undici/blob/main/SECURITY.md)
Some context is required to explain the issue so this is quite long, sorry!
In general, given a setup like:
Undici client -> proxy.example -> remote-server.example
There's two possible ways


## Undici ProxyAgent vulnerable to MITM
- 等级：High | 项目：Internet | 披露：2022-07-13 | CVE：-
- 原文：https://hackerone.com/reports/1599063

- - - - - - - - 
Full GitHub advisory summarizing the issue is here: https://github.com/nodejs/undici/security/advisories/GHSA-pgw7-wx7w-2w33
The original Node.js HackerOne report is here: https://hackerone.com/bugs?report_id=1583680
This was fixed & disclosed in Undici v5.5.1.
This primarily affects Undici, a subproject under the Node.js umbrella, which is experimentally included as part of recent Node.js releases. This issue doesn't immediately affect standalone Node.js usage today due to the limited APIs initially exposed, but it does affect all usage of Node.js's new Fetch API with HTTP proxies (since Undici was required for that) and @mcollina in https://hackerone.com/bugs?report_id=158


## Acronis True Image 2021 (windows) does not validate server hostname on a login TLS connection
- 等级：High | 项目：Acronis | 披露：2021-08-10 | CVE：-
- 原文：https://hackerone.com/reports/1070533

- - - - - - - - 
Acronis True Image prior to 2021 Update 4 for Windows, Acronis True Image prior to 2021 Update 5 for Mac did not properly validate SSL certificate. The issue was assigned CVE-2021-32581. We have seen no signs of the exploitation of this vulnerability.
---


## Acronis True Image  (Windows) does not validate server certificate on a TLS connection
- 等级：High | 项目：Acronis | 披露：2021-08-05 | CVE：-
- 原文：https://hackerone.com/reports/1056144

- - - - - - - - 
Acronis True Image prior to 2021 Update 4 for Windows, Acronis True Image prior to 2021 Update 5 for Mac did not implement SSL certificate validation. The issue was assigned CVE-2021-32581. We have seen no signs of the exploitation of this vulnerability.
---


## Only OpenSSL handles a CRL when passed in via CApath
- 等级：High | 项目：curl | 披露：2021-01-08 | CVE：-
- 原文：https://hackerone.com/reports/713975

- - - - - - - - 
## Summary:
Code in vtls/nss.c interprets CApath option differently than OpenSSL-using code,
user can be mislead to unsecure use of curl/libcurl easily. CApath directory
can contain CRL files in addition to CA certificate files and they are used
for certificate verification when curl calls OpenSSL. Code path using NSS blindly
loads all files residing in CApath as CA certificates instead, which has two effects:
first, the meaning of CRLs is ignored and revoked certificates can be accepted,
second, NSS may find duplicate SN in corrupt 'CA certificate' during TLS handshake and break
connection to legitimate server (NSS does not perform full validation in load
and search routine

