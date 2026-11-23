# HackerOne 实战案例：unrestricted-upload-of-file-with-dangerous-type

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Unrestricted File Upload at ██████████
- 等级：Critical | 项目：Mars | 披露：2024-02-19 | CVE：-
- 原文：https://hackerone.com/reports/2357778

- - - - - - - - 
The endpoint "████████" enables unrestricted file uploads, meaning anyone on the internet, without registration, can upload any type of file. This poses a security risk as unauthorized users could upload potentially harmful or malicious files without restriction.
---


## Stored XSS on ████████helpdesk
- 等级：High | 项目：U.S. | 披露：2020-07-30 | CVE：-
- 原文：https://hackerone.com/reports/901799

- - - - - - - - 
A Department of Defense(DoD) asset was vulnerable to Stored XSS due to a file upload feature. This may have led to Local File Inclusion. The DoD Representatives were responsive and thorough when handling my report.
**Summary (researcher):**
A Department of Defense(DoD) asset was vulnerable to Stored XSS due to a file upload feature. This may have led to Local File Inclusion. The DoD Representatives were responsive and thorough when handling my report.
---


## Unrestricted File Upload Leads to XSS & Potential RCE
- 等级：High | 项目：U.S. | 披露：2020-07-08 | CVE：-
- 原文：https://hackerone.com/reports/900179

- - - - - - - - 
**Summary:**
Unrestricted file upload at████████/request?openform. When the user wants to upload a file the app allows the user to upload a HTML file leading to stored XSS and creation of a simple php script. A user can upload the HTML file and trigger XSS and trigger potential RCE with php shell. Please go to the ██████ Request that I created at -- ██████████AllOpenOrders/4F4D0C69EA2B33A58525858A001E2B8C?opendocument and select the file at the bottom "unsure1.html" to trigger payload to show XSS and php shell. You can also go directly to the uploaded file at ████0/4f4d0c69ea2b33a58525858a001e2b8c/$FILE/unsure1.html. Please see the attached PoC video as well. Thanks.
## Impa


## Tricking the "Create snippet" feature into displaying the wrong filetype can lead to RCE on Slack users
- 等级：High | 项目：Slack | 披露：2020-06-30 | CVE：-
- 原文：https://hackerone.com/reports/833080

- - - - - - - - 
An issue in Slack's Create snippet feature results in filetypes being displayed incorrectly. This can lead to RCE if a Slack user downloads an executable file thinking that it is a CSV or other benign file type.
**Summary (researcher):**
https://www.youtube.com/watch?v=cIlGfnn4iG8
---

