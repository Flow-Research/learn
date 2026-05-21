---
id: curriculum-intro
title: About this curriculum
---

# About this curriculum

Flow Research is an evolving organization. Our research teams explore distributed systems, AI, and protocol infrastructure, and the work feeds into products still taking shape. This curriculum is the learning layer of that ecosystem — a structured path for engineers who want to build the kind of public-good technology these products depend on.

Things are moving fast, and this will change as we do.

## Products

The team is building a set of products that work as one system. Here is how they fit together:

- **[Jarvis](products/jarvis)** — the agent runtime. Spawns, configures, and secures Personal Operators so they can connect to the Flow economy.
- **[Garden](products/garden)** — the human-agent workspace. A persistent space where people and agents collaborate with connected tools, workflows, and approvals.
- **[WorkStream](products/workstream)** — the task pipeline. Takes work from economic value sources, distributes it to humans and agents, verifies outputs, and handles attribution and rewards.
- **[Harnessy](products/harnessy)** — the reliability layer. Tests agent behavior, evaluates task output, and closes the feedback loop so agents can be trusted with real work.
Jarvis gives the agent life. Garden gives the agent a workspace. WorkStream gives the agent and human valuable work. Harnessy makes the agent reliable.

## Contributing

Flow Research runs a [fellowship program](contributing/joining-fellowship) for engineers who want to help build these products or explore new ideas through the [research track](contributing/research-track). Contributions are tracked in [FlowLedger](products/flowledger) — points, badges, and a public ledger that makes every contribution visible and rewardable.

For now, the curriculum covers five areas:

### Foundations

How to learn, take rigorous notes, write design docs, and build a public portfolio.

- [Concepts](foundations/concepts/learning-hierarchy) — learning hierarchy, maieutic thinking, student vs engineer mindset
- [Practice](foundations/practice/reading-comprehension) — reading comprehension, effective notes, building a portfolio
- [Tooling](foundations/tooling/markdown-and-documentation) — markdown, version control, collaboration workflows
- [Specification](foundations/specification/writing-design-docs) — design docs, ADRs, API specs, research notes

Start here if you're new.

### Blockchain

From fundamentals through smart contracts and security to protocol engineering and scalability.

Beginner — [what is blockchain](Blockchain/beginner/fundamentals/what-is-blockchain), [layer 1 vs layer 2](Blockchain/beginner/ecosystem/layer-1-vs-layer-2), [tokens and incentives](Blockchain/beginner/ecosystem/tokens-and-economic-incentives), [decentralized identity](Blockchain/beginner/ecosystem/decentralized-identity)

Intermediate — smart contract design patterns, testing and deployment, common vulnerabilities, code audits, pen-test workflows

Advanced — protocol architecture, consensus tuning, governance mechanisms, state channels, rollups and sharding, interoperability

### AI/ML

Understand, use, and govern AI-driven components in production systems.

Beginner — [math for ML](AI-ML/beginner/foundations/math-for-ml), data pipelines, model lifecycle, Python ecosystem, notebooks, ML libraries

Intermediate — supervised learning, feature engineering, hyperparameter tuning, CI/CD for models, monitoring and drift, deployment patterns

Advanced — transformers, graph neural networks, reinforcement learning, paper replication, model alignment, ethics and responsibility

### Protocol Engineering

Design, implement, and evolve reusable protocols that systems communicate over.

Beginner — [protocol vs application](Protocol%20Engineering/beginner/protocol-concepts/protocol-vs-application), state machines, communication patterns, specification writing, versioning, interoperability

Intermediate — compatibility testing, scaling design, resilience patterns, upgrade paths, interchain protocols, community feedback

Advanced — latency optimization, consensus economics, security modeling, regulatory compliance, performance auditing, enterprise integration

### Agent Systems

How agents work under the hood — orchestration, tool use, memory, planning, safety, and evaluation.

- [What are agent systems?](agent-systems/what-are-agent-systems) — core components and how they fit Flow
- [LLM orchestration](agent-systems/llm-orchestration) — prompts, chains, routers, tool loops
- [Tool calling and integration](agent-systems/tool-calling-and-integration) — tool design, registry, security
- [Memory and state](agent-systems/memory-and-state) — short-term, long-term, episodic, procedural
- [Planning and reasoning](agent-systems/planning-and-reasoning) — approaches, failure recovery, reflection
- [Safety and guardrails](agent-systems/safety-and-guardrails) — input/output guardrails, escalation, kill switches
- [Evaluating agents](agent-systems/evaluating-agents) — correctness, faithfulness, adversarial testing, human eval

This area maps directly to Jarvis, Garden, WorkStream, and Harnessy — agents are the core of every Flow product.

---

## How to use this

**If you're just starting out** — begin with Foundations, then go deep in whichever area fits your interest.

**If you're experienced but new to this stack** — skip what you know, fill the gaps.

**If you're building a real project** — map your project across the curriculum. After each lesson, refactor your spec or diagrams.

Use the exercises at the end of each lesson to build a portfolio you can show others.

---

## What this assumes

You are willing to write, diagram, and code as you go. You care about maintainability and understandability, not just making things work. You do not need a PhD or a fancy title — you do need the habit of shipping small, explicit artifacts that show what you've learned.

---

## Next steps

Start with [Foundations](foundations/concepts/learning-hierarchy), or jump straight into an area:

- [AI/ML: Math for ML](AI-ML/beginner/foundations/math-for-ml)
- [Protocol Engineering: Protocol vs Application](Protocol%20Engineering/beginner/protocol-concepts/protocol-vs-application)
- [Blockchain: What is Blockchain](Blockchain/beginner/fundamentals/what-is-blockchain)
- [Agent Systems: What are agent systems?](agent-systems/what-are-agent-systems)
