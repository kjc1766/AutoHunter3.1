# HackerOne 实战案例：session-fixation

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## ████████ portal is open to enumeration once authenticated.  Session ID's appear static.  All PII available once a valid session ID is found.
- 等级：Critical | 项目：U.S. | 披露：2021-04-20 | CVE：-
- 原文：https://hackerone.com/reports/1150573

- - - - - - - - 
**Description:**
Once Authenticated to █████████ portal with valid credentials you can type in another members session id and you can see any service members data as if you were authenticated as them.
https://█████████
I did not see if there was a way to dump all session id's, but wouldn't be too surprised if it was vulnerable to this.
## References
Replacing that string above with valid session ID's let me see ██████ info
## Impact
All PII held in ██████████ portal exposed.  █████████.  
If website doesn't stop me, I could either dump the list of id's or utilize a tool to brute force a range.
## System Host(s)
█████████
## Affected Product(s) and Version(s)
## CVE Numbers
#


## Cookie injection from non-secure context
- 等级：High | 项目：curl | 披露：2022-05-13 | CVE：-
- 原文：https://hackerone.com/reports/1560324

- - - - - - - - 
## Summary:
Curl allows injecting cookies over insecure HTTP connection that will then be sent to the target site when connecting over HTTPS.
As documented in lib/cookie.c https://github.com/curl/curl/blob/a04f0b961333e1a19848d073d8c7db9c20b2a371/lib/cookie.c#L1039 this should not be possible:
[code omitted]
This will allow session fixation (CWE-384) attack where the attacker replaces the session of the victim with their own. If the victim performs for example upload operations the upload will be sent to the account controlled bit he attacker.
This attack requires that the application in question does or  can be coaxed to make accesses to the same host over insecure HTTP con

