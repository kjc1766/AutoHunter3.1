# HackerOne 实战案例：use-after-free

_17 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## UAF on JSEthereumProvider
- 等级：Critical | 项目：Brave | 披露：2023-10-11 | CVE：-
- 原文：https://hackerone.com/reports/1977252

- - - - - - - - 
There is a UAF (Use After Free) vulnerability in the renderer implementation of the Ethereum wallet.
When the Ethereum wallet is connected, every V8 render gets this piece of code installed, creating a new object ethereum accessible from V8. You can find the code here: https://github.com/brave/brave-core/blob/45c6649a124dd8d0ffb19ca6f7047bebb6e6da2c/components/brave_wallet/renderer/js_ethereum_provider.cc#L163-L164
I will highlight some parts of the JSEthereumProvider::Install function that show the bug:
[code omitted]
The bug can be triggered through JavaScript with the following steps:
1. Get a reference to ethereum._metamask.
2. Delete the ethereum object, which deletes p


## Use after free and out of bounds read in xmlrpc_decode()
- 等级：Critical | 项目：Internet | 披露：2020-11-09 | CVE：CVE-2019-9020
- 原文：https://hackerone.com/reports/477896

- - - - - - - - 
Malformed input can lead to use after free and out of bounds memory errors.
This has been fixed with the latest updates of PHP (7.1.26/7.2.14/7.3.1).
(Note: I reported those as separate bugs to PHP, but they had the same underlying bug and were fixed by the same commit. The release notes only mention "out of bounds read", but this is misleading, as a use after free error is potentially more severe.)
Bugs reported to PHP:
https://bugs.php.net/bug.php?id=77242
https://bugs.php.net/bug.php?id=77249
## Impact
If the xmlrpc functionality of PHP is used to parse untrusted input from a public API point it can potentially be used to gain code execution.
---


## efree() on uninitialized Heap data in imagescale leads to use-after-free
- 等级：Critical | 项目：Internet | 披露：2020-10-10 | CVE：CVE-2016-10166
- 原文：https://hackerone.com/reports/478367

- - - - - - - - 
The core bug: https://bugs.php.net/bug.php?id=77269
This bugfix actually involves two vulnerabilities: a call to efree on uninitialized data and another free()  based vulnerability. What is described below is a bug that was fixed in libgd two years ago (CVE-2016-10166), but the patch was never applied to PHP's libgd. Furthermore, the patch for that CVE introduced a use after free vulnerability, also in PHPs `imagescale()` function. This can be seen in the comment history of the PHP bug.
----
The bug occurs in ext/gd/libgd/gd_interpolation.c in the function _gdContributionsAlloc(int line_size, int windows_size). The function will attempt to allocate helper structs and receive


## Exim use-after-free vulnerability while reading mail header involving BDAT commands
- 等级：Critical | 项目：Internet | 披露：2019-11-12 | CVE：CVE-2017-16943
- 原文：https://hackerone.com/reports/296991

- - - - - - - - 
Original article is [here](https://devco.re/blog/2017/12/11/Exim-RCE-advisory-CVE-2017-16943-en/)
# Use-after-free in receive_msg leads to RCE


## Use-After-Free in SMB connection reuse (req->path dangling pointer after needle destruction)
- 等级：High | 项目：curl | 披露：2026-04-29 | CVE：-
- 原文：https://hackerone.com/reports/3591956

- - - - - - - - 
## Summary
A heap-use-after-free occurs in `smb_send_open()` at `lib/smb.c` when curl processes two SMB URLs targeting the same host. The function `smb_parse_url_path()` sets `req->path` as a non-owning pointer into `smbc->share` (connection-owned memory). During connection reuse, the needle connection is freed via `Curl_conn_free()` → `smb_conn_dtor()`, which frees `smbc->share`, but `req->path` (on the easy handle) still references the freed buffer. The subsequent `strlen(req->path)` in `smb_send_open()` reads freed heap memory.
## Affected Version
curl 8.19.0-DEV (master branch, built March 8 2026)
Platform: Ubuntu 22.04 on x86_64 (WSL2)
Built with: gcc, OpenSSL, --enable


## Use-after-free in `curl_easy_ssls_export()` during callback re-entrancy
- 等级：High | 项目：curl | 披露：2026-04-29 | CVE：-
- 原文：https://hackerone.com/reports/3682666

- - - - - - - - 
## Summary:
`curl_easy_ssls_export()` iterates the SSL session list and invokes a caller-provided callback for each entry. If that callback calls `curl_easy_ssls_import()` on the same easy handle, the import path can evict and free the current session node while the export loop still holds it. The subsequent `Curl_node_next(n)` dereferences freed memory and triggers AddressSanitizer as a heap-use-after-free. I reproduced this on curl GitHub HEAD `54ded66618a2388e88e715c5eb4477d1083582ef`. The relevant code path is `lib/vtls/vtls_scache.c`, primarily `Curl_ssl_session_export()` around line 1214 with the related eviction path in `cf_scache_peer_add_session()` around line 781.



## Title: Use-After-Free in cURL Test Suite via Improper Cleanup of Global Handle
- 等级：High | 项目：curl | 披露：2025-12-05 | CVE：-
- 原文：https://hackerone.com/reports/3452725

- - - - - - - - 
**Title: Use-After-Free in cURL Test Suite via Improper Cleanup of Global Handle**
[code omitted]
**Description:**  
The `t1555_curl` global static pointer is improperly managed in the test cleanup routine. The function `test_cleanup` calls `curl_easy_cleanup(t1555_curl)` without ensuring the handle is either valid or NULL before cleanup, and it fails to reset the pointer to NULL after freeing it. This could lead to use-after-free or double-free conditions if `test_cleanup` is invoked multiple times (e.g., in loops or concurrent test executions).
**Attack Scenario:**  
An attacker could craft a test sequence that repeatedly triggers the cleanup routine, exploiting the lack o


## Stack use-after-scope in HTTP/3 POST request processing via CURLOPT_POSTFIELDS
- 等级：High | 项目：curl | 披露：2025-07-31 | CVE：-
- 原文：https://hackerone.com/reports/3279804

- - - - - - - - 
## Summary
  A stack use-after-scope vulnerability exists in libcurl's HTTP/3 request processing when using `CURLOPT_POSTFIELDS` with stack-allocated buffers. libcurl retains a pointer to user-provided POST data but accesses it after the original stack frame has been destroyed, leading to memory corruption and potential denial of service.
  The vulnerability occurs in `Curl_pretransfer()` at `transfer.c:569` when libcurl calls `strlen()` on the previously stored POST data pointer that now points to invalid stack memory.
 ##  Steps to Reproduce / Proof of Concept
  ### Environment
  - libcurl version: 8.16.0-DEV (master branch)
  - Compiler: Clang 20.1.8 with AddressSanitizer


## Use-After-Free in OpenSSL Keylog Callback via SSL_get_ex_data() in libcurl
- 等级：High | 项目：curl | 披露：2025-07-09 | CVE：-
- 原文：https://hackerone.com/reports/3242005

- - - - - - - - 
Summary:
A Use-After-Free (UAF) vulnerability exists in libcurl when the OpenSSL SSL_CTX_set_keylog_callback is set. The callback may be invoked after the associated SSL object has been freed via SSL_free(), leading to access to a dangling pointer and potential crash or information leak via SSL_get_ex_data().
This can be triggered manually or accidentally through custom keylog callbacks when ex_data is accessed inside the callback and the SSL object is no longer valid.
Security impact: Under specific conditions (when keylog callback is configured), it results in a segmentation fault (DoS). If further heap grooming or ex_data abuse is possible, this may lead to code execution


## sys_fsc2h_ctrl kernel stack free
- 等级：High | 项目：PlayStation | 披露：2025-04-18 | CVE：-
- 原文：https://hackerone.com/reports/2900606

- - - - - - - - 
## Summary
It is possible to cause a kernel stack free in the syscall sys_fsc2h_ctrl.
Consider 4 threads:
Thread 1: The command CMD_WAIT (0x10001) in sys_fsc2h_ctrl waits for path 1.
Thread 2: The command CMD_WAIT (0x10001) in sys_fsc2h_ctrl waits for path 2.
Thread 3: The command CMD_RESOLVE (0x20005) in sys_fsc2h_ctrl sets the pointer of path 2 to a local stack buffer and sleeps.
Thread 4: The command CMD_COMPLETE (0x20003) in sys_fsc2h_ctrl writes data into that local stack buffer and wakes up the thread 3.
Thread 2: This thread wakes up before thread 3 and it will free path 2. However, that is not a malloc() allocation, but it is actually a pointer to kernel stack.
## Im


## Use-after-free in setsockopt IPV6_2292PKTOPTIONS (CVE-2020-7457)
- 等级：High | 项目：PlayStation | 披露：2022-09-20 | CVE：CVE-2020-7457
- 原文：https://hackerone.com/reports/1441103

- - - - - - - - 
The PS5 is vulnerable to https://hackerone.com/reports/826026 which easily grants kernel access to an attacker. This vulnerability had been reported by me for the PS4 2 years ago when the PS5 did not yet exist, thus this should be considered as a new report and **not a duplicate**.
I was able to use this vulnerability in conjunction with the bd-j exploit chain to gain kernel access.
See https://www.freebsd.org/security/advisories/FreeBSD-SA-20:20.ipv6.asc for more details.
## Impact
Gain kernel access on PS5.
---


## CVE-2021-22901: TLS session caching disaster
- 等级：High | 项目：curl | 披露：2021-05-26 | CVE：CVE-2021-22901
- 原文：https://hackerone.com/reports/1180380

- - - - - - - - 
## Summary:
lib/vtls/openssl.c `ossl_connect_step1` sets up the `ossl_new_session_cb` sessionid callback with  `SSL_CTX_sess_set_new_cb`, and adds association from `data_idx` and `connectdata_idx` to current `conn` and `data` respectively:
[code omitted]
...
[code omitted]
 
Whenever the `ossl_new_session_cb` callback is called the code fetches the `conn` and `data` associated  via:
[code omitted]
However, it is possible that the connection is disassociated from these pointers via `Curl_detach_connnection`, and reassociated to a different connection via `Curl_attach_connnection`. Yet, `Curl_detach_connnection` doesn't `SSL_set_ex_data` the `data_idx` / `connectdata_idx`/ to 


## Node.js: use-after-free in TLSWrap
- 等级：High | 项目：Node.js | 披露：2021-01-05 | CVE：CVE-2020-8265
- 原文：https://hackerone.com/reports/988103

- - - - - - - - 
Node.js: use-after-free in TLSWrap
Node v14.11.0 (Current) is vulnerable to a use-after-free bug in its TLS implementation.
When writing to a TLS enabled socket, node::StreamBase::Write calls node::TLSWrap::DoWrite
with a freshly allocated WriteWrap object as first argument. If the DoWrite method
does not return an error, this object is passed back to the caller as part of a 
StreamWriteResult structure:
  // stream_base-inl.h
  WriteWrap* req_wrap = CreateWriteWrap(req_wrap_obj);
  err = DoWrite(req_wrap, bufs, count, send_handle);
  bool async = err == 0;
  if (!async) {
    req_wrap->Dispose();
    req_wrap = nullptr;
  }
  const char* msg = Error();
  if (msg != nullptr)


## Use-After-Free In IPV6_2292PKTOPTIONS leading To Arbitrary Kernel R/W Primitives
- 等级：High | 项目：PlayStation | 披露：2020-07-06 | CVE：-
- 原文：https://hackerone.com/reports/826026

- - - - - - - - 
## Summary
Due to missing locks in option `IPV6_2292PKTOPTIONS` of `setsockopt` , it is possible to race and free the `struct ip6_pktopts ` buffer, while it is being handled by `ip6_setpktopt`. This structure contains pointers (`ip6po_pktinfo`) that can be hijacked to obtain arbitrary kernel R/W primitives. As a consequence, it is easy to have kernel code execution. This vulnerability is reachable from WebKit sandbox and is available in the latest FW, that is 7.02.
## Attachment
Attached is a Proof-Of-Concept that achieves a Local Privilege Escalation on FreeBSD 9 and FreeBSD 12.
## Impact
- In conjunction with a WebKit exploit, a fully chained remote attack can be achieved.


## mod_http2, memory corruption on early pushes (CVE-2019-10081)
- 等级：High | 项目：Internet | 披露：2019-10-15 | CVE：CVE-2019-10081
- 原文：https://hackerone.com/reports/677557

- - - - - - - - 
HTTP/2 very early pushes, for example configured with `H2PushResource`, could lead to an overwrite of memory in the pushing request's pool, leading to crashes. The memory copied is that of the configured push link header values, not data supplied by the client. Scenarios where an attacker may be able to influence response header values could potentially lead to controlled code execution. (Code execution has not been demonstrated and is unlikely with the config included here.) This issue affects versions 2.4.20 through 2.4.39.
This CVE is noted on the [Apache HTTPD advisory list](https://httpd.apache.org/security/vulnerabilities_24.html) as of August 14, 2019.
Reproduction is


## CVE-2017-10966: Heap-use-after-free in Irssi <1.0.4
- 等级：High | 项目：Internet | 披露：2019-10-14 | CVE：CVE-2017-10966
- 原文：https://hackerone.com/reports/247028

- - - - - - - - 
35 days after reading https://irssi.org/2017/05/12/fuzzing-irssi/, I was able to trigger a heap-use-after-free in irssi 1.0.2.
Timeline:
Report to vendor: 16 June 2017
Acknowledge by vendor: 16 June 2017
Fixed by vendor: 7 July 2017
Advisory:
http://seclists.org/oss-sec/2017/q3/80
Patch:
https://github.com/irssi/irssi/commit/5e26325317c72a04c1610ad952974e206
[code omitted]
---


## CVE-2017-12858: Heap UAF in _zip_buffer_free() / Double free in _zip_dirent_read()
- 等级：High | 项目：Internet | 披露：2019-10-08 | CVE：CVE-2017-12858
- 原文：https://hackerone.com/reports/260414

- - - - - - - - 
libzip is a C library for reading, creating, and modifying zip archives. A partial list of projects using libzip include: [Plex Home Theater](https://support.plex.tv/hc/en-us/articles/204096476-License-Information), MySQL Workbench, ckmame, fuse-zip, lua-zip, **php zip extension**, zipruby, Endeavour2, FreeDink, DeaDBeeF (vfs_zip plugin), OpenLierox, ebook-tools, PDF Expert, ReaddleDocs, simple basic C++ wrapper for libzip, libzip++ - safe and modern c++14 wrapper around libzip, **Adobe (e.g., in Edge)**, PureBasic (ZipPacker), freebasic (ExtLibZip), Mercedes (S-Class), Kerkythea, G3D Innovation Engine, D'Fusion Studio, odt2tex - Libre/OpenOffice to LaTeX converter, *Kobo eR

