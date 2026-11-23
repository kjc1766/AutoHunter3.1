# HackerOne 实战案例：client-side-enforcement-of-server-side-security

_4 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## Ability to  bypass Admin override on Cloudflare WARP Android
- 等级：High | 项目：Cloudflare | 披露：2023-09-07 | CVE：CVE-2023-3747
- 原文：https://hackerone.com/reports/2043885

- - - - - - - - 
Zero Trust Administrators have the ability to disallow end users from disabling WARP on their devices. Override codes can also be created by the Administrators to allow a device to temporarily be disconnected from WARP, however, due to lack of server side validation, an attacker with local access to the device, could extend the maximum allowed disconnected time of WARP client granted by an override code by changing the date & time on the local device where WARP is running.
---


## Ability to bypass locked Cloudflare WARP on wifi networks.
- 等级：High | 项目：Cloudflare | 披露：2022-11-16 | CVE：CVE-2022-3512
- 原文：https://hackerone.com/reports/1635748

- - - - - - - - 
Using warp-cli command "add-trusted-ssid", a user was able to disconnect WARP client and bypass the "Lock WARP switch" feature resulting in Zero Trust policies not being enforced on an affected endpoint.
---


## I found another way to bypass Cloudflare Warp lock!
- 等级：High | 项目：Cloudflare | 披露：2022-11-07 | CVE：CVE-2022-3321
- 原文：https://hackerone.com/reports/1605847

- - - - - - - - 
It was possible to bypass [Lock WARP switch feature](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/warp-settings/#lock-warp-switch) on WARP iOS mobile client by enabling both "Disable for cellular networks" and "Disable for Wi-Fi networks" switches at once in the application settings. Such configuration caused WARP client to disconnect and allowed the user to bypass restrictions and policies enforced by the Zero Trust platform.
The issue was fixed in version 6.14 of the iOS mobile client.
---


## Completely remove VPN profile from locked WARP iOS cient.
- 等级：High | 项目：Cloudflare | 披露：2022-11-07 | CVE：CVE-2022-3337
- 原文：https://hackerone.com/reports/1633231

- - - - - - - - 
It was possible for a user to delete VPN profile from  WARP mobile client on iOS platform despite the [Lock WARP switch](https://developers.cloudflare.com/cloudflare-one/connections/connect-devices/warp/warp-settings/#lock-warp-switch) feature being enabled on Zero Trust Platform. This led to bypassing policies and restriction enforced for enrolled devices by the Zero Trust platform.
The issue was fixed in Warp iOS mobile client v. 6.15.
---

