# HackerOne 实战案例：use-of-cryptographically-weak-pseudo-random-number-generator-prng

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Weak randomness in WebCrypto keygen
- 等级：High | 项目：Node.js | 披露：2022-10-26 | CVE：CVE-2022-35255
- 原文：https://hackerone.com/reports/1690000

- - - - - - - - 
https://github.com/nodejs/node/pull/35093 introduced a call to `EntropySource()` in `SecretKeyGenTraits::DoKeyGen()` in `src/crypto/crypto_keygen.cc`. There are two problems with this:
1. It does not check the return value, it assumes `EntropySource()` always succeeds, but it can (and sometimes will) fail.
2. The random data returned by`EntropySource()` may not be cryptographically strong and therefore not suitable as keying material.
An example is a freshly booted system or a system without `/dev/random` or `getrandom(2)`.
## Impact
`EntropySource()` calls out to openssl's `RAND_poll()` and `RAND_bytes()` in a best-effort attempt to obtain random data.
OpenSSL has a built-i

