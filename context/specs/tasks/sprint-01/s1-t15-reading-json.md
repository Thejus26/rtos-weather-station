# s1-t15: Reading JSON

| Field | Value |
|-------|-------|
| Task ID | `s1-t15-reading-json` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-11. `components/app_logic/reading_json.[ch]`: format a reading into a caller-supplied buffer with length checking (no heap).

## Acceptance criteria

- [ ] Returns an error instead of overflowing a too-small buffer.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| NFR-1 | No dynamic allocation in steady state |
| NFR-4 | Signal-processing logic is pure C (no ESP-IDF or FreeRTOS includes), tested on the host |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-11** (settled in this task): JSON schema, timestamp format and pre-sync behaviour
  - Recommended default: `device_id`, ISO 8601 UTC `ts`, `temperature_c`, `humidity_pct`, `dew_point_c`; before SNTP sync send an explicit marker, not a fake time
  - Why it matters: FR-6 names the fields loosely; the SNTP delay at boot is not specified

## Dependencies

**Depends on:** 
- [`s1-t1-decide-average-and-dewpoint`](s1-t1-decide-average-and-dewpoint.md) (Decide average and dew point)

**Blocks:** 
- [`s1-t16-reading-json-test`](s1-t16-reading-json-test.md) (Reading JSON test)
- [`s5-t8-json-payload`](../sprint-05/s5-t8-json-payload.md) (JSON payload)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
