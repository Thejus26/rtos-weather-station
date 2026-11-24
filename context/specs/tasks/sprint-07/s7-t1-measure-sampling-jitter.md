# s7-t1: Measure sampling jitter

| Field | Value |
|-------|-------|
| Task ID | `s7-t1-measure-sampling-jitter` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Sampling jitter: toggle a spare GPIO at each `sensor_task` wake-up and capture at least 100 intervals on the logic analyser. Cross-check with the `esp_timer` log.

## Acceptance criteria

- [ ] Maximum deviation is under +/-50 ms.
- [ ] The capture is saved.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-1 | Sampling period 5 s, jitter under +/-50 ms |
| DEL-3d | Test evidence: timing measurements against the requirements table |
| GOAL-3 | Meet defined timing with `vTaskDelayUntil` and measure it |

## Dependencies

**Depends on:** 
- [`s6-t12-keep-gates-green`](../sprint-06/s6-t12-keep-gates-green.md) (Keep gates green)

**Blocks:** 
- [`s7-t13-soak-24h`](s7-t13-soak-24h.md) (Soak 24 h)

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
