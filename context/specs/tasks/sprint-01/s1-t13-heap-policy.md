# s1-t13: Heap policy

| Field | Value |
|-------|-------|
| Task ID | `s1-t13-heap-policy` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-14. `components/app_logic/heap_policy.[ch]`: decide ok / warn / restart from free-heap samples against the 20 KB threshold and the falling-trend rule.

## Acceptance criteria

- [ ] The decision is a pure function of the supplied samples.

## Requirements covered

| ID | Requirement |
|----|-------------|
| ERR-6 | Low heap (for example below 20 KB): log a warning, restart if it keeps falling |
| FR-9 | Task watchdog and heap monitor; status LED shows system state |
| NFR-3 | 24-hour continuous run without reset or heap growth |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-14** (settled in this task): "Restart if heap continues to fall" criterion
  - Recommended default: Below 20 KB threshold, restart if the minimum free heap fell on N consecutive housekeeping checks (choose N and log it)
  - Why it matters: ERR-6 does not define "continues"

## Dependencies

**Depends on:** 
- [`s0-t4-harness-smoke-test`](../sprint-00/s0-t4-harness-smoke-test.md) (Harness smoke test)

**Blocks:** 
- [`s1-t14-heap-policy-test`](s1-t14-heap-policy-test.md) (Heap policy test)
- [`s6-t8-heap-monitor`](../sprint-06/s6-t8-heap-monitor.md) (Heap monitor)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
