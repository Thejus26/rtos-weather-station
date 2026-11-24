# s1-t18: Full suite run

| Field | Value |
|-------|-------|
| Task ID | `s1-t18-full-suite-run` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Delete `test_smoke.c`. Run the whole suite from clean. Save the passing output to `docs/test-results/host-tests.txt`.

## Acceptance criteria

- [ ] `make test` exits 0 with no warnings.
- [ ] Output file is saved.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |
| DEL-3a | Test evidence: unit tests for moving average, validation and dew point |
| ACC-5 | `make docker-test` passes in the lightweight container with no warnings |

## Dependencies

**Depends on:** 
- [`s1-t3-moving-average-test`](s1-t3-moving-average-test.md) (Moving average test)
- [`s1-t5-validate-test`](s1-t5-validate-test.md) (Validate test)
- [`s1-t7-dew-point-test`](s1-t7-dew-point-test.md) (Dew point test)
- [`s1-t10-backoff-test`](s1-t10-backoff-test.md) (Backoff test)
- [`s1-t12-fault-policy-test`](s1-t12-fault-policy-test.md) (Fault policy test)
- [`s1-t14-heap-policy-test`](s1-t14-heap-policy-test.md) (Heap policy test)
- [`s1-t16-reading-json-test`](s1-t16-reading-json-test.md) (Reading JSON test)

**Blocks:** 
- [`s1-t19-sync-layout-docs`](s1-t19-sync-layout-docs.md) (Sync layout docs)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
