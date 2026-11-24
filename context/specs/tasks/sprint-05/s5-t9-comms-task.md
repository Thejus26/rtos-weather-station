# s5-t9: Comms task

| Field | Value |
|-------|-------|
| Task ID | `s5-t9-comms-task` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`comms_task`: wait on `WIFI_CONNECTED_BIT`, run the connection lifecycle, and publish entries from `publish_queue` only when MQTT is connected. Remove an entry only after a successful publish.

## Acceptance criteria

- [ ] Readings arrive at the subscriber.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| TSK-5 | `comms_task`: priority 3, 6 KB, waits on `WIFI_CONNECTED_BIT` |
| OBJ-2 | `publish_queue`: 10 x `reading_t`, `process_task` to `comms_task`, drop oldest when full |

## Dependencies

**Depends on:** 
- [`s5-t7-mqtt-client`](s5-t7-mqtt-client.md) (MQTT client)
- [`s5-t8-json-payload`](s5-t8-json-payload.md) (JSON payload)

**Blocks:** 
- [`s5-t10-outage-buffering`](s5-t10-outage-buffering.md) (Outage buffering)
- [`s5-t11-measure-publish-cadence`](s5-t11-measure-publish-cadence.md) (Measure publish cadence)
- [`s5-t13-credential-hygiene`](s5-t13-credential-hygiene.md) (Credential hygiene)
- [`s5-t14-comms-stack-check`](s5-t14-comms-stack-check.md) (Comms stack check)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
