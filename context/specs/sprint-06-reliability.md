# Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED)

## Goal

Make the system detect each fault in the error-handling table and recover on its own. Branch: `feature/fault-handling`. Needs hardware.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s6-t1 · Monitor task full
- **ID:** s6-t1-monitor-task-full
- **Description:** Full `monitor_task`: wait on `error_queue` with a bounded timeout (D-9) and run 10 s housekeeping by tick comparison, not by a 10 s block.
- **Acceptance criteria:**
  - The monitor wakes well inside the watchdog window.
- **Dependencies:** s3-t12-monitor-task-stub
- **Effort:** M
- **Covers:** TSK-1, TIM-9

### s6-t2 · Error dispatch
- **ID:** s6-t2-error-dispatch
- **Description:** Error dispatch: per-source and per-code counters and a log line at the right severity for each event.
- **Acceptance criteria:**
  - Counters appear in the housekeeping log.
- **Dependencies:** s6-t1-monitor-task-full
- **Effort:** S
- **Covers:** FR-9, OBJ-3

### s6-t3 · Sensor recovery
- **ID:** s6-t3-sensor-recovery
- **Description:** Settle D-12. Sensor recovery: after 3 consecutive failures (from `fault_policy`) `monitor_task` notifies `sensor_task`, which re-initialises the driver under `i2c_mutex` and keeps `SENSOR_OK_BIT` cleared until a read succeeds.
- **Acceptance criteria:**
  - Unplugging then replugging the sensor recovers without a reset.
- **Dependencies:** s6-t2-error-dispatch, s1-t11-fault-policy
- **Effort:** L
- **Covers:** FR-8, TIM-8, ERR-1, OBJ-7, GOAL-4

### s6-t4 · Restart after failed recoveries
- **ID:** s6-t4-restart-after-failed-recoveries
- **Description:** Count failed recoveries. After 10, log the cause and call `esp_restart()`.
- **Acceptance criteria:**
  - A permanently dead sensor ends in a restart with a logged reason.
- **Dependencies:** s6-t3-sensor-recovery
- **Effort:** M
- **Covers:** FR-8, TIM-8

### s6-t5 · Validation faults feed policy
- **ID:** s6-t5-validation-faults-feed-policy
- **Description:** Out-of-range and jump rejections count as sensor faults and feed the same policy.
- **Acceptance criteria:**
  - Repeated bad values trigger re-init like I2C errors.
- **Dependencies:** s6-t3-sensor-recovery
- **Effort:** S
- **Covers:** ERR-2, FR-8

### s6-t6 · Status LED states
- **ID:** s6-t6-status-led-states
- **Description:** Settle D-6. Status LED state machine driven by `monitor_task`: OK, no network, sensor fault, critical.
- **Acceptance criteria:**
  - Each state shows its own pattern on the LED.
- **Dependencies:** s6-t2-error-dispatch, s2-t13-status-led-driver
- **Effort:** M
- **Covers:** FR-9, HW-5

### s6-t7 · Task watchdog
- **ID:** s6-t7-task-watchdog
- **Description:** Task watchdog: subscribe `sensor_task`, `process_task` and `monitor_task`, and have each feed its own entry in its loop. On a timeout, log which task hung and restart.
- **Acceptance criteria:**
  - A stalled task causes a logged restart after 10 s.
- **Dependencies:** s6-t1-monitor-task-full, s0-t8-sdkconfig-defaults
- **Effort:** M
- **Covers:** FR-9, TIM-9, ERR-5, GOAL-4

### s6-t8 · Heap monitor
- **ID:** s6-t8-heap-monitor
- **Description:** Heap monitor in housekeeping: read free and minimum-free heap and act on the `heap_policy` result (warn below 20 KB, restart if it keeps falling).
- **Acceptance criteria:**
  - Heap numbers appear in the housekeeping log.
- **Dependencies:** s6-t1-monitor-task-full, s1-t13-heap-policy
- **Effort:** M
- **Covers:** FR-9, ERR-6, NFR-3

### s6-t9 · Reset reason logging
- **ID:** s6-t9-reset-reason-logging
- **Description:** Log the reset reason and a boot counter at start-up, so watchdog and brown-out restarts are visible in logs.
- **Acceptance criteria:**
  - The reset reason is shown on every boot.
- **Dependencies:** s6-t7-task-watchdog
- **Effort:** S
- **Covers:** ERR-5, NFR-3

### s6-t10 · Drop counters
- **ID:** s6-t10-drop-counters
- **Description:** Surface queue-full and drop counters (for `raw_queue` and `publish_queue`) in the housekeeping log.
- **Acceptance criteria:**
  - Counts appear.
  - Counts increase when a queue is overfilled.
- **Dependencies:** s6-t2-error-dispatch, s3-t11-process-task-publish-queue
- **Effort:** S
- **Covers:** ERR-4

### s6-t11 · Fault-injection hooks
- **ID:** s6-t11-fault-injection-hooks
- **Description:** Fault-injection hooks behind a Kconfig flag that is off by default: force N consecutive sensor errors, inject out-of-range values, hold `i2c_mutex`, stall a task, leak heap, force Wi-Fi and MQTT disconnects, and fill `publish_queue`.
- **Acceptance criteria:**
  - Each injection can be switched on from `menuconfig`.
  - The default build contains none of them.
- **Dependencies:** s6-t7-task-watchdog, s6-t8-heap-monitor
- **Effort:** L
- **Covers:** ERR-1 to ERR-6, TIM-6, TIM-8

### s6-t12 · Keep gates green
- **ID:** s6-t12-keep-gates-green
- **Description:** Keep `make docker-test` and `idf.py build` green, with no new warnings.
- **Acceptance criteria:**
  - Both pass.
- **Dependencies:** s6-t11-fault-injection-hooks
- **Effort:** S
- **Covers:** BLD-2, BLD-3

## Definition of Done

- Each fault in the error-handling table can be provoked.
- Each is detected, reported, and recovered from (or restarted from) without manual action.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-6** (s6-t6): status LED patterns. Recommended default: solid = OK, slow blink = no network, fast blink = sensor fault, double blink = critical. FR-9 says "shows system state" without defining states.
- **D-12** (s6-t3): how `monitor_task` asks `sensor_task` to re-init. Recommended default: task notification to `sensor_task`, which re-initialises itself under `i2c_mutex`.
- **s6-t4:** "count failed recoveries" does not say when a recovery counts as failed (for example no successful read within one sample period after re-init). `fault_policy` from s1-t11 defines the counter, but the roadmap does not define the failure timing.
- **s6-t7:** the watchdog covers three of the five tasks (`sensor_task`, `process_task`, `monitor_task`). The roadmap does not say whether `display_task` and `comms_task` are deliberately excluded.
- **s6-t8:** the N for "keeps falling" comes from D-14 in Sprint 1. If it was not logged there, it must be settled before this task.
