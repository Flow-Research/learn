---
id: version-control
title: Version Control for Engineers
track: foundations
level: beginner
version: 1.1
---

# Version Control for Engineers

## Watch First

<div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
 <iframe
 src="https://www.youtube.com/embed/USjZcfj8yxE"
 title="Learn Git In 15 Minutes"
 style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
 allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
 referrerPolicy="strict-origin-when-cross-origin"
 allowFullScreen
 />
</div>

## Learning Objectives

By the end of this lesson, you will be able to:

- Explain why version control matters in real engineering work.
- Use Git to track changes, review history, and recover from mistakes.
- Collaborate safely with others using branches and pull requests.
- Apply version-control practices to your Flow Initiative curriculum and labs.

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

Version control is the backbone of collaborative engineering. Without it:

- It is difficult to see what changed and why.
- Multiple people cannot work on the same code safely.
- Recovering from a bad change or experiment becomes risky.

In the Flow Initiative, every lesson, lab, and contribution lives in a version-controlled repository. Git is the tool that lets you:

- Commit your work,
- Review changes,
- Branch and experiment, and
- Merge improvements back into the shared codebase.

For engineering, good version-control habits are especially important when working asynchronously and across time zones.

## What Is Version Control?

Version control is a system that:

- Tracks every change to a project.
- Lets you see who changed what and when.
- Lets you revert or branch from a known state.

Git is the most widely used version-control system. It is distributed, which means every contributor has a full copy of the history.

## Why Engineers Need Version Control

Without version control, you rely on:

- Copying folders with names like `project_v2_backup_final`.
- Manually comparing text files.
- Losing work when mistakes happen.

With Git:

- Every change is recorded.
- You can experiment safely in branches.
- You can review changes before they are merged.
- You can roll back to a known-good state.

This is essential for:

- Open-source collaboration,
- Labs that evolve over time,
- Curriculum content that the whole team maintains.

## Core Concepts

### 1. Repository

A **repository** (or "repo") is a project's version-controlled space. It contains:

- Code,
- Markdown/lesson files,
- Configuration, and
- The history of changes.

The Flow Initiative monorepo is a Git repository.

### 2. Commit

A **commit** is a snapshot of changes at a point in time. Every commit has:

- A message explaining the change.
- A list of modified files.
- A timestamp and author.

Good commits are small and focused on one logical change.

### 3. Branch

A **branch** is a line of development. It lets you:

- Work on a new feature without breaking the main version.
- Experiment safely.
- Submit changes for review without affecting everyone immediately.

In Flow, you will often work on a branch before opening a pull request.

### 4. Pull Request (PR)

A **pull request** is a proposal to merge changes from one branch into another. It is the primary place for:

- Code review,
- Discussion, and
- Documentation of changes.

In the Flow program, every curriculum update, lab, or contribution should be reviewed via a PR.

### 5. Conflict and Merge

A **conflict** happens when two people change the same part of a file differently. Resolving a conflict means deciding which version to keep or how to combine them.

A **merge** combines the changes from one branch into another after conflicts are resolved.

## Using Git in Practice

For Flow trainees, Git is used to:

- Contribute lessons to `curriculum/`.
- Submit lab implementations to `labs/`.
- Propose new articles or fixes to `knowledge-base/`.
- Track documentation changes in `website/`.

Here are the basic patterns you will use.

### 1. Initialize and Clone

To start:

```bash
git clone https://github.com/flow-education/flow-hub.git
```

This copies the entire repo to your local machine.

### 2. Branch for a Task

Create a branch for the work you plan to do:

```bash
git checkout -b feature/new-lesson
```

Name your branch meaningfully, e.g., `fix/lesson-typo`, `feat/blockchain-lab-01`, `docs/reading-comprehension-exercise`.

### 3. Make and Commit Changes

Edit your files (e.g., Markdown lessons, lab code), then:

```bash
git add.
git commit -m "Describe what you changed"
```

A good commit message:

- Starts with a verb in the imperative (e.g., `Add`, `Fix`, `Update`).
- Explains the change in one line.
- Describes why it matters if needed.

### 4. Push and Open a Pull Request

Push your branch:

```bash
git push origin feature/new-lesson
```

On GitHub, open a pull request from that branch to `main` (or `master`, depending on convention). In the PR, describe:

- What this change does.
- Why it is needed.
- How it was tested.

### 5. Review and Merge

Team members will review your changes, suggest edits, and approve the PR. Once approved, it is merged:

```bash
git checkout main
git pull
```

Your local repo now reflects the updated state.

## Version Control and Safe Experimentation

Git encourages experimentation:

- Create a branch to try a new idea.
- Break things, then decide whether to keep or discard the changes.
- If the experiment fails, you can always return to a stable state.

In Flow, this is crucial for:

- Trying aggressive optimizations.
- Testing new learning patterns.
- Exploring new protocol or AI techniques.

## Common Pitfalls and How to Avoid Them

### Mistake 1: Large, Unfocused Commits

Committing "everything" at once makes it hard to review and revert.

**Solution:**
Make small, focused commits. One logical change per commit.

### Mistake 2: Ignoring the Commit Message

A vague message like "fix stuff" does not help anyone.

**Solution:**
Write clear, descriptive messages that explain what changed and why.

### Mistake 3: Forgetting to Pull Changes

If you do not pull the latest changes, you may create conflicts.

**Solution:**
Always pull the latest changes before starting new work.

### Mistake 4: Not Using Branches

Working directly on `main` is risky because mistakes affect everyone.

**Solution:**
Use feature branches for every new change.

## Version Control and Flow Initiative Workflow

In Flow, the version-control workflow supports:

- Human-in-the-loop review of AI-generated content.
- Iterative refinement of lessons and labs.
- Public-goods documentation that is transparent and auditable.

Every trainee should:

- Learn basic Git commands.
- Open PRs for their contributions.
- Respond to feedback on those PRs.
- Take ownership of the code and documentation they submit.

## Implementation Sketch

```yaml
lesson: version-control
artifact: short written note or working demo
evidence:
 - explain the idea in your own words
 - apply it in a small task
 - record feedback and next action
```

## Practical Exercises

### Exercise 1: Create a Feature Branch

Pick a small change you can make (e.g., add a note to a lab or fix a typo):

- Create a new branch.
- Edit a file.
- Commit and push the branch.
- Open a pull request on GitHub.

Practice this until it feels natural.

### Exercise 2: Review a Pull Request

Find a pull request in the Flow repo (or simulate one with a teammate):

- Read the diff.
- Ask clarifying questions.
- Suggest improvements or mark it as approved.

### Exercise 3: Reset and Re-do

Make a small intentional mistake in a local branch (e.g., delete a line you did not mean to):

- Practice restoring it from Git history.
- Commit the fix with a clear message.

This helps you get comfortable with recovery.

## Self-Assessment

Rate yourself from 1 to 5:

- I understand why version control matters.
- I can create and switch Git branches.
- I can make clear, small commits.
- I can open and review a pull request.

Action item: complete at least one end-to-end Git workflow (branch -> commit -> push -> PR -> review) in the Flow repo.

## Further Reading

- [Bloom taxonomy](https://cft.vanderbilt.edu/guides-sub-pages/blooms-taxonomy/)
- [Markdown syntax](https://www.markdownguide.org/basic-syntax/)
- [Git documentation](https://git-scm.com/doc)
- [GitHub flow](https://docs.github.com/en/get-started/using-github/github-flow)

## Next Steps

- Read `03-collaboration-workflows.md` next to see how version control integrates with communication and collaboration.
- Treat every change in the Flow monorepo as a practice opportunity with Git.
- View your Git history as a record of your engineering growth.

---

*This lesson teaches Flow Initiative trainees to use Git and version control as core engineering practices that support collaboration, experimentation, and safe iteration across the monorepo and beyond.*
