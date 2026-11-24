# s2-t6: BME280 measure

| Field | Value |
|-------|-------|
| Task ID | `s2-t6-bme280-measure` |
| Sprint | [Sprint 2: Hardware Bring-up and Drivers](../../sprint-02-hardware-bring-up.md) |
| Branch | `feature/drivers` |
| Effort | L: most of a sprint (roadmap relative size, no hours given) |
| Marked [HW] in roadmap | No |
| Status | Not started |

## Description

BME280 forced-mode measurement with temperature and humidity compensation, returning `esp_err_t`. No allocation.

## Acceptance criteria

- [ ] Readings are plausible against a reference thermometer.
- [ ] Breathing on the sensor raises humidity.

## Requirements covered

| ID | Requirement |
|----|-------------|
| HW-2 | BME280 on I2C, address 0x76 or 0x77 |
| FR-1 | Sample temperature and humidity every 5 s |
| NFR-1 | No dynamic allocation in steady state |

## Dependencies

**Depends on:** 
- [`s2-t5-bme280-init`](s2-t5-bme280-init.md) (BME280 init)

**Blocks:** 
- [`s2-t7-bme280-address-config`](s2-t7-bme280-address-config.md) (BME280 address config)
- [`s2-t8-sensor-interface`](s2-t8-sensor-interface.md) (Sensor interface)
- [`s2-t9-i2c-error-bounded`](s2-t9-i2c-error-bounded.md) (I2C error bounded)
- [`s2-t15-bringup-loop`](s2-t15-bringup-loop.md) (Bring-up loop)

## Source

Derived from [`sprint-02-hardware-bring-up.md`](../../sprint-02-hardware-bring-up.md) and [`spec-roadmap.md`](../../spec-roadmap.md). If this file and the roadmap disagree, the roadmap wins.
