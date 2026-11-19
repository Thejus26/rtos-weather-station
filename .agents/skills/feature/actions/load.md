# Load Action

1. Check `$ARGUMENTS` (after "load"):
   - If it looks like a filename (single word, no spaces): Look for `context/specs/{name}.md` OR `context/features/{name}.md`
   - If it's multiple words: Use as inline feature description, generate goals
   - If empty: Error - "load" requires a spec filename or feature description

2. **Knowledge Graph Interrogation (Token-Frugal Discovery)**:
   - If `graphify-out/graph.json` exists, do not read raw code files to discover symbols, callers, or structure. Run graphify via the local virtual environment:
     ```powershell
     & .\.venv\Scripts\graphify.exe query "<feature/module name>"
     & .\.venv\Scripts\graphify.exe explain "<key_function_or_class>"
     & .\.venv\Scripts\graphify.exe path "<source_component>" "<target_component>"
     ```
   - Extract dependent modules, callers, and function signatures from the graph response instead of reading whole files.
   - If there is no graph yet (new project), skip this step.

3. Update `context/current-feature.md`:
   - Update the H1 heading to include the feature name (e.g., `# Current Feature: calculator-tool`)
   - Compile a self-contained, actionable **Technical Brief** under `## Goals` and `## Notes`:
     - **Deliverables**: Enumerated deliverables with target file paths.
     - **Key Signatures**: Exact function and class signatures (from graphify or existing code) to remove guesswork during implementation.
     - **Errors**: The specific `AssistantError` subclasses raised and how each is surfaced (to the model as a tool result, or to the user).
     - **Tool Schema**: For a tool feature, the JSON schema (name, description, parameters) and example calls.
     - **Test Scenarios**: Concrete pytest cases matching the Definition of Done, using the fake LLM client.
     - **Boundaries**: Module boundaries, import direction, config values, timeouts, and iteration limits under `## Notes`.
   - Set Status to `Not Started`

4. Confirm the spec is loaded and display the feature summary.
