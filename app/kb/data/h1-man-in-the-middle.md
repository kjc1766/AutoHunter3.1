# HackerOne 实战案例：man-in-the-middle

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Fetching the update json scheme from concrete5 over HTTP leads to remote code execution
- 等级：High | 项目：Concrete | 披露：2021-09-22 | CVE：CVE-2021-40099
- 原文：https://hackerone.com/reports/982130

- - - - - - - - 
Hi,
I noticed that concrete5 fetches the update JSON scheme from www.concrete5.org over HTTP.
The fetched json defines the download URL, so we can simply tamper with this JSON in order to make the update URL point to a server controlled by us.
Combining this with the possibility to set an arbitrary proxy for outgoing communications leads to RCE.
Privileges required: Administrator
Preconditions: the directory "updates" has to be writable from the application. 
Magic word for submitting the report: crayons
Here the steps to reproduce:
- Login with a user with Administrator privileges.
- Set the proxy to an attacker controlled proxy (here I used a Burp instance for the sake of 


## Repositories of datanucleus are fetched over insecure protocol (http insted of https)
- 等级：High | 项目：Central | 披露：2020-10-05 | CVE：-
- 原文：https://hackerone.com/reports/879740

- - - - - - - - 
Maven artifact
groupId: org.datanucleus
artifactId: datanucleus-maven-parent
version: 4.0.0
Vulnerability
the jar files inside repositories are fetched using insecure protocol (http instead of https). This allows these artifacts to be potentially MITMed to maliciously compromise them and infect the build artifacts that are produced. Additionally, if any of these JARs or other dependencies were compromised, any developers or production servers using these could continue to be infected past updating to fix this.
Additional Details
Source File and Line Number: https://search.maven.org/artifact/org.datanucleus/datanucleus-maven-parent/4.0.0/pom (line : 21)
Vulnerable File(s): ht


## Node.js: TLS session reuse can lead to hostname verification bypass
- 等级：High | 项目：Node.js | 披露：2020-06-03 | CVE：CVE-2020-8172
- 原文：https://hackerone.com/reports/811502

- - - - - - - - 
The Node.js TLS library supports client side reuse of TLS sessions when multiple connections to the same server are opened.
Code that wants to use this feature can listen for the 'session' event (https://nodejs.org/api/tls.html#tls_event_session) on a tls.TLSSocket to get notified of newly created TLS sessions. The documentation for this event explicitly mentions that the passed sessions "can be used immediately or later".
The problem with this design is that 'session' events are triggered even if verification of the server certificate hostname in onConnectSecure fails. (https://github.com/nodejs/node/blob/b1d4c13430c92e94920f0c8c9ba1295c075c9e89/lib/_tls_wrap.js#L1502):
onC


## Industry-Wide MITM Vulnerability Impacting the JVM Ecosystem
- 等级：High | 项目：Internet | 披露：2019-09-10 | CVE：-
- 原文：https://hackerone.com/reports/608620

- - - - - - - - 
I've been exploring the industry-wide scope of the use of HTTP to resolve dependencies in build infrastructure across the industry. What I unearthed was that some of the most popular libraries and two compilers were impacted by this vulnerability.
## Vulnerability
[CWE-829: Inclusion of Functionality from Untrusted Control Sphere](https://cwe.mitre.org/data/definitions/829.html)
[CWE-494: Download of Code Without Integrity Check](https://cwe.mitre.org/data/definitions/494.html)
The full scope of this vulnerability is captured in my blog post here:
[Want to take over the Java ecosystem? All you need is a MITM!](https://medium.com/@jonathan.leitschuh/want-to-take-over-the-java


## Catch mails sent to an SMTP Server over SSL using an Evil SMTP Server
- 等级：High | 项目：Ubiquiti | 披露：2019-08-22 | CVE：CVE-2019-5456
- 原文：https://hackerone.com/reports/519582

- - - - - - - - 
A malicious actor setting up an SMTP proxy server between the UniFi Controller and their actual SMTP server can record their SMTP credentials for malicious use.
---

