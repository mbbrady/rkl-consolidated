# Secure Reasoning Brief - HTML Demo

**Competition Submission Demo** • Kaggle 5-Day AI Agents Intensive Capstone

---

## What's Included

This standalone HTML demo showcases the automated research brief system:

### Files
- **`index.html`** - Overview and system description
- **`daily_briefs.html`** - All daily executive summaries
- **`weekly_synthesis.html`** - Weekly deep analysis with citations

### Features Demonstrated
✅ Multi-agent AI system (18 agents)
✅ Type III compliance (raw data protection)
✅ Daily + weekly briefing formats
✅ IEEE-style academic citations
✅ Phase-0 telemetry integration
✅ RKL professional branding

---

## How to View

### Option 1: Direct File Open
```bash
# Open in browser
open index.html

# Or on Linux
xdg-open index.html
```

### Option 2: Local Web Server
```bash
# Start server
python -m http.server 8000

# Visit in browser
http://localhost:8000
```

### Option 3: Include in Competition Submission
- Zip the entire `demo/` folder
- Include in Kaggle submission package
- Judges can view directly or via local server

---

## What This Demonstrates

### 1. Multi-Agent Architecture
- 18 specialized agents in pipeline
- Feed monitoring → Filtering → Summarization → Analysis
- Local AI (Ollama) + Cloud AI (Gemini) coordination

### 2. Type III Compliance
- Raw data processed locally only
- Cloud APIs receive derived summaries only
- Full governance documentation
- Audit trail in Phase-0 telemetry

### 3. Real-World Application
- Automated research monitoring
- 2x daily collection (9 AM, 9 PM)
- Weekly synthesis (Sunday 10 PM)
- Professional output for practitioners

### 4. Academic Rigor
- IEEE-style citations
- Verifiable claims (all links included)
- Expert synthesis by Gemini
- Transparent methodology

---

## Technical Details

**System:**
- Python 3.11 + cron automation
- Ollama API (llama3.2:3b) for local processing
- Google Gemini API (2.0-flash) for synthesis
- Phase-0 Research Telemetry (4 artifact types)

**Data Sources:**
- ArXiv AI research feed
- AI Alignment Forum
- Google AI Blog

**Processing:**
- ~20 papers per run (2x daily)
- ~280 papers per week
- Type III: Raw content stays local, summaries go to cloud

---

## Files & Structure

```
demo/
├── README.md                 # This file
├── index.html                # Landing page
├── daily_briefs.html         # Daily summaries
└── weekly_synthesis.html     # Weekly analysis
```

All files are self-contained with:
- Embedded CSS (RKL brand colors)
- Embedded fonts (Google Fonts)
- No external dependencies
- Works offline

---

## Competition Evaluation Points

This demo addresses competition requirements:

✅ **Multi-agent system:** 18 agents, coordinated pipeline
✅ **Real-world application:** Research monitoring for practitioners
✅ **Telemetry:** Phase-0 integration with 4 artifact types
✅ **Innovation:** Type III compliance for secure reasoning
✅ **Quality:** Professional output, academic citations
✅ **Automation:** Fully automated 2x daily + weekly
✅ **Documentation:** Complete system description

---

## Next Steps (Post-Competition)

1. **Integration:** Copy to RKL Hugo website
2. **Enhancement:** Add paper tracking and cross-references
3. **Expansion:** Add more data sources
4. **Telemetry:** Implement Phase-1 enhancements
5. **Publication:** Deploy to resonantknowledgelab.org

---

## Contact

**Resonant Knowledge Lab**
- Website: [resonantknowledgelab.org](https://resonantknowledgelab.org)
- Competition: Kaggle 5-Day AI Agents Intensive Capstone
- Submission Date: November 2025

---

*Generated from markdown briefs using RKL brand styling*
