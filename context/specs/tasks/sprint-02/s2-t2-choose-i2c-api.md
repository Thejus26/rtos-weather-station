# s2-t2: Choose I2C API

| Field | Value |
|-------|-------|
| Task ID | `s2-t2-choose-i2c-api` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-4: choose the I2C driver API after reading the installed ESP-IDF version's documentation.

## Acceptance criteria

- [ ] The choice is recorded with the version it was checked against.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-6 | Wiring: SDA GPIO21, SCL GPIO22, 3.3 V/GND, 4.7 k pull-ups if the breakouts lack them, breadboard |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-4** (settled in this task): I2C driver API
  - Recommended default: The ESP-IDF v5.x `i2c_master` driver, if the installed version documents it as current; confirm against its docs
  - Why it matters: The legacy driver is deprecated in v5.x

## Dependencies

**Depends on:** 
- [`s0-t6-scaffold-project`](../sprint-00/s0-t6-scaffold-project.md) (Scaffold project)

**Blocks:** 
- [`s2-t3-i2c-bus-driver`](s2-t3-i2c-bus-driver.md) (I2C bus driver)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
