# s1-t14: Heap policy test

| Field | Value |
|-------|-------|
| Task ID | `s1-t14-heap-policy-test` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`test/host/test_heap_policy.c`: above threshold, below threshold, falling then recovering, falling for N checks.

## Acceptance criteria

- [ ] Assertions pass.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-6 | Low heap (for example below 20 KB): log a warning, restart if it keeps falling |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s1-t13-heap-policy`](s1-t13-heap-policy.md) (Heap policy)

**Blocks:** 
- [`s1-t18-full-suite-run`](s1-t18-full-suite-run.md) (Full suite run)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
