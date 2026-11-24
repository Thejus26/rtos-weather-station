# s4-t9: Measure display latency

| Field | Value |
|-------|-------|
| Task ID | `s4-t9-measure-display-latency` |
| Sprint | [Sprint 4: Display and Button](../../sprint-04-display-button.md) |
| Branch | `feature/display-button` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | Yes (needs the board and parts) |
| Status | Not started |

## Description

Measure sample-to-display latency using the sample timestamp and the draw-complete time.

## Acceptance criteria

- [ ] Latency is under 1.5 s.
- [ ] Numbers are recorded.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-2 | Sample-to-display latency under 1.5 s |

## Dependencies

**Depends on:** 
- [`s4-t6-render-values`](s4-t6-render-values.md) (Render values)

**Blocks:** none in the roadmap

## Open questions

- the roadmap gives no measurement method (logic analyser, serial timestamps) beyond the sample timestamp and draw-complete time in s4-t9.

## Source

Derived from [`sprint-04-display-button.md`](../../sprint-04-display-button.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
