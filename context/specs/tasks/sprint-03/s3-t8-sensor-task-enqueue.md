# s3-t8: Sensor task enqueue

| Field | Value |
|-------|-------|
| Task ID | `s3-t8-sensor-task-enqueue` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`sensor_task` builds a `sample_t` with a timestamp and sends it to `raw_queue`. If the queue is full, report it and drop.

## Acceptance criteria

- [ ] Samples reach the queue every 5 s.

## Requirements covered

| ID | Requirement |
|----|-------------|
| OBJ-1 | `raw_queue`: 8 x `sample_t`, `sensor_task` to `process_task` |
| FR-1 | Sample temperature and humidity every 5 s |

## Dependencies

**Depends on:** 
- [`s3-t6-sensor-task-i2c-mutex`](s3-t6-sensor-task-i2c-mutex.md) (Sensor task I2C mutex)

**Blocks:** 
- [`s3-t9-process-task-validate`](s3-t9-process-task-validate.md) (Process task validate)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
