# HackerOne 实战案例：missing-required-cryptographic-step

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Constant-time comparison is not always implemented; critical areas are vulnerable to key-timing attacks
- 等级：Critical | 项目：Monero | 披露：2018-08-06 | CVE：-
- 原文：https://hackerone.com/reports/363680

- - - - - - - - 
In my most superficial of reviews, constant-time comparison appears to not be globally implemented (at a glance, only implemented within the ref10 implementation).
With that said, the following areas either appear to be vulnerable, or are potentially vulnerable, to key-timing attacks:
1. Containers used for RingCT (in particular, the key struct) as deployed throughout RingCT
2. The definition and implementations of `CRYPTO_MAKE_COMPARABLE`
3. `equalKeys` in rctOps.cpp, whose comparison speed appears to be relative to its available hardware
For points 1 and 2, as a steadfast rule; do **NOT** use `memcmp` when comparing cryptographic secrets (or any cryptographic material for 


## Missing AES-GCM Authentication Tag Validation and Improper Deprecation Handling
- 等级：High | 项目：Node.js | 披露：2025-12-19 | CVE：-
- 原文：https://hackerone.com/reports/3463949

- - - - - - - - 
**Summary:**
In Node.js' crypto module, the `createDecipheriv` states that "the `authTagLength` option defaults to 16 bytes and must be set to a different value if a different length is used." ([here](https://nodejs.org/api/crypto.html#class-decipheriv:~:text=the%20authTagLength%20option%20defaults%20to%2016%20bytes%20and%20must%20be%20set%20to%20a%20different%20value%20if%20a%20different%20length%20is%20used.))
The authentication tag's length is however not validated against that default value and can be truncated down to either 4, 8, 12, 13, 14, or 15 bytes. ([here](https://github.com/nodejs/node/blob/4f24aff94ad9160bceaf9dcc9cf5235a65f01029/deps/ncrypto/ncrypto.h#L407-L40

