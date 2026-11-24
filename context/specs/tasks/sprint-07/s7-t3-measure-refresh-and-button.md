# s7-t3: Measure refresh and button

| Field | Value |
|-------|-------|
| Task ID | `s7-t3-measure-refresh-and-button` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Display refresh period and button response over at least 20 presses, with Wi-Fi and MQTT active.

## Acceptance criteria

- [ ] Refresh is 1 s.
- [ ] Response is at or under 200 ms.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-3 | Display refresh 1 s |
| TIM-4 | Button response within 200 ms |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
