# HackerOne 实战案例：xml-entity-expansion

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Pippo XML Entity Expansion (Billion Laughs Attack)
- 等级：High | 项目：Central | 披露：2019-06-10 | CVE：CVE-2019-5442
- 原文：https://hackerone.com/reports/506791

- - - - - - - - 
# Maven artifact
**groupId:** ro.pippo
**artifactId:** pippo-jaxb
**version:** 1.12.0
# Vulnerability
## Vulnerability Description
> Pippo unsafely parses user provided XML. The `fromString()` in the `ro.pippo.jaxb.JaxbEngine` class allows user provided DTDs that the rest of the XML may reference. This can lead to recursive entity expansion and a subsequent billion laughs attack.
## Additional Details
**Source File and Line Number:** https://github.com/pippo-java/pippo/blob/7da9f4db945d10113cf4ea4ed44ba0f1a7f83a8f/pippo-content-type-parent/pippo-jaxb/src/main/java/ro/pippo/jaxb/JaxbEngine.java#L78
## Steps To Reproduce:
> Detailed steps to reproduce with all required referen

