# s2-t15: Bring-up loop

| Field | Value |
|-------|-------|
| Task ID | `s2-t15-bringup-loop` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Throwaway bring-up loop in `main.c`: read the sensor, print to serial, draw on the OLED, blink the LED, count presses. Remove it (or keep it behind a Kconfig flag) before Sprint 3.

## Acceptance criteria

- [ ] All four parts work together on one bus.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |
| HW-3 | SSD1306 128x64 OLED on I2C, address 0x3C, sharing the bus with the sensor |
| HW-4 | Push button on GPIO4, internal pull-up, falling-edge interrupt |
| HW-5 | Status LED on GPIO2 (or onboard) with 330 ohm resistor |

## Dependencies

**Depends on:** 
- [`s2-t6-bme280-measure`](s2-t6-bme280-measure.md) (BME280 measure)
- [`s2-t12-oled-layout`](s2-t12-oled-layout.md) (OLED layout)
- [`s2-t13-status-led-driver`](s2-t13-status-led-driver.md) (Status LED driver)
- [`s2-t14-button-bounce-measure`](s2-t14-button-bounce-measure.md) (Button bounce measure)

**Blocks:** 
- [`s3-t1-event-bits-and-handles`](../sprint-03/s3-t1-event-bits-and-handles.md) (Event bits and handles)

## Open questions

- "remove it (or keep it behind a Kconfig flag)" leaves the choice open.

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
