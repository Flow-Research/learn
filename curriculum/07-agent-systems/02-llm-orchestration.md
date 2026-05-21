---
id: llm-orchestration
title: LLM Orchestration
---

# LLM Orchestration

LLMs are the reasoning engine for most modern agent systems. Orchestration is how you structure calls to the LLM — what context you give it, how you parse its output, and how you handle failures.

## Patterns

- **Single prompt** — one call, one response. Simple but limited.
- **Chain** — output of one call feeds into the next. Useful for multi-step reasoning.
- **Router** — the LLM decides which path to take based on input classification.
- **Tool loop** — the LLM requests a tool call, the system executes it and returns the result, and the LLM decides the next action.

## Prompt structure

- **System prompt** — fixed instructions that define the agent's role, constraints, and output format.
- **Context** — dynamic information about the current task, user, and environment.
- **History** — previous turns so the agent can maintain coherence.
- **Tool definitions** — descriptions of available tools so the LLM can choose correctly.

## Common failure modes

- Hallucination — the LLM invents facts or tool outputs.
- Loop — the LLM repeats the same action without progress.
- Refusal — the LLM declines to act due to perceived safety constraints.
- Format errors — the LLM outputs malformed JSON or incorrect tool call syntax.

## Exercises

1. Write a system prompt for a Personal Operator that has access to email and a calendar. What constraints do you include?
2. Design a tool loop: define three tools, write the prompt that tells the LLM how to use them, and trace one interaction cycle.
3. Given a failed tool call (API timeout), write the error message you would return to the LLM so it can recover gracefully.
