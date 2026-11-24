# Task Specs

One spec per roadmap task (129 in total), grouped by sprint. Generated from the sprint specs and `spec-roadmap.md`. If a task changes, edit the roadmap and the sprint spec first, then regenerate or edit the task file to match.

## Sprint 0: Foundation and Toolchain (13 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s0-t1-parts-and-hardware-check`](sprint-00/s0-t1-parts-and-hardware-check.md) | Parts and hardware check | S |  |
| [`s0-t2-test-image`](sprint-00/s0-t2-test-image.md) | Test image | S |  |
| [`s0-t3-makefile`](sprint-00/s0-t3-makefile.md) | Makefile | S |  |
| [`s0-t4-harness-smoke-test`](sprint-00/s0-t4-harness-smoke-test.md) | Harness smoke test | S |  |
| [`s0-t5-install-esp-idf`](sprint-00/s0-t5-install-esp-idf.md) | Install ESP-IDF | M |  |
| [`s0-t6-scaffold-project`](sprint-00/s0-t6-scaffold-project.md) | Scaffold project | S |  |
| [`s0-t7-container-firmware-build`](sprint-00/s0-t7-container-firmware-build.md) | Container firmware build (optional) | S |  |
| [`s0-t8-sdkconfig-defaults`](sprint-00/s0-t8-sdkconfig-defaults.md) | `sdkconfig.defaults` | S |  |
| [`s0-t9-app-config-header`](sprint-00/s0-t9-app-config-header.md) | `app_config.h` | S |  |
| [`s0-t10-kconfig-menu`](sprint-00/s0-t10-kconfig-menu.md) | Kconfig menu | S |  |
| [`s0-t11-flash-scaffold`](sprint-00/s0-t11-flash-scaffold.md) | Flash scaffold | S | yes |
| [`s0-t12-adapt-agent-tooling`](sprint-00/s0-t12-adapt-agent-tooling.md) | Adapt agent tooling | M |  |
| [`s0-t13-load-sprint-1`](sprint-00/s0-t13-load-sprint-1.md) | Load Sprint 1 | S |  |

## Sprint 1: Pure-C Logic (host only) (19 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s1-t1-decide-average-and-dewpoint`](sprint-01/s1-t1-decide-average-and-dewpoint.md) | Decide average and dew point | S |  |
| [`s1-t2-moving-average`](sprint-01/s1-t2-moving-average.md) | Moving average | S |  |
| [`s1-t3-moving-average-test`](sprint-01/s1-t3-moving-average-test.md) | Moving average test | S |  |
| [`s1-t4-validate`](sprint-01/s1-t4-validate.md) | Validate | M |  |
| [`s1-t5-validate-test`](sprint-01/s1-t5-validate-test.md) | Validate test | S |  |
| [`s1-t6-dew-point`](sprint-01/s1-t6-dew-point.md) | Dew point | S |  |
| [`s1-t7-dew-point-test`](sprint-01/s1-t7-dew-point-test.md) | Dew point test | S |  |
| [`s1-t8-unit-convert`](sprint-01/s1-t8-unit-convert.md) | Unit convert | S |  |
| [`s1-t9-backoff`](sprint-01/s1-t9-backoff.md) | Backoff | S |  |
| [`s1-t10-backoff-test`](sprint-01/s1-t10-backoff-test.md) | Backoff test | S |  |
| [`s1-t11-fault-policy`](sprint-01/s1-t11-fault-policy.md) | Fault policy | M |  |
| [`s1-t12-fault-policy-test`](sprint-01/s1-t12-fault-policy-test.md) | Fault policy test | S |  |
| [`s1-t13-heap-policy`](sprint-01/s1-t13-heap-policy.md) | Heap policy | M |  |
| [`s1-t14-heap-policy-test`](sprint-01/s1-t14-heap-policy-test.md) | Heap policy test | S |  |
| [`s1-t15-reading-json`](sprint-01/s1-t15-reading-json.md) | Reading JSON | M |  |
| [`s1-t16-reading-json-test`](sprint-01/s1-t16-reading-json-test.md) | Reading JSON test | S |  |
| [`s1-t17-app-types-header`](sprint-01/s1-t17-app-types-header.md) | App types header | S |  |
| [`s1-t18-full-suite-run`](sprint-01/s1-t18-full-suite-run.md) | Full suite run | S |  |
| [`s1-t19-sync-layout-docs`](sprint-01/s1-t19-sync-layout-docs.md) | Sync layout docs | S |  |

## Sprint 2: Hardware Bring-up and Drivers (16 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s2-t1-wire-circuit`](sprint-02/s2-t1-wire-circuit.md) | Wire circuit | M | yes |
| [`s2-t2-choose-i2c-api`](sprint-02/s2-t2-choose-i2c-api.md) | Choose I2C API | S |  |
| [`s2-t3-i2c-bus-driver`](sprint-02/s2-t3-i2c-bus-driver.md) | I2C bus driver | M |  |
| [`s2-t4-i2c-scan`](sprint-02/s2-t4-i2c-scan.md) | I2C scan | S | yes |
| [`s2-t5-bme280-init`](sprint-02/s2-t5-bme280-init.md) | BME280 init | M |  |
| [`s2-t6-bme280-measure`](sprint-02/s2-t6-bme280-measure.md) | BME280 measure | L |  |
| [`s2-t7-bme280-address-config`](sprint-02/s2-t7-bme280-address-config.md) | BME280 address config | S |  |
| [`s2-t8-sensor-interface`](sprint-02/s2-t8-sensor-interface.md) | Sensor interface | S |  |
| [`s2-t9-i2c-error-bounded`](sprint-02/s2-t9-i2c-error-bounded.md) | I2C error bounded | S | yes |
| [`s2-t10-ssd1306-init`](sprint-02/s2-t10-ssd1306-init.md) | SSD1306 init | M |  |
| [`s2-t11-ssd1306-text`](sprint-02/s2-t11-ssd1306-text.md) | SSD1306 text | M |  |
| [`s2-t12-oled-layout`](sprint-02/s2-t12-oled-layout.md) | OLED layout | S |  |
| [`s2-t13-status-led-driver`](sprint-02/s2-t13-status-led-driver.md) | Status LED driver | S | yes |
| [`s2-t14-button-bounce-measure`](sprint-02/s2-t14-button-bounce-measure.md) | Button bounce measure | M | yes |
| [`s2-t15-bringup-loop`](sprint-02/s2-t15-bringup-loop.md) | Bring-up loop | S |  |
| [`s2-t16-wiring-doc`](sprint-02/s2-t16-wiring-doc.md) | Wiring doc | S |  |

## Sprint 3: RTOS Core and Sensing Pipeline (16 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s3-t1-event-bits-and-handles`](sprint-03/s3-t1-event-bits-and-handles.md) | Event bits and handles | S |  |
| [`s3-t2-create-shared-objects`](sprint-03/s3-t2-create-shared-objects.md) | Create shared objects | M |  |
| [`s3-t3-latest-struct`](sprint-03/s3-t3-latest-struct.md) | Latest struct | S |  |
| [`s3-t4-create-tasks`](sprint-03/s3-t4-create-tasks.md) | Create tasks | M |  |
| [`s3-t5-sensor-task-period`](sprint-03/s3-t5-sensor-task-period.md) | Sensor task period | S |  |
| [`s3-t6-sensor-task-i2c-mutex`](sprint-03/s3-t6-sensor-task-i2c-mutex.md) | Sensor task I2C mutex | M |  |
| [`s3-t7-sensor-task-retry`](sprint-03/s3-t7-sensor-task-retry.md) | Sensor task retry | S |  |
| [`s3-t8-sensor-task-enqueue`](sprint-03/s3-t8-sensor-task-enqueue.md) | Sensor task enqueue | S |  |
| [`s3-t9-process-task-validate`](sprint-03/s3-t9-process-task-validate.md) | Process task validate | M |  |
| [`s3-t10-process-task-filter`](sprint-03/s3-t10-process-task-filter.md) | Process task filter | S |  |
| [`s3-t11-process-task-publish-queue`](sprint-03/s3-t11-process-task-publish-queue.md) | Process task publish queue | M |  |
| [`s3-t12-monitor-task-stub`](sprint-03/s3-t12-monitor-task-stub.md) | Monitor task stub | S |  |
| [`s3-t13-stack-hwm-logging`](sprint-03/s3-t13-stack-hwm-logging.md) | Stack high-water-mark logging | S |  |
| [`s3-t14-sample-logging`](sprint-03/s3-t14-sample-logging.md) | Sample logging | S |  |
| [`s3-t15-hw-cadence-check`](sprint-03/s3-t15-hw-cadence-check.md) | Hardware cadence check | S | yes |
| [`s3-t16-keep-gates-green`](sprint-03/s3-t16-keep-gates-green.md) | Keep gates green | S |  |

## Sprint 4: Display and Button (10 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s4-t1-button-isr`](sprint-04/s4-t1-button-isr.md) | Button ISR | M |  |
| [`s4-t2-debounce`](sprint-04/s4-t2-debounce.md) | Debounce | S |  |
| [`s4-t3-display-task-loop`](sprint-04/s4-t3-display-task-loop.md) | Display task loop | S |  |
| [`s4-t4-display-task-draw-locking`](sprint-04/s4-t4-display-task-draw-locking.md) | Display task draw locking | M |  |
| [`s4-t5-unit-toggle`](sprint-04/s4-t5-unit-toggle.md) | Unit toggle | S |  |
| [`s4-t6-render-values`](sprint-04/s4-t6-render-values.md) | Render values | M |  |
| [`s4-t7-render-link-status`](sprint-04/s4-t7-render-link-status.md) | Render link status | S |  |
| [`s4-t8-measure-button-response`](sprint-04/s4-t8-measure-button-response.md) | Measure button response | M | yes |
| [`s4-t9-measure-display-latency`](sprint-04/s4-t9-measure-display-latency.md) | Measure display latency | S | yes |
| [`s4-t10-i2c-contention-test`](sprint-04/s4-t10-i2c-contention-test.md) | I2C contention test | M | yes |

## Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration) (14 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s5-t1-kconfig-network-options`](sprint-05/s5-t1-kconfig-network-options.md) | Kconfig network options | S |  |
| [`s5-t2-local-broker`](sprint-05/s5-t2-local-broker.md) | Local broker | S |  |
| [`s5-t3-nvs-config`](sprint-05/s5-t3-nvs-config.md) | NVS config | S |  |
| [`s5-t4-wifi-station`](sprint-05/s5-t4-wifi-station.md) | Wi-Fi station | M |  |
| [`s5-t5-wifi-backoff`](sprint-05/s5-t5-wifi-backoff.md) | Wi-Fi backoff | S |  |
| [`s5-t6-sntp-time`](sprint-05/s5-t6-sntp-time.md) | SNTP time | M |  |
| [`s5-t7-mqtt-client`](sprint-05/s5-t7-mqtt-client.md) | MQTT client | M |  |
| [`s5-t8-json-payload`](sprint-05/s5-t8-json-payload.md) | JSON payload | S |  |
| [`s5-t9-comms-task`](sprint-05/s5-t9-comms-task.md) | Comms task | L |  |
| [`s5-t10-outage-buffering`](sprint-05/s5-t10-outage-buffering.md) | Outage buffering | M |  |
| [`s5-t11-measure-publish-cadence`](sprint-05/s5-t11-measure-publish-cadence.md) | Measure publish cadence | S | yes |
| [`s5-t12-network-outage-test`](sprint-05/s5-t12-network-outage-test.md) | Network outage test | M | yes |
| [`s5-t13-credential-hygiene`](sprint-05/s5-t13-credential-hygiene.md) | Credential hygiene | S |  |
| [`s5-t14-comms-stack-check`](sprint-05/s5-t14-comms-stack-check.md) | Comms stack check | S |  |

## Sprint 6: Reliability (Monitor, Recovery, Watchdog, Heap, LED) (12 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s6-t1-monitor-task-full`](sprint-06/s6-t1-monitor-task-full.md) | Monitor task full | M |  |
| [`s6-t2-error-dispatch`](sprint-06/s6-t2-error-dispatch.md) | Error dispatch | S |  |
| [`s6-t3-sensor-recovery`](sprint-06/s6-t3-sensor-recovery.md) | Sensor recovery | L |  |
| [`s6-t4-restart-after-failed-recoveries`](sprint-06/s6-t4-restart-after-failed-recoveries.md) | Restart after failed recoveries | M |  |
| [`s6-t5-validation-faults-feed-policy`](sprint-06/s6-t5-validation-faults-feed-policy.md) | Validation faults feed policy | S |  |
| [`s6-t6-status-led-states`](sprint-06/s6-t6-status-led-states.md) | Status LED states | M |  |
| [`s6-t7-task-watchdog`](sprint-06/s6-t7-task-watchdog.md) | Task watchdog | M |  |
| [`s6-t8-heap-monitor`](sprint-06/s6-t8-heap-monitor.md) | Heap monitor | M |  |
| [`s6-t9-reset-reason-logging`](sprint-06/s6-t9-reset-reason-logging.md) | Reset reason logging | S |  |
| [`s6-t10-drop-counters`](sprint-06/s6-t10-drop-counters.md) | Drop counters | S |  |
| [`s6-t11-fault-injection-hooks`](sprint-06/s6-t11-fault-injection-hooks.md) | Fault-injection hooks | L |  |
| [`s6-t12-keep-gates-green`](sprint-06/s6-t12-keep-gates-green.md) | Keep gates green | S |  |

## Sprint 7: Verification and Measurement (15 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s7-t1-measure-sampling-jitter`](sprint-07/s7-t1-measure-sampling-jitter.md) | Measure sampling jitter | M | yes |
| [`s7-t2-measure-display-latency`](sprint-07/s7-t2-measure-display-latency.md) | Measure display latency | S | yes |
| [`s7-t3-measure-refresh-and-button`](sprint-07/s7-t3-measure-refresh-and-button.md) | Measure refresh and button | S | yes |
| [`s7-t4-measure-publish-interval`](sprint-07/s7-t4-measure-publish-interval.md) | Measure publish interval | S | yes |
| [`s7-t5-verify-mutex-timeout`](sprint-07/s7-t5-verify-mutex-timeout.md) | Verify mutex timeout | S | yes |
| [`s7-t6-verify-backoff`](sprint-07/s7-t6-verify-backoff.md) | Verify backoff | S | yes |
| [`s7-t7-verify-recovery-counts`](sprint-07/s7-t7-verify-recovery-counts.md) | Verify recovery counts | S | yes |
| [`s7-t8-verify-watchdog`](sprint-07/s7-t8-verify-watchdog.md) | Verify watchdog | S | yes |
| [`s7-t9-verify-tick-rate`](sprint-07/s7-t9-verify-tick-rate.md) | Verify tick rate | S |  |
| [`s7-t10-fault-injection-matrix`](sprint-07/s7-t10-fault-injection-matrix.md) | Fault-injection matrix | L | yes |
| [`s7-t11-stack-hwm-final`](sprint-07/s7-t11-stack-hwm-final.md) | Stack high-water marks, final | M | yes |
| [`s7-t12-priority-inversion-experiment`](sprint-07/s7-t12-priority-inversion-experiment.md) | Priority-inversion experiment | M |  |
| [`s7-t13-soak-24h`](sprint-07/s7-t13-soak-24h.md) | Soak 24 h | L | yes |
| [`s7-t14-no-alloc-audit`](sprint-07/s7-t14-no-alloc-audit.md) | No-allocation audit | M |  |
| [`s7-t15-final-gates-run`](sprint-07/s7-t15-final-gates-run.md) | Final gates run | S |  |

## Sprint 8: Documentation, Demo and Acceptance (10 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s8-t1-wiring-diagram`](sprint-08/s8-t1-wiring-diagram.md) | Wiring diagram | S |  |
| [`s8-t2-task-comm-diagram`](sprint-08/s8-t2-task-comm-diagram.md) | Task and communication diagram | M |  |
| [`s8-t3-stack-table`](sprint-08/s8-t3-stack-table.md) | Stack table | S |  |
| [`s8-t4-collect-test-evidence`](sprint-08/s8-t4-collect-test-evidence.md) | Collect test evidence | M |  |
| [`s8-t5-demo-media`](sprint-08/s8-t5-demo-media.md) | Demo media | M |  |
| [`s8-t6-reflection-notes`](sprint-08/s8-t6-reflection-notes.md) | Reflection notes | M |  |
| [`s8-t7-source-review`](sprint-08/s8-t7-source-review.md) | Source review | M |  |
| [`s8-t8-acceptance-walkthrough`](sprint-08/s8-t8-acceptance-walkthrough.md) | Acceptance walkthrough | M |  |
| [`s8-t9-finalise-docs-status`](sprint-08/s8-t9-finalise-docs-status.md) | Finalise docs status | S |  |
| [`s8-t10-tag-release`](sprint-08/s8-t10-tag-release.md) | Tag release | S |  |

## Sprint 9: Backlog (Stretch Goals) (4 tasks)

| Task | Title | Effort | HW |
|------|-------|:------:|:--:|
| [`s9-t1-dht22-comparison`](sprint-09/s9-t1-dht22-comparison.md) | DHT22 comparison | L |  |
| [`s9-t2-sleep-and-current`](sprint-09/s9-t2-sleep-and-current.md) | Sleep and current | L |  |
| [`s9-t3-ble-or-http-dashboard`](sprint-09/s9-t3-ble-or-http-dashboard.md) | BLE or HTTP dashboard | L |  |
| [`s9-t4-stm32-port`](sprint-09/s9-t4-stm32-port.md) | STM32 port | L |  |
