# HackerOne 实战案例：use-of-a-broken-or-risky-cryptographic-algorithm

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## 0 Click account takeover via timed requests to ███████forgot-password (single-packet attack)
- 等级：High | 项目：Mars | 披露：2024-07-11 | CVE：-
- 原文：https://hackerone.com/reports/2142109

- - - - - - - - 
An account takeover vulnerability was present in the forgot password functionality of ██████████. By sending carefully timed requests using a single-packet attack to the ████forgot-password path, an attacker is able to obtain the password reset token for any account on the platform. This attack requires only knowledge of the victim's email address registered on █████████████████████████████████.
---


## Inadequate Cryptographic Key Size and Insecure Cryptographic Mode.  File Name :- curl_ntlm_core.c
- 等级：High | 项目：curl | 披露：2021-03-08 | CVE：-
- 原文：https://hackerone.com/reports/1113663

- - - - - - - - 
The application is generating cryptographic keys or key pairs using a short and inadequate length.
This application is using the ECB (Electronic Codebook) mode of operation to perform encryption, which is considered semantically insecure.
Vulnerable File name :- curl_ntlm_core.c
Vulnerable line no. 274 :- err = CCCrypt(kCCEncrypt, kCCAlgorithmDES, kCCOptionECBMode, key,
## Impact
If a message with identical blocks is encrypted, an attacker get a certain advantage to have information on plaintext, by only observing CipherText.
---

