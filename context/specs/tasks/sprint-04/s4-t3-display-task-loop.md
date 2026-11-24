# s4-t3: Display task loop

| Field | Value |
|-------|-------|
| Task ID | `s4-t3-display-task-loop` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`display_task` waits on `button_sem` with a 1 s timeout and refreshes on timeout or on a press.

## Acceptance criteria

- [ ] The display refreshes each second.
- [ ] It refreshes immediately on a press.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on the 128x64 OLED, refreshed every 1 s |
| TSK-4 | `display_task`: priority 3, 3 KB, takes `button_sem` with 1 s timeout |
| TIM-3 | Display refresh 1 s |
| OBJ-6 | `button_sem` binary semaphore, ISR to `display_task`, debounced |

## Dependencies

**Depends on:** 
- [`s3-t4-create-tasks`](../sprint-03/s3-t4-create-tasks.md) (Create tasks)
- [`s4-t1-button-isr`](s4-t1-button-isr.md) (Button ISR)

**Blocks:** 
- [`s4-t4-display-task-draw-locking`](s4-t4-display-task-draw-locking.md) (Display task draw locking)

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
