# HackerOne 实战案例：blind-sql-injection

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Blind SQL injection on id.indrive.com
- 等级：Critical | 项目：inDrive | 披露：2023-11-24 | CVE：-
- 原文：https://hackerone.com/reports/2051931

- - - - - - - - 
## Summary:
The server does not perform sanitization on user input, allowing an attacker to inject arbitrary SQL commands into a query.
## Steps To Reproduce:
  1. Go to https://promo.indrive.com/10ridestogetprize_ru/random
  2. Click "Сгенерировать". A request to https://id.indrive.com/api/ten-drives/custom-winners/ten_drive_kz_second_weeks/number_trips/29/5/phone will be made:
████████
 3. Repeat this request, but change the path to: 
[code omitted]
A random entry from the database will be returned:
████
  4. Change the path in a query to:
[code omitted]
The response from the server will be empty:
███████
**Both requests in curl format**
[code omitted]
[code omitted]
## Im

