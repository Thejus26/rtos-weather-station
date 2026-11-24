# Sprint 7: Verification and Measurement

## Goal

Collect evidence that the system meets every requirement. Branch: `test/verification`. Needs hardware, a logic analyser and a machine that can capture serial for a full day. Freeze features first: only fixes from here on.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s7-t1 · Measure sampling jitter [HW]
- **ID:** s7-t1-measure-sampling-jitter
- **Description:** Sampling jitter: toggle a spare GPIO at each `sensor_task` wake-up and capture at least 100 intervals on the logic analyser. Cross-check with the `esp_timer` log.
- **Acceptance criteria:**
  - Maximum deviation is under +/-50 ms.
  - The capture is saved.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** M
- **Covers:** TIM-1, DEL-3d, GOAL-3

### s7-t2 · Measure display latency [HW]
- **ID:** s7-t2-measure-display-latency
- **Description:** Sample-to-display latency, final measurement under normal load.
- **Acceptance criteria:**
  - Maximum latency is under 1.5 s.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** S
- **Covers:** TIM-2, DEL-3d

### s7-t3 · Measure refresh and button [HW]
- **ID:** s7-t3-measure-refresh-and-button
- **Description:** Display refresh period and button response over at least 20 presses, with Wi-Fi and MQTT active.
- **Acceptance criteria:**
  - Refresh is 1 s.
  - Response is at or under 200 ms.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** S
- **Covers:** TIM-3, TIM-4, DEL-3d

### s7-t4 · Measure publish interval [HW]
- **ID:** s7-t4-measure-publish-interval
- **Description:** MQTT publish interval over at least 20 publishes.
- **Acceptance criteria:**
  - The interval is 30 s within +/-1 s.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** S
- **Covers:** TIM-5, DEL-3d

### s7-t5 · Verify mutex timeout [HW]
- **ID:** s7-t5-verify-mutex-timeout
- **Description:** I2C mutex timeout: hold the mutex past 100 ms with the injection hook and confirm the error is reported.
- **Acceptance criteria:**
  - The timeout is logged within about 100 ms.
- **Dependencies:** s6-t11-fault-injection-hooks
- **Effort:** S
- **Covers:** TIM-6, DEL-3d

### s7-t6 · Verify backoff [HW]
- **ID:** s7-t6-verify-backoff
- **Description:** Reconnect backoff: capture reconnect timing with the AP off.
- **Acceptance criteria:**
  - Delays follow 1 s doubling to 60 s.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** S
- **Covers:** TIM-7, DEL-3d

### s7-t7 · Verify recovery counts [HW]
- **ID:** s7-t7-verify-recovery-counts
- **Description:** Fault recovery counts: 3 consecutive failures trigger re-init, and 10 failed recoveries trigger a restart.
- **Acceptance criteria:**
  - Both thresholds are observed in the log.
- **Dependencies:** s6-t11-fault-injection-hooks
- **Effort:** S
- **Covers:** TIM-8, DEL-3d

### s7-t8 · Verify watchdog [HW]
- **ID:** s7-t8-verify-watchdog
- **Description:** Watchdog: stall each monitored task for more than 10 s.
- **Acceptance criteria:**
  - The cause is logged.
  - The device restarts.
- **Dependencies:** s6-t11-fault-injection-hooks
- **Effort:** S
- **Covers:** TIM-9, ERR-5, DEL-3d

### s7-t9 · Verify tick rate
- **ID:** s7-t9-verify-tick-rate
- **Description:** Confirm the tick rate at run time (1 ms per tick) and in the generated config.
- **Acceptance criteria:**
  - The runtime value and `sdkconfig` agree on 1000 Hz.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** S
- **Covers:** TIM-10, DEL-3d

### s7-t10 · Fault-injection matrix [HW]
- **ID:** s7-t10-fault-injection-matrix
- **Description:** Fault-injection matrix: sensor unplugged, out-of-range value, Wi-Fi off, broker down, queue overflow, task hang, low heap. One row per fault with the steps, the expected response, the observed response, and the log excerpt.
- **Acceptance criteria:**
  - Every row recovers without manual intervention.
- **Dependencies:** s6-t11-fault-injection-hooks
- **Effort:** L
- **Covers:** ERR-1 to ERR-6, ACC-3, DEL-3b, GOAL-4

### s7-t11 · Stack high-water marks, final [HW]
- **ID:** s7-t11-stack-hwm-final
- **Description:** Stack high-water marks under worst-case load (reconnect, publish, redraw). Resize any task over 75% used and re-measure.
- **Acceptance criteria:**
  - Every task has at least 25% headroom.
  - The final table is recorded.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** M
- **Covers:** NFR-2, ACC-4, DEL-2

### s7-t12 · Priority-inversion experiment
- **ID:** s7-t12-priority-inversion-experiment
- **Description:** Show the effect with a plain binary semaphore in place of `i2c_mutex`, then with the mutex, and record the difference.
- **Acceptance criteria:**
  - The observed difference is written up for the README Notes.
- **Dependencies:** s6-t12-keep-gates-green
- **Effort:** M
- **Covers:** OBJ-4, GOAL-2, DEL-5

### s7-t13 · Soak 24 h [HW]
- **ID:** s7-t13-soak-24h
- **Description:** 24-hour soak. Capture serial to a file with timestamps, free and minimum-free heap, uptime, reset reason and drop counters. Apply the D-17 criterion.
- **Acceptance criteria:**
  - No reset.
  - No heap growth beyond the criterion.
  - The log and a summary are saved.
- **Dependencies:** s7-t1-measure-sampling-jitter, s7-t10-fault-injection-matrix, s7-t11-stack-hwm-final
- **Effort:** L
- **Covers:** NFR-3, DEL-3c

### s7-t14 · No-allocation audit
- **ID:** s7-t14-no-alloc-audit
- **Description:** NFR-1 audit: search application code for `malloc`, `calloc`, `realloc`, `free` and `new`, and use heap tracing or the soak heap log to show no steady-state allocation in application code (D-13).
- **Acceptance criteria:**
  - No allocation calls in steady-state paths.
  - `app_logic` has no ESP-IDF includes.
- **Dependencies:** s7-t13-soak-24h
- **Effort:** M
- **Covers:** NFR-1, NFR-4

### s7-t15 · Final gates run
- **ID:** s7-t15-final-gates-run
- **Description:** Re-run `make docker-test` and `idf.py build` on the final tree and save the output.
- **Acceptance criteria:**
  - Both pass with no warnings.
- **Dependencies:** s7-t14-no-alloc-audit
- **Effort:** S
- **Covers:** BLD-2, BLD-3, ACC-5

## Definition of Done

- Every timing requirement and every fault row has recorded evidence.
- The soak passed.
- Every stack is within budget.
- Failures go back to the owning sprint as fix branches, then the affected measurement is repeated.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-17** (s7-t13): soak pass criterion for "no heap growth". Recommended default: minimum free heap at hour 24 is no lower than at hour 1 minus a stated margin (for example 1 KB), and no reset. NFR-3 does not quantify growth. Settle it before the soak starts.
- **s7-t8:** the roadmap says "stall each monitored task", which relies on the fault-injection hooks from s6-t11 but does not list a separate hook per task.
- **s7-t13:** the roadmap says the soak needs "a stable power supply and a machine that can capture serial for a full day", but does not say whether fault-injection hooks must be off during the soak. They are off by default in the build (s6-t11).
- **s7-t14:** "no steady-state allocation" with heap tracing is only possible if tracing is enabled in the build. The roadmap does not say how it is turned on.
