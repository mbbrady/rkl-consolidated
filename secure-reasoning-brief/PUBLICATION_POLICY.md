# Publication Policy - What Gets Published Where

**Purpose:** Define what content is safe to publish vs. what must remain local

---

## ✅ Safe to Publish (Website & Competition)

### Daily Briefs
**File pattern:** `*_DAILY.md`

**Contains:**
- Executive summary (Gemini-generated)
- High-priority paper highlights
- Key takeaways
- YAML frontmatter (metadata only)

**Does NOT contain:**
- Raw article content
- Full Ollama summaries
- `raw_content_excerpt` field

**Publish to:**
- ✅ RKL website (`/briefs/daily/`)
- ✅ Competition demo HTML
- ✅ GitHub (public repo)

---

### Weekly Synthesis
**File pattern:** `*_WEEKLY_BLOG.md`

**Contains:**
- Gemini-written synthesis
- IEEE-style citations (metadata only: title, link, date, source)
- Trend analysis
- Recommendations

**Does NOT contain:**
- Raw article content
- `raw_content_excerpt` field
- Full technical/lay summaries (only excerpts sent to Gemini)

**Publish to:**
- ✅ RKL website (`/briefs/weekly/`)
- ✅ Competition demo HTML
- ✅ GitHub (public repo)

---

## ❌ DO NOT Publish (Local Only)

### Raw Data Files
**File pattern:** `*_articles.json`

**Contains:**
- `raw_content_excerpt` (8000 chars of article content)
- Full technical summaries (Ollama output)
- Full lay explanations (Ollama output)
- Complete Gemini analysis

**Why local only:**
- Contains raw article content (Type III compliance)
- Demonstrates we store for auditability but don't expose
- Competition value: proves secure reasoning principles

**Store at:**
- ❌ NOT on website
- ❌ NOT in competition HTML demo
- ✅ Local filesystem only
- ✅ Competition submission package (as evidence)
- ✅ GitHub (if private repo, or gitignored if public)

---

### Technical Detail Files
**File pattern:** `*_READABLE.md`

**Contains:**
- Full article-by-article breakdown
- Complete Ollama summaries
- Detailed Gemini analysis per article
- All metadata and scores

**Why local only:**
- Too detailed for public consumption
- Contains full Ollama output (derived but verbose)
- Intended for internal review/verification

**Store at:**
- ❌ NOT on website
- ❌ NOT in competition HTML demo
- ✅ Local filesystem only
- ✅ GitHub (gitignored)

---

### Telemetry Data
**File pattern:** `data/research/**/*.parquet`

**Contains:**
- Execution context (model calls, prompts)
- Reasoning graph edges
- Governance ledger
- Artifact lineage

**Why local only:**
- Research-grade data for analysis
- May contain prompt content
- Intended for competition evaluation, not public

**Store at:**
- ❌ NOT on website
- ✅ Competition submission (as evidence)
- ✅ Local filesystem
- ✅ GitHub (private or as compressed sample)

---

## Publication Checklist

### For RKL Website
```
✅ Daily briefs (*_DAILY.md)
✅ Weekly synthesis (*_WEEKLY_BLOG.md)
❌ Raw data (*_articles.json)
❌ Technical details (*_READABLE.md)
❌ Telemetry (*.parquet)
```

### For Competition Demo (HTML)
```
✅ Daily briefs (converted to HTML)
✅ Weekly synthesis (converted to HTML)
✅ Overview/landing page
❌ Raw data files
❌ Technical detail files
❌ Telemetry (included separately in submission)
```

### For Competition Submission Package
```
✅ HTML demo (index.html, daily_briefs.html, weekly_synthesis.html)
✅ Source code (scripts, telemetry library)
✅ Documentation (README, architecture diagrams)
✅ Sample telemetry data (compressed, 5-10 MB)
✅ Sample raw data JSON (1-2 files as evidence)
❌ Full raw data archive (too large)
❌ Full telemetry archive (too large)
```

### For GitHub (Public Repo)
```
✅ Scripts and source code
✅ Documentation
✅ Sample daily briefs
✅ Sample weekly synthesis
✅ HTML demo
✅ Telemetry library code
❌ Full raw data (add to .gitignore)
❌ Full telemetry data (add to .gitignore)
⚠️  Sample data only (1-2 examples)
```

---

## Type III Compliance Verification

**Question:** How do we prove raw data never left the system?

**Answer:**
1. **Telemetry shows it:** Governance ledger documents `raw_data_exposed: false`
2. **Code shows it:** Gemini prompts don't include `raw_content_excerpt`
3. **We demonstrate storage:** Include 1-2 JSON files in submission showing we *have* the raw data locally
4. **We don't publish it:** Website/demo only show derived briefs

**Key message for judges:**
> "We store raw content locally for auditability (Type III requirement), but only derived insights are published. The competition submission includes sample raw data files to verify we have them, but the public website does not expose them."

---

## File Organization

### Current Structure
```
secure-reasoning-brief/
├── content/briefs/
│   ├── 2025-11-20_evening_DAILY.md        ✅ Publishable
│   ├── 2025-11-20_WEEKLY_BLOG.md          ✅ Publishable
│   ├── 2025-11-20_2304_articles.json      ❌ Local only
│   ├── 2025-11-20_2304_READABLE.md        ❌ Local only
│   └── ...
├── data/research/                          ❌ Local only (telemetry)
├── demo/                                   ✅ Publishable (HTML)
└── scripts/                                ✅ Publishable (source)
```

### Website Deployment (Future)
```
website/content/briefs/
├── daily/
│   ├── 2025-11-20-evening.md             ✅ Published
│   └── ...
└── weekly/
    ├── 2025-11-24.md                      ✅ Published
    └── ...
```

---

## Summary

**Publish publicly:**
- Daily briefs (Gemini summaries)
- Weekly synthesis (Gemini analysis with citations)
- HTML demo (competition)
- Source code

**Keep local:**
- Raw data JSON (with `raw_content_excerpt`)
- Technical READABLE files
- Full telemetry archives

**Include in competition (but not on website):**
- Sample raw data (1-2 files as evidence)
- Sample telemetry data (compressed)
- Proves we have the data but don't expose it

**This demonstrates Type III compliance:** We can prove we store and process raw data locally, while only publishing derived insights.

---

*Last updated: 2025-11-22*
