# s1-t7: Dew point test

| Field | Value |
|-------|-------|
| Task ID | `s1-t7-dew-point-test` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`test/host/test_dew_point.c`: 20 C and 50 %RH gives about 9.27 C (within 0.1); 100 %RH returns the air temperature; 0 %RH is defined; a negative-temperature case.

## Acceptance criteria

- [ ] Assertions pass.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-3 | Calculate dew point from the filtered values |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s1-t6-dew-point`](s1-t6-dew-point.md) (Dew point)

**Blocks:** 
- [`s1-t18-full-suite-run`](s1-t18-full-suite-run.md) (Full suite run)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
