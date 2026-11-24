# s4-t10: I2C contention test

| Field | Value |
|-------|-------|
| Task ID | `s4-t10-i2c-contention-test` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Run both bus users for 30 minutes with no unexpected mutex timeouts. Then hold `i2c_mutex` for 150 ms on purpose and confirm the timeout is reported.

## Acceptance criteria

- [ ] No spurious timeouts in the 30-minute run.
- [ ] The forced timeout is logged.

## Requirements covered

| ID | Requirement |
|----|-------------|
| RUL-1 | Keep mutex hold times short (microseconds to a few milliseconds) |
| TIM-6 | I2C mutex wait timeout 100 ms; a timeout is reported as an error |
| OBJ-4 | `i2c_mutex` with priority inheritance, shared by `sensor_task` and `display_task` |

## Dependencies

**Depends on:** 
- [`s4-t4-display-task-draw-locking`](s4-t4-display-task-draw-locking.md) (Display task draw locking)

**Blocks:** none in the roadmap

## Open questions

- to hold `i2c_mutex` for 150 ms on purpose, a test hook is needed. The roadmap only adds fault-injection hooks in s6-t11, so it does not say how this is done here (for example a temporary local change).

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
