# HackerOne 实战案例：information-exposure-through-an-error-message

_3 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Lack of rate limiting in https://███/PKI/PassReset.aspx leads to PII disclosure and potential account takeover
- 等级：Critical | 项目：U.S. | 披露：2024-10-25 | CVE：-
- 原文：https://hackerone.com/reports/2748003

- - - - - - - - 
The password reset functionality of AFPC Secure is intended to be used by users who do not have a PKI credential for AFPC secure. It allows a user to provide their SSAN and Mother's Maiden Name to reset their password. The issue lies in the fact that if an SSAN for a user with an active PKI credential is found, the system will inform the user of that fact with the following error message:
[code omitted]
Additionally, there is no rate limiting done for this site, meaning an attacker can brute force through approximately 772,000,000 social security numbers to find SSANs for active U.S. Air Force personnel. Furthermore, if any SSANs are found that aren't tied to active PKI cred


## Able to log in with default ██████g creds at  https█████████████████████.mil
- 等级：High | 项目：U.S. | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/710813

- - - - - - - - 
**Summary████**
was able to use ████████████████████████ to log into this instance of Adobe Experience Manager, though it does not seem to be in used at the moment 
**Description███████**
while navigating to https█████████████████████████.mil, I performed some fuzzing and found that `/repository` was available which asked for authentication using `███████████████████` worked and I could then access another path found by fuzing `lc` [link](https█████████████.mil/lc) which then showed me the ██████ panel. 
## Impact
Medium since it is not being used
## Step-by-step Reproduction Instructions
1. Navigate to  https████████████████.mil/repository 
2. use ████████████████ (username


## information disclosure of secret_key_base via encoding charcters
- 等级：High | 项目：GitLab | 披露：2019-06-13 | CVE：-
- 原文：https://hackerone.com/reports/460545

- - - - - - - - 
@paresh_parmar discovered an error page that was disclosing the value of the `secret_key_base` key of customers.gitlab.com to unauthenticated users, which would have allowed an attacker to arbitrarily decrypt signed cookies.
**Summary (researcher):**
So I was fuzzing one parameter with different type of encodings. And one character threw error page .that page has secret token (rails)of application.
you can get RCE using a secret key base token. BUT  in this case serialization  was json `action_dispatch.cookies_serializer"=>:json`  so RCE was not possible that time.  still, you can do lots of stuff with `secret_key_base`  of application, depends on the application logic.
 tha

