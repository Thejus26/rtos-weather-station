# Sprint 5: Connectivity (Wi-Fi, SNTP, MQTT, Configuration)

## Goal

Get readings to a broker every 30 s, keep configuration out of code, and make sure a network outage does not stop sampling. Branch: `feature/comms`. Needs hardware, a Wi-Fi access point and a local MQTT broker.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s5-t1 · Kconfig network options
- **ID:** s5-t1-kconfig-network-options
- **Description:** Settle D-15. Extend `Kconfig.projbuild` with Wi-Fi SSID and password, broker URI, topic base and device ID. Confirm `sdkconfig.defaults` has no credentials.
- **Acceptance criteria:**
  - The options appear in `menuconfig`.
  - No secrets are in tracked files.
- **Dependencies:** s0-t10-kconfig-menu
- **Effort:** S
- **Covers:** FR-10, FR-6

### s5-t2 · Local broker
- **ID:** s5-t2-local-broker
- **Description:** Run Mosquitto locally (`mosquitto -v`) and subscribe with `mosquitto_sub -t "weather/#" -v`.
- **Acceptance criteria:**
  - A manual publish shows up in the subscriber.
- **Dependencies:** None
- **Effort:** S
- **Covers:** FR-6

### s5-t3 · NVS config
- **ID:** s5-t3-nvs-config
- **Description:** NVS initialisation with erase-and-retry on a version mismatch, and reading of the configuration values.
- **Acceptance criteria:**
  - The boot log shows config loaded.
  - No credentials are printed.
- **Dependencies:** s5-t1-kconfig-network-options
- **Effort:** S
- **Covers:** FR-10

### s5-t4 · Wi-Fi station
- **ID:** s5-t4-wifi-station
- **Description:** Wi-Fi station start-up. The event handler sets and clears `WIFI_CONNECTED_BIT`.
- **Acceptance criteria:**
  - The bit follows the connection state.
- **Dependencies:** s5-t3-nvs-config
- **Effort:** M
- **Covers:** FR-7, OBJ-7

### s5-t5 · Wi-Fi backoff
- **ID:** s5-t5-wifi-backoff
- **Description:** Reconnect with exponential backoff using `backoff_next_ms` (1 s, doubling to 60 s), reset after a success.
- **Acceptance criteria:**
  - The log shows 1, 2, 4 ... 60 s delays with the AP off.
- **Dependencies:** s5-t4-wifi-station, s1-t9-backoff
- **Effort:** S
- **Covers:** TIM-7, FR-7, ERR-3

### s5-t6 · SNTP time
- **ID:** s5-t6-sntp-time
- **Description:** SNTP start-up with a synchronised flag and ISO 8601 UTC timestamps. Before sync, use the marker chosen in D-11.
- **Acceptance criteria:**
  - Timestamps are correct after sync.
  - They are clearly marked before sync.
- **Dependencies:** s5-t4-wifi-station
- **Effort:** M
- **Covers:** FR-6

### s5-t7 · MQTT client
- **ID:** s5-t7-mqtt-client
- **Description:** MQTT client start-up. The event handler sets and clears `MQTT_CONNECTED_BIT` and handles reconnects.
- **Acceptance criteria:**
  - The bit follows the broker connection.
- **Dependencies:** s5-t4-wifi-station
- **Effort:** M
- **Covers:** FR-6, FR-7, OBJ-7

### s5-t8 · JSON payload
- **ID:** s5-t8-json-payload
- **Description:** Build the JSON payload with `reading_to_json` into a static buffer, from the `publish_queue` entry plus the device ID and timestamp.
- **Acceptance criteria:**
  - The subscriber shows valid JSON with all fields.
- **Dependencies:** s5-t6-sntp-time, s1-t15-reading-json
- **Effort:** S
- **Covers:** FR-6, NFR-1

### s5-t9 · Comms task
- **ID:** s5-t9-comms-task
- **Description:** `comms_task`: wait on `WIFI_CONNECTED_BIT`, run the connection lifecycle, and publish entries from `publish_queue` only when MQTT is connected. Remove an entry only after a successful publish.
- **Acceptance criteria:**
  - Readings arrive at the subscriber.
- **Dependencies:** s5-t7-mqtt-client, s5-t8-json-payload
- **Effort:** L
- **Covers:** FR-6, FR-7, TSK-5, OBJ-2

### s5-t10 · Outage buffering
- **ID:** s5-t10-outage-buffering
- **Description:** Settle D-16. During an outage `comms_task` stops consuming, `process_task` drops oldest when the queue is full, and on reconnect the backlog is sent oldest first at a bounded rate.
- **Acceptance criteria:**
  - After a long outage there is no crash and no unbounded burst.
  - The drop count is logged.
- **Dependencies:** s5-t9-comms-task
- **Effort:** M
- **Covers:** ERR-3, ERR-4, FR-7

### s5-t11 · Measure publish cadence [HW]
- **ID:** s5-t11-measure-publish-cadence
- **Description:** Verify publish cadence on the subscriber side over at least 20 publishes.
- **Acceptance criteria:**
  - The interval is 30 s within +/-1 s.
- **Dependencies:** s5-t9-comms-task
- **Effort:** S
- **Covers:** TIM-5

### s5-t12 · Network outage test [HW]
- **ID:** s5-t12-network-outage-test
- **Description:** Turn Wi-Fi off, then take the broker down. Confirm sampling and display continue in both cases, and publishing resumes afterward.
- **Acceptance criteria:**
  - The OLED and serial keep updating through both outages.
  - Publishing resumes afterward.
- **Dependencies:** s5-t10-outage-buffering
- **Effort:** M
- **Covers:** FR-7, ERR-3

### s5-t13 · Credential hygiene
- **ID:** s5-t13-credential-hygiene
- **Description:** Confirm `sdkconfig` is ignored, search source and logs for the password, and confirm nothing sensitive was printed.
- **Acceptance criteria:**
  - The search finds no credentials in tracked files or logs.
- **Dependencies:** s5-t9-comms-task
- **Effort:** S
- **Covers:** FR-10, DEL-1

### s5-t14 · Comms stack check
- **ID:** s5-t14-comms-stack-check
- **Description:** Check the `comms_task` stack high-water mark during connect, reconnect and publish, and resize if needed.
- **Acceptance criteria:**
  - At least 25% headroom at the worst point.
- **Dependencies:** s5-t9-comms-task
- **Effort:** S
- **Covers:** NFR-2, TSK-5

## Definition of Done

- JSON readings arrive every 30 s.
- Credentials live only in `menuconfig`/NVS.
- Sampling and display survive both a Wi-Fi outage and a broker outage.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

Decisions assigned to this sprint (roadmap section 4). Log each outcome in roadmap section 10.

- **D-15** (s5-t1): MQTT topic, QoS and retain. Recommended default: topic `weather/<device_id>/reading`, QoS 1, no retain. The overview's subscriber example uses only `weather/#`.
- **D-16** (s5-t10): behaviour on reconnect with buffered readings. Recommended default: oldest first, one per publish tick or rate-limited, never an unbounded burst. The roadmap does not give the rate limit.
- **s5-t6:** the roadmap does not say how long to wait for the first SNTP sync after boot, or what `comms_task` does with readings that carry the pre-sync marker (publish or hold).
- **s5-t2:** the broker is run locally on the developer machine. The roadmap does not say whether the board and the broker must be on the same network or whether authentication is used.
