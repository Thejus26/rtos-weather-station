# s1-t5: Validate test

| Field | Value |
|-------|-------|
| Task ID | `s1-t5-validate-test` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`test/host/test_validate.c`: limits accepted (-40, 85, 0, 100), just outside rejected, a jump of exactly 10 accepted and more than 10 rejected, first sample, NaN.

## Acceptance criteria

- [ ] Every rejection branch is hit at least once.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-2 | Out-of-range value (temp -40 to 85, humidity 0 to 100, jump over 10 C): discard and count as a fault |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s1-t4-validate`](s1-t4-validate.md) (Validate)

**Blocks:** 
- [`s1-t18-full-suite-run`](s1-t18-full-suite-run.md) (Full suite run)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
