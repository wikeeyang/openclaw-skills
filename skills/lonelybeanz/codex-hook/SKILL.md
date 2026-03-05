# Skill: codex-hook

Task scheduler and callback system for OpenAI Codex CLI. Enables asynchronous code execution with automatic completion notifications, integration with OpenClaw heartbeat, and multi-channel callbacks (Telegram, webhook, pending-wake).

## 🎯 Overview

`codex-hook` is a task scheduling and callback system for OpenAI Codex CLI in OpenClaw. Enables asynchronous code execution with automatic completion notifications.

**Key Features:**

- ✅ **Async dispatch** - Submit tasks without blocking
- ✅ **Session isolation** - Each task runs in isolated sub-session
- ✅ **Auto callbacks** - Telegram, webhook, AGI heartbeat integration
- ✅ **State tracking** - Persistent metadata and outputs
- ✅ **Retry & timeout** - Built-in failure handling
- ✅ **Git integration** - Auto-capture recent commits and modified files

## Quick Reference

```bash
# Dispatch a task (async, returns immediately)
dispatch-codex.sh \
  -t "Implement user authentication API" \
  -n "auth-api" \
  -w "~/projects/backend" \
  -g "-1003884099816" \
  -c "telegram" \
  --timeout 3600

# Check task status
codex-tasks list          # Show all tasks
codex-tasks status TASK_ID  # Show specific task

# Configure default callback channel
codex-tasks config --default-channel telegram --default-group "-100123"
```

## Architecture

```
dispatch-codex.sh
  │
  ├─ 写入 task-meta.json (任务元数据)
  ├─ 调用 runner.py → sessions_spawn 启动 Codex 子会话
  │   └─ 返回 task_id
  │
  └─ 立即返回 task_id 给用户 (不阻塞)
      │
      └─ watcher.py (后台监听)
          │
          ├─ 轮询 sessions_list 检查状态
          ├─ 检测完成 → 读取 transcript
          ├─ 写入结果文件 (latest.json, pending-wake.json)
          ├─ 发送 Telegram 通知 (如果配置)
          ├─ 调用 webhook (如果配置)
          └─ 更新任务状态为 completed/failed
```

## 📦 Installation

### 1. Copy scripts to PATH

```bash
mkdir -p ~/bin
cp skills/codex-hook/scripts/* ~/bin/
chmod +x ~/bin/*

# Ensure ~/bin is in PATH
echo 'export PATH="$HOME/bin:$PATH"' >> ~/.zshrc
source ~/.zshrc
```

### 2. Create Codex agent (once)

```bash
openclaw agents add codex --workspace ~/projects --model openai-codex/gpt-5.2 --non-interactive
```

### 3. Configure defaults (optional)

```bash
codex-tasks config --set default_channel telegram
codex-tasks config --set default_group "YOUR_GROUP_ID"  # Replace with actual group ID
codex-tasks config --set result_dir "$HOME/.local/share/codex-hook/results"
```

## 🚀 Quick Start

### Dispatch a task

```bash
dispatch-codex.sh \
  -t "Your task description" \
  -n "task-name" \
  -w "~/projects" \
  --timeout 3600
```

**Example:**

```bash
dispatch-codex.sh \
  -t "Create a Python script that implements a simple REST API" \
  -n "rest-api" \
  -w "~/dev/project" \
  --timeout 1800
```

Output:
```
✅ Task dispatched: codex-1740857284-a1b2c3d4
   Monitor: codex-tasks status codex-1770857284-a1b2c3d4
```

### Monitor tasks

```bash
# List all tasks (most recent first)
codex-tasks list

# Show task details
codex-tasks status <task_id>

# Watch continuously (in separate terminal)
while true; do clear; codex-tasks list; sleep 2; done
```

### Enable Telegram notifications

1. Set `default_group` in config:
```bash
codex-tasks config --set default_group "-100xxxxxxxxxx"
```

2. Dispatch with callback:
```bash
dispatch-codex.sh \
  -t "Refactor authentication module" \
  -n "refactor-auth" \
  -c telegram \
  -g "-100xxxxxxxxxx"
```

When task completes, you'll receive a Telegram message with:
- Task name and status
- Duration
- Output summary
- Recent git commits (if workspace is a git repo)
- Modified files list

### Heartbeat integration (for AGI)

Add to your AGI's heartbeat routine:

```bash
# Process pending completions
process-codex-callbacks
```

This reads `pending-wake.json` and marks entries as processed.

## 📋 Commands

| Command | Description |
|---------|-------------|
| `dispatch-codex.sh -t "task" -n "name"` | Dispatch new task (required: -t, -n) |
| `codex-tasks list` | List all tasks |
| `codex-tasks status <id>` | Show task details |
| `codex-tasks cancel <id>` | Cancel running task |
| `codex-tasks retry <id>` | Retry failed task |
| `codex-tasks cleanup --days N` | Delete tasks older than N days |
| `codex-tasks config --set key val` | Set config option |
| `process-codex-callbacks` | Process pending wake entries |
| `start-codex-daemon.sh` | Start watcher daemon |
| `stop-codex-daemon.sh` | Stop watcher daemon |

## 🔧 Configuration

### Config file: `~/.config/codex-hook/config.json`

```json
{
  "result_dir": "/tmp/codex-results",
  "pending_wake_file": "/tmp/codex-results/pending-wake.json",
  "latest_result_file": "/tmp/codex-results/latest.json",
  "default_channel": "telegram",
  "default_group": "YOUR_GROUP_ID",
  "default_webhook_url": "",
  "poll_interval": 5,
  "max_concurrent": 4,
  "heartbeat_integration": true,
  "archive_days": 30,
  "output_max_chars": 4000,
  "retention": {
    "completed": 30,
    "failed": 7,
    "running": 1
  }
}
```

### Configuration options

- `result_dir` - Where task data is stored
- `default_channel` - Default notification channel (telegram, webhook)
- `default_group` - Default target group/channel ID
- `poll_interval` - How often watcher checks task status (seconds)
- `max_concurrent` - Maximum concurrent tasks (not enforced yet)
- `heartbeat_integration` - Write to pending-wake.json for AGI heartbeat
- `output_max_chars` - Max output characters to store/notify
- `retention` - How long to keep tasks by status

## 📁 Output Files

### Directory structure

```
result_dir/
├── latest.json                      # Latest completed task
├── pending-wake.json               # Append-only log for heartbeat
├── tasks/
│   └── <task_id>/
│       └── task-meta.json          # Task metadata
├── archives/
│   └── YYYY-MM/
│       └── <task_id>.json
└── logs/
    └── watcher.log
```

### `latest.json`

```json
{
  "task_id": "codex-1740857284-a1b2c3d4",
  "task_name": "rest-api",
  "status": "completed",
  "started_at": "2026-03-01T20:30:00Z",
  "completed_at": "2026-03-01T20:35:00Z",
  "duration_seconds": 300,
  "exit_code": 0,
  "output": "Full task output...",
  "output_truncated": false,
  "session_key": "agent:acp:codex-a1b2c3d4",
  "workspace": "~/dev/project"
}
```

### `pending-wake.json` (JSONL)

```json
{
  "task_id": "codex-1740857284-a1b2c3d4",
  "task_name": "rest-api",
  "status": "completed",
  "completed_at": "2026-03-01T20:35:00Z",
  "summary": "Created REST API with Flask",
  "processed": false,
  "callback_channels": ["telegram:-100xxxxx"]
}
```

## 🔔 Notification Channels

### Telegram

Set `default_group` in config, then either:

1. Configure globally (used for all tasks):
```bash
codex-tasks config --set default_group "-100xxxxxxxxxx"
```

2. Specify per-task:
```bash
dispatch-codex.sh -t "task" -n "name" -c telegram -g "-100xxxxxxxxxx"
```

**Notification format:**

```
🤖 Codex Task Completed
📋 Task: rest-api
⏱️ Duration: 5m 30s
📊 Status: completed

📝 Output Summary:
```
Successfully created Flask REST API.
- Implemented User and Post endpoints
- Added error handling
- Wrote unit tests
```

📁 /home/user/project
📂 Recent commits:
  • abc1234 Add REST API implementation
  • def5678 Update requirements.txt

📝 Modified files:
  • app.py
  • models.py
  • tests/test_api.py
  • requirements.txt
```

### Webhook

```bash
dispatch-codex.sh \
  -t "task" \
  -n "name" \
  -c webhook \
  --webhook-url "https://your-server.com/api/codex/callback"
```

**POST payload:**

```json
{
  "task_id": "codex-1740857284-a1b2c3d4",
  "task_name": "rest-api",
  "status": "completed",
  "completed_at": "2026-03-01T20:35:00Z",
  "duration_seconds": 300,
  "exit_code": 0,
  "output": "Full output text...",
  "output_truncated": false,
  "session_key": "agent:acp:codex-a1b2c3d4",
  "workspace": "~/dev/project"
}
```

### Multiple callbacks

```bash
dispatch-codex.sh \
  -t "task" \
  -n "multi" \
  -c telegram -g "-100111" \
  -c webhook --webhook-url "https://api/callback"
```

## 🔄 Heartbeat Integration

Your main AGI can automatically react to task completions:

```bash
#!/bin/bash
# In heartbeat routine

PENDING_WAKE="$HOME/.config/codex-hook/pending-wake.json"

if [ -f "$PENDING_WAKE" ]; then
    process-codex-callbacks "$PENDING_WAKE" --no-mark > /tmp/new-completions.json
    
    # Read and react to new completions
    jq -r '.tasks[] | "\(.task_name) - \(.status)"' /tmp/new-completions.json | while read line; do
        # Send notification or trigger actions
        echo "Task completed: $line"
    done
    
    # Mark as processed
    process-codex-callbacks "$PENDING_WAKE"
fi
```

## How It Works

### 1. Task Dispatch (`dispatch-codex.sh`)
- Generates unique `task_id`
- Writes `task-meta.json` to result directory
- Calls `runner.py` which uses `sessions_spawn` to start Codex
- Returns `task_id` immediately

### 2. Task Execution (`runner.py`)
- Configures Codex agent with proper workspace, model, tools
- Sets timeouts and context limits
- Logs session key to result directory
- Exits (Codex runs in background)

### 3. Status Watching (`watcher.py`)
- Runs as daemon (or triggered by cron)
- Polls `sessions_list` for tasks in `meta/`
- Detects completion (status=completed, aborted, or timeout)
- Extracts output from `sessions_history`
- Triggers callbacks

### 4. Callback Handling (`callback.py`)
- Sends Telegram message (if configured)
- POSTs to webhook (if configured)
- Writes `latest.json` and `pending-wake.json`
- Marks task as processed

## 🛠️ Advanced Usage

### Custom agent and model

```bash
dispatch-codex.sh \
  -t "Complex task" \
  -n "complex" \
  --agent-id "codex-backend" \
  --model "openai-codex/gpt-5.2" \
  --context-messages 20 \
  --timeout 7200
```

### Workspace-specific tasks

```bash
dispatch-codex.sh \
  -t "Refactor frontend components" \
  -n "frontend-refactor" \
  -w "~/projects/frontend" \
  --timeout 3600
```

### Priority tasks

```bash
dispatch-codex.sh \
  -t "Security patch CVE-2026-1234" \
  -n "security-patch" \
  --priority high
```

## 📊 Monitoring

### Real-time dashboard

```bash
watch -n 2 'codex-tasks list --limit 10'
```

### Check daemon log

If running watcher daemon:
```bash
tail -f /tmp/codex-results/logs/daemon.log
```

### Disk usage

```bash
du -sh /tmp/codex-results/tasks/
du -sh /tmp/codex-results/archives/
```

### Cleanup old tasks

```bash
# Using built-in command
codex-tasks cleanup --days 30

# Or manually
find /tmp/codex-results/tasks -type d -mtime +30 -exec rm -rf {} \;
```

## 📝 Examples

### CI/CD Integration

```bash
#!/bin/bash
# Run tests asynchronously
TASK_ID=$(dispatch-codex.sh \
  -t "Run full test suite and generate coverage report" \
  -n "ci-tests" \
  -w "~/project" \
  --timeout 1800 \
  --webhook-url "https://ci.example.com/callback/codex" \
  | grep 'TASK_ID:' | cut -d: -f2 | tr -d ' ')

echo "Tests running, task ID: $TASK_ID"
# CI server receives webhook when done
```

### Bulk refactoring

```bash
# Refactor multiple components in parallel
for component in Navbar Footer Sidebar; do
  dispatch-codex.sh \
    -t "Refactor $component to TypeScript + Hooks" \
    -n "refactor-$component" \
    -w "~/project/src/components" \
    --timeout 1200 &
done
wait
```

### Scheduled code review

```bash
# In crontab (weekly review)
0 9 * * 1 dispatch-codex.sh \
  -t "Review all changes from last week, check security issues" \
  -n "weekly-review" \
  -w "~/project" \
  --timeout 7200 \
  -c telegram -g "YOUR_GROUP_ID"
```

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| Tasks not starting | 1. Check agent exists: `openclaw agents list`<br>2. Check Codex auth: `codex login status` |
| No Telegram messages | 1. Verify `default_group` is set correctly in config<br>2. Verify bot token and group ID in config |
| Watcher not detecting completion | 1. Check daemon is running (if using daemon)<br>2. Increase `poll_interval` in config<br>3. Check `sessions_list` manually |
| Output truncated | Increase `output_max_chars` in config (default 4000) |
| Permission denied | Ensure result directory is writable (chmod 700) |
| Task stuck in "running" | 1. Check `ps` for hanging process, use `codex-tasks cancel`<br>2. Check `sessions_list` for hanging sessions, may need manual cancel |

## Performance & Limits

- **Polling overhead**: Minimal (2-5s interval typical)
- **Concurrent tasks**: Controlled by `max_concurrent` (default 4)
- **Output storage**: 4000 chars by default (configurable)
- **Archive retention**: 30 days completed, 7 days failed (configurable)

## Security Considerations

- Result directory should be writable only by owner (chmod 700)
- Webhook URLs should use HTTPS in production
- Task output may contain sensitive data; consider sanitizing before callbacks
- Limit `max_concurrent` to avoid resource exhaustion

## License

Part of OpenClaw ecosystem. Compatible with OpenClaw License.
