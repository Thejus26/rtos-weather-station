# s2-t12: OLED layout

| Field | Value |
|-------|-------|
| Task ID | `s2-t12-oled-layout` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-5. Draw a static layout with temperature, humidity, dew point, unit and a status line.

## Acceptance criteria

- [ ] The layout fits the screen with no clipping.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-5** (settled in this task): OLED layout and font
  - Recommended default: Four text lines (temperature, humidity, dew point, status) plus unit marker, small fixed font
  - Why it matters: FR-4 lists the fields but not the layout

## Dependencies

**Depends on:** 
- [`s2-t11-ssd1306-text`](s2-t11-ssd1306-text.md) (SSD1306 text)

**Blocks:** 
- [`s2-t15-bringup-loop`](s2-t15-bringup-loop.md) (Bring-up loop)
- [`s4-t4-display-task-draw-locking`](../sprint-04/s4-t4-display-task-draw-locking.md) (Display task draw locking)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
