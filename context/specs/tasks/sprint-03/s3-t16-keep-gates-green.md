# s3-t16: Keep gates green

| Field | Value |
|-------|-------|
| Task ID | `s3-t16-keep-gates-green` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Keep `make docker-test` and `idf.py build` green, with no new warnings.

## Acceptance criteria

- [ ] Both pass.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |
| BLD-3 | Firmware build with ESP-IDF v5.x, natively or in the `espressif/idf` container |

## Dependencies

**Depends on:** 
- [`s3-t14-sample-logging`](s3-t14-sample-logging.md) (Sample logging)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
