## C Coding Standards (ESP-IDF v5.x, FreeRTOS)

Applies to every `.c` and `.h` file in `main/`, `components/` and `test/host/`. The full rules are in `context/coding-standards.md`, which is authoritative. This file is the short list to keep in mind while editing.

### Style and naming
- Language: C11, ESP-IDF naming: `snake_case`, a module prefix on public functions, `esp_err_t` return codes in firmware code.
- Pins, periods, priorities, stack sizes and queue depths live in `main/app_config.h`, not scattered in code.
- Log with `ESP_LOGx(TAG, ...)`, one `static const char *TAG` per file. No logging from ISRs.

### Layering
- `components/app_logic/` stays **pure C**: no ESP-IDF, FreeRTOS or driver includes, and its own result enum instead of `esp_err_t`. It builds and is tested in the Docker host container. Put decisions there and keep task code thin.
- Only `components/app_logic/` and `test/host/` build in the test container. `main/` needs ESP-IDF.

### RTOS rules
- **Allocation**: no `malloc`, `calloc`, `realloc` or `free` in steady state. Create queues, mutexes, the semaphore, the event group and tasks at startup.
- **ISRs**: `FromISR` APIs only inside the ISR, never in tasks. No mutex, queue wait or logging in an ISR.
- **Mutexes**: short hold times, never two at once. If unavoidable, take `i2c_mutex` before `data_mutex`. A mutex timeout is an error, reported to `error_queue`.
- **Timing**: periodic tasks use `vTaskDelayUntil`, not `vTaskDelay` or busy waits.
- **Faults**: `ESP_ERROR_CHECK` only at startup. Steady-state paths recover. Senders to `error_queue` use a zero timeout. Wi-Fi or broker loss never stops sampling or display.
- **Stacks**: each task keeps at least 25% headroom (at most 75% used).

### Secrets
- Never hard-code Wi-Fi credentials, broker URLs or device IDs. Use `menuconfig`/NVS. `sdkconfig` is git-ignored, and `sdkconfig.defaults` holds no credentials.

### Testing and claims
- Host tests: one `test/host/test_<module>.c` per module with plain `assert()`. Never define `NDEBUG`. They must pass under `-Wall -Wextra -Werror`.
- Do not claim hardware behaviour (timing, stack use, I2C, Wi-Fi) is verified from host tests or a container build. That needs the real board.

### Edit guard
- The `guard-c-code.py` hook is a text heuristic, a cheap reminder and not proof of compliance. It denies ESP-IDF or FreeRTOS includes in `components/app_logic/`. It asks for confirmation on `malloc`, `calloc`, `realloc`, `free`, `heap_caps_*`, `pvPortMalloc`, `vPortFree`, `strdup`, `strndup`, `asprintf` and `vasprintf` (other allocating APIs such as `cJSON_Print*` are not detected), on hard-coded broker URLs, and on Wi-Fi credentials written as string literals. A line that is deliberately fine can carry a `/* rule-ok: <reason> */` comment, which the hook skips (for example an allocation inside startup code).
