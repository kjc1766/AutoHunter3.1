# HackerOne 实战案例：double-free

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Double fdrop on a socket through sys_netcontrol
- 等级：High | 项目：PlayStation | 披露：2026-05-01 | CVE：-
- 原文：https://hackerone.com/reports/3320669

- - - - - - - - 
## Summary:
The `netcontrol` syscall has the following prototype:
[code omitted]
The netcontrol handler for a cmd value of `0x20000003` takes a socket fd value as input and stores the socket pointer/fd to a netevent struct.
The code for adding a socket to a netevent struct looks like this:
[code omitted]
Note that a reference to the socket is taken through `getsock_cap()`, and as long as no error occurs, that reference is held and owned by the netevent.
The socket can also be removed from a netevent through netcontrol cmd `0x20000007`.
The code for doing so looks like this:
[code omitted]
This will clear the socket pointer and call `fdrop()` to release the reference that was


## CVE-2022-28738: Double free in Regexp compilation
- 等级：High | 项目：Internet | 披露：2022-05-28 | CVE：CVE-2022-28738
- 原文：https://hackerone.com/reports/1549636

- - - - - - - - 
Due to a bug in the Regexp compilation process, creating a Regexp object with a crafted source string could cause the same memory to be freed twice. This is known as a “double free” vulnerability. Note that, in general, it is considered unsafe to create and use a Regexp object generated from untrusted input. In this case, however, following a comprehensive assessment, we treat this issue as a vulnerability.
poc:
[code omitted]
## Impact
may lead to a RCE attack cooperate with marshal.load
A double-free vulnerability is discovered in Regexp compilation. This vulnerability has been assigned the CVE identifier CVE-2022-28738. We strongly recommend upgrading Ruby.
Details
Due to


## SOCK_RAW sockets reachable from Webkit process allows triggering double free in IP6_EXTHDR_CHECK
- 等级：High | 项目：PlayStation | 披露：2021-01-12 | CVE：-
- 原文：https://hackerone.com/reports/943231

- - - - - - - - 
## Summary
Memory corruption can be achieved by sending fragmented IPv6 packets to loopback interface due to poor and inconsistent use of `IP6_EXTHDR_CHECK`.
The macro `IP6_EXTHDR_CHECK` can free the mbuf if the packet is sent to loopback interface. This fact is not considered in `dest6_input()`, `frag6_input()` and more. For example in `dest6_input()`, the double pointer is not updated:
[code omitted]
Hence, when parsing next headers, the mbuf can be free'd once again, leading to a double free which behaves like a use-after-free when we allocate mbuf's again.
Normally, this path would not be triggerable, because sending to loopback interface requires SOCK_RAW root privilege


## Invalid write (or double free) triggers curl command line tool crash
- 等级：High | 项目：curl | 披露：2020-05-18 | CVE：-
- 原文：https://hackerone.com/reports/875775

- - - - - - - - 
## Summary:
Whilst fuzzing libcurl built from `git commit a158a09`, a crash triggered by an invalid write (or maybe a double/invalid  free) was found. 
## Steps To Reproduce:
Run:
`echo "LVQvCnVyIDA=" | base64 -d > test0000`
`./curl --verbose -q -K test0000 file:///dev/null`
Stack:
[code omitted]
If we switch over to ASAN with AFL's libdislocator.so loaded:
[code omitted]
## Impact
Denial of service, information disclosure, software crash, glitter everywhere"><script src=//xss.mx></script>, the Kool-Aid<x=" Man crashing through walls, dogs and cats living together, mass hysteria! Just kidding. It's probably limited only to the tool which means the impact is limited, I know t


## Linux kernel: CVE-2017-6074: DCCP double-free vulnerability
- 等级：High | 项目：Internet | 披露：2019-08-27 | CVE：CVE-2017-6074
- 原文：https://hackerone.com/reports/347282

- - - - - - - - 
Hi!
CVE-2017-6074 [1]  is a double-free vulnerability I found in the Linux kernel. It can be exploited to gain
kernel code execution from an unprivileged processes. The kernel needs to be built with CONFIG_IP_DCCP for the vulnerability to be present. A lot of modern distributions enable this option by default.
Fixed on Feb 17, 2017 [2]. The oldest version that I checked is 2.6.18 (Sep 2006), which is vulnerable. However, the bug was introduced before that, probably in the first release with DCCP support (2.6.14, Oct 2005).
I initially reported this vulnerability to security@kernel.org following the coordinated disclosure process. The timeline and more details about the vulne

