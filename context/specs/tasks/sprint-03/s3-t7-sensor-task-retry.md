# s3-t7: Sensor task retry

| Field | Value |
|-------|-------|
| Task ID | `s3-t7-sensor-task-retry` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`sensor_task` retries a failed read up to 3 times, then reports the failure, and sets or clears `SENSOR_OK_BIT`.

## Acceptance criteria

- [ ] Unplugging the sensor clears the bit after 3 attempts.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-1 | I2C read failure or timeout: retry up to 3 times, report, clear `SENSOR_OK`, re-init sensor |
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |

## Dependencies

**Depends on:** 
- [`s3-t6-sensor-task-i2c-mutex`](s3-t6-sensor-task-i2c-mutex.md) (Sensor task I2C mutex)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
