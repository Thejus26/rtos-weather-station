# Current Feature: s0-t1-parts-and-hardware-check

## Status
In Progress

## Goals
<!-- Source: context/specs/tasks/sprint-00/s0-t1-parts-and-hardware-check.md (roadmap wins on any disagreement). Branch: chore/foundation. Effort: S. Not marked [HW]. Depends on: none. -->

Hardware/procurement task. No firmware, no host tests, no code. Deliverable is a checked parts list with pull-up notes.

### Deliverables
1. A parts checklist, each line marked **in hand** or **on order** (with supplier/ETA if ordered). Suggested location: a "Parts check" section in `README.md` Notes (mirror nothing into `context/project-overview.md` unless the spec itself changes), or `context/hardware-check.md` if you prefer a standalone file. Decide before `start`. If a new file is added, update `context/project-structure.md` in the same change.
2. Pull-up notes for the BME280 and SSD1306 breakouts (present / absent, and value if known).
3. BME280 address strap noted (SDO low = `0x76`, SDO high = `0x77`).

### Parts checklist (HW requirement IDs)
| Part | Requirement | Check |
|------|-------------|-------|
| ESP32-DevKitC, WROOM-32E, 4 MB flash, USB 5 V power | HW-1 | [ ] |
| BME280 breakout, I2C, address `0x76` or `0x77` | HW-2 | [ ] |
| SSD1306 128x64 I2C OLED, address `0x3C` | HW-3 | [ ] |
| Push button (GPIO4, internal pull-up, falling edge) | HW-4 | [ ] |
| LED + 330 ohm resistor (GPIO2 or onboard) | HW-5 | [ ] |
| Breadboard | HW-6 | [ ] |
| Jumper wires | HW-6 | [ ] |
| 4.7 k resistors (x2, for SDA/SCL if breakouts lack pull-ups) | HW-6 | [ ] |
| USB data cable (data lines, not charge-only) | HW-1 | [ ] |
| Logic analyser (needed for the Sprint 7 jitter measurement) | Sprint 7 | [ ] |

### Acceptance criteria
- [ ] Every part is in hand or on order.
- [ ] Pull-up presence on the breakouts is noted.

### Pass criteria
- No unchecked line without an "on order" note.
- Pull-up note names each breakout (BME280, SSD1306) explicitly. Rule of thumb for the note: most BME280 breakouts have 10 k pull-ups, most SSD1306 modules have none or 4.7 k. Check the board or the seller datasheet. Do not assume.

## Notes
- **Pins to keep in mind while checking** (from `AGENTS.md`): SDA GPIO21, SCL GPIO22, button GPIO4, LED GPIO2. 3.3 V logic. Confirm both breakouts are 3.3 V tolerant.
- **Pull-up decision rule:** if both breakouts already carry pull-ups, parallel values lower the effective resistance. Add external 4.7 k only if neither has them. Record the conclusion for Sprint 2 (`s2-t1-wire-circuit`).
- **Address check:** expect `0x76` (or `0x77`) and `0x3C` on the I2C scan in Sprint 2. A `0x3D` OLED strap or a `0x77` BME280 is acceptable but must be noted, because `app_config.h` holds the addresses.
- **Blocks:** `s0-t11-flash-scaffold` (needs the board and a data cable) and `s2-t1-wire-circuit` (needs everything).
- **Scope guard:** the `/feature` skill templates in `.claude/skills/feature` are written for a Python tool-calling assistant. They do not fit this task (no pytest, ruff, mypy, or agent loop). `test` and `review` for this feature mean a manual check of the list above, not running `.venv` tools.
- **Owner decision (2026-11-24):** no hardware will be bought; code-only build. Acceptance criteria are waived, not met. Both are recorded as such in README Notes. Roadmap tasks marked `[HW]` and the Sprint 7 jitter measurement are deferred. The roadmap itself was not edited. Decide separately whether to mark those tasks skipped.
- **Decided:** the checklist and pull-up tables live in `README.md` Notes ("Parts check" and "I2C breakout notes"). No new file, so `context/project-structure.md` is unchanged. The tables are templates: the Status and pull-up cells stay empty until the parts are physically checked.

## History
<!-- Append-only. Keep the 3-5 most recent completed features here; archive older ones to context/feature-history.md. -->
