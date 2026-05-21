---
id: memory-and-state
title: Memory and State
---

# Memory and State

An agent without memory starts fresh every interaction. Memory gives an agent continuity — it remembers past conversations, learned preferences, and task progress.

## Types of memory

- **Short-term / working memory** — the current conversation or task context. Usually the LLM's context window.
- **Long-term memory** — persisted information across sessions. User preferences, past decisions, learned skills.
- **Episodic memory** — records of past actions and outcomes. Useful for debugging, audit, and improvement.
- **Procedural memory** — how to do things. Skills, workflows, and standard operating procedures the agent has learned or been given.

## Storage approaches

- **Context window** — everything fits in the LLM's prompt. Simple but limited.
- **Vector store** — embeddings for semantic retrieval. The agent retrieves relevant memories based on current context.
- **Structured database** — relational or document store for structured state like task status, user settings, or tool configurations.
- **Hybrid** — combination of the above. Typically vector store for semantic retrieval plus structured DB for operational state.

## Challenges

- **Context window limits** — you cannot fit everything. You need retrieval strategies.
- **Staleness** — memories become outdated. The agent needs to know when to refresh.
- **Privacy** — agent memory may contain sensitive information. Access controls and selective forgetting are required.

## Exercises

1. Design a hybrid memory system for a Personal Operator. What goes in the vector store? What goes in the structured DB?
2. Write a prompt that instructs the agent how to decide whether to trust a memory or ask the user again.
3. Design a forgetting policy: when should the agent discard old memories?
