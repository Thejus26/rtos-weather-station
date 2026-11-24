# s3-t4: Create tasks

| Field | Value |
|-------|-------|
| Task ID | `s3-t4-create-tasks` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Create the five tasks with the overview's priorities and stack sizes (6, 5, 4, 3, 3 and 3, 4, 3, 3, 6 KB), initially as logging stubs.

## Acceptance criteria

- [ ] All five tasks appear in the runtime task list with the right priorities.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TSK-1 | `monitor_task`: priority 6, 3 KB, blocks on `error_queue` plus 10 s housekeeping |
| TSK-2 | `sensor_task`: priority 5, 4 KB, every 5 s with `vTaskDelayUntil` |
| TSK-3 | `process_task`: priority 4, 3 KB, blocks on `raw_queue` |
| TSK-4 | `display_task`: priority 3, 3 KB, takes `button_sem` with 1 s timeout |
| TSK-5 | `comms_task`: priority 3, 6 KB, waits on `WIFI_CONNECTED_BIT` |
| GOAL-1 | Multi-task FreeRTOS application with clean task boundaries |

## Dependencies

**Depends on:** 
- [`s3-t2-create-shared-objects`](s3-t2-create-shared-objects.md) (Create shared objects)

**Blocks:** 
- [`s3-t5-sensor-task-period`](s3-t5-sensor-task-period.md) (Sensor task period)
- [`s3-t12-monitor-task-stub`](s3-t12-monitor-task-stub.md) (Monitor task stub)
- [`s4-t3-display-task-loop`](../sprint-04/s4-t3-display-task-loop.md) (Display task loop)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
