# s0-t8: `sdkconfig.defaults`

| Field | Value |
|-------|-------|
| Task ID | `s0-t8-sdkconfig-defaults` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Create `sdkconfig.defaults`: FreeRTOS tick 1000 Hz, task watchdog enabled with a 10 s timeout and restart on timeout. No credentials.

## Acceptance criteria

- [ ] After `fullclean` and a rebuild, the generated `sdkconfig` shows those values.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-10 | FreeRTOS tick 1000 Hz |
| TIM-9 | Task watchdog 10 s on `sensor_task`, `process_task` and `monitor_task` |
| FR-9 | Task watchdog and heap monitor; status LED shows system state |

## Dependencies

**Depends on:** 
- [`s0-t6-scaffold-project`](s0-t6-scaffold-project.md) (Scaffold project)

**Blocks:** 
- [`s6-t7-task-watchdog`](../sprint-06/s6-t7-task-watchdog.md) (Task watchdog)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
