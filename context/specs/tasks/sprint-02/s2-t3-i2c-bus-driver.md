# s2-t3: I2C bus driver

| Field | Value |
|-------|-------|
| Task ID | `s2-t3-i2c-bus-driver` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`main/drivers/i2c_bus.[ch]`: initialise the master bus on the configured pins, with finite transaction timeouts. No mutex inside the driver.

## Acceptance criteria

- [ ] The bus initialises.
- [ ] A transaction to an absent address fails within its timeout.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-6 | Wiring: SDA GPIO21, SCL GPIO22, 3.3 V/GND, 4.7 k pull-ups if the breakouts lack them, breadboard |
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |

## Dependencies

**Depends on:** 
- [`s2-t2-choose-i2c-api`](s2-t2-choose-i2c-api.md) (Choose I2C API)
- [`s0-t9-app-config-header`](../sprint-00/s0-t9-app-config-header.md) (`app_config.h`)

**Blocks:** 
- [`s2-t4-i2c-scan`](s2-t4-i2c-scan.md) (I2C scan)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
