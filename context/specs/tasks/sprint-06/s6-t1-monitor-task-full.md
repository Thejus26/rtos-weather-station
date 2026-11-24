# s6-t1: Monitor task full

| Field | Value |
|-------|-------|
| Task ID | `s6-t1-monitor-task-full` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Full `monitor_task`: wait on `error_queue` with a bounded timeout (D-9) and run 10 s housekeeping by tick comparison, not by a 10 s block.

## Acceptance criteria

- [ ] The monitor wakes well inside the watchdog window.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TSK-1 | `monitor_task`: priority 6, 3 KB, blocks on `error_queue` plus 10 s housekeeping |
| TIM-9 | Task watchdog 10 s on `sensor_task`, `process_task` and `monitor_task` |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-9** (referenced here): Watchdog interaction with blocking waits
  - Recommended default: `process_task` and `monitor_task` wait with a timeout well under 10 s (for example 2 s) and each subscribed task feeds its own watchdog entry
  - Why it matters: `process_task` blocks on `raw_queue` and `monitor_task` has a 10 s housekeeping period, which would equal the 10 s watchdog timeout and cause false resets when the sensor fails

## Dependencies

**Depends on:** 
- [`s3-t12-monitor-task-stub`](../sprint-03/s3-t12-monitor-task-stub.md) (Monitor task stub)

**Blocks:** 
- [`s6-t2-error-dispatch`](s6-t2-error-dispatch.md) (Error dispatch)
- [`s6-t7-task-watchdog`](s6-t7-task-watchdog.md) (Task watchdog)
- [`s6-t8-heap-monitor`](s6-t8-heap-monitor.md) (Heap monitor)

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
