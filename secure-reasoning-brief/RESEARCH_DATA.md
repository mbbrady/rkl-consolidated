# RKL Research Data Collection

**Turning operational system into landmark AI research datasets**

This document describes how the Secure Reasoning Brief Agent generates research-grade datasets for the AI science community.

---

## Vision

**Transform RKL's operational brief generation into a research platform that advances:**
- AI safety science (hallucination detection, verification)
- Agentic systems (multi-agent coordination)
- Governance implementation (Type III, CARE principles)
- Prompt engineering (evolution under production constraints)

---

## What Makes This Unique

### 1. **Real-World, Not Lab Data**
- Production system, not controlled experiment
- Actual messiness and edge cases
- Emergent behaviors from 18 interacting agents
- Human-AI collaboration in practice

### 2. **Structural Telemetry**
- No raw text = privacy-preserving by design
- SHA-256 hashes for cross-referencing
- Complete provenance without exposure
- Reproducible while protecting sensitive content

### 3. **Type III Demonstration**
- **Proof** that secure reasoning works at scale
- Boundary enforcement logs
- CARE principles in action
- Zero-cost local processing

### 4. **Longitudinal & Multi-Agent**
- Tracks evolution over 52+ weeks
- 18 specialized agents coordinating
- Quality improvement trajectories
- Prompt engineering evolution

---

## Data Collection Architecture

```
Operational System              Research Datasets
─────────────────              ──────────────────

18 Agent Pipeline      →       Phase 0 (Now):
                                - Execution context
Betty Cluster                   - Agent graph
+ Ollama                        - Boundary events
                                - Governance ledger
Type III Compliance
                               Phase 1 (Q1 2026):
Complete Audit Trail            - Reasoning traces
                                - Quality trajectories
                                - Retrieval provenance

                               Phase 2 (Q2 2026):
                                - Hallucination matrix
                                - Failure snapshots
                                - Human interventions
```

---

## Phase 0 Artifacts (Implemented)

### 1. Execution Context & Hyperparameters
**Captures:** Model configs, token usage, latency
**Value:** Compare models, tune hyperparameters, understand costs
**Volume:** ~1K records/brief
**Size:** ~100KB/brief (Parquet)

**Research Questions:**
- How does temperature affect hallucination rates?
- What's the cost/quality tradeoff for different models?
- Where are the performance bottlenecks?

### 2. Multi-Agent Reasoning Graph
**Captures:** Agent-to-agent message passing (structural)
**Value:** Study coordination, identify emergent patterns
**Volume:** ~500 edges/brief
**Size:** ~50KB/brief

**Research Questions:**
- What coordination patterns emerge?
- How do revision loops affect quality?
- Can we predict agent failures from graph topology?

### 3. Type III Boundary Enforcement Log
**Captures:** Compliance checks, violations, enforcement actions
**Value:** Prove secure reasoning works, refine policies
**Volume:** ~50 events/brief
**Size:** ~10KB/brief

**Research Questions:**
- What violations occur in practice?
- How effective are automated boundaries?
- Can we detect attempted breaches?

### 4. Governance Traceability Ledger
**Captures:** Publication events with full provenance
**Value:** Complete audit trail for CARE compliance
**Volume:** 1 record/brief
**Size:** ~2KB/brief

**Research Questions:**
- Is provenance tracking sufficient?
- Can we reconstruct entire pipeline from ledger?
- How do we prove CARE compliance?

---

## Data Volume Estimates

### Per Brief (Weekly)
- Execution context: ~100KB
- Agent graph: ~50KB
- Boundary events: ~10KB
- Governance ledger: ~2KB
- **Total:** ~160KB/brief

### Annual (52 Briefs)
- Total: ~8.3MB/year
- Compressed (Parquet): ~2-3MB/year
- With Phase 1+2: ~50MB/year

**Storage cost: Negligible**

---

## Privacy & Release Tiers

### Tier 1: Internal (Restricted)
- **Access:** RKL staff only
- **Content:** Complete raw data
- **Purpose:** System debugging, improvement
- **Privacy:** Full data, no sanitization

### Tier 2: Research (Upon Request)
- **Access:** Academic researchers
- **Content:** Sanitized (hashed sensitive fields)
- **Purpose:** AI safety/governance research
- **Privacy:** No raw text, structural + hashes

### Tier 3: Public Benchmark (Open)
- **Access:** Anyone
- **Content:** Anonymized (structural only)
- **Purpose:** Model evaluation benchmarks
- **Privacy:** Statistical fields only

---

## Research Use Cases

### For AI Safety Researchers
**Datasets:**
- Hallucination detection in summarization
- Model reliability across configurations
- Failure mode taxonomy

**Papers:**
- "Hallucinations in Governance Domain Summarization"
- "Type III Secure Reasoning: A Year in Production"

### For Agentic Systems Researchers
**Datasets:**
- Multi-agent coordination patterns
- Revision loop effectiveness
- Quality evolution trajectories

**Papers:**
- "Emergent Behaviors in 18-Agent Pipelines"
- "Prompt Engineering Under Production Constraints"

### For Governance Researchers
**Datasets:**
- CARE principles implementation
- Boundary enforcement effectiveness
- Human-AI collaboration patterns

**Papers:**
- "Implementing Indigenous Data Sovereignty in AI Systems"
- "Type III Boundaries: Theory vs. Practice"

### For HCI Researchers
**Datasets:**
- Human intervention patterns
- Quality threshold calibration
- Trust indicators in agent systems

**Papers:**
- "When Do Humans Override AI Agents?"
- "Explainability Requirements for Trustworthy Agents"

---

## Dataset Naming & Versioning

### Naming Convention
```
RKL-SecureReason-{Artifact}-{Version}

Examples:
- RKL-SecureReason-ExecContext-v2025.Q4
- RKL-SecureReason-AgentGraph-v2026.Q1
- RKL-SecureReason-Complete-v2026.Q2
```

### Versioning
- **Quarterly releases**: v2025.Q4, v2026.Q1, etc.
- **Breaking changes**: Major version bump
- **Schema updates**: Documented in manifest

---

## Publication Plan

### Q4 2025 (Now)
- ✅ Implement Phase 0 logging
- ✅ Generate first 4-8 weeks of data
- ✅ Create dataset documentation

### Q1 2026
- Release RKL-SecureReason-v2026.Q1 (research tier)
- Submit to arXiv
- Announce on social media
- Reach out to research groups

### Q2 2026
- Implement Phase 1+2 artifacts
- Release comprehensive dataset
- Submit benchmark to leaderboards
- Publish research paper

### Q3 2026
- First external papers using dataset
- Conference presentations
- Community feedback integration

---

## Expected Impact

### Citation Potential
- **High**: Real-world agentic system data is rare
- **Novel**: Type III secure reasoning proof
- **Valuable**: 18-agent coordination patterns
- **Timely**: Governance frameworks needed now

### Benchmark Potential
- "Evaluated on RKL-SecureReason-ExecContext"
- "Our method improves hallucination detection by 15% on RKL dataset"
- "Validated using RKL-SecureReason boundary enforcement logs"

### Teaching Potential
- Used in AI safety courses
- Governance framework case studies
- Agentic systems tutorials
- Type III implementation guide

---

## Getting Started

### Enable Logging
```python
from rkl_logging import StructuredLogger

logger = StructuredLogger(
    base_dir="./data/research",
    rkl_version="1.0"
)

# In your agent code:
logger.log("execution_context", {
    "session_id": session_id,
    "agent_id": "summarizer",
    "model_id": "llama3.2:8b",
    ...
})
```

### Review Collected Data
```python
import pandas as pd

# Load execution context
df = pd.read_parquet("data/research/execution_context/2025/11/11/")
print(df.describe())

# Check manifest
import json
manifest = json.load(open("data/manifests/2025-11-11.json"))
print(manifest["artifacts"])
```

### Generate Research Release
```bash
# Sanitize for research tier
python scripts/prepare_research_release.py \
  --input data/research/ \
  --output releases/v2026.Q1/ \
  --tier research

# Create public benchmark
python scripts/prepare_research_release.py \
  --input data/research/ \
  --output releases/v2026.Q1-public/ \
  --tier public
```

---

## Contributing

### Suggest New Artifacts
- What data would help your research?
- What's missing from current schema?
- What analysis would you run?

### Share Your Research
- Used RKL data in a paper? Tell us!
- Found interesting patterns? Share insights!
- Built on our datasets? Contribute back!

---

## Resources

- **[rkl_logging/README.md](rkl_logging/README.md)** - Logging package docs
- **[config/logging.yaml](config/logging.yaml)** - Configuration reference
- **[ARCHITECTURE.md](ARCHITECTURE.md)** - System architecture
- **[schemas/](rkl_logging/schemas/)** - All artifact schemas

---

## Contact

**Questions about data:**
- Email: info@resonantknowledgelab.org
- GitHub: [Issue tracker]

**Data requests:**
- Research tier access: Submit proposal
- Custom datasets: Contact us
- Collaborations: Always welcome!

---

**This operational system becomes a research platform that advances the field while demonstrating RKL's methods.**

---

*Last updated: 2025-11-11*
*Version: 1.0*
