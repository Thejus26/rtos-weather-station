# s5-t4: Wi-Fi station

| Field | Value |
|-------|-------|
| Task ID | `s5-t4-wifi-station` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Wi-Fi station start-up. The event handler sets and clears `WIFI_CONNECTED_BIT`.

## Acceptance criteria

- [ ] The bit follows the connection state.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |

## Dependencies

**Depends on:** 
- [`s5-t3-nvs-config`](s5-t3-nvs-config.md) (NVS config)

**Blocks:** 
- [`s5-t5-wifi-backoff`](s5-t5-wifi-backoff.md) (Wi-Fi backoff)
- [`s5-t6-sntp-time`](s5-t6-sntp-time.md) (SNTP time)
- [`s5-t7-mqtt-client`](s5-t7-mqtt-client.md) (MQTT client)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
