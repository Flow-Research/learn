# Contributing Guide

Thank you for your interest in contributing to this project! This guide will walk you through everything you need — from forking the repo to submitting your changes.

---

## Step 1: Fork the Repository

1. Go to the official repository: [https://github.com/Flow-Research/learn](https://github.com/Flow-Research/learn)
2. Click the **Fork** button in the top-right corner of the page.
3. This creates a personal copy of the repo under your own GitHub account (e.g., `https://github.com/YOUR_USERNAME/learn`).

---

## Step 2: Clone Your Fork to Your PC

Once you have forked the repo, bring it down to your local machine.

1. Open a terminal (Command Prompt, PowerShell, or Git Bash on Windows).
2. Run the following command, replacing `YOUR_USERNAME` with your GitHub username:

   ```sh
   git clone https://github.com/YOUR_USERNAME/learn.git
   ```

3. Navigate into the project folder:

   ```sh
   cd learn
   ```

4. Add the official repository as an `upstream` remote so you can stay up to date with changes:

   ```sh
   git remote add upstream https://github.com/Flow-Research/learn.git
   ```

> **Tip:** To pull in future updates from the main repo, run:
> ```sh
> git fetch upstream
> git merge upstream/main
> ```

---

## Step 3: Create a Branch

Never work directly on `main`. Create a new branch for your changes:

```sh
git checkout -b your-branch-name
```

Use a descriptive name, e.g., `add-lesson-variables` or `fix-typo-intro`.

---

## Step 4: Make Your Changes to the Curriculum

All curriculum content lives in the `curriculum/` directory. Navigate to the appropriate subfolder and make your edits or additions there. Follow the conventions below to keep lessons consistent.

### 4a. Directory Structure & Naming

The curriculum uses three organizational patterns depending on the section:

**Skill-level nested** (Blockchain, AI/ML, Protocol Engineering) — lessons organized by skill tier, then topic, then individual lesson:
```
section/
  _category_.json
  index.md
  01-beginner/
    01-subtopic/
      01-lesson.md
      02-lesson.md
      03-lesson.md
    02-subtopic/
      ...
  02-intermediate/
    ...
  03-advanced/
    ...
```

**Topic-organized** (Foundations) — lessons grouped by theme rather than skill level:
```
section/
  01-concepts/
  02-practice/
  03-tooling/
  04-specification/
```

**Flat sequential** (Rust Engineering, Agent Systems, Products) — lessons as consecutive files in the section root:
```
section/
  01-first-lesson.md
  02-second-lesson.md
  03-third-lesson.md
  ...
```

**File naming rules:**
- Prefix every file with a two-digit number for ordering: `NN-descriptive-kebab-slug.md`
- Use kebab-case for all names: `my-file-name.md`, not `myFileName.md` or `my_file_name.md`
- Place `_category_.json` in each section directory to set the sidebar label
- Place `index.md` in each section directory as a landing page with a bullet list of lessons

### 4b. Frontmatter

Every lesson file must begin with YAML frontmatter between `---` delimiters:

```yaml
---
id: kebab-case-unique-id       # Required. Must match the file slug.
title: Human Readable Title    # Required. Display title.
track: section-slug            # Include for structured tracks (blockchain, ai-ml, etc.)
level: beginner|intermediate|advanced|foundation  # Include for structured tracks
version: 1.0                   # Bump when materially rewriting a lesson
---
```

**Section index pages** (`index.md`) use different frontmatter:

```yaml
---
title: Section Title
description: A one-line description
image: /img/og/section/card.jpg
sidebar_position: 0
---
```

### 4c. Lesson Structure

Each lesson should follow this template in order:

1. **`# Title`** — H1 matching the `title` frontmatter field.

2. **`## Watch First`** (optional) — Embedded YouTube video at the top of the page using a responsive iframe:
   ```mdx
   <div style={{position: 'relative', paddingBottom: '56.25%', height: 0, overflow: 'hidden', maxWidth: '100%', marginBottom: '1.5rem'}}>
     <iframe
       src="https://www.youtube.com/embed/VIDEO_ID"
       title="Descriptive video title"
       style={{position: 'absolute', top: 0, left: 0, width: '100%', height: '100%', border: 0}}
       allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share"
       referrerPolicy="strict-origin-when-cross-origin"
       allowFullScreen
     />
   </div>
   ```

3. **`## Learning Objectives`** — A bullet list starting with "By the end of this lesson, you will be able to:" that states concrete, measurable outcomes.

4. **`## Concept Map`** (optional but encouraged) — A Mermaid diagram that visualizes the core concept:
   ```mermaid
   flowchart LR
     A["Step one"] --> B["Step two"]
     B --> C["Step three"]
   ```
   Use `flowchart`, `sequenceDiagram`, or `graph` where they genuinely clarify the lesson.

5. **`## Quantitative Lens`** (optional) — Mathematical formulas rendered via LaTeX:
   ```
   $$
   formula = here
   $$
   ```
   Define every symbol in plain language after the formula.

6. **Body content** — Standard prose with subsections. Use `###` for subsections. Keep one concept per lesson. Link to other lessons using relative markdown paths:
   ```
   See the [previous lesson](01-related-lesson.md) for background.
   ```

7. **`## Implementation Sketch`** (optional) — A brief, self-contained code block (include imports, use synthetic data):
   ```python
   import hashlib
   # short, runnable example
   ```

8. **`## Practical Exercises`** — Step-by-step tasks. Include a time estimate and a concrete deliverable.

9. **`## Self-Assessment`** — A rating scale (1–5) or reflective questions that let learners gauge their understanding.

10. **`## Key Takeaways`** — A summary bullet list of the 3–5 most important points.

11. **`## Further Reading`** — Links to official docs, papers, or trustworthy primary sources. Avoid generic or broken links.

12. **`## Next Steps`** — What to read or do next, with relative links to subsequent lessons.

13. **Footer** — A horizontal rule `---` followed by an italic closing note.

Not every lesson needs every section, but **Learning Objectives**, **Practical Exercises**, **Self-Assessment**, **Key Takeaways**, and **Further Reading** are expected in all structured lessons.

### 4d. Content Quality Guidelines

- **Be specific** — Every section should be specific to the lesson topic. Avoid generic filler.
- **Write for engineers** — Use clear, direct language. Explain trade-offs, not just concepts.
- **Code must be self-contained** — Include imports and minimal inline data. Readers should be able to copy-paste and run.
- **Diagrams must clarify** — Don't turn an entire lesson into one sprawling diagram. Keep Mermaid charts focused.
- **Use math deliberately** — Only include formulas that explain the core idea. Always define symbols afterward.
- **Cite primary sources** — Link to official documentation, original papers, or project docs. Avoid blog-spam or secondary summaries.
- **Link between lessons** — Use relative paths to connect related content: `(related-lesson.md)`

### 4e. Quick Checklist

Before moving to the next step, verify:

- [ ] File follows the `NN-descriptive-kebab-slug.md` naming convention
- [ ] Frontmatter includes `id`, `title`, and track/level/version where applicable
- [ ] Learning objectives are concrete and measurable
- [ ] Code examples are self-contained and copy-paste ready
- [ ] All links are valid and point to primary sources
- [ ] No placeholder text, broken citations (`[1][2]`), or empty sections
- [ ] Lesson links to adjacent lessons using relative paths
- [ ] `_category_.json` exists in section directory (if creating a new section)
- [ ] `index.md` updated with link to new lesson (if creating one)

---

## Step 5: Preview the Site Locally

Before submitting, verify your changes look correct by running the site on your machine.

1. Navigate to the `website/` folder:

   ```sh
   cd website
   ```

2. Install dependencies and start the development server:

   ```sh
   npm install
   npm run start
   ```

3. Open the local URL shown in your terminal in your browser to preview the site.

---

## Step 6: Commit and Push Your Changes

Once you are happy with your changes:

1. Stage and commit with a clear message:

   ```sh
   git add .
   git commit -m "Brief description of what you changed"
   ```

2. Push your branch to your forked repo:

   ```sh
   git push origin your-branch-name
   ```

---

## Step 7: Open a Pull Request

1. Go to your fork on GitHub: `https://github.com/YOUR_USERNAME/learn`
2. You should see a prompt to **Compare & pull request** — click it.
3. Set the base repository to `Flow-Research/learn` and the base branch to `main`.
4. Write a clear description of your changes.
5. Click **Create Pull Request**.

A maintainer will review your PR and may request changes before merging.

---

## General Contribution Tips

- Follow the existing folder and file structure.
- Use clear, concise language in lessons and documentation.
- Keep one logical change per pull request — this makes reviews faster.
- If you are unsure about something, open an issue or ask in the project discussions before starting.

Thank you for helping improve this project!