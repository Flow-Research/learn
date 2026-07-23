---
id: economic-incentive-design
title: Economic and Incentive Design
track: products
level: intermediate
version: 1.0
Prerequisites: "00-value-engine, 03-workstream, 05-flowledger"
Duration: "~30-45 minutes (reading + 3 exercises)"
Format: "Concept lesson with 3 hands-on exercises (gameability mitigation, reward function design, comparative analysis)"
Future_Topics: "Deeper mechanism-design case studies, Governance of Incentive Parameters, Anti-Sybil Primitives (proof-of-personhood, staking), 02-Blockchain Tokens and Economic Incentives"
Related_docs:
  - 03-workstream
  - 05-flowledger
  - 02-Blockchain/01-beginner/02-ecosystem/02-tokens-and-economic-incentives
  - 02-Blockchain/03-advanced/01-protocol-engineering/03-governance-mechanisms
---

# Economic and Incentive Design

Flow Research's value engine depends on incentives that align contributor behavior with system health. WorkStream handles task distribution and rewards. FlowLedger tracks contributions. Understanding how incentives work helps you design better attribution, reward, and reputation mechanisms.

## Key concepts

- **Attribution** — linking output to the contributor who produced it. WorkStream's attribution stage determines who gets credit.
- **Reward functions** — how points are assigned based on task difficulty, quality, and impact.
- **Reputation** — accumulated history of reliable work. Enables trust without repeated verification.
- **Sybil resistance** — preventing a single actor from pretending to be many. Essential for fair reward distribution.
- **Gameability** — every incentive system can be gamed. Good design anticipates exploits and builds guards.

## Connection to FlowLedger

FlowLedger is the operational layer that implements incentive design for the fellowship. Points, badges, and the leaderboard are specific reward mechanisms. The theory behind them — what motivates contribution, how to measure quality, how to prevent abuse — is what this topic covers.

## Exercises

1. Identify a potential gameability vector in a point-based contribution system. Propose a mitigation.
2. Design a reward function for a task type in WorkStream. What inputs does it need? How does it prevent abuse?
3. Compare FlowLedger's reputation model with another system you know (stackoverflow, Gitcoin, etc.). What tradeoffs does each make?
