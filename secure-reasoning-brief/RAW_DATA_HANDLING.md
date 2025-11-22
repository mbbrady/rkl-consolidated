# Raw Data Handling - Phase-0 Compliance

## Overview

This document explains how raw data is handled in the pipeline to demonstrate Phase-0 research telemetry compliance and secure reasoning principles.

---

## Data Flow

```
RSS Feed → Full Article Content → Ollama Processing → Derived Summaries → Storage
    ↓              ↓                       ↓                 ↓              ↓
Public         8000 chars            Local LLM         Releasable    JSON + Ledger
Internet       (excerpt)             (Private)         Insights      (Auditable)
```

---

## What We Store

### 1. Raw Content Excerpt (`raw_content_excerpt`)

**Stored:** First 8000 characters of article content

**Why this amount:**
- **ArXiv abstracts:** Typically 1500-2000 chars → We get 100% of abstract
- **AI Alignment Forum:** Full posts can be 50,000+ chars → We get first 8000
- **Google AI Blog:** Posts can be 10,000-20,000 chars → We get first 8000
- **Ollama context window:** llama3.2:3b supports 128K tokens → 8000 chars is ~2K tokens (very conservative)

**Purpose:**
- Provenance: What raw data did Ollama actually see?
- Verification: Can we validate summaries against source?
- Auditability: Full reasoning chain from input to output

**Future upgrade path:**
```python
# Current limit
raw_content_excerpt = article["content"][:8000]

# After memory upgrade, can increase:
raw_content_excerpt = article["content"][:50000]  # Much more context for Ollama
```

---

### 2. Derived Insights (What Gets Published)

**Published artifacts:**
- Technical summaries (Ollama-generated)
- Lay explanations (Ollama-generated)
- Tags (Ollama-extracted)
- Gemini analysis (secure reasoning relevance)

**NOT published:**
- Raw article content beyond excerpt
- Full text of blog posts
- Any unpublished/sensitive information (if source were private)

---

## Phase-0 Governance Ledger

Every pipeline run logs to `governance_ledger` with detailed raw data handling:

```json
{
  "type3_verified": true,
  "raw_data_exposed": false,
  "derived_insights_only": true,
  "raw_data_handling": {
    "raw_content_stored": true,
    "raw_content_location": "local_filesystem",
    "processing_location": "local_ollama",
    "published_artifacts": ["summaries", "tags", "gemini_analysis"],
    "verification_capability": "enabled",
    "privacy_level": "public_internet_articles"
  }
}
```

**What this proves:**
1. ✅ Raw data was stored locally for auditability
2. ✅ Raw data never left local filesystem
3. ✅ Processing happened on local Ollama (not cloud)
4. ✅ Only derived insights were published
5. ✅ Verification is possible (summaries vs. raw)
6. ✅ Privacy level is documented

---

## Use Case: Protecting Sensitive Data

This same pattern works for sensitive/proprietary data:

### Example: Medical Records

```
Patient Medical Records → Truncate to relevant sections → Local Ollama → De-identified summaries
         ↓                         ↓                            ↓                ↓
    PHI Protected            Only relevant data          Local processing    Published insights
    (HIPAA compliance)       (no full record)            (never cloud)       (no PHI)
```

**Governance ledger would show:**
```json
{
  "raw_data_exposed": false,  // PHI never published
  "processing_location": "local_ollama",  // No cloud API calls
  "published_artifacts": ["de-identified_summaries"],
  "privacy_level": "phi_protected"  // Documents sensitivity
}
```

---

## Verification Example

**Scenario:** "Did Ollama hallucinate details in the technical summary?"

**Process:**
1. Load brief JSON
2. Read `technical_summary` (Ollama's output)
3. Read `raw_content_excerpt` (what Ollama saw)
4. Compare: Are details in summary actually present in excerpt?

**Code:**
```python
article = brief['articles'][0]

summary = article['technical_summary']
raw = article['raw_content_excerpt']

# Check if summary claims appear in raw content
if "combines retrieval with prioritization" in summary:
    if "retrieval" in raw and "prioritization" in raw:
        print("✅ Summary detail verified in raw content")
    else:
        print("⚠️ Potential hallucination detected")
```

---

## Current Limits

### Content Limits by Source

| Source | Typical Length | We Store | Coverage |
|--------|---------------|----------|----------|
| ArXiv abstracts | 1,500-2,000 chars | 8,000 chars | 100% |
| AI Alignment Forum | 50,000+ chars | 8,000 chars | ~15% |
| Google AI Blog | 10,000-20,000 chars | 8,000 chars | 40-80% |

### Ollama Context Window

- **Model:** llama3.2:3b
- **Context window:** 128K tokens (~500K characters)
- **We use:** 8,000 chars (~2K tokens)
- **Utilization:** ~1.5% of available context

**Plenty of room for expansion!**

---

## Upgrade Path

### When Memory/Performance Allows

```python
# Current (conservative)
OLLAMA_CONTEXT_CHARS = 8000

# After upgrade (moderate)
OLLAMA_CONTEXT_CHARS = 50000  # Full blog posts, most long-form content

# After major upgrade (aggressive)
OLLAMA_CONTEXT_CHARS = 200000  # Use ~80% of 128K token window
```

**Benefits of more context:**
- Better summaries (more information to synthesize)
- Fewer truncated blog posts
- More accurate tag extraction
- Richer lay explanations

**Tradeoffs:**
- Longer processing time per article
- Higher memory usage
- More data to store per article

---

## File Size Impact

### Current (8000 char excerpts)

**Per article:**
- Metadata: ~200 bytes
- Raw excerpt: ~8,000 bytes
- Ollama summaries: ~1,200 bytes
- Gemini analysis: ~1,000 bytes
- **Total:** ~10,400 bytes per article

**Per brief (20 articles):**
- ~208 KB per brief
- 2 briefs/day = ~416 KB/day
- ~12 MB/month

**Storage cost:** Negligible (< $0.01/month)

### After Upgrade (50000 char excerpts)

**Per article:**
- Raw excerpt: ~50,000 bytes (6x larger)
- **Total:** ~52,000 bytes per article

**Per brief (20 articles):**
- ~1 MB per brief
- 2 briefs/day = ~2 MB/day
- ~60 MB/month

**Storage cost:** Still negligible (< $0.05/month)

---

## Competition Value

### What This Demonstrates

1. **Provenance Tracking**
   - We can trace every summary back to raw source
   - Full audit trail from input to output

2. **Local Processing**
   - Sensitive data never leaves local system
   - Ollama processes everything locally

3. **Privacy-Preserving**
   - Raw data stored locally
   - Only derived insights published

4. **Verifiable AI**
   - Can validate LLM outputs against inputs
   - Detect hallucinations or errors

5. **Phase-0 Compliance**
   - Governance ledger documents all handling
   - Meets Type III safety requirements

---

## Summary

**Current State:**
- ✅ Storing 8000 char excerpts (what Ollama sees)
- ✅ Governance ledger documents handling
- ✅ Can verify summaries against raw
- ✅ Privacy-preserving pattern demonstrated

**Future Enhancement:**
- 📈 Increase to 50K chars after memory upgrade
- 📈 Give Ollama more context for better summaries
- 📈 Maintain same governance/audit patterns

**Key Message:**
"We process raw data with local LLMs, maintain full audit trails, and only publish derived insights - demonstrating secure reasoning principles in practice."
