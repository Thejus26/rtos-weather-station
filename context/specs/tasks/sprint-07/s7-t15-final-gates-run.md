# s7-t15: Final gates run

| Field | Value |
|-------|-------|
| Task ID | `s7-t15-final-gates-run` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Re-run `make docker-test` and `idf.py build` on the final tree and save the output.

## Acceptance criteria

- [ ] Both pass with no warnings.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |
| BLD-3 | Firmware build with ESP-IDF v5.x, natively or in the `espressif/idf` container |
| ACC-5 | `make docker-test` passes in the lightweight container with no warnings |

## Dependencies

**Depends on:** 
- [`s7-t14-no-alloc-audit`](s7-t14-no-alloc-audit.md) (No-allocation audit)

**Blocks:** 
- [`s8-t2-task-comm-diagram`](../sprint-08/s8-t2-task-comm-diagram.md) (Task and communication diagram)
- [`s8-t4-collect-test-evidence`](../sprint-08/s8-t4-collect-test-evidence.md) (Collect test evidence)
- [`s8-t5-demo-media`](../sprint-08/s8-t5-demo-media.md) (Demo media)
- [`s8-t7-source-review`](../sprint-08/s8-t7-source-review.md) (Source review)

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
