# s4-t4: Display task draw locking

| Field | Value |
|-------|-------|
| Task ID | `s4-t4-display-task-draw-locking` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`display_task` copies `latest` under `data_mutex` and releases it, then takes `i2c_mutex` (100 ms timeout) to draw. A timeout is reported.

## Acceptance criteria

- [ ] The two mutexes are never held together.

## Requirements covered

| ID | Requirement |
|----|-------------|
| RUL-2 | Never hold two mutexes at once; if unavoidable take `i2c_mutex` before `data_mutex` |
| OBJ-4 | `i2c_mutex` with priority inheritance, shared by `sensor_task` and `display_task` |
| OBJ-5 | `data_mutex` protecting the shared `latest` struct |
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |

## Dependencies

**Depends on:** 
- [`s3-t3-latest-struct`](../sprint-03/s3-t3-latest-struct.md) (Latest struct)
- [`s2-t12-oled-layout`](../sprint-02/s2-t12-oled-layout.md) (OLED layout)
- [`s4-t3-display-task-loop`](s4-t3-display-task-loop.md) (Display task loop)

**Blocks:** 
- [`s4-t5-unit-toggle`](s4-t5-unit-toggle.md) (Unit toggle)
- [`s4-t6-render-values`](s4-t6-render-values.md) (Render values)
- [`s4-t7-render-link-status`](s4-t7-render-link-status.md) (Render link status)
- [`s4-t10-i2c-contention-test`](s4-t10-i2c-contention-test.md) (I2C contention test)

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
