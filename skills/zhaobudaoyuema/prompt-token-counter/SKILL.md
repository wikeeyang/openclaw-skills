---
name: prompt-token-counter
version: 1.0.1
description: Count tokens and estimate costs for 300+ LLM models. Primary use: audit OpenClaw workspace token consumption—memory files, persona (SOUL/IDENTITY/AGENTS), and skills (SKILL.md). Trigger when user asks about token counting, prompt length, API cost, or OpenClaw context token usage.
---

# Prompt Token Counter (toksum)

> **First load reminder:** This skill provides the `scripts` CLI (toksum). Use it when the user asks to count tokens, estimate API costs, or **audit OpenClaw component token consumption** (memory, persona, skills).

## Primary Use: OpenClaw Token Consumption Audit

**Goal:** Help users identify which OpenClaw components consume tokens and how much.

### 1. Memory & Persona Files

These files are injected into sessions and consume tokens. Search and count them:

| File | Purpose | Typical Location |
|------|---------|------------------|
| `AGENTS.md` | Operating instructions, workflow, priorities | `~/.openclaw/workspace/` |
| `SOUL.md` | Persona, tone, values, behavioral guidelines | `~/.openclaw/workspace/` |
| `IDENTITY.md` | Name, role, goals, visual description | `~/.openclaw/workspace/` |
| `USER.md` | User preferences, communication style | `~/.openclaw/workspace/` |
| `MEMORY.md` | Long-term memory, persistent facts | `~/.openclaw/workspace/` |
| `TOOLS.md` | Tool quirks, path conventions | `~/.openclaw/workspace/` |
| `HEARTBEAT.md` | Periodic maintenance checklist | `~/.openclaw/workspace/` |
| `BOOT.md` | Startup ritual (when hooks enabled) | `~/.openclaw/workspace/` |
| `memory/YYYY-MM-DD.md` | Daily memory logs | `~/.openclaw/workspace/memory/` |

**Workspace path:** Default `~/.openclaw/workspace`; may be overridden in `~/.openclaw/openclaw.json` via `agent.workspace`.

### 2. Skill Files (SKILL.md)

Skills are loaded per session. Count each `SKILL.md`:

| Location | Scope |
|----------|-------|
| `~/.openclaw/skills/*/SKILL.md` | OpenClaw managed skills |
| `~/.openclaw/workspace/skills/*/SKILL.md` | Workspace-specific skills (override) |

### 3. Audit Workflow

1. **Locate workspace:** Resolve `~/.openclaw/workspace` (or config override).
2. **Collect files:** List all memory/persona files and `SKILL.md` paths above.
3. **Count tokens:** For each file, run `python -m scripts.cli -f <path> -m <model> -c`.
4. **Summarize:** Group by category (memory, persona, skills), report total and per-file.

**Example audit command (PowerShell):**
```powershell
$ws = "$env:USERPROFILE\.openclaw\workspace"
python -m scripts.cli -m gpt-4o -c -f "$ws\AGENTS.md" -f "$ws\SOUL.md" -f "$ws\USER.md" -f "$ws\IDENTITY.md" -f "$ws\MEMORY.md" -f "$ws\TOOLS.md"
```

**Example audit (Bash):**
```bash
WS=~/.openclaw/workspace
python -m scripts.cli -m gpt-4o -c -f "$WS/AGENTS.md" -f "$WS/SOUL.md" -f "$WS/USER.md" -f "$WS/IDENTITY.md" -f "$WS/MEMORY.md" -f "$WS/TOOLS.md"
```

---

## Project Layout

```
prompt_token_counter/
├── SKILL.md
├── scripts/                    # Python package, CLI
│   ├── cli.py                  # Entry point
│   ├── core.py                 # TokenCounter, estimate_cost
│   └── registry/
│       ├── models.py           # 300+ models
│       └── pricing.py          # Pricing data
└── examples/
    ├── count_prompt.sh / .ps1
    ├── estimate_cost.sh / .ps1
    └── batch_compare.sh
```

Invoke: `python -m scripts.cli` from project root.

---

## Runtime Dependencies

- **Python 3** — required
- **tiktoken** (optional) — `pip install tiktoken` for exact OpenAI counts

---

## Language Rule

**Respond in the user's language.** Match the user's language (e.g. Chinese if they write in Chinese, English if they write in English).

---

## CLI Usage

```bash
python -m scripts.cli [OPTIONS] [TEXT ...]
```

| Option | Short | Description |
|--------|-------|-------------|
| `--model` | `-m` | Model name (required unless `--list-models`) |
| `--file` | `-f` | Read from file (repeatable) |
| `--url` | `-u` | Read from URL (repeatable) |
| `--list-models` | `-l` | List supported models |
| `--cost` | `-c` | Show cost estimate |
| `--output-tokens` | | Use output token pricing |
| `--currency` | | USD or INR |
| `--verbose` | `-v` | Detailed output |

### Examples

```bash
# Inline text
python -m scripts.cli -m gpt-4 "Hello, world!"

# File with cost
python -m scripts.cli -f input.txt -m claude-3-opus -c

# Multiple files (OpenClaw audit)
python -m scripts.cli -v -c -f AGENTS.md -f SOUL.md -f MEMORY.md -m gpt-4o

# List models
python -m scripts.cli -l
```

---

## Python API

```python
from scripts import TokenCounter, count_tokens, estimate_cost, get_supported_models

tokens = count_tokens("Hello!", "gpt-4")
counter = TokenCounter("claude-3-opus")
tokens = counter.count_messages([
    {"role": "system", "content": "..."},
    {"role": "user", "content": "..."}
])
cost = estimate_cost(tokens, "gpt-4", input_tokens=True)
```

---

## Supported Models

300+ models across 34+ providers: OpenAI, Anthropic, Google, Meta, Mistral, Cohere, xAI, DeepSeek, etc. Use `python -m scripts.cli -l` for full list.

- **OpenAI:** exact via tiktoken
- **Others:** ~85–95% approximation

---

## Common Issues

| Issue | Action |
|-------|--------|
| "tiktoken is required" | `pip install tiktoken` |
| UnsupportedModelError | Use `-l` for valid names |
| Cost "NA" | Model has no pricing; count still valid |

---

## When to Use

- User asks: token count, prompt length, API cost
- User mentions: OpenClaw context size, memory/persona/skills token usage
- Agent needs: audit workspace token consumption before/after changes

---

## Quick Reference

| Item | Command |
|------|---------|
| Invoke | `python -m scripts.cli` |
| List models | `python -m scripts.cli -l` |
| Cost | `-c` (input) / `--output-tokens` (output) |
| Currency | `--currency USD` or `INR` |
