# Sprint 3: RTOS Core and Sensing Pipeline

## Goal

Create every shared object and task, and make a sample flow from the sensor to the shared data and the publish queue. Branch: `feature/rtos-core`. Needs hardware.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s3-t1 · Event bits and handles
- **ID:** s3-t1-event-bits-and-handles
- **Description:** Settle D-7, D-8, D-13. Define the event bits `WIFI_CONNECTED_BIT`, `MQTT_CONNECTED_BIT`, `SENSOR_OK_BIT` and a header that exposes the shared handles to the tasks.
- **Acceptance criteria:**
  - Names match `coding-standards.md` section 3.
  - Decisions are logged.
- **Dependencies:** s2-t15-bringup-loop
- **Effort:** S
- **Covers:** OBJ-7, GOAL-1

### s3-t2 · Create shared objects
- **ID:** s3-t2-create-shared-objects
- **Description:** `main.c` creates every shared object at startup with sizes from `app_config.h`: `raw_queue` (8), `publish_queue` (10), `error_queue` (8), `i2c_mutex` (a real mutex, for priority inheritance), `data_mutex`, `button_sem` (binary), `sys_events`. Check for NULL.
- **Acceptance criteria:**
  - The boot log confirms every object was created.
  - None are created after startup.
- **Dependencies:** s1-t17-app-types-header, s3-t1-event-bits-and-handles
- **Effort:** M
- **Covers:** OBJ-1 to OBJ-7, NFR-1, GOAL-2

### s3-t3 · Latest struct
- **ID:** s3-t3-latest-struct
- **Description:** The shared `latest` struct with copy-in and copy-out accessors that take `data_mutex` with a timeout.
- **Acceptance criteria:**
  - Accessors hold the mutex only for the copy.
- **Dependencies:** s3-t2-create-shared-objects
- **Effort:** S
- **Covers:** OBJ-5, RUL-1

### s3-t4 · Create tasks
- **ID:** s3-t4-create-tasks
- **Description:** Create the five tasks with the overview's priorities and stack sizes (6, 5, 4, 3, 3 and 3, 4, 3, 3, 6 KB), initially as logging stubs.
- **Acceptance criteria:**
  - All five tasks appear in the runtime task list with the right priorities.
- **Dependencies:** s3-t2-create-shared-objects
- **Effort:** M
- **Covers:** TSK-1 to TSK-5, GOAL-1

### s3-t5 · Sensor task period
- **ID:** s3-t5-sensor-task-period
- **Description:** `sensor_task` skeleton: 5 s period with `vTaskDelayUntil`, logging the measured period with `esp_timer`.
- **Acceptance criteria:**
  - The log shows 5000 ms periods.
- **Dependencies:** s3-t4-create-tasks
- **Effort:** S
- **Covers:** FR-1, TSK-2, TIM-1, GOAL-3

### s3-t6 · Sensor task I2C mutex
- **ID:** s3-t6-sensor-task-i2c-mutex
- **Description:** `sensor_task` reads through `sensor_read()` while holding `i2c_mutex` (100 ms timeout), releasing it right after. A timeout is reported to `error_queue` with a zero timeout.
- **Acceptance criteria:**
  - The mutex is held only around the transaction.
- **Dependencies:** s3-t5-sensor-task-period, s2-t8-sensor-interface
- **Effort:** M
- **Covers:** TIM-6, OBJ-4, OBJ-3, RUL-1, RUL-2

### s3-t7 · Sensor task retry
- **ID:** s3-t7-sensor-task-retry
- **Description:** `sensor_task` retries a failed read up to 3 times, then reports the failure, and sets or clears `SENSOR_OK_BIT`.
- **Acceptance criteria:**
  - Unplugging the sensor clears the bit after 3 attempts.
- **Dependencies:** s3-t6-sensor-task-i2c-mutex
- **Effort:** S
- **Covers:** ERR-1, FR-8, OBJ-7

### s3-t8 · Sensor task enqueue
- **ID:** s3-t8-sensor-task-enqueue
- **Description:** `sensor_task` builds a `sample_t` with a timestamp and sends it to `raw_queue`. If the queue is full, report it and drop.
- **Acceptance criteria:**
  - Samples reach the queue every 5 s.
- **Dependencies:** s3-t6-sensor-task-i2c-mutex
- **Effort:** S
- **Covers:** OBJ-1, FR-1

### s3-t9 · Process task validate
- **ID:** s3-t9-process-task-validate
- **Description:** `process_task` waits on `raw_queue` with a timeout under 10 s (D-9), validates each sample, and reports rejects to `error_queue`.
- **Acceptance criteria:**
  - A forced bad value is discarded and reported.
- **Dependencies:** s3-t8-sensor-task-enqueue, s1-t4-validate
- **Effort:** M
- **Covers:** TSK-3, FR-2, ERR-2, OBJ-3

### s3-t10 · Process task filter
- **ID:** s3-t10-process-task-filter
- **Description:** `process_task` applies the moving average and dew point to accepted samples and writes `latest` under `data_mutex`.
- **Acceptance criteria:**
  - `latest` holds filtered values and a dew point.
- **Dependencies:** s3-t9-process-task-validate, s1-t2-moving-average, s1-t6-dew-point
- **Effort:** S
- **Covers:** FR-2, FR-3, OBJ-5

### s3-t11 · Process task publish queue
- **ID:** s3-t11-process-task-publish-queue
- **Description:** `process_task` enqueues a `reading_t` to `publish_queue` every 30 s. When the queue is full it drops the oldest entry and counts the drop.
- **Acceptance criteria:**
  - A drop counter increments when the queue is deliberately filled.
- **Dependencies:** s3-t10-process-task-filter
- **Effort:** M
- **Covers:** FR-6, OBJ-2, ERR-4, TIM-5

### s3-t12 · Monitor task stub
- **ID:** s3-t12-monitor-task-stub
- **Description:** `monitor_task` stub: wait on `error_queue` with a bounded timeout and log each event. The full behaviour comes in Sprint 6.
- **Acceptance criteria:**
  - Every reported error appears in the log.
- **Dependencies:** s3-t4-create-tasks
- **Effort:** S
- **Covers:** TSK-1, OBJ-3

### s3-t13 · Stack high-water-mark logging
- **ID:** s3-t13-stack-hwm-logging
- **Description:** Log each task's stack high-water mark every 10 s so measurement starts early.
- **Acceptance criteria:**
  - The log shows a number for each of the five tasks.
- **Dependencies:** s3-t12-monitor-task-stub
- **Effort:** S
- **Covers:** NFR-2

### s3-t14 · Sample logging
- **ID:** s3-t14-sample-logging
- **Description:** Log each processed sample (raw, filtered, dew point) on serial.
- **Acceptance criteria:**
  - The serial log shows a line every 5 s.
- **Dependencies:** s3-t10-process-task-filter
- **Effort:** S
- **Covers:** FR-1

### s3-t15 · Hardware cadence check [HW]
- **ID:** s3-t15-hw-cadence-check
- **Description:** Run for 10 minutes. Check that the cadence holds and `raw_queue` never fills. Record preliminary jitter from the `esp_timer` log.
- **Acceptance criteria:**
  - Preliminary jitter is within +/-50 ms.
  - `raw_queue` never fills.
- **Dependencies:** s3-t14-sample-logging
- **Effort:** S
- **Covers:** TIM-1, GOAL-3

### s3-t16 · Keep gates green
- **ID:** s3-t16-keep-gates-green
- **Description:** Keep `make docker-test` and `idf.py build` green, with no new warnings.
- **Acceptance criteria:**
  - Both pass.
- **Dependencies:** s3-t14-sample-logging
- **Effort:** S
- **Covers:** BLD-2, BLD-3

## Definition of Done

- All objects and tasks exist.
- The serial log shows a processed sample every 5 s.
- An injected bad sample is rejected and reported.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-7** (s3-t1): event-bit naming. Recommended default: bits named as in the overview, with macros `<NAME>_BIT`.
- **D-8** (s3-t1): task core affinity. Recommended default: unpinned (`xTaskCreate`) unless measurement shows a need, and document why.
- **D-9** (s3-t9): watchdog interaction with blocking waits. Recommended default: `process_task` and `monitor_task` wait with a timeout well under 10 s (for example 2 s). The roadmap states the reason: a 10 s wait would equal the 10 s watchdog.
- **D-13** (s3-t1): scope of "no dynamic allocation". Recommended default: application code only, with ESP-IDF internals covered by the heap-growth check.
- **s3-t11:** the roadmap says to enqueue "every 30 s" but does not say whether the 30 s reading is the latest filtered value or an average over the period. The roadmap gives no rule.
- **s3-t13:** the 10 s stack logging period matches the `monitor_task` housekeeping period, but the stub in s3-t12 has no housekeeping yet. The roadmap does not say which task does the logging.
