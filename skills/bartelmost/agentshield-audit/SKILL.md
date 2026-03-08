---
name: agentshield-audit
description: Initiate and manage AgentShield security audits for AI agents. Use when a user wants to audit their agent's security posture, generate cryptographic identity keys, obtain security certificates, or verify other agents' trustworthiness. Triggers on phrases like "audit my agent", "get security certificate", "verify agent", or "activate AgentShield".
triggers: ["audit my agent", "get security certificate", "verify agent", "activate AgentShield", "security audit"]
---

# AgentShield Audit Skill

**Audit your agent's security and obtain verifiable trust certificates for inter-agent communication.**

No API key required. No registration. Just install and run.

---

## DEVELOPER NOTE (IMPORTANT)

> **Current Status:** The AgentShield API backend is currently hosted on a Heroku development server. 
> This is a temporary setup for development and testing purposes.
>
> **Migration Plan:** Once all features are integrated and fully tested, the backend will be migrated 
> to a trusted production infrastructure with dedicated infrastructure and audit logging.
>
> **Current Endpoint:** `agentshield-api-bartel-fe94823ceeea.herokuapp.com`
> **Future:** Migration to enterprise-grade hosting with SOC2 compliance planned.

---

## One-Line Quick Start

```bash
clawhub install agentshield-audit && python -m agentshield_audit
```

That's it. Your agent will be audited in ~30 seconds.

---

## The Complete Workflow

```
Step 1: INSTALL
  clawhub install agentshield-audit
         |
         v
Step 2: USER APPROVAL (Human-in-the-Loop)
  Skill asks user permission before reading sensitive files
  (IDENTITY.md, SOUL.md, system prompts)
  User must explicitly approve: "Yes, proceed with audit"
         |
         v
Step 3: AUTO-DETECT (with consent)
  Skill detects agent name & platform
  Only reads files user has approved
         |
         v
Step 4: GENERATE KEYS
  Ed25519 keypair created locally
  Stored in: ~/.agentshield/agent.key
  Private keys NEVER leave your workspace
         |
         v
Step 5: RUN AUDIT (~30 seconds)
  - System Prompt Extraction Test
  - Instruction Override Test
  - Tool Permission Check
  - Memory Isolation Test
  - Secret Leakage Detection
         |
         v
Step 6: RECEIVE CERTIFICATE
  90 days validity
  Verifiable by anyone
```

---

## Human-in-the-Loop: User Consent Required

**IMPORTANT:** Before accessing any potentially sensitive configuration files 
(IDENTITY.md, SOUL.md, system prompts, API keys), AgentShield will:

1. **Ask for explicit user approval** - "Do you want to proceed with the security audit? This will scan your agent configuration."
2. **Show exactly which files will be read** - Full transparency
3. **Never auto-proceed without consent** - No silent scanning
4. **Allow selective opt-out** - User can skip specific tests

The user must explicitly respond with confirmation (e.g., "Yes, proceed", "Approved", "Go ahead") 
before any sensitive file access occurs.

---

## When to Use

- User wants to audit their agent's security
- User wants a trust certificate for their agent
- User wants to verify another agent's certificate
- Setting up inter-agent secure communication
- Before installing untrusted skills

---

## Installation Methods

### Method A: One-Line (Recommended)
```bash
clawhub install agentshield-audit && python -m agentshield_audit
```

### Method B: Step by Step
```bash
# Install the skill
clawhub install agentshield-audit

# Navigate to skill directory
cd ~/.openclaw/workspace/skills/agentshield-audit

# Run with explicit user confirmation
python initiate_audit.py --auto

# The script will prompt:
# "This audit will scan your agent configuration. 
#  Approve reading IDENTITY.md and SOUL.md? (yes/no)"
# User must type "yes" to proceed.
```

### Method C: Manual Specification (No File Reading)
```bash
# Skip auto-detection entirely - user provides info manually
python initiate_audit.py --name "MyAgent" --platform telegram
```

---

## Security Score (0-100)

| Score | Tier | Description |
|-------|------|-------------|
| 90-100 | HARDENED | Passed all critical tests. Top-tier security. |
| 75-89 | PROTECTED | Passed most tests. Minor issues found. |
| 50-74 | BASIC | Minimum requirements met. Room for improvement. |
| <50 | VULNERABLE | Failed critical tests. Immediate action recommended. |

---

## Security Model

- **User Consent Required** - No silent file access, explicit approval needed
- **Private keys never leave** the agent's workspace
- **Challenge-response authentication** prevents replay attacks
- **Certificates signed by AgentShield** and verifiable by anyone
- **90-day validity** encourages regular re-auditing
- **Rate limiting:** 1 audit per hour per IP (prevents abuse)

---

## Script Reference

| Script | Purpose | Example |
|--------|---------|---------|
| `initiate_audit.py` | Start new audit (asks for user consent) | `python initiate_audit.py --auto` |
| `verify_peer.py` | Verify another agent | `python verify_peer.py --agent-id "agent_xyz789"` |
| `show_certificate.py` | Display your certificate | `python show_certificate.py` |
| `audit_client.py` | Low-level API client | Import for custom integrations |

---

## Demo Mode / Free Usage

**First 3 audits are completely free.** No registration, no API key.

After that:
- Rate limit: 1 audit per hour per IP
- No payment required for basic usage
- Enterprise/high-volume: Contact us

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No certificate found" | Run `initiate_audit.py` first |
| "Challenge failed" | Check system clock (NTP sync required) |
| "API unreachable" | Verify internet connection |
| "Rate limited" | Wait 1 hour between audits |
| "User declined" | The user chose not to proceed with the audit |
| Auto-detection failed | Use `--name` and `--platform` manually |

---

## Developer Information

**Version:** 1.0.0
**License:** MIT
**Author:** Kalle-OC (@bartelmost)
**GitHub:** https://github.com/bartelmost/agentshield

**Backend Status:** Development (Heroku) → Production migration planned
**Current API:** agentshield-api-bartel-fe94823ceeea.herokuapp.com

---

## Questions?

Open an issue on GitHub or ping @Kalle-OC on Moltbook.

**Secure yourself. Verify others. Trust nothing by default.**
