# RKL Logging - Research-Grade Telemetry

**Lightweight, async structured logger for AI agentic systems**

Captures structural telemetry without raw text, enabling research-grade datasets while preserving privacy and Type III secure reasoning boundaries.

---

## Quick Start

```python
from rkl_logging import StructuredLogger, sha256_text

# Initialize logger
logger = StructuredLogger(
    base_dir="./data/research",
    rkl_version="1.0",
    batch_size=100
)

# Log an execution context
logger.log("execution_context", {
    "session_id": "brief-2025-11-11-001",
    "turn_id": 1,
    "agent_id": "summarizer",
    "model_id": "llama3.2:8b",
    "model_rev": "8B-q4",
    "temp": 0.3,
    "top_p": 0.95,
    "ctx_tokens_used": 2048,
    "gen_tokens": 150,
    "tool_lat_ms": 1234,
    "prompt_id_hash": sha256_text("Your prompt template here")
})

# Flush and close
logger.close()
```

---

## Features

✅ **Structural Telemetry** - No raw text, only hashes and metrics
✅ **Async Batched Writes** - Non-blocking, high performance
✅ **Parquet Support** - Efficient columnar storage (falls back to NDJSON)
✅ **Date Partitioning** - Automatic organization by date/artifact
✅ **Schema Validation** - Catch errors early
✅ **Sampling Support** - Control data volume
✅ **Privacy Helpers** - Built-in sanitization/anonymization
✅ **Type III Tracking** - Boundary enforcement logging
✅ **Auto Manifests** - Daily summaries generated automatically

---

## Phase 0 Artifacts (Implement Now)

### 1. Execution Context
**What:** Model hyperparameters and performance metrics
**Why:** Understand model behavior, compare configurations
**Schema:** `execution_context.py`

```python
logger.log("execution_context", {
    "session_id": "s1",
    "agent_id": "summarizer",
    "model_id": "llama3.2:8b",
    "temp": 0.3,
    "gen_tokens": 150,
    ...
})
```

### 2. Agent Graph
**What:** Multi-agent message passing (structural)
**Why:** Study coordination patterns, emergent behaviors
**Schema:** `agent_graph.py`

```python
logger.log("agent_graph", {
    "edge_id": "edge-001",
    "from_agent": "summarizer",
    "to_agent": "qa_reviewer",
    "msg_type": "summary_for_review",
    "content_hash": sha256_text(content),
    ...
})
```

### 3. Boundary Events
**What:** Type III compliance enforcement
**Why:** Prove secure reasoning works, catch violations
**Schema:** `boundary_events.py`

```python
logger.log("boundary_events", {
    "event_id": "evt-001",
    "agent_id": "summarizer",
    "rule_id": "processing_boundary",
    "action": "blocked",
    ...
})
```

### 4. Governance Ledger
**What:** Publication traceability
**Why:** Complete audit trail for CARE compliance
**Schema:** `governance_ledger.py`

```python
logger.log("governance_ledger", {
    "publish_id": "pub-001",
    "artifact_ids": ["brief-2025-11-11"],
    "contributing_agent_ids": ["summarizer", "qa_reviewer"],
    "verification_hashes": [...],
    ...
})
```

---

## Configuration

### Sampling Rates
```python
logger = StructuredLogger(
    base_dir="./data/research",
    sampling={
        "execution_context": 1.0,      # 100% - always log
        "agent_graph": 1.0,             # 100%
        "boundary_events": 1.0,         # 100%
        "governance_ledger": 1.0,       # 100%
        "reasoning_traces": 0.05,       # 5% - expensive
        "failure_snapshots": 0.05       # 5%
    }
)
```

### Batch Size
```python
logger = StructuredLogger(
    base_dir="./data/research",
    batch_size=100  # Write after 100 records
)
```

---

## Privacy & Sanitization

### For Research Datasets
```python
from rkl_logging import sanitize_for_research

# Hashes sensitive fields, keeps structure
safe_record = sanitize_for_research(record)
```

### For Public Benchmarks
```python
from rkl_logging import anonymize_for_public

# Only structural fields, no content
public_record = anonymize_for_public(record)
```

---

## Directory Structure

```
data/research/
├── execution_context/
│   └── 2025/11/11/
│       ├── execution_context_091523.parquet
│       └── execution_context_101234.parquet
│
├── agent_graph/
│   └── 2025/11/11/
│       └── agent_graph_091523.parquet
│
├── boundary_events/
│   └── 2025/11/11/
│       └── boundary_events_091523.parquet
│
└── governance_ledger/
    └── 2025/11/11/
        └── governance_ledger_100000.parquet

data/manifests/
└── 2025-11-11.json
```

---

## Manifest Format

```json
{
  "date": "2025-11-11",
  "rkl_version": "1.0",
  "artifacts": {
    "execution_context": {
      "rows": 1234,
      "writes": 13,
      "schema_version": "v1.0"
    },
    "agent_graph": {
      "rows": 567,
      "writes": 6,
      "schema_version": "v1.0"
    }
  },
  "generated_at": "2025-11-11T12:00:00Z"
}
```

---

## Integration Example

### In Agent Code

```python
from rkl_logging import StructuredLogger, sha256_text

class SummarizerAgent:
    def __init__(self, logger: StructuredLogger):
        self.logger = logger
        self.agent_id = "summarizer"

    def summarize(self, article, session_id, turn_id):
        # Your summarization logic
        prompt = self.build_prompt(article)
        response = ollama.generate(prompt)

        # Log execution context
        self.logger.log("execution_context", {
            "session_id": session_id,
            "turn_id": turn_id,
            "agent_id": self.agent_id,
            "model_id": "llama3.2:8b",
            "temp": 0.3,
            "ctx_tokens_used": len(prompt.split()),
            "gen_tokens": len(response.split()),
            "tool_lat_ms": response.latency,
            "prompt_id_hash": sha256_text(prompt)
        })

        return response
```

---

## Research Use Cases

### AI Safety Research
- Hallucination detection patterns
- Model reliability across configurations
- Failure mode analysis

### Governance Research
- Type III boundary enforcement effectiveness
- CARE principles implementation
- Audit trail completeness

### Agentic Systems Research
- Multi-agent coordination patterns
- Emergent behaviors
- Quality improvement trajectories

### Prompt Engineering Research
- Prompt evolution effectiveness
- Temperature/top_p impact studies
- Model comparison studies

---

## Performance

- **Async writes** - Non-blocking, ~0.1ms overhead
- **Batching** - Reduces I/O by 100x
- **Parquet compression** - 10x smaller than JSON
- **Date partitioning** - Fast time-range queries

---

## Testing

```python
# Test basic logging
from rkl_logging import StructuredLogger

logger = StructuredLogger(base_dir="./test_data")

logger.log("execution_context", {
    "session_id": "test-1",
    "agent_id": "test_agent",
    "model_id": "llama3.2:1b",
    "timestamp": "2025-11-11T09:00:00Z"
})

logger.close()

# Check output
import pandas as pd
df = pd.read_parquet("./test_data/execution_context/2025/11/11/")
print(df.head())
```

---

## Roadmap

### Phase 0 (Week 1-2) - ✅ DONE
- Execution context
- Agent graph
- Boundary events
- Governance ledger

### Phase 1 (Week 3-6) - Coming Soon
- Secure reasoning traces
- Retrieval provenance
- Quality trajectories

### Phase 2 (Q2 2026) - Planned
- Hallucination matrix
- Failure snapshots
- Human intervention events

---

## License

Apache 2.0 - Open for research and commercial use

## Citation

```bibtex
@software{rkl_logging_2025,
  title={RKL Logging: Research-Grade Telemetry for AI Agentic Systems},
  author={Resonant Knowledge Lab},
  year={2025},
  url={https://github.com/rkl/secure-reasoning-brief}
}
```

---

**Questions?** See [ARCHITECTURE.md](../ARCHITECTURE.md) or contact info@resonantknowledgelab.org
