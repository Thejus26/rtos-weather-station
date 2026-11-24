# s1-t3: Moving average test

| Field | Value |
|-------|-------|
| Task ID | `s1-t3-moving-average-test` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`test/host/test_moving_average.c`: first sample, partial window, full window, rollover, constant input, step input.

## Acceptance criteria

- [ ] All assertions pass in the container.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s1-t2-moving-average`](s1-t2-moving-average.md) (Moving average)

**Blocks:** 
- [`s1-t18-full-suite-run`](s1-t18-full-suite-run.md) (Full suite run)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
