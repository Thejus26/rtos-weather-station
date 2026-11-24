# s0-t4: Harness smoke test

| Field | Value |
|-------|-------|
| Task ID | `s0-t4-harness-smoke-test` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Add a temporary `test/host/test_smoke.c`. Prove a passing test exits 0 and a deliberately failing `assert` stops `make` with a non-zero exit, under `--memory 256m --cpus 1`.

## Acceptance criteria

- [ ] Both outcomes (pass and fail) are observed.
- [ ] Resource caps (256 MB, 1 CPU) are respected.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-1 | Lightweight host test image (Alpine + GCC, about 280 MB) running within 256 MB and 1 CPU |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s0-t3-makefile`](s0-t3-makefile.md) (Makefile)

**Blocks:** 
- [`s0-t13-load-sprint-1`](s0-t13-load-sprint-1.md) (Load Sprint 1)
- [`s1-t1-decide-average-and-dewpoint`](../sprint-01/s1-t1-decide-average-and-dewpoint.md) (Decide average and dew point)
- [`s1-t8-unit-convert`](../sprint-01/s1-t8-unit-convert.md) (Unit convert)
- [`s1-t9-backoff`](../sprint-01/s1-t9-backoff.md) (Backoff)
- [`s1-t11-fault-policy`](../sprint-01/s1-t11-fault-policy.md) (Fault policy)
- [`s1-t13-heap-policy`](../sprint-01/s1-t13-heap-policy.md) (Heap policy)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
