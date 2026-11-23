# HackerOne 实战案例：file-manipulation

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Overwrite any file of the web server
- 等级：Critical | 项目：MOD | 披露：2024-11-05 | CVE：-
- 原文：https://hackerone.com/reports/2733190

- - - - - - - - 
## Summary:
With this vulnerability an attacker can override all the files from the server due to a vulnerable module used to generate █████████s
## Steps To Reproduce:
  1. Go to ██████████ to check the actual payload (*Save ███████ to:*) to do it (███████goedix.php -> This will create a file in /██████_h1goedix.php but this can be edited to index.php and replacing any php file in the server or outside the web server) █████
  1. Go to ███████ to start the job that creates the ███ in the target filepath
  1. Go to https://██████████_h1goedix.php or the targeted file and check that it returns an empty page! ██████████
> As note, if you want to do any action in /█████████ you 

