# HackerOne 实战案例：storing-passwords-in-a-recoverable-format

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## External storage app saves password for all users in the database
- 等级：High | 项目：Nextcloud | 披露：2021-03-01 | CVE：CVE-2020-8296
- 原文：https://hackerone.com/reports/867164

- - - - - - - - 
External storage (files_external) app save passwords of all users to database table "oc_credentials" even when "Log-in credentials, save in database" option is not used.
It's a security risk that allow password extraction of all users.
A local system admin that has access to database and nextcloud config file could decrypt any user password.


## Password Cracking - Weak Password Used to Secure ████ Containing a Plaintext Password
- 等级：High | 项目：U.S. | 披露：2021-02-18 | CVE：-
- 原文：https://hackerone.com/reports/985133

- - - - - - - - 
**Summary:**
I was able to crack the password to the ████████ located at ██████, as the pdf was protected with a weak password contained in a common word list. This guide contains steps to set-up the ███████ secure communication application with the unprotected configuration file located at██████████. This guide also contains a plaintext password for the configuration file.
## Step-by-step Reproduction Instructions
1. Browse to ███
2. Click `████████`. You will be prompted for a password.
3. Using wget, download the pdf: `wget ████████`.
4. Once downloaded, you can use `pdf2john` to convert the pdf password into a format that is parse-able by `john`: 
`perl /path/to/john/pdf

