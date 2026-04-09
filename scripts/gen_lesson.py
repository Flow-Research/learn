"""
gen_lesson.py
-------------
Generates structured curriculum lessons and drops them into the correct
curriculum module directory.

Lessons are Docusaurus docs (not blog posts), so they use:
  - sidebar_position for ordering
  - id for internal linking
  - No date prefix in filename

Usage:
  python gen_lesson.py --topic "Zero-Knowledge Proofs" --module 02-Blockchain
  python gen_lesson.py --topic "Transformer Architecture" --module 03-AI-ML --dry-run
  python gen_lesson.py --from-file topics.txt --module 01-Foundations

topics.txt format (one topic per line):
  What is a Blockchain
  Consensus Mechanisms
  Merkle Trees
"""

import argparse
import logging
import os
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from core_ai_logic import _get_client, _chat, _parse_json_safely, _fallback_slug

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------

SCRIPT_DIR     = Path(__file__).resolve().parent
REPO_ROOT      = SCRIPT_DIR.parent
CURRICULUM_DIR = REPO_ROOT / "curriculum"

VALID_MODULES = [
    "01-Foundations",
    "02-Blockchain",
    "03-AI-ML",
    "04-Protocol-Engineering",
]

# ---------------------------------------------------------------------------
# Logging
# ---------------------------------------------------------------------------

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s — %(message)s",
    datefmt="%H:%M:%S",
)
logger = logging.getLogger("gen_lesson")

# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

_SYSTEM_LESSON_WRITER = """
You are a senior curriculum designer for Flow Education Initiative — an African-focused
blockchain, AI, and protocol engineering learning platform targeting emerging developers.

Write educational lessons that are:
- Clear and beginner-accessible, but technically accurate.
- Structured as: Learning Objectives → Concept Explanation → Worked Example or
  Analogy → Key Takeaways → Further Reading.
- Written in plain markdown with ## subheadings.
- Practical: show real code snippets (Python or Rust) where helpful.
- Culturally inclusive: use analogies and examples relevant to African developers
  where natural (e.g. M-Pesa for payments, local infrastructure context).
- Target length: 600–900 words.
- Do NOT include YAML frontmatter.
- Do NOT include the title as H1 — that comes from frontmatter.
""".strip()

_SYSTEM_LESSON_META = """
You are a metadata extractor for a curriculum system. Given a lesson topic and module,
return ONLY valid JSON with exactly these keys:

{
  "id":               "<lowercase-hyphen-id, max 40 chars>",
  "title":            "<clear lesson title, max 70 chars>",
  "description":      "<one-sentence lesson description, max 120 chars>",
  "keywords":         ["<kw1>", "<kw2>", "<kw3>"]
}

Return ONLY the JSON — no fences, no explanation.
""".strip()


# ---------------------------------------------------------------------------
# Sidebar position helper
# ---------------------------------------------------------------------------

def _next_sidebar_position(module_dir: Path) -> int:
    """Find the highest existing sidebar_position in a module and return +1."""
    if not module_dir.exists():
        return 1
    max_pos = 0
    for md_file in module_dir.glob("*.md"):
        text = md_file.read_text(encoding="utf-8")
        m = re.search(r"sidebar_position:\s*(\d+)", text)
        if m:
            max_pos = max(max_pos, int(m.group(1)))
    return max_pos + 1


# ---------------------------------------------------------------------------
# Frontmatter builder
# ---------------------------------------------------------------------------

def _build_lesson_frontmatter(meta: dict, sidebar_pos: int) -> str:
    kw_yaml = "\n".join(f"  - {k}" for k in meta.get("keywords", []))
    return f"""---
id: {meta['id']}
title: "{meta['title']}"
description: "{meta.get('description', '')}"
sidebar_position: {sidebar_pos}
keywords:
{kw_yaml}
---
"""


# ---------------------------------------------------------------------------
# Core generation
# ---------------------------------------------------------------------------

def generate_lesson(topic: str, module: str, dry_run: bool = False) -> Path:
    """
    Generate a single lesson for a topic within a module.
    Returns the path of the written file.
    """
    module_dir = CURRICULUM_DIR / module
    sidebar_pos = _next_sidebar_position(module_dir)

    logger.info("Generating lesson: '%s' → %s (position %d)", topic, module, sidebar_pos)

    # --- 1. Metadata ---
    meta_prompt = f"Module: {module}\nTopic: {topic}"
    raw_meta    = _chat(_SYSTEM_LESSON_META, meta_prompt, temperature=0.2)
    meta        = _parse_json_safely(raw_meta)

    if not meta.get("id"):
        meta["id"]    = _fallback_slug(topic)
        meta["title"] = topic

    # --- 2. Lesson body ---
    body_prompt = (
        f"Module: {module.replace('-', ' ')}\n"
        f"Lesson title: {meta['title']}\n"
        f"Write a complete lesson on this topic."
    )
    body = _chat(_SYSTEM_LESSON_WRITER, body_prompt, temperature=0.75)

    # --- 3. Compose file ---
    frontmatter = _build_lesson_frontmatter(meta, sidebar_pos)
    content     = frontmatter + "\n" + body

    filename = f"{meta['id']}.md"
    out_path = module_dir / filename

    if dry_run:
        logger.info("[DRY-RUN] Would write: %s", out_path.relative_to(REPO_ROOT))
        lines = content.splitlines()
        print("\n" + "─" * 60)
        print("\n".join(lines[:25]))
        if len(lines) > 25:
            print(f"  ... ({len(lines) - 25} more lines)")
        print("─" * 60 + "\n")
        return out_path

    module_dir.mkdir(parents=True, exist_ok=True)

    # Avoid overwriting existing files
    if out_path.exists():
        stem = out_path.stem
        i = 1
        while out_path.exists():
            out_path = module_dir / f"{stem}-v{i}.md"
            i += 1

    out_path.write_text(content, encoding="utf-8")
    logger.info("✅ Written: %s", out_path.relative_to(REPO_ROOT))
    return out_path


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Generate curriculum lessons via DeepSeek")
    parser.add_argument("--topic",     type=str, default="",
                        help="Single topic to generate a lesson for")
    parser.add_argument("--from-file", type=Path, default=None,
                        help="Text file with one topic per line")
    parser.add_argument("--module",    type=str, required=True,
                        choices=VALID_MODULES,
                        help="Target curriculum module")
    parser.add_argument("--dry-run",   action="store_true",
                        help="Generate but do NOT write files")
    args = parser.parse_args()

    topics = []

    if args.topic:
        topics.append(args.topic.strip())

    if args.from_file:
        if not args.from_file.exists():
            logger.error("Topics file not found: %s", args.from_file)
            sys.exit(1)
        lines = args.from_file.read_text(encoding="utf-8").splitlines()
        topics.extend(line.strip() for line in lines if line.strip())

    if not topics:
        logger.error("Provide at least one topic via --topic or --from-file")
        sys.exit(1)

    for topic in topics:
        try:
            generate_lesson(topic, args.module, dry_run=args.dry_run)
        except Exception as exc:
            logger.error("Failed to generate lesson '%s': %s", topic, exc)


if __name__ == "__main__":
    main()