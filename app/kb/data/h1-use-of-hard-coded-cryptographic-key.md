# HackerOne 实战案例：use-of-hard-coded-cryptographic-key

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Exposure of Hard-coded Private Keys and Credentials in curl Source Repository (CWE-321)
- 等级：Critical | 项目：curl | 披露：2025-08-12 | CVE：-
- 原文：https://hackerone.com/reports/3295650

- - - - - - - - 
Multiple private/test RSA keys and example credentials were discovered embedded in the public curl source repository and associated documentation. These sensitive secrets were detected using automated tools (gitleaks) and manual review. Their presence could allow attackers to impersonate trusted curl infrastructure, decrypt traffic, or pivot into build or CI systems if reused, creating a severe supply chain risk. Such exposures also risk compliance violations (e.g., GDPR, PCI-DSS, HIPAA) and undermine trust in open source releases.
This report, including the verification steps and analysis, was prepared using an AI security assistant to ensure comprehensive and reproducible 


## Slack DTLS uses a private key that is in the public domain, which may lead to SRTP stream hijack
- 等级：High | 项目：Slack | 披露：2020-03-12 | CVE：-
- 原文：https://hackerone.com/reports/531032

- - - - - - - - 
- Affects: Janus DTLS certificate

