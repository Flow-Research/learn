---
id: contract-design-patterns
title: Contract Design Patterns
track: blockchain
level: intermediate
version: 1.1
---

# Contract Design Patterns

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/da52yRwWi1E"
 title="Smart contract design patterns"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Identify common on-chain design patterns (modular, upgradeable, token-like contracts).
- Recognize standard patterns such as ERC-20, ERC-721, and basic access control.
- Map patterns to trade-offs in security, upgradeability, and composability.
- Use this pattern sense when you read or write contracts in Flow labs.

## Concept Map

```mermaid
flowchart TD
 A["Source code"] --> B["Compiler"]
 B --> C["Bytecode"]
 C --> D["Deployment"]
 D --> E["Contract calls"]
```

## Quantitative Lens

Every state-changing call has a cost:

$$
Total\ fee = gasUsed \times gasPrice
$$

## Introduction

Writing a smart contract is not just about syntax; it is about **architectural style**.
The same business logic can be written in many ways, with very different consequences for:

- security,
- upgradeability,
- gas cost, and
- how easy it is to compose with other contracts.

In the Flow Initiative, you will see many contracts that reuse well-known patterns.
This lesson teaches you to **recognize** those patterns, not just write them from scratch.

You do not need to memorize every line. You need to develop **pattern-level intuition** so that when you open a contract, you can quickly answer:

- "What is this trying to do?"
- "What assumptions is it making?"
- "What risks does this pattern introduce?"

## What Is a Design Pattern?

In software engineering, a **design pattern** is a proven way to solve a recurring problem.
In smart contracts, the problems are:

- How to represent balances and tokens.
- How to grant and revoke permissions.
- How to upgrade code without breaking data.
- How to compose multiple contracts safely.

A pattern is **not** a piece of code you copy-paste blindly. It is a **concept** that you adapt to your context.

For Flow trainees, this is especially important because:

- You will read and modify many contracts.
- You will mix them with L1/L2 and token-based incentives.
- You will need to **change, not just consume**, existing patterns.

## Common Patterns in Contracts

### 1. Token-Like Contracts (ERC-20, ERC-721)

Many contracts are built around **tokens** - fungible (ERC-20-style) or non-fungible (ERC-721-style).

Key traits:

- A **mapping** from addresses to balances or IDs.
- Core functions like `transfer`, `approve`, and `allowance`.
- Events like `Transfer` and `Approval` for front-ends and indexers.

From an engineer's view:

- The pattern defines **who can move value** and **how transparency works**.
- You can specialize it for Flow-internal tokens, governance tokens, or local lab currencies.

### 2. Modular Contracts (Libraries and Interfaces)

Large systems rarely live in one file.
Common patterns:

- **Libraries** - reusable code for math, data structures, or utilities.
- **Interfaces** - abstract descriptions of what a contract can do, without implementation.
- **Inheritance** (in Solidity) - reusing logic across multiple contracts.

Advantages:

- Avoid duplicating logic.
- Make upgrades and changes more localized.
- Support composability: many contracts calling each other.

Disadvantages:

- Extra complexity: you must reason about multiple files.
- Harder to audit if the call graph is deep.

### 3. Upgradeable Contracts (Proxy Patterns)

Blockchains are immutable, but business rules change.
To reconcile this, teams use **upgradeable patterns**:

- A **proxy** contract that stores the address of the real implementation.
- An **implementation** contract that can be replaced.
- An **admin** (or DAO) that controls upgrades.

From an engineer's view:

- This pattern trades **trust** (who controls the admin?) for **flexibility**.
- It is common in production protocols but riskier for trustless systems.

In Flow labs, you may see simplified proxies for experimentation, without deploying them to real funds.

### 4. Access Control (Ownable, Roles)

Many contracts control who can do what.
Common patterns:

- **Ownable** contracts - one "owner" with special privileges.
- **Role-based access** - groups of users with defined permissions (e.g., "admin", "minter").

You will see:

- A `require` statement that checks a role before allowing an action.
- Events that log role changes.

This is basic **on-chain authorization**.
For Flow engineers, it is important to ask:

- Who controlled the initial role assignments?
- How can those roles change over time?

### 5. State Machine-Style Contracts

Some contracts model **state machines**. For example:

- A "workflow" with steps like `Created` -> `Funded` -> `Locked` -> `Completed`.
- Each function can only be called in a specific state.

Patterns:

- An explicit `state` variable that tracks where the contract is.
- Guards at the start of functions that check the state.

This is a **safety pattern** that prevents invalid transitions and clarifies the system's behavior.

### 6. Composable Contracts (Delegation, Hooks)

In real-world protocols, contracts are rarely isolated.
Common patterns:

- **Delegation** - one contract forwards calls to another.
- **Hooks** - callback functions that let other contracts react to specific events.

These are how:

- Token contracts integrate with governance,
- Oracles feed data into logic,
- Or L2s coordinate with L1s.

Composability is powerful but increases complexity; you must reason about the whole graph.

## Why Patterns Matter for Security

Design patterns shape security:

- A token pattern that uses `transferFrom` and `allowance` must be careful about **reentrancy** and **malicious approvals**.
- An upgradeable pattern that centralizes control introduces **single-point-of-failure risk**.
- A state-machine pattern can prevent some bugs but can be bypassed if the state is not enforced correctly.

As an engineer, you should:

- Recognize the pattern first.
- Then ask: "What are the canonical attacks on this pattern?"
- And finally, "Does this specific instance handle them?"

You will not prevent all bugs, but you can avoid repeating well-known mistakes.

## How This Fits Into the Flow Initiative

In Flow labs:

- You will see **ERC-20-style tokens** for internal use or examples.
- You will see **modular contracts** that reuse logic.
- You may see **upgradeable patterns** for experimentation, often with warnings.

Your job is:

- To read contracts and identify the patterns.
- To tweak them to suit Flow-specific use cases.
- To document the assumptions and trade-offs clearly.

In public-good contexts, this is especially important when:

- You are building trustless systems for communities.
- Gas cost and upgradeability decisions directly affect users.
- You must balance **security** and **accessibility**.

## Implementation Sketch

```solidity
contract Counter {
 uint256 public count;
 function increment() external { count += 1; }
}
```

## Practical Exercises

### Exercise 1: Identify Patterns in a Contract

Take a small contract from a Flow lab (or an example in docs):

- Write a short note identifying:
 - Whether it looks like a token-like pattern.
 - Whether it uses modular or library-style code.
 - Whether it might be upgradeable or state-machine-style.

- For each pattern, write one sentence describing what it is responsible for.

### Exercise 2: Sketch a Simple Token Pattern

Without writing real Solidity/Vyper, sketch a **conceptual token pattern**:

- A mapping from addresses to balances.
- Functions like `transfer` and `approve`.
- Events like `Transfer` and `Approval`.

Diagram this as a **mental model**, not code.
Then, list one potential security issue (e.g., overflow, approval misuse).

### Exercise 3: Relate to a Flow Use Case

Imagine a Flow system that:

- Issues tokens to trainees.
- Lets them transfer tokens to each other.
- Logs all transfers for transparency.

Design a small "contract blueprint" in markdown:

- What state do you store?
- What functions do you expose?
- What pattern names (e.g., ERC-20, state machine, proxy) could apply?

This is a **high-level design exercise** for the kind of contract you will write later.

## Self-Assessment

Rate yourself from 1 to 5:

- I can recognize common contract patterns (tokens, modular, upgradeable, state machine).
- I can explain what each pattern is trying to solve.
- I can point to one security or limitation trade-off per pattern.
- I can connect patterns to real-world Flow-style use cases.

Action item: write a short note in your lab repo describing which pattern you would use for a "trainee-reward token" and why.

## Further Reading

- [Solidity docs](https://docs.soliditylang.org/)
- [Vyper docs](https://docs.vyperlang.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)
- [Hardhat docs](https://hardhat.org/docs)

## Next Steps

- Read the next lesson in the smart-contracts track, such as `03-security-anti-patterns.md`, to see how common patterns can be misused.
- Use this pattern vocabulary when you read or discuss other contracts.
- Treat design patterns as **shared mental tools** that let you reason about on-chain systems efficiently.

---

*This lesson gives Flow Initiative trainees an engineer-style understanding of common smart-contract design patterns, focusing on tokens, modularity, upgradeability, and state-machine structures, and how they shape security and composability on the blockchain.*
