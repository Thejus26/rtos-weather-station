# s6-t12: Keep gates green

| Field | Value |
|-------|-------|
| Task ID | `s6-t12-keep-gates-green` |
| Sprint | [Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)](../../sprint-06-reliability.md) |
| Branch | `feature/fault-handling` |
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
- [`s6-t11-fault-injection-hooks`](s6-t11-fault-injection-hooks.md) (Fault-injection hooks)

**Blocks:** 
- [`s7-t1-measure-sampling-jitter`](../sprint-07/s7-t1-measure-sampling-jitter.md) (Measure sampling jitter)
- [`s7-t2-measure-display-latency`](../sprint-07/s7-t2-measure-display-latency.md) (Measure display latency)
- [`s7-t3-measure-refresh-and-button`](../sprint-07/s7-t3-measure-refresh-and-button.md) (Measure refresh and button)
- [`s7-t4-measure-publish-interval`](../sprint-07/s7-t4-measure-publish-interval.md) (Measure publish interval)
- [`s7-t6-verify-backoff`](../sprint-07/s7-t6-verify-backoff.md) (Verify backoff)
- [`s7-t9-verify-tick-rate`](../sprint-07/s7-t9-verify-tick-rate.md) (Verify tick rate)
- [`s7-t11-stack-hwm-final`](../sprint-07/s7-t11-stack-hwm-final.md) (Stack high-water marks, final)
- [`s7-t12-priority-inversion-experiment`](../sprint-07/s7-t12-priority-inversion-experiment.md) (Priority-inversion experiment)

## Source

Derived from [`sprint-06-reliability.md`](../../sprint-06-reliability.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
