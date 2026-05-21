# Flow Education Initiative

Learning resource for engineers who want to contribute to building Flow's products — Personal Operators for people and enterprises.

## Repo structure

```
curriculum/       Structured lessons (foundations, blockchain, AI/ML, protocol engineering, agent systems)
knowledge-base/   Drafted articles (blog content preserved for future use)
website/          Docusaurus frontend (learn.flowresearch.tech)
scripts/          AI-assisted content generation tools
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
Our curriculum uses precise track-tier-section-lesson organization for clarity.

- `01-foundations/`
  - sections directly at root: `01-concepts`, `02-practice`, `03-tooling`
  - lessons like `01-learning-hierarchy.md`, `02-effective-notes.md`, `03-collaboration-workflows.md`

- `02-blockchain/`, `03-ai-ml/`, `04-protocol-eng/`
  - tier folders: `beginner`, `intermediate`, `advanced`
  - each tier has domain sections (e.g., blockchain advanced has `01-protocol-engineering`, `02-scalability`)
  - each section contains lesson markdown files named by topic (e.g., `01-protocol-architecture.md`)

- This structure is intended to map directly to competency progression:
  - **beginner**: concepts and fundamentals
  - **intermediate**: applied building and safety
  - **advanced**: architecture, deployment, ecosystem leadership

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

## 📜 Contribution & Policy
All lessons and research articles go through a **Human-in-the-Loop** review process. AI-generated content is staged in a Pull Request for review by the technical team. 

```bash
cd website
npm install
npm run start     # local dev server
npm run build     # production build
```

## Contributing

See [curriculum/00-intro.md](curriculum/00-intro.md) for an overview of the learning path. Pull requests welcome.
