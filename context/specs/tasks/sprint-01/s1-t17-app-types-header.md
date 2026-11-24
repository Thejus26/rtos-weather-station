# s1-t17: App types header

| Field | Value |
|-------|-------|
| Task ID | `s1-t17-app-types-header` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-3. `main/app_types.h` (stdint-only): `sample_t`, `reading_t`, `error_event_t`, and fault source/code enums.

## Acceptance criteria

- [ ] Compiles in the firmware build and on the host.

## Requirements covered

| ID | Requirement |
|----|-------------|
| OBJ-1 | `raw_queue`: 8 x `sample_t`, `sensor_task` to `process_task` |
| OBJ-2 | `publish_queue`: 10 x `reading_t`, `process_task` to `comms_task`, drop oldest when full |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |
| FR-8 | Detect sensor failures (I2C error or out-of-range), report them, recover by re-initialising |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-3** (settled in this task): Where shared types live
  - Recommended default: `main/app_types.h`, stdint-only; `app_logic` functions take plain values
  - Why it matters: Keeps `app_logic` free of project types and still host-testable

## Dependencies

**Depends on:** 
- [`s1-t4-validate`](s1-t4-validate.md) (Validate)

**Blocks:** 
- [`s3-t2-create-shared-objects`](../sprint-03/s3-t2-create-shared-objects.md) (Create shared objects)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
