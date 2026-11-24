# s2-t1: Wire circuit

| Field | Value |
|-------|-------|
| Task ID | `s2-t1-wire-circuit` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Wire the circuit: SDA to GPIO21, SCL to GPIO22 (BME280 and OLED on the same bus), button GPIO4 to GND, LED on GPIO2 with 330 ohm, 3.3 V and GND. Add 4.7 k pull-ups if the breakouts have none.

## Acceptance criteria

- [ ] Wiring matches the overview's table.
- [ ] It was checked by eye twice before power-up.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |
| HW-3 | SSD1306 128x64 OLED on I2C, address 0x3C, sharing the bus with the sensor |
| HW-4 | Push button on GPIO4, internal pull-up, falling-edge interrupt |
| HW-5 | Status LED on GPIO2 (or onboard) with 330 ohm resistor |
| HW-6 | Wiring: SDA GPIO21, SCL GPIO22, 3.3 V/GND, 4.7 k pull-ups if the breakouts lack them, breadboard |

## Dependencies

**Depends on:** 
- [`s0-t1-parts-and-hardware-check`](../sprint-00/s0-t1-parts-and-hardware-check.md) (Parts and hardware check)
- [`s0-t11-flash-scaffold`](../sprint-00/s0-t11-flash-scaffold.md) (Flash scaffold)

**Blocks:** 
- [`s2-t4-i2c-scan`](s2-t4-i2c-scan.md) (I2C scan)
- [`s2-t13-status-led-driver`](s2-t13-status-led-driver.md) (Status LED driver)
- [`s2-t14-button-bounce-measure`](s2-t14-button-bounce-measure.md) (Button bounce measure)
- [`s2-t16-wiring-doc`](s2-t16-wiring-doc.md) (Wiring doc)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
