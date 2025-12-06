# Secure Reasoning Public Blog – Design Notes

Last updated: 2025-12-06  
Owner: Resonant Knowledge Lab (Secure Reasoning Brief pipeline)

## Purpose

- Make the existing Secure Reasoning Briefs (daily and weekly) public-facing at `resonantknowledgelab.org`.
- Keep the current agentic pipeline and internal outputs intact; the blog is a new presentation layer on top.
- Serve two roles:
  - A **lay-friendly safety brief** for organizations using cloud AI on sensitive data.
  - A **resource hub / data source** for ML engineers, safety researchers, and other AI systems.

## Audiences

- **Primary**
  - Org leaders, data stewards, CISOs, and practitioners responsible for protecting sensitive data while using cloud AI.
  - Needs: plain language, clear risks/opportunities, concrete actions.

- **Secondary**
  - ML engineers, safety and alignment researchers.
  - Needs: pointers to methods, benchmarks, failure modes, and implementation signals.

- **Tertiary**
  - Policy and governance stakeholders.
  - Needs: short “policy angle” highlights, not full legal analysis.
  - Other AI systems / agents crawling the web (machine-readable, stable structure).

## Source of Truth

- Existing Secure Reasoning Brief pipeline remains as-is:
  - JSON article dumps in `content/briefs/*_articles.json`.
  - Daily Markdown:
    - `*_DAILY.md` – human-readable daily snapshots.
    - `*_READABLE.md` – per-paper summaries with technical + organizational analysis.
  - Weekly Markdown:
    - `*_WEEKLY_BLOG.md` – weekly narrative, top papers, emerging trends, references.
- The public blog consumes these files; it does **not** introduce a separate editorial pipeline.

## Content Model – Single Brief, Multiple Views

Each brief (daily or weekly) is treated as a **single canonical object** with layered content that can be presented in different “views”:

- **General view (default)**
  - Target: primary audience.
  - Language: plain, non-technical.
  - Focus: “What happened?”, “Why orgs with sensitive data should care”, “What to do / watch”.

- **ML / Technical view**
  - Target: ML engineers, safety researchers.
  - Shows General content plus additional technical details:
    - Threat models and failure modes.
    - Key methods, architectures, benchmarks.
    - Implementation guidance (e.g., monitoring, evals, mitigations).

- **Policy view (optional, later)**
  - Target: policy / governance stakeholders.
  - Short bullets per theme about regulatory or governance implications.

- **Full view**
  - All content visible (general + technical + policy + references).
  - Useful for deep readers, printing, and machine consumption.

### UX – View Selection

- Each public brief page exposes a simple toggle at the top, e.g.:

  - `View: [ General ] [ ML / Technical ] [ Full ]`

- Behavior:
  - `General`: only general-audience blocks are shown.
  - `ML / Technical`: general + ML/technical blocks are shown.
  - `Full`: all blocks are shown.
- Preference:
  - The selected view can be stored in localStorage or a cookie so that subsequent briefs open in the same mode.

### Implementation Sketch (HTML Layering)

- Content comes from a single HTML/Markdown source per brief.
- Blocks are annotated with audience classes/attributes, for example:

  - General: `<div class="view-general">…</div>`
  - ML / Technical: `<div class="view-ml">…</div>`
  - Policy: `<div class="view-policy">…</div>`

- Client-side JS/CSS:
  - Shows/hides these blocks based on the current view.
  - Updates the URL (`?view=general|ml|full`) and remembers user preference.

## Weekly Blog Template (Public-Facing)

Weekly briefs will be the primary entry point on the public blog. They are backed by `*_WEEKLY_BLOG.md` plus selected daily highlights.

### Front Matter (Example)

Intended for Hugo or similar static-site generator:

```yaml
---
title: "This Week in Secure Reasoning: [Plain-English Theme]"
date: 2025-11-30
slug: "secure-reasoning-2025-11-30"
type: "blog"
tags: ["secure reasoning", "AI safety", "data governance"]
categories: ["Weekly Brief"]
audience_primary: ["orgs", "data_stewards", "CISOs"]
audience_secondary: ["ml_engineers", "safety_researchers", "policy"]
alignment_themes: ["interpretability", "robustness", "governance"]
risk_domains: ["healthcare", "finance", "public_sector"]  # optional
source_briefs:
  - daily: "2025-11-25_morning"
  - daily: "2025-11-27_evening"
  - weekly_internal: "2025-11-23_WEEKLY_BLOG"
generated_by: "RKL Secure Reasoning Brief Agent"
agent_session_ids:
  - "brief-2025-11-23-…"
---
```

This preserves agentic provenance and makes posts easy to index (for humans and machines).

### Body Structure

1. **Title and Intro (General)**
   - `# This Week in Secure Reasoning: [Theme]`
   - 2–3 sentences:
     - Situate the week.
     - Explain why orgs using cloud AI on sensitive data should care.
     - Provide a quick “risk + opportunity” one-liner.

2. **If You Handle Sensitive Data, Start Here (General)**
   - 3–5 bullets, plain language.
   - Each bullet maps to a cluster of research, not a single paper.
   - Style: “do / watch / ask” (practical).

3. **Technical Highlights for Practitioners (ML/Technical)**
   - 4–7 items, 2–3 sentences each.
   - Each item corresponds to a “Top paper” or strongly supported cluster.
   - Structure per item:
     - Paper name + ID and very short claim.
     - Why it matters for secure reasoning (alignment, robustness, interpretability, governance).
     - Optional: tags / good starting points, e.g., `jailbreaking`, `formal_verification`.

4. **Policy Angle (Optional, Policy View)**
   - 2–4 bullets.
   - Very short statements about regulatory / governance implications.
   - Kept small so as not to dominate the narrative.

5. **Themes We’re Watching (General)**
   - Adapted from “Emerging Trends” in `*_WEEKLY_BLOG.md`.
   - 3–4 trends, each 1–2 sentences, with plain-language labels (e.g., “Fighting hallucinations”, “Explainability by design”).

6. **For Researchers & ML Engineers (ML/Technical)**
   - Short paragraph on how to use the site as a hub:
     - Links to daily briefs for the same week.
     - Pointers to tag-based navigation (interpretability, jailbreaking, formal verification, etc.).

7. **How This Brief Was Generated (General)**
   - 3–5 sentences:
     - It is an agentic system that scans AI safety / secure reasoning research, filters, and synthesizes.
     - Human oversight expectations (if any).
     - Statement about secure reasoning/data handling (e.g., Type III compliance: raw telemetry and proprietary data stay on local systems).

8. **References (Full View)**
   - Reference list carried over from `*_WEEKLY_BLOG.md`.
   - Stable IDs and links for each paper.
   - This section is especially important for researchers and other AI systems.

## Daily Briefs on the Public Site

Daily briefs can be published as a lighter-weight archive:

- URL pattern: `/briefs/2025-11-25/`.
- Content:
  - Snapshot (from `*_DAILY.md`): number of papers, number marked important, top tags.
  - “Must Read” section: titles + 1–2 sentence summaries + links.
  - Optional link into per-paper detail pages that reuse content from `*_READABLE.md`.

- Views:
  - The same `General / ML / Full` view model can apply here:
    - General: snapshot + plain-language summaries.
    - ML: adds technical details and per-paper “why it matters” sections.
    - Full: includes the more detailed per-paper sections and any quality verdicts / scores.

## Machine-Readable and Ecosystem Considerations

- **Metadata**
  - Front matter fields (as above) for every public brief.
  - Consistent tags for:
    - Alignment themes (`interpretability`, `robustness`, `governance`, `alignment`, `jailbreaking`, etc.).
    - Risk domains (e.g., `healthcare`, `finance`, `public_sector`).
    - Audience and view type.

- **Feeds / APIs**
  - Provide an RSS/Atom/JSON feed that exposes:
    - Basic article metadata.
    - Key fields like: total articles, number marked important, main themes, session IDs.
  - Optionally, a more detailed JSON endpoint that mirrors the internal brief structure for agents.

- **Structured Data**
  - Use `schema.org` types such as `Article` or `BlogPosting`.
  - Consider `about` / `keywords` fields so that AI systems can discover:
    - Which failure modes are discussed (jailbreaking, backdoors, reward hacking, hallucinations).
    - Which mitigation strategies or evaluation frameworks are covered.

## Deployment Strategy

- Domain: `resonantknowledgelab.org`.
- Initial release:
  - It is acceptable and expected to launch **only the blog** section first.
  - The rest of the nonprofit site (about, programs, methods, etc.) can be added later without changing existing blog URLs.
- Likely structure:
  - Research briefs section at `/pub-briefs/` (labelled **Research Briefs** in the main nav).
  - Daily and weekly pub-brief URLs under `/pub-briefs/daily/...` and `/pub-briefs/weekly/...`.
  - Home page spotlight block that links to the latest pub-briefs.
  - Internal navigation that lets a reader move between weekly summaries and the related daily snapshots.

### Current Implemented Website Behavior (2025-12-06)

- **Navigation**
  - Main menu includes a **Research Briefs** tab pointing to `/pub-briefs/`.

- **Home page**
  - Shows a “Latest Research Brief” spotlight:
    - Automatically selects the most recent `pub-briefs` page.
    - Displays title, date, description, and a “Read the latest brief” button.
  - Optionally shows the latest daily pub-brief in a side card if different from the latest overall brief.

- **Research Briefs section (`/pub-briefs/`)**
  - Uses a custom list template (`layouts/pub-briefs/list.html`).
  - Renders the **full content of the latest pub-brief** as the main body:
    - “Latest Research Brief” heading.
    - Title (`h1`), date, and full article content.
  - Shows the intro/body of `content/pub-briefs/_index.md` in an “About These Briefs” sidebar card.
  - Below the latest brief, a “More Research Briefs” section lists all other pub-briefs using their summary views.

## Integration with the Secure Reasoning Brief Pipeline

The Secure Reasoning Brief pipeline remains the **internal source of truth** and stays in its own project directory under `secure-reasoning-brief/`. The public blog in `website/` is a separate consumer of its outputs.

### Separation of Concerns

- `secure-reasoning-brief/`:
  - Own virtual environment, telemetry, logs, and internal data.
  - Generates internal artifacts:
    - Daily: `*_DAILY.md`, `*_READABLE.md`.
    - Weekly: `*_WEEKLY_BLOG.md`.
  - Never exposed directly to the public web.

- `website/`:
  - Hugo-based public site at `resonantknowledgelab.org`.
  - Contains only **sanitized pub-briefs** and other public content.
  - Receives pub-brief markdown files from the pipeline via an export step.

This separation preserves security (internal telemetry never leaves the governed environment) and keeps the website repo clean and focused on presentation.

### Target Format for Pub-Briefs

The pipeline should emit website-ready pub-briefs into:

- Daily pub-briefs:
  - `rkl-consolidated/website/content/pub-briefs/daily/YYYY-MM-DD-secure-reasoning-brief.md`

- Weekly pub-briefs:
  - `rkl-consolidated/website/content/pub-briefs/weekly/YYYY-MM-DD-weekly-secure-reasoning-brief.md`

Minimal required front matter:

```yaml
type: "pub-briefs"
pub_brief_kind: "daily"        # or "weekly"
source_brief: "2025-12-05_evening_DAILY"   # or e.g. "2025-11-30_WEEKLY_BLOG"
title: "Daily Secure Reasoning Pub-Brief – December 5, 2025 (Evening)"
date: 2025-12-05
description: "Short, plain-language summary of why today’s research matters."
tags: [...]
categories: [...]
```

Body structure:

- Daily:
  - Sections as in `website/content/pub-briefs/daily/2025-12-05-secure-reasoning-brief.md`:
    - “If You Use Cloud AI on Sensitive Data, Start Here”
    - “Today’s Key Research, in Plain Language”
    - “Technical Notes for ML Engineers and Safety Practitioners”
    - “How This Brief Was Generated”

- Weekly:
  - Sections as in `website/content/pub-briefs/weekly/2025-11-20-secure-reasoning-brief.md` plus the design in this document:
    - Intro / Executive Summary
    - Top papers / themes for organizations
    - Technical highlights
    - Themes / trends
    - How generated
    - References

### Export Step from Internal Briefs to Pub-Briefs

Add a small export tool under `secure-reasoning-brief/` (for example, `scripts/export_pub_brief.py`) that:

- Accepts:
  - `--kind` (`daily` or `weekly`).
  - `--source-id` (e.g. `2025-12-05_evening_DAILY`, `2025-11-30_WEEKLY_BLOG`).
  - `--website-root` (path to `website/content`).

- Locates the corresponding internal brief, such as:
  - Daily: `content/briefs/<source-id>.md` or the preferred `_DAILY.md`.
  - Weekly: `content/briefs/<source-id>.md` (`*_WEEKLY_BLOG.md`).

- Generates a website-ready pub-brief markdown file in:
  - `"$website_root/pub-briefs/daily/..."` or
  - `"$website_root/pub-briefs/weekly/..."`.

- Uses a text template (Jinja2 or similar) that:
  - Inserts the appropriate front matter.
  - Fills in body sections following the public design:
    - General layer for orgs (always present).
    - ML/technical notes section.
    - “How generated” section.

Configuration:

- The export script should read a configuration value like:

  - `RKL_WEBSITE_CONTENT_ROOT=/home/mike/project/rkl-consolidated/website/content`

  so it knows where to write the pub-brief files, without moving the pipeline itself.

### Automated Daily and Weekly Export

Integrate the exporter into the existing pipeline orchestration:

- After generating internal briefs, call the exporter, for example:

  - Daily:
    - `export_pub_brief.py --kind daily --source-id 2025-12-05_evening_DAILY --website-root ../website/content`

  - Weekly:
    - `export_pub_brief.py --kind weekly --source-id 2025-11-30_WEEKLY_BLOG --website-root ../website/content`

This creates or updates the corresponding pub-brief files in the website repo for Hugo to render.

### Future: Publishing and Verification Agents

Once the export step is stable:

- Add a **publish agent** (script or workflow) under `secure-reasoning-brief/` that:
  - Runs the exporter for the latest daily/weekly briefs.
  - Triggers a Hugo build/deploy (or signals Netlify/GitHub Actions).
  - Optionally fetches the live URLs and verifies:
    - Correct title and date.
    - Presence of key sections.
    - References rendered as expected.

- This agent becomes part of the secure reasoning pipeline while treating the website as a downstream consumer:
  - Internal reasoning and telemetry stay in `secure-reasoning-brief/`.
  - Public HTML and deployment remain in `website/` and associated infrastructure.


## Open Questions / Next Steps

- Finalize the exact HTML structure and CSS classes for view toggling.
- Align this design with the existing nonprofit site HTML templates (already drafted separately).
- Decide how much of the `_READABLE.md` per-paper detail to expose publicly and under which view.
- Design JSON/feeds so that other agents can easily ingest the same data humans see.
