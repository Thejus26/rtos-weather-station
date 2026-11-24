# s2-t10: SSD1306 init

| Field | Value |
|-------|-------|
| Task ID | `s2-t10-ssd1306-init` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`main/drivers/ssd1306.[ch]`: init sequence for 128x64, static 1 KB framebuffer, clear and flush.

## Acceptance criteria

- [ ] The screen clears.
- [ ] A test pattern displays.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-3 | SSD1306 128x64 OLED on I2C, address 0x3C, sharing the bus with the sensor |
| NFR-1 | No dynamic allocation in steady state |

## Dependencies

**Depends on:** 
- [`s2-t4-i2c-scan`](s2-t4-i2c-scan.md) (I2C scan)

**Blocks:** 
- [`s2-t11-ssd1306-text`](s2-t11-ssd1306-text.md) (SSD1306 text)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
