---
id: specification-writing
title: Specification Writing
track: protocol-engineering
level: beginner
version: 1.1
Prerequisites: "protocol-vs-application, state-machines, communication-patterns"
Duration: "~40-50 minutes (longest beginner lesson because of full spec writing exercise)"
Format: "Watch First video + reading + Mermaid concept map + spec-writing exercise (draft a tiny protocol spec)"
Future_Topics: "Formal and Semi-Formal Notation, Versioning Strategies, Template Library"
Related_docs:
  - 01-beginner/01-protocol-concepts/03-communication-patterns
  - 01-beginner/02-standards/02-versioning-strategies
  - 01-foundations/04-specification/01-writing-design-docs
---

# Specification Writing

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/cIhaSS7B8BA"
 title="Expert Specification Writing: Applying the Best Practice Guide"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain why a **clear written specification** is essential for protocol design.
- Identify the **core sections** of a protocol or system specification (e.g., scope, behavior, constraints, diagrams).
- Write **simple, testable "shall"-style requirements** without vague language.
- Use diagrams (state machines, data-flow sketches) to complement text in your spec.

## Concept Map

```mermaid
flowchart TD
  A["Problem statement"] --> B["Normative requirements"]
  B --> C["Message formats"]
  C --> D["State transitions"]
  D --> E["Error handling"]
  E --> F["Test vectors"]
```

## Quantitative Lens

A specification becomes clearer as more requirements become testable:

$$
Ambiguity = Requirements - TestableStatements
$$

## Introduction

You already know how to:

- distinguish **protocol vs application**,
- model behavior with **state machines**, and
- structure **communication patterns**.

Now it is time to **document** those ideas in a way that:

- other engineers can understand,
- stakeholders can review, and
- the future-you can read without guessing.

A **specification** (often called a "spec") is a **written description** of what a system or protocol **must do**, not just what it *might* do.

In Flow Research-style work, good specs help you:

- align teams,
- avoid mis-implementations, and
- keep protocols **reusable and maintainable**.

---

## What Is a Specification?

A **specification** is a document that describes:

- **what** a system or protocol should do,
- **how** it behaves in key scenarios, and
- **what constraints** it must satisfy (e.g., performance, safety, security).

For protocols, a spec usually answers:

- Who are the **actors** (clients, servers, nodes, voters, etc.)?
- What **messages** can they exchange?
- What **state** can the system be in?
- What **invariants or guarantees** hold (e.g., "no double-spend")?

A good spec is:

- **clear**: written in simple, precise language.
- **complete enough**: enough to build from, but not overly detailed.
- **testable**: each requirement can, at least in principle, be checked or tested.

This is the "paper-design" stage before you drop into code.

---

## Why Specs Matter for Protocols

Protocols are often **shared** across many implementations and teams.
Without a written spec:

- everyone has a slightly different mental model.
- small differences in interpretation lead to **interoperability bugs**.

For example:

- the IETF and similar standards bodies insist on **detailed protocol specs** because they expect **many independent implementations** to talk to each other.

In Flow Research-style thinking:

- writing a spec is an **engineering discipline**, not "extra documentation."
- it reduces churn, mis-alignment, and re-design later.

---

## Core Sections of a Protocol Spec

You do not need every section to be huge; just make sure each one is present and clear.

### 1. Title, Metadata, and Scope

- **Title** and **short description** of the protocol.
- **Authors / maintainers** and contact.
- **Audience**: who is this spec for? (engineers, PMs, governance bodies?)
- **Scope**: what is in-scope and what is not-scope.

The "scope" is especially important because it:

- stops people from over-designing the protocol,
- and keeps the spec focused on the core behavior.

### 2. Terminology and Definitions

- Define **special terms** used in the protocol, even if they seem obvious.
- Point to **external standards** when you rely on them (e.g., "we use the definitions from RFC 2119 for `MUST`, `SHOULD`, `MAY`").

This avoids confusion like:

- Does "user" mean "learner" or "admin"?
- What does "valid proposal" actually mean?

### 3. Actors and Roles

Describe:

- **Who the actors are** (e.g., learner, mentor, validator, dashboard, governance-body).
- **What each role is allowed to do** (e.g., "only governance-body can approve a proposal").

This is part of **security and policy** design, not just naming.

### 4. Behavior and State

Here you combine:

- **State machine** ideas (from `02-state-machines.md`).
- **Key messages or events** (from `03-communication-patterns.md`).

Structure this section around:

- **Core states** of the protocol (e.g., `DRAFT`, `UNDER_REVIEW`, `APPROVED`).
- **Transitions** between states (e.g., when event `approve` arrives, move from `UNDER_REVIEW` to `APPROVED`).
- **Message formats** (e.g., JSON-style shapes for requests, events, or transactions).

You can write:

- a **state-transition table**,
- or short **scenarios** (e.g., "happy-path proposal flow" and "rejection flow").

### 5. Requirements and Constraints

Turn behavior into **requirements**.

A common pattern is to use **"shall" language** to make specs testable:

- "The system **shall** persist the proposal when it transitions from `DRAFT` to `UNDER_REVIEW`."
- "The system **shall not** allow a proposal in state `EXECUTED` to be moved back to `UNDER_REVIEW`."

Other constraints you may include:

- **Performance**: latency, throughput, or load bounds.
- **Security**: e.g., "only authenticated users may submit proposals."
- **Availability / durability**: how the system behaves under failures or restarts.

### 6. Data Formats and APIs

For protocol-style systems, you often want to pin down:

- **Data formats** (e.g., fields in a proposal, fields in a vote or reward).
- **APIs or message endpoints** (e.g., HTTP-style endpoints or event-schema).

Even if you are not writing an RFC-style spec, sketching these as:

- JSON-style examples,
- or pseudocode type-signatures,

helps prevent ambiguity when others implement clients or services.

### 7. Examples and Diagrams

- Include **example flows** (e.g., "submit -> review -> approve -> execute").
- Add **diagrams**:

 - a **state-machine diagram**,
 - a **simple data-flow** between actors.

Diagrams are not "nice-to-have"; they are **part of the spec** and often prevent misunderstandings faster than pages of text.

---

## Good Writing Habits for Specs

### 1. Be Precise, Not Vague

Avoid:

- "the system should handle proposals quickly"
- "users might be able to approve proposals."

Instead:

- "The system **shall** persist the proposal within 2 seconds of receiving a valid `submit` request."
- "Only users with role `governance_admin` **shall** be allowed to send an `approve` event."

Precision makes it possible to **verify** and **test** the spec.

### 2. Use "Shall", "Must", "Should", and "May"

Standards like RFC 2119 define:

- **MUST / SHALL** = this is required.
- **SHOULD** = strongly recommended but there can be rare exceptions.
- **MAY** = optional.

You do not need to follow RFC 2119 exactly, but **being consistent** helps everyone know what is mandatory and what is optional.

### 3. Keep It Lean and Focused

- Do **not** try to document every implementation detail.
- Focus on:

 - what the protocol **must guarantee**,
 - and what the implementer is **allowed to choose** (e.g., internal algorithms, serialization format).

This keeps the spec readable and maintainable.

---

## How This Fits Into Flow Research-Style Work

In Flow Research-style protocols you can:

- Write a **core spec** for the protocol (e.g., governance-state machine, reward-calculation rules).
- Write **second-level specs** for:

 - specific **applications** (e.g., dashboard, CLI, API).
 - or for **ML-driven score layers** that plug into the protocol.

This separation allows:

- the **protocol spec** to stay stable,
- while **applications** can evolve without changing the underlying rules.

Furthermore, a good spec:

- makes it easier to **add new actors** (e.g., new governance-tools) later.
- and makes **onboarding** new engineers much faster.

---

## Implementation Sketch

```markdown
The server MUST reject messages with expired timestamps.
The client SHOULD retry idempotent requests after transient failures.
The implementation MAY cache public metadata for 300 seconds.
```

## Practical Exercises

### Exercise 1: Draft a Tiny Protocol Spec

Pick a small Flow Research-style workflow (e.g., a proposal flow, reward-calculation, or on-ramp):

- Write a short spec that includes:

 - title, authors, and scope,
 - a list of actors and roles,
 - a small state-machine description (states + transitions),
 - a few "shall"-style requirements.

Do not aim for perfection; aim for **clarity and testability**.

### Exercise 2: Add Examples and Diagrams

Using the same workflow:

- Add **one example scenario** (e.g., "happy-path" and one "error-path").
- Sketch a **state-machine diagram** (boxes + arrows) and paste it into your lab repo.

This trains you to **write and draw at the same time**.

### Exercise 3: Review and Refine

Ask yourself:

- Is anything **still ambiguous**?
- Are there places where **different implementers might disagree** on behavior?

Revise the spec to remove ambiguity and see how much clearer it becomes.

---

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain why a written specification is important for protocol design.
- I can structure a spec with core sections (scope, actors, behavior, requirements, data, examples).
- I can write simple "shall"-style requirements that are testable.
- I can see how diagrams and text fit together in a Flow Research-style protocol spec.

Action item: write a short note in your lab repo describing one Flow Research-style protocol you documented in a spec and how that changed how you think about the design.

---

## Further Reading

- [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 2119 keywords](https://www.rfc-editor.org/rfc/rfc2119)
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

## Next Steps

- Read `02-formal-and-semi-formal-notation.md` next to learn lightweight ways to add more rigor (e.g., simple state-machine tables) to your specs.
- Treat every new Flow Research-style protocol as something that **must have a spec**, even if it is short.
- Keep your specs living: update them as you learn and iterate, just like your codebase.

---

*This lesson gives Flow Research Initiative trainees a beginner-level understanding of specification writing in protocol engineering, focusing on clear structure (title, scope, behavior, requirements, data, and examples), precise "shall"-style requirements, and how to use diagrams to complement text in Flow Research-style protocol and governance-style systems.*
