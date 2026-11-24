# s2-t4: I2C scan

| Field | Value |
|-------|-------|
| Task ID | `s2-t4-i2c-scan` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Temporary I2C scan routine.

## Acceptance criteria

- [ ] Scan reports 0x76 (or 0x77) and 0x3C.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |
| HW-3 | SSD1306 128x64 OLED on I2C, address 0x3C, sharing the bus with the sensor |
| HW-6 | Wiring: SDA GPIO21, SCL GPIO22, 3.3 V/GND, 4.7 k pull-ups if the breakouts lack them, breadboard |

## Dependencies

**Depends on:** 
- [`s2-t1-wire-circuit`](s2-t1-wire-circuit.md) (Wire circuit)
- [`s2-t3-i2c-bus-driver`](s2-t3-i2c-bus-driver.md) (I2C bus driver)

**Blocks:** 
- [`s2-t5-bme280-init`](s2-t5-bme280-init.md) (BME280 init)
- [`s2-t10-ssd1306-init`](s2-t10-ssd1306-init.md) (SSD1306 init)

## Open questions

- the roadmap gives no "done when" beyond the scan result, and the scan routine is temporary. It does not say whether the routine should be deleted or kept after s2-t15.

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
