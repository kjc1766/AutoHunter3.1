# HackerOne 实战案例：improper-null-termination

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## HackerOne SAML signup domain enforcement bypass results in unauthorized access to HackerOne PullRequest organization
- 等级：High | 项目：HackerOne | 披露：2024-02-04 | CVE：-
- 原文：https://hackerone.com/reports/2101076

- - - - - - - - 
**Summary:**
SAML signup domain enforcement for new signups that belong to a SAML-enabled organization can be bypassed with trailing control characters. While the described issue affects all organizations with this feature enabled, it's possible to leverage it to access the PullRequest HackerOne organization, giving a real attacker access to HackerOne source code in Pull Requests.
**Description:**
When signing up on hackerone.com, email domains enforced by HackerOne SSO are not allowed for regular registration. The request to `/POST users` returns a redirect to the SSO provider:
[code omitted]
[code omitted]
However, adding a `%0d%0a` in the end of the email param will make 


## Improper handling of untypical characters in domain names
- 等级：High | 项目：Node.js | 披露：2021-09-10 | CVE：CVE-2021-22931
- 原文：https://hackerone.com/reports/1178337

- - - - - - - - 
# Description
Missing input validation of host names returned by Domain Name Servers in node's `dns` library can lead to output of wrong hostnames (leading to Domain Hijacking) and injection vulnerabilities in applications using the library (leading to Remote Code Execution, XSS, Applications crashes, etc.).
# Discoverer(s)/Credits
Philipp Jeitner, Fraunhofer SIT
# References
Injection Attacks Reloaded: Tunnelling Malicious Payloads over DNS
https://www.usenix.org/conference/usenixsecurity21/presentation/jeitner
(Available starting from August 11, 2021)
# Steps To Reproduce
Using the example application (`main.js`) which does dns lookups via node.
[code omitted]
Run the code


## Null byte Injection in https://████/
- 等级：High | 项目：U.S. | 披露：2020-05-14 | CVE：-
- 原文：https://hackerone.com/reports/709072

- - - - - - - - 
#Description:
Microsoft .NET Framework is prone to multiple NULL-byte injection vulnerabilities because it fails to adequately sanitize user-supplied data.
#Vulnerable URL: https://████/%2F%20This%20website%20is%20vulnerable%20to%20NULL%20BYTE%20INJECTION/
#Steps to Reproduce:
1) An attacker can exploit this issue via a browser.
The following example URI request is available:
https://███████/%2F%20This%20website%20is%20vulnerable%20to%20NULL%20BYTE%20INJECTION%00
#Mitigation: https://www.securityfocus.com/bid/24791/solution
#See Also: https://www.exploit-db.com/exploits/30281
#Proof of Concept: Screenshots attached.
## Impact
An attacker can exploit these issues to access se


## Vulnerability in http-parser & embedded NULL header handling
- 等级：High | 项目：Node.js | 披露：2020-02-13 | CVE：CVE-2019-9900
- 原文：https://hackerone.com/reports/536954

- - - - - - - - 
Due to a snafu in how security@node.js.org is setup to forward (see https://github.com/envoyproxy/envoy/issues/5155), the following bug report was not made available prior to disclosure. For completeness, I'm providing the original e-mail below. 
Please note that this has been fixed in http-parser since disclosures. I understand that Node has moved away from http-parser, but this might affect Node.JS LTS for earlier versions. See https://github.com/nodejs/http-parser/issues/468 for the fix.
Rather than file a full report, I would like to share with Node.JS security WG the following resources:
* Envoy CVE: https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2019-9900
* Envoy G


## Unauthenticated user can upload an attachment to the last updated report draft
- 等级：High | 项目：HackerOne | 披露：2018-10-09 | CVE：-
- 原文：https://hackerone.com/reports/419896

- - - - - - - - 
"What, HackerOne resolved a report that was submitted by @jobert?"
At HackerOne we often find security vulnerabilities ourselves. In most cases, we find them before new features even make it into production. Sometimes we find them when they're already in the wild. Recently we've launched a new feature called [retesting](https://docs.hackerone.com/hackers/retesting.html). Up until now, HackerOne would always retest our own findings. We're changing that. This is the first report we identified ourselves where we're expanding retesting to the community. When we identified this vulnerability, we filed a ticket to our own bug bounty program instead of filing an internal ticket. We

