# Sprint 2: Hardware Bring-up and Drivers

## Goal

Make every part work on its own, outside the RTOS design. Branch: `feature/drivers`. Needs the board, sensor, OLED, LED and button.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s2-t1 · Wire circuit [HW]
- **ID:** s2-t1-wire-circuit
- **Description:** Wire the circuit: SDA to GPIO21, SCL to GPIO22 (BME280 and OLED on the same bus), button GPIO4 to GND, LED on GPIO2 with 330 ohm, 3.3 V and GND. Add 4.7 k pull-ups if the breakouts have none.
- **Acceptance criteria:**
  - Wiring matches the overview's table.
  - It was checked by eye twice before power-up.
- **Dependencies:** s0-t1-parts-and-hardware-check, s0-t11-flash-scaffold
- **Effort:** M
- **Covers:** HW-2, HW-3, HW-4, HW-5, HW-6

### s2-t2 · Choose I2C API
- **ID:** s2-t2-choose-i2c-api
- **Description:** Settle D-4: choose the I2C driver API after reading the installed ESP-IDF version's documentation.
- **Acceptance criteria:**
  - The choice is recorded with the version it was checked against.
- **Dependencies:** s0-t6-scaffold-project
- **Effort:** S
- **Covers:** HW-6

### s2-t3 · I2C bus driver
- **ID:** s2-t3-i2c-bus-driver
- **Description:** `main/drivers/i2c_bus.[ch]`: initialise the master bus on the configured pins, with finite transaction timeouts. No mutex inside the driver.
- **Acceptance criteria:**
  - The bus initialises.
  - A transaction to an absent address fails within its timeout.
- **Dependencies:** s2-t2-choose-i2c-api, s0-t9-app-config-header
- **Effort:** M
- **Covers:** HW-6, TIM-6

### s2-t4 · I2C scan [HW]
- **ID:** s2-t4-i2c-scan
- **Description:** Temporary I2C scan routine.
- **Acceptance criteria:**
  - Scan reports 0x76 (or 0x77) and 0x3C.
- **Dependencies:** s2-t1-wire-circuit, s2-t3-i2c-bus-driver
- **Effort:** S
- **Covers:** HW-2, HW-3, HW-6

### s2-t5 · BME280 init
- **ID:** s2-t5-bme280-init
- **Description:** `main/drivers/bme280.[ch]`: check chip ID, soft reset, read calibration data.
- **Acceptance criteria:**
  - Chip ID matches.
  - Calibration values are non-zero.
- **Dependencies:** s2-t4-i2c-scan
- **Effort:** M
- **Covers:** HW-2

### s2-t6 · BME280 measure
- **ID:** s2-t6-bme280-measure
- **Description:** BME280 forced-mode measurement with temperature and humidity compensation, returning `esp_err_t`. No allocation.
- **Acceptance criteria:**
  - Readings are plausible against a reference thermometer.
  - Breathing on the sensor raises humidity.
- **Dependencies:** s2-t5-bme280-init
- **Effort:** L
- **Covers:** HW-2, FR-1, NFR-1

### s2-t7 · BME280 address config
- **ID:** s2-t7-bme280-address-config
- **Description:** BME280 address selectable between 0x76 and 0x77 from Kconfig.
- **Acceptance criteria:**
  - Both addresses work when the strap is changed.
- **Dependencies:** s2-t6-bme280-measure, s0-t10-kconfig-menu
- **Effort:** S
- **Covers:** HW-2

### s2-t8 · Sensor interface
- **ID:** s2-t8-sensor-interface
- **Description:** `main/drivers/sensor.h`: a one-function `sensor_read()` interface that hides the BME280, so SHT31 or DHT22 can replace it later.
- **Acceptance criteria:**
  - Tasks call only `sensor_read()`.
- **Dependencies:** s2-t6-bme280-measure
- **Effort:** S
- **Covers:** HW-7

### s2-t9 · I2C error bounded [HW]
- **ID:** s2-t9-i2c-error-bounded
- **Description:** Unplug SDA or SCL during reads and confirm the driver returns an error within its timeout instead of hanging.
- **Acceptance criteria:**
  - An error is returned in bounded time.
  - The bus recovers when reconnected.
- **Dependencies:** s2-t6-bme280-measure
- **Effort:** S
- **Covers:** ERR-1

### s2-t10 · SSD1306 init
- **ID:** s2-t10-ssd1306-init
- **Description:** `main/drivers/ssd1306.[ch]`: init sequence for 128x64, static 1 KB framebuffer, clear and flush.
- **Acceptance criteria:**
  - The screen clears.
  - A test pattern displays.
- **Dependencies:** s2-t4-i2c-scan
- **Effort:** M
- **Covers:** HW-3, NFR-1

### s2-t11 · SSD1306 text
- **ID:** s2-t11-ssd1306-text
- **Description:** SSD1306 text drawing from a static font table, with a draw-line API.
- **Acceptance criteria:**
  - Text is readable at the chosen font size.
- **Dependencies:** s2-t10-ssd1306-init
- **Effort:** M
- **Covers:** HW-3, FR-4

### s2-t12 · OLED layout
- **ID:** s2-t12-oled-layout
- **Description:** Settle D-5. Draw a static layout with temperature, humidity, dew point, unit and a status line.
- **Acceptance criteria:**
  - The layout fits the screen with no clipping.
- **Dependencies:** s2-t11-ssd1306-text
- **Effort:** S
- **Covers:** FR-4

### s2-t13 · Status LED driver [HW]
- **ID:** s2-t13-status-led-driver
- **Description:** `main/drivers/status_led.[ch]`: on, off and toggle on GPIO2.
- **Acceptance criteria:**
  - The LED toggles from firmware.
- **Dependencies:** s2-t1-wire-circuit
- **Effort:** S
- **Covers:** HW-5

### s2-t14 · Button bounce measure [HW]
- **ID:** s2-t14-button-bounce-measure
- **Description:** Configure GPIO4 as input with pull-up and falling-edge interrupt. Log edge timestamps and measure the contact bounce duration with the logic analyser.
- **Acceptance criteria:**
  - The bounce window is measured and recorded.
  - The value is available to size the debounce in s4-t2-debounce.
- **Dependencies:** s2-t1-wire-circuit
- **Effort:** M
- **Covers:** HW-4, FR-5

### s2-t15 · Bring-up loop
- **ID:** s2-t15-bringup-loop
- **Description:** Throwaway bring-up loop in `main.c`: read the sensor, print to serial, draw on the OLED, blink the LED, count presses. Remove it (or keep it behind a Kconfig flag) before Sprint 3.
- **Acceptance criteria:**
  - All four parts work together on one bus.
- **Dependencies:** s2-t6-bme280-measure, s2-t12-oled-layout, s2-t13-status-led-driver, s2-t14-button-bounce-measure
- **Effort:** S
- **Covers:** HW-2, HW-3, HW-4, HW-5

### s2-t16 · Wiring doc
- **ID:** s2-t16-wiring-doc
- **Description:** Write `docs/wiring.md` with the wiring table, I2C addresses and a photo or diagram draft.
- **Acceptance criteria:**
  - A second person could rebuild the circuit from it.
- **Dependencies:** s2-t1-wire-circuit
- **Effort:** S
- **Covers:** DEL-2

## Definition of Done

- The I2C scan shows both devices.
- The sensor returns plausible values.
- The OLED shows text.
- The LED toggles.
- The button bounce is measured.
- Driver errors are bounded in time.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-4** (s2-t2): I2C driver API. Recommended default: the ESP-IDF v5.x `i2c_master` driver, if the installed version documents it as current. Confirm against its docs, because the legacy driver is deprecated in v5.x.
- **D-5** (s2-t12): OLED layout and font. Recommended default: four text lines (temperature, humidity, dew point, status) plus unit marker, small fixed font.
- **s2-t4:** the roadmap gives no "done when" beyond the scan result, and the scan routine is temporary. It does not say whether the routine should be deleted or kept after s2-t15.
- **s2-t15:** "remove it (or keep it behind a Kconfig flag)" leaves the choice open.
