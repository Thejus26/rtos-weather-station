/*
 * app_config.h - the single place for pins, periods, priorities, stack sizes,
 * queue depths and timeouts (AGENTS.md "Conventions").
 *
 * Macros only, no includes, so it can be syntax-checked in the host container.
 * Only code under main/ may include it. components/app_logic/ must not: it
 * stays pure C and takes plain values as parameters.
 *
 * Units: durations in ms (convert with pdMS_TO_TICKS at the use site), stack
 * sizes in bytes (ESP-IDF xTaskCreate takes bytes), pins as plain GPIO numbers
 * (cast to gpio_num_t at the use site). No secrets, broker URLs or device IDs
 * here: those go in menuconfig/NVS.
 *
 * Values come from context/project-overview.md. The requirement IDs are from
 * context/specs/spec-roadmap.md.
 */
#ifndef APP_CONFIG_H
#define APP_CONFIG_H

/* ---- Pins (HW-4, HW-5, HW-6) ------------------------------------------ */
#define APP_PIN_I2C_SDA             21   /* BME280 and OLED share this bus */
#define APP_PIN_I2C_SCL             22
#define APP_PIN_BUTTON              4    /* to GND, internal pull-up, falling-edge interrupt */
#define APP_PIN_STATUS_LED          2    /* 330 ohm resistor, or the onboard LED */

/* ---- I2C addresses (HW-6) --------------------------------------------- */
#define APP_I2C_ADDR_BME280         0x76 /* default */
#define APP_I2C_ADDR_BME280_ALT     0x77 /* when SDO is tied high */
#define APP_I2C_ADDR_OLED           0x3C /* SSD1306 */
/* I2C clock speed is not in the overview. Decide it in s2-t3-i2c-bus-driver. */

/* ---- Periods and timeouts, ms (TSK-1, TSK-2, TSK-4, TIM-3, TIM-5, TIM-6) */
#define APP_SAMPLE_PERIOD_MS        5000  /* sensor_task, vTaskDelayUntil */
#define APP_DISPLAY_PERIOD_MS       1000  /* display refresh */
#define APP_BUTTON_SEM_TIMEOUT_MS   1000  /* display_task wait on button_sem */
#define APP_PUBLISH_PERIOD_MS       30000 /* MQTT publish, and process_task enqueue */
#define APP_HOUSEKEEPING_PERIOD_MS  10000 /* monitor_task housekeeping */
#define APP_I2C_MUTEX_TIMEOUT_MS    100   /* a timeout is reported as an error */
/* Shorter waits for process_task and monitor_task are pending decision D-9. */

/* ---- Task priorities, higher number = higher priority (TSK-1..TSK-5) --- */
#define APP_PRIO_MONITOR            6
#define APP_PRIO_SENSOR             5
#define APP_PRIO_PROCESS            4
#define APP_PRIO_DISPLAY            3
#define APP_PRIO_COMMS              3

/* ---- Task stack sizes, bytes (TSK-1..TSK-5) ---------------------------- */
#define APP_STACK_MONITOR           (3 * 1024)
#define APP_STACK_SENSOR            (4 * 1024)
#define APP_STACK_PROCESS           (3 * 1024)
#define APP_STACK_DISPLAY           (3 * 1024)
#define APP_STACK_COMMS             (6 * 1024)

/* ---- Queue depths, items (OBJ-1, OBJ-2, OBJ-3) -------------------------- */
#define APP_RAW_QUEUE_DEPTH         8    /* sample_t, sensor_task -> process_task */
#define APP_PUBLISH_QUEUE_DEPTH     10   /* reading_t, drop oldest when full */
#define APP_ERROR_QUEUE_DEPTH       8    /* error_event_t, senders never block */

/* ---- Wi-Fi reconnect backoff, ms (TIM-7) -------------------------------- */
#define APP_BACKOFF_MIN_MS          1000
#define APP_BACKOFF_MAX_MS          60000
#define APP_BACKOFF_FACTOR          2    /* doubles each attempt */

/* ---- Fault recovery (ERR-1, TIM-8) -------------------------------------- */
#define APP_I2C_RETRY_MAX           3    /* retries before reporting to error_queue */
#define APP_SENSOR_REINIT_AFTER     3    /* consecutive failures before sensor re-init */
#define APP_RESTART_AFTER_RECOVERIES 10  /* failed recoveries before esp_restart() */

/* ---- Watchdog and heap (TIM-9, ERR-6) ----------------------------------- */
#define APP_WDT_TIMEOUT_S           10   /* keep equal to CONFIG_ESP_TASK_WDT_TIMEOUT_S */
#define APP_HEAP_LOW_BYTES          (20 * 1024) /* warn below this; restart rule is D-14 */

#endif /* APP_CONFIG_H */
