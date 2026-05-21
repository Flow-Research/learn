---
id: what-are-agent-systems
title: What Are Agent Systems?
---

# What Are Agent Systems?

An agent system is software that perceves its environment, makes decisions, and takes actions to achieve goals. In the Flow ecosystem, a Personal Operator is one kind of agent system — persistent, configurable, and accountable.

## Agents vs programs

A traditional program follows a fixed path. An agent decides what to do next based on context. That decision-making is what makes agents powerful and what makes them hard to build reliably.

## Core components

- **Runtime** — the environment where the agent executes (Jarvis).
- **Orchestration** — how the agent decides what to do next (LLM calls, tool selection, planning).
- **Tools** — external capabilities the agent can invoke (APIs, databases, filesystems).
- **Memory** — what the agent remembers across interactions.
- **Safety** — boundaries that prevent the agent from acting outside its scope.

## Flow context

Every Flow product touches agent systems. Jarvis is the runtime. Garden is the workspace where agents and humans collaborate. WorkStream distributes tasks to agents. Harnessy evaluates their output. Understanding agent systems broadly helps you contribute to any of them.

## Exercises

1. List three differences between a traditional web application and an agent system.
2. What happens when an agent makes a wrong decision? Trace the failure modes.
3. Identify which agent system components are present in Jarvis, Garden, WorkStream, and Harnessy respectively.
