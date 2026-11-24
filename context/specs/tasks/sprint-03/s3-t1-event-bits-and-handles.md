# s3-t1: Event bits and handles

| Field | Value |
|-------|-------|
| Task ID | `s3-t1-event-bits-and-handles` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | S: one focused sitting (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

Settle D-7, D-8, D-13. Define the event bits `WIFI_CONNECTED_BIT`, `MQTT_CONNECTED_BIT`, `SENSOR_OK_BIT` and a header that exposes the shared handles to the tasks.

## Acceptance criteria

- [ ] Names match `coding-standards.md` section 3.
- [ ] Decisions are logged.

## Requirements covered

| ID | Requirement |
|----|-------------|
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |
| GOAL-1 | Multi-task FreeRTOS application with clean task boundaries |

## Decisions

Log any outcome in roadmap section 10 (Decision log).

- **D-7** (settled in this task): Event-group bit naming
  - Recommended default: Bits named as in the overview, macros `<NAME>_BIT`
  - Why it matters: The overview uses both `WIFI_CONNECTED` and `WIFI_CONNECTED_BIT`
- **D-8** (settled in this task): Task core affinity
  - Recommended default: Unpinned (`xTaskCreate`) unless measurement shows a need; document why
  - Why it matters: The ESP32 is dual-core and the overview mentions pinning only as an available feature
- **D-13** (settled in this task): Scope of NFR-1 "no dynamic allocation"
  - Recommended default: Application code only: static buffers for JSON, framebuffer and averages; ESP-IDF internals (Wi-Fi, MQTT) are excluded and covered by the heap-growth check
  - Why it matters: The Wi-Fi and MQTT stacks allocate internally

## Dependencies

**Depends on:** 
- [`s2-t15-bringup-loop`](../sprint-02/s2-t15-bringup-loop.md) (Bring-up loop)

**Blocks:** 
- [`s3-t2-create-shared-objects`](s3-t2-create-shared-objects.md) (Create shared objects)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
