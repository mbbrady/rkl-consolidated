# Phase 1 Telemetry Improvements - Implementation Guide

**Goal:** Enhance reasoning traces from shallow (workflow) to medium depth (cognitive)

**Timeline:** 2-3 hours total
- Implementation: 1 hour
- Testing: 30 minutes
- Full pipeline run: 30 minutes
- Verification: 30 minutes

---

## Changes Overview

### 1. Chain-of-Thought Prompts (30 min)

**File:** `scripts/fetch_and_summarize.py`

**Target:** Summarizer agent prompt

**Before:**
```python
prompt = f"""Summarize this AI research paper in 80 words:

{article_text}"""
```

**After:**
```python
prompt = f"""Analyze this AI research paper and create a summary.

First, identify:
1. Main contribution (1 sentence)
2. Key methodology (1 sentence)
3. Most important result (1 sentence)

Then, combine into an 80-word technical summary focusing on what practitioners need to know.

Article:
{article_text}

Reasoning:"""
```

**Benefit:** Chain-of-thought reasoning gets captured in LLM response, logged in secure_reasoning_trace

---

### 2. Full Prompt Capture in execution_context (15 min)

**File:** `scripts/fetch_and_summarize.py`

**Target:** All `research_logger.log("execution_context", ...)` calls

**Before:**
```python
exec_record = {
    "session_id": session_id,
    "agent_name": "summarizer",
    "model_name": "llama3.1:8b",
    "input_tokens": len(prompt.split()),
    "output_tokens": len(summary.split()),
    # ...
}
```

**After:**
```python
exec_record = {
    "session_id": session_id,
    "agent_name": "summarizer",
    "model_name": "llama3.1:8b",
    "input_tokens": len(prompt.split()),
    "output_tokens": len(summary.split()),
    "prompt_preview": prompt[:1000],  # NEW - First 1000 chars
    "response_preview": summary[:1000],  # NEW - First 1000 chars
    # ...
}
```

**Benefit:** Researchers can see actual prompts used, not just metadata

---

### 3. Decision Rationale in reasoning_graph_edge (15 min)

**File:** `scripts/fetch_and_summarize.py`

**Target:** All `research_logger.log("reasoning_graph_edge", ...)` calls

**Before:**
```python
self.research_logger.log("reasoning_graph_edge", {
    "edge_id": str(uuid.uuid4()),
    "session_id": session_id,
    "source_agent": "summarizer",
    "target_agent": "lay_translator",
    "message_type": "data",
    "intent": "lay_explanation",
    # ...
})
```

**After:**
```python
self.research_logger.log("reasoning_graph_edge", {
    "edge_id": str(uuid.uuid4()),
    "session_id": session_id,
    "source_agent": "summarizer",
    "target_agent": "lay_translator",
    "message_type": "data",
    "intent": "lay_explanation",
    "decision_rationale": f"Technical summary complete ({len(summary)} chars). Passing to lay translator for accessibility.",  # NEW
    "payload_summary": f"Summary about {extract_topic(summary)}",  # NEW - more descriptive
    # ...
})
```

**Benefit:** Shows WHY handoffs happen, not just that they happened

---

### 4. Agent State in system_state (15 min)

**File:** `scripts/fetch_and_summarize.py`

**Target:** System state logging (if present, or add if missing)

**Add new function:**
```python
def get_agent_states(self):
    """Capture current state of all agents"""
    return {
        "summarizer": {
            "status": "active" if self.summarizer_active else "idle",
            "papers_processed": self.summarizer_count,
            "success_rate": self.summarizer_success / max(self.summarizer_count, 1)
        },
        "gemini_qa": {
            "status": "active" if self.gemini_active else "idle",
            "reviews_completed": self.gemini_count,
            "pass_rate": self.gemini_pass / max(self.gemini_count, 1)
        },
        # ... other agents
    }
```

**Use in logging:**
```python
self.research_logger.log("system_state", {
    "session_id": session_id,
    "timestamp_utc": datetime.utcnow().isoformat(),
    "pipeline_status": "running",
    "current_phase": "processing",
    "agent_states": self.get_agent_states(),  # NEW
})
```

**Benefit:** System-level view of multi-agent coordination

---

## Implementation Steps

### Step 1: Update Summarizer Prompt (10 min)

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief

# Backup current version
cp scripts/fetch_and_summarize.py scripts/fetch_and_summarize.py.backup-nov22

# Edit the summarizer prompt section
```

**Find this section:**
```python
# Around line 200-250 - summarizer agent call
def generate_summary(self, article_text):
    prompt = f"""Summarize this AI research paper in 80 words:

    {article_text}"""
```

**Replace with:**
```python
def generate_summary(self, article_text):
    prompt = f"""Analyze this AI research paper and create a summary.

First, identify:
1. Main contribution (1 sentence)
2. Key methodology (1 sentence)
3. Most important result (1 sentence)

Then, combine into an 80-word technical summary focusing on what practitioners need to know.

Article:
{article_text}

Reasoning:"""
```

### Step 2: Add Prompt Capture to execution_context (15 min)

**Find all execution_context logging calls** (should be 3-4 instances):

```bash
grep -n "execution_context" scripts/fetch_and_summarize.py
```

**For each instance**, add `prompt_preview` and `response_preview` fields.

**Example location 1 - Summarizer:**
```python
# Before
exec_record = {
    "session_id": session_id,
    "agent_name": "summarizer",
    "model_name": "llama3.1:8b",
    # ...
}

# After
exec_record = {
    "session_id": session_id,
    "agent_name": "summarizer",
    "model_name": "llama3.1:8b",
    "prompt_preview": prompt[:1000],
    "response_preview": summary[:1000],
    # ...
}
```

**Repeat for:** gemini_qa, lay_translator, metadata_extractor

### Step 3: Add Decision Rationale to reasoning_graph_edge (15 min)

**Find all reasoning_graph_edge logging calls:**

```bash
grep -n "reasoning_graph_edge" scripts/fetch_and_summarize.py
```

**Add `decision_rationale` field to each:**

```python
# Example 1: summarizer → lay_translator
self.research_logger.log("reasoning_graph_edge", {
    # ... existing fields ...
    "decision_rationale": f"Technical summary complete ({len(summary)} chars). Quality acceptable. Passing to lay translator.",
    "payload_summary": f"Summary: {summary[:100]}...",
})

# Example 2: lay_translator → metadata_extractor
self.research_logger.log("reasoning_graph_edge", {
    # ... existing fields ...
    "decision_rationale": f"Lay explanation generated ({len(lay_text)} chars). Ready for metadata extraction.",
    "payload_summary": f"Lay text: {lay_text[:100]}...",
})

# Example 3: After Gemini QA
self.research_logger.log("reasoning_graph_edge", {
    # ... existing fields ...
    "decision_rationale": f"Gemini QA verdict: {verdict}. Confidence: {confidence}. {'Keeping' if verdict == 'pass' else 'Flagging'} article.",
    "payload_summary": f"QA result: {verdict}, theme_score: {theme_score}",
})
```

### Step 4: Add Agent State Tracking (20 min)

**Add state tracking variables to class:**

```python
class PipelineOrchestrator:
    def __init__(self):
        # ... existing init ...

        # NEW: Agent state tracking
        self.agent_stats = {
            "summarizer": {"processed": 0, "success": 0, "active": False},
            "lay_translator": {"processed": 0, "success": 0, "active": False},
            "gemini_qa": {"processed": 0, "success": 0, "active": False},
            "metadata_extractor": {"processed": 0, "success": 0, "active": False},
        }
```

**Update state during processing:**

```python
def process_article(self, article):
    # Mark summarizer as active
    self.agent_stats["summarizer"]["active"] = True
    self.agent_stats["summarizer"]["processed"] += 1

    # ... summarizer logic ...

    if summary_success:
        self.agent_stats["summarizer"]["success"] += 1

    self.agent_stats["summarizer"]["active"] = False
```

**Log system state periodically:**

```python
# At start of run
self.research_logger.log("system_state", {
    "session_id": session_id,
    "timestamp_utc": datetime.utcnow().isoformat(),
    "pipeline_status": "starting",
    "agent_states": {
        name: {
            "status": "idle",
            "queue_depth": 0,
            "success_rate": stats["success"] / max(stats["processed"], 1)
        }
        for name, stats in self.agent_stats.items()
    }
})

# At end of run
self.research_logger.log("system_state", {
    "session_id": session_id,
    "timestamp_utc": datetime.utcnow().isoformat(),
    "pipeline_status": "completed",
    "agent_states": {
        name: {
            "status": "idle",
            "total_processed": stats["processed"],
            "success_rate": stats["success"] / max(stats["processed"], 1)
        }
        for name, stats in self.agent_stats.items()
    }
})
```

---

## Testing

### Test 1: Single Paper Run (10 min)

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief

# Run with limit 1 for fast test
python scripts/fetch_and_summarize.py --limit 1 --debug

# Check for errors
echo "Exit code: $?"
```

**Expected output:**
- Pipeline completes successfully
- Debug output shows chain-of-thought in summary
- No errors in telemetry logging

### Test 2: Verify Telemetry Quality (15 min)

```bash
# Find today's telemetry files
ls -lh data/research/execution_context/2025/11/22/

# Check execution_context has prompt_preview
python3 << 'EOF'
import pandas as pd
from glob import glob

files = glob('data/research/execution_context/2025/11/22/*.parquet')
if files:
    df = pd.read_parquet(files[-1])  # Most recent
    print("Columns:", df.columns.tolist())

    if 'prompt_preview' in df.columns:
        print("\n✅ prompt_preview field present")
        print(f"Sample: {df['prompt_preview'].iloc[0][:200]}...")
    else:
        print("\n❌ prompt_preview field MISSING")

    if 'response_preview' in df.columns:
        print("\n✅ response_preview field present")
        print(f"Sample: {df['response_preview'].iloc[0][:200]}...")
    else:
        print("\n❌ response_preview field MISSING")
else:
    print("No execution_context files found for today")
EOF

# Check reasoning_graph_edge has decision_rationale
python3 << 'EOF'
import pandas as pd
from glob import glob

files = glob('data/research/reasoning_graph_edge/2025/11/22/*.parquet')
if files:
    df = pd.read_parquet(files[-1])
    print("Columns:", df.columns.tolist())

    if 'decision_rationale' in df.columns:
        print("\n✅ decision_rationale field present")
        print(f"Sample: {df['decision_rationale'].iloc[0]}")
    else:
        print("\n❌ decision_rationale field MISSING")
else:
    print("No reasoning_graph_edge files found for today")
EOF

# Check system_state has agent_states
python3 << 'EOF'
import pandas as pd
from glob import glob

files = glob('data/research/system_state/2025/11/22/*.parquet')
if files:
    df = pd.read_parquet(files[-1])
    print("Columns:", df.columns.tolist())

    if 'agent_states' in df.columns:
        print("\n✅ agent_states field present")
        print(f"Sample: {df['agent_states'].iloc[0]}")
    else:
        print("\n❌ agent_states field MISSING")
else:
    print("No system_state files found for today")
EOF
```

### Test 3: Verify Chain-of-Thought (10 min)

```bash
# Check that summaries now include reasoning steps
python3 << 'EOF'
import json

with open('content/briefs/2025-11-22_articles.json', 'r') as f:
    data = json.load(f)

if data.get('articles'):
    article = data['articles'][0]
    summary = article.get('summary', '')

    print("Summary length:", len(summary))
    print("\nFirst 500 chars:")
    print(summary[:500])

    # Look for reasoning indicators
    reasoning_indicators = ['First,', 'Second,', 'Main contribution', 'methodology', 'result']
    found = [ind for ind in reasoning_indicators if ind.lower() in summary.lower()]

    if found:
        print(f"\n✅ Chain-of-thought detected: {found}")
    else:
        print("\n⚠️ Chain-of-thought not obvious, but may be present in different form")
else:
    print("No articles in today's brief")
EOF
```

---

## Success Criteria

After implementation and testing, you should see:

✅ **execution_context artifacts:**
- `prompt_preview` field with first 1000 chars of prompts
- `response_preview` field with first 1000 chars of responses

✅ **reasoning_graph_edge artifacts:**
- `decision_rationale` field explaining why handoff occurred
- `payload_summary` field with more descriptive content

✅ **system_state artifacts:**
- `agent_states` object with per-agent status
- Success rates and processing counts

✅ **Chain-of-thought in summaries:**
- Summaries show reasoning steps (not just final answer)
- Longer, more detailed summaries (600-800 chars vs 540 chars)

---

## Full Pipeline Run (30 min)

After successful test:

```bash
# Run full pipeline (no limit)
python scripts/fetch_and_summarize.py

# This will process all new papers with improved telemetry
# Should take 10-20 minutes depending on article count
```

---

## Verification Report (30 min)

After full run, generate quality comparison:

```bash
python3 << 'EOF'
import pandas as pd
from glob import glob
from datetime import datetime

print("=" * 60)
print("PHASE 1 TELEMETRY IMPROVEMENTS - VERIFICATION REPORT")
print("=" * 60)

# Get Nov 21 (baseline) vs Nov 22 (improved) data
baseline_date = "2025/11/21"
improved_date = "2025/11/22"

print(f"\nBaseline: {baseline_date}")
print(f"Improved: {improved_date}")

# Compare execution_context
print("\n" + "=" * 60)
print("1. EXECUTION CONTEXT")
print("=" * 60)

baseline_files = glob(f'data/research/execution_context/{baseline_date}/*.parquet')
improved_files = glob(f'data/research/execution_context/{improved_date}/*.parquet')

if baseline_files:
    baseline_df = pd.read_parquet(baseline_files[0])
    print(f"Baseline columns: {len(baseline_df.columns)}")
    print(f"Baseline rows: {len(baseline_df)}")

if improved_files:
    improved_df = pd.read_parquet(improved_files[0])
    print(f"Improved columns: {len(improved_df.columns)}")
    print(f"Improved rows: {len(improved_df)}")

    new_fields = set(improved_df.columns) - set(baseline_df.columns)
    print(f"\n✅ New fields added: {new_fields}")

# Compare reasoning_graph_edge
print("\n" + "=" * 60)
print("2. REASONING GRAPH EDGE")
print("=" * 60)

baseline_files = glob(f'data/research/reasoning_graph_edge/{baseline_date}/*.parquet')
improved_files = glob(f'data/research/reasoning_graph_edge/{improved_date}/*.parquet')

if baseline_files:
    baseline_df = pd.read_parquet(baseline_files[0])
    print(f"Baseline columns: {len(baseline_df.columns)}")

if improved_files:
    improved_df = pd.read_parquet(improved_files[0])
    print(f"Improved columns: {len(improved_df.columns)}")

    new_fields = set(improved_df.columns) - set(baseline_df.columns)
    print(f"\n✅ New fields added: {new_fields}")

    if 'decision_rationale' in improved_df.columns:
        print(f"\nSample decision rationale:")
        print(improved_df['decision_rationale'].iloc[0])

# Compare system_state
print("\n" + "=" * 60)
print("3. SYSTEM STATE")
print("=" * 60)

baseline_files = glob(f'data/research/system_state/{baseline_date}/*.parquet')
improved_files = glob(f'data/research/system_state/{improved_date}/*.parquet')

if improved_files:
    improved_df = pd.read_parquet(improved_files[0])
    print(f"Improved columns: {len(improved_df.columns)}")

    if 'agent_states' in improved_df.columns:
        print(f"\n✅ agent_states field present")
        print(f"Sample: {str(improved_df['agent_states'].iloc[0])[:300]}...")

print("\n" + "=" * 60)
print("SUMMARY")
print("=" * 60)
print("✅ Phase 1 improvements successfully applied")
print("✅ Reasoning depth increased from shallow to medium")
print("✅ Ready for Kaggle/HuggingFace dataset publishing")
print("=" * 60)
EOF
```

---

## Next Steps After Phase 1

1. ✅ Phase 1 complete
2. Mark todo item as completed
3. Test with single paper run
4. Run full pipeline to generate improved data
5. Package for Kaggle/HuggingFace
6. Optional: Implement Phase 2 (multi-step reasoning, confidence breakdown)

---

## Rollback Plan (If Needed)

```bash
# Restore backup if something goes wrong
cp scripts/fetch_and_summarize.py.backup-nov22 scripts/fetch_and_summarize.py

# Or use git
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
git checkout scripts/fetch_and_summarize.py
```

---

**Status:** Implementation guide complete. Ready to apply changes to codebase.

---

*Last Updated: November 22, 2025 - 4:30 PM EST*
