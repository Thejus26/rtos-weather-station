# s5-t14: Comms stack check

| Field | Value |
|-------|-------|
| Task ID | `s5-t14-comms-stack-check` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Check the `comms_task` stack high-water mark during connect, reconnect and publish, and resize if needed.

## Acceptance criteria

- [ ] At least 25% headroom at the worst point.

## Requirements covered

| ID | Requirement |
|----|-------------|
| NFR-2 | Every task has a measured stack high-water mark with at least 25% headroom |
| TSK-5 | `comms_task`: priority 3, 6 KB, waits on `WIFI_CONNECTED_BIT` |

## Dependencies

**Depends on:** 
- [`s5-t9-comms-task`](s5-t9-comms-task.md) (Comms task)

**Blocks:** none in the roadmap

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
