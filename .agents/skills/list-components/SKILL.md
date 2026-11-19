---
name: list-components
description: List the modules and components of the tool-calling assistant
argument-hint: [layer-or-subdirectory]
---

## Task

List all modules, classes, and source files across the layers of the assistant. If `context/project-structure.md` describes a layout, follow it. Otherwise use the default layout from `rules/python-standards.md`:

- **Agent Loop (`agent.py`)**: message history, the send, tool-call, execute, feed-back cycle, the `MAX_ITERATIONS` guard, and the final-answer stop condition.
- **LLM Client (`llm.py`)**: thin wrapper over the chosen API (Anthropic, OpenAI, or a local model), request/response parsing, timeouts.
- **Tool Registry & Schemas (`tools/`)**: JSON-schema definitions, name-to-function dispatch, argument validation.
- **Tools (`tools/*.py`)**: calculator, weather, web search, and any others.
- **Configuration (`config.py`, `.env.example`)**: env loading, model name, limits, timeouts.
- **Errors (`errors.py` or similar)**: the `AssistantError` hierarchy.
- **CLI / Entry Point (`cli.py`, `__main__.py`)**: user input loop and output.
- **Tests (`tests/`)**: fake LLM client, per-module test files.

If a `[layer-or-subdirectory]` argument is provided via `$ARGUMENTS`, only list files within that layer or directory.

## Output Format

- Numbered list of modules and source files with relative paths.
- Brief one-line description of each component's responsibility.
- Layer mapping and the import direction between layers (for example `cli -> agent -> llm/tools -> config`).
- Summary count at the end.

If no components are found, output: "No assistant components found."
