---
id: safety-and-guardrails
title: Safety and Guardrails
---

# Safety and Guardrails

An agent with tools and autonomy can cause real harm — deleted data, unintended purchases, leaked information. Safety systems constrain what the agent can do and catch problems before they propagate.

## Safety layers

- **Input guardrails** — filter harmful or out-of-scope instructions before they reach the agent.
- **Output guardrails** — validate the agent's proposed actions before execution.
- **Escalation policies** — define when the agent must ask a human before proceeding.
- **Kill switches** — mechanisms to stop an agent that is behaving unexpectedly.
- **Audit logging** — record every decision and action for post-hoc review.

## Common safety issues

- **Prompt injection** — a user or external input tricks the agent into ignoring its instructions.
- **Tool abuse** — the agent uses a tool in an unintended way (e.g., deleting files when asked to read them).
- **Runaway costs** — the agent enters a loop that generates expensive API calls.
- **Data leakage** — the agent includes sensitive context in a tool call that exposes it to third parties.

## Flow context

Harnessy is Flow's reliability layer — it tests agent behavior, evaluates output, and closes feedback loops so agents can be trusted with real work. Safety guardrails are a prerequisite for that trust. Without them, evaluation is reactive rather than preventive.

## Exercises

1. Design an output guardrail for an agent with tool-calling ability. What would you check before allowing a "delete file" action?
2. Write an escalation policy: which actions should the agent take without asking, which require approval, and which are forbidden entirely?
3. Identify three prompt injection scenarios specific to a Personal Operator with access to email.
