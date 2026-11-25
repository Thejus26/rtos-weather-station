# s0-t7: Container firmware build (optional)

| Field | Value |
|-------|-------|
| Task ID | `s0-t7-container-firmware-build` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Optional: build the scaffold in the pinned `espressif/idf` container. Record image size and first-build time, and replace the "not pulled or measured" notes in the docs with the numbers.

Update: the image pull was done in s0-t5 and the first build in s0-t6, so this task is now documentation only. It copies the measured numbers into the README Notes. The roadmap row keeps its original wording (the roadmap wins on conflict).

## Acceptance criteria

- [ ] Container build produces `build/*.bin`.
- [ ] Image size and first-build time are recorded.

## Requirements covered

| ID | Requirement |
|----|-------------|
| BLD-3 | Firmware build with ESP-IDF v5.x, natively or in the `espressif/idf` container |

## Dependencies

**Depends on:** 
- [`s0-t6-scaffold-project`](s0-t6-scaffold-project.md) (Scaffold project)

**Blocks:** none in the roadmap

## Open questions

- is the optional container build wanted? It is the only task that replaces the "not pulled or measured" notes with real numbers.

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
