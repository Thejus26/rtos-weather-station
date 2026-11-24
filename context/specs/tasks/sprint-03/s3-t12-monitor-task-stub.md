# s3-t12: Monitor task stub

| Field | Value |
|-------|-------|
| Task ID | `s3-t12-monitor-task-stub` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`monitor_task` stub: wait on `error_queue` with a bounded timeout and log each event. The full behaviour comes in Sprint 6.

## Acceptance criteria

- [ ] Every reported error appears in the log.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TSK-1 | `monitor_task`: priority 6, 3 KB, blocks on `error_queue` plus 10 s housekeeping |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |

## Dependencies

**Depends on:** 
- [`s3-t4-create-tasks`](s3-t4-create-tasks.md) (Create tasks)

**Blocks:** 
- [`s3-t13-stack-hwm-logging`](s3-t13-stack-hwm-logging.md) (Stack high-water-mark logging)
- [`s6-t1-monitor-task-full`](../sprint-06/s6-t1-monitor-task-full.md) (Monitor task full)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
