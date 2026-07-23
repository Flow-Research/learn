---
id: state-machines
title: State Machines
track: protocol-engineering
level: beginner
version: 1.1
Prerequisites: "01-protocol-vs-application"
Duration: "~30-40 minutes"
Format: "Watch First video + reading + Mermaid state diagram + small TypeScript FSM coding exercise"
Future_Topics: "Communication Patterns, Specification Writing, Formal Notation, State Machine Implementation"
Related_docs:
  - 01-beginner/01-protocol-concepts/01-protocol-vs-application
  - 01-beginner/01-protocol-concepts/03-communication-patterns
  - 03-AI-ML/03-advanced/01-modern-architectures/02-graph-neural-networks
---

# State Machines

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/-ZP2Xm-mY4E"
 title="An introduction to finite state machines and the state pattern"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain what a **state machine** is and why it is useful for specifying protocols.
- Define the core components: **states, transitions, events, and actions**.
- Draw a simple **state diagram** for a small protocol-like system (e.g., on-ramp flow, request-response, governance vote).
- Connect state-machines to **smart-contract-like** and **distributed** systems in Flow Research-style contexts.

## Concept Map

```mermaid
stateDiagram-v2
 [*] --> Draft
 Draft --> UnderReview: submit
 UnderReview --> Approved: approve
 UnderReview --> Rejected: reject
 Approved --> Executed: execute
```

## Quantitative Lens

A deterministic state machine has one next state for a given state and event:

$$
S_{t+1} = transition(S_t, event_t)
$$

## Introduction

In **protocol engineering**, you often need to describe **how a system behaves over time** under different inputs.

A **state machine** is one of the cleanest ways to model this:

- It tracks a **current state** of the system and defines rules for **how that state changes** when events or messages arrive.

For Flow Research-style systems, this is especially useful for:

- governance-workflow protocols,
- on-boarding flows,
- or any stateful interaction between actors.

This lesson gives you a **working, intuitive** understanding of state machines so you can start using them to pin down protocol rules.

---

## What Is a State Machine?

A **finite state machine (FSM)** is a model of a system that:

- lives in one of a **finite number of states** at any time.
- reacts to **events or inputs** by:

 - changing its state, and
 - optionally running some **actions** (e.g., logging, sending a message, updating a field).

Informally, you can think of a state machine like a **state-based script**:

- There is a **current state** (e.g., `WAITING`, `PENDING`, `APPROVED`).
- An **input arrives** (e.g., a user submits a form, an approval arrives).
- The machine decides: "from this state, given this input, move to a new state and do X."

### Key Terms

- **State**: a condition the system is in (e.g., `IDLE`, `PENDING_APPROVAL`, `APPROVED`).
- **Transition**: a move from one state to another triggered by an event.
- **Event/Trigger**: an input that causes a transition (e.g., `submit_request`, `approve`, `reject`).
- **Action**: something that happens during or after a transition (e.g., send notification, emit log, update score).

These are the building blocks you will use when you design protocol rules.

---

## Why State Machines Matter for Protocols

Protocols are often defined as **state-transition rules**:

- "What state can the system be in?"
- "What inputs can arrive?"
- "How should the state change when each input arrives?"

Examples of systems that are naturally viewed as state machines:

- **Web protocols** (e.g., HTTP-style request-response flows, TLS handshake).
- **Smart contracts** and **blockchain-style ledgers**, where the chain state evolves via transactions.
- **IoT / device control systems**, where devices move between states like `OFF`, `STANDBY`, `RUNNING`, `FAULT`.

In Flow Research-style thinking:

- a **state machine** is a **formal sketch** of your protocol's behavior.
- once you specify it clearly, you can:

 - implement it in code,
 - document it for other engineers,
 - and even use it to reason about correctness and safety.

---

## Core Components in Detail

### 1. States

A **state** is a named condition of the system. For example, in a governance-proposal flow:

- `DRAFT`
- `UNDER_REVIEW`
- `APPROVED`
- `REJECTED`
- `EXECUTED`

At any point in time, a proposal should be in **exactly one of these states** (or a small set of them, if you allow composite states).

### 2. Transitions

A **transition** is a rule like:

- "If the system is in state `UNDER_REVIEW` and event `approve` arrives, move to state `APPROVED` and, optionally, run action `notify_admin`."

Transitions are usually:

- **triggered by events**,
- sometimes **guarded** by conditions (e.g., only if `user_role == 'admin'`).

This is how you encode **valid behavior** in a protocol.

### 3. Events and Inputs

**Events** or **inputs** are the "things that happen" that can change state:

- User submits a form.
- A node receives a message.
- An approval or rejection event is received.

In practice, you can think of events as:

- explicit messages,
- or method calls that the protocol accepts.

### 4. Actions

**Actions** are what the system does during a transition:

- updating a field in a database,
- emitting an event into a log or message bus,
- sending a webhook or email.

Actions keep the protocol not only **state-correct** but also **observable and useful**.

---

## Simple State Diagram Example

A **state diagram** is a picture of your state machine. It helps you and your team see the protocol at a glance.

### Example: Governance Proposal Flow

States:

- `DRAFT`
- `UNDER_REVIEW`
- `APPROVED`
- `REJECTED`
- `EXECUTED`

Key transitions (sketch):

- `DRAFT` -> `UNDER_REVIEW` on event `submit`.
- `UNDER_REVIEW` -> `APPROVED` on event `approve`.
- `UNDER_REVIEW` -> `REJECTED` on event `reject`.
- `APPROVED` -> `EXECUTED` on event `execute`.

In a diagram, this looks like a set of bubbles (states) with arrows (transitions) labeled by events.

Even if you don't draw it in code, sketching this kind of diagram is a powerful way to **pin down protocol rules**.

---

## State Machines in Code (Concepts)

You do not need a heavyweight framework to start. At the core, a state machine in code usually has:

- A **current state variable** (e.g., `state: str`).
- A **set of transition rules** (e.g., a table or a switch-style structure) that maps:

 - `(current_state, event)` -> `(next_state, action)`.

In many languages, this can be written as:

- a `match` or `switch` over the current state,
- with cases that check the event type and decide the next state and what to do.

More advanced patterns (e.g., state-pattern in OOP, or dedicated FSM libraries) build on this idea but keep the same conceptual structure.

---

## How This Fits Into Flow Research-Style Systems

### 1. Governance-Style Protocols

For governance-style flows:

- each **proposal** can be modeled as a state machine.
- protocol rules define:

 - who can trigger events,
 - what states are allowed, and
 - what transitions are valid.

This makes it easy to audit:

- "Is this proposal in a valid state?"
- "Was this transition allowed?"

### 2. Smart-Contract-Like Systems

Smart contracts are essentially **state machines on the blockchain**:

- the contract has internal state (e.g., balances, flags).
- transactions are inputs that trigger state transitions.
- the blockchain itself is a **global state machine** that evolves via transactions.

In Flow Research-style thinking, you can design your **on-chain logic** as a small state machine and then:

- verify it mentally or with tests,
- and keep it as simple as possible.

### 3. Distributed Systems

In distributed-style architectures (e.g., replicated state machines, IoT control), state machines are used to:

- define **consistent state transitions** across nodes,
- and to recover from failures by replaying inputs.

This is another way protocol-style thinking converges with distributed-system design.

---

## Implementation Sketch

```typescript
const transitions = {
 Draft: { submit: "UnderReview" },
 UnderReview: { approve: "Approved", reject: "Rejected" },
 Approved: { execute: "Executed" }
} as const;
```

## Practical Exercises

### Exercise 1: Draw a State Diagram

Pick a Flow Research-style workflow (e.g., learner on-ramp, governance-proposal, or reward-application):

- List all meaningful **states** the system can be in.
- List all meaningful **events** that can arrive (e.g., `submit`, `approve`, `reject`, `execute`).
- Sketch a simple state diagram (boxes + arrows) showing which transitions are allowed.

You can do this on paper or in a simple diagramming tool and add it to your lab repo.

### Exercise 2: Write a Simple FSM in Pseudocode

Using the same workflow:

- Implement a tiny state-machine class or function in pseudocode (or your preferred language, keeping it minimal):

 - store `current_state`.
 - define a `handle_event(event_name)` function that maps `(current_state, event_name)` to a next state and an optional action.

This trains you to move from diagrams to actual code that enforces protocol rules.

### Exercise 3: Spot Invalid Transitions

Take your state diagram and ask:

- Are there transitions that **should never happen** (e.g., from `EXECUTED` back to `UNDER_REVIEW`)?
- How would you write a test or assertion that prevents those transitions in code?

This is how you start **enforcing** protocol rules, not just describing them.

---

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what a state machine is and why it is useful.
- I can define states, transitions, events, and actions clearly.
- I can draw a simple state diagram for a Flow Research-style workflow.
- I can see how state machines relate to smart-contract-like and distributed systems.

Action item: write a short note in your lab repo describing one Flow Research-style workflow you modeled as a state machine and how that improved your understanding of the protocol rules.

---

## Further Reading

- [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 2119 keywords](https://www.rfc-editor.org/rfc/rfc2119)
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

## Next Steps

- Read `03-protocol-specification.md` next to learn how to write **text-plus-diagram** specifications for your protocols.
- Use state machines as your **default mental model** for any protocol that evolves over time.
- Keep them small and focused; a simple state machine is easier to verify, document, and maintain than a sprawling blob of logic.

---

*This lesson gives Flow Research Initiative trainees a beginner-level understanding of state machines, focusing on how to model protocols as combinations of states, transitions, events, and actions, and how that fits into governance-style, smart-contract-like, and distributed systems in Flow Research-style contexts.*
