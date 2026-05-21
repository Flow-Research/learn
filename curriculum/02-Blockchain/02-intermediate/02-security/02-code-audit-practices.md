---
id: code-audit-practices
title: Code Audit Practices
track: blockchain
level: intermediate
version: 1.1
---

# Code Audit Practices

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/ylP44hSbI1o"
 title="End-to-End Smart Contract Audit"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what a code audit is and why it matters in blockchain systems.
- Follow a simple, repeatable process for reading and reviewing contracts.
- Use checklists and heuristics to spot common issues.
- Write useful, structured audit notes that help the team improve the code.

## Concept Map

```mermaid
flowchart LR
 A["Scope"] --> B["Threat model"]
 B --> C["Review"]
 C --> D["Exploit test"]
 D --> E["Fix verification"]
```

## Quantitative Lens

Prioritize security work by expected loss:

$$
Risk = Impact \times Likelihood
$$

## Introduction

A **code audit** is a focused review of source code to find bugs, vulnerabilities, and design problems *before* deployment.
In blockchain, audits are especially important because:

- Contracts are hard to change after they go live.
- Bugs can lead to irreversible loss of value.
- Security is not just a "nice-to-have"; it is a core part of the product.

In the Flow Initiative, you will not be expected to perform full-blown, professional-grade audits.
You *are* expected to **read critically** and **ask the right questions** when you see a contract.

This lesson teaches you lightweight **audit-style practices** that fit Flow-style labs and onboarding work.

## What Is a Code Audit?

A code audit is:

- A **systematic inspection** of code.
- Done by one or more reviewers.
- Motivated by **risk**, not perfection.

In practice, an audit:

- Identifies **vulnerabilities**, defects, and anti-patterns.
- Documents **assumptions** and **edge cases**.
- Makes **recommendations** for fixes or improvements.

For Flow engineers, the goal is **risk-aware review**, not theoretical completeness.
You do not need to prove the contract is "perfect"; you need to reduce the chance of catastrophic failure.

## Core Principles of Auditing

### 1. Assume the Code Can Be Misused

Treat every contract as if it will be:

- Called by honest and malicious actors.
- Used in unexpected ways.
- Interfaced with many other systems.

This is different from "assuming good faith" in normal software.
Blockchains demand a **threat-modeling mindset**.

### 2. Focus on High-Impact Areas

Auditors usually prioritize:

- Functions that handle **value** (e.g., transfers, minting, burning).
- Functions that control **access** (e.g., owner, admin, upgrade).
- State-changing functions that interact with **external contracts**.

You can copy this priority list in Flow labs:
Spend more time on **value- and access-sensitive** logic; less on read-only helpers.

### 3. Use Checklists and Heuristics

Experienced auditors keep checklists for common issues such as:

- Reentrancy.
- Integer overflow/underflow.
- Access-control flaws.
- Gas-related issues.
- Misconfigured or uninitialized state.

Even if you do not have a professional checklist, you can **build your own** from the vulnerabilities you learned in `01-common-vulns.md`.

### 4. Review the Design, Not Just the Code

An audit is not just about syntax and style. It includes:

- The **contract design** (what it is trying to do).
- The **business logic** (how it enforces rules).
- The **dependencies** (what other contracts or libraries it uses).

This is where Flow-style systems benefit: you can reason about **incentives, tokens, and L1/L2** impacts, not just code.

## How to Audit a Contract (Step-by-Step)

### Step 1: Understand the Purpose

Before reading a line of code, ask:

- What is this contract *for*?
- What problem does it solve?
- What assumptions does it make about the environment?

If the answer is unclear, write a short note that describes the **goal** and **scope**.
This is the **audit context**.

### Step 2: Map the State

List the main state variables:

- Balances, ownership, configuration.
- Who is allowed to read or write each piece?

Ask:

- Is this state well-protected?
- Are there any "dangerous" variables that can freeze or empty the contract?

Map these to the **vulnerability** patterns you know (e.g., overflow, access control).

### Step 3: Trace the Functions

For each function:

- Identify its **purpose** (e.g., transfer, pause, upgrade).
- Check its **visibility** (public, external, internal, private).
- Identify where it **reads or writes state**.
- Mark where it **calls external contracts**.

At this stage, you are not just reading; you are **building a mental model** of the control-flow.

### Step 4: Flag Risky Patterns

Use your checklist:

- **Reentrancy**: does state change after external calls?
- **Overflow**: are there unchecked arithmetic operations?
- **Access control**: who can call this? Is that reasonable?
- **Gas**: are there loops over user-controlled arrays?
- **Initialization**: was the contract set up correctly?

For each pattern you see:

- Label it in your notes.
- Write one sentence describing the risk.
- Suggest a simple fix or workaround.

### Step 5: Write Audit Notes

A good audit note includes:

- The **file and line** being referenced.
- A **short description** of the issue.
- An **impact** statement (e.g., "could allow unauthorized minting").
- A **recommended action** (e.g., "move state update before the call").

You do not need to prove every claim formally. You *do* need to be **clear and actionable**.

## Lightweight Audit Checklist for Flow Labs

You can use this as a template when reviewing any Flow-style contract:

- Is the **state layout** clear and protected?
- Are **value-handling** functions safe from overflow and reentrancy?
- Are **privileged functions** restricted to the right roles?
- Are **gas-hungry** operations bounded or chunked?
- Is the **initialization** obvious and tested?
- Are **external calls** minimized and well-documented?

Score each item 1-5, and write a brief comment where you score low.

## How This Fits Into the Flow Initiative

In Flow labs:

- You will review and modify contracts written by others.
- You will write your own simple contracts.
- You may also join **peer-review** sessions.

Your audit-style mindset helps:

- Catch issues before they are deployed.
- Improve the **quality and safety** of the codebase.
- Develop a **shared understanding** of what "safe" means in your context.

In public-good contexts, this is especially important when:

- Contracts handle real-world assets or incentives.
- Communities must trust the system without a central authority.
- Mistakes can have significant real-life consequences.

## Implementation Sketch

```yaml
finding:
 severity: high
 impact: funds can be lost or frozen
 proof: failing test or transaction trace
 recommendation: update state before external calls
```

## Practical Exercises

### Exercise 1: Perform a Mini-Audit

Take a small contract from a Flow lab:

- Follow the five-step audit process above.
- Write a short audit note (no more than one page) describing:
 - What the contract is for.
 - What state it stores.
 - What risky patterns you see.
 - What you would change.

This is a **real-world-style exercise**, even if you never deploy it.

### Exercise 2: Build a Personal Checklist

Using what you learned in `01-common-vulns.md` and this lesson, build a **personal auditing checklist**:

- Write it as a markdown list.
- Include at least 5 items.
- For each item, add a short explanation.

Keep this in your lab repo and update it as you learn more.

### Exercise 3: Peer Review

If you are in a cohort or community:

- Trade contracts with a peer.
- Each of you audits the other's code using the checklist.
- Share your notes and discuss.

This is how you build **collaborative security culture**.

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what a code audit is.
- I can follow a simple step-by-step process to review a contract.
- I can use a checklist to spot common issues.
- I can write useful audit notes.

Action item: write a short note in your lab repo describing one risk you would flag in a Flow-style contract and how you would reduce it.

## Further Reading

- [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)
- [Solidity security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)
- [Ethereum smart contract security](https://ethereum.org/en/developers/docs/smart-contracts/security/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)

## Next Steps

- Read the next lesson in the security track (e.g., `03-formal-checking-and-tools.md`) to see how tools can help automate parts of auditing.
- Use this audit-style practice every time you open a contract.
- Treat security as a **team sport**, not an individual skill.

---

*This lesson gives Flow Initiative trainees an engineer-style understanding of code audit practices, focusing on how to read, review, and document contracts for security and reliability, and how to build lightweight, repeatable audit workflows in Flow-style labs.*
