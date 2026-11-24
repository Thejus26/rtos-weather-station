# s5-t7: MQTT client

| Field | Value |
|-------|-------|
| Task ID | `s5-t7-mqtt-client` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

MQTT client start-up. The event handler sets and clears `MQTT_CONNECTED_BIT` and handles reconnects.

## Acceptance criteria

- [ ] The bit follows the broker connection.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |

## Dependencies

**Depends on:** 
- [`s5-t4-wifi-station`](s5-t4-wifi-station.md) (Wi-Fi station)

**Blocks:** 
- [`s5-t9-comms-task`](s5-t9-comms-task.md) (Comms task)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
