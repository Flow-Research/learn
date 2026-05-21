---
id: rollups-and-sharding
title: Rollups and Sharding
track: blockchain
level: advanced
version: 1.1
---

# Rollups and Sharding

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/BgCgauWVTs0"
 title="Ethereum Layer 2 Scaling Explained"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain how **rollups** and **sharding** scale blockchain throughput without sacrificing security.
- Distinguish between **validity-proof rollups**, **fraud-proof rollups**, and **sharded L1s**.
- Map rollup and sharding patterns to trade-offs in latency, security, and decentralization.
- Use these patterns strategically in Flow-style L1/L2 designs.

## Concept Map

```mermaid
flowchart TD
  A["User transactions"] --> B["Sequencer"]
  B --> C["Batch"]
  C --> D["Proof or fraud window"]
  D --> E["Layer 1 settlement"]
  A --> F["Shard or data partition"]
```

## Quantitative Lens

Rollup economics are driven by amortization:

$$
Fee_{user} = \frac{Fee_{L1Data} + Fee_{proof}}{BatchSize}
$$

Sharding attacks the same pressure from another angle: it partitions data or execution so every node does not do every job.

## Introduction

Blockchain L1s are limited by how fast all nodes can process every transaction.
**Rollups** and **sharding** are two major families of solutions that:

- Push **most computation or data off-chain or to a subset of nodes**,
- While **still anchoring trust to the L1** or a single security layer.

From an engineer's view:

- A **rollup** is a **layer-2 system** that batches many transactions and submits proofs or data to the L1.
- **Sharding** is a way for the L1 itself to split work across **parallel "shards"** that coordinate via a shared validator set.

Neither is magic; both are **system design choices** that trade off ease-of-use for complexity and trust assumptions.

This lesson focuses on **concepts and mental models**, not low-level protocol specs.

---

## What Are Rollups?

A **rollup** is an L2 system that:

- Processes many transactions **off-chain**.
- Periodically submits a **compressed representation** (e.g., state root, proof, or data) to the L1.
- Lets the L1 (or an on-chain contract) **verify or adjudicate** disputes if needed.

At a high level, a rollup looks like:

- **On-chain**:
 - A contract that accepts state roots or proofs.
 - A mechanism for users to deposit and withdraw.

- **Off-chain**:
 - A sequencer or set of nodes that execute transactions.
 - A layer that produces proofs or data that can be checked on-chain.

Users benefit from:

- High throughput and low fees on the L2.
- The security of the L1 anchoring the final state.

---

## Types of Rollups

### 1. Validity-Proof Rollups ("ZK-Rollups")

- The L2 computes a **cryptographic proof** (often zero-knowledge) that some state change is valid.
- The L1 contract **verifies the proof** and accepts the state if it passes.

Properties:

- Strong **safety**: invalid state cannot be accepted.
- Fast **finality** once the proof is submitted.
- Complex **cryptography**, both to design and run.

Good fit for:

- High-security, high-value applications.
- Systems where trustless verification is preferred.

### 2. Fraud-Proof Rollups ("Optimistic Rollups")

- The L2 assumes the sequencer is honest by default.
- Off-chain challengers can submit **fraud proofs** to the L1 if they detect invalid state.

Properties:

- Simple **computation** on the L2; heavy work only on disputes.
- Cheaper to operate in normal conditions.
- Requires a **challenge window** during which anyone can dispute.

Good fit for:

- General-purpose applications.
- Systems where disputes are rare but must be handled.

---

## How Rollups Fit Into the Ecosystem

Rollups sit **on top of an L1**:

- The L1 provides **security and data availability**.
- The L2 provides **scalability and UX**.

You can mentally place rollups like this:

- **On-chain L1** -> **Rollups** -> **State channels**.

Each layer is optimized for different workloads:

- **On-chain**: settlement, governance, rare high-value interactions.
- **Rollups**: frequent, high-volume transactions and computations.
- **State channels**: very frequent, low-value, small-group interactions.

For Flow-style engineers, this is a **tiered scaling model**: you choose where to put each flow based on value, frequency, and trust requirements.

---

## What Is Sharding?

**Sharding** is a way for the L1 itself to:

- Split the state and computation into **parallel shards**.
- Have each shard processed by a **subset of validators**,
- With a **shared layer** that coordinates across shards.

Conceptually:

- A **shard** is a mini-chain with its own state and transactions.
- Validators hop between shards or rotate, so that **no one shard is permanently controlled**.
- Shard size and validator count are tuned to keep the system decentralizable.

Sharding trades **simplicity** for **throughput**:

- Each shard can process transactions in parallel.
- But cross-shard communication is more complex.

---

## Rollups vs. Sharding

| Aspect | Rollups | Sharding |
|-----------------------|----------------------------------------------------------|----------------------------------------------------------------|
| **Where it lives** | Layer-2 (on top of L1) | Built into the L1 itself |
| **Trust model** | Anchored to L1 security | Security shared across shards |
| **Complexity** | Adds off-chain sequencers and proofs | Adds cross-shard coordination and validator rotation |
| **Throughput** | Can be very high for many use cases | High, but limited by shard count and communication overhead |
| **Flexibility** | Easy to add new rollups for specific apps | Changing the sharding structure is a major protocol upgrade |

Neither is universally "better."
You choose:

- **Rollups** when you want **flexible, app-specific scaling** on top of an existing L1.
- **Sharding** when you want **deep integration** and **massive parallelization** at the L1 level.

---

## Why This Matters for Flow Engineers

Flow-style engineers will:

- Encounter rollups and sharded L1s in many ecosystems.
- Design or critique systems that must balance **speed, security, and cost**.
- Need to decide **where to put each layer** (on-chain, rollup, channel).

Understanding rollups and sharding helps you:

- **Architect** systems that push low-value, high-frequency flows to L2s while keeping security on-chain.
- **Communicate** trade-offs to stakeholders (e.g., "this is a ZK-rollup because we want trustless verification").
- **Evaluate** when a new protocol or tool is appropriate for a given context.

In public-good contexts, this is especially important when:

- Designing **public-good protocols** that must be transparent and understandable.
- Balancing **accessibility** (low fees, high throughput) with **security**.
- Ensuring that **economic incentives** align with long-term community interests.

---

## Implementation Sketch

```json
{
  "batchNumber": 1024,
  "txCount": 2500,
  "stateRootBefore": "0x...",
  "stateRootAfter": "0x...",
  "dataAvailability": "posted"
}
```

## Practical Exercises

### Exercise 1: Sketch a Rollup Architecture

Take a simple Flow-style app:

- Draw a diagram showing:
 - The L1.
 - A rollup.
 - A few users.
- Mark where transactions are processed, where proofs are submitted, and where disputes are handled.

Write a short note describing the flow.

### Exercise 2: Analyze a Sharded L1

Find a real-world sharded L1 (e.g., a popular chain or research project):

- Identify how many shards it has.
- Describe how validators rotate or coordinate across shards.
- Write a short note explaining the **trade-offs** of this design.

### Exercise 3: Relate to a Flow Lab

Look at a Flow-style lab that involves frequent transactions:

- Design a small **rollup-style** model for it:
 - Who are the sequencers?
 - What is the proof or data submitted to the L1?
 - How are disputes handled?

This is a **high-level design exercise** for the kind of flow you might implement later.

---

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what a rollup is.
- I can distinguish between validity-proof and fraud-proof rollups.
- I can explain what sharding is.
- I can see how these patterns fit into a Flow-style system.

Action item: write a short note in your lab repo describing one Flow-style system where rollups or sharding would improve scalability.

## Further Reading

- [Cosmos IBC](https://ibc.cosmos.network/)
- [Chainlink CCIP](https://docs.chain.link/ccip)
- [Ethereum bridges](https://ethereum.org/en/developers/docs/bridges/)
- [W3C DID Core](https://www.w3.org/TR/did-core/)

## Next Steps

- Read the next lesson in the advanced track (e.g., `03-state-channels-and-LN-style-systems.md`) to see how this pattern generalizes to more complex networks.
- Use this rollup and sharding mindset when you design or critique scalability solutions.
- Treat rollups and sharding as **layered, scalable complements** to on-chain and L1-style systems.

---

*This lesson gives Flow Initiative trainees an engineer-style understanding of rollups and sharding in blockchain systems, focusing on how to recognize, design, and use them as scalable, secure alternatives to on-chain transactions.*
