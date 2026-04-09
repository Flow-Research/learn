# Scripts — Flow Education AI Content Pipeline

Automated article and lesson generation powered by DeepSeek.

---

## Setup

```bash
cd scripts
pip install -r requirements.txt
export DEEPSEEK_API_KEY=sk-your-key-here
# Optional — raises GitHub API rate limit from 60 to 5000 req/hr
export GITHUB_TOKEN=ghp_your-token-here
```

---

## Generating Articles (knowledge-base)

```bash
# Generate articles from all enabled sources (arXiv + GitHub releases)
python gen_article.py

# Preview what would be generated without writing any files
python gen_article.py --dry-run

# Limit to 3 new articles per run
python gen_article.py --limit 3

# Use a custom config file
python gen_article.py --config path/to/myconfig.yml
```

Articles are written to `knowledge-base/articles/` as `YYYY-MM-DD-slug.md`.

---

## Generating Lessons (curriculum)

```bash
# Generate a single lesson
python gen_lesson.py --topic "Zero-Knowledge Proofs" --module 02-Blockchain

# Generate multiple lessons from a file (one topic per line)
python gen_lesson.py --from-file topics.txt --module 01-Foundations

# Dry-run preview
python gen_lesson.py --topic "Transformer Architecture" --module 03-AI-ML --dry-run
```

Valid modules: `01-Foundations`, `02-Blockchain`, `03-AI-ML`, `04-Protocol-Engineering`

Lessons are written to `curriculum/<module>/` with auto-incrementing `sidebar_position`.

---

## File Structure

```
scripts/
├── core_ai_logic.py     # DeepSeek wrapper — LLM calls, prompts, data types
├── sources.py           # Discovery plugins: arXiv, GitHub releases
├── gen_article.py       # Article pipeline orchestrator
├── gen_lesson.py        # Lesson generator
├── config.yml           # Your control panel — edit sources, filters, settings
├── requirements.txt     # Python dependencies
├── authors.yml          # Copy to knowledge-base/articles/authors.yml
└── .seen_hashes.json    # Auto-created — tracks already-processed content
```

---

## Customising Sources

To add a new source, add a function to `sources.py`:

```python
def fetch_my_source(config: dict) -> list[SourceItem]:
    # ...fetch and return SourceItem objects
    return items

# Register it:
SOURCES["my_source"] = fetch_my_source
```

Then enable it in `config.yml`:

```yaml
sources:
  my_source:
    enabled: true
    my_option: value
```

---

## Workflow

```
Run script locally
      ↓
Articles appear in knowledge-base/articles/
      ↓
Review the generated .md files
      ↓
git add . && git commit -m "feat: add AI-generated articles"
      ↓
git push → GitHub Pages auto-deploys
```