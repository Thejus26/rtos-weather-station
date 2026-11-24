# s5-t11: Measure publish cadence

| Field | Value |
|-------|-------|
| Task ID | `s5-t11-measure-publish-cadence` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Verify publish cadence on the subscriber side over at least 20 publishes.

## Acceptance criteria

- [ ] The interval is 30 s within +/-1 s.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-5 | MQTT publish every 30 s, tolerance +/-1 s when connected |

## Dependencies

**Depends on:** 
- [`s5-t9-comms-task`](s5-t9-comms-task.md) (Comms task)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
