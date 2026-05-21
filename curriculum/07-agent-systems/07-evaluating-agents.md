---
id: evaluating-agents
title: Evaluating Agents
---

# Evaluating Agents

Unlike traditional software where a function either passes or fails, agent output is probabilistic. Evaluation determines whether the agent did the right thing — not just whether it ran without error.

## What to evaluate

- **Correctness** — did the agent produce the right answer or take the right action?
- **Faithfulness** — did the agent follow its instructions and stay within scope?
- **Efficiency** — did it use reasonable resources (calls, tokens, time)?
- **Safety** — did it avoid prohibited actions or outputs?
- **Recoverability** — did it handle errors gracefully?

## Evaluation methods

- **Unit tests** — deterministic checks for specific behaviors (tool selection, output format, refusal).
- **Golden datasets** — known inputs with expected outputs. Run the agent and compare.
- **Adversarial testing** — try to break the agent with edge cases, injections, and ambiguous instructions.
- **Human evaluation** — reviewers assess agent performance on real or simulated tasks.
- **Automated judges** — another LLM evaluates the agent's output against rubric criteria.

## Flow context

Harnessy provides the evaluation infrastructure. It integrates with WorkStream verification so that agent output can be validated before it is accepted and rewarded. A contributor working on Harnessy might build a new evaluation method, improve the rubric, or create adversarial test suites.

## Exercises

1. Write three unit tests for an agent that sends emails. What behaviors do you test?
2. Design a golden dataset with five test cases for an agent that answers questions about a codebase. Include at least one edge case.
3. Propose an adversarial test for an agent with access to a database. Can you make it produce a harmful query?
