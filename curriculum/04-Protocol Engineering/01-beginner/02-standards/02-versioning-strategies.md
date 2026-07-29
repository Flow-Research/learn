---
id: versioning-strategies
title: Versioning Strategies
track: protocol-engineering
level: beginner
version: 1.1
Prerequisites: "specification-writing"
Duration: "~30-40 minutes"
Format: "Watch First video + reading + SemVer classification exercise + v1-to-v2 migration plan exercise"
Future_Topics: "Protocol Lifecycle and Governance, Upgrade Paths, Deprecation Policies"
Related_docs:
  - 01-beginner/02-standards/01-specification-writing
  - 02-intermediate/02-governance-and-ecosystem/01-upgrade-paths
  - 06-rust-engineering/06-modules-crates-workspaces-project-shape
---

# Versioning Strategies

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/97i9pOa2EyE"
 title="What is Semantic Versioning"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain why **versioning** is critical for evolving protocols and APIs.
- Describe common **versioning schemes** (e.g., semantic versioning, URIs, headers).
- Classify **breaking vs non-breaking changes** and how they affect version numbers.
- Choose a versioning strategy for a Flow Research-style protocol or API.

## Concept Map

```mermaid
flowchart LR
  A["Patch"] --> B["Bug fix"]
  C["Minor"] --> D["Backward-compatible feature"]
  E["Major"] --> F["Breaking change"]
```

## Quantitative Lens

Semantic versioning separates compatibility from chronology:

$$
version = major.minor.patch
$$

Increment `major` when existing clients must change to remain correct.

## Introduction

In protocol work, you rarely "freeze" a design forever.
New features, bug fixes, and security updates inevitably change how systems talk to each other.

**Versioning** is the practice of:

- tagging each released form of a protocol or API with a **version identifier**,
- and using that tag to control **breaking** versus **non-breaking** evolution.

In Flow Research-style systems, versioning keeps:

- different implementations (e.g., clients, dashboards, governance tools)
- able to **interoperate** even as the protocol changes over time.

---

## Why Versioning Matters

Without versioning, a small change in a protocol can:

- break existing clients,
- confuse users,
- or create multiple "local forks" of the same protocol in practice.

Versioning gives you:

- **clear boundaries** between different eras of a protocol,
- **upgrade paths** for implementers,
- and a way to **support multiple versions** while evolving forward.

In Flow Research-style thinking:

- a protocol is a **shared contract** between actors.
- **versioning** is how you manage that contract over time without losing trust.

---

## Semantic Versioning (SemVer)

The most widely used scheme is **semantic versioning**: `MAJOR.MINOR.PATCH`.

Given a version string `1.2.3`:

- **MAJOR** (1): increment when you make **incompatible API or protocol changes**.
- **MINOR** (2): increment when you add **new features** in a **backward-compatible** way.
- **PATCH** (3): increment when you make **backward-compatible bug fixes**.

For example:

- `1.2.3` -> `1.2.4`: small bug-fix; no breaking changes.
- `1.2.4` -> `1.3.0`: added new features; existing clients still work.
- `1.3.0` -> `2.0.0`: incompatible changes (e.g., removed fields, changed semantics).

In Flow Research-style systems:

- use SemVer for **public contracts** (e.g., protocol APIs, event schemas).
- treat `MAJOR` bumps as **migration events** that require planning and communication.

---

## Common Versioning Patterns for APIs and Protocols

### 1. URI-Versioning

- Encode the version in the **URL path**:

 - `/api/v1/users`
 - `/api/v2/users`

This pattern is:

- highly visible to users and tools,
- and easy to cache and route, since each version has its own URI.

It works well for **public APIs** but can create many URLs to manage.

Flow Research-style twist:

- each major protocol revision (e.g., governance-state machine changes) can live under a new `/vN/...` path.

### 2. Header-Based Versioning

- Pass the version in an HTTP header, such as:

 - `Accept: application/vnd.myapi.v1+json`

This keeps the **URI clean** and moves the versioning decision to the client headers.

Pros:

- less noise in the URL.
Cons:

- harder to see which version is being used just from the URL, and less cache-friendly.

Flow Research-style twist:

- useful when you want **one endpoint** but **multiple protocol variants** behind it.

### 3. Query-Parameter Versioning

- Put the version in a query string:

 - `/api/users?version=2`

This is flexible but:

- less REST-like,
- and can create caching and bookmarking issues.

Use this sparingly, and prefer **URI** or **header**-based schemes for public protocols.

---

## Versioning in Protocol Design

Protocols need versioning just like APIs:

- **Message formats** must change gracefully.
- **State-machine transitions** may be added or removed.
- **event schemas** evolve over time.

Good practices for protocol versioning include:

- Define a **version field** in key messages or in the handshake (e.g., `protocol_version: 1` in an initial message).
- Use **semantic versioning semantics**: clearly document what counts as a breaking change for the protocol.
- Support **multiple versions** for a transition window, then **deprecate** and **retire** older ones.

In Flow Research-style systems:

- a protocol version can correspond to:

 - a **state-machine definition**,
 - a **schema for events or proposals**,
 - and a **set of invariants** enforced by validators or nodes.

---

## Breaking vs Non-Breaking Changes

A key idea in versioning is to classify changes:

### 1. Breaking Changes

A **breaking change** is one that:

- existing clients or validators **cannot handle** without modification.

Examples:

- Removing or renaming required fields in requests or events.
- Changing the **meaning** of a field (e.g., `score` used to be 0-100, now 0-1).
- Removing a state or transition that clients relied on.

These should trigger a **MAJOR** version bump under SemVer and careful migration planning.

### 2. Non-Breaking Changes

A **non-breaking change** keeps existing clients working "as-is."

Examples:

- Adding optional fields.
- Adding new endpoints or events that old clients simply ignore.
- Fixing bugs in behavior that did not affect the contract.

These can usually be handled with **MINOR** or **PATCH** bumps.

In Flow Research-style practice:

- the **spec** (from `01-specification-writing.md`) should classify which changes are breaking and which are not.

---

## How to Use Versioning in Flow Research-Style Work

### 1. Plan Versioning Early

- Decide on a **versioning scheme** (e.g., SemVer + URI-based) **before** you publish the first protocol version.
- Document how you will **label** and **communicate** new versions.

This avoids painful retrofits later.

### 2. Communicate and Deprecate Clearly

- Publish **changelogs** that explain:

 - what changed,
 - whether it is breaking,
 - and what clients must do.

- Give users **time to migrate** before retiring an old version.

Clear communication is part of **trust-engineering**.

### 3. Keep Contract Versioning Separate from Implementation Versioning

- An internal **implementation** (e.g., rewriting a service from Python to Rust) should not force a **protocol version bump** if the **contract** does not change.
- Separate implementation releases from **contract** releases.

This keeps clients from needing to constantly update for non-breaking internal changes.

---

## Implementation Sketch

```yaml
compatibility_policy:
  patch: bug fixes only
  minor: additive fields or endpoints
  major: removed fields or changed meaning
```

## Practical Exercises

### Exercise 1: Version a Small Flow Research-Style Protocol

Take a protocol you defined in `01-specification-writing.md`:

- Assign it an initial version (e.g., `1.0.0`).
- Make a **small change** (e.g., add a new optional field or event) and decide whether it should be a `PATCH`, `MINOR`, or `MAJOR` change.
- Write a short note explaining your reasoning.

### Exercise 2: Choose a Versioning Pattern for an API

Design a small API that exposes your protocol (e.g., `/governance/v1/proposals`):

- Decide whether you will use URI, header, or query-parameter versioning.
- Write a short note explaining why that pattern suits your Flow Research-style context.

### Exercise 3: Plan a Migration from v1 to v2

Imagine your protocol needs a **breaking** change:

- Rename a key field, or add a new state that changes the governance-flow.
- Sketch a **migration plan**:

 - which version you keep live during transition,
 - how clients will be notified,
 - and how long old clients can still work.

This trains you to think in **time-boxed transitions**, not just "big-bang" upgrades.

---

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain why versioning is important for protocols and APIs.
- I can describe semantic versioning (`MAJOR.MINOR.PATCH`) and what each part means.
- I can recognize breaking vs non-breaking changes.
- I can choose a versioning pattern for a Flow Research-style protocol or API.

Action item: write a short note in your lab repo describing how you versioned a Flow Research-style protocol and how you would handle a future breaking change.

---

## Further Reading

- [RFC 9110 HTTP semantics](https://www.rfc-editor.org/rfc/rfc9110)
- [RFC 2119 keywords](https://www.rfc-editor.org/rfc/rfc2119)
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

## Next Steps

- Read `03-protocol-lifecycle-and-governance.md` next to see how versioning connects to **deprecation, migration, and policy** over time.
- Treat versioning as **part of your protocol contract**, not an afterthought.
- When you release a Flow Research-style protocol, include a **version**, clear **changelog**, and known **deprecation** schedule.

---

*This lesson gives Flow Research Initiative trainees a beginner-level understanding of versioning strategies in protocol engineering, focusing on semantic versioning (`MAJOR.MINOR.PATCH`), common API-style patterns (URI, header, query-parameter), and how to classify and manage breaking vs non-breaking changes in Flow Research-style governance-style and ML-driven protocols.*
