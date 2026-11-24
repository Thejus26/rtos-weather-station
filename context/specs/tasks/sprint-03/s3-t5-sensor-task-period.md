# s3-t5: Sensor task period

| Field | Value |
|-------|-------|
| Task ID | `s3-t5-sensor-task-period` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`sensor_task` skeleton: 5 s period with `vTaskDelayUntil`, logging the measured period with `esp_timer`.

## Acceptance criteria

- [ ] The log shows 5000 ms periods.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-1 | Sample temperature and humidity every 5 s |
| TSK-2 | `sensor_task`: priority 5, 4 KB, every 5 s with `vTaskDelayUntil` |
| TIM-1 | Sampling period 5 s, jitter under +/-50 ms |
| GOAL-3 | Meet defined timing with `vTaskDelayUntil` and measure it |

## Dependencies

**Depends on:** 
- [`s3-t4-create-tasks`](s3-t4-create-tasks.md) (Create tasks)

**Blocks:** 
- [`s3-t6-sensor-task-i2c-mutex`](s3-t6-sensor-task-i2c-mutex.md) (Sensor task I2C mutex)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
