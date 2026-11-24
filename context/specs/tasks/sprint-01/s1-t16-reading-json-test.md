# s1-t16: Reading JSON test

| Field | Value |
|-------|-------|
| Task ID | `s1-t16-reading-json-test` |
| Sprint | [Sprint 1: Pure-C Logic (host only)](../../sprint-01-pure-c-logic.md) |
| Branch | `feature/app-logic` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`test/host/test_reading_json.c`: exact output for a known reading, truncation detection, pre-sync timestamp marker.

## Acceptance criteria

- [ ] Assertions pass.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| BLD-2 | `make test` / `make docker-test` with `-Wall -Wextra -Werror`, non-zero exit on failure |

## Dependencies

**Depends on:** 
- [`s1-t15-reading-json`](s1-t15-reading-json.md) (Reading JSON)

**Blocks:** 
- [`s1-t18-full-suite-run`](s1-t18-full-suite-run.md) (Full suite run)

## Source

Derived from [`sprint-01-pure-c-logic.md`](../../sprint-01-pure-c-logic.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
