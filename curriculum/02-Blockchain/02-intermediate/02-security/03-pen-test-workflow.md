---
id: pen-test-workflow
title: Penetration Testing Workflow
track: blockchain
level: intermediate
version: 1.1
---

# Penetration Testing Workflow

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/h38VYngecJ0"
 title="Penetration Testing for Blockchain Governance Frameworks"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Describe the core phases of a blockchain-oriented penetration-testing workflow.
- Apply a simple pen-test checklist to a Flow-style contract or lab.
- Use pen-testing thinking to design more robust systems (not just "break them").
- Distinguish between **manual testing**, **automated tools**, and **real-world engagements**.

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

**Penetration testing** (often called "pen testing") is the practice of **ethically attacking** a system to find vulnerabilities before real attackers do.
In blockchain, this usually means:

- Testing smart contracts,
- Their surrounding infrastructure (nodes, wallets, APIs),
- And the **economic and governance** rules that drive them.

For Flow Initiative trainees, you will not usually be hired as full-time penetration testers.
But you *will* benefit from learning a **pen-tester-style mindset** so you can:

- design systems that are harder to abuse,
- spot exploitable patterns in labs, and
- understand what "we tested this" actually means.

This lesson focuses on a **workflow** you can mentally apply to any Flow-style contract or ecosystem.

## What Penetration Testing Is (and Isn't)

Penetration testing is:

- A **structured, goal-driven** process.
- Conducted by people or tools that **simulate attackers**.
- Done to **discover exploitable weaknesses**, not just theoretical bugs.

It is **not**:

- A one-off quick scan.
- Guaranteed to find every bug.
- A replacement for good design, testing, or audits.

In blockchain, pen tests are especially valuable because:

- Bugs can be **irreversible** and **high-value**.
- Attackers are **highly motivated** and well-funded.
- Economic models can be exploited in subtle ways (e.g., governance manipulation, MEV-style attacks).

## Core Phases of a Pen-Test Workflow

Most blockchain-oriented pen-test workflows share a few high-level stages:

### 1. Scope and Reconnaissance

Before you touch the code:

- **Define scope**:
 - What contracts, networks, or components are in scope?
 - What is absolutely out of scope (e.g., mainnet, real user funds)?

- **Gather intel (recon)**:
 - Identify public contracts and their addresses.
 - Understand the ecosystem (tokens, oracles, governance, L2s).
 - Collect public docs, ABI, and any known usage patterns.

In Flow-style contexts, this usually means:

- Reading the lab instructions and context,
- Mapping which contracts you are allowed to "attack,"
- Confirming you are on a **local** or **testnet-style** environment.

### 2. Manual Analysis and Threat Modeling

Next, you **think like an attacker**:

- **Threat-modeling questions**:
 - Who would want to attack this?
 - What would they gain (money, governance power, disruption)?
 - What are the "crown-jewel" functions (e.g., minting, pausing, upgrading)?

- **Manual review**:
 - Read the code for the same patterns you learned (`01-common-vulns.md`).
 - Trace state changes and external calls.
 - Map out the **attack surface** (what can you influence).

This is where your earlier lessons pay off:
You already know to look for reentrancy, overflow, access-control over-privileges, and gas-related DoS.

### 3. Automated Scanning

Now you bring in tools:

- **Static analysis** (e.g., Slither, Mythril) to flag common patterns.
- **Security scanners** or IDE-integrated analyzers that highlight potential issues.

These tools help you:

- Find low-hanging-fruit bugs,
- Spot things you missed in manual review,
- Prioritize which functions to attack first.

But tools are not magic:

- They miss **novel** or **design-level** bugs.
- They can generate **false positives**.

So you treat their output as **input** for the next phase, not a final verdict.

### 4. Active Testing and Exploitation

In this phase, you **simulate an attack**:

- **Craft transactions** that exercise edge cases:
 - High-value transfers.
 - Zero- or extreme-value inputs.
 - Strange call sequences (e.g., calling a function twice in a row, or in a specific order).

- **Try to exploit known vulnerability patterns**:
 - Reentrancy: trigger a call that re-enters before updating state.
 - Overflow: push arithmetic beyond safe limits.
 - Access-control bypass: try calling admin-only functions with a non-admin account.

In Flow-style labs, you should:

- Do this **only in local or testnet environments**.
- Clearly distinguish between **learning** and **real-world** engagements.

The goal is **understanding**, not causing real damage.

### 5. Reporting and Remediation

After you find issues:

- **Write a simple report**:
 - What you tested.
 - What vulnerabilities you found.
 - How to reproduce them.
 - Their **impact** (e.g., could drain funds).

- **Suggest fixes**:
 - At a high level, what change would close the vulnerability.
 - What design or pattern would reduce risk.

This is not a full-professional-style audit report.
It is a **structured note** that helps the team improve.

### 6. Retesting

Finally:

- **Retest** the same scenarios after fixes are applied.
- Confirm that the vulnerability is **truly gone**.

This closes the loop and shows that the fix is effective.

## Why This Matters for Flow Engineers

In Flow-style labs:

- You will design and modify contracts that resemble real-world systems.
- You may later work on projects that **actually** pay money or govern communities.
- You will read and write **security-sensitive code**.

By learning a pen-test-style workflow, you:

- Develop **attack-oriented thinking** that helps you **design safer systems**.
- Understand what "we tested this" really means behind the scenes.
- Gain confidence that you can **find and fix** real-world-like issues.

In public-good contexts, this is especially important when:

- Contracts handle real-world assets or incentives.
- Communities must trust the system without a central watchdog.
- Mistakes can have real-life consequences.

## How to Apply This in a Flow-Style Lab

You do not need a full-scale pen-test every time.
But you *can* apply the **mental workflow**:

1. **Scope**: Define what you are allowed to test and in which environment.
2. **Recon**: Read the contract and ecosystem docs.
3. **Manual review**: Apply your vulnerability checklist.
4. **Automated scan**: Run a static analyzer if possible.
5. **Active testing**: Craft transactions that probe edge cases.
6. **Reporting**: Write a short note describing findings and suggested fixes.
7. **Retest**: Confirm changes work.

This is a **lightweight pen-testing practice** that fits Flow-style exploration.

## Implementation Sketch

```yaml
finding:
 severity: high
 impact: funds can be lost or frozen
 proof: failing test or transaction trace
 recommendation: update state before external calls
```

## Practical Exercises

### Exercise 1: Sketch a Simple Pen-Test

Take a small Flow-style contract:

- Sketch a pen-test workflow for it:
 - Scope and recon.
 - What to test.
 - What tools to use.
 - What to check.

Write this as a **mental model**, not code.

### Exercise 2: Build a Personal Checklist

Using what you learned in `01-common-vulns.md` and this lesson, build a **pen-test checklist**:

- Write it as a markdown list.
- Include at least 5 items.
- For each item, add a short explanation.

Keep this in your lab repo and update it as you learn more.

### Exercise 3: Simulate an Attack

In a local or testnet environment:

- Attempt to exploit a known vulnerability (e.g., reentrancy) in a Flow-style contract.
- Document the steps and the outcome.
- Note how you would fix it.

This is a **hands-on⁠-in-a-safe-environment** exercise.

## Self-Assessment

Rate yourself from 1 to 5:

- I can list the main phases of a pen-test workflow.
- I can apply this workflow to a Flow-style contract.
- I can see how pen-testing thinking helps design safer systems.
- I can distinguish between learning and real-world engagements.

Action item: write a short note in your lab repo describing one vulnerability you would test in a Flow-style contract and how you would test it.

## Further Reading

- [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)
- [Solidity security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)
- [Ethereum smart contract security](https://ethereum.org/en/developers/docs/smart-contracts/security/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)

## Next Steps

- Read the next lesson in the security track (e.g., `04-security-best-practices.md`) to see how to integrate this workflow into daily practice.
- Use this pen-test-style mindset every time you design or modify a contract.
- Treat security as a **continuous process**, not a one-time event.

---

*This lesson gives Flow Initiative trainees an engineer-style understanding of a penetration testing workflow for blockchain systems, focusing on how to think like an attacker, apply structured testing, and integrate this mindset into Flow-style labs.*
