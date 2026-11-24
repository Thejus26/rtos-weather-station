# s2-t5: BME280 init

| Field | Value |
|-------|-------|
| Task ID | `s2-t5-bme280-init` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`main/drivers/bme280.[ch]`: check chip ID, soft reset, read calibration data.

## Acceptance criteria

- [ ] Chip ID matches.
- [ ] Calibration values are non-zero.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |

## Dependencies

**Depends on:** 
- [`s2-t4-i2c-scan`](s2-t4-i2c-scan.md) (I2C scan)

**Blocks:** 
- [`s2-t6-bme280-measure`](s2-t6-bme280-measure.md) (BME280 measure)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
