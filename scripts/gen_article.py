"""
gen_article.py
--------------
Orchestrates the full article generation pipeline:

  1. Load config (config.yml or inline defaults)
  2. Discover content via enabled sources (arXiv, GitHub releases)
  3. Deduplicate against already-published articles
  4. Generate article markdown via DeepSeek (core_ai_logic.py)
  5. Write .md files to knowledge-base/articles/

Usage:
  python gen_article.py                     # uses config.yml in same directory
  python gen_article.py --config myconf.yml
  python gen_article.py --dry-run           # discover & generate but do NOT write files
  python gen_article.py --limit 3           # cap how many articles to generate
"""

import argparse
import hashlib
import json
import logging
import os
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

# ---------------------------------------------------------------------------
# Path setup — allow running from any working directory
# ---------------------------------------------------------------------------

SCRIPT_DIR   = Path(__file__).resolve().parent
REPO_ROOT    = SCRIPT_DIR.parent
ARTICLES_DIR = REPO_ROOT / "knowledge-base" / "articles"
HASHES_FILE  = SCRIPT_DIR / ".seen_hashes.json"   # persists dedup state

sys.path.insert(0, str(SCRIPT_DIR))

from core_ai_logic import SourceItem, GeneratedArticle, generate_article
from sources import SOURCES, content_hash

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("gen_article")

# ---------------------------------------------------------------------------
# Default configuration (overridden by config.yml)
# ---------------------------------------------------------------------------

DEFAULT_CONFIG = {
    "sources": {
        "arxiv": {
            "enabled": True,
            "search_query": "blockchain OR zero-knowledge proofs OR large language model",
            "max_results": 5,
        },
        "github_releases": {
            "enabled": True,
            "repos": [
                "ethereum/go-ethereum",
                "bitcoin/bitcoin",
                "solana-labs/solana",
                "rust-lang/rust",
            ],
            "max_per_repo": 2,
        },
    },
    "output": {
        "articles_dir": str(ARTICLES_DIR),
        "default_author": "flow_ai",
    },
    "filters": {
        "min_credibility_score": 5,
    },
}

# ---------------------------------------------------------------------------
# Config loader
# ---------------------------------------------------------------------------

def load_config(path: Path) -> dict:
    if path.exists():
        logger.info("Loading config from %s", path)
        with open(path) as f:
            user_cfg = yaml.safe_load(f) or {}
        return _deep_merge(DEFAULT_CONFIG, user_cfg)
    logger.info("No config.yml found — using defaults")
    return DEFAULT_CONFIG


def _deep_merge(base: dict, override: dict) -> dict:
    result = base.copy()
    for k, v in override.items():
        if k in result and isinstance(result[k], dict) and isinstance(v, dict):
            result[k] = _deep_merge(result[k], v)
        else:
            result[k] = v
    return result


# ---------------------------------------------------------------------------
# Deduplication
# ---------------------------------------------------------------------------

def load_seen_hashes() -> set:
    if HASHES_FILE.exists():
        with open(HASHES_FILE) as f:
            data = json.load(f)
        return set(data.get("hashes", []))
    return set()


def save_seen_hashes(hashes: set) -> None:
    with open(HASHES_FILE, "w") as f:
        json.dump({"hashes": sorted(hashes)}, f, indent=2)


def is_duplicate(item: SourceItem, seen: set) -> bool:
    h = content_hash(item.source_url)
    return h in seen


def mark_seen(item: SourceItem, seen: set) -> None:
    seen.add(content_hash(item.source_url))


# ---------------------------------------------------------------------------
# Markdown file writer
# ---------------------------------------------------------------------------

def build_frontmatter(article: GeneratedArticle, author: str) -> str:
    tags_yaml = "\n".join(f"  - {t}" for t in article.tags)
    return f"""---
slug: {article.slug}
title: "{_escape_yaml(article.title)}"
authors: [{author}]
tags:
{tags_yaml}
date: {article.date}
source_url: "{article.source_url}"
source_type: {article.source_type}
credibility_score: {article.credibility_score}
description: "{_escape_yaml(article.summary_one_liner)}"
---
"""


def _escape_yaml(s: str) -> str:
    return s.replace('"', '\\"').replace("\n", " ")


def write_article(article: GeneratedArticle, articles_dir: Path, author: str, dry_run: bool = False) -> Path:
    filename  = f"{article.date}-{article.slug}.md"
    out_path  = articles_dir / filename
    frontmatter = build_frontmatter(article, author)
    excerpt_marker = "\n\n<!-- truncate -->\n\n"
    content   = frontmatter + "\n" + article.summary_one_liner + excerpt_marker + article.body_markdown

    if dry_run:
        logger.info("[DRY-RUN] Would write: %s", out_path)
        _print_preview(content)
        return out_path

    articles_dir.mkdir(parents=True, exist_ok=True)

    if out_path.exists():
        # Avoid clobbering — append a counter suffix
        stem   = out_path.stem
        suffix = out_path.suffix
        i      = 1
        while out_path.exists():
            out_path = articles_dir / f"{stem}-{i}{suffix}"
            i += 1

    out_path.write_text(content, encoding="utf-8")
    logger.info("✅ Written: %s", out_path.relative_to(REPO_ROOT))
    return out_path


def _print_preview(content: str) -> None:
    lines = content.splitlines()
    preview = "\n".join(lines[:30])
    print("\n" + "─" * 60)
    print(preview)
    if len(lines) > 30:
        print(f"  ... ({len(lines) - 30} more lines)")
    print("─" * 60 + "\n")


# ---------------------------------------------------------------------------
# Main pipeline
# ---------------------------------------------------------------------------

def run(config: dict, dry_run: bool = False, limit: int = 0) -> None:
    articles_dir = Path(config["output"]["articles_dir"])
    author       = config["output"]["default_author"]
    min_score    = config["filters"]["min_credibility_score"]

    seen = load_seen_hashes()

    # --- 1. Discovery ---
    all_items: list[SourceItem] = []

    for source_name, source_cfg in config["sources"].items():
        if not source_cfg.get("enabled", True):
            logger.info("Source '%s' is disabled — skipping", source_name)
            continue
        if source_name not in SOURCES:
            logger.warning("Unknown source '%s' — skipping", source_name)
            continue

        logger.info("Fetching from source: %s", source_name)
        fetched = SOURCES[source_name](source_cfg)
        all_items.extend(fetched)

    logger.info("Total items discovered: %d", len(all_items))

    # --- 2. Deduplication ---
    new_items = [i for i in all_items if not is_duplicate(i, seen)]
    logger.info("New items (after dedup): %d", len(new_items))

    if not new_items:
        logger.info("Nothing new to generate. Done.")
        return

    if limit:
        new_items = new_items[:limit]
        logger.info("Limiting to %d items", limit)

    # --- 3. Generate & write ---
    written = 0
    skipped = 0

    for item in new_items:
        logger.info("─── Generating: %s", item.title[:70])
        try:
            article = generate_article(item)
        except Exception as exc:
            logger.error("Failed to generate article for '%s': %s", item.title[:50], exc)
            skipped += 1
            continue

        if article.credibility_score < min_score:
            logger.info(
                "⚠️  Skipping '%s' — credibility score %d < min %d",
                article.title[:50], article.credibility_score, min_score
            )
            mark_seen(item, seen)   # still mark as seen so we don't retry
            skipped += 1
            continue

        write_article(article, articles_dir, author, dry_run=dry_run)
        mark_seen(item, seen)
        written += 1

    # --- 4. Persist hashes ---
    if not dry_run:
        save_seen_hashes(seen)

    logger.info("═══ Summary: %d written, %d skipped ═══", written, skipped)


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate knowledge-base articles via DeepSeek")
    parser.add_argument("--config",  type=Path, default=SCRIPT_DIR / "config.yml",
                        help="Path to config YAML (default: scripts/config.yml)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Discover and generate but do NOT write files")
    parser.add_argument("--limit",   type=int, default=0,
                        help="Max number of articles to generate (0 = unlimited)")
    args = parser.parse_args()

    config = load_config(args.config)
    run(config, dry_run=args.dry_run, limit=args.limit)


if __name__ == "__main__":
    main()