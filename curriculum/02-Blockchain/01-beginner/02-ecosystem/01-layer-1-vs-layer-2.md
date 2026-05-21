---
id: layer-1-vs-layer-2
title: Layer-1 vs Layer-2
track: blockchain
level: beginner
version: 1.1
---

# Layer-1 vs Layer-2

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

- Explain the roles of L1 and L2 in a blockchain ecosystem.
- Identify the trade-offs each layer brings (security, latency, cost, flexibility).
- Map L1/L2 concepts onto real-world chains and Flow labs.
- Decide, at a high level, where to place different kinds of logic (on-chain vs off-chain).

## Concept Map

```mermaid
flowchart TD
  A["Users"] --> B["Layer 2 execution"]
  B --> C["Batch or proof"]
  C --> D["Layer 1 settlement"]
  D --> E["Base-layer security"]
```

## Quantitative Lens

Layer 2 cost usually improves through batching:

$$
CostPerTx = \frac{CostToSettleBatch}{TransactionsInBatch}
$$

The design question is what security, latency, and withdrawal assumptions come with that lower cost.

## Introduction

Most blockchains today are not single monolithic systems. They are layered.
The two most common layers are:

- **Layer-1 (L1)** - the foundational chain that provides consensus and state.
- **Layer-2 (L2)** - a secondary system that builds on top of an L1 to improve speed, cost, or features.

In the Flow Initiative, you will encounter L1s and L2s in labs, tutorials, and protocol discussions.
This lesson treats L1/L2 as **system design patterns**, not buzzwords, so you can reason about them like an engineer.

## Why Layering Exists

Single-layer blockchains face a "triangle" of constraints:

- **Decentralization** - many nodes can participate.
- **Security** - the system is hard to subvert.
- **Scalability** - the system can handle many transactions.

Improving one often affects the others.
Layering is a way to:

- keep the **L1 lean and secure**, and
- push **high-throughput or application-specific logic** to **L2s**.

This is similar to classical system design: a strong core kernel with richer services on top.

## What a Layer-1 (L1) Is

A **Layer-1** is the base blockchain that:

- Defines the core consensus mechanism.
- Maintains the primary state (e.g., account balances, basic contracts).
- Provides the main security properties (immutability, finality, censorship resistance).

From an engineer's view, an L1 is:

- The **source of truth** for what happened.
- The **final arbiter** of state disputes.
- The **costly but trusted layer** you lean on when L2s disagree.

Typical L1 roles:

- Settlement: final recording of value transfers.
- Dispute resolution: validating or rejecting L2 proofs.
- Governance: upgrades and coordination of the whole stack.

Examples in practice:

- Ethereum-style chains, Bitcoin-style chains, many PoS-based L1s.

## What a Layer-2 (L2) Is

A **Layer-2** is a system that:

- Operates above an L1.
- Processes transactions or state changes faster and cheaper.
- Eventually anchors its results back to the L1 (often via proofs or data availability).

L2s do not redefine the core security model; they **rely on it**.

Common L2 patterns:

- **Rollups** - bundle many transactions off-chain and submit compressed proofs or data to the L1.
- **Sidechains** - run their own consensus but periodically sync or challenge with the L1.
- **State channels / payment channels** - keep most state off-chain and only settle on the L1 when needed.

From an engineer's view, an L2 is:

- The **high-capacity runway** for user-facing flows.
- The place where you **experiment with UX and performance**.
- The subsystem that must still respect the L1's **finality and security model**.

## How L1 and L2 Interact

At a high level, the interaction looks like this:

1. **User action**
 - A user sends a transaction to an L2 (e.g., a rollup node or a channel).

2. **Off-chain processing**
 - The L2 processes many such actions quickly and cheaply.
 - It keeps an internal state that tracks changes.

3. **Commitment to L1**
 - Periodically, the L2 submits a **compressed representation** (e.g., a Merkle root, a validity proof, or sequencer data) to the L1.

4. **L1 adjudication**
 - The L1 stores that commitment.
 - If there is a dispute, the L1 uses predefined rules to resolve it.

This pattern lets you:

- get fast UX from the L2,
- while still resting on the security and decentralization of the L1.

## Key Trade-Offs

### L1 Strengths

- Strong security and decentralization.
- Long-term immutability.
- Clear, consensus-enforced rules.

### L1 Limitations

- Limited throughput (many designs are "slow by design").
- High transaction cost (especially in busy periods).
- Less flexibility for app-specific logic.

### L2 Strengths

- Higher throughput and lower cost for many use cases.
- Faster latency for users.
- More room for custom logic, UX tweaks, or experimental designs.

### L2 Limitations

- Extra complexity: more moving parts, more failure modes.
- Dependency on the L1's health and upgrades.
- Potential centralization risks (e.g., single sequencers, off-chain operators).

As an engineer, you choose:

- Put **core settlement and critical state on L1**.
- Put **high-volume, user-facing interactions on L2**.

## Why This Matters for Flow Engineers

Flow Initiative trainees will work across:

- L1 ecosystems (e.g., Ethereum-compatible chains),
- L2 solutions (rollups, sidechains, channels), and
- hybrid designs that mix on-chain and off-chain logic.

Understanding L1 vs L2 helps you:

- Design apps that do not overpay for on-chain execution.
- Reason about when data is "final" and when it is "pending."
- Build systems that gracefully handle L2 failures or upgrades.

In public-good contexts, this is especially relevant when:

- Users have limited bandwidth and patience.
- Compute and L1-tx costs are high.
- L2s can smooth out cost and UX while still anchoring trust to an L1.

## Practical Examples You Will See

### Example 1: Simple Rollup-Style Design

- L1: Ethereum-style chain that stores state roots and receives proofs.
- L2: Rollup that batches thousands of user transactions per second.
- Flow pattern:
 - Transactions are signed and sent to the L2.
 - The L2 submits state commitments to the L1 once in a while.
 - L1 ensures the L2 cannot cheat forever.

### Example 2: Sidechain for Data Availability

- L1: Provides finality and anchors hashes.
- L2/Sidechain: Handles fast, cheap writes for logs or sensor data.
- Flow pattern:
 - Local nodes ingest data and seal it into bundles.
 - Commitments are sent to the L1 at intervals.
 - Users query the L2 for fresh data, L1 for proof.

### Example 3: State Channels / Channels

- L1: Governs disputes and settlements.
- L2/Channels: Keep long-running sessions off-chain.
- Flow pattern:
 - Users open channels and transact locally.
 - Only disputes or closes touch the L1.

You will see simplified versions of these patterns in Flow labs and later protocol-engineering work.

## Implementation Sketch

```yaml
use_layer_2_when:
  - users need lower fees
  - transactions can be batched
  - settlement can wait for the base layer
keep_layer_1_when:
  - strongest neutrality matters
  - final settlement must be direct
```

## Practical Exercises

### Exercise 1: Classify a System

Pick a chain or ecosystem you know (e.g., Ethereum + an L2 rollup, or a sidechain-style system):

- Identify which component is the L1 and which is the L2.
- Write one sentence describing what the L1 is responsible for.
- Write one sentence describing what the L2 is responsible for.

### Exercise 2: Sketch a Mini-Architecture

Draw a simple diagram with:

- An L1 node,
- An L2 node, and
- One user.

Show:

- Where the user sends transactions.
- Where the L2 processes them.
- Where commitments go to the L1.

Label each arrow with a short phrase (e.g., "submit tx", "send proof").

This is a **concept map** for how the two layers coordinate.

### Exercise 3: Relate to a Flow Lab

Look at a blockchain lab from the Flow curriculum that uses a real or local chain, and:

- Guess whether it targets an L1 or an L2 (or both).
- Write one sentence describing why that layer is appropriate for the lab's goal.
- Write one sentence describing what you could move off-chain to speed it up.

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what L1 and L2 mean.
- I can identify where security and finality live.
- I can see why L2s exist for scalability and UX.
- I can think about how to split logic between L1 and L2.

Action item: write a short note in your lab repo describing one concrete example of L1-L2 split that you might build.

## Further Reading

- [Ethereum developer docs](https://ethereum.org/en/developers/docs/)
- [Ethereum transactions](https://ethereum.org/en/developers/docs/transactions/)
- [Ethereum proof of stake](https://ethereum.org/en/developers/docs/consensus-mechanisms/pos/)
- [Ethereum layer 2](https://ethereum.org/en/layer-2/)

## Next Steps

- Read `02-tokens-and-economic-incentives.md` next to see how money and incentives are layered on top of L1/L2 systems.
- Use this conceptual model whenever you encounter a new chain or SDK.
- Treat L1 and L2 as **complementary engineering layers**, not competing ideologies.

---

*This lesson gives Flow Initiative trainees a clear, engineering-style understanding of Layer-1 vs Layer-2 in blockchain ecosystems, emphasizing security, scalability, and how to reason about where to place logic in real-world systems.*
