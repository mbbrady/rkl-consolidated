# Automated Blog System - Schedule and Architecture

## Overview

The system runs **automated data collection 2x daily** and **weekly blog synthesis** every Monday.

---

## Schedule

### Daily Operations (2x/day)

**Morning Run: 9:00 AM**
```
Cron: 0 9 * * *
Script: cron_pipeline_wrapper.sh → fetch_and_summarize.py
```

**Evening Run: 9:00 PM**
```
Cron: 0 21 * * *
Script: cron_pipeline_wrapper.sh → fetch_and_summarize.py
```

**What happens:**
1. Scrape RSS feeds (ArXiv, AI Alignment Forum, Google AI Blog)
2. Ollama generates technical summaries and lay explanations
3. Gemini analyzes each article for secure reasoning relevance
4. Save 3 files:
   - `YYYY-MM-DD_HHMM_articles.json` - Machine-readable with Gemini analysis
   - `YYYY-MM-DD_HHMM_READABLE.md` - Human-readable structured format
   - Research telemetry data (Parquet files)

**Output:** 2 briefs/day × 20 articles/brief = ~40 articles/day with expert analysis

---

### Weekly Blog Synthesis (Monday 10:00 AM)

**Cron: 0 10 * * 1**
```
Script: cron_weekly_blog_wrapper.sh → generate_weekly_blog.py
```

**What happens:**
1. Load all briefs from past 7 days (14 files = 2 runs/day × 7 days)
2. Extract all articles with Gemini analysis (~280 articles/week)
3. Ask Gemini to synthesize:
   - Top papers of the week (3-5 featured)
   - Emerging trends across papers
   - Notable mentions
   - What's missing (research gaps)
   - Weekly recommendations for practitioners
   - Looking ahead
4. Save as `YYYY-MM-DD_WEEKLY_BLOG.md`

**Output:** 1 weekly blog post synthesizing ~280 articles

---

## Data Flow

```
┌─────────────────────────────────────────────────────────────┐
│                    DAILY (2x/day: 9 AM, 9 PM)                │
└─────────────────────────────────────────────────────────────┘

RSS Feeds → Ollama Summaries → Gemini Analysis → Save JSON + MD
   ↓              ↓                    ↓                ↓
ArXiv AI      Technical           Relevance       YYYY-MM-DD_HHMM_
AI Forum      Lay Explanation     Key Insight     articles.json
Google Blog   Tags                Significance    _READABLE.md
                                  Recommendation


┌─────────────────────────────────────────────────────────────┐
│                  WEEKLY (Monday 10 AM)                       │
└─────────────────────────────────────────────────────────────┘

Load 14 JSONs → Extract ~280 articles → Gemini Synthesizes → Blog
    ↓                    ↓                       ↓              ↓
Past 7 days      All Gemini analyses     Trends, highlights   WEEKLY_BLOG.md
(2 runs/day)     Significance levels     Top papers
                 Themes                   Recommendations
```

---

## File Naming Convention

### Daily Files (2 per day)

**Morning run (9 AM):**
- `2025-11-20_0900_articles.json`
- `2025-11-20_0900_READABLE.md`

**Evening run (9 PM):**
- `2025-11-20_2100_articles.json`
- `2025-11-20_2100_READABLE.md`

### Weekly File (Monday 10 AM)

- `2025-11-20_WEEKLY_BLOG.md`

---

## Crontab Entries

```bash
# Daily data collection
0 9 * * * /path/to/cron_pipeline_wrapper.sh # rkl-phase0-morning
0 21 * * * /path/to/cron_pipeline_wrapper.sh # rkl-phase0-evening

# Weekly blog synthesis
0 10 * * 1 /path/to/cron_weekly_blog_wrapper.sh # rkl-phase0-weekly-blog
```

**Verify with:** `crontab -l | grep rkl-phase0`

---

## Agent Roles

### Ollama (llama3.2:3b) - Local Processing
**Runs:** 2x daily (during pipeline)
**Role:** Content summarization
**Tasks:**
- Generate technical summaries from abstracts
- Create lay explanations for practitioners
- Extract initial tags

**Why local:** Privacy-preserving, cost-effective, fast

---

### Gemini (2.0-flash) - Expert Analysis
**Runs:** 2x daily (during pipeline) + 1x weekly (blog synthesis)

**Daily role:** Article-level expert analysis
- Validate Ollama summary quality (pass/fail/uncertain)
- Score secure reasoning relevance (0-1)
- Provide key insights (why this matters)
- Assess significance (breakthrough → tangential)
- Make recommendations (must-include → exclude)

**Weekly role:** Trend synthesis
- Identify top papers of the week
- Spot emerging research patterns
- Note research gaps
- Provide practitioner recommendations
- Write cohesive narrative blog post

**Why cloud:** Domain expertise, nuanced analysis, writing quality

---

## Output Formats

### Daily JSON Brief
**Purpose:** Machine-readable, API integration, archival
**Size:** ~50KB per file
**Content:** Full article metadata + Gemini analysis

```json
{
  "session_id": "brief-2025-11-20-19e285ec",
  "generated_at": "2025-11-20T09:00:00Z",
  "articles": [
    {
      "title": "...",
      "technical_summary": "...",
      "gemini_analysis": {
        "relevance_score": 0.85,
        "key_insight": "...",
        "significance": "important"
      }
    }
  ]
}
```

---

### Daily Readable Markdown
**Purpose:** Human review, internal sharing
**Size:** ~50KB per file
**Content:** Structured sections with clear headers

```markdown
## 1. PathMind: A Retrieve-Prioritize-Reason Framework...

### 📋 Technical Summary
*Generated by Ollama (llama3.2:3b)*

### 🔍 Expert Secure Reasoning Analysis
*Generated by Gemini (2.0-flash)*

**Relevance Score:** 0.85 / 1.0
**Why This Matters:** ...
```

---

### Weekly Blog Post
**Purpose:** Public consumption, practitioner updates
**Size:** ~8-10KB per file
**Content:** Cohesive narrative synthesizing week's research

```markdown
# Secure Reasoning Research - Weekly Brief: Nov 13 - Nov 20, 2025

This week saw a surge in investigations into LLM vulnerabilities...

## Top Papers of the Week
- **PathMind:** This is a game-changer because...

## Emerging Trends
- Proactive defense against adversarial attacks
- Explainability by design

## Weekly Recommendations
1. Prioritize explainability by design
2. Implement proactive defenses
...
```

---

## Cost Analysis

### Daily Operations (2x/day)
**Ollama:** $0 (local deployment)
**Gemini per run:**
- 20 articles × ~1500 chars/article = ~30K chars input
- 20 analyses × ~1200 chars/analysis = ~24K chars output
- Total: ~54K chars = ~13K tokens
- Cost: ~$0.004 per run

**Daily cost:** $0.004 × 2 runs = **$0.008/day**

---

### Weekly Blog (1x/week)
**Gemini:**
- Input: ~100 article summaries = ~50K tokens
- Output: ~8K char blog = ~2K tokens
- Total: ~52K tokens
- Cost: ~$0.016 per week

**Weekly cost:** **$0.016/week**

---

### Monthly Total
**Daily:** $0.008/day × 30 days = **$0.24/month**
**Weekly:** $0.016/week × 4 weeks = **$0.064/month**

**Total:** **~$0.30/month**

---

## Manual Operations

### Generate Weekly Blog On-Demand

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
/home/mike/miniforge3/envs/rkl-briefs/bin/python scripts/generate_weekly_blog.py
```

### Test Daily Pipeline

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
/home/mike/miniforge3/envs/rkl-briefs/bin/python scripts/fetch_and_summarize.py --max-articles 5
```

### View Logs

**Daily pipeline:**
```bash
ls -lht logs/cron/pipeline_*.log | head -5
tail -f logs/cron/pipeline_*.log
```

**Weekly blog:**
```bash
ls -lht logs/cron/weekly_blog_*.log | head -5
tail -f logs/cron/weekly_blog_*.log
```

---

## Monitoring

### Check Last Run Status

**Daily pipeline:**
```bash
# Check latest morning run (should be at 9 AM)
ls -lh content/briefs/*_0900_articles.json | tail -1

# Check latest evening run (should be at 9 PM)
ls -lh content/briefs/*_2100_articles.json | tail -1
```

**Weekly blog:**
```bash
# Check latest Monday blog (should be at 10 AM)
ls -lh content/briefs/*_WEEKLY_BLOG.md | tail -1
```

### Verify Cron Jobs

```bash
crontab -l | grep rkl-phase0
```

Should show:
- 2 daily entries (9 AM, 9 PM)
- 1 weekly entry (Monday 10 AM)

---

## Competition Demo

For the competition, we can demonstrate:

1. **Automated daily collection** - Show cron logs, multiple timestamped files
2. **Expert analysis** - Show JSON with Gemini's secure reasoning analysis
3. **Weekly synthesis** - Show Gemini identifying trends across 280+ articles
4. **Phase-0 telemetry** - Show research data captured throughout

**Key talking points:**
- Fully automated (no human intervention)
- Hybrid model (Ollama + Gemini) with clear role separation
- Expert-quality output (Gemini as senior AI safety researcher)
- Production-ready (scheduled, logged, monitored)
- Cost-effective (~$0.30/month for 2x daily + weekly blog)

---

## Post-Competition: Website Integration

**Production vision:**
```
https://rkl.org/secure-reasoning-research
├── /latest           → Latest weekly blog
├── /archive          → Past weekly blogs
├── /daily            → Daily briefs (searchable)
├── /api/briefs       → JSON API access
└── /rss              → RSS feed
```

**Additional features:**
- Search/filter by secure reasoning aspect
- Tag-based navigation
- Email subscriptions
- Practitioner dashboard

---

## Summary

**Current state:** Fully automated 2x daily data collection + weekly blog synthesis

**Daily:** Ollama summaries → Gemini expert analysis → JSON + Markdown

**Weekly:** Load 14 briefs → Gemini synthesizes trends → Blog post

**Output:** ~40 articles/day analyzed, 1 weekly synthesis blog (~280 articles)

**Cost:** ~$0.30/month for complete automated system

**Next:** Deploy to RKL website for public consumption
