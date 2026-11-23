# HackerOne 实战案例：missing-encryption-of-sensitive-data

_3 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Waketime Payment Gateway Vulnerability
- 等级：High | 项目：WakaTime | 披露：2023-08-05 | CVE：-
- 原文：https://hackerone.com/reports/2097517

- - - - - - - - 
Summary: Waketime's payment gateway does not encrypt data in transit, which could allow an attacker to intercept and capture card information. This vulnerability could be exploited by a man-in-the-middle (MITM) attack, in which the attacker would insert themselves between the user and the payment gateway, intercepting the data as it is transmitted.
Steps to Reproduce:
Visit the Waketime website.
Proceed to subscribe and enter your credit card information.
Observe that the data is not encrypted in transit.
Expected Results: The data should be encrypted in transit, using a secure protocol.
Actual Results: The data is not encrypted in transit, and could be intercepted by an att


## ChaCha20-Poly1305 with long nonces
- 等级：High | 项目：Internet | 披露：2019-09-30 | CVE：CVE-2019-1543
- 原文：https://hackerone.com/reports/506040

- - - - - - - - 
This report relates to CVE-2019-1543, https://www.openssl.org/news/secadv/20190306.txt, which I reported to the OpenSSL maintainers a few days ago.
OpenSSL accepts nonces for the AEAD cipher ChaCha20-Poly1305 of up to 16-bytes. This support is advertised in the OpenSSL documentation and via the CHACHA_CTR_SIZE (16) constant.
However, the specification for ChaCha20-Poly1305 supports only up to 12-bytes.
If a user passes a 16-byte nonce to OpenSSL, OpenSSL will discard the first 4-bytes of the nonce.
## Impact
The maintainers classified the severity of this as LOW since it only affects user applications of OpenSSL, while at the same time recognizing the severity of this for th


## Yarn transfers npm credentials over unencrypted http connection
- 等级：High | 项目：Node.js | 披露：2019-08-14 | CVE：CVE-2019-5448
- 原文：https://hackerone.com/reports/640904

- - - - - - - - 
# Module
**module name:** yarn
**version:** 1.16.0
**npm page:** `https://www.npmjs.com/package/yarn`
## Module Description
> Fast, reliable, and secure dependency management.
## Module Stats
> Replace stats below with numbers from npm’s module page:
166 703 downloads in the last day
849 928 downloads in the last week
3 772 290 downloads in the last month
# Vulnerability
## Vulnerability Description
For scoped packages that are listed as `resolved "http://registry.npmjs.org/@...` in yarn.lock, yarn trasfers npm credentials (i.e. `_authToken`) over unencrypted http connection. This allows any MitM (for example, a proxy or a VPN) to sniff out npm credentials, given that the de

