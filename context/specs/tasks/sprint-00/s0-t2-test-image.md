# s0-t2: Test image

| Field | Value |
|-------|-------|
| Task ID | `s0-t2-test-image` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Install Docker. Create `Dockerfile.test` (`alpine:3.20`, `build-base`, `make`, `WORKDIR /work`) and `.dockerignore`.

## Acceptance criteria

- [ ] `docker build -f Dockerfile.test -t rtos-host-test .` succeeds.
- [ ] Image size is about 230 MB.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-1 | Lightweight host test image (Alpine + GCC, about 230 MB) running within 256 MB and 1 CPU |

## Dependencies

**Depends on:** none

**Blocks:** 
- [`s0-t3-makefile`](s0-t3-makefile.md) (Makefile)

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
