# HackerOne 实战案例：modification-of-assumed-immutable-data-maid

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## property-expr - Prototype pollution
- 等级：High | 项目：Node.js | 披露：2020-09-24 | CVE：-
- 原文：https://hackerone.com/reports/910206

- - - - - - - - 
I would like to report Prototype pollution in property-expr
It allows attacker to modify the prototype of a base object.
# Module
**module name:** property-expr
**version:** 2.0.2
**npm page:** `https://www.npmjs.com/package/property-expr`
## Module Description
> Tiny property path utilities, including path parsing and metadata and deep property setters and getters
## Module Stats
> Replace stats below with numbers from npm’s module page:
[1,057,612] weekly downloads
# Vulnerability
## Vulnerability Description
> The functions setter can be tricked into modifying properties of the Object prototype. These properties will be present on all objects.
## Steps To Reproduce:
Run t

