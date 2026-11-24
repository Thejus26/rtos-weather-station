# s3-t14: Sample logging

| Field | Value |
|-------|-------|
| Task ID | `s3-t14-sample-logging` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Log each processed sample (raw, filtered, dew point) on serial.

## Acceptance criteria

- [ ] The serial log shows a line every 5 s.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-1 | Sample temperature and humidity every 5 s |

## Dependencies

**Depends on:** 
- [`s3-t10-process-task-filter`](s3-t10-process-task-filter.md) (Process task filter)

**Blocks:** 
- [`s3-t15-hw-cadence-check`](s3-t15-hw-cadence-check.md) (Hardware cadence check)
- [`s3-t16-keep-gates-green`](s3-t16-keep-gates-green.md) (Keep gates green)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
