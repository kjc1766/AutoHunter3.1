# HackerOne 实战案例：download-of-code-without-integrity-check

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## RCE on build server via misconfigured pip install
- 等级：Critical | 项目：Yelp | 披露：2021-02-09 | CVE：-
- 原文：https://hackerone.com/reports/946409

- - - - - - - - 
The following Python library has been installed on at least one Yelp owned build server directly from the public PyPI registry.
* https://pypi.org/project/yelp-cgeom/
This package should normally be downloaded from the internal Yelp registry, but a misconfiguration appears to have caused it to be downloaded from `pypi.org` instead.
This package name was previously unclaimed on PyPI. In order to detect such misconfigurations, I have uploaded my own code under the `yelp-cgeom` name.
Whenever `yelp-cgeom` is installed, my `setup.py` script is executed on the machine where it is downloaded. The script sends a callback to my server containing:
* the originating IP
* the machine's

