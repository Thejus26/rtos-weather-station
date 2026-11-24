# s6-t8: Heap monitor

| Field | Value |
|-------|-------|
| Task ID | `s6-t8-heap-monitor` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Heap monitor in housekeeping: read free and minimum-free heap and act on the `heap_policy` result (warn below 20 KB, restart if it keeps falling).

## Acceptance criteria

- [ ] Heap numbers appear in the housekeeping log.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-9 | Task watchdog and heap monitor; status LED shows system state |
| ERR-6 | Low heap (for example below 20 KB): log a warning, restart if it keeps falling |
| NFR-3 | 24-hour continuous run without reset or heap growth |

## Dependencies

**Depends on:** 
- [`s6-t1-monitor-task-full`](s6-t1-monitor-task-full.md) (Monitor task full)
- [`s1-t13-heap-policy`](../sprint-01/s1-t13-heap-policy.md) (Heap policy)

**Blocks:** 
- [`s6-t11-fault-injection-hooks`](s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

## Open questions

- the N for "keeps falling" comes from D-14 in Sprint 1. If it was not logged there, it must be settled before this task.

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
