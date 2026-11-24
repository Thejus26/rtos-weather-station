# s5-t12: Network outage test

| Field | Value |
|-------|-------|
| Task ID | `s5-t12-network-outage-test` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Turn Wi-Fi off, then take the broker down. Confirm sampling and display continue in both cases, and publishing resumes afterward.

## Acceptance criteria

- [ ] The OLED and serial keep updating through both outages.
- [ ] Publishing resumes afterward.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| ERR-3 | Wi-Fi/MQTT loss: keep sampling and displaying, buffer, reconnect with backoff |

## Dependencies

**Depends on:** 
- [`s5-t10-outage-buffering`](s5-t10-outage-buffering.md) (Outage buffering)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
