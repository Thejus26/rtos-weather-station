# AGENTS.md

Guidance for AI coding agents working in this repository.

## Project

RTOS weather station on an **ESP32 (ESP32-DevKitC)** using **ESP-IDF v5.x** and **FreeRTOS** (not the Arduino framework). It samples temperature and humidity from a BME280, validates and smooths the readings, shows them on an SSD1306 OLED, and publishes JSON over Wi-Fi via MQTT. The goal is to practise RTOS design: tasks, queues, mutexes, semaphores, event groups, timing and fault handling.

**Status: not started.** The repository currently holds only documentation. No source code, Dockerfile or Makefile exists yet.

## Read these first

| File | Contents |
|------|----------|
| `context/project-overview.md` | Full specification: FR-1 to FR-10, hardware and wiring, task and queue tables, timing, error handling, Docker workflow, deliverables, acceptance criteria. This is the source of truth. |
| `context/project-structure.md` | Current and target file layout, with `[exists]`/`[planned]` tags. |
| `README.md` | Mirror of the overview, plus Status and Notes sections. |

If the code and the specification disagree, ask before changing either.

## Key design facts

- **Tasks (priority):** `monitor_task` 6, `sensor_task` 5, `process_task` 4, `display_task` 3, `comms_task` 3. The button ISR is not a task. It gives `button_sem` with `xSemaphoreGiveFromISR`.
- **Shared objects:** queues `raw_queue` (8), `publish_queue` (10, drop oldest when full), `error_queue` (8, senders never block); mutexes `i2c_mutex` and `data_mutex`; binary semaphore `button_sem`; event group `sys_events` (`WIFI_CONNECTED`, `MQTT_CONNECTED`, `SENSOR_OK`).
- **Pins:** I2C SDA GPIO21, SCL GPIO22, button GPIO4 (pull-up, falling edge), status LED GPIO2. I2C addresses: BME280 `0x76`/`0x77`, OLED `0x3C`.
- **Timing:** sample every 5 s with `vTaskDelayUntil` (jitter under ±50 ms), display refresh 1 s, MQTT publish every 30 s, FreeRTOS tick 1000 Hz, task watchdog 10 s.

## Rules

- **Mutexes:** keep hold times short, never hold two at once. If unavoidable, take `i2c_mutex` before `data_mutex`.
- **ISRs:** use `FromISR` APIs only inside the ISR, and never in tasks.
- **Memory:** no dynamic allocation in steady state. Create queues, mutexes and tasks at startup.
- **Secrets:** never hard-code Wi-Fi credentials, broker URLs or device IDs. Use `menuconfig`/NVS. Do not commit `sdkconfig`; keep shared defaults in `sdkconfig.defaults`.
- **Fault handling:** the system must keep sampling and displaying when Wi-Fi or the broker is down. Errors go to `error_queue` with a zero timeout.
- **`components/app_logic/` must stay pure C** with no ESP-IDF or FreeRTOS includes, so it builds in the host test container. Put decisions there, and keep task code thin.
- **Task stacks:** each must keep at least 25% headroom (no more than 75% used).
- Do not claim hardware behaviour (timing, stack use, I2C, Wi-Fi) is verified from host tests. Those need the real board.

## Build and test

Planned workflow (files are not created yet; see `context/project-overview.md`, section "Build and Test with Docker"):

```
# host unit tests in the lightweight container (Alpine + GCC, ~230 MB)
docker build -f Dockerfile.test -t rtos-host-test .
docker run --rm --memory 256m --cpus 1 -v "${PWD}:/work" rtos-host-test make test
make docker-test                      # wrapper for the line above

# firmware (ESP-IDF toolchain: espressif/idf:v5.5.6 container, run with --memory 2g --cpus 2)
idf.py set-target esp32
idf.py build
idf.py -p COMx flash monitor          # flash from the host, not from Docker
```

- Run host tests before building firmware. They must pass with `-Wall -Wextra -Werror`.
- On Windows, bind mounts can fail in Git Bash because of path translation. Use PowerShell, or set `MSYS_NO_PATHCONV=1`.
- Only `components/app_logic/` and `test/host/` build in the test container. `main/` needs ESP-IDF.
- The test container approach was checked with a sample function. The `espressif/idf:v5.5.6` image was pulled and measures 9.22 GB on disk; `idf.py --version` in it prints `ESP-IDF v5.5.6`.

## Conventions

- Language: C (ESP-IDF, CMake). Follow ESP-IDF naming: `snake_case`, a module prefix on public functions, and `esp_err_t` return codes.
- Keep pins, periods, priorities and queue sizes in `main/app_config.h`, not scattered in code.
- When you add, move or remove files, update `context/project-structure.md` in the same change.
- When you change the specification, update `context/project-overview.md` and `README.md` together. They are kept in sync by hand. The only intended difference is the `03-iot-devices` link path and the README's Status and Notes sections.
- Use `README.md` Notes for reflections (priority inversion, stack sizing, STM32 porting).
