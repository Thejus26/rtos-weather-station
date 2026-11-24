# s5-t13: Credential hygiene

| Field | Value |
|-------|-------|
| Task ID | `s5-t13-credential-hygiene` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Confirm `sdkconfig` is ignored, search source and logs for the password, and confirm nothing sensitive was printed.

## Acceptance criteria

- [ ] The search finds no credentials in tracked files or logs.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-10 | Configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code |
| DEL-1 | Source code in the specified layout, commented, no hard-coded credentials |

## Dependencies

**Depends on:** 
- [`s5-t9-comms-task`](s5-t9-comms-task.md) (Comms task)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
