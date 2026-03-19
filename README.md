# Flow Education Initiative: Building Africa’s Decentralized AI Talent Pipeline

Welcome to the **flow-learning**, the central nervous system for the **Flow Initiative**. This repository is a unified monorepo containing our specialized curriculum, research knowledge base, hands-on labs, and the AI-driven engine that keeps our content synchronized with the bleeding edge of Web3 and AI protocols.

## 🎯 Mission
Flow is a non-profit talent pipeline. We identify mid-level African engineers (1-3 years experience) and move them from "Learners" to "Active Contributors" in decentralized infrastructure. We focus on public goods that distribute control, computation, and value.

---

## 🏗️ Repository Architecture

```text
/flow-hub (The Unified Repo)
├── .github/                  # CI/CD, Issue Templates (Onboarding/Questions)
├── scripts/                  # THE UNIFIED AI ENGINE
│   ├── core_ai_logic.py      # LLM wrappers & Scraping utilities
│   ├── gen_lesson.py         # AI script to generate /curriculum content
│   └── gen_article.py        # AI script to generate /knowledge-base content
├── curriculum/               # THE EDUCATION LAYER (Structured Learning)
│   ├── 01-foundations/       # Cross-pillar basics (Networks, P2P, Crypto)
│   ├── 02-blockchain/        # Track 1: L1/L2 Infrastructure & Smart Contracts
│   ├── 03-ai-ml/             # Track 2: Federated Learning & Privacy-Preserving ML
│   └── 04-protocol-eng/      # Track 3: Libp2p, Storage Markets, & Consensus Research
├── knowledge-base/           # THE RESEARCH LAYER (Public Insights/Blog)
│   ├── articles/             # AI-generated + Human-reviewed technical posts
│   ├── research-papers/      # Summaries of critical ecosystem papers
│   └── ecosystem-updates/    # Scraped/Synthesized updates from partner protocols
├── labs/                     # THE WORKSHOP (Hands-on Code)
│   ├── foundation/           # Boilerplate for Phase 1 exercises
│   └── specialization/       # Complex projects (e.g., custom Flower workers)
├── website/                  # Docusaurus SSG Frontend (Docs + Blog)
└── docusaurus.config.js      # Global site & navigation configuration
```

---

## 🤖 AI Agent Instructions (System Context)

**If you are an AI Agent interacting with this repository, adhere to these constraints:**

### 1. The Three Technical Pillars
Every piece of content must align with one or more of these pillars:
*   **AI/ML:** Federated Learning (Flower, PySyft), Decentralized Training, Model Privacy.
*   **Blockchain:** Infrastructure (Ethereum, Filecoin, Bittensor), Incentive Design.
*   **Protocol Engineering:** P2P Networking (libp2p), Distributed Storage (IPFS), Compute (Akash/Gensyn).

### 2. The Learning Hierarchy
We do not use "Beginner" or "Advanced." We use professional competency levels:
1.  **Level 1: Foundations:** Concept-heavy, understanding "the what."
2.  **Level 2: Practitioner:** Implementation-heavy, "the how."
3.  **Level 3: Contributor:** OSS-focused, deep-diving into partner codebases for PR readiness.

### 3. Voice & Tone
*   **Audience:** Mid-level Software Engineers.
*   **Tone:** Engineering-first, technical, concise. Avoid marketing fluff.
*   **Context:** Use African-centric technical examples where possible (e.g., low-bandwidth optimization, local payment gateways).

### 4. Content Automation Loop
The `scripts/` directory is designed to:
1.  Scrape external protocol documentation (e.g., Protocol Labs, Flower Labs).
2.  Generate new lessons or blog articles based on documentation updates.
3.  Rewrite outdated `labs/` code snippets when a protocol updates its API.
4.  **Requirement:** All generated Markdown MUST include YAML frontmatter with `id`, `title`, `track`, `level`, and `version`.

---

## 🛠️ Tech Stack
*   **Content:** Markdown (MDX)
*   **Frontend:** Docusaurus (React-based SSG)
*   **Automation:** Python (OpenAI/Anthropic APIs, BeautifulSoup for scraping)
*   **Infrastructure:** GitHub Actions, GitHub Pages/Vercel

---

## 👥 The Team
*   **Julian Duru:** Co-Founder (Fintech scaling, Operational Lead)
*   **Florence Dairo:** Lead Product Designer (UX/UI & Design Systems)
*   **Bashir Admin:** Community Admin (Lead Software Engineer & Mentor)

---

## 📜 Contribution & Policy
All lessons and research articles go through a **Human-in-the-Loop** review process. AI-generated content is staged in a Pull Request for review by the technical team. 

**Flow Initiative is a Non-Profit. Our goal is to create sustainable income pathways for African engineers through global open-source public goods.**

***

*This README is intended for both humans and machines. Please maintain its structure when updating.*