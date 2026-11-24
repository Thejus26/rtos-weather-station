# s3-t6: Sensor task I2C mutex

| Field | Value |
|-------|-------|
| Task ID | `s3-t6-sensor-task-i2c-mutex` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`sensor_task` reads through `sensor_read()` while holding `i2c_mutex` (100 ms timeout), releasing it right after. A timeout is reported to `error_queue` with a zero timeout.

## Acceptance criteria

- [ ] The mutex is held only around the transaction.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |
| OBJ-4 | `i2c_mutex` with priority inheritance, shared by `sensor_task` and `display_task` |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |
| RUL-1 | Keep mutex hold times short (microseconds to a few milliseconds) |
| RUL-2 | Never hold two mutexes at once; if unavoidable take `i2c_mutex` before `data_mutex` |

## Dependencies

**Depends on:** 
- [`s3-t5-sensor-task-period`](s3-t5-sensor-task-period.md) (Sensor task period)
- [`s2-t8-sensor-interface`](../sprint-02/s2-t8-sensor-interface.md) (Sensor interface)

**Blocks:** 
- [`s3-t7-sensor-task-retry`](s3-t7-sensor-task-retry.md) (Sensor task retry)
- [`s3-t8-sensor-task-enqueue`](s3-t8-sensor-task-enqueue.md) (Sensor task enqueue)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
