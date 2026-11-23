# HackerOne 实战案例：insufficient-session-expiration

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Can use the Reddit android app as usual even though revoking the access of it from reddit.com
- 等级：Critical | 项目：Reddit | 披露：2022-07-16 | CVE：-
- 原文：https://hackerone.com/reports/1632186

- - - - - - - - 
## Summary:
Hi Team,
For the last 4 days, I kept testing reddit web. That time, I revoked app access from the old.reddit.com and i checked my app and as expected i was not able to use the account in my app. 
After 2 days I was checking the chat invites feature on the web and after some time I turned on the internet on my mobile and got a Reddit "invitation accept"  notification. I clicked on that and I was surprised that I was able to use the previously revoked user account again in the Reddit app.
After I tried to reproduce the scenario again. I  thought the revoked account get access again after clicking on the app "chat invite" notification. 
- I again revoked the app acc


## Web Server Predictable Session ID on EdgeSwitch
- 等级：High | 项目：Ubiquiti | 披露：2021-05-23 | CVE：CVE-2020-8234
- 原文：https://hackerone.com/reports/774393

- - - - - - - - 
In EdgeSwitch legacy web interface the SIDSSL cookie for admin can be guessed, enabling the attacker to obtain high privileges and get a root shell by a Command injection.
These vulnerabilities were found on EdgeSwitch 1G switch (ESWH) and EdgeSwitch 10G switch (ESGH) firmware v1.9.0.
The fix for these vulnerabilities were included in the new version of EdgeMax EdgeSwitch firmware v1.9.1
For more details please visit:
https://community.ui.com/releases/EdgeMAX-EdgeSwitch-Firmware-v1-9-1-v1-9-1/8a87dfc5-70f5-4055-8d67-570db1f5695c
https://www.ui.com/download/edgemax
---


## Узнаем несколько цифр номера телефона юзера (можно флудить смс), всего раз узнав его remixsid и его ид юзера, и установка оффлайна юзерам.
- 等级：High | 项目：VK.com | 披露：2019-05-10 | CVE：-
- 原文：https://hackerone.com/reports/390126

- - - - - - - - 
Недостаточные проверки сессии.
**Summary (researcher):**
Было можно узнать часть номера телефона юзера и отправлять ему смс с ссылкой на приложение (https://vk.com/mobile) всего раз узнав его `remixsid`, вне зависимости сколько раз были ресетнуты сессии. Самый давний валидный для этой темы `remixsid`  был давности ~ май 2016 года.
Была возможность имея только ид юзера установить ему статус "оффлайн" (т.е. был в сети 1 сек назад и тд) и сбросить ему queue-ключи, что принудительно вызывало `/notifier.php?act=a_get_key` где был рейт лимит на получение ключей, таким образом можно было отключить юзеру queue серв (нотифиер, не тот что `imv4`, а `queuev4` - те реалтайм события не п


## Session replay vulnerability in www.urbandictionary.com
- 等级：High | 项目：Urban | 披露：2017-06-20 | CVE：-
- 原文：https://hackerone.com/reports/216294

- - - - - - - - 
# Session replay vulnerability in www.urbandictionary.com
I considered titling this bug "*Session tokens not expiring*", which is what you need to tell your development team. But I titled it as I did to emphasize at least one attack made possible by the bug. There may be others.
## Description
Privileged functions, e.g., `/handle.save.php` can still be used after the user has clicked the "sign out" link. The cause of the vulnerability seems to be that the server is not invalidating session cookies when the user "signs out". I observed session tokens remaining valid even 72 hours after being issued.
Exploitation requires the anti-CSRF `authenticity_token` from the privileged 

