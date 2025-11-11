# Implementation Notes - RKL Logging Package

**Response to GPT-5 Pro's guidance notes**

This document addresses the implementation details and design decisions for the `rkl_logging` package based on GPT-5 Pro's recommendations and our RKL requirements.

---

## GPT's Guidance Points

### 1. Schema Alignment ✅ IMPLEMENTED

> "Keep the schemas in SCHEMAS aligned with your evolving agent artifacts; extend field specs as you finalize prompts/roles."

**Status:** ✅ Complete

**Implementation:**
- All Phase 0 schemas defined in `rkl_logging/schemas/`:
  - `execution_context.py` - Model hyperparameters and performance
  - `agent_graph.py` - Multi-agent message passing
  - `boundary_events.py` - Type III compliance enforcement
  - `governance_ledger.py` - Publication traceability

- Master registry in `schemas/__init__.py`:
  ```python
  SCHEMAS = {
      "execution_context": EXECUTION_CONTEXT_SCHEMA,
      "agent_graph": AGENT_GRAPH_SCHEMA,
      "boundary_events": BOUNDARY_EVENTS_SCHEMA,
      "governance_ledger": GOVERNANCE_LEDGER_SCHEMA
  }
  ```

- Schema evolution plan:
  - Version field in every schema (e.g., `"version": "v1.0"`)
  - `deprecated_fields` list for migrations
  - `validate_record()` function catches drift
  - GitHub Action tests schema stability on every commit

**Next steps:**
- As we finalize agent prompts/roles in Phase 1.5 (MCP implementation), extend schemas:
  - Add new optional fields as agents evolve
  - Update schema versions (v1.0 → v1.1)
  - Document migrations in CHANGELOG

---

### 2. Phase 0 Go-Live Artifacts ✅ IMPLEMENTED

> "For Phase 0 go-live, ensure your agents emit: execution_context, reasoning_graph_edge, boundary_event, governance_ledger"

**Status:** ✅ Complete (minor naming adjustment)

**Implementation:**
We emit all Phase 0 artifacts with one naming clarification:
- ✅ `execution_context` - Captured
- ✅ `agent_graph` (not "reasoning_graph_edge") - Multi-agent coordination edges
- ✅ `boundary_events` (plural) - Type III violations/checks
- ✅ `governance_ledger` - Publication events

**Naming rationale:**
- `agent_graph` instead of `reasoning_graph_edge`:
  - More accurate for multi-agent systems
  - Each record = one edge in the coordination graph
  - "Reasoning traces" are Phase 1 (future)

- `boundary_events` (plural):
  - Consistent with other artifact naming
  - Represents stream of events, not single boundary

**Agent integration example:**
```python
from rkl_logging import StructuredLogger, sha256_text

logger = StructuredLogger(base_dir="./data/research")

# Execution context
logger.log("execution_context", {
    "session_id": session_id,
    "agent_id": "summarizer",
    "model_id": "llama3.2:8b",
    "temp": 0.3,
    "gen_tokens": 150,
    "prompt_id_hash": sha256_text(prompt)
})

# Agent graph
logger.log("agent_graph", {
    "edge_id": f"{from_agent}-{to_agent}-{timestamp}",
    "from_agent": "summarizer",
    "to_agent": "qa_reviewer",
    "msg_type": "summary_for_review",
    "content_hash": sha256_text(content)
})

# Boundary event
logger.log("boundary_events", {
    "event_id": event_id,
    "agent_id": "summarizer",
    "rule_id": "processing_boundary",
    "action": "passed"
})

# Governance ledger
logger.log("governance_ledger", {
    "publish_id": publish_id,
    "artifact_ids": [brief_id],
    "contributing_agent_ids": agent_ids,
    "verification_hashes": hashes
})
```

---

### 3. Hashing Instead of Raw Text ✅ IMPLEMENTED

> "Use hashes instead of raw text everywhere; use sha256_text() for IDs (prompts, inputs, outputs) and keep any sensitive content out of logs by design."

**Status:** ✅ Complete

**Implementation:**

**Hashing utilities** (`utils/hashing.py`):
```python
sha256_text(text: str) -> str
    # "sha256:abc123..." format

sha256_dict(data: dict) -> str
    # Deterministic dict hashing

sha256_file(file_path: str) -> str
    # File content hashing

hash_prompt(prompt: str) -> str
    # Alias for clarity

hash_document(doc: str) -> str
    # Alias for clarity
```

**Privacy by design:**
- ✅ NO raw prompts in logs
- ✅ NO raw input/output text in logs
- ✅ NO sensitive content in logs
- ✅ Only SHA-256 hashes for cross-referencing

**Privacy helpers** (`utils/privacy.py`):
```python
sanitize_for_research(record: dict) -> dict
    # Replaces text fields with hashes
    # "prompt_text" → "prompt_text_hash"

anonymize_for_public(record: dict) -> dict
    # Keeps only structural fields
    # Removes all content, even hashes
```

**Three-tier release model:**
1. **Internal**: Full data (for debugging)
2. **Research**: Sanitized (hashes replace text)
3. **Public**: Anonymized (structural only)

**Example usage:**
```python
# Agent code
summary = ollama.generate(prompt)

# DO NOT log this:
# logger.log("execution_context", {"prompt": prompt})  ❌

# DO log this:
logger.log("execution_context", {
    "prompt_id_hash": sha256_text(prompt),  ✅
    "input_hash": sha256_text(article),     ✅
    "output_hash": sha256_text(summary)     ✅
})
```

---

### 4. Backpressure Behavior ✅ IMPLEMENTED

> "Backpressure behavior: if the queue is full, noncritical logs drop silently; for must-capture streams (e.g., governance_ledger) you can change put_nowait → put to block or fork to a fallback file."

**Status:** ✅ Implemented with design decisions

**Implementation:**

**Current design** (`logging.py`):
- **Batched in-memory buffers** (not async queues)
- Writes trigger when batch_size reached
- Thread-safe with `threading.Lock()`
- No queue overflow possible (grows dynamically)

**Design rationale:**
```python
class StructuredLogger:
    def __init__(self, batch_size=100, ...):
        self._buffers: Dict[str, List[Dict]] = defaultdict(list)
        self._lock = threading.Lock()

    def log(self, artifact_type, record):
        with self._lock:
            self._buffers[artifact_type].append(record)

            if len(self._buffers[artifact_type]) >= self.batch_size:
                self._write_batch(artifact_type)
```

**Why not async queues?**
1. **Simpler**: No asyncio complexity in Phase 1.0
2. **Sufficient**: Logging overhead ~0.1ms per record
3. **No blocking**: Agents aren't I/O bound on logging
4. **Dynamic growth**: Buffers grow as needed

**Handling criticality tiers:**

**Option A: Sampling-based (current)**
```python
logger = StructuredLogger(
    sampling={
        "execution_context": 1.0,       # 100% - always capture
        "governance_ledger": 1.0,       # 100% - always capture
        "boundary_events": 1.0,         # 100% - always capture
        "expensive_traces": 0.05        # 5% - drop 95%
    }
)
```

**Option B: Force-write critical logs**
```python
# Critical log - write immediately, no batching
logger.log("governance_ledger", record, force_write=True)

# Normal log - batched
logger.log("execution_context", record)
```

**Option C: Fallback file (future)**
If needed in Phase 1.5+, implement:
```python
def log(self, artifact_type, record, critical=False):
    if critical and buffer_full:
        # Write to fallback file immediately
        self._write_fallback(artifact_type, record)
    else:
        # Normal batching
        self._buffers[artifact_type].append(record)
```

**Recommendation for now:**
- Use `force_write=True` for governance_ledger
- Use sampling to control volume
- Phase 1.5: Add async queues if needed

---

### 5. Parquet Dependencies ✅ IMPLEMENTED

> "To enable Parquet, install dependencies in your environment: pip install pandas pyarrow"

**Status:** ✅ Complete with fallback

**Implementation:**

**requirements.txt:**
```txt
# Core dependencies (required)
python-dotenv>=1.0.0
pyyaml>=6.0
requests>=2.31.0
feedparser>=6.0.10

# Research data (optional but recommended)
pandas>=2.0.0
pyarrow>=12.0.0
```

**Fallback logic** (`logging.py`):
```python
try:
    import pandas as pd
    PARQUET_AVAILABLE = True
except ImportError:
    PARQUET_AVAILABLE = False

def _write_batch(self, artifact_type):
    if PARQUET_AVAILABLE:
        # Preferred: Parquet (10x compression)
        df = pd.DataFrame(records)
        df.to_parquet(output_file, compression='snappy')
    else:
        # Fallback: NDJSON (readable, no dependencies)
        with open(output_file, 'w') as f:
            for record in records:
                f.write(json.dumps(record) + '\n')
```

**Why Parquet?**
- **10x compression** vs JSON
- **Columnar storage** - fast analytics
- **Schema enforcement** - type safety
- **Industry standard** - Pandas/Spark/DuckDB

**Why NDJSON fallback?**
- **Zero dependencies** - works everywhere
- **Human readable** - debugging
- **Line-by-line** - stream processing
- **Git-friendly** - diffs work

**Installation:**
```bash
# Full installation (recommended)
pip install -r requirements.txt

# Minimal installation (NDJSON only)
pip install python-dotenv pyyaml requests feedparser
```

**GitHub Action testing:**
- Tests with Parquet (pandas + pyarrow)
- Tests without Parquet (NDJSON fallback)
- Ensures both code paths work

---

### 6. Storage Guidance ✅ IMPLEMENTED

> "Storage guidance (defaults are conservative): Structural logs are tiny; full-text deep captures should be kept out of this logger (or written via a separate, gated path) to maintain privacy and low overhead."

**Status:** ✅ Enforced by design

**Implementation:**

**Volume estimates per brief:**
```
Phase 0 artifacts (structural only):
- execution_context: ~100KB (1000 records × 100 bytes)
- agent_graph: ~50KB (500 edges × 100 bytes)
- boundary_events: ~10KB (50 events × 200 bytes)
- governance_ledger: ~2KB (1 record × 2KB)
─────────────────────────────────────────────
Total per brief: ~160KB uncompressed
                 ~50KB compressed (Parquet)
```

**Annual storage (52 briefs):**
```
Year 1 (Phase 0):
- Raw: 8.3MB
- Compressed: 2.6MB
- Cost: $0.00 (negligible)

Year 2 (Phase 0+1+2):
- With all artifacts: ~50MB
- Cost: Still negligible
```

**Design principles:**

**✅ DO log (structural):**
- Model hyperparameters (temp, top_p)
- Token counts (ctx_tokens_used, gen_tokens)
- Latency metrics (tool_lat_ms)
- Hashes (prompt_id_hash, content_hash)
- Agent IDs, session IDs, timestamps
- Quality scores, retry counts
- Boundary check results

**❌ DO NOT log (content):**
- Raw prompts (use `sha256_text(prompt)`)
- Input articles (use `sha256_text(article)`)
- Generated summaries (use `sha256_text(summary)`)
- Retrieved documents (use `sha256_text(doc)`)
- User queries (use `sha256_text(query)`)
- Anything with PII

**Gated path for full-text (if needed):**

If you need to capture full text for debugging:

```python
# Option 1: Separate logger instance
debug_logger = StructuredLogger(
    base_dir="./data/debug-full-text",  # Different directory
    type3_enforcement=False,             # Disable Type III checks
    auto_manifest=False                  # Don't include in releases
)

debug_logger.log("debug_traces", {
    "session_id": session_id,
    "full_prompt": prompt,              # OK in debug logger
    "full_output": output               # OK in debug logger
})

# Option 2: Manual gated file
if os.getenv("RKL_DEBUG_FULL_TEXT") == "true":
    with open("./data/debug/full_trace.txt", "a") as f:
        f.write(f"Prompt: {prompt}\n")
        f.write(f"Output: {output}\n\n")
```

**Add to `.gitignore`:**
```gitignore
# Never commit full-text logs
data/debug-full-text/
data/debug/
*.full.log
```

---

### 7. Unit Tests & CI ✅ IMPLEMENTED

> "If you want, I can also generate a tiny unit test file and a GitHub Action to run schema drift checks and ensure we don't regress the logging interface as you iterate."

**Status:** ✅ Complete

**Implementation:**

**Test file:** `rkl_logging/test_logging.py`

Tests cover:
1. ✅ Schema registry (all Phase 0 schemas present)
2. ✅ Schema validation (valid/invalid records)
3. ✅ Hashing utilities (deterministic, correct format)
4. ✅ Privacy helpers (sanitization, anonymization)
5. ✅ Basic logging (writes files correctly)
6. ✅ Sampling (0% drops, 100% keeps)
7. ✅ Manifest generation (statistics tracked)
8. ✅ Schema drift detection (no unexpected changes)

**Run tests:**
```bash
cd rkl_logging
python test_logging.py
```

**GitHub Action:** `.github/workflows/test-logging.yml`

Runs on:
- Every push to main/develop
- Every PR affecting `rkl_logging/`
- Tests Python 3.9, 3.10, 3.11

Jobs:
1. **test**: Run full test suite
   - With Parquet (pandas + pyarrow)
   - Without Parquet (NDJSON fallback)

2. **schema-drift-check**: Detect schema changes
   - Compares schemas between commits
   - Warns if schemas modified
   - Reminds to update version numbers

3. **lint**: Code quality checks
   - flake8 (syntax errors)
   - pylint (style warnings)

**Schema snapshot:**
- Exports schemas on every test run
- Uploads as artifact (30-day retention)
- Enables historical comparison

---

## Summary: GPT's Guidance → Our Implementation

| GPT Guidance | Status | Location |
|--------------|--------|----------|
| Schema alignment | ✅ | `rkl_logging/schemas/` |
| Phase 0 artifacts | ✅ | All 4 schemas defined |
| Hashing everywhere | ✅ | `utils/hashing.py` + privacy helpers |
| Backpressure handling | ✅ | Batching + sampling + force_write |
| Parquet dependencies | ✅ | `requirements.txt` + fallback |
| Storage guidance | ✅ | Enforced by design (no raw text) |
| Unit tests | ✅ | `test_logging.py` (8 tests) |
| GitHub Action | ✅ | `.github/workflows/test-logging.yml` |

---

## Additional Enhancements Beyond GPT's Guidance

### 1. Three-Tier Privacy Model
- Internal: Full data
- Research: Sanitized (hashes)
- Public: Anonymized (structural)

### 2. Date Partitioning
```
data/research/
└── execution_context/
    └── 2025/11/11/
        ├── execution_context_091523.parquet
        └── execution_context_101234.parquet
```

### 3. RKL Metadata Enrichment
Every record auto-enriched with:
- `rkl_version`: System version
- `timestamp`: ISO 8601 UTC
- `type3_compliant`: Boundary flag

### 4. CARE Principles Metadata
Optional `care_metadata` field:
```python
"care_metadata": {
    "collective_benefit": True,
    "authority_to_control": "local",
    "responsibility": "audit-001",
    "ethics": "consent_verified"
}
```

### 5. Manual Manifest Generation
```python
logger.generate_manifest()  # Writes to data/manifests/YYYY-MM-DD.json
```

### 6. Force-Write for Critical Logs
```python
logger.log("governance_ledger", record, force_write=True)
```

---

## Next Steps: Phase 1.5 Enhancements

When we implement full MCP architecture (Q1 2026), consider:

### 1. Async Queue-Based Logging
```python
import asyncio

class AsyncStructuredLogger:
    def __init__(self, ...):
        self._queue = asyncio.Queue(maxsize=10000)
        self._worker_task = asyncio.create_task(self._worker())

    async def log(self, artifact_type, record):
        try:
            self._queue.put_nowait((artifact_type, record))
        except asyncio.QueueFull:
            # Drop noncritical, fallback for critical
            if artifact_type in CRITICAL_ARTIFACTS:
                await self._write_fallback(artifact_type, record)
```

### 2. Streaming to Remote Storage
```python
# Stream to S3/GCS for long-term archival
logger = StructuredLogger(
    base_dir="./data/research",
    remote_sync={
        "enabled": True,
        "provider": "s3",
        "bucket": "rkl-research-data",
        "frequency": "daily"
    }
)
```

### 3. Real-Time Metrics Dashboard
```python
# Expose Prometheus metrics
logger = StructuredLogger(
    monitoring={
        "enabled": True,
        "prometheus_port": 9090
    }
)
```

### 4. Phase 1+2 Artifacts
- Reasoning traces (5% sampling)
- Retrieval provenance (10% sampling)
- Quality trajectories (100%)
- Hallucination matrix (100%)
- Failure snapshots (5% sampling)
- Human interventions (100%)

---

## Testing the Implementation

### Quick Test
```bash
cd rkl_logging
python test_logging.py
```

### Integration Test
```bash
cd rkl_logging
python example.py
```

Expected output:
```
╔══════════════════════════════════════════════════════════╗
║          RKL Logging Package Examples                   ║
╚══════════════════════════════════════════════════════════╝

Example 1: Basic Logging
✓ Logged 5 execution contexts
✓ Check output in: ./example_data/execution_context/

Example 2: All Phase 0 Artifacts
✓ Logged execution_context
✓ Logged agent_graph
✓ Logged boundary_events
✓ Logged governance_ledger

Example 3: Privacy Helpers
✓ Sanitized for RESEARCH
✓ Anonymized for PUBLIC

Example 4: Sampling Configuration
✓ Logged 20 agent_graph records with 50% sampling

Example 5: Schema Validation
✓ Valid record accepted
⚠ Invalid record logged with warning

All examples completed successfully!
```

### Inspect Output
```python
import pandas as pd

# Load execution context
df = pd.read_parquet("example_data/execution_context/")
print(df.head())
print(df.describe())

# Check schemas
from rkl_logging import SCHEMAS
print(SCHEMAS["execution_context"]["required_fields"])
```

---

## Questions for GPT-5 Pro

If GPT-5 Pro has additional guidance, we'd love to hear about:

1. **Backpressure**: Should we implement async queues now or wait for Phase 1.5?
2. **Critical logs**: Should `governance_ledger` use `force_write=True` by default?
3. **Schema versioning**: Is our approach (v1.0, v1.1, ...) aligned with best practices?
4. **Performance**: Any optimizations for high-volume logging (>10K records/min)?
5. **Testing**: Are there edge cases we should add to `test_logging.py`?

---

## Contact

**Implementation questions:**
- GitHub: [rkl-consolidated/secure-reasoning-brief]
- Email: info@resonantknowledgelab.org

**GPT-5 Pro collaboration:**
- We're grateful for the logging skeleton guidance
- Open to further refinements
- Happy to share learnings with the community

---

*Last updated: 2025-11-11*
*Version: 1.0*
*Author: Resonant Knowledge Lab*
