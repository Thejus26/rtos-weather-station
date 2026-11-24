# s6-t7: Task watchdog

| Field | Value |
|-------|-------|
| Task ID | `s6-t7-task-watchdog` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Task watchdog: subscribe `sensor_task`, `process_task` and `monitor_task`, and have each feed its own entry in its loop. On a timeout, log which task hung and restart.

## Acceptance criteria

- [ ] A stalled task causes a logged restart after 10 s.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-9 | Task watchdog and heap monitor; status LED shows system state |
| TIM-9 | Task watchdog 10 s on `sensor_task`, `process_task` and `monitor_task` |
| ERR-5 | Task hang: task watchdog logs the cause and restarts |
| GOAL-4 | Handle sensor, network and resource faults without hanging |

## Dependencies

**Depends on:** 
- [`s6-t1-monitor-task-full`](s6-t1-monitor-task-full.md) (Monitor task full)
- [`s0-t8-sdkconfig-defaults`](../sprint-00/s0-t8-sdkconfig-defaults.md) (`sdkconfig.defaults`)

**Blocks:** 
- [`s6-t9-reset-reason-logging`](s6-t9-reset-reason-logging.md) (Reset reason logging)
- [`s6-t11-fault-injection-hooks`](s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

## Open questions

- the watchdog covers three of the five tasks (`sensor_task`, `process_task`, `monitor_task`). The roadmap does not say whether `display_task` and `comms_task` are deliberately excluded.

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
