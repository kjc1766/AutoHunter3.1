# HackerOne 实战案例：information-exposure-through-debug-information

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Information Disclosure through DEBUG at Subscription [https://app.dropcontact.io/app/subscription?connector=salesforce
- 等级：Critical | 项目：Dropcontact | 披露：2020-08-21 | CVE：-
- 原文：CRITICAL

](https://hackerone.com/reports/963921)
- - - - - - - - 
We were displaying some sytem information in case of app crashing.
---


## Trace.axd page leaks sensitive information
- 等级：Critical | 项目：U.S. | 披露：2019-08-19 | CVE：-
- 原文：https://hackerone.com/reports/519418

- - - - - - - - 
## Summary
`Trace.axd` leaks sensitive information on `██████████` by allowing signed in users to view previous requests sent to the webserver.
## Impact
Information leaked includes (but is not limited to):
- full names
- email addresses
- social security numbers
- dates of birth
- plaintext passwords
- cookies, session tokens, and CSRF tokens
- IP addresses and headers
- application specific information (endpoints, files and directories on the filesystem, software versions, )
## Step-by-step Reproduction Instructions
1. Visit https://████████/Gateway/sso.aspx and sign in. Note that any user can create a user (and any privilege level works for this vulnerability as long as a


## ASP.NET Application Trace Enabled
- 等级：High | 项目：U.S. | 披露：2026-01-12 | CVE：-
- 原文：https://hackerone.com/reports/2928785

- - - - - - - - 
**Description:**
The ASP.NET application trace feature is enabled on the public-facing URL: ██████████. This exposes sensitive internal information, including Session ID values and the physical file paths of server-side resources. An attacker could leverage this data to gain unauthorized insights into the server environment or session management mechanisms, increasing the risk of further exploitation.
PoC: ██████
## References
███████
███
## Impact
Information Disclosure: Reveals internal application structure and configuration.
Session Hijacking Risk: Exposed Session ID values could potentially allow unauthorized access to active user sessions.
Attack Surface Expansion: Exp


## Information Disclosure through Sentry Instance ███████
- 等级：High | 项目：Eternal | 披露：2019-09-19 | CVE：-
- 原文：https://hackerone.com/reports/697512

- - - - - - - - 
Hello team 
I found a bug (sensitive information ) can be used from attackers to perfom attack in youre server 
I don't know if this in scope so i'm sorry if i'm wrrong 
withou spending youre time 
 here the steps how i found this bug :
1-Please use burp suite to reproduce the same result 
2-i notice you have as tool for track errors (sentry) 
3- i send the request to ███ via /api/20/store█████████
4-change request from get to post 
Request:
==
POST /api/20/store██████ HTTP/1.1
Host: ███
Connection: close
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
██████
Sec-Fetch-Mode: navigate
Sec-Fetch-User: ?1
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image


## Real Time Error Logs Through Debug Information
- 等级：High | 项目：Slack | 披露：2019-04-11 | CVE：-
- 原文：https://hackerone.com/reports/503283

- - - - - - - - 
**Summary**: During the assessment, I have found the debug URL on slackb.com which is disclosing the World Wide real time error logs of Slack users.
The information leaked includes the following:
1. User Device Information
2. Redacted Token
3. Client IP Address
4. Description
5. Session ID
6. Team ID
7. User ID
8. User Agent
9. Server Response
10. Timestamp
11. api_call
12. x-amz-cf-id
13. x-amz-id-2
And other user sensitive information.
**Steps to Reproduce**
Open below URL in browser and refresh it to see real time logs.
https://slackb.com/debug
The vulnerable domain here is slackb.com. I have confirmed this with Slack to report this on Hackerone and mention the vulnerable

