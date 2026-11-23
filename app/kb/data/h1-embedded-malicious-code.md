# HackerOne 实战案例：embedded-malicious-code

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## flatmap-stream malicious package (distributed via the popular events-stream)
- 等级：Critical | 项目：Node.js | 披露：2018-11-26 | CVE：-
- 原文：https://hackerone.com/reports/450006

- - - - - - - - 
I would like to report a case of malicious package (flat-stream) that made it's way into many other npm packages. One such popular package is `event-stream` (user dominictarr transferred the ownership of an npm module to another user because he wasn't actively maintaining it. That user then added malicious dependency to the package)
See discussion here: 
https://github.com/dominictarr/event-stream/issues/116
# Module
**module name:**  flatmap-stream
**version:** [MODULE VERSION]
**npm page:** `https://www.npmjs.com/package/flatmap-stream` (removed from npm by now)
## Module Description
It is not yet clear what the malicious code was doing. 
See discussion here: https://githu

