# s4-t8: Measure button response

| Field | Value |
|-------|-------|
| Task ID | `s4-t8-measure-button-response` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Measure button-to-OLED response over at least 20 presses, and the display refresh period.

## Acceptance criteria

- [ ] Response is at or under 200 ms.
- [ ] Refresh is at 1 s.
- [ ] Numbers are recorded.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-3 | Display refresh 1 s |
| TIM-4 | Button response within 200 ms |

## Dependencies

**Depends on:** 
- [`s4-t5-unit-toggle`](s4-t5-unit-toggle.md) (Unit toggle)

**Blocks:** none in the roadmap

## Open questions

- the roadmap gives no measurement method (logic analyser, serial timestamps) beyond the sample timestamp and draw-complete time in s4-t9.

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
