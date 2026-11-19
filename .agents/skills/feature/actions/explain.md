# Explain Action

1. Read `context/current-feature.md` to understand what was implemented.
2. Run `git diff main --name-only` (or the base branch) to get the list of modified and new files.
3. For the entire feature:
   - **Start with a Relatable Real-World Analogy**: Use an intuitive metaphor (e.g., a manager delegating errands to an assistant who reports back, a restaurant order slip going to the kitchen and returning with a dish) to explain the overall concept simply, as you would to a bright 15-year-old.
4. For each file created or modified:
   - Show the file path (`src/.../*.py`, `requirements.txt`, `tests/...`).
   - Give a clear 1-2 sentence plain-English explanation of what it does and why it changed, avoiding dense jargon.
   - Use concrete comparisons to explain functions, classes, JSON schemas, and the message history.
5. **How It All Connects (The Step-by-Step Story)**:
   - Trace the exact journey: user prompt, message history, LLM call, tool request, argument validation, tool execution, tool result appended, next LLM call, final answer or `MAX_ITERATIONS` stop.
   - **Token-Frugal Topology Discovery**: If a graph exists, use graphify instead of reading raw source files:
     ```powershell
     & .\.venv\Scripts\graphify.exe path "<source_component>" "<target_component>"
     & .\.venv\Scripts\graphify.exe explain "<key_function_or_class>"
     ```
   - Provide an intuitive Mermaid sequence or flowchart diagram of this verified journey.
6. **Why This Matters in Practice**:
   - Tie the feature back to the project goal: what this piece shows about what agent frameworks do under the hood, and what failure it prevents (runaway loops, crashes on a bad tool call, injection through tool arguments).

## Output Format

### 💡 The Big Picture (Real-World Analogy)
[Vivid, relatable metaphor explaining the core problem and how this feature solves it in plain English]

### 📁 Files Changed
- **`src/assistant/agent.py`** *(New/Modified)*
  - *What it is*: [Simple plain-English description]
  - *Real-world analogy*: [Everyday comparison, e.g. "Like a manager checking the to-do list until it is empty..."]
  - *Key functions/classes*: [Plain explanation]

### 🔗 How It All Connects
[Step-by-step diagram and narrative from user prompt to final answer]

### 🧠 Why This Matters
[What this teaches about agent internals, and which failure it guards against]
