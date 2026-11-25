---
name: list-components
description: List the modules and components of the RTOS weather station
argument-hint: [layer-or-subdirectory]
---

## Task

List all modules, source files and tasks across the layers of the weather station. Follow `context/project-structure.md` for the layout and check which files actually exist, since many are only `[planned]`. The layers are:

- **Pure logic (`components/app_logic/`)**: validation, smoothing, dew point, formatting and other decisions. Pure C, no ESP-IDF or FreeRTOS includes.
- **Firmware tasks (`main/`)**: `monitor_task` (6), `sensor_task` (5), `process_task` (4), `display_task` (3), `comms_task` (3), and `main.c` startup that creates every queue, mutex, semaphore, event group and task.
- **Shared objects**: queues `raw_queue`, `publish_queue`, `error_queue`; mutexes `i2c_mutex`, `data_mutex`; semaphore `button_sem`; event group `sys_events`.
- **Drivers and interrupts**: BME280 over I2C, SSD1306 OLED, button ISR (GPIO4), status LED (GPIO2), Wi-Fi and MQTT.
- **Configuration**: `main/app_config.h`, `main/Kconfig.projbuild`, `sdkconfig.defaults`, root and `main/` `CMakeLists.txt`.
- **Build and test**: `Dockerfile.test`, `Makefile`, `test/host/test_*.c`.

If a `[layer-or-subdirectory]` argument is provided via `$ARGUMENTS`, only list files within that layer or directory.

## Output Format

- Numbered list of modules and source files with relative paths, tagged `[exists]` or `[planned]`.
- Brief one-line description of each component's responsibility.
- Layer mapping and the data direction between layers (for example `sensor_task -> raw_queue -> process_task -> app_logic`, `process_task -> data_mutex/latest -> display_task`, faults -> `error_queue -> monitor_task`).
- Summary count at the end.

If no components are found, output: "No weather station components found."
