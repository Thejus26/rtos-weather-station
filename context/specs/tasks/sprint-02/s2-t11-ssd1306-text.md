# s2-t11: SSD1306 text

| Field | Value |
|-------|-------|
| Task ID | `s2-t11-ssd1306-text` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

SSD1306 text drawing from a static font table, with a draw-line API.

## Acceptance criteria

- [ ] Text is readable at the chosen font size.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-3 | SSD1306 128x64 OLED on I2C, address 0x3C, sharing the bus with the sensor |
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |

## Dependencies

**Depends on:** 
- [`s2-t10-ssd1306-init`](s2-t10-ssd1306-init.md) (SSD1306 init)

**Blocks:** 
- [`s2-t12-oled-layout`](s2-t12-oled-layout.md) (OLED layout)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
