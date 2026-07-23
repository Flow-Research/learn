---
id: key-terms-and-models
title: Key Terms and Models in Blockchain
track: blockchain
level: beginner
version: 1.1
Prerequisites: "01-what-is-blockchain"
Duration: "~30-45 minutes"
Format: "Glossary + classification exercises + reading"
Future_Topics: "Consensus Overview, Layer-1 vs Layer-2, Tokens and Economic Incentives, Decentralized Identity"
Related_docs:
  - 01-beginner/01-fundamentals/01-what-is-blockchain
  - 01-beginner/01-fundamentals/03-consensus-overview
  - 01-beginner/02-ecosystem/01-layer-1-vs-layer-2
---

# Key Terms and Models in Blockchain

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/J36YzMnsy5U"
 title="Blockchain Nodes Explained: Security and Consensus Made Simple"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Recognize and define core blockchain terms (node, block, transaction, address, gas, etc.).
- Distinguish between common blockchain models (public, private, consortium, L1, L2).
- Map these terms and models onto real-world examples from the Flow Research Initiative curriculum.
- Use this vocabulary to read Ethereum-style documents and protocol docs with confidence.

## Concept Map

```mermaid
flowchart LR
 A["Users"] --> B["Transactions"]
 B --> C["Validation"]
 C --> D["Consensus"]
 D --> E["Shared state"]
```

## Quantitative Lens

Blockchain engineering is state-transition engineering:

$$
state_{t+1} = apply(state_t, tx)
$$

The useful question is always: who is allowed to change state, under which rules, and how can others verify it?

## Introduction

Blockchain systems are full of jargon. Some terms are marketing noise; others are actual technical primitives.
In this lesson you will learn the **essential, engineering-grade vocabulary** of blockchain and a few **simple models** that help you reason about how different systems work.

For Flow Research Initiative trainees, this is not a "dictionary" drill. It is a **concept map** that connects terminology to:

- decentralized ledgers,
- smart contracts, and
- incentive-driven infrastructure.

Once you internalize these terms, later lessons on Ethereum-style chains, L2s, and token economics will feel much more concrete.

## Core Blockchain Terms

### 1. Node

A **node** is a participant in the blockchain network that runs the protocol software.

Nodes can:

- Store the blockchain's state and history.
- Relay messages to other nodes.
- Validate transactions and blocks.
- (Optionally) propose or attest blocks, depending on the consensus model.

From an engineer's view, a node is just **a process that follows agreed-on rules** and talks to its peers.

### 2. Transaction

A **transaction** is a cryptographically signed message that requests a change to the system state.

In a payment-style chain, this often means:

- Transfer value from one address to another.
- Pay a fee for processing.

In smart-contract chains, a transaction can also:

- Call a function in a contract,
- Update storage,
- Emit events.

A transaction is **deterministic**: given the same context, it always produces the same outcome.

### 3. Block

A **block** is a data structure that bundles multiple transactions (or state updates) and includes:

- A reference to the previous block (its hash).
- A timestamp or block number.
- A consensus-related field (e.g., nonce, proposer signature, attester list).

Chaining blocks together creates the **ledger history**.

### 4. Block Hash

The **block hash** is a cryptographic digest of the block's contents. It uniquely identifies the block and links it to the chain.

If even a single bit in the block changes, the hash changes, making tampering easy to detect.

### 5. Address

An **address** is a public identifier derived from a public key, often used to represent accounts or contracts.

There are typically two broad styles:

- **Externally Owned Accounts (EOAs)** - controlled by a private key, used for users.
- **Contract Accounts** - smart contracts that live on the chain and respond to transactions.

An address is **not a person**; it is a cryptographic identity.

### 6. Wallet

A **wallet** is a tool that:

- Manages your private keys.
- Signs transactions on your behalf.
- Interacts with the node or RPC provider.

Think of a wallet as your **user interface to the chain**, not the chain itself.

### 7. Gas / Fee

In many blockchains, users must pay a **fee** (often called **gas**) to execute transactions.

Gas serves two main purposes:

- It compensates validators/miners for work.
- It constrains computation so that spam or infinite loops are too expensive.

As a developer, you care about:

- how much gas a transaction consumes,
- and how gas price affects user experience.

### 8. State

The **state** is the current snapshot of the ledger: account balances, contract storage, and rules encoded in smart contracts.

Nodes keep a copy of the state and update it block by block.
In many designs, state changes are **deterministic**: the same inputs and blocks always lead to the same state.

### 9. Consensus Mechanism

A **consensus mechanism** is the protocol that ensures nodes agree on:

- which blocks are valid,
- in what order they are accepted.

Common families:

- **Proof-of-Work (PoW)** - nodes solve computational puzzles to propose blocks.
- **Proof-of-Stake (PoS)** - nodes stake value as collateral to participate.
- **Variants** like delegated PoS, Byzantine Fault-tolerant (BFT) systems, etc.

Each consensus model makes different trade-offs in security, decentralization, and performance.

### 10. Fork

A **fork** happens when the network has two or more competing chains of blocks.

Forks can be:

- **Temporary** - a "chain split" resolved automatically by the protocol.
- **Permanent** - a deliberate protocol change that splits the community (e.g., a contentious upgrade).

Engineers must understand how their application behaves under different fork conditions.

## Common Blockchain Models

### 1. Public Blockchain

A **public** blockchain is open to anyone:

- Anyone can download the software.
- Anyone can run a node.
- Anyone can send transactions.
- Anyone can validate or propose blocks (depending on consensus).

Examples: Bitcoin, Ethereum-style chains.
Public chains prioritize **censorship resistance** and **permission-lessness**.

### 2. Private (Permissioned) Blockchain

A **private** blockchain restricts participation:

- Only a small set of known organizations or nodes can join.
- Access to read or write state is controlled.

These are often used internally by enterprises for:

- auditing,
- tracking,
- or internal coordination.

They trade openness for control and privacy.

### 3. Consortium / Consortium-Style Networks

A **consortium** model sits between public and private:

- A defined group of entities jointly operates the chain.
- Governance is shared among participants.

This is common in:

- supply-chain tracking,
- regulated financial ecosystems,
- or multi-stakeholder data sharing.

### 4. Layer-1 (L1) vs Layer-2 (L2)

**Layer-1** (L1) is the **base chain** that provides:

- consensus,
- state, and
- the primary security layer.

**Layer-2** (L2) is a system that builds on top of an L1 to:

- improve throughput,
- reduce fees, or
- add features.

Typical L2 patterns:

- Rollups that **batch and submit proofs** to the L1.
- Sidechains that operate under their own consensus but link back to the L1 for security or data availability.

Think of L1 as the "ground truth" and L2 as the "high-capacity runway" above it.

## Why Models Matter for Engineers

Engineers do not just "use" a model; they design around its assumptions:

- On a **public L1**, you assume:

 - High latency and high cost for some operations.
 - Transparent, auditable state.
 - Long-term immutability.

- On a **private or consortium** network, you assume:

 - Known participants.
 - Faster finality.
 - Stronger control over upgrades and access.

Knowing the model helps you:

- set realistic expectations for performance and security.
- choose the right place to compute (on-chain vs off-chain).
- design smart contracts that respect the network's constraints.

## Relating Terms to the Flow Research Initiative

In the Flow Research curriculum, you will soon see these terms and models in:

- **`blockchain` track labs** - where you call contracts, read state, and send transactions.
- **`protocol-eng` track** - where you reason about consensus, nodes, and network behavior.
- **`AI-ML` / `blockchain` intersections** - where you use L1s or L2s as coordination layers for federated learning or incentive-driven data markets.

For example:

- A **node** in a lab might be your local `geth` or `anvil` instance.
- A **transaction** might be a small JS/Python script that interacts with a deployed contract.
- A **gas fee** might be a number you watch while testing in a local environment.

Seeing these terms in practice helps you move from "vocabulary" to "mental model."

## Implementation Sketch

```json
{
 "stateBefore": "0x...",
 "transaction": "0x...",
 "stateAfter": "0x...",
 "proof": "verified"
}
```

## Practical Exercises

### Exercise 1: Create a Glossary Map

Make a small table or list that maps:

- Term (e.g., `node`, `transaction`, `block`)
to
- Your one-sentence engineering definition.

Do this in `labs/` or in a markdown note so you can reuse it later.

### Exercise 2: Classify a Chain

Pick one blockchain you know (e.g., Bitcoin, Ethereum, Solana, or a local chain you've used) and classify it:

- Is it **public**, **private**, or **consortium**?
- Is it an **L1** or **L2**?
- What is its main **consensus model**?

Write a short note explaining your classification.

### Exercise 3: Trace a Simple Flow

Imagine the simplest possible flow:

1. A user signs a transaction in a wallet.
2. The transaction is sent to a node.
3. The node relays it to the network.
4. A validator includes it in a block.
5. The block is added to the chain.

For each step, name the key term(s) involved (e.g., `wallet`, `node`, `transaction`, `validator`, `block`) and write a one-sentence explanation.

## Self-Assessment

Rate yourself from 1 to 5:

- I can define core blockchain terms in my own words.
- I can distinguish between public, private, and consortium models.
- I can differentiate L1 and L2 roles.
- I can connect these terms to simple labs or examples.

Action item: update your Flow Research lab notes with a short glossary section using these terms.

## Further Reading

- [Ethereum developer docs](https://ethereum.org/en/developers/docs/)
- [Ethereum transactions](https://ethereum.org/en/developers/docs/transactions/)
- [Ethereum proof of stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/)
- [Ethereum layer 2](https://ethereum.org/en/layer-2/)

## Next Steps

- Read `03-consensus-overview.md` next to see how consensus models turn these terms into operational behavior.
- Use this lesson as a reference whenever you encounter a new protocol doc or SDK.
- Treat terminology as part of your mental toolkit for reading, not just for writing.

---

*This lesson gives Flow Research Initiative trainees a clear, engineer-friendly set of definitions and models for blockchain, laying the groundwork for more advanced work in the beginner, intermediate, and advanced tracks.*
