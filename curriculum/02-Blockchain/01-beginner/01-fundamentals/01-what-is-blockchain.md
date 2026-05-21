---
id: what-is-blockchain
title: What Is Blockchain?
track: blockchain
level: beginner
version: 1.1
---

# What Is Blockchain?

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/hEsdzcQEzvk"
 title="ETH002 - Ethereum Basics - What are blockchains?"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Define a blockchain as a technical system, not just a buzzword.
- Identify the core components of a blockchain (blocks, state, consensus, network).
- Explain the problems blockchain solves relative to traditional databases.
- Connect blockchain concepts to real-world systems practiced in the Flow Initiative.

## Concept Map

```mermaid
flowchart LR
  A["Transaction"] --> B["Block body"]
  B --> C["Block hash"]
  C --> D["Next block"]
  D --> E["Shared history"]
```

## Quantitative Lens

A block commits to the previous block and its own transaction data:

$$
H_i = hash(H_{i-1} || txRoot_i || metadata_i)
$$

Changing old data changes the hash chain, which is why verification is cheap but rewriting history is hard.

## Introduction

Blockchain is often presented as magic money machine. In reality, it is a very specific **engineering pattern** for building shared, append-only ledgers across many machines and people.

For Flow Initiative trainees, the goal is not to "believe in crypto" but to understand blockchain as a **distributed systems primitive**. You will eventually apply this to:

- decentralized ledgers,
- incentive-driven infrastructure, and
- public-goods applications that redistribute control and value.

This lesson grounds "blockchain" in concrete components and assumptions, not marketing narratives.

## A Minimal Definition

A blockchain is a **public, distributed, append-only database** where:

- Data is grouped into **blocks**.
- Each block cryptographically refers to its **previous block**.
- A **consensus mechanism** decides which blocks are valid and accepted by the network.

Unlike a centralized database:

- There is no single owner.
- Anyone can verify the state by running their own node.
- Once data is accepted, it is hard to change without coordinated effort.

## Why "Blockchain" Exists

Blockchains solve several related problems:

- **Trust minimization** - you do not need to rely fully on a single party.
- **Censorship resistance** - it is hard for any one player to block or erase data.
- **State transparency** - everyone can see the same history of changes.
- **Programmable incentives** - you can design reward and penalty rules for participants.

From an engineer's perspective, what matters is:

- what guarantees the system actually offers,
- what assumptions it makes about the environment, and
- what trade-offs you accept by choosing it.

## Core Components

### 1. Blocks

A **block** is a data structure that usually contains:

- A list of transactions or state updates.
- A reference (hash) to the previous block.
- Metadata such as timestamp, fees, and validator info.

When blocks are chained together, you get a **history** of the ledger's state.

### 2. State

The **state** is the current representation of all balances, contracts, and rules defined on the chain.

Different blockchains organize state differently:

- Account-based (e.g., Ethereum),
- UTXO-based (e.g., Bitcoin).

Regardless of model, the state evolves deterministically from block to block.

### 3. Consensus

**Consensus** is the process by which nodes agree on which blocks are valid. Without consensus, every node would maintain its own incompatible view of the state.

Common consensus families:

- **Proof-of-Work (PoW)** - nodes prove computational work to propose blocks.
- **Proof-of-Stake (PoS)** - nodes "stake" value as collateral to participate in validation.

Different consensus mechanisms make different assumptions about:

- cost of attack,
- liveness vs. safety, and
- performance under network partitions.

### 4. Network

A blockchain is a **peer-to-peer network** of nodes:

- Some nodes **propose** blocks.
- Some nodes **validate** and **relay** them.
- Some nodes **execute** transactions and store state.

The network layer is responsible for:

- message propagation,
- fork handling, and
- re-synchronization after failures.

### 5. Cryptography

Blockchains rely on standard cryptographic tools:

- **Cryptographic hashes** - to link blocks and detect tampering.
- **Public-key cryptography** - to authenticate participants and sign messages.
- **Digital signatures** - to prove origin and integrity of data.

These tools are not invented for blockchain; they are **composed** into a new pattern for trust-minimized coordination.

## How Blockchain Differs from a Regular Database

### Traditional Database

- Usually owned by one organization.
- State is updated by a small, trusted set of administrators.
- Replication is controlled by a single entity.
- Failure modes are relatively simple: disk, network, operator.

### Blockchain

- Ideally, **no central owner**.
- State is updated by many participants under shared rules.
- Replication is **decentralized and competitive**.
- Failure modes involve **Byzantine behavior, incentives, and forks**.

From an engineer's viewpoint, this means:

- your code must reason about **partial knowledge** and **competing histories**.
- your system must be **resilient to misaligned or malicious actors**.

## Practical Examples Trainees Will Encounter

As you move deeper into the Flow Initiative blockchain track, you will see variants of:

- **L1 blockchains** - base-layer ledgers with consensus and state, such as Ethereum-style chains.
- **L2 networks** - systems that scale and bundle transactions without sacrificing the security of the base layer.
- **Smart contracts** - code stored on the chain that defines rules and state transitions.

Even at the beginner level, it helps to see these patterns:

- A **payment system** where transactions must be ordered and irreversible.
- A **registry** where identity or credentials are stored transparently.
- A **token economy** where value accrues to participants based on agreed-on rules.

## Why This Matters for Flow Engineers

Flow trainees work on **public-good infrastructure**, where:

- single-points of failure are dangerous,
- trust in institutions can be low or contested, and
- cost-effective, open systems are often needed.

Blockchain is one pattern for:

- building **trust-minimized payments** and incentives,
- creating **shared, auditable data** across organizations, and
- enabling **public-goods infrastructure** whose rules are encoded and transparent rather than hidden in closed systems.

Your job is not to treat blockchain as a universal solution. It is to understand **when and why** it fits a problem.

## Key Takeaways

- A blockchain is a **distributed, append-only ledger** with cryptographic links across blocks.
- **Consensus** is the engine that makes this ledger coherent across many nodes.
- **State** is the outcome of all accepted blocks.
- The **network** and **cryptography** layers enforce the rules and detect attacks.

These are the pieces you will dissect in later lessons.

## Implementation Sketch

```python
import hashlib

def block_hash(previous_hash, tx_root, metadata):
    payload = f"{previous_hash}|{tx_root}|{metadata}".encode()
    return hashlib.sha256(payload).hexdigest()
```

## Practical Exercise

### Exercise 1: Sketch a Simple Blockchain

On paper or in a text editor, sketch a tiny blockchain with 3 blocks:

- Block 0 (genesis): contains an initial state.
- Block 1: contains 2 transactions.
- Block 2: contains 1 transaction and a nonce.

For each block, write:

- a hash (e.g., `0x...`),
- a reference to the previous block hash, and
- a short description of the state change.

This is a **minimal mental model** of how blocks fit together.

### Exercise 2: Relate to Real-World Systems

Think of one real-world system that reminds you of a blockchain (e.g., a shared ledger, a consensus-driven process, a tamper-resistant log). Write:

- What it does.
- How it is similar to a blockchain.
- How it is different.

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what a blockchain is in one sentence.
- I can list the main components (blocks, state, consensus, network).
- I can explain how it differs from a traditional database.
- I can see why this pattern might matter for public-goods infrastructure.

Action item: write a 3-sentence note in your Flow lab repo describing how a blockchain is like a "shared, append-only log" with rules.

## Further Reading

- [Ethereum developer docs](https://ethereum.org/en/developers/docs/)
- [Ethereum transactions](https://ethereum.org/en/developers/docs/transactions/)
- [Ethereum proof of stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/)
- [Ethereum layer 2](https://ethereum.org/en/layer-2/)

## Next Steps

- Read `02-key-terms-and-models.md` next to build precise language for blockchain work.
- Use this conceptual model when you later encounter Ethereum-style chains, L2s, or token-based systems in the Flow curriculum.
- Treat blockchain as a **distributed systems primitive**, not a miracle technology.

---

*This lesson equips Flow Initiative trainees with a grounded, engineering-style understanding of blockchain as a distributed, append-only ledger driven by consensus and cryptography, preparing them for deeper work in the beginner, intermediate, and advanced tracks.*
