# s0-t5: Install ESP-IDF

| Field | Value |
|-------|-------|
| Task ID | `s0-t5-install-esp-idf` |
| Sprint | [Sprint 0: Foundation and Toolchain](../../sprint-00-foundation.md) |
| Branch | `chore/foundation` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Install ESP-IDF v5.x natively (or commit to the container route) and record the exact version.

## Acceptance criteria

- [ ] `idf.py --version` prints a v5.x version.

## Requirements covered

| ID | Requirement |
|----|-------------|
| PLT-1 | ESP32-DevKitC, ESP-IDF v5.x, native FreeRTOS (not the Arduino framework) |
| BLD-3 | Firmware build with ESP-IDF v5.x, natively or in the `espressif/idf` container |

## Dependencies

**Depends on:** none

**Blocks:** 
- [`s0-t6-scaffold-project`](s0-t6-scaffold-project.md) (Scaffold project)

## Open questions

- native ESP-IDF install or the container route? The roadmap allows either and asks only that the choice and exact version be recorded.

## Source

Derived from [`sprint-00-foundation.md`](../../sprint-00-foundation.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
