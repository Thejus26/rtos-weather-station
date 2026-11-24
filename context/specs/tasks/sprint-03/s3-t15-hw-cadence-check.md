# s3-t15: Hardware cadence check

| Field | Value |
|-------|-------|
| Task ID | `s3-t15-hw-cadence-check` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Run for 10 minutes. Check that the cadence holds and `raw_queue` never fills. Record preliminary jitter from the `esp_timer` log.

## Acceptance criteria

- [ ] Preliminary jitter is within +/-50 ms.
- [ ] `raw_queue` never fills.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-1 | Sampling period 5 s, jitter under +/-50 ms |
| GOAL-3 | Meet defined timing with `vTaskDelayUntil` and measure it |

## Dependencies

**Depends on:** 
- [`s3-t14-sample-logging`](s3-t14-sample-logging.md) (Sample logging)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
