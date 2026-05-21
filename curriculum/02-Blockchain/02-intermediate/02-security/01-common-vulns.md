---
id: common-vulns
title: Common Vulnerabilities
track: blockchain
level: intermediate
version: 1.1
---

# Common Vulnerabilities

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

- Recognize the most common smart-contract vulnerabilities (e.g., reentrancy, integer overflow, front-running).
- Map each vulnerability to the system properties it exploits (shared state, gas, visibility).
- Use a "defensive mindset" when reading or writing contracts.
- Avoid blindly copying patterns from the web without checking for known flaws.

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

Smart contracts are powerful because they are **public, persistent, and executable**.
But this same power makes them a target for **very specific, very predictable** vulnerabilities.

In the Flow Initiative, you will not be expected to discover new classes of bugs.
You *are* expected to **avoid the common ones** and to **recognize them quickly** when you see them in code.

This lesson focuses on:

- High-impact, well-known vulnerabilities,
- How they appear in real-world contracts, and
- Simple engineering rules you can follow in Flow-style labs.

You will practice **reading for danger**, not just reading for correctness.

## What a "Vulnerability" Means Here

In blockchain systems, a **vulnerability** is a flaw that lets an attacker:

- Steal or block value,
- Disrupt service, or
- Extract information or control.

Unlike regular web apps, many of these flaws are **strictly deterministic** and **exploitable forever** once the contract is deployed.

So your goal is to **anticipate** and **prevent** them, not just react.

## Common Vulnerability Patterns

### 1. Reentrancy

**What it is:**
A contract calls an external contract, and that external contract calls back into the original contract before the first call finishes.
This can allow the attacker to:

- Drain balances multiple times,
- Bypass checks, or
- Lock up state.

**Why it happens:**
- State is updated **after** external calls.
- The attacker triggers the call, then re-enters the same function.

**Defensive rule:**
- Update state **before** making external calls (the **checks-effects-interactions** pattern).
- In Flow-style contracts, prefer simple, non-reentrant designs.

### 2. Integer Overflow / Underflow

**What it is:**
A number calculation grows beyond the maximum or minimum that the data type can hold.
On older chains, this could wrap around silently, leading to:

- Fake balances,
- Incorrect allowances, or
- Unauthorized actions.

**Why it happens:**
- Developers assume inputs are "reasonable."
- No explicit bounds checking.

**Defensive rule:**
- Use **safe math libraries** or modern compilers that revert on overflow.
- Sanitize inputs and never trust external numbers without checks.

### 3. Access-Control Issues

**What it is:**
Incorrect or missing access control lets unauthorized actors:

- Upgrade contracts,
- Pause or unpause,
- Mint or burn tokens, or
- Change configuration.

**Why it happens:**
- Owner or admin roles are too powerful.
- No role-based structure or too many privileged functions.

**Defensive rule:**
- Grant the **minimum necessary privileges**.
- Prefer **role-based schemes** over single-owner models.
- Force multi-party control for critical operations.

### 4. Gas-Related Issues (Gas Limit, Denial of Service)

**What it is:**
A contract's gas cost can be **too high** or **too low**, depending on the vulnerability:

- **Gas limit exceeded**: the function cannot finish, so it reverts.
- **Denial of Service (DoS)**: an attacker forces the gas cost to be so high that the function is unusable.

**Why it happens:**
- Operations that scale with user count (e.g., dynamic loops).
- Unbounded external calls.

**Defensive rule:**
- Avoid unbounded loops over user-controlled data.
- Chunk work into multiple transactions.
- Profile gas usage under realistic load.

### 5. Front-Running and MEV-Like Patterns

**What it is:**
An attacker sees a pending transaction and acts before it or in response to it, extracting value.
This is common in:

- Auctions,
- Marketplaces,
- On-chain games.

**Why it happens:**
- Transactions are public in the mempool.
- Timing matters more than in traditional systems.

**Defensive rule:**
- Design flows that are **less sensitive to timing order** when possible.
- Use commitments and reveals, or private order-flow solutions where feasible.
- As a first-level, **assume transactions are public and inspectable**.

### 6. Uninitialized or Misconfigured State

**What it is:**
A contract deploys with state that is:

- Not initialized correctly, or
- Configured in a way that breaks assumptions.

This can lead to:

- Lost funds,
- Disabled functions, or
- Confusion about who owns what.

**Why it happens:**
- Deployment scripts skip initialization steps.
- Tests pass in a controlled environment but fail in production.

**Defensive rule:**
- Write a clear **initialization plan** for the contract.
- Test the **deploy-init-use** flow end-to-end.
- Never assume default values are safe.

## Why These Patterns Matter for Flow Engineers

Flow Initiative trainees will work on:

- **Token-style contracts** (balances, allowances),
- **Upgradeable patterns**,
- **State-machine-style systems**.

Each of these is fertile ground for the vulnerabilities above.

Your job is to:

- **Read** contracts with an eye for these patterns.
- **Write** contracts that explicitly avoid the common traps.
- **Document** the assumptions and limitations you've accepted.

In public-good contexts, this is especially important when:

- Contracts handle real-world assets or incentives.
- Communities must trust the system without a central watchdog.
- Mistakes can have real-life consequences.

## How to Practice "Reading for Danger"

When you open a contract (Flow lab or example):

1. **Check state**
 - Where is the critical data (balances, ownership, configuration)?
 - Is it updated before or after external calls?

2. **Check functions**
 - Which functions are privileged?
 - What are their gas costs?
 - Do they loop over user-controlled data?

3. **Check external calls**
 - Where do they call outside contracts?
 - Could those contracts call back into the same contract?

4. **Check deployment and init**
 - How is the contract initialized?
 - Who owns it?
 - Can it be upgraded?

This is a **checklist mindset**, not a one-off inspection.

## Implementation Sketch

```yaml
finding:
 severity: high
 impact: funds can be lost or frozen
 proof: failing test or transaction trace
 recommendation: update state before external calls
```

## Practical Exercises

### Exercise 1: Label a Vulnerable Snippet

Find a small, public-domain example of a contract that has a known vulnerability (e.g., reentrancy or integer overflow):

- Identify the vulnerability and label it with its name.
- Mark in the code where the risky pattern appears.
- Write a short note describing how you would fix it at a high level.

Do not actually deploy anything; keep this in a notes file.

### Exercise 2: Sketch a "Safe Skeleton"

Sketch a simple contract "skeleton" that:

- Stores balances,
- Has a `transfer` function,
- And a privileged `pause` function.

Then, annotate:

- Where the vulnerable patterns could appear.
- How you would avoid them (e.g., update state first, use safe math, restrict access).

This is a **design sketch**, not a full implementation.

### Exercise 3: Relate to a Flow Lab

Look at a Flow-style blockchain lab that uses a contract:

- Identify one place where a common vulnerability *could* appear (e.g., unbounded loop, external call, missing access control).
- Write a short note describing how you would change the design to make it safer.
- If you feel confident, propose a small, concrete code change (even if you don't run it).

## Self-Assessment

Rate yourself from 1 to 5:

- I can name at least three common vulnerabilities (e.g., reentrancy, overflow, access control).
- I can explain how each one works in plain language.
- I can see where they might appear in simple contracts.
- I can list at least one defensive rule for each.

Action item: write a short note in your lab repo describing which vulnerability you find hardest to avoid and why.

## Further Reading

- [OWASP Smart Contract Top 10](https://owasp.org/www-project-smart-contract-top-10/)
- [Solidity security considerations](https://docs.soliditylang.org/en/latest/security-considerations.html)
- [Ethereum smart contract security](https://ethereum.org/en/developers/docs/smart-contracts/security/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)

## Next Steps

- Read the next lesson in the security track (e.g., `02-formal-checking-and-tools.md`) to see how tools can help automate some of this inspection.
- Use this "vulnerability-reading" habit every time you look at a new contract.
- Treat security as a **continuous practice**, not a one-time exam.

---

*This lesson gives Flow Initiative trainees an engineer-style understanding of the most common smart-contract vulnerabilities, focusing on reentrancy, overflow, access control, gas-related issues, front-running, and misconfigured state, and how to read and avoid them in practical labs.*
