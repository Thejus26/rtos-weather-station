# s3-t9: Process task validate

| Field | Value |
|-------|-------|
| Task ID | `s3-t9-process-task-validate` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`process_task` waits on `raw_queue` with a timeout under 10 s (D-9), validates each sample, and reports rejects to `error_queue`.

## Acceptance criteria

- [ ] A forced bad value is discarded and reported.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TSK-3 | `process_task`: priority 4, 3 KB, blocks on `raw_queue` |
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| ERR-2 | Out-of-range value (temp -40 to 85, humidity 0 to 100, jump over 10 C): discard and count as a fault |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-9** (referenced here): Watchdog interaction with blocking waits
  - Recommended default: `process_task` and `monitor_task` wait with a timeout well under 10 s (for example 2 s) and each subscribed task feeds its own watchdog entry
  - Why it matters: `process_task` blocks on `raw_queue` and `monitor_task` has a 10 s housekeeping period, which would equal the 10 s watchdog timeout and cause false resets when the sensor fails

## Dependencies

**Depends on:** 
- [`s3-t8-sensor-task-enqueue`](s3-t8-sensor-task-enqueue.md) (Sensor task enqueue)
- [`s1-t4-validate`](../sprint-01/s1-t4-validate.md) (Validate)

**Blocks:** 
- [`s3-t10-process-task-filter`](s3-t10-process-task-filter.md) (Process task filter)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
