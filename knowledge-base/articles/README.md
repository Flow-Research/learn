# Articles (Drafted — Not Live)

This directory contains blog/article content that is **drafted and preserved** for future revival.

Per the 2026-05-20 team meeting decision:
- The Articles/Blog section was removed from the live learning site to avoid duplication with the main Flow Research site's writing surface.
- These source files are kept intact so the section can be re-enabled easily.

## How to revive

In `website/docusaurus.config.ts`:
1. Uncomment the `blog` block inside the classic preset.
2. Uncomment the navbar item linking to `/blog`.
3. Add `{label: 'Blog', to: '/blog'}` back to the footer if desired.
4. Rebuild the site.
