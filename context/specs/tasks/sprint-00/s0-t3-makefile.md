# s0-t3: Makefile

| Field | Value |
|-------|-------|
| Task ID | `s0-t3-makefile` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Create `Makefile` with `test`, `docker-test`, `clean`, from the reference in `code-build.md` section 4. Recipe lines use tabs. Host binaries go to `build-host/`.

## Acceptance criteria

- [ ] `make` parses.
- [ ] Targets match the reference.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s0-t2-test-image`](s0-t2-test-image.md) (Test image)

**Blocks:** 
- [`s0-t4-harness-smoke-test`](s0-t4-harness-smoke-test.md) (Harness smoke test)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
