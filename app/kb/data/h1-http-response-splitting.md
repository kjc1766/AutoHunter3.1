# HackerOne 实战案例：http-response-splitting

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## HTTP Smuggling multiple issues in Squid 3.x & squid 4.x
- 等级：Critical | 项目：Internet | 披露：2021-08-26 | CVE：CVE-2019-18678,
- 原文：https://hackerone.com/reports/758445

- - - - - - - - 
Hello, as can be seen on a recent public security update by Squid I reported several smuggling issues.
If you want some background on impact of Smuggling issues You can check the current works of James Keetle or my own previous published works.
* https://www.youtube.com/watch?v=upEMlJeU_Ik  HTTP Desync Attacks: Smashing Into The Cell Next Door - James Kettle
* https://www.youtube.com/watch?v=dVU9i5PsMPY  DEF CON 24 - regilero - Hiding Wookiees in HTTP: HTTP smuggling
But I'm quite sure that the recent additions of Smuggling tools in Burp suite is making Smuggling impacts issues more easy to understand now.
# CVE-2019-18678
 
* http://www.squid-cache.org/Advisories/SQUID-2019


## RubyのCGIライブラリにHTTPレスポンス分割（HTTPヘッダインジェクション）があり、秘密情報が漏洩する
- 等级：High | 项目：Ruby | 披露：2022-11-24 | CVE：CVE-2021-33621,
- 原文：https://hackerone.com/reports/1204695

- - - - - - - - 
PoC1:
[code omitted]
Actual Result1:
[code omitted]
このケースでは不正なクッキーが注入される。
PoC2:
[code omitted]
Actual Result2:
[code omitted]
このケースでは500 Internal Server Errorのため、Locationヘッダは無視され、JavaScriptが実行される。
## Impact
意図しないHTTPレスポンスヘッダやHTTPレスポンスボディを外部から注入できます。
単純なHTTPヘッダインジェクションでは、クッキーのインジェクションやリダイレクト等が主な影響となりますが、このケースでは、レスポンスボディが注入できるため、不正なJavaScript実行に及ぶため、影響が大きいと考えます。
他の言語の場合、PHPのheader関数は "\r"  "\n"   "\r\n"   等をすべてエラーにするため、上記の攻撃はできません。
過去のWEBrickやPumaにも類似の脆弱性がありましたが、これらは単独のキャリッジリターン "\r" による攻撃しかできず、リバースプロキシとしてNginxがあれば、Nginx側にてエラーになります。したがって、現実的な危険性はほとんどないと考えます。
https://www.ruby-lang.org/en/news/2019/10/01/http-response-splitting-in-webrick-cve-2019-16254/
https://github.com/puma/

