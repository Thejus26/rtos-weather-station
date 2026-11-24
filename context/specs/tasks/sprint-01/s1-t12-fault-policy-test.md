# s1-t12: Fault policy test

| Field | Value |
|-------|-------|
| Task ID | `s1-t12-fault-policy-test` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`test/host/test_fault_policy.c`: 2 failures do nothing, 3 request re-init, success resets, 10 failed recoveries request restart.

## Acceptance criteria

- [ ] Assertions pass.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-8 | Sensor re-init after 3 consecutive failures; restart after 10 failed recoveries |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s1-t11-fault-policy`](s1-t11-fault-policy.md) (Fault policy)

**Blocks:** 
- [`s1-t18-full-suite-run`](s1-t18-full-suite-run.md) (Full suite run)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
