# s0-t9: `app_config.h`

| Field | Value |
|-------|-------|
| Task ID | `s0-t9-app-config-header` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Create `main/app_config.h`: pins (GPIO21, 22, 4, 2), I2C addresses, sample/display/publish periods, task priorities and stack sizes in bytes, queue depths, mutex timeout, backoff limits, watchdog and heap thresholds.

## Acceptance criteria

- [ ] Values match the overview tables.
- [ ] No magic numbers are planned outside this file.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-4 | Push button on GPIO4, internal pull-up, falling-edge interrupt |
| HW-5 | Status LED on GPIO2 (or onboard) with 330 ohm resistor |
| HW-6 | Wiring: SDA GPIO21, SCL GPIO22, 3.3 V/GND, 4.7 k pull-ups if the breakouts lack them, breadboard |
| TSK-1 | `monitor_task`: priority 6, 3 KB, blocks on `error_queue` plus 10 s housekeeping |
| TSK-2 | `sensor_task`: priority 5, 4 KB, every 5 s with `vTaskDelayUntil` |
| TSK-3 | `process_task`: priority 4, 3 KB, blocks on `raw_queue` |
| TSK-4 | `display_task`: priority 3, 3 KB, takes `button_sem` with 1 s timeout |
| TSK-5 | `comms_task`: priority 3, 6 KB, waits on `WIFI_CONNECTED_BIT` |
| OBJ-1 | `raw_queue`: 8 x `sample_t`, `sensor_task` to `process_task` |
| OBJ-2 | `publish_queue`: 10 x `reading_t`, `process_task` to `comms_task`, drop oldest when full |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |

## Dependencies

**Depends on:** 
- [`s0-t6-scaffold-project`](s0-t6-scaffold-project.md) (Scaffold project)

**Blocks:** 
- [`s2-t3-i2c-bus-driver`](../sprint-02/s2-t3-i2c-bus-driver.md) (I2C bus driver)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
