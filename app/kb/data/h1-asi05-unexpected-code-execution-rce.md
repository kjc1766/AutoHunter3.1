# HackerOne 实战案例：asi05-unexpected-code-execution-rce

_1 份已披露报告（High/Critical 优先），来源 HackerOne 公开披露_

## MQTT CONNACK Packet Type Bypass leads to RCE via Malicious Broker
- 等级：Critical | 项目：curl | 披露：2026-05-05 | CVE：-
- 原文：https://hackerone.com/reports/3712343

- - - - - - - - 
## Summary:
`mqtt_verify_connack()` in `lib/mqtt.c` never checks that the received packet type is actually a CONNACK (`0x20`). The constant `MQTT_MSG_CONNACK` is commented out at line 45, making the check impossible to write. A malicious broker can send any packet — e.g. PUBACK (`0x40`) — with `remaining_length=2` and payload `0x00 0x00`, and curl will accept it as a valid handshake, subscribe to the topic, and begin receiving PUBLISH data. Since the broker now fully controls what bytes curl writes to the application's output, any caller that pipes or executes curl's output (OTA updaters, script runners, config loaders) is exposed to remote code execution. The existing 8.20.

