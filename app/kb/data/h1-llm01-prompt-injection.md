# HackerOne 实战案例：llm01-prompt-injection

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Prompt Injection via GitHub Patch in Brave AI Chat (Leo)
- 等级：High | 项目：Brave | 披露：2025-08-22 | CVE：-
- 原文：https://hackerone.com/reports/3086301

- - - - - - - - 
**Component:** Brave AI Chat (`brave-core/components/ai_chat/`)
## Vulnerability Summary
The Brave AI Chat feature allows fetching `.patch` files from GitHub pull request pages to use as context. A combination of **insufficient path sanitization during URL construction** and **reliance on default URL normalization** allows an attacker to specify a crafted GitHub PR URL that, when processed by the Leo AI Chat feature, results in fetching a `.patch` file from an arbitrary public GitHub repository. Furthermore, the fetched patch content is **not adequately sanitized** before being included in the AI model's context, enabling prompt injection or context manipulation.
## Vulnerab

