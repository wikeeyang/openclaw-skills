---
name: owletto-openclaw
description: Install and configure the Owletto memory plugin for OpenClaw, including OAuth login and MCP health verification.
---

# Owletto OpenClaw Setup

Use this skill when a user wants Owletto long-term memory working in OpenClaw.

## Setup Flow

1. Ensure CLI prerequisites are available.

```bash
node --version
pnpm --version
owletto --help
```

2. Install the OpenClaw plugin package.

```bash
openclaw plugins install owletto-openclaw-plugin
```

3. Log in to Owletto for MCP access.

```bash
owletto openclaw login --mcpUrl https://owletto.com/mcp
```

4. Configure OpenClaw plugin settings.

```bash
owletto openclaw configure --mcpUrl https://owletto.com/mcp
```

5. Verify auth + MCP connectivity.

```bash
owletto openclaw health --mcpUrl https://owletto.com/mcp
```

## Notes

- For self-hosted or non-default environments, replace `https://owletto.com/mcp` with the target MCP URL.
- If `openclaw` is not on PATH, install OpenClaw CLI first, then rerun setup.
- If browser login is unavailable, complete OAuth on another machine/browser and rerun from a shell with browser access.
