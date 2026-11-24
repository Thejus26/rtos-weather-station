# s7-t14: No-allocation audit

| Field | Value |
|-------|-------|
| Task ID | `s7-t14-no-alloc-audit` |
| Sprint | [Sprint 7: Verification and Measurement](../../sprint-07-verification.md) |
| Branch | `test/verification` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

NFR-1 audit: search application code for `malloc`, `calloc`, `realloc`, `free` and `new`, and use heap tracing or the soak heap log to show no steady-state allocation in application code (D-13).

## Acceptance criteria

- [ ] No allocation calls in steady-state paths.
- [ ] `app_logic` has no ESP-IDF includes.

## Requirements covered

| ID | Requirement |
|----|-------------|
| NFR-1 | No dynamic allocation in steady state |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-13** (referenced here): Scope of NFR-1 "no dynamic allocation"
  - Recommended default: Application code only: static buffers for JSON, framebuffer and averages; ESP-IDF internals (Wi-Fi, MQTT) are excluded and covered by the heap-growth check
  - Why it matters: The Wi-Fi and MQTT stacks allocate internally

## Dependencies

**Depends on:** 
- [`s7-t13-soak-24h`](s7-t13-soak-24h.md) (Soak 24 h)

**Blocks:** 
- [`s7-t15-final-gates-run`](s7-t15-final-gates-run.md) (Final gates run)

## Open questions

- "no steady-state allocation" with heap tracing is only possible if tracing is enabled in the build. The roadmap does not say how it is turned on.

## Source

Derived from [`sprint-07-verification.md`](../../sprint-07-verification.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
