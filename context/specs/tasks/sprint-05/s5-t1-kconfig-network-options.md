# s5-t1: Kconfig network options

| Field | Value |
|-------|-------|
| Task ID | `s5-t1-kconfig-network-options` |
| Sprint | [Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)](../../sprint-05-connectivity.md) |
| Branch | `feature/comms` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-15. Extend `Kconfig.projbuild` with Wi-Fi SSID and password, broker URI, topic base and device ID. Confirm `sdkconfig.defaults` has no credentials.

## Acceptance criteria

- [ ] The options appear in `menuconfig`.
- [ ] No secrets are in tracked files.

## Requirements covered

| ID | Requirement |
|----|-------------|
| FR-10 | Configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code |
| FR-6 | Publish JSON readings to MQTT every 30 s with SNTP timestamp and device ID |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-15** (settled in this task): MQTT topic, QoS and retain
  - Recommended default: Topic `weather/<device_id>/reading`, QoS 1, no retain
  - Why it matters: The overview's subscriber example uses `weather/#` only

## Dependencies

**Depends on:** 
- [`s0-t10-kconfig-menu`](../sprint-00/s0-t10-kconfig-menu.md) (Kconfig menu)

**Blocks:** 
- [`s5-t3-nvs-config`](s5-t3-nvs-config.md) (NVS config)

## Source

Derived from [`sprint-05-connectivity.md`](../../sprint-05-connectivity.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
