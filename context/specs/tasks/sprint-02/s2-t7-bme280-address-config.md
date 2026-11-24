# s2-t7: BME280 address config

| Field | Value |
|-------|-------|
| Task ID | `s2-t7-bme280-address-config` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

BME280 address selectable between 0x76 and 0x77 from Kconfig.

## Acceptance criteria

- [ ] Both addresses work when the strap is changed.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |

## Dependencies

**Depends on:** 
- [`s2-t6-bme280-measure`](s2-t6-bme280-measure.md) (BME280 measure)
- [`s0-t10-kconfig-menu`](../sprint-00/s0-t10-kconfig-menu.md) (Kconfig menu)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
