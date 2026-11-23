# HackerOne 实战案例：use-of-cache-containing-sensitive-information

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Cache Deception Allows Account Takeover
- 等级：High | 项目：Expedia | 披露：2023-04-01 | CVE：-
- 原文：https://hackerone.com/reports/1698316

- - - - - - - - 
## Summary:
I'm able to extract user's session (HASESSIONV3) as it is disclosed in a cacheable page, allowing me to access  the `ha.crumb` token located in  `/traveler/profile/edit` 
[code omitted]
## Steps To Reproduce:
Victim Steps:
1->Visit https://www.abritel.fr/search/keywords:soissons-france-(xss)/minNightlyPrice/x.jpeg?triagethis
Attacker Steps:
1->Visit the same URL using any other browser or do 
[code omitted]
{F1923081}
2-> use the token 
[code omitted]
and look for the `ha.crumb` variable in the response
## Recommended Remediation Steps 
  1. Add cache rules for certain all cacheable extensions
## Impact
Account Takeover
**Summary (researcher):**
I was able to Tak

