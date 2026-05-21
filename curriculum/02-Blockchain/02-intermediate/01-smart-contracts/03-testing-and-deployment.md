---
id: testing-and-deployment
title: Testing and Deployment
track: blockchain
level: intermediate
version: 1.1
---

# Testing and Deployment

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/H-yL6nloq3I"
 title="Hardhat Testing Tutorial"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Identify the main steps in the contract lifecycle: write, test, deploy, monitor.
- Use basic testing strategies (unit tests, integration tests, state checks).
- Understand the difference between local testnets, testnets, and mainnets.
- Apply a "deploy-only-when-tested" discipline in Flow-style labs.

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

Writing a contract is only half the story.
You must also **test it thoroughly** and **deploy it safely** to the chain you care about.
In the Flow Initiative, you will run contracts on:

- Local development environments,
- Testnets, and
- Simulated mainnets (or local chains standing in for them).

This lesson is not about learning every testing framework in depth.
It is about **engineering discipline**: how to treat testing and deployment as part of the design process, not an afterthought.

## Why Testing Matters in Smart Contracts

Smart contracts differ from regular code in two ways:

- Once deployed, they are hard to change.
- Bugs can lead to **irreversible loss of value**.

Testing is the **last line of defense** before deployment:

- You cannot rely solely on code review or "hope it works."
- You must check behavior under different conditions, inputs, and edge cases.

For Flow trainees, this is especially important because:

- Labs and examples can later evolve into production-like systems.
- Public-good infrastructure often has **high stakes** and **low forgiveness** for mistakes.

Your job is to **build a testing mindset** into how you design and write contracts.

## Key Testing Strategies

### 1. Unit Tests

**Unit tests** verify small pieces of logic in isolation:

- Does a `transfer` function correctly update balances?
- Do access-control guards reject unauthorized callers?
- Do state transitions match the expected pattern?

Unit tests are fast and deterministic.
In Flow-style labs, you may use frameworks like:

- Hardhat or Foundry for Solidity,
- or Vyper-specific tooling.

The goal is **coverage of core flows**, not every line.

### 2. Integration Tests

**Integration tests** check how multiple contracts work together:

- Does a token contract correctly interact with a governance or reward contract?
- Do upgradeable patterns behave correctly under simulated upgrades?
- Do L2 bridge patterns handle disputes or timeouts?

Integration tests are slower and more complex, but they reveal **system-level bugs**.

### 3. State and Event Checks

In addition to function-level checks, you should:

- Inspect the **on-chain state** after key operations.
- Check that **events** fire with the expected data.

This is how you verify that the contract's *observable behavior* matches your expectations.

### 4. Fuzzing and Invariant Checks

More advanced teams add:

- **Fuzzing** - automatically generating random inputs to find edge cases.
- **Invariant checks** - ensuring certain conditions always hold (e.g., total supply never decreases incorrectly).

For beginner-intermediate Flow labs, focus on **unit and integration tests**.
Fuzzing and invariants are a "next-level" practice.

## Deployment Environments

Contracts are typically deployed in stages:

### 1. Local Development Environment

- Runs on your machine.
- No real economic value at stake.
- Used for fast iteration and debugging.

Flow labs often start here: you write, test, and debug contracts without worrying about gas or permanence.

### 2. Testnet

- A public network with "fake" but valuable-looking funds.
- Used to test how contracts behave under real-world conditions.
- Catches issues like gas limits, network latency, and integration with real wallets.

Testnets are optional but recommended for anything that will interact with real users later.

### 3. Mainnet (or Equivalent)

- The production network where real value is at stake.
- For Flow exercises, this may be a **simulated L1** or **local mainnet-equivalent**.

Deployment here is **irreversible**.
You must only deploy after thorough testing.

## Deployment Discipline

To avoid mistakes, adopt a deployment checklist:

1. **Code Review**
 - Have another engineer (or the community) review the contract.
 - Check for known anti-patterns (e.g., reentrancy, overflow).

2. **Testing**
 - Run all tests and ensure they pass.
 - Check gas usage and performance under load.

3. **Environment**
 - Decide if this is local, testnet, or mainnet-style.
 - Confirm the correct network and wallet.

4. **Post-Deployment Checks**
 - Verify that the contract is correctly deployed.
 - Check events and state for a few transactions.

This discipline is crucial for Flow-style systems that may later handle real-world value.

## How This Fits Into the Flow Initiative

In Flow labs:

- You will write contracts in Solidity or Vyper.
- You will run tests in your local environment.
- You may deploy to a testnet or simulated chain for experimentation.

Your goal is to:

- Treat **testing as part of the design** process.
- Use **clear, repeatable deployments**.
- Learn from mistakes in a safe environment.

In public-good contexts, this is especially important when:

- You are building trustless systems for communities.
- Gas cost and deployment safety directly affect users.
- You must balance **security** and **accessibility**.

## Implementation Sketch

```solidity
contract Counter {
 uint256 public count;
 function increment() external { count += 1; }
}
```

## Practical Exercises

### Exercise 1: Write a Simple Test Plan

Take a small contract from a Flow lab:

- Write a short test plan identifying:
 - What functions need unit tests.
 - What scenarios need integration tests.
 - What state and events to check.

This is a **high-level test plan**, not code.

### Exercise 2: Sketch a Deployment Flow

Sketch a deployment flow for a Flow-style contract:

- From local development to testnet to mainnet (or simulated mainnet).
- Including code review, testing, and post-deployment checks.

This is a **mental model** of the deployment lifecycle.

### Exercise 3: Relate to a Flow Lab

Look at a blockchain lab that mentions deployment:

- Write one sentence describing the deployment environment.
- Write one sentence describing the test plan.
- Write one sentence describing what you would improve.

This helps you see deployment as a **systematic process**.

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain the difference between unit and integration tests.
- I can identify the main steps in the deployment lifecycle.
- I can see why testing is crucial for smart contracts.
- I can connect these practices to Flow-style labs.

Action item: write a short note in your lab repo describing a deployment checklist for a Flow-style contract.

## Further Reading

- [Solidity docs](https://docs.soliditylang.org/)
- [Vyper docs](https://docs.vyperlang.org/)
- [OpenZeppelin Contracts](https://docs.openzeppelin.com/contracts/)
- [Hardhat docs](https://hardhat.org/docs)

## Next Steps

- Read the next lesson in the smart-contracts track, such as `04-security-anti-patterns.md`, to see how to avoid common deployment mistakes.
- Use this testing and deployment mindset whenever you write or deploy contracts.
- Treat deployment as a **disciplined engineering process**, not a one-time event.

---

*This lesson gives Flow Initiative trainees an engineer-style understanding of smart-contract testing and deployment, focusing on unit tests, integration tests, and deployment environments, and how they fit into the contract lifecycle on the blockchain.*
