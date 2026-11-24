# s2-t9: I2C error bounded

| Field | Value |
|-------|-------|
| Task ID | `s2-t9-i2c-error-bounded` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Unplug SDA or SCL during reads and confirm the driver returns an error within its timeout instead of hanging.

## Acceptance criteria

- [ ] An error is returned in bounded time.
- [ ] The bus recovers when reconnected.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-1 | I2C read failure or timeout: retry up to 3 times, report, clear `SENSOR_OK`, re-init sensor |

## Dependencies

**Depends on:** 
- [`s2-t6-bme280-measure`](s2-t6-bme280-measure.md) (BME280 measure)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
