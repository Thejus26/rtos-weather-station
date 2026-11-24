# s4-t2: Debounce

| Field | Value |
|-------|-------|
| Task ID | `s4-t2-debounce` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-10. Debounce using the bounce window measured in s2-t14-button-bounce-measure, so one press gives one semaphore.

## Acceptance criteria

- [ ] 20 presses produce exactly 20 toggles.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-5 | Push button toggles C/F, via ISR and semaphore |
| HW-4 | Push button on GPIO4, internal pull-up, falling-edge interrupt |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-10** (settled in this task): Button debounce method
  - Recommended default: Ignore edges within a window set from the bounce measured in s2-t14-button-bounce-measure, applied in the ISR
  - Why it matters: Must give one press = one semaphore give and stay inside the 200 ms response budget

## Dependencies

**Depends on:** 
- [`s4-t1-button-isr`](s4-t1-button-isr.md) (Button ISR)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
