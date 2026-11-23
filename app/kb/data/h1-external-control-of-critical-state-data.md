# HackerOne 实战案例：external-control-of-critical-state-data

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## match
- 等级：High | 项目：curl | 披露：2022-06-09 | CVE：-
- 原文：https://hackerone.com/reports/1555440

- - - - - - - - 
## Steps To Reproduce:
lib/telnet.c suboption function incorrecly checks for the sscanf return value. Instead of checking that 2 elements are parsed, the code also continues if just one element matches:
if(sscanf(v->data, "%127[^,],%127s", varname, varval)) {
As such it is possible to construct environment values that don't update the varval buffer and instead use the previous value. In combination of advancing in the temp buffer by strlen(v->data) + 1, this means that there will be uninitialized gaps in the generated output temp buffer. These gaps will contain whatever stack contents from previous operation of the application.
Fortunately the environment is controlled by th


## Disclosure of internal information using hidden NTLM authentication leading to an exploit server
- 等级：High | 项目：MTN | 披露：2021-08-04 | CVE：-
- 原文：https://hackerone.com/reports/853284

- - - - - - - - 
By using a request get on the url [██████████](███████) of the blog.
we collect sensitive information from blogs
## step 
Typically, when visiting a website  █████████ or directory  ██████ requiring privileged access, the server will initiate a login prompt. This allows the client to send blank username and password values to check for NTLM authentication and receive the encoded response. However, if the target server is configured to allow windowsAuthentication, it may be possible to invoke this response without a login prompt. This can be done by adding “Authorization: ███” to the request headers.
Once an NTLM challenge is returned in the “WWW-Authenticate” value of the re

