# s4-t1: Button ISR

| Field | Value |
|-------|-------|
| Task ID | `s4-t1-button-isr` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Button ISR: place it in IRAM, call `xSemaphoreGiveFromISR(button_sem)` and request a yield if a higher-priority task woke. No logging or blocking calls inside it.

## Acceptance criteria

- [ ] A press wakes `display_task`.
- [ ] No `FromISR` calls exist outside the ISR.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-5 | Push button toggles C/F, via ISR and semaphore |
| ISR-1 | Button ISR is not a task; it calls `xSemaphoreGiveFromISR(button_sem)` |
| RUL-3 | Use `FromISR` APIs only inside the ISR |
| OBJ-6 | `button_sem` binary semaphore, ISR to `display_task`, debounced |

## Dependencies

**Depends on:** 
- [`s3-t2-create-shared-objects`](../sprint-03/s3-t2-create-shared-objects.md) (Create shared objects)
- [`s2-t14-button-bounce-measure`](../sprint-02/s2-t14-button-bounce-measure.md) (Button bounce measure)

**Blocks:** 
- [`s4-t2-debounce`](s4-t2-debounce.md) (Debounce)
- [`s4-t3-display-task-loop`](s4-t3-display-task-loop.md) (Display task loop)

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
