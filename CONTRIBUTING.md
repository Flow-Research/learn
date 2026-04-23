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

All curriculum content lives in the `curriculum/` directory. Navigate to the appropriate subfolder and make your edits or additions there.

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