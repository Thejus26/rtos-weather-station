# s3-t2: Create shared objects

| Field | Value |
|-------|-------|
| Task ID | `s3-t2-create-shared-objects` |
| Sprint | [Sprint 3: RTOS Core and Sensing Pipeline](../../sprint-03-rtos-core.md) |
| Branch | `feature/rtos-core` |
| Effort | M: a few sittings (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

`main.c` creates every shared object at startup with sizes from `app_config.h`: `raw_queue` (8), `publish_queue` (10), `error_queue` (8), `i2c_mutex` (a real mutex, for priority inheritance), `data_mutex`, `button_sem` (binary), `sys_events`. Check for NULL.

## Acceptance criteria

- [ ] The boot log confirms every object was created.
- [ ] None are created after startup.

## Requirements covered

| ID | Requirement |
|----|-------------|
| OBJ-1 | `raw_queue`: 8 x `sample_t`, `sensor_task` to `process_task` |
| OBJ-2 | `publish_queue`: 10 x `reading_t`, `process_task` to `comms_task`, drop oldest when full |
| OBJ-3 | `error_queue`: 8 x `error_event_t`, all tasks to `monitor_task`, senders never block |
| OBJ-4 | `i2c_mutex` with priority inheritance, shared by `sensor_task` and `display_task` |
| OBJ-5 | `data_mutex` protecting the shared `latest` struct |
| OBJ-6 | `button_sem` binary semaphore, ISR to `display_task`, debounced |
| OBJ-7 | `sys_events` event group, 3 bits: `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK` |
| NFR-1 | No dynamic allocation in steady state |
| GOAL-2 | Queues, mutexes, binary semaphores and event groups, each for the problem it suits |

## Dependencies

**Depends on:** 
- [`s1-t17-app-types-header`](../sprint-01/s1-t17-app-types-header.md) (App types header)
- [`s3-t1-event-bits-and-handles`](s3-t1-event-bits-and-handles.md) (Event bits and handles)

**Blocks:** 
- [`s3-t3-latest-struct`](s3-t3-latest-struct.md) (Latest struct)
- [`s3-t4-create-tasks`](s3-t4-create-tasks.md) (Create tasks)
- [`s4-t1-button-isr`](../sprint-04/s4-t1-button-isr.md) (Button ISR)

## Source

Derived from [`sprint-03-rtos-core.md`](../../sprint-03-rtos-core.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
