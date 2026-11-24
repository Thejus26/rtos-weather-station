# s5-t5: Wi-Fi backoff

| Field | Value |
|-------|-------|
| Task ID | `s5-t5-wifi-backoff` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Reconnect with exponential backoff using `backoff_next_ms` (1 s, doubling to 60 s), reset after a success.

## Acceptance criteria

- [ ] The log shows 1, 2, 4 ... 60 s delays with the AP off.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-7 | Wi-Fi reconnect backoff 1 s doubling up to 60 s |
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| ERR-3 | Wi-Fi/MQTT loss: keep sampling and displaying, buffer, reconnect with backoff |

## Dependencies

**Depends on:** 
- [`s5-t4-wifi-station`](s5-t4-wifi-station.md) (Wi-Fi station)
- [`s1-t9-backoff`](../sprint-01/s1-t9-backoff.md) (Backoff)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
