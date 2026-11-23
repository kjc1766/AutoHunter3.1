# HackerOne 实战案例：incorrect-privilege-assignment

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## A potential risk in the experimental-programmatic-access-ccft which can be used to privilege escalation.
- 等级：High | 项目：AWS | 披露：2024-11-06 | CVE：-
- 原文：https://hackerone.com/reports/2808412

- - - - - - - - 
**Summary:**  I found a potential risk in the experimental-programmatic-access-ccft when I deployed it in the AWS Serverless Application Repository. A malicious can leverage the "sts:AssumeRole" permissions for "*" resources to escalate permission.
**Description:**  The experimental-programmatic-access-ccft application creates a function named ExtractCarbonEmissionsFunction, and the associated role is assigned policies with permissions such as "sts:AssumeRole " for  "*"  resources. A malicious user can leverage the "sts:AssumeRole" permissions to assume into any AWS Account in the AWS Organization, resulting in privilege escalation. This poses a significant security risk to 

