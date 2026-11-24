# s2-t8: Sensor interface

| Field | Value |
|-------|-------|
| Task ID | `s2-t8-sensor-interface` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`main/drivers/sensor.h`: a one-function `sensor_read()` interface that hides the BME280, so SHT31 or DHT22 can replace it later.

## Acceptance criteria

- [ ] Tasks call only `sensor_read()`.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-7 | Alternate sensors (SHT31) can replace the BME280 |

## Dependencies

**Depends on:** 
- [`s2-t6-bme280-measure`](s2-t6-bme280-measure.md) (BME280 measure)

**Blocks:** 
- [`s3-t6-sensor-task-i2c-mutex`](../sprint-03/s3-t6-sensor-task-i2c-mutex.md) (Sensor task I2C mutex)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
