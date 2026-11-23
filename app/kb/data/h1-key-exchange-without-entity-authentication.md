# HackerOne 实战案例：key-exchange-without-entity-authentication

_2 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## 明確な認証不備および潜在的な中間者攻撃の可能性（Clear Authentication Deficiencies & Potential for Man-in-the-Middle Attacks）
- 等级：High | 项目：Sony | 披露：2025-07-08 | CVE：-
- 原文：https://hackerone.com/reports/2642615

- - - - - - - - 
English follows Japanese.
ソニーグループ株式会社 様
この度，弊社製品のWH-1000XM5に深刻なセキュリティ脆弱性を確認いたしましたのでご報告いたします．
セキュリティ研究者として，貴社製品の継続的なセキュリティと完全性を確保するために，このような発見を報告することは極めて重要であると考えます．
# Sec.0 要約
- 本レポートは，貴社製品のWH-1000XM5に確認された認証不備の脆弱性を示します．
- 本脆弱性をBluetoothの既存攻撃と組み合わせることで，容易にMitM攻撃を達成できます．
- 報告者は，本脆弱性へのCVE番号の割り当てを要求します．
# Sec.1 脆弱性の種類
認証不備
# Sec.2 脆弱性の詳細
悪意ある第三者（以後，攻撃者）WH-1000XM5とペアリングされたデバイスになりすますことで，WH-1000XM5が**ペアリングモードでなくても**，且つ**WH-1000XM5のユーザの操作を一切必要とせず**攻撃者デバイスと接続されます．
Bluetoothパケットを確認すると，WH-1000XM5の再接続時の認証に不備があり，Secure Simple Paring（SSP）の再接続時プロセスに準拠していません．
# Sec.3 影響を受ける製品
[WH-1000XM5](https://www.sony.jp/headphone/products/WH-1000XM5/)
**NOTE**
本脆弱性は，WH-1000XM5に限らない可能性があります．
# Sec.4 PoC


## Broken Authentication: A project addition request can be used multiple time for different users
- 等级：High | 项目：Semrush | 披露：2018-03-13 | CVE：-
- 原文：https://hackerone.com/reports/319480

- - - - - - - - 
> NOTE! Thanks for submitting a report! Please replace *all* the [square] sections below with the pertinent details. Remember, the more detail you provide, the easier it is for us to verify and then potentially issue a bounty, so be sure to take your time filling out the report!
**Summary:** 
[**Broken Authentication**. A project addition request can be used multiple time for different users]
**Description:** 
[**Reusable requests**. Once a project addition request is captured it can be used any number of times even after logout not only for the corresponding user but for any user with API key.
## Steps To Reproduce:
  1. Create two users for semrush.com 
		i) cleganearya1@g

