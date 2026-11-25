# Explain Action

1. Read `context/current-feature.md` to understand what was implemented.
2. Run `git diff main --name-only` (or the base branch) for the list of modified and new files.
3. For the entire feature:
   - **Start with a relatable real-world analogy**: an intuitive metaphor (for example a restaurant order slip passing from waiter to kitchen, or a mailbox shared by two people with one key) that explains the overall idea simply, as you would to a bright 15-year-old.
4. For each file created or modified:
   - Show the file path (`components/app_logic/*.c`, `main/*.c`, `test/host/*.c`, config or docs).
   - Give a clear 1-2 sentence plain-English explanation of what it does and why it changed, avoiding dense jargon.
   - Use concrete comparisons for functions, structs, queues, mutexes and config macros.
5. **How it all connects (step-by-step story)**:
   - Trace the data path for this feature: sensor sample, `raw_queue`, validation and smoothing in `app_logic`, `data_mutex`-guarded `latest`, display and `publish_queue`, MQTT, plus the fault path to `error_queue` and `monitor_task`. Cover only the parts the feature touches.
   - If a graph exists, `& .\.venv\Scripts\graphify.exe path "<A>" "<B>"` and `explain "<symbol>"` give the topology without reading every file.
   - Provide a Mermaid sequence or flowchart diagram of the verified path.
6. **Why this matters in practice**:
   - Tie it to the project goal: which RTOS concept it practises (priorities, queues, mutexes and priority inheritance, event groups, timing, fault handling) and which failure it prevents (priority inversion, deadlock, queue overflow, a hung task, a lost connection stopping sampling).
   - Say which parts are host-tested and which still need the real board.

## Output Format

### 💡 The Big Picture (Real-World Analogy)
[Vivid, relatable metaphor explaining the core problem and how this feature solves it]

### 📁 Files Changed
- **`components/app_logic/<module>.c`** *(New/Modified)*
  - *What it is*: [Simple plain-English description]
  - *Real-world analogy*: [Everyday comparison]
  - *Key functions/structs*: [Plain explanation]

### 🔗 How It All Connects
[Step-by-step diagram and narrative]

### 🧠 Why This Matters
[The RTOS concept practised, the failure it guards against, and what remains unverified without hardware]
