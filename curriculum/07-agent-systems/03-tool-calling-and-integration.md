---
id: tool-calling-and-integration
title: Tool Calling and Integration
---

# Tool Calling and Integration

Agents are useful because they can act on the world through tools. A tool is a well-defined function the agent can invoke — reading a file, sending an email, querying a database, calling an API.

## Tool design principles

- **Idempotency** — running the same tool twice should have the same effect as running it once. This lets the agent retry safely.
- **Well-defined schemas** — the LLM needs clear input and output schemas to use the tool correctly. Ambiguous parameters cause failures.
- **Error handling** — tools should return structured errors the LLM can interpret and recover from, not crash the agent.
- **Rate limiting and cost** — tools have real-world costs. The agent should respect limits and surface cost information.

## Tool registry

A tool registry is the catalog of all tools available to an agent. In the Flow system, Garden manages which tools are connected and who can use them. WorkStream may grant temporary tools based on the task.

## Security considerations

- Tools expand the agent's attack surface.
- Validate inputs before passing them to underlying systems.
- Scope tool access to the minimum needed for the task.
- Log all tool invocations for audit.

## Exercises

1. Define a tool schema for "send an email" — inputs, outputs, and error cases.
2. Identify which tools in a hypothetical Garden workspace would need human approval before execution.
3. Design a rate-limiting policy for an agent with access to a paid API. What happens when the limit is reached?
