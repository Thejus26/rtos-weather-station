# s4-t6: Render values

| Field | Value |
|-------|-------|
| Task ID | `s4-t6-render-values` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Draw temperature, humidity, dew point and unit, with a "no data yet" state before the first sample and a visible sensor-fault indicator driven by `SENSOR_OK_BIT`.

## Acceptance criteria

- [ ] Unplugging the sensor shows the indicator.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |

## Dependencies

**Depends on:** 
- [`s4-t4-display-task-draw-locking`](s4-t4-display-task-draw-locking.md) (Display task draw locking)

**Blocks:** 
- [`s4-t9-measure-display-latency`](s4-t9-measure-display-latency.md) (Measure display latency)

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
