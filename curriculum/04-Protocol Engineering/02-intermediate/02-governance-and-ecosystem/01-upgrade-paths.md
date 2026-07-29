---
id: upgrade-paths
title: Upgrade Paths
track: protocol-engineering
level: intermediate
version: 1.1
Prerequisites: "versioning-strategies; helpful: resilience-patterns"
Duration: "~40-50 minutes"
Format: "Watch First video + reading + upgrade-plan design exercise + migration-script design exercise + rollback planning"
Future_Topics: "Governance Models for Evolution, Deprecation Schedules, Migration Tooling, 02-Blockchain Governance Mechanisms"
Related_docs:
  - 01-beginner/02-standards/02-versioning-strategies
  - 02-intermediate/02-governance-and-ecosystem/03-community-feedback
  - 02-Blockchain/03-advanced/01-protocol-engineering/03-governance-mechanisms
---

# Upgrade Paths

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

- Explain what an **upgrade path** is and why it matters for evolving protocols and APIs.
- Describe common **migration strategies** for moving from one protocol version to another (e.g., side-by-side, gradual cutover, migration tools).
- Design a **clear, safe migration plan** for a Flow Research-style protocol (e.g., governance-state machine, reward-calculation) from v1 to v2.
- Communicate **deprecation timelines** and **backwards-compatibility policies** to other teams and users.

## Concept Map

```mermaid
flowchart LR
  A["v1 active"] --> B["v2 announced"]
  B --> C["Dual support"]
  C --> D["v1 deprecated"]
  D --> E["v1 removed"]
```

## Quantitative Lens

A migration is safer when the overlap window exceeds real client upgrade time:

$$
OverlapWindow \geq p95(ClientUpgradeDuration)
$$

## Introduction

At the intermediate level, you cannot assume that your protocol will stay at `v1` forever.
New features, performance improvements, and corrected design flaws will require **breaking or non-breaking changes** over time.

An **upgrade path** is the **planned route** from an older version of a protocol or API to a newer version, designed so that:

- existing clients can **migrate safely**, and
- the system can **evolve without breaking everyone at once**.

In Flow Research-style systems, this is especially important because:

- protocols may be used by:

 - governance dashboards,
 - ML-scoring services,
 - and on-ramp tools,

often built by different teams at different times.

Planning upgrade paths early reduces:

- chaos in production,
- "stuck" clients on old versions, and
- risk of fragmented ecosystems.

---

## What Is an Upgrade Path?

An **upgrade path** is a set of **steps and constraints** that describe how to move from **one state (e.g., v1 protocol)** to **another (e.g., v2)**:

- who can upgrade,
- when,
- in what order, and
- with what guarantees.

Two complementary ideas:

- **Backwards compatibility**: newer v2 servers can still talk to older v1 clients.
- **Forwards compatibility**: v1 clients can still talk to v2 servers where possible, or at least fail gracefully.

In practice, an upgrade path usually includes:

- **Timeline**: when v1 will be deprecated, when v2 goes live.
- **Tooling**: migration scripts, converters, or bridges.
- **Escalation plan**: what to do if something goes wrong (e.g., rollback, feature flags).

For Flow Research-style protocols, this is a **governance and engineering concern**, not just an infra detail.

---

## Common Upgrade-Path Patterns

### 1. Side-by-Side Deployment

Run **v1 and v2 in parallel**, so that:

- clients can choose which version to use,
- and new clients can start on v2 while old ones stay on v1.

Typical setup:

- v1 and v2 expose **different endpoints or URIs** (e.g., `/v1/...` vs `/v2/...`).
- A **load balancer**, **feature flags**, or a **routing rule** controls which traffic goes where.

Advantages:

- smooth, **gradual migration**,
- ability to **A/B** compare v1 and v2 behavior.

Disadvantages:

- requires **running two stacks** for a time,
- and careful **state-synchronization** if they share underlying data.

Flow Research-style motivation:

- lets governance-tools and dashboards migrate at their own pace.

### 2. Gradual Cutover (Traffic-Shifting)

Instead of a "big-bang" switch, you:

- slowly **shift traffic** from v1 to v2, e.g., via:

 - DNS,
 - traffic-management services, or
 - feature-flag percentages.

This is common in cloud-style environments where you can:

- route 10%, 50%, then 100% of governance- or learner-traffic to v2.

Benefits:

- if v2 has bugs, you can **pause or roll back**.
- reduces risk of massive disruption.

Flow Research-style use-case:

- shifting governance-proposal traffic from v1 to v2 while monitoring for state-consistency issues.

### 3. Migration Tools and Converters

Some protocols provide:

- an official **migration tool** that converts v1-style data or state into v2-style.

Examples:

- Aave provided a **v1 -> v2 migration tool** for positions and funds.
- Other blockchains provide **snapshot- and replay-based** migration tools.

How this works in practice:

- freeze or mark v1 as read-only,
- run a converter that transforms governance-state or reward-state into v2 format,
- then start v2 from the converted state.

This is powerful when v2 has a **changed state-machine** or schema.

Flow Research-style twist:

- you can design similar **"state-converter"** binaries that translate Flow Research-style learner-or-governance state across versions.

### 4. Optional vs Mandatory Migration

Sometimes v1 -> v2 is:

- **Optional**: teams can keep using v1 for a while, but no new features are added there.
- **Mandatory**: after a deprecation date, v1 is shut down, and everyone must upgrade.

Best practice:

- start with **optional**, then move to **mandatory** after a deprecation window.

This gives teams time to plan, test, and train.

Flow Research-style motivation:

- lets slower-moving governance communities or dashboards avoid forced rush-upgrades.

---

## How to Design a Concrete Upgrade Path

For a Flow Research-style protocol, a good upgrade-path design usually includes these steps:

### 1. Assess the Change

- Classify the change:

 - **Backwards-compatible** (e.g., added optional fields) -> can keep v1 and v2 alive together.
 - **Breaking** (e.g., removed fields, changed state-machine) -> likely requires a migration plan.

- Decide whether you will:

 - support both versions,
 - or force a migration.

### 2. Define a Timeline

- Publish a **timeline** with:

 - release date of v2,
 - "soft" deprecation date of v1,
 - and "hard" shutdown date of v1.

Clear deprecation dates prevent **accidental lock-in** to old versions.

Flow Research-style best practice:

- keep the deprecation window **long enough** for governance bodies and dashboards to coordinate.

### 3. Build Tooling and Scripts

Design a **migration path** between versions by:

- writing:

 - **state-conversion scripts**,
 - **idempotent migration tools** that can be rerun safely,
 - and **validation checks** that confirm state is consistent after migration.

Example:

- a script that:

 - dumps v1 governance-proposals,
 - transforms them into v2-style state,
 - and validates that `APPROVED` proposals still have the same semantics.

### 4. Test the Upgrade in Staging

- Run the upgrade on **staging or canary** environments that mirror production.
- Verify that:

 - dashboards still show correct state,
 - forecasts and ML-style scores still work,
 - and governance-nodes behave as expected.

Testing the upgrade path is as important as testing the protocol itself.

### 5. Communicate, Communicate, Communicate

- Publish:

 - upgrade guide,
 - deprecation schedule,
 - and example clients or adapters.

Clear communication reduces:

- confusion,
- and the risk of "someone forgot to upgrade."

Flow Research-style style:

- treat upgrade communication as part of **governance and on-boarding**, not just ops.

---

## How This Fits Into Flow Research-Style Systems

In Flow Research-style protocols you can:

- plan upgrades around **versioned specs** (from `01-specification-writing.md`) and **semantic versioning** (from `02-versioning-strategies.md`).
- use **migration-style thinking** not just for protocols, but for:

 - governance-state machines,
 - reward-calculation logic,
 - and learner-on-ramp flows.

Upgrade-path design connects directly to:

- **deployment patterns** (e.g., side-by-side, canary, feature flags),
- **governance** (e.g., "when will this v2 change be mandated?"),
- and **MLOps** (e.g., "will this protocol change break ML-based reward-scoring?").

---

## Implementation Sketch

```json
{
  "version": "2.0",
  "deprecatedVersions": ["1.x"],
  "sunsetDate": "2026-12-31",
  "migrationGuide": "/docs/migrate-v2"
}
```

## Practical Exercises

### Exercise 1: Sketch an Upgrade Path for a Flow Research-Style Protocol

Take a protocol you have designed (e.g., governance-state machine or reward-calculation):

- Decide whether v2 will be **backwards-compatible** or **breaking**.
- Sketch an upgrade path that includes:

 - side-by-side or gradual cutover plan,
 - a simple state-migration idea (e.g., JSON-to-JSON transform),
 - and a deprecation timeline.

Write it as a short plan, not full code.

### Exercise 2: Design a Migrating Script

- For the same protocol, design a **state-migration script** at the API level:

 - which endpoints or data you would read from v1,
 - how you would transform it,
 - and which endpoints or data you would write into v2.

This trains you to think in **data-flow terms**, not just state-machine diagrams.

### Exercise 3: Plan for Rollback

- Imagine your v2 deployment has a bug that breaks governance-state semantics.
- Sketch a **rollback plan**:

 - from v2 back to v1 (or a safe v1.1),
 - including data-backup and validation steps.

This trains you to treat upgrades as **two-way paths**, not one-way jumps.

---

## Self-Assessment

Rate yourself from 1 to 5:

- I can explain what an upgrade path is and why it matters for protocols and APIs.
- I can describe common patterns (side-by-side, gradual cutover, migration tools, optional vs mandatory).
- I can sketch a concrete upgrade path for a Flow Research-style protocol.
- I can connect upgrade paths to deployment patterns and governance decisions.

Action item: write a short note in your lab repo describing one upgrade path you designed for a Flow Research-style protocol and how it balances safety, risk, and coordination across teams.

---

## Further Reading

- [Pact contract testing](https://docs.pact.io/)
- [Semantic Versioning](https://semver.org/)
- [OpenAPI specification](https://spec.openapis.org/oas/latest.html)
- [Enterprise Integration Patterns](https://www.enterpriseintegrationpatterns.com/)

## Next Steps

- Read `02-governance-models-for-evolution.md` next to see how to align upgrade paths with **on-chain or off-chain governance bodies**.
- Treat every major protocol release as something that must have a **written upgrade path and deprecation schedule**.
- When you release a Flow Research-style protocol, document not only the v2 design, but **how v1 clients will move into it safely**.

---

*This lesson gives Flow Research Initiative trainees an intermediate-level understanding of upgrade paths in protocol engineering, focusing on side-by-side deployment, gradual cutover, migration tools, and deprecation timelines, and how to design safe, communicated paths from v1 to v2 for Flow Research-style governance-style and ML-driven protocols.*
