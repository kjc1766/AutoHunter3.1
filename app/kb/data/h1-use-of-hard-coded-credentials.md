# HackerOne 实战案例：use-of-hard-coded-credentials

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Exposed valid AWS, Mysql, Sendgrid and other secrets
- 等级：Critical | 项目：Glovo | 披露：2022-07-08 | CVE：-
- 原文：https://hackerone.com/reports/1580567

- - - - - - - - 
## Summary:
Hi team,
I just discovered some hardcoded credentials allowing access to AWS, Mysql database, ...
To make this report short, here is the POC: 
see ███ & █████
## Steps To Reproduce:
where there are the info : 
<p>
APP_NAME=Glovo
APP_ENV=local
APP_KEY=█████
APP_DEBUG=false
APP_URL=http://localhost
LOG_CHANNEL=stack
LOG_LEVEL=debug
DB_CONNECTION=mysql
DB_HOST=██████████
DB_PORT=3306
DB_DATABASE=████████
DB_USERNAME=█████
DB_PASSWORD=█████████
BROADCAST_DRIVER=log
CACHE_DRIVER=file
QUEUE_CONNECTION=sync
SESSION_DRIVER=file
SESSION_LIFETIME=120
MEMCACHED_HOST=127.0.0.1
REDIS_HOST=█████
REDIS_PASSWORD=██████████
REDIS_PORT=11773
MAIL_MAILER=smtp
MAIL_HOST=mailhog
MAIL


## Hardcoded AWS credentials in ███████.msi
- 等级：Critical | 项目：8x8 | 披露：2022-04-29 | CVE：-
- 原文：https://hackerone.com/reports/1368690

- - - - - - - - 
A hardcoded AWS access token was discovered within an MSI file available for download on the 8x8 site. The researcher was able to demonstrate access to 8x8 AWS infrastructure. The token was promptly restricted.
---


## JumpCloud API Key leaked via Open Github Repository.
- 等级：Critical | 项目：Starbucks | 披露：2019-12-30 | CVE：-
- 原文：https://hackerone.com/reports/716292

- - - - - - - - 
**Summary:** Open Github Repo Leaking Starbucks JumbCloud API Key
**Description:** 
Team,
While going through Github search I discovered a public repository which contains Jumbcloud API Key of Starbucks. 
Repo:  [https://github.com/██████████/Project](https://github.com/██████████/Project).
File: [https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go](https://github.com/████/Project/blob/0d56bb910923da2fbee95971778923f734a25f68/getSystemUsers.go)
[code omitted]
**POC**
* List systems [code omitted] There are multiple AWS instances present
* [code omitted]
* SSO Applications [code omitted] AWS login SAM config is presents. This would 


## Important information leaked on Github
- 等级：High | 项目：Equifax-vdp | 披露：2019-08-22 | CVE：-
- 原文：https://hackerone.com/reports/649322

- - - - - - - - 
While searchin on Github about Equifax i found some juicy information like a username and password of this subdomain (https://transport5.ec.equifax.com/), internal ip of the database and its username & password 
 In the following link (https://github.com/ajiththorali/Testing/blob/49025b364451fb2076f85ad009a0dc50a941c5ce/target/classes/API_Equifax/propertiesHandle.properties) you could find this info 
*******
XML_URL = https://transport5.ec.equifax.com/ists/stspost?require_security= HTTP/1.1
Username = 50404
Password = ny5b2MuswjrFq3J2P9
service_name = acroxmltest
Content_Type = application/xml
*******
jdbc_driver = com.mysql.jdbc.Driver
db_url = jdbc:mysql://192.168.84.225:3

