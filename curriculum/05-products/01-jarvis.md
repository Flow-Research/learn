---
id: jarvis
title: Jarvis
---

# Jarvis

Jarvis is a **governed human-agent collaboration and shared learning protocol**. It defines the records, operations, and boundaries required for humans and AI agents to work together effectively — ensuring work is reviewable, attributable, and portable across sessions.

**Jarvis is not** a product, runtime, backend service, SDK, database, sandbox, or cloud stack. It does not own execution; it only defines the records of that execution. The **Host** (the system running the agent) owns execution.

## Four-Layer Architecture

Jarvis separates its responsibilities into four layers:

| Layer | What it defines |
|---|---|
| **1. Protocol Semantics** | Collaboration and shared learning between humans and agents |
| **2. Protocol Objects** | Data structures — `WorkSession`, `Policy`, `Request`, `Review`, `Takeover`, `EvidenceManifest`, `LearningRecord`, `MemoryProposal` |
| **3. Protocol Operations** | Allowed actions — `create WorkSession`, `record Review`, `export EvidenceManifest`, etc. |
| **4. OpenAPI 3.1 Binding** | HTTP paths, JSON schemas, and security schemes |

Anything related to UI, databases, or model providers is **outside Jarvis** and belongs to the Host implementation.

## Core Protocol Objects (v0.1 "Spine")

The minimum objects required to prove a collaboration loop:

- **WorkSession** — the primary container and source of truth for a task or period of work
- **Policy** — human-defined boundaries for what an agent can and cannot do
- **Request** — a scoped blocker created when an agent is blocked or acting outside Policy (a formal control-plane object, not a chat message)
- **Review** — a human's response to a Request (Approve, Deny, Narrow, Correct, or Needs Revision)
- **Takeover** — human takes manual control, creating a lock epoch that rejects further autonomous agent actions until resolved
- **EvidenceManifest** — a record of work evidence captured during the session
- **LearningRecord / MemoryProposal** — governed objects capturing what was learned to improve future WorkSessions

## Core Architecture Principles

- **Protocol-only:** Jarvis defines the records; the Host owns execution.
- **Human-Agent Team:** The primary unit of value is collaboration between a `HumanWorker` and an `AgentWorker`.
- **Policy-Governed Autonomy:** Agent actions become official protocol state only after a `PolicyDecision`.
- **Human Judgment Central:** Human authority is preserved via `Requests`, `Reviews`, and `Takeovers`.
- **Attributable Contribution:** Contributions of humans, agents, and services remain distinguishable.
- **Governed Learning:** Learning records and memory updates cannot silently mutate state — they must be governed and reviewable.

## Control Flow & Zero-Trust Security

Every mutation to protocol state passes through a **Mutation Gate** that checks:

- **Authority:** Is the actor authorized?
- **Integrity:** Does the `Previous-Event-Hash` match?
- **Policy:** Is there a `PolicyDecision` allowing this action?

**Control flow invariants:**

- Actions inside Policy record events and evidence.
- Actions outside Policy **must** create a Request.
- Agents cannot execute a blocked action until a human provides a Review or Takeover.

## Ecosystem Integration

Jarvis integrates with — but does not replace — existing agent protocols:

- **MCP (Model Context Protocol):** Jarvis records tool/resource use as `PolicyDecisions` and `Evidence`.
- **A2A (Agent-to-Agent):** Jarvis records delegation evidence and participating agent references.
- **Agent SDKs:** Jarvis records the policy, review, and contributions around execution.
- **AG-UI:** Jarvis records how a host exposes its session to a frontend.

## Roadmap & v0.1 Scope

The initial protocol focuses on locking the **spine** — the core contract and OpenAPI schemas. Deferred items include Notifications, ProgressUpdate objects, collaboration metrics, Initiative Balance, and multi-agent reviewer protocols.

## How it fits

Jarvis is the protocol layer on which Flow Research's products (Garden, WorkStream, Harnessy) are built. It provides the governed collaboration and shared learning foundation that makes Personal Operators trustworthy and accountable.
