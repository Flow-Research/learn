"""
core_ai_logic.py
----------------
DeepSeek-powered content generation engine.
Handles all LLM interactions: article body, frontmatter metadata, and credibility scoring.
"""

import os
import json
import re
import logging
from dataclasses import dataclass
from typing import Optional
from openai import OpenAI  # DeepSeek uses an OpenAI-compatible API

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY", "")
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"

# ---------------------------------------------------------------------------
# Data structures
# ---------------------------------------------------------------------------

@dataclass
class SourceItem:
    """Normalised representation of a discovered content item."""
    title: str
    summary: str          # abstract / release notes / description
    source_url: str
    source_type: str      # "arxiv" | "github"
    published_date: str   # ISO-8601 date string  e.g. "2026-04-09"
    authors: list[str] = None   # relevant for arXiv papers
    extra: dict = None          # any additional metadata from the source


@dataclass
class GeneratedArticle:
    """Everything needed to write a Docusaurus blog markdown file."""
    slug: str
    title: str
    date: str
    tags: list[str]
    credibility_score: int      # 1–10
    source_url: str
    source_type: str
    summary_one_liner: str      # used as Docusaurus description / excerpt marker
    body_markdown: str          # full article body (no frontmatter)


# ---------------------------------------------------------------------------
# DeepSeek client
# ---------------------------------------------------------------------------

def _get_client() -> OpenAI:
    if not DEEPSEEK_API_KEY:
        raise EnvironmentError(
            "DEEPSEEK_API_KEY is not set. "
            "Export it before running: export DEEPSEEK_API_KEY=sk-..."
        )
    return OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)


def _chat(system_prompt: str, user_prompt: str, temperature: float = 0.7) -> str:
    """Single-turn chat completion. Returns the assistant message as a string."""
    client = _get_client()
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user",   "content": user_prompt},
        ],
        temperature=temperature,
        max_tokens=2048,
    )
    return response.choices[0].message.content.strip()


# ---------------------------------------------------------------------------
# Prompt templates
# ---------------------------------------------------------------------------

_SYSTEM_ARTICLE_WRITER = """
You are a senior technical writer for Flow Education Initiative — an African-focused
blockchain, AI, and protocol engineering learning platform.

Your job is to turn raw source material (arXiv abstracts, GitHub release notes, etc.)
into clear, engaging, educational markdown articles for developers and learners.

Rules:
- Write in plain, direct English. No fluff, no hype.
- Structure: brief intro → key points → implications / why it matters → conclusion.
- Use ### subheadings (not # or ##).
- Use bullet lists for technical details; prose for narrative sections.
- Include a single :::info callout box with a "TL;DR" summary.
- Do NOT include YAML frontmatter — that is handled separately.
- Do NOT include the article title as an H1 — it is added via frontmatter.
- Target length: 400–700 words.
""".strip()

_SYSTEM_METADATA_EXTRACTOR = """
You are a metadata extraction assistant. Given a source item, return ONLY a valid
JSON object with these exact keys:

{
  "slug":               "<url-friendly-slug, max 60 chars, hyphens only>",
  "title":              "<concise, engaging article title, max 80 chars>",
  "tags":               ["<tag1>", "<tag2>", "<tag3>"],
  "credibility_score":  <integer 1-10>,
  "summary_one_liner":  "<one sentence, max 160 chars>"
}

Tag guidelines:
- Use lowercase, hyphen-separated values.
- Choose from: blockchain, ethereum, bitcoin, solana, ai-ml, deep-learning,
  llm, protocol-engineering, cryptography, defi, layer2, zero-knowledge,
  consensus, networking, rust, python, security, research, tooling, africa.
- Pick 2–4 most relevant tags.

Credibility score rubric:
  9-10 → peer-reviewed paper, official protocol spec, core dev team release
  7-8  → reputable project release notes, well-known research lab
  5-6  → community post, blog from known developer
  3-4  → unverified / speculative content
  1-2  → low-signal noise

Return ONLY the JSON — no markdown fences, no explanation.
""".strip()


# ---------------------------------------------------------------------------
# Public API
# ---------------------------------------------------------------------------

def generate_article(item: SourceItem) -> GeneratedArticle:
    """
    Main entry point: takes a SourceItem, returns a fully populated GeneratedArticle.
    Makes two LLM calls:
      1. Extract structured metadata (slug, title, tags, score, one-liner)
      2. Write the article body
    """
    logger.info("Generating article for: %s", item.source_url)

    # --- 1. Extract metadata ---
    metadata_prompt = (
        f"Source type: {item.source_type}\n"
        f"Title hint: {item.title}\n"
        f"Summary: {item.summary}\n"
        f"URL: {item.source_url}\n"
        f"Date: {item.published_date}\n"
    )
    if item.authors:
        metadata_prompt += f"Authors: {', '.join(item.authors)}\n"

    raw_metadata = _chat(_SYSTEM_METADATA_EXTRACTOR, metadata_prompt, temperature=0.2)
    metadata = _parse_json_safely(raw_metadata)

    # --- 2. Write article body ---
    body_prompt = (
        f"Source type: {item.source_type}\n"
        f"Title: {metadata.get('title', item.title)}\n"
        f"Source URL: {item.source_url}\n"
        f"Date: {item.published_date}\n"
        f"Content to expand on:\n\n{item.summary}\n"
    )
    if item.authors:
        body_prompt += f"\nOriginal authors: {', '.join(item.authors)}"

    body_markdown = _chat(_SYSTEM_ARTICLE_WRITER, body_prompt, temperature=0.75)

    return GeneratedArticle(
        slug=metadata.get("slug", _fallback_slug(item.title)),
        title=metadata.get("title", item.title),
        date=item.published_date,
        tags=metadata.get("tags", ["research"]),
        credibility_score=int(metadata.get("credibility_score", 5)),
        source_url=item.source_url,
        source_type=item.source_type,
        summary_one_liner=metadata.get("summary_one_liner", ""),
        body_markdown=body_markdown,
    )


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _parse_json_safely(raw: str) -> dict:
    """Parse JSON from LLM output, stripping markdown fences if present."""
    cleaned = re.sub(r"^```(?:json)?\s*", "", raw.strip())
    cleaned = re.sub(r"\s*```$", "", cleaned)
    try:
        return json.loads(cleaned)
    except json.JSONDecodeError as exc:
        logger.error("Failed to parse metadata JSON: %s\nRaw output:\n%s", exc, raw)
        return {}


def _fallback_slug(title: str) -> str:
    """Generate a basic slug from a title as a last resort."""
    slug = title.lower()
    slug = re.sub(r"[^a-z0-9\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug.strip())
    return slug[:60]