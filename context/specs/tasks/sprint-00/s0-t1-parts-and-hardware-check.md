# s0-t1: Parts and hardware check

| Field | Value |
|-------|-------|
| Task ID | `s0-t1-parts-and-hardware-check` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Parts check: ESP32-DevKitC (WROOM-32E, 4 MB), BME280 breakout (note its address strap and whether it has pull-ups), SSD1306 128x64 I2C OLED, push button, LED + 330 ohm resistor, breadboard, jumpers, 4.7 k resistors, USB data cable, logic analyser (needed for the Sprint 7 jitter measurement). Order anything missing now.

## Acceptance criteria

- [ ] Every part is in hand or on order.
- [ ] Pull-up presence on the breakouts is noted.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-1 | ESP32-DevKitC (WROOM-32E, 4 MB flash), USB 5 V power |
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |
| HW-3 | SSD1306 128x64 OLED on I2C, address 0x3C, sharing the bus with the sensor |
| HW-4 | Push button on GPIO4, internal pull-up, falling-edge interrupt |
| HW-5 | Status LED on GPIO2 (or onboard) with 330 ohm resistor |
| HW-6 | Wiring: SDA GPIO21, SCL GPIO22, 3.3 V/GND, 4.7 k pull-ups if the breakouts lack them, breadboard |

## Dependencies

**Depends on:** none

**Blocks:** 
- [`s0-t11-flash-scaffold`](s0-t11-flash-scaffold.md) (Flash scaffold)
- [`s2-t1-wire-circuit`](../sprint-02/s2-t1-wire-circuit.md) (Wire circuit)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
