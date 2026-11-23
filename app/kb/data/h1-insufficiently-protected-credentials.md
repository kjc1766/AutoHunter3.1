# HackerOne 实战案例：insufficiently-protected-credentials

_9 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Authentication Token Theft via Open Redirect in Callback URL Parameter
- 等级：Critical | 项目：lemlist | 披露：2025-11-14 | CVE：-
- 原文：https://hackerone.com/reports/3419636

- - - - - - - - 
An open redirect vulnerability has been identified in the email signup flow of taplio.com that enables authentication token theft through manipulation of the callback URL parameter. 
The vulnerability occurs when an attacker modifies the callbackUrl parameter during the email signup process to point to an attacker-controlled domain. 
When a victim completes the email verification process by clicking the verification link, they are redirected to the malicious domain along with their authentication tokens. 
This redirection happens automatically as part of the normal signup flow, making it particularly dangerous since users expect to be redirected after email verification. 
Th


## Hashed data exposure via WebSockets to Workspace Members
- 等级：Critical | 项目：Slack | 披露：2023-09-21 | CVE：-
- 原文：https://hackerone.com/reports/1639600

- - - - - - - - 
When users created or revoked a Shared Invite Link for their workspace, Slack transmitted a hashed version of their password to other workspace members. This hashed password was not visible in any Slack clients; discovering it required actively monitoring encrypted network traffic coming from Slack’s servers. We immediately fixed the underlying bug and released an update the same day. While we have no reason to believe that anyone was able to obtain plaintext passwords because of this issue, we reset affected users’ Slack passwords and notified customers about the issue. See Slack’s blog post from August 2022 for additional details https://slack.com/intl/en-in/blog/news/noti


## Weak/Auto Fill Password
- 等级：Critical | 项目：MTN | 披露：2022-09-03 | CVE：-
- 原文：https://hackerone.com/reports/817331

- - - - - - - - 
## Summary:
https://mtnc-selfservice.mtncameroon.net
The following url has admin/admin as user name and password 
## Steps To Reproduce:
  1. open the url in any browser of your choice
  1. enter admin as user name and password
  1. booom .... full asset to super admin full panel 
## Supporting Material/References:
See attached screenshots
## Impact
Attacker can make major configuration changes to the services.
**Summary (researcher):**
Pure luck!!!  - admin/admin
All login page ==MUST== be tested with admin/admin & root/root.
---


## CVE-2022-27774: Credential leak on redirect
- 等级：High | 项目：curl | 披露：2022-04-27 | CVE：CVE-2022-27774
- 原文：https://hackerone.com/reports/1543773

- - - - - - - - 
## Summary:
Curl can be coaxed to leak user credentials to third-party host by issuing HTTP redirect to ftp:// URL.
## Steps To Reproduce:
  1. Configure for example Apache2 on `firstsite.tld` to perform redirect with mod_rewrite:
     [code omitted]
  2. Capture credentials at `secondsite.tld` for example with:
     [code omitted]
  3. `curl -L --user foo  https://firstsite.tld/redirectpoc`
  4. The entered password is visible in the fake FTP server:
[code omitted]
There are several issues here:
1. The credentials are sent to a completely different host than the original host (`firstsite.tld` vs `secondsite.tld`). This is definitely not what the user could expect, consideri


## Insecure ███████ credentials on staging app at ████ leads to application takeover
- 等级：High | 项目：U.S. | 披露：2021-02-10 | CVE：-
- 原文：https://hackerone.com/reports/1051885

- - - - - - - - 
**Summary:**
A ██████████ application called "████" has an old endpoint that accepts insecure/test ████████ credentials despite being a publicly-accessible IP. This endpoint also provides the ability to view information that may be FOUO, to exfiltrate information on registered personnel or contractors, to upload files, and to change configuration settings with ███████████████ privileges.
**Description:**
The IP address ███ points to a deployment of an application called ████/█████, which is a DoD-owned system on █████████). The login for this deployment accepts insecure ███ credentials (███).
There is also an authentication/█████ panel accessible at https://██████████externa


## nextcloud-snap CircleCI project has vulnerable configuration which can lead to exposing secrets
- 等级：High | 项目：Nextcloud | 披露：2021-01-29 | CVE：-
- 原文：https://hackerone.com/reports/794407

- - - - - - - - 
## Summary:
CircleCI allows projects to configure whether builds will run as a result of a pull request from a fork, and also whether these fork PRs have access to the secrets stored in the parent repo's CircleCI settings. When both settings are enabled, and the repo associated with the project allows PRs to come from forks from any user (which Github always allows), then a CircleCI project is vulnerable to leaking secrets. Please see the following for documentation on this:
https://circleci.com/docs/2.0/oss/#pass-secrets-to-builds-from-forked-pull-requests
Particularly:
> If you are comfortable sharing secrets with anyone who forks your project and opens a PR, you can enabl


## Improper integrity protection of server-side encryption keys
- 等级：High | 项目：Nextcloud | 披露：2020-11-13 | CVE：CVE-2020-8259
- 原文：https://hackerone.com/reports/732431

- - - - - - - - 
The public keys used for the server-side encryption are not integrity-protected. These can easily replaced by anyone who has access to the data-at-rest data (even when the per-user-keys are enabled, as described in https://nextcloud.com/security/threat-model/). This holds true for all key types - from the master key, the per-user-keys as well as for the (optional) recovery key.
Attack scenarios may look like this:
* A recovery key is set by the admin and users enabled the recovery feature (or it was mandatorily set by adding the corresponding configuration to the `oc_preferences` table for all users). As it is unlikely that the recovery key is used very often, a person that 


## China - Leaked credentials permitted a limited ability to create Starbucks coupons and cards
- 等级：High | 项目：Starbucks | 披露：2020-04-01 | CVE：-
- 原文：https://hackerone.com/reports/766770

- - - - - - - - 
neweq discovered a Github repository exposing credentials with which they could obtain an access token. The access token permitted limited access to generate Starbucks coupons and cards.
@neweq — thank you for reporting this vulnerability.
---


## Account takeover via leaked session cookie
- 等级：High | 项目：HackerOne | 披露：2019-12-03 | CVE：-
- 原文：https://hackerone.com/reports/745324

- - - - - - - - 
**Summary:**
You are disclose for me you session
**Description:**
you are gevi me your session on last report
I am can use your session(sorry)
███
████████
█████████
## Impact
HackerOneStaff Access, i can read all reports @security and more program
# Incident Report | 2019-11-24 Account Takeover via Disclosed Session Cookie
*Last updated: 2019-11-27*
## Issue Summary
On November 24, 2019 at 13:08 UTC, HackerOne was notified through the HackerOne Bug Bounty Program by a HackerOne community member (“hacker”) that they had accessed a HackerOne Security Analyst’s HackerOne account. A session cookie was disclosed due to a human error, which led to the hacker being able to access 

