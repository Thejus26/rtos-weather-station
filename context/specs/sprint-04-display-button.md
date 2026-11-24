# Sprint 4: Display and Button

## Goal

Make the OLED show live values, and make the button work through an ISR and a semaphore. Branch: `feature/display-button`. Needs hardware.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s4-t1 · Button ISR
- **ID:** s4-t1-button-isr
- **Description:** Button ISR: place it in IRAM, call `xSemaphoreGiveFromISR(button_sem)` and request a yield if a higher-priority task woke. No logging or blocking calls inside it.
- **Acceptance criteria:**
  - A press wakes `display_task`.
  - No `FromISR` calls exist outside the ISR.
- **Dependencies:** s3-t2-create-shared-objects, s2-t14-button-bounce-measure
- **Effort:** M
- **Covers:** FR-5, ISR-1, RUL-3, OBJ-6

### s4-t2 · Debounce
- **ID:** s4-t2-debounce
- **Description:** Settle D-10. Debounce using the bounce window measured in s2-t14-button-bounce-measure, so one press gives one semaphore.
- **Acceptance criteria:**
  - 20 presses produce exactly 20 toggles.
- **Dependencies:** s4-t1-button-isr
- **Effort:** S
- **Covers:** FR-5, HW-4

### s4-t3 · Display task loop
- **ID:** s4-t3-display-task-loop
- **Description:** `display_task` waits on `button_sem` with a 1 s timeout and refreshes on timeout or on a press.
- **Acceptance criteria:**
  - The display refreshes each second.
  - It refreshes immediately on a press.
- **Dependencies:** s3-t4-create-tasks, s4-t1-button-isr
- **Effort:** S
- **Covers:** FR-4, TSK-4, TIM-3, OBJ-6

### s4-t4 · Display task draw locking
- **ID:** s4-t4-display-task-draw-locking
- **Description:** `display_task` copies `latest` under `data_mutex` and releases it, then takes `i2c_mutex` (100 ms timeout) to draw. A timeout is reported.
- **Acceptance criteria:**
  - The two mutexes are never held together.
- **Dependencies:** s3-t3-latest-struct, s2-t12-oled-layout, s4-t3-display-task-loop
- **Effort:** M
- **Covers:** RUL-2, OBJ-4, OBJ-5, TIM-6

### s4-t5 · Unit toggle
- **ID:** s4-t5-unit-toggle
- **Description:** Keep the C/F state in `display_task` and convert only for display with `c_to_f`. Published data stays in Celsius.
- **Acceptance criteria:**
  - The toggle changes the shown unit and nothing else.
- **Dependencies:** s4-t4-display-task-draw-locking, s1-t8-unit-convert
- **Effort:** S
- **Covers:** FR-5

### s4-t6 · Render values
- **ID:** s4-t6-render-values
- **Description:** Draw temperature, humidity, dew point and unit, with a "no data yet" state before the first sample and a visible sensor-fault indicator driven by `SENSOR_OK_BIT`.
- **Acceptance criteria:**
  - Unplugging the sensor shows the indicator.
- **Dependencies:** s4-t4-display-task-draw-locking
- **Effort:** M
- **Covers:** FR-4, OBJ-7

### s4-t7 · Render link status
- **ID:** s4-t7-render-link-status
- **Description:** Draw Wi-Fi and MQTT status from `sys_events`. It shows "disconnected" until Sprint 5 sets the bits.
- **Acceptance criteria:**
  - Status text follows the event-group bits.
- **Dependencies:** s4-t4-display-task-draw-locking
- **Effort:** S
- **Covers:** FR-4, OBJ-7

### s4-t8 · Measure button response [HW]
- **ID:** s4-t8-measure-button-response
- **Description:** Measure button-to-OLED response over at least 20 presses, and the display refresh period.
- **Acceptance criteria:**
  - Response is at or under 200 ms.
  - Refresh is at 1 s.
  - Numbers are recorded.
- **Dependencies:** s4-t5-unit-toggle
- **Effort:** M
- **Covers:** TIM-3, TIM-4

### s4-t9 · Measure display latency [HW]
- **ID:** s4-t9-measure-display-latency
- **Description:** Measure sample-to-display latency using the sample timestamp and the draw-complete time.
- **Acceptance criteria:**
  - Latency is under 1.5 s.
  - Numbers are recorded.
- **Dependencies:** s4-t6-render-values
- **Effort:** S
- **Covers:** TIM-2

### s4-t10 · I2C contention test [HW]
- **ID:** s4-t10-i2c-contention-test
- **Description:** Run both bus users for 30 minutes with no unexpected mutex timeouts. Then hold `i2c_mutex` for 150 ms on purpose and confirm the timeout is reported.
- **Acceptance criteria:**
  - No spurious timeouts in the 30-minute run.
  - The forced timeout is logged.
- **Dependencies:** s4-t4-display-task-draw-locking
- **Effort:** M
- **Covers:** RUL-1, TIM-6, OBJ-4

## Definition of Done

- The OLED shows live, filtered values updating each second.
- The button toggles the unit within 200 ms.
- The I2C bus is shared without unexpected timeouts.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-10** (s4-t2): button debounce method. Recommended default: ignore edges within a window sized from the bounce measured in s2-t14, applied in the ISR. It must give one press = one semaphore give and stay inside the 200 ms response budget.
- **s4-t10:** to hold `i2c_mutex` for 150 ms on purpose, a test hook is needed. The roadmap only adds fault-injection hooks in s6-t11, so it does not say how this is done here (for example a temporary local change).
- **s4-t8 / s4-t9:** the roadmap gives no measurement method (logic analyser, serial timestamps) beyond the sample timestamp and draw-complete time in s4-t9.
