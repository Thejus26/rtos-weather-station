---
name: research
description: Run a research task on LLM tool-use APIs, JSON-schema tool design, or Python library behavior
argument-hint: <prompt-name>
---

## Task

Execute research task: `$ARGUMENTS`

---

### Instructions

1. If no argument is provided, return error: `"Usage: /research <prompt-name>"`
2. Look for research prompt file at `context/research/{$ARGUMENTS}.md`
3. If not found, return error: `"Prompt file not found at context/research/{$ARGUMENTS}.md"`
4. Read the research prompt file, which defines:
   - **Output**: Target documentation file (e.g., `docs/tool-use-message-format.md` or `context/specs/tool-schema-spec.md`)
   - **Research Scope**: LLM provider tool-use APIs (Anthropic, OpenAI, Ollama), JSON-schema tool definitions, the message and tool-result formats, stop reasons, streaming, rate limits, or Python libraries (`httpx`, `pydantic`, `jsonschema`, `python-dotenv`, `pytest`)
   - **Include**: Request and response shapes, error and retry behavior, token and cost implications, minimal runnable examples
   - **Sources**: Official provider documentation and SDK references, library docs, relevant RFCs
5. Execute the research:
   - Read the provider docs for the exact tool-calling request/response format and how tool results must be returned
   - Search the codebase for existing message-handling code, tool schemas, and config constants
   - Note version-specific behavior (SDK version, model name) so the findings can be dated
6. Write structured findings to the specified output location
7. Provide a concise summary of the findings

---

### Rules

- This command produces **DOCUMENTATION ONLY**
- Do NOT modify source code files
- Do NOT create branches or commits
- Output documents should be written to `docs/` or `context/`
- Cite the documentation source and date for every API behavior claim
- Never put API keys in research output
