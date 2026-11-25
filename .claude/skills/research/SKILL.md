---
name: research
description: Run a research task on ESP-IDF, FreeRTOS, sensor/display drivers, MQTT or host-test tooling
argument-hint: <prompt-name>
---

## Task

Execute research task: `$ARGUMENTS`

---

### Instructions

1. If no argument is provided, return error: `"Usage: /research <prompt-name>"`
2. Look for research prompt file at `context/research/{$ARGUMENTS}.md`
3. If not found, return error: `"Prompt file not found at context/research/{$ARGUMENTS}.md"`
4. Read the research prompt file, which defines:
   - **Output**: Target documentation file (for example `docs/i2c-master-notes.md` or `context/specs/mqtt-topic-spec.md`)
   - **Research Scope**: ESP-IDF v5.x APIs (I2C master driver, GPIO ISR service, Wi-Fi, `esp-mqtt`, NVS, task watchdog), FreeRTOS behaviour (queues, mutexes and priority inheritance, event groups, `vTaskDelayUntil`, stack high-water marks), the BME280 and SSD1306 datasheets, or the Docker test container and Makefile
   - **Include**: Function signatures, config options (`menuconfig` / `sdkconfig` symbols), error codes, timing and memory costs, minimal compilable examples
   - **Sources**: Official Espressif and FreeRTOS documentation, datasheets, the ESP-IDF headers in the pinned `espressif/idf:v5.5.6` image
5. Execute the research:
   - Read the official docs for the exact API behaviour, and check headers in the container when the docs are unclear
   - Search the codebase for existing code that uses the API, and for config constants in `main/app_config.h`
   - Note the ESP-IDF version (v5.5.6) so the findings can be dated
6. Write structured findings to the specified output location
7. Provide a concise summary of the findings

---

### Rules

- This command produces **DOCUMENTATION ONLY**
- Do NOT modify source code files
- Do NOT create branches or commits
- Output documents should be written to `docs/` or `context/`
- Cite the documentation source, version and date for every behaviour claim
- Do not claim hardware behaviour is verified from documentation or a container build
- Never put Wi-Fi credentials, broker URLs or device IDs in research output
