# 01-rtos-based-applications

# RTOS Weather Station: Project Specification

## Overview

A multi-task weather station that samples temperature and humidity, filters the readings, shows them on a local OLED, and publishes them over Wi-Fi via MQTT. It runs on **FreeRTOS** (via ESP-IDF) on an **ESP32**. The point of the project is to practise real RTOS design: tasks, queues, mutexes, semaphores, event groups, timing and fault handling.

**Level:** Intermediate. **Status:** Not started.

**Platform decision:** ESP32 DevKitC with ESP-IDF v5.x and FreeRTOS (justification in [Platform Selection](#platform-selection-esp32-vs-stm32)).

**Build and test workflow:** Docker-based, split into two tiers (details in [Build and Test with Docker](#build-and-test-with-docker)).
- **Tier 1, host build and unit tests (lightweight):** a small Alpine + GCC container (~230 MB) compiles the hardware-independent C logic (moving average, validation, dew point) and runs its unit tests on the development machine. It needs no ESP32 and no ESP-IDF, and runs comfortably within 256 MB of RAM and one CPU.
- **Tier 2, firmware build (heavy, on demand):** the ESP32 cross-compile uses the official `espressif/idf:v5.5.6` image (no native ESP-IDF install). It is about 9 GB on disk and is only needed to produce `weather_station.bin`.
- **On hardware only:** flashing, I2C/OLED, Wi-Fi/MQTT, timing jitter, stack high-water marks, fault injection and the 24-hour soak test. Docker cannot replace the device for these.

## Objectives

### Goals
1. Design and implement a multi-task FreeRTOS application with clean task boundaries.
2. Use queues, mutexes, binary semaphores and event groups, each for the problem it suits.
3. Meet defined timing requirements using `vTaskDelayUntil` and measure them.
4. Handle sensor, network and resource faults without hanging the system.

### Functional Requirements

| ID | Requirement |
|----|-------------|
| FR-1 | Sample temperature (°C) and relative humidity (%RH) every 5 s. |
| FR-2 | Validate samples (range and rate-of-change checks) and smooth them with a 5-sample moving average. |
| FR-3 | Calculate dew point from the filtered values. |
| FR-4 | Show temperature, humidity, dew point and Wi-Fi/MQTT status on a 128×64 OLED, refreshed every 1 s. |
| FR-5 | A push button toggles °C/°F on the display. It uses an ISR and signals the task with a semaphore. |
| FR-6 | Publish JSON readings to an MQTT broker every 30 s, with a timestamp (SNTP) and a device ID. |
| FR-7 | Keep operating (sample and display) when Wi-Fi or the broker is down. Reconnect with exponential backoff (1 s to 60 s). |
| FR-8 | Detect sensor failures (I2C error or out-of-range value), report them, and recover by re-initialising the sensor. |
| FR-9 | Run a task watchdog and a heap monitor. A status LED shows system state. |
| FR-10 | Store configuration (Wi-Fi credentials, broker URL, intervals) in `menuconfig`/NVS, not in code. |

### Non-Functional Requirements
- No dynamic allocation in steady state (queues, mutexes and tasks are created at startup).
- Every task has a measured stack high-water mark with at least 25% headroom.
- Continuous run of 24 hours without a reset or heap growth.
- Signal-processing logic (validation, moving average, dew point) is pure C with no ESP-IDF or FreeRTOS includes, so it builds and is tested on the host inside the Docker test container.

## Hardware

| Component | Choice | Notes |
|-----------|--------|-------|
| MCU board | ESP32-DevKitC (ESP32-WROOM-32E) | Dual-core, 4 MB flash, built-in Wi-Fi/BLE. |
| Temp/humidity sensor | **BME280** (I2C, addr `0x76`/`0x77`) | Temperature ±1 °C, humidity ±3 %RH, plus pressure for later extension. |
| Alternates | SHT31 (I2C, more accurate humidity), DHT22 (1-Wire, slow and timing-sensitive) | Use DHT22 only as a stretch exercise to compare against I2C. |
| Display | SSD1306 128×64 OLED (I2C, addr `0x3C`) | Shares the I2C bus with the sensor. This makes the mutex necessary. |
| Input | Tactile push button | GPIO4, internal pull-up, falling-edge interrupt. |
| Indicator | LED + 330 Ω resistor | GPIO2 (or the onboard LED). |
| Power | USB 5 V (development) | Optional: 18650 + regulator for the power-profiling stretch goal. |
| Misc | Breadboard, jumper wires, 4.7 kΩ I2C pull-ups if the breakouts lack them | |

**Wiring**

| Signal | ESP32 pin |
|--------|-----------|
| I2C SDA (BME280, OLED) | GPIO21 |
| I2C SCL (BME280, OLED) | GPIO22 |
| Button | GPIO4 → GND |
| Status LED | GPIO2 |
| Power | 3.3 V / GND |

### Platform Selection: ESP32 vs STM32

| Criterion | ESP32 (ESP-IDF) | STM32 (e.g. F411/L476, HAL + CubeMX) |
|-----------|-----------------|--------------------------------------|
| **RTOS support** | FreeRTOS is built into ESP-IDF and always on, with SMP support for dual cores. Tasks, queues and event groups work immediately. | FreeRTOS is available through CubeMX (CMSIS-RTOS v2 wrapper) and needs manual setup. Heap, tick and priority configuration is the user's job. |
| **Learning value (RTOS)** | High. Dual-core scheduling, task pinning, event groups and the task watchdog are all available. Real-world patterns (Wi-Fi events, esp_timer) are integrated. | High for fundamentals (priorities, tick config, ISR-safe APIs, HAL interaction). More hands-on with hardware, but the CMSIS wrapper hides some native FreeRTOS APIs. |
| **Sensor interfacing** | Two I2C and four SPI controllers, RMT for 1-Wire/DHT22. Pins are freely mappable via the GPIO matrix. | I2C, SPI and GPIO available. Pins are fixed per alternate function. Bit-banging 1-Wire requires a timer setup. |
| **Connectivity** | Built-in Wi-Fi and BLE. MQTT, SNTP and TLS come with ESP-IDF. | No radio. Needs an external module (ESP-01 AT, WINC1500, W5500 Ethernet), which adds a driver layer and a new failure surface. |
| **Power** | Higher active (~80–240 mA with Wi-Fi). Good deep and light sleep modes, but Wi-Fi dominates. | Lower active and much lower sleep power (e.g. L4 series). Better for battery-first designs, but only once a radio is added. |
| **Toolchain** | ESP-IDF + CMake + `idf.py`, VS Code extension. Setup is easy; the framework is large. | STM32CubeIDE/CubeMX, GCC and OpenOCD/ST-Link. Generated code and regeneration conflicts are common pain points. |
| **Cost** | ~$5–10 for a DevKit. USB and programmer included. | ~$15–25 for a Nucleo (ST-Link included) plus ~$5–10 for a Wi-Fi/Ethernet module. |
| **Community resources** | Very large: Espressif docs, examples, forums, many weather-station and MQTT tutorials. | Large and professional: ST docs, CubeMX examples. Fewer end-to-end IoT examples for this use case. |

**Recommendation: ESP32 with ESP-IDF (not the Arduino framework).**

1. **Connectivity is the deciding factor.** The weather station needs Wi-Fi/MQTT. On ESP32 that is built in. On STM32 it would add an external module and an AT-command or driver layer that has nothing to do with learning RTOS.
2. **FreeRTOS is the native environment.** Tasks, queues, mutexes, event groups and the task watchdog are used directly, with the full native API.
3. **Cost and setup.** A cheaper board with USB flashing and one install gives a faster path to a working multi-task system.
4. **Concurrency is realistic.** The Wi-Fi stack runs its own tasks, so priority and stack decisions matter in practice.

Trade-offs accepted: higher power draw, and a large framework that hides some hardware detail. **When STM32 would be better:** a battery-first, offline, or hard-real-time design, or when the goal is to learn bare-metal peripherals and HAL. A natural follow-up is to port this project to STM32 (see [03-iot-devices](../../03-iot-devices)).

## Software Architecture (RTOS tasks)

### Task Breakdown

| Task | Priority | Stack | Period / trigger | Responsibility |
|------|----------|-------|------------------|----------------|
| `monitor_task` (error handling) | 6 (highest) | 3 KB | Blocks on `error_queue`, plus 10 s housekeeping | Logs errors, drives the status LED, feeds the task watchdog, checks heap, restarts the sensor after repeated failures, calls `esp_restart()` on unrecoverable faults. |
| `sensor_task` (sampling) | 5 | 4 KB | Every 5 s, `vTaskDelayUntil` | Takes `i2c_mutex`, triggers a BME280 forced-mode read, releases the mutex, and sends `sample_t` to `raw_queue`. Reports faults to `error_queue`. |
| `process_task` (data processing) | 4 | 3 KB | Blocks on `raw_queue` | Validates samples, applies the moving average, calculates dew point, updates the shared `latest` struct under `data_mutex`, and enqueues a reading to `publish_queue` every 30 s. |
| `display_task` (display) | 3 | 3 KB | Takes `button_sem` with a 1 s timeout | Refreshes the OLED each second or immediately after a button press. Copies `latest` under `data_mutex`, then takes `i2c_mutex` to draw. |
| `comms_task` (communication) | 3 | 6 KB | Waits on `WIFI_CONNECTED_BIT` | Runs the Wi-Fi/MQTT/SNTP lifecycle and publishes from `publish_queue`. Reconnects with backoff. |

The button ISR is not a task. It calls `xSemaphoreGiveFromISR(button_sem)`.

Priorities follow the rule that tasks needing the most predictable timing and the fault monitor rank above tasks that can tolerate delay. Display and comms are lowest because a late frame or publish does not lose data.

### Inter-task Communication

| Object | Type | Size / depth | Producer → Consumer | Purpose |
|--------|------|--------------|---------------------|---------|
| `raw_queue` | Queue of `sample_t` | 8 | `sensor_task` → `process_task` | Decouples sampling from processing. |
| `publish_queue` | Queue of `reading_t` | 10 | `process_task` → `comms_task` | Buffers readings during network outages. When full, the oldest entry is dropped. |
| `error_queue` | Queue of `error_event_t` | 8 | All tasks → `monitor_task` | Central fault reporting. Senders never block (timeout 0). |
| `i2c_mutex` | Mutex | n/a | `sensor_task`, `display_task` | Serialises access to the shared I2C bus. Priority inheritance prevents priority inversion. |
| `data_mutex` | Mutex | n/a | `process_task`, `display_task` | Protects the shared `latest` struct. |
| `button_sem` | Binary semaphore | n/a | Button ISR → `display_task` | Signals a button press (ISR to task, with debounce). |
| `sys_events` | Event group | 3 bits | `comms_task`, `sensor_task` → `display_task`, `monitor_task` | `WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK`. Used for status display and gating. |

**Rules:** keep mutex hold times short (microseconds to a few milliseconds), never hold two mutexes at once (avoids deadlock; if unavoidable, always take `i2c_mutex` before `data_mutex`), and use `FromISR` APIs only inside the ISR.

### Timing Requirements

| Item | Requirement |
|------|-------------|
| Sampling period | 5 s, jitter under ±50 ms (`vTaskDelayUntil`). |
| Sample-to-display latency | Under 1.5 s from a sensor read to updated OLED. |
| Display refresh | 1 s. Button response within 200 ms. |
| MQTT publish | Every 30 s, tolerance ±1 s when connected. |
| I2C mutex wait | Timeout 100 ms, and a timeout is reported as an error. |
| Wi-Fi reconnect backoff | 1 s, doubling up to 60 s. |
| Fault recovery | Sensor re-initialisation after 3 consecutive failures. Restart after 10 failed recoveries. |
| Task watchdog | 10 s timeout on `sensor_task`, `process_task` and `monitor_task`. |
| FreeRTOS tick | 1000 Hz (1 ms). |

### Error Handling

| Fault | Detection | Response |
|-------|-----------|----------|
| I2C read failure or timeout | `esp_err_t` return | Retry up to 3 times, then report to `error_queue`, clear `SENSOR_OK`, re-initialise the sensor. |
| Out-of-range value | Temperature −40 to 85 °C, humidity 0–100 %, or a jump of more than 10 °C between samples | Discard the sample and count it as a fault. |
| Wi-Fi/MQTT loss | Event handler | Keep sampling and displaying, buffer readings, and reconnect with backoff. |
| Queue full | `xQueueSend` timeout | Drop the oldest, count the drop, and log it. |
| Task hang | Task watchdog | Log the cause and restart. |
| Low heap | Heap monitor below the threshold (for example 20 KB) | Log a warning, and restart if it continues to fall. |

### Suggested Project Layout

```
01-rtos-based-applications/
├── CMakeLists.txt
├── sdkconfig.defaults
├── Dockerfile.test         # lightweight host build/test image (Alpine + GCC)
├── .dockerignore           # excludes build/, managed_components/, sdkconfig
├── Makefile                # `make test` (host) and `make docker-test` (in container)
├── main/
│   ├── main.c              # creates queues, mutexes, tasks
│   ├── app_config.h        # pins, periods, priorities, queue sizes
│   ├── Kconfig.projbuild   # "Weather Station" menuconfig menu: periods, device ID, BME280 address
│   ├── tasks/              # sensor, process, display, comms, monitor
│   └── drivers/            # bme280, ssd1306 wrappers
├── components/
│   └── app_logic/          # pure C, no ESP-IDF includes: moving_average, validate, dew_point
├── test/
│   └── host/               # host unit tests for app_logic, built by the Makefile
└── docs/                   # wiring diagram, task diagram, test results
```

Only `components/app_logic/` and `test/host/` are compiled in the test container. The tasks and drivers depend on FreeRTOS and ESP-IDF headers, so they are built only by the firmware toolchain.

## Build and Test with Docker

### What runs where

| Activity | Where | Why |
|----------|-------|-----|
| Compile and unit-test `app_logic` (moving average, validation, dew point) | **Test container** (Alpine + GCC, ~230 MB) | Pure C, needs only `gcc`, `make` and `libm`. Fast and reproducible. |
| Static checks and warnings (`-Wall -Wextra -Werror`, optional `cppcheck`) | **Test container** | Same toolchain on every machine and in CI. |
| Cross-compile the ESP32 firmware | `espressif/idf:v5.5.6` container | Needs the Xtensa toolchain and ESP-IDF, which is about 9 GB on disk. Not part of the lightweight workflow. |
| Flash and monitor | Host machine (`idf.py -p COMx flash monitor`) | USB serial passthrough from Docker on Windows is unreliable. Flash from the host. |
| Timing jitter, stack high-water marks, I2C/OLED, Wi-Fi/MQTT, fault injection, 24 h soak | Real ESP32 | These depend on real hardware and the real FreeRTOS scheduler. |

The test container was checked with a sample dew-point function and test: the image builds to about 231 MB (an earlier check measured about 282 MB) and the test compiles with `-Wall -Wextra -Werror` and passes under `--memory 256m --cpus 1`. The `espressif/idf:v5.5.6` image was pulled and measures 9.22 GB on disk (about 5 GB compressed); `idf.py --version` in it prints `ESP-IDF v5.5.6`. A firmware build in it has not been run yet.

### Test image

`Dockerfile.test`:

```dockerfile
FROM alpine:3.20
RUN apk add --no-cache build-base make
WORKDIR /work
```

The source tree is bind-mounted, not copied, so there is no rebuild of the image when code changes. Rebuild the image only when the toolchain changes.

### Commands

```
# one-time: build the image
docker build -f Dockerfile.test -t rtos-host-test .

# build and run the host unit tests with a small resource cap
docker run --rm --memory 256m --cpus 1 -v "${PWD}:/work" rtos-host-test make test

# or via the Makefile wrapper
make docker-test
```

Run these from the project root (PowerShell or a Linux/macOS shell). In Git Bash on Windows, bind-mount paths can fail to translate: use PowerShell, or set `MSYS_NO_PATHCONV=1`.

`make test` compiles every file in `test/host/` together with `components/app_logic/*.c`, using `-Wall -Wextra -Werror -lm`, runs the binary, and exits non-zero on any failed assertion, so it works as a CI step.

### Optional: firmware build in the official ESP-IDF image

```
docker run --rm --memory 2g --cpus 2 -v "${PWD}:/project" -w /project espressif/idf:v5.5.6 idf.py set-target esp32 build
```

The project is pinned to `espressif/idf:v5.5.6` (ESP-IDF v5.5.6); never use `latest`. Always run it with `--memory 2g --cpus 2` so a build cannot starve the laptop (the Docker VM is also capped at 3 GB and 2 CPUs in `~/.wslconfig`). This produces the `.bin` files in `build/`. Flash them from the host with `idf.py -p COMx flash monitor` (or `esptool.py`). Expect a multi-GB image and a slower first build. A native ESP-IDF install is not used in this project.

### Limits of this approach

- Host tests prove the logic is correct. They do not prove task timing, priorities, stack sizes or I2C behaviour. Those are verified on the board (see Deliverables).
- Task code that calls FreeRTOS or ESP-IDF APIs is not covered by the lightweight container. Keep that code thin and move decisions into `app_logic`.
- A FreeRTOS POSIX-port simulation of the queue and mutex logic is possible but is a stretch goal, not part of the baseline workflow.

## Setup Instructions

1. **Install Docker** (Docker Desktop or Docker Engine) and build the test image: `docker build -f Dockerfile.test -t rtos-host-test .`
2. **Get the firmware toolchain:** pull the pinned container, `docker pull espressif/idf:v5.5.6` (about 5 GB download, 9.22 GB on disk), and check it with `docker run --rm --memory 2g --cpus 2 espressif/idf:v5.5.6 idf.py --version`. Builds run in the container. A native ESP-IDF install is not used. Flashing, if a board is ever bought, needs `esptool.py` on the host.
3. **Run the host tests first:** `make docker-test`. All `app_logic` tests must pass before building firmware.
4. **Wire the hardware** as in the table above and confirm the I2C addresses with an I2C scan (expect `0x76` and `0x3C`).
5. **Get the project:** `idf.py set-target esp32`.
6. **Configure:** run `idf.py menuconfig` and set Wi-Fi SSID/password, MQTT broker URI and topic, sample and publish intervals. Enable the task watchdog and set `CONFIG_FREERTOS_HZ=1000`.
7. **Build, flash and monitor:** `idf.py build flash monitor` (add `-p COMx` on Windows if needed).
8. **Run a broker:** Mosquitto locally (`mosquitto -v`) or a public/test broker. Subscribe with `mosquitto_sub -t "weather/#" -v` to see the readings.
9. **Verify:** serial log shows the 5 s samples. The OLED updates each second. The button toggles °C/°F. Unplugging Wi-Fi does not stop sampling.
10. **Measure:** use `vTaskGetInfo`/`uxTaskGetStackHighWaterMark` for stacks, and a GPIO toggle with a logic analyser for timing jitter.

## Deliverables

1. **Source code:** ESP-IDF project with the layout above, commented, with no hard-coded credentials.
2. **Documentation (`docs/`):** wiring diagram, task and communication diagram, and a table of priorities, stack sizes and measured high-water marks.
3. **Test evidence:**
   - Unit tests for the moving-average, validation and dew-point logic, run in the Docker test container (`make docker-test`) with the passing output saved in `docs/`.
   - Fault-injection results: sensor unplugged, Wi-Fi off, broker down, queue overflow.
   - A 24-hour soak test log showing stable heap and no resets.
   - Timing measurements against the requirements table.
4. **Demo:** short video or screenshots of the OLED, serial log and MQTT subscriber output.
5. **Reflection notes (README Notes section):** priority-inversion and stack-sizing observations, plus what to change when porting to STM32.

### Acceptance Criteria
- All functional requirements FR-1 to FR-10 pass.
- All timing requirements are met in measurement.
- The system recovers from every fault in the error-handling table without manual intervention.
- No task stack above 75% usage.
- `make docker-test` passes in the lightweight container with no warnings.

### Stretch Goals
- Add the DHT22 on the RMT peripheral and compare it with the BME280.
- Add deep or light sleep between samples and measure current.
- Use BLE to serve readings, or HTTP/web dashboard.
- Port the application to STM32 with an external Wi-Fi module.
