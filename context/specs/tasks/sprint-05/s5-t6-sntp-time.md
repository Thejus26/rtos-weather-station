# s5-t6: SNTP time

| Field | Value |
|-------|-------|
| Task ID | `s5-t6-sntp-time` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

SNTP start-up with a synchronised flag and ISO 8601 UTC timestamps. Before sync, use the marker chosen in D-11.

## Acceptance criteria

- [ ] Timestamps are correct after sync.
- [ ] They are clearly marked before sync.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-11** (referenced here): JSON schema, timestamp format and pre-sync behaviour
  - Recommended default: `device_id`, ISO 8601 UTC `ts`, `temperature_c`, `humidity_pct`, `dew_point_c`; before SNTP sync send an explicit marker, not a fake time
  - Why it matters: FR-6 names the fields loosely; the SNTP delay at boot is not specified

## Dependencies

**Depends on:** 
- [`s5-t4-wifi-station`](s5-t4-wifi-station.md) (Wi-Fi station)

**Blocks:** 
- [`s5-t8-json-payload`](s5-t8-json-payload.md) (JSON payload)

## Open questions

- the roadmap does not say how long to wait for the first SNTP sync after boot, or what `comms_task` does with readings that carry the pre-sync marker (publish or hold).

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
