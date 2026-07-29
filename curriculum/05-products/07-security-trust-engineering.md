---
id: security-trust-engineering
title: Security and Trust Engineering
track: products
level: intermediate
version: 1.0
Prerequisites: "00-value-engine, 00-personal-operator, 01-jarvis, 02-garden"
Duration: "~45-60 minutes (reading + 3 exercises)"
Format: "Concept lesson with 3 hands-on exercises (threat modeling, access-control policy design, least-privilege audit)"
Future_Topics: "Prompt-Injection Defenses, Secure Tool-Integration Patterns, Red-Teaming Personal Operators, Audit-Trail Schema and Review Workflows, 07-agent-systems Safety and Guardrails, 04-Protocol Engineering Security Modeling"
Related_docs:
  - 01-jarvis
  - 02-garden
  - 07-agent-systems/06-safety-and-guardrails
  - 04-Protocol Engineering/03-advanced/01-lead-architect/03-security-modeling
---

# Security and Trust Engineering

Personal Operators run with access to tools, data, and compute. Securing them requires thinking beyond traditional application security — the threat model includes malicious inputs, compromised tools, prompt injection, and unauthorized access to agent capabilities.

## Core concepts

- **Threat modeling** — identifying what you are protecting, who might attack it, and what vectors they have.
- **Least privilege** — the operator and its tools should have only the access needed for the task at hand.
- **Sandboxing** — isolating agent compute so a compromised operator cannot affect the host system.
- **Access control** — who or what can start, stop, configure, or communicate with an operator.
- **Audit trails** — recording every action an operator takes so behavior can be reviewed after the fact.

## Flow Research context

Jarvis defines the security model and control flow that enforce these boundaries. The protocol's Mutation Gate checks authority, integrity, and policy for every state change. The Gateway controls agent access, the sandboxed VM isolates compute, and the control layer manages lifecycle permissions. WorkStream verification and Harnessy evaluation depend on these guarantees — you cannot trust an operator's output if you cannot trust the governance of its runtime.

## Exercises

1. Write a threat model for a Personal Operator with access to email, a code repository, and a payment API.
2. Design an access control policy for a team of five people sharing one Garden workspace. Who can approve tool connections? Who can deploy skills?
3. Audit an existing system you know against the least privilege principle. Where does it violate it?
