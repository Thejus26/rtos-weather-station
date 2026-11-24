# s9-t2: Sleep and current

| Field | Value |
|-------|-------|
| Task ID | `s9-t2-sleep-and-current` |
| Sprint | [Sprint 9: Backlog (Stretch Goals)](../../sprint-09-backlog.md) |
| Branch | none (backlog, not scheduled) |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Light or deep sleep between samples. Measure current with and without sleep, and optionally run from an 18650 and regulator.

## Acceptance criteria

- [ ] A measured current table exists.
- [ ] Any timing regressions are fixed.

## Requirements covered

| ID | Requirement |
|----|-------------|
| STR-2 | Stretch: deep or light sleep between samples, with current measurement (optional 18650 power) |

## Dependencies

**Depends on:** 
- [`s8-t10-tag-release`](../sprint-08/s8-t10-tag-release.md) (Tag release)

**Blocks:** none in the roadmap

## Open questions

- the current-measurement tool is not named, and nothing says what sleep period or timing regression threshold is acceptable (TIM-1 jitter is the nearest existing limit).

## Source

Derived from [`sprint-09-backlog.md`](../../sprint-09-backlog.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
