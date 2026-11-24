# s6-t2: Error dispatch

| Field | Value |
|-------|-------|
| Task ID | `s6-t2-error-dispatch` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Error dispatch: per-source and per-code counters and a log line at the right severity for each event.

## Acceptance criteria

- [ ] Counters appear in the housekeeping log.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-9 | Task watchdog and heap monitor; status LED shows system state |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |

## Dependencies

**Depends on:** 
- [`s6-t1-monitor-task-full`](s6-t1-monitor-task-full.md) (Monitor task full)

**Blocks:** 
- [`s6-t3-sensor-recovery`](s6-t3-sensor-recovery.md) (Sensor recovery)
- [`s6-t6-status-led-states`](s6-t6-status-led-states.md) (Status LED states)
- [`s6-t10-drop-counters`](s6-t10-drop-counters.md) (Drop counters)

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
