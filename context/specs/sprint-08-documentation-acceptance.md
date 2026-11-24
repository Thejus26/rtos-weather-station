# Sprint 8: Documentation, Demo and Acceptance

## Goal

Complete the deliverables and check the acceptance criteria against evidence. Branch: `docs/deliverables`. No new hardware work, but the demo capture needs the running board.

## Tasks

Effort uses the roadmap's relative sizes: S = one focused sitting, M = a few sittings, L = most of a sprint. The roadmap gives no hours. Task IDs are the roadmap's.

### s8-t1 · Wiring diagram
- **ID:** s8-t1-wiring-diagram
- **Description:** Finalise the wiring diagram in `docs/` (from `docs/wiring.md`, with a clean diagram or photo).
- **Acceptance criteria:**
  - The diagram matches the real circuit.
- **Dependencies:** s2-t16-wiring-doc
- **Effort:** S
- **Covers:** DEL-2, HW-6

### s8-t2 · Task and communication diagram
- **ID:** s8-t2-task-comm-diagram
- **Description:** Task and communication diagram: five tasks, the ISR, every queue, mutex, semaphore and event group, and who produces and consumes each.
- **Acceptance criteria:**
  - The diagram matches the code and the overview tables.
- **Dependencies:** s7-t15-final-gates-run
- **Effort:** M
- **Covers:** DEL-2, GOAL-1, GOAL-2

### s8-t3 · Stack table
- **ID:** s8-t3-stack-table
- **Description:** Table of priorities, stack sizes and measured high-water marks (from s7-t11-stack-hwm-final).
- **Acceptance criteria:**
  - Every task row has a measured value and a percentage used.
- **Dependencies:** s7-t11-stack-hwm-final
- **Effort:** S
- **Covers:** DEL-2, NFR-2, ACC-4

### s8-t4 · Collect test evidence
- **ID:** s8-t4-collect-test-evidence
- **Description:** Collect test evidence under `docs/test-results/`: host unit-test output, the fault-injection matrix, the soak log and summary, and the timing measurements.
- **Acceptance criteria:**
  - One folder holds all four evidence sets.
  - Each is linked from the README.
- **Dependencies:** s7-t15-final-gates-run
- **Effort:** M
- **Covers:** DEL-3a, DEL-3b, DEL-3c, DEL-3d

### s8-t5 · Demo media
- **ID:** s8-t5-demo-media
- **Description:** Demo: a short video or screenshots of the OLED, the serial log and the MQTT subscriber output.
- **Acceptance criteria:**
  - Media is saved.
  - It is referenced from the README.
- **Dependencies:** s7-t15-final-gates-run
- **Effort:** M
- **Covers:** DEL-4, FR-4, FR-6

### s8-t6 · Reflection notes
- **ID:** s8-t6-reflection-notes
- **Description:** Reflection notes in the README "Notes" section: priority-inversion findings (from s7-t12-priority-inversion-experiment), stack-sizing observations, and what to change when porting to STM32.
- **Acceptance criteria:**
  - All three topics are covered with evidence.
- **Dependencies:** s7-t12-priority-inversion-experiment, s8-t3-stack-table
- **Effort:** M
- **Covers:** DEL-5, STR-4

### s8-t7 · Source review
- **ID:** s8-t7-source-review
- **Description:** Source review: comments on the non-obvious parts, no hard-coded credentials (search), no leftover bring-up code, `coding-standards.md` followed.
- **Acceptance criteria:**
  - The search and review checklist show no findings.
- **Dependencies:** s7-t15-final-gates-run
- **Effort:** M
- **Covers:** DEL-1, FR-10

### s8-t8 · Acceptance walkthrough
- **ID:** s8-t8-acceptance-walkthrough
- **Description:** Acceptance walk-through: check FR-1 to FR-10 and ACC-1 to ACC-5, each against a named piece of evidence.
- **Acceptance criteria:**
  - A checklist exists with a link beside every item.
- **Dependencies:** s8-t3-stack-table, s8-t4-collect-test-evidence
- **Effort:** M
- **Covers:** ACC-1 to ACC-5, FR-1 to FR-10

### s8-t9 · Finalise docs status
- **ID:** s8-t9-finalise-docs-status
- **Description:** Set Status to complete in the overview and README, sync the two files, update `project-structure.md` to the final tree, and clear `current-feature.md`.
- **Acceptance criteria:**
  - Docs agree and match the repo.
- **Dependencies:** s8-t8-acceptance-walkthrough
- **Effort:** S
- **Covers:** none listed

### s8-t10 · Tag release
- **ID:** s8-t10-tag-release
- **Description:** Tag `v1.0` and push. Confirm with the owner before pushing, because the repository is public.
- **Acceptance criteria:**
  - The tag exists on the remote.
- **Dependencies:** s8-t9-finalise-docs-status
- **Effort:** S
- **Covers:** none listed

## Definition of Done

- ACC-1 to ACC-5 each point at evidence in the repo.
- The documentation and tracker are in their final state.
- The sprint-close checklist in roadmap section 1 is complete.

## Open Questions

- **s8-t5:** the roadmap allows "video or screenshots" without a preference or a size limit for the repository.
- **s8-t6:** STR-4 (STM32 port) is listed as covered here, but only the porting notes are a deliverable. The port itself is Backlog task s9-t4.
- **s8-t10:** the roadmap says the repository is public and requires owner confirmation. It does not say who the owner is or what to do if the confirmation is declined.
- **Acceptance evidence:** the roadmap lists the required evidence sets but gives no file names for the checklist in s8-t8.
