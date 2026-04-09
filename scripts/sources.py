"""
sources.py
----------
Content discovery plugins.

Each source implements a single function:
    fetch(config: dict) -> list[SourceItem]

Currently supported:
  - arXiv (via public API)
  - GitHub releases (via public REST API)

Adding a new source:
  1. Create a new module-level function `fetch_<name>(config) -> list[SourceItem]`
  2. Register it in SOURCES at the bottom of this file.
"""

import hashlib
import logging
import re
import time
from datetime import datetime, timezone
from typing import Optional

import requests
import xml.etree.ElementTree as ET

from core_ai_logic import SourceItem

logger = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Shared helpers
# ---------------------------------------------------------------------------

def _get(url: str, params: dict = None, headers: dict = None, retries: int = 3) -> requests.Response:
    """HTTP GET with simple retry logic."""
    for attempt in range(retries):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=15)
            resp.raise_for_status()
            return resp
        except requests.RequestException as exc:
            logger.warning("GET %s failed (attempt %d/%d): %s", url, attempt + 1, retries, exc)
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Failed to fetch {url} after {retries} attempts")


def _today_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def _parse_date(raw: str) -> str:
    """Try to normalise various date strings to YYYY-MM-DD."""
    for fmt in ("%Y-%m-%dT%H:%M:%SZ", "%Y-%m-%dT%H:%M:%S%z", "%Y-%m-%d"):
        try:
            return datetime.strptime(raw[:19], fmt[:len(raw[:19])]).strftime("%Y-%m-%d")
        except ValueError:
            continue
    return _today_iso()


def content_hash(source_url: str) -> str:
    """Stable SHA-256 fingerprint for deduplication."""
    return hashlib.sha256(source_url.encode()).hexdigest()


# ---------------------------------------------------------------------------
# arXiv source
# ---------------------------------------------------------------------------
# arXiv Atom API: https://arxiv.org/help/api/user-manual

ARXIV_API = "https://export.arxiv.org/api/query"
ARXIV_NS  = "http://www.w3.org/2005/Atom"

_INTERESTING_CATEGORIES = {
    "cs.CR",   # Cryptography and Security
    "cs.DC",   # Distributed Computing
    "cs.LG",   # Machine Learning
    "cs.AI",   # Artificial Intelligence
    "cs.NI",   # Networking and Internet Architecture
    "eess.SP", # Signal Processing
}

def fetch_arxiv(config: dict) -> list[SourceItem]:
    """
    Fetch recent arXiv papers matching a search query.

    config keys:
      search_query  (str)  — arXiv search string, e.g. "blockchain consensus"
      max_results   (int)  — default 10
      category      (str)  — optional arXiv category filter e.g. "cs.CR"
    """
    query   = config.get("search_query", "blockchain OR zero-knowledge OR LLM")
    max_r   = int(config.get("max_results", 10))
    cat     = config.get("category", "")

    search  = f"all:{query}"
    if cat:
        search = f"cat:{cat} AND ({query})"

    logger.info("arXiv: querying '%s' (max %d)", search, max_r)

    params = {
        "search_query": search,
        "start": 0,
        "max_results": max_r,
        "sortBy": "submittedDate",
        "sortOrder": "descending",
    }

    resp  = _get(ARXIV_API, params=params)
    root  = ET.fromstring(resp.text)
    items = []

    for entry in root.findall(f"{{{ARXIV_NS}}}entry"):
        arxiv_id  = (entry.findtext(f"{{{ARXIV_NS}}}id") or "").strip()
        title     = (entry.findtext(f"{{{ARXIV_NS}}}title") or "").replace("\n", " ").strip()
        summary   = (entry.findtext(f"{{{ARXIV_NS}}}summary") or "").replace("\n", " ").strip()
        published = _parse_date(entry.findtext(f"{{{ARXIV_NS}}}published") or "")
        authors   = [
            a.findtext(f"{{{ARXIV_NS}}}name") or ""
            for a in entry.findall(f"{{{ARXIV_NS}}}author")
        ]

        if not arxiv_id or not summary:
            continue

        items.append(SourceItem(
            title=title,
            summary=summary,
            source_url=arxiv_id,
            source_type="arxiv",
            published_date=published,
            authors=authors,
        ))
        logger.debug("  arXiv: found '%s'", title[:60])

    logger.info("arXiv: %d items fetched", len(items))
    return items


# ---------------------------------------------------------------------------
# GitHub Releases source
# ---------------------------------------------------------------------------
# GitHub REST API: https://docs.github.com/en/rest/releases

GITHUB_API = "https://api.github.com"

def fetch_github_releases(config: dict) -> list[SourceItem]:
    """
    Fetch the latest releases from one or more GitHub repositories.

    config keys:
      repos        (list[str])  — e.g. ["ethereum/go-ethereum", "bitcoin/bitcoin"]
      max_per_repo (int)        — default 3
      token        (str)        — optional GitHub Personal Access Token
                                  (raises rate-limit ceiling from 60 → 5000 req/hr)
    """
    repos       = config.get("repos", [])
    max_per     = int(config.get("max_per_repo", 3))
    token       = config.get("token") or os.getenv("GITHUB_TOKEN", "")

    headers = {"Accept": "application/vnd.github+json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    items = []

    for repo in repos:
        url = f"{GITHUB_API}/repos/{repo}/releases"
        try:
            resp  = _get(url, params={"per_page": max_per}, headers=headers)
            releases = resp.json()
        except Exception as exc:
            logger.warning("GitHub: could not fetch %s — %s", repo, exc)
            continue

        for rel in releases[:max_per]:
            name    = rel.get("name") or rel.get("tag_name", "")
            body    = (rel.get("body") or "").strip()
            html_url = rel.get("html_url", "")
            pub_date = _parse_date(rel.get("published_at") or _today_iso())

            if not body:
                logger.debug("  GitHub: skipping %s (no release notes)", name)
                continue

            # Clean GitHub markdown a little — strip HTML comments
            body = re.sub(r"<!--.*?-->", "", body, flags=re.DOTALL).strip()

            items.append(SourceItem(
                title=f"{repo}: {name}",
                summary=body[:2000],   # cap to avoid very long prompts
                source_url=html_url,
                source_type="github",
                published_date=pub_date,
                authors=[],
                extra={"repo": repo, "tag": rel.get("tag_name", "")},
            ))
            logger.debug("  GitHub: found release '%s' from %s", name, repo)

    logger.info("GitHub: %d releases fetched across %d repos", len(items), len(repos))
    return items


# ---------------------------------------------------------------------------
# Source registry
# ---------------------------------------------------------------------------

import os  # needed by fetch_github_releases (placed here to satisfy import order)

SOURCES: dict[str, callable] = {
    "arxiv":            fetch_arxiv,
    "github_releases":  fetch_github_releases,
}