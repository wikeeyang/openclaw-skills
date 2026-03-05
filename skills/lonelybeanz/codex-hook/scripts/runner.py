#!/usr/bin/env python3
"""
Runner: Spawns a Codex task using openclaw agent in background and records metadata.
"""
import os
import sys
import json
import time
import uuid
import argparse
import subprocess
from datetime import datetime
from pathlib import Path

def load_config():
    """Load codex-hook configuration"""
    config_path = Path.home() / ".config" / "codex-hook" / "config.json"
    if config_path.exists():
        with open(config_path) as f:
            return json.load(f)
    return {
        "result_dir": "/tmp/codex-results",
        "pending_wake_file": "/tmp/codex-results/pending-wake.json",
        "latest_result_file": "/tmp/codex-results/latest.json"
    }

def generate_task_id():
    """Generate unique task ID"""
    timestamp = int(time.time())
    return f"codex-{timestamp}-{uuid.uuid4().hex[:8]}"

def ensure_result_dir(result_dir):
    """Ensure result directory exists"""
    Path(result_dir).mkdir(parents=True, exist_ok=True)
    try:
        Path(result_dir).chmod(0o700)
    except:
        pass

def write_task_meta(task_dir, task_meta):
    """Write task metadata JSON"""
    meta_file = task_dir / "task-meta.json"
    with open(meta_file, 'w') as f:
        json.dump(task_meta, f, indent=2)

def spawn_codex_session(task):
    """
    Spawn Codex task in background using openclaw agent.
    Returns (session_key, pid).
    """
    session_key = f"agent:acp:codex-{task['task_id']}"
    output_file = Path(task['result_dir']) / "output.txt"

    # Build command
    cmd = [
        "openclaw", "agent",
        "--agent", task.get('agent_id', 'codex'),
        "--session-id", session_key,
        "--message", task['prompt'],
        "--timeout", str(task.get('timeout', 3600))
    ]

    # Start process in background, redirect output
    try:
        proc = subprocess.Popen(
            cmd,
            stdout=open(output_file, 'w'),
            stderr=subprocess.STDOUT,
            start_new_session=True  # Detach from parent
        )
        return session_key, proc.pid
    except Exception as e:
        raise RuntimeError(f"Failed to start agent: {e}")

def main():
    parser = argparse.ArgumentParser(description="Run Codex task with hooks")
    parser.add_argument("-t", "--task", required=True, help="Task prompt")
    parser.add_argument("-n", "--name", required=True, help="Task name")
    parser.add_argument("-w", "--workspace", default="~/projects", help="Workspace directory")
    parser.add_argument("--agent-id", default="codex", help="Agent ID from openclaw config")
    parser.add_argument("--model", help="Model override (e.g., openai-codex/gpt-5.2)")
    parser.add_argument("--timeout", type=int, default=3600, help="Total timeout in seconds")
    parser.add_argument("--operation-timeout", type=int, default=300, help="Per-operation timeout")
    parser.add_argument("--context-messages", type=int, default=10, help="Context window size")
    parser.add_argument("--result-dir", help="Override result directory")
    parser.add_argument("--priority", choices=["low", "normal", "high"], default="normal")

    args = parser.parse_args()

    # Load config
    config = load_config()
    result_dir = Path(args.result_dir or config['result_dir'])
    ensure_result_dir(result_dir)

    # Generate task ID and create task directory
    task_id = generate_task_id()
    task_dir = result_dir / "tasks" / task_id
    task_dir.mkdir(parents=True, exist_ok=True)

    # Build task metadata
    task_meta = {
        "task_id": task_id,
        "task_name": args.name,
        "prompt": args.task,
        "workspace": args.workspace,
        "agent_id": args.agent_id,
        "model": args.model,
        "timeout": args.timeout,
        "operation_timeout": args.operation_timeout,
        "context_messages": args.context_messages,
        "priority": args.priority,
        "status": "starting",
        "started_at": datetime.utcnow().isoformat() + "Z",
        "result_dir": str(task_dir)
    }

    # Write initial metadata
    write_task_meta(task_dir, task_meta)

    try:
        # Spawn Codex session in background
        print(f"🚀 Starting Codex task: {task_id}")
        print(f"   Task: {args.name}")
        print(f"   Workspace: {args.workspace}")

        session_key, pid = spawn_codex_session(task_meta)
        task_meta["session_key"] = session_key
        task_meta["pid"] = pid
        task_meta["status"] = "running"

        # Update metadata
        write_task_meta(task_dir, task_meta)

        print(f"✅ Task spawned successfully")
        print(f"   Session: {session_key}")
        print(f"   PID: {pid}")
        print(f"   Task ID: {task_id}")
        print(f"   Monitor: codex-tasks status {task_id}")
        print("")
        print("The watcher will automatically detect completion and send callbacks.")

        # Return task_id (for dispatcher to capture)
        return task_id

    except Exception as e:
        task_meta["status"] = "failed"
        task_meta["error"] = str(e)
        task_meta["completed_at"] = datetime.utcnow().isoformat() + "Z"
        write_task_meta(task_dir, task_meta)
        print(f"❌ Failed to start task: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    result = main()
    if result:
        # Output task_id for dispatcher
        print(f"TASK_ID:{result}")
        sys.exit(0)
    else:
        sys.exit(1)
