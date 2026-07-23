---
id: communication-patterns
title: Communication Patterns
track: protocol-engineering
level: beginner
version: 1.1
Prerequisites: "01-protocol-vs-application, 02-state-machines"
Duration: "~30-40 minutes"
Format: "Watch First video + reading + Mermaid sequence diagram + pattern-selection exercise"
Future_Topics: "Specification Writing, Versioning Strategies, Interoperable Design, Message Queue Implementation, 02-interchain-protocols"
Related_docs:
  - 01-beginner/01-protocol-concepts/02-state-machines
  - 01-beginner/02-standards/01-specification-writing
  - 02-intermediate/02-governance-and-ecosystem/02-interchain-protocols
---

# Communication Patterns

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/O1PgqUqZKTA"
 title="Publish-Subscribe Architecture"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Recognize several common **communication patterns** in distributed systems and protocols.
- Identify when to use **request-response**, **publish-subscribe**, and **message-queue**-style patterns.
- Sketch how these patterns fit into Flow Research-style protocols (e.g., governance events, ML-driven alerts, or on-ramp flows).
- Decide, at a high level, which pattern is right for a given Flow Research-style interaction.

## Concept Map

```mermaid
sequenceDiagram
 participant P as Publisher
 participant B as Broker
 participant S as Subscriber
 P->>B: Publish event
 B->>S: Deliver event
 S-->>B: Ack
```

## Quantitative Lens

Queues grow when arrival rate exceeds processing rate:

$$
QueueGrowth = \lambda_{in} - \mu_{out}
$$

## Introduction

So far you have learned:

- the difference between **protocol** and **application**,
- and how to model behavior over time with **state machines**.

Now it is time to look at **how messages move** between components:

- who sends what,
- who receives what,
- and when.

These are **communication patterns**. They are not protocols by themselves, but they shape how protocols are structured.

In Flow Research-style systems, choosing the right pattern affects:

- responsiveness,
- coupling,
- and scalability.

---

## What Are Communication Patterns?

A **communication pattern** is a **reusable way** that components exchange messages in a system.

Patterns impose structure on questions like:

- Is the sender **blocked** while waiting for a reply?
- Does the sender know its **exact receiver(s)**?
- Is communication **synchronous** or **asynchronous**?

By picking a pattern up front, you avoid inventing a new ad-hoc scheme for every interaction.

---

## Key Communication Patterns

### 1. Request-Response

**Request-response** (also called **pull**) is the most familiar pattern:

- A **client** sends a **request** to a **server**.
- The **server** processes the request and sends back a **response**.
- The client usually **waits** until it receives the response.

Examples:

- HTTP requests and responses.
- API calls to a model-serving endpoint.
- queries to a governance-state or learner-profile service.

**When to use request-response:**

- When you need **immediate answers** and it is okay to block while waiting.
- When interactions are **point-to-point** (one sender talks to one known receiver).

In Flow Research-style systems, this is natural for:

- dashboards asking for updated state,
- or for on-ramp forms that must immediately validate.

### 2. Publish-Subscribe (Pub/Sub)

**Publish-subscribe** (pub/sub) is a pattern where:

- **Publishers** send messages to **channels** or **topics** without knowing who will receive them.
- **Subscribers** express interest in certain topics and receive messages that match.

No one component has to know all the others; they just know the **topic** semantics.

Key properties:

- **Decoupled**: publishers and subscribers do not need to know each other.
- **Asynchronous**: the sender does not wait for everyone to receive the message.
- **Many-to-many**: one event can reach many listeners.

Examples:

- Event-driven systems (e.g., "proposal-created", "vote-received", "reward-processed").
- Notification systems (e.g., "new learning path available", "governance-event scheduled").

**When to use pub/sub in Flow Research-style contexts:**

- You want **event-driven workflows** (e.g., governance-events, ML-driven alerts).
- You want to avoid hard-coded dependencies between components (e.g., dashboard, analytics, rewards, and governance services).

---

### 3. Message Queues (Point-to-Point)

**Message queues** (also called **point-to-point** or **queue-style**) are:

- A **producer** sends a message to a **queue**.
- A **consumer** (or set of consumers) reads and processes messages from that queue, often in order.

Unlike pub/sub, a queue usually:

- targets **one or a small group** of consumers,
- may ensure **at-least-once** or **exactly-once** delivery.

Key properties:

- **Decoupled in time**: the producer can send messages even if the consumer is offline.
- **Ordered and buffered**: the queue can smooth out bursts of work.

Examples:

- Task queues (e.g., "process this governance-proposal", "compute this reward-batch").
- Background jobs (e.g., re-score learners, aggregate activity logs).

**When to use message queues:**

- You have **asynchronous work** that should not block the user.
- You want to **balance load** over time (e.g., ML-based scoring, bulk computations).

---

### 4. Other Common Patterns (High-Level View)

Several other patterns appear in protocol and distributed-system design:

- **Event-driven**: components react to **events** from other parts of the system (often layered on top of pub/sub or queues).
- **Broadcast/multicast**: one sender sends to **many receivers** simultaneously (sometimes used in IoT or real-time dashboards).
- **Push / pull streaming**: systems that continuously stream data (e.g., WebSockets, Kafka-style topics).

You don't need to dive deep into all of these now; the key is to **recognize** them when you see them and know that they are **patterns**, not random ad-hoc designs.

---

## Choosing a Pattern for Your Flow Research-Style Protocol

To decide which communication pattern to use, ask:

### 1. Do you need an immediate answer?

- Yes -> lean toward **request-response**.
- No -> lean toward **pub/sub** or **message queues**.

### 2. Do you know your receivers?

- Yes (specific, known services) -> **request-response** or **message queues**.
- No (many unknown services may care) -> **pub/sub**.

### 3. Do you want decoupling and async?

- Yes -> **pub/sub** or **message queues**.
- No (simple client-server interaction) -> **request-response**.

In Flow Research-style thinking, a typical setup combines:

- **request-response** for user-facing APIs (e.g., dashboard queries).
- **pub/sub** (or event streams) for **protocol-level events** (e.g., governance-state changes, learner-activity events).
- **message queues** for **background work** (e.g., re-scoring, batch processing).

This allows you to keep **core protocols** simple and let **applications** opt in to what they care about.

---

## Implementation Sketch

```yaml
message:
 type: protocol.event
 id: unique-id
 required_fields: [type, id, timestamp, payload]
 compatibility: backward-compatible additions only
```

## Practical Exercises

### Exercise 1: Identify Patterns in Existing Systems

Pick two real-world systems you know (e.g., a web app, a learning platform, or a governance-tool):

- For each, identify at least one **request-response** interaction.
- Identify at least one **pub/sub** or **event-driven** interaction (even if you only infer it).
- Write a short note explaining why each pattern fits that use-case.

This trains you to see patterns instead of "just HTTP."

### Exercise 2: Sketch a Flow Research-Style Event-Driven Flow

Design a small Flow Research-style workflow (e.g., governance-proposal approval):

- Decide which parts should use **request-response** (e.g., user submits a proposal).
- Decide which parts should use **pub/sub** (e.g., "proposal-submitted" event that triggers notifications, analytics, and governance-dashboard updates).
- Decide which parts should use **message queues** (e.g., async scoring or reward-calculation).

Sketch this as a simple diagram or list of steps annotated with patterns.

### Exercise 3: Refactor a Design

Take a design you previously wrote as a plain request-response API:

- Imagine replacing some of its synchronous calls with **events** and **queues**.
- Write a short note describing what would change and how this affects coupling and observability.

This helps you move from "everything is an immediate API call" to **pattern-aware** design.

---

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain request-response, pub/sub, and message queues at a high level.
- I can say when each pattern is appropriate for a given interaction.
- I can sketch which pattern to use for Flow Research-style use-cases like governance-events or ML-driven alerts.
- I can see how communication patterns sit under protocol design.

Action item: write a short note in your lab repo describing one Flow Research-style interaction you reframed using a better communication pattern and why that improved the design.

---

## Further Reading

- [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 2119 keywords](https://www.rfc-editor.org/rfc/rfc2119)
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

## Next Steps

- Read `04-protocol-specification.md` next to learn how to write **text-plus-diagram** spec for protocols that use these communication patterns.
- Treat communication patterns as **first-class design choices**, not implementation details.
- When you design a protocol, start by asking: "What pattern will we use for this interaction?"

---

*This lesson gives Flow Research Initiative trainees a beginner-level understanding of communication patterns in distributed systems and protocols, focusing on request-response, publish-subscribe (pub/sub), and message-queue styles, and how to choose the right pattern for Flow Research-style governance-event, ML-driven, and on-ramp flows.*
