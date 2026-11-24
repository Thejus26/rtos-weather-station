# s4-t7: Render link status

| Field | Value |
|-------|-------|
| Task ID | `s4-t7-render-link-status` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Draw Wi-Fi and MQTT status from `sys_events`. It shows "disconnected" until Sprint 5 sets the bits.

## Acceptance criteria

- [ ] Status text follows the event-group bits.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |

## Dependencies

**Depends on:** 
- [`s4-t4-display-task-draw-locking`](s4-t4-display-task-draw-locking.md) (Display task draw locking)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
