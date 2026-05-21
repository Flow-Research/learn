---
id: planning-and-reasoning
title: Planning and Reasoning
---

# Planning and Reasoning

A capable agent does not just react — it plans. Given a high-level goal, it breaks it into steps, executes them, and adapts when things go wrong.

## Planning approaches

- **Single-shot** — the agent produces a full plan upfront and executes it. Fast but fragile.
- **Replanning** — the agent plans one step at a time, re-evaluating after each action. More robust but slower and more expensive.
- **Hierarchical** — the agent decomposes the goal into subgoals and plans each subgoal separately. Scales to complex tasks.

## Reasoning techniques

- **Chain of thought** — the agent prompts itself through intermediate reasoning steps before answering.
- **ReAct** — interleaves reasoning steps with tool actions. Think, act, observe, repeat.
- **Reflection** — after completing a task, the agent reviews its own output and corrects mistakes.

## Failure recovery

- Plans fail. The agent needs strategies: retry, escalate to a human, or decompose differently.
- Good agents surface failures clearly rather than silently producing wrong results.

## Exercises

1. Given the goal "research topic X and write a summary," write the plan an agent would produce. What subgoals? What tools at each step?
2. Simulate a failure: the agent's first research query returns no results. Write the ReAct trace for how it recovers.
3. Design a reflection prompt. After the agent finishes a task, what questions should it ask itself before presenting the result?
