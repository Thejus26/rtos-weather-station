# s7-t4: Measure publish interval

| Field | Value |
|-------|-------|
| Task ID | `s7-t4-measure-publish-interval` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

MQTT publish interval over at least 20 publishes.

## Acceptance criteria

- [ ] The interval is 30 s within +/-1 s.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-5 | MQTT publish every 30 s, tolerance +/-1 s when connected |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
