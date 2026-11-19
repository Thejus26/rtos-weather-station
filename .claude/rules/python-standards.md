## Python Coding Standards (Tool-Calling Assistant)

Applies to every `.py` file in this project. Python 3.10+.

### Style & tooling
- Format and lint with **ruff** (line length 100). Type-check `src/` with **mypy**.
- Type hints on every function signature. Use `X | None`, not `Optional[X]`.
- Docstrings on public modules, classes and functions (one-line summary is enough).
- Prefer `pathlib.Path` over string paths, and f-strings over `%` or `.format`.
- No mutable default arguments. No wildcard imports.

### Default layout (adjust only with a reason)
```
src/assistant/
    agent.py        # the loop: send -> tool call? -> execute -> feed back -> repeat
    llm.py          # thin wrapper around the chosen LLM API
    tools/          # one module per tool + a registry holding the JSON schemas
    config.py       # env loading, constants (model name, MAX_ITERATIONS, timeouts)
    cli.py          # entry point
tests/
requirements.txt   requirements-dev.txt   .env.example
```

### Agent-loop invariants
- **Bounded**: the loop has a `MAX_ITERATIONS` guard. Hitting it raises or returns a clear error, never an endless loop.
- **Stops on a final answer**: no tool call in the model's reply means the loop ends.
- **History stays valid**: every tool request is followed by a matching tool result, and both are appended to the message history before the next model call.
- **Tool failures don't crash the loop**: catch exceptions at the dispatch boundary and return the error text to the model as the tool result.
- **Unknown tool names and bad arguments are handled** the same way. Validate arguments against the tool's JSON schema before executing.
- **Every network call has a timeout** (LLM API and tools alike).

### Safety
- Never pass model-controlled text to `eval`, `exec`, `os.system`, `os.popen`, `subprocess(..., shell=True)`, `pickle.loads` or `yaml.load`. The calculator tool must use an `ast`-based safe evaluator or a strict parser.
- The edit guard asks for confirmation when code contains one of these. A line that is deliberately safe can carry a `# unsafe-ok: <reason>` comment, which the guard skips.
- Secrets come from the environment. Never log keys, request headers or full prompts that may contain personal data.

### Errors
- Define a small exception hierarchy rooted at `AssistantError` (for example `ToolError`, `LLMError`, `MaxIterationsError`).
- No bare `except:`. No silent `except Exception: pass`. Re-raise or log with context.

### Logging & output
- Use the `logging` module (`logger = logging.getLogger(__name__)`). Log tool name, arguments summary and latency.
- `print()` is allowed only in `cli.py` for user-facing output. Never leave `print`, `breakpoint()` or `pdb` calls in library code.

### Testing
- pytest, one test module per source module. Use a fake LLM client that returns scripted responses.
- Cover: direct answer (no tool), single tool call, multiple tool calls in a row, tool raises, unknown tool, malformed arguments, max iterations reached, API error or timeout.
- Keep tests fast and offline.

### Scope
- Plain Python loop, no agent frameworks. Memory, planning and multi-agent features belong to later projects.
