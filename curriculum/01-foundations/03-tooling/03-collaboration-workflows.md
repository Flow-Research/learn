---
id: collaboration-workflows
title: Collaboration Workflows
track: foundations
level: beginner
version: 1.1
---

# Collaboration Workflows

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/a5IaAZbWmzg"
 title="Work with the GitHub Workflow"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Use GitHub issues and pull requests as part of your engineering workflow.
- Propose and iterate on ideas through RFC-style discussions.
- Communicate effectively in technical channels (GitHub, chat, meetings).
- Treat collaboration as a systems-thinking practice, not just a social activity.

## Concept Map

```mermaid
flowchart LR
 A["Source"] --> B["Question"]
 B --> C["Practice"]
 C --> D["Artifact"]
 D --> E["Review"]
 E --> B
```

## Quantitative Lens

A learning loop is strongest when practice and feedback both happen:

$$
M = U \times P \times F
$$

$M$ is mastery, $U$ is understanding, $P$ is deliberate practice, and $F$ is feedback quality.

## Introduction

Coding is a solo activity only when you are prototyping. Real engineering happens in teams, in public repos, and in shared spaces where decisions are discussed, reviewed, and documented.

In the Flow Initiative, collaboration is **baked into the infrastructure**:

- GitHub issues for planning and tracking.
- Pull requests for code and content.
- Docusaurus for shared knowledge.
- Community channels for async discussion.

This lesson teaches you how to move from "working alone" to "working with intent" in a distributed, open-source-style environment.

## Why Collaboration Is an Engineering Skill

Collaboration is not just about being nice. It is about:

- Avoiding duplication of work.
- Making decisions visible and reversible.
- Surfacing hidden assumptions early.
- Building shared mental models across the team.

For engineering, good collaboration workflows matter especially when:

- Team members are in different time zones,
- Sync time is limited,
- And clarity of intent is critical for remote work.

## Collaboration Inside the Flow Monorepo

The `flow-hub` repo is your primary collaboration surface. It holds:

- **`curriculum/`** - joint learning design.
- **`labs/`** - shared experiments and exercises.
- **`knowledge-base/`** - public insights and analysis.
- **`website/`** - the Docusaurus frontend that surfaces the content.

Every change should be visible, traceable, and discussable.

## Core Collaboration Tools

### 1. GitHub Issues

Issues are used for:

- Proposing new features or lessons.
- Reporting bugs or unclear content.
- Planning release or milestone work.

A good issue:

- Has a clear title.
- States the problem, not just the symptom.
- Includes context (e.g., error messages, environment, constraints).
- Ends with a concrete proposal or question.

Example issue structure:

```md
## What I want to change

## What problem it solves

## Current behavior

## Proposed behavior

## Questions for the team
```

### 2. Pull Requests (PRs)

PRs are the place where changes are reviewed and integrated.

Every PR should:

- Explain **what** changed and **why**.
- Reference the issue or discussion that motivated it.
- Include a small, focused change set.
- Invite feedback with specific questions.

Reviewers should:

- Check for correctness.
- Consider clarity and maintainability.
- Think about edge cases and constraints.
- Comment constructively.

### 3. RFC-Style Proposals

For larger ideas (e.g., a new track, a new lab series, or a major restructuring), use an RFC-style document.

An RFC is:

- A short Markdown-style design note.
- Posted in a relevant directory or issue.
- Open for discussion and iteration.

It usually answers:

- What problem are we solving?
- What are the alternative solutions?
- What are the trade-offs?
- What is the next step?

RFCs help the team align on direction before heavy implementation.

## Communication Channels

Flow uses multiple channels:

- GitHub issues and PRs for **asynchronous, written** collaboration.
- Chat or community channels for **quick questions and sync**.
- Docusaurus or wiki-style pages for **persistent knowledge**.

To keep collaboration efficient:

- Put **decisions and important context** in GitHub or Docusaurus.
- Use chat for "how do I run this?" style questions.
- Use meetups or cohort calls for big-picture reflection.

## Effective Collaboration Habits

### 1. Write Directly, Not Vaguely

Good communication is clear and specific:

- Not: "Something is wrong."
- Instead: "X returns Y when I expect Z under condition A. Here is a minimal example."

### 2. Summarize and Link

When you answer a question or resolve an issue:

- Write a short summary of what happened.
- Link to the relevant code, PR, or lesson.

This creates a **searchable trail** for future learners.

### 3. Use Templates Wisely

GitHub issue and PR templates help you structure your thinking:

- Use them as checklists.
- Do not skip sections just because they are optional.
- Add context that matters to your environment (e.g., bandwidth, local infrastructure).

### 4. Give and Receive Feedback

Feedback is part of the collaboration loop.

When giving feedback:

- Be specific.
- Focus on the work, not the person.
- Suggest alternatives when possible.

When receiving feedback:

- Assume positive intent.
- Ask clarifying questions.
- Choose what to adopt and what to challenge.

### 5. Own Your Communication

If you open an issue or PR, you are responsible for:

- Responding to questions.
- Clarifying your intent.
- Iterating on the change until it is accepted or closed.

This is the "owner-style" mindset, not the "submit-and-forget" style.

## Collaboration in the Flow Initiative

Inside Flow, collaboration workflows are used to:

- **Design curriculum** - issues and PRs for lessons and exercises.
- **Run labs** - shared instructions, feedback, and iterations.
- **Maintain knowledge** - articles, RFCs, and ecosystem updates.
- **Onboard new trainees** - through guided issues and starter tasks.

As a trainee, you are not just consuming this system. You are also **part of it**, even at the beginner level.

## Implementation Sketch

```yaml
lesson: collaboration-workflows
artifact: short written note or working demo
evidence:
 - explain the idea in your own words
 - apply it in a small task
 - record feedback and next action
```

## Practical Exercises

### Exercise 1: Open an Issue

Pick one small improvement you can suggest:

- A typo fix.
- A missing example.
- A missing explanation.

Open a GitHub issue in the Flow repo and fill it in fully:

- Title.
- Problem.
- Suggested fix.
- Question for the team.

### Exercise 2: Submit a PR

Take a small issue (yours or someone else's) and:

- Fork or clone the repo.
- Make the change.
- Commit and push.
- Open a pull request that references the issue.

Practice explaining your change in the PR description.

### Exercise 3: Review a Peer's PR

Find a PR from another trainee (or simulate a pair-review):

- Read the code and notes.
- Ask at least two clarifying questions.
- Highlight one thing that is clear and one improvement.

This will help you practice giving constructive feedback.

## Self-Assessment

Rate yourself from 1 to 5:

- I can write a clear GitHub issue.
- I can open and describe a pull request.
- I can give and receive feedback constructively.
- I can treat collaboration as part of the engineering process.

Action item: complete at least one closed-loop collaboration cycle (issue -> PR -> review -> merge or close) in the Flow repo.

## Further Reading

- [Bloom taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
- [Markdown syntax](https://www.markdownguide.org/basic-syntax/)
- [Git documentation](https://git-scm.com/doc)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)

## Next Steps

- Use collaboration workflows in every track you join (blockchain, AI/ML, protocol engineering).
- Treat every issue and PR as a reflection of your engineer mindset.
- Keep your communication clear, documented, and aligned with the Flow mission.

---

*This lesson teaches Flow Initiative trainees how to collaborate effectively across GitHub, chat, and Docusaurus, treating collaboration as an engineering-grade workflow, not just a social layer around the code.*
