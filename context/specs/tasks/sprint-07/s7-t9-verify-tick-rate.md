# s7-t9: Verify tick rate

| Field | Value |
|-------|-------|
| Task ID | `s7-t9-verify-tick-rate` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Confirm the tick rate at run time (1 ms per tick) and in the generated config.

## Acceptance criteria

- [ ] The runtime value and `sdkconfig` agree on 1000 Hz.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-10 | FreeRTOS tick 1000 Hz |
| DEL-3d | Test evidence: timing measurements against the requirements table |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
