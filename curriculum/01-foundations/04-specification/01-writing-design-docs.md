---
id: writing-design-docs
title: Writing Design Docs and Specifications
---

# Writing Design Docs and Specifications

Every product change at Flow starts with a clear design document. Writing one forces clarity before code and leaves a record others can review, challenge, and build on.

## Why design docs matter

- They surface assumptions before implementation.
- They give reviewers something to critique early, when changes are cheap.
- They serve as documentation for why a system works the way it does.

## What a good design doc includes

- **Context** — what problem are we solving and why now?
- **Goals and non-goals** — what is in scope and what is explicitly out.
- **Design** — the proposed approach, including diagrams where useful.
- **Tradeoffs** — what alternatives were considered and why this one was chosen.
- **Open questions** — what is not yet decided.

## Other forms

- **ADRs** (Architecture Decision Records) — lightweight records of individual decisions. One decision per ADR, structured as context → decision → consequences.
- **API specs** — contract definitions before implementation. Can be OpenAPI, protobuf, or plain markdown depending on the project.
- **Research notes** — exploratory writing with no decision required. Used in the research track to capture what was learned and what remains unknown.

## Exercises

1. Take a system you know well and write a one-page design doc for a small change to it.
2. Write an ADR for a decision you made in a recent project.
3. Review another contributor's design doc and leave structured feedback.
