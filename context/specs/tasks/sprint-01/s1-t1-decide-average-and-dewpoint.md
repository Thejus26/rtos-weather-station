# s1-t1: Decide average and dew point

| Field | Value |
|-------|-------|
| Task ID | `s1-t1-decide-average-and-dewpoint` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-1 (partial moving-average window) and D-2 (dew point at 0 %RH). Log both in roadmap section 10.

## Acceptance criteria

- [ ] Both decisions are written down with the chosen behaviour.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-2 | Validate samples (range, rate of change) and smooth with a 5-sample moving average |
| FR-3 | Calculate dew point from the filtered values |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-1** (settled in this task): Moving-average output before 5 samples exist
  - Recommended default: Average of the samples received so far
  - Why it matters: "5-sample moving average" does not say what the first four outputs are
- **D-2** (settled in this task): Dew point at 0 %RH
  - Recommended default: Clamp humidity to a small minimum (for example 1 %) inside `dew_point`, and document it
  - Why it matters: 0 %RH is valid per FR-2, but the Magnus formula takes `log(0)` and returns NaN (checked in a container run)

## Dependencies

**Depends on:** 
- [`s0-t4-harness-smoke-test`](../sprint-00/s0-t4-harness-smoke-test.md) (Harness smoke test)

**Blocks:** 
- [`s1-t2-moving-average`](s1-t2-moving-average.md) (Moving average)
- [`s1-t4-validate`](s1-t4-validate.md) (Validate)
- [`s1-t6-dew-point`](s1-t6-dew-point.md) (Dew point)
- [`s1-t15-reading-json`](s1-t15-reading-json.md) (Reading JSON)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
