# RKL Secure Reasoning Brief Agent

**Type III Secure Reasoning in Practice: CARE-Enabled Insight Exchange**

A comprehensive multi-agent system that generates weekly briefs on AI governance while demonstrating, auditing, and teaching secure reasoning principles.

---

## Quick Links

- 📐 **[Architecture Documentation](ARCHITECTURE.md)** - Complete system design
- 🔧 **[Agent Configurations](config/agents/)** - Individual agent settings
- 📊 **[Published Briefs](../website/content/briefs/)** - Weekly outputs
- 🔍 **[Transparency Reports](public/transparency/)** - Public compliance data
- 📚 **[Educational Content](public/education/)** - Teaching materials

---

## Session Summary – RKL Phase-0 Telemetry Sprint

### Critical Issues and Status
1. **Worker Node Sleep Problem (BLOCKER → LOCKED AWAKE)**  
   - Work node now has `/etc/systemd/logind.conf.d/no-suspend.conf`, `sleep.target`/`suspend.target`/`suspend-idle.timer` are masked, and the keep-awake script ran—box stays awake until we restore sleep.  
   - When sprint ends, follow `cluster/management/RESTORE_SLEEP.md` to remove the override, unmask the units, and re-enable timers.
2. **Empty Summaries (PARTIALLY FIXED)**  
   - Articles 1–17 now have valid `technical_summary` and `lay_explanation` fields (e.g., Article 1: 556/613 chars).  
   - Articles 18–20 are empty because the worker slept mid-run and `generate()` swallows errors while the pipeline exits with code 0.  
   - `conda run -n rkl-briefs python scripts/fetch_and_summarize.py` succeeds locally, but this sandbox lacks outbound network so RSS pulls return zero rows—rerun the command on the worker itself to refill Articles 18–20.  
   - `scripts/fetch_and_summarize.py` now fails loudly (exit 1) if any article returns an empty technical or lay summary, so bad runs no longer produce “success” JSON.  
   - **Remaining:** Re-run the last 3 articles on the worker to replace Article 18–20 blanks (pipeline will enforce the checks automatically).
3. **Gemini Integration (PARTIAL - QA hook present, needs API key to run)**  
   - `scripts/fetch_and_summarize.py` now has an optional Gemini QA/verdict hook (logs to `hallucination_matrix`) gated by `ENABLE_GEMINI_QA` and `GOOGLE_API_KEY`.  
   - To fully enable, set `ENABLE_GEMINI_QA=true` and a valid Google key; deeper integration pass planned after automation is stable.
4. **Cron Automation (READY BUT UNVERIFIED)**  
   - Two jobs are configured (9:00 and 21:00) via `scripts/cron_pipeline_wrapper.sh`, targeting conda env `rkl-briefs` with logs under `logs/cron/`.  
   - Once the worker stays awake, run `crontab -l | grep rkl-phase0` and exercise a full automated cycle while tailing logs.

### What Currently Works
- Telemetry: manifest generation (with merge fix), partitioned Parquet, four artifact types logged, schema health check passes.  
- Article ingestion: RSS feeds (ArXiv AI, ArXiv Crypto, AI Alignment Forum) collect 50 articles, pipeline processes 20/run with metadata captured.  
- Summary generation (worker awake): Ollama endpoint `http://192.168.1.11:11434/api/generate` with `llama3.2:3b`, ~35–40 seconds/article; Articles 1–17 confirmed.

### Critical Next Steps (Priority Order)
1. **Keep the worker awake:** physical wake + `logind` override + 15-minute stability test.  
2. **Finish the current brief:** re-run Articles 18–20 and validate `/home/mike/project/rkl-consolidated/secure-reasoning-brief/content/briefs/2025-11-17_articles.json`.  
3. **Fail loudly on empty summaries:** update pipeline to exit non-zero when summaries are missing or counts fall below threshold.  
4. **Integrate Gemini:** define QA role, wire `scripts/gemini_client.py`, and document behavior for competition scoring.  
5. **Test cron automation:** verify both daily runs, monitor logs, and target 20–30 sessions (Nov 18–26) for 200+ execution records.

### Files Touched This Session
- Created: `cluster/management/scripts/force-awake-worker.sh`, `cluster/management/scripts/setup_cron.sh`, `rkl-consolidated/secure-reasoning-brief/scripts/cron_pipeline_wrapper.sh`.  
- Existing helpers still relevant: `scripts/health_check.py`, `scripts/fix_manifest.py`, `rkl_logging/structured_logger.py`, `cluster/management/scripts/disable-sleep-for-sprint.sh`, `cluster/management/scripts/restore-sleep-after-sprint.sh`.

### Lessons Learned
- Do not celebrate output until logs are grep’d for `error|failed|exception` **and** content spot-checks pass.  
- Treat automation as downstream of core reliability—pause and fix blockers before celebrating.  
- Wait for explicit “done” confirmation; no more trophy emojis until the summaries exist.

### Competition Status (13 Days to 2025‑12‑01 Deadline)
- ✅ 18-agent system, Phase-0 telemetry, manifest merge fix, competition-grade health check.  
- ⚠️ Summary generation works but depends on worker stability.  
- ❌ Outstanding: Gemini integration, cron validation, 20+ operational sessions, architecture diagram, documentation (<1500 words), demo video (+10 bonus). Immediate blocker remains the sleepy worker.

---

## What This System Does

### 1. **Operational**: Generates Weekly Briefs
Automatically monitors AI research feeds, summarizes developments, and publishes insights for organizational leaders.

### 2. **Demonstrational**: Proves Type III Secure Reasoning
Shows how organizations can process sensitive/governed data locally while publishing derived insights publicly.

### 3. **Educational**: Creates Teaching Materials
Generates case studies, tutorials, and transparency reports from operational data for community education.

### 4. **Auditable**: Maintains Complete Governance Records
Full audit trail demonstrates CARE principles and Type III compliance in practice.

---

## Type III Secure Reasoning Explained

| Type | Description | This System |
|------|-------------|-------------|
| **Type I** | Private Reasoning - Nothing leaves | ❌ |
| **Type II** | Open Knowledge Sharing - Everything open | ❌ |
| **Type III** | **CARE-Enabled Insight Exchange** - Insights travel, data stays | ✅ **YES** |

### What Type III Means Here:

**Stays Local (Never Published):**
- Raw RSS feed content
- Full article text
- Intermediate processing files
- Individual agent logs
- Complete audit trails

**Published (Derived Insights Only):**
- Weekly briefs with summaries
- Theme analysis
- Recommendations
- Aggregated metrics (anonymized)
- Case studies (anonymized)

**This demonstrates how organizations can:**
- Process governed data locally
- Apply AI reasoning safely
- Share insights publicly
- Maintain complete control
- Prove compliance

---

## System Architecture

```
18 Specialized Agents in 6 Groups:

📡 Discovery (3)        → Collect & filter articles
⚙️  Processing (6)       → Summarize, analyze, synthesize
✅ Governance (3)        → QA, compliance, fact-checking
📤 Publishing (3)        → Format, publish, archive
📊 Monitoring (2)        → Performance & audit tracking
📚 Education (1)         → Generate teaching content

All coordinated by MCP-based Orchestrator
```

See [**ARCHITECTURE.md**](ARCHITECTURE.md) for complete details.

---

## Quick Start

### Prerequisites

```bash
# Required
- Python 3.8+
- Ollama running on Betty cluster (192.168.1.10:11434)
- Git
- Hugo (optional, for local testing)

# Recommended models
ollama pull llama3.2:1b    # Fast agents
ollama pull llama3.2:8b    # Core agents
ollama pull llama3.2:70b   # Critical QA/fact-checking
```

### Installation

```bash
# 1. Navigate to project
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief

# 2. Create Python environment
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# 3. Configure environment
cp .env.example .env
# Edit .env if needed (defaults point to Betty)

# 4. Create logs directory
mkdir -p data/logs

# 5. Verify Ollama connectivity
curl http://192.168.1.10:11434/api/tags

# 6. Test feed collection (Phase 1.0)
python scripts/fetch_and_summarize.py
```

### Generate Your First Brief

```bash
# Phase 1.0 (Simple - Working Now)
source venv/bin/activate
python scripts/fetch_and_summarize.py  # Step 1: Collect & summarize
python scripts/publish_brief.py         # Step 2: Generate & publish

# Phase 1.5 (Full MCP - Coming Soon)
python scripts/orchestrator.py --workflow weekly-brief

# Phase 2.0 (ADK - Future)
adk run secure-reasoning-brief
```

---

## Configuration

All agents are configurable via YAML files in [`config/agents/`](config/agents/):

### Example: Fine-Tune the Summarizer

```yaml
# config/agents/summarizer.yaml
model:
  primary: "llama3.2:8b"
  temperature: 0.3

prompts:
  technical_summary:
    parameters:
      max_words: 80  # Adjust word limit
      temperature: 0.3  # Adjust creativity
```

### Example: Adjust QA Thresholds

```yaml
# config/agents/qa_reviewer.yaml
thresholds:
  pass_score: 7.0  # Minimum quality score
  max_iterations: 3  # Revision attempts

quality_rubric:
  content_quality:
    weight: 0.30  # Adjust category weights
```

**See individual agent configs for all tunable parameters.**

---

## Phased Development

### Phase 1.0: Simplified Python (Current)
**Status:** ✅ Ready to use
**Tech:** Python scripts + Cron
**Cost:** $0/month

```bash
# Run manually
python scripts/fetch_and_summarize.py
python scripts/publish_brief.py

# Or via cron (weekly)
0 9 * * 1 cd /path/to/brief && /path/to/venv/bin/python scripts/fetch_and_summarize.py && /path/to/venv/bin/python scripts/publish_brief.py
```

### Phase 1.5: Full MCP Implementation (Next)
**Status:** 🚧 In design
**Tech:** MCP agents + Python orchestrator
**Cost:** $0/month

**Features:**
- 18 specialized MCP servers
- Agent-to-agent communication
- Parallel processing
- Real-time monitoring
- Enhanced audit trails

### Phase 2.0: ADK + Cloud Orchestration (Future)
**Status:** 📋 Planned
**Tech:** Google ADK + Betty cluster
**Cost:** ~$5-15/month

**Features:**
- Cloud-based scheduling
- Better observability
- Multi-brief support
- Federated Type III

---

## Directory Structure

```
secure-reasoning-brief/
├── README.md                    # This file
├── ARCHITECTURE.md              # Complete system design
├── requirements.txt             # Python dependencies
├── .env.example                 # Configuration template
│
├── config/                      # Agent configurations
│   ├── agents/                  # Per-agent YAML (18 agents)
│   ├── governance/              # Type III compliance rules
│   ├── orchestration/           # Workflow coordination
│   └── audit/                   # Audit policies
│
├── scripts/                     # Agent implementations
│   ├── fetch_and_summarize.py  # Phase 1.0: Simplified
│   ├── publish_brief.py         # Phase 1.0: Simplified
│   └── orchestrator.py          # Phase 1.5: Full MCP (coming)
│
├── data/                        # INTERNAL - Never published
│   ├── raw/                     # RSS feed cache
│   ├── intermediate/            # Processing artifacts
│   └── logs/                    # Complete execution logs
│       ├── agent_traces/        # Individual agent logs
│       ├── ollama_calls/        # Model API calls
│       └── governance_events/   # CARE compliance events
│
├── telemetry/                   # INTERNAL - Metrics
│   ├── metrics/                 # Time-series data
│   ├── performance/             # Agent performance
│   └── quality/                 # QA scores
│
├── audit/                       # INTERNAL - Compliance
│   ├── reports/                 # Full audit reports
│   ├── compliance/              # Type III verification
│   └── data_flow/               # Provenance tracking
│
└── public/                      # EXTERNAL - Publishable
    ├── transparency/            # Public compliance reports
    │   ├── monthly-reports/     # Type III compliance
    │   ├── case-studies/        # Teaching examples
    │   └── metrics/             # Aggregated analytics
    ├── education/               # Teaching materials
    │   ├── tutorials/           # How-to guides
    │   ├── demonstrations/      # Interactive demos
    │   └── best-practices/      # Extracted patterns
    └── architecture/            # System documentation
```

**Hugo Integration:**
```
../website/content/briefs/      # Published weekly briefs
```

---

## Agent Roster (18 Agents)

### Discovery Agents
- **A. Feed Monitor** - Watch RSS feeds
- **B. Content Filter** - Pre-filter articles
- **C. Source Credibility** - Assess reliability

### Processing Agents
- **D. Technical Summarizer** - Generate summaries
- **E. Translation Agent** - Convert to lay language
- **F. Metadata Extractor** - Extract tags/themes
- **G. Relationship Analyzer** - Find connections
- **H. Theme Synthesizer** - Weekly patterns
- **I. Recommendation Generator** - Action items

### Governance Agents
- **J. QA Reviewer** - Quality assurance
- **K. Terminology Compliance** - RKL standards
- **L. Fact Checker** - Verify claims

### Publishing Agents
- **M. Brief Composer** - Assemble final brief
- **N. Git Publisher** - Commit & push
- **O. Archive Manager** - Historical archives

### Monitoring Agents
- **P. Performance Monitor** - System health
- **Q. Governance Auditor** - Compliance tracking

### Education Agent
- **R. Education Content Generator** - Teaching materials

**Each agent is independently configurable!**

---

## Cost Analysis

### Phase 1.0 & 1.5: $0/month
| Component | Provider | Cost |
|-----------|----------|------|
| Compute | Betty cluster (local) | $0 |
| AI Models | Ollama (Llama, Mistral) | $0 |
| Hosting | Netlify (free tier) | $0 |
| Storage | Local + GitHub | $0 |
| **Total** | | **$0** |

**Electricity:** ~$5-10/month (amortized across all cluster services)

### Phase 2.0: ~$5-15/month
| Component | Cost |
|-----------|------|
| Google ADK orchestration | $5-10 |
| All processing (still local) | $0 |
| **Total** | **$5-15** |

---

## Type III Compliance & CARE Principles

### Type III Boundaries

```
PUBLIC SOURCES          LOCAL PROCESSING          PUBLIC OUTPUTS
──────────────          ────────────────          ──────────────

RSS Feeds               • 18 Agents                Weekly Briefs
ArXiv                   • Ollama (local)           Transparency Reports
Research Blogs          • Full audit               Case Studies
                        • Governance checks        Metrics Dashboard

[Public Domain]         [Local Control]            [Derived Insights]
                        NEVER PUBLISHED
```

### CARE Principles Implementation

| Principle | Implementation | Verification |
|-----------|---------------|--------------|
| **Collective Benefit** | Insights shared publicly | Briefs freely available |
| **Authority to Control** | All processing local | 100% Betty cluster |
| **Responsibility** | Full audit trail | Complete lineage tracking |
| **Ethics** | Transparent methods | Open documentation |

### Monthly Compliance Reporting

Automated reports published at [`public/transparency/monthly-reports/`](public/transparency/monthly-reports/):
- Type III boundary verification
- CARE principles adherence
- Data flow audit summary
- Agent performance metrics
- Quality assurance statistics

---

## Educational Outputs

This system generates teaching materials for:

### RKL Internal Use
- **MCP Training** - Real agent-to-agent examples
- **Governance Workshops** - Audit logs for teaching
- **Type III Demos** - Working implementation

### External Community
- **Case Studies** - Anonymized decision examples
- **Tutorials** - How to build secure reasoning systems
- **Best Practices** - Extracted from operational data
- **Metrics Dashboards** - Public transparency

### Academic Research
- **Aggregated Data** - For research papers
- **Architecture Patterns** - Reusable designs
- **Compliance Methods** - Governance techniques

---

## Troubleshooting

### Ollama Connection Issues
```bash
# Check Betty head node
curl http://192.168.1.10:11434/api/tags

# Wake cluster if needed
/home/mike/project/cluster/management/scripts/wake-cluster.sh

# Check Ollama service
ssh mike-serv@192.168.1.10 'systemctl status ollama'
```

### No Articles Found
- Check `config/feeds.json` keywords aren't too restrictive
- Verify RSS feeds are accessible
- Review `BRIEF_MAX_ARTICLES` in `.env`
- Check logs in `data/logs/`

### Quality Issues
- Review QA scores in `telemetry/quality/scores.jsonl`
- Adjust thresholds in `config/agents/qa_reviewer.yaml`
- Check agent configs for prompt tuning

### Git Publishing Fails
- Verify git repository status
- Check credentials configured
- Review logs in `data/logs/git/`

---

## Development Roadmap

### Q4 2025 (Current)
- ✅ Phase 1.0 implementation
- ✅ Complete documentation
- 🚧 First production brief
- 🚧 Initial transparency report

### Q1 2026
- Phase 1.5: Full MCP implementation
- 18 specialized MCP servers
- Real-time monitoring dashboard
- Interactive education demos

### Q2 2026
- Phase 2.0: ADK integration
- Cloud orchestration
- Multi-brief support
- Federated Type III pilots

### Q3 2026
- Custom fine-tuned models
- Multi-language support
- Advanced knowledge graphs
- Automated research publications

---

## Contributing

This project demonstrates RKL's open methods for secure reasoning.

**Ways to Contribute:**
- **Feed Sources** - Suggest new RSS feeds
- **Keywords** - Propose governance-relevant terms
- **Agent Configs** - Share improved prompts
- **Case Studies** - Submit anonymized examples
- **Code** - Improve MCP implementations

**Process:**
1. Fork repository
2. Create feature branch
3. Test changes
4. Submit pull request
5. Include audit/compliance notes

---

## License & Attribution

**Resonant Knowledge Lab (RKL)** - Secure reasoning. Local control.

All briefs and educational content include transparent attribution and provenance consistent with CARE Principles.

**Generated Content Attribution:**
- Agent-generated briefs include generation metadata
- Transparency reports show data sources
- Case studies are anonymized appropriately
- All operational data maintains full lineage

**Contact:** info@resonantknowledgelab.org

---

## Technical Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| **Core** | Python 3.8+ | Agent implementation |
| **AI** | Ollama | Local LLM inference |
| **Models** | Llama 3.2, Mistral | Open-source reasoning |
| **Protocol** | MCP (Phase 1.5+) | Agent communication |
| **Publishing** | Hugo | Static site generation |
| **Deployment** | Netlify | Auto-deploy on push |
| **Version Control** | Git | Code & brief tracking |
| **Scheduling** | Cron / ADK | Automated execution |
| **Config** | YAML | Agent settings |
| **Data** | JSON/JSONL | Interchange & logs |

---

## Acknowledgments

This project builds on:
- **CARE Principles** - Indigenous data governance framework
- **Model Context Protocol (MCP)** - Anthropic's agent communication standard
- **Google ADK** - Agent orchestration toolkit (Phase 2.0)
- **Hugo** - Fast static site generator
- **Ollama** - Local LLM infrastructure

Special thanks to the open-source AI community.

---

## Quick Reference

```bash
# Generate brief (Phase 1.0)
python scripts/fetch_and_summarize.py && python scripts/publish_brief.py

# View agent configs
ls config/agents/

# Check audit logs
less data/logs/governance_events/type3_compliance.jsonl

# View telemetry
less telemetry/metrics/pipeline_latest.jsonl

# Test Ollama
curl http://192.168.1.10:11434/api/tags

# Wake Betty cluster
/home/mike/project/cluster/management/scripts/wake-cluster.sh
```

---

**Version:** 1.0
**Last Updated:** 2025-11-11
**Status:** Phase 1.0 Ready for Production

**Next Steps:** Generate first brief, publish transparency report, create first case study.

---

*This README is maintained as living documentation and updated with each phase.*
