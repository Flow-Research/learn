---
id: security-trust-engineering
title: Security and Trust Engineering
---

# Security and Trust Engineering

Personal Operators run with access to tools, data, and compute. Securing them requires thinking beyond traditional application security — the threat model includes malicious inputs, compromised tools, prompt injection, and unauthorized access to agent capabilities.

## Core concepts

- **Threat modeling** — identifying what you are protecting, who might attack it, and what vectors they have.
- **Least privilege** — the operator and its tools should have only the access needed for the task at hand.
- **Sandboxing** — isolating agent compute so a compromised operator cannot affect the host system.
- **Access control** — who or what can start, stop, configure, or communicate with an operator.
- **Audit trails** — recording every action an operator takes so behavior can be reviewed after the fact.

## Flow context

Jarvis includes the security and sentinel systems that enforce these boundaries. The Jarvis Gateway controls agent access, the sandboxed VM isolates compute, and the control layer manages lifecycle permissions. WorkStream verification and Harnessy evaluation depend on these guarantees — you cannot trust an operator's output if you cannot trust its runtime.

## Exercises

1. Write a threat model for a Personal Operator with access to email, a code repository, and a payment API.
2. Design an access control policy for a team of five people sharing one Garden workspace. Who can approve tool connections? Who can deploy skills?
3. Audit an existing system you know against the least privilege principle. Where does it violate it?
