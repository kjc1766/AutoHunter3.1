# HackerOne 实战案例：missing-critical-step-in-authentication

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## JWT audience claim is not verified
- 等级：Critical | 项目：Internet | 披露：2023-04-16 | CVE：CVE-2023-22482
- 原文：https://hackerone.com/reports/1889161

- - - - - - - - 
All versions of Argo CD starting with v1.8.2 are vulnerable to an improper authorization bug causing the API to accept certain invalid tokens.
OIDC providers include an aud (audience) claim in signed tokens. The value of that claim specifies the intended audience(s) of the token (i.e. the service or services which are meant to accept the token). Argo CD does validate that the token was signed by Argo CD's configured OIDC provider. But Argo CD does not validate the audience claim, so it will accept tokens that are not intended for Argo CD.
## Impact
If Argo CD's configured OIDC provider also serves other audiences (for example, a file storage service), then Argo CD will accep

