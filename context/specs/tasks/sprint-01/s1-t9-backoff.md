# s1-t9: Backoff

| Field | Value |
|-------|-------|
| Task ID | `s1-t9-backoff` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`components/app_logic/backoff.[ch]`: next delay starts at 1000 ms, doubles, caps at 60000 ms, resets on success.

## Acceptance criteria

- [ ] Compiles clean.

## Requirements covered

| ID | Requirement |
|----|-------------|
| TIM-7 | Wi-Fi reconnect backoff 1 s doubling up to 60 s |
| FR-7 | Keep sampling and displaying when Wi-Fi or broker is down; reconnect with exponential backoff 1 s to 60 s |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Dependencies

**Depends on:** 
- [`s0-t4-harness-smoke-test`](../sprint-00/s0-t4-harness-smoke-test.md) (Harness smoke test)

**Blocks:** 
- [`s1-t10-backoff-test`](s1-t10-backoff-test.md) (Backoff test)
- [`s5-t5-wifi-backoff`](../sprint-05/s5-t5-wifi-backoff.md) (Wi-Fi backoff)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
