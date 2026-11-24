# s5-t2: Local broker

| Field | Value |
|-------|-------|
| Task ID | `s5-t2-local-broker` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Run Mosquitto locally (`mosquitto -v`) and subscribe with `mosquitto_sub -t "weather/#" -v`.

## Acceptance criteria

- [ ] A manual publish shows up in the subscriber.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |

## Dependencies

**Depends on:** none

**Blocks:** none in the roadmap

## Open questions

- the broker is run locally on the developer machine. The roadmap does not say whether the board and the broker must be on the same network or whether authentication is used.

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
