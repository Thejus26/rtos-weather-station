# s5-t8: JSON payload

| Field | Value |
|-------|-------|
| Task ID | `s5-t8-json-payload` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Build the JSON payload with `reading_to_json` into a static buffer, from the `publish_queue` entry plus the device ID and timestamp.

## Acceptance criteria

- [ ] The subscriber shows valid JSON with all fields.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |
| NFR-1 | No dynamic allocation in steady state |

## Dependencies

**Depends on:** 
- [`s5-t6-sntp-time`](s5-t6-sntp-time.md) (SNTP time)
- [`s1-t15-reading-json`](../sprint-01/s1-t15-reading-json.md) (Reading JSON)

**Blocks:** 
- [`s5-t9-comms-task`](s5-t9-comms-task.md) (Comms task)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
