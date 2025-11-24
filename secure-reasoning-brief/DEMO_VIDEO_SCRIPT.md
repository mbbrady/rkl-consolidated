# Demo Video Script - Secure Reasoning Research Brief

**Target Duration:** 3 minutes
**Audience:** Kaggle competition judges
**Tone:** Professional, clear, technically credible

---

## Script Outline

### Opening (0:00 - 0:40) - 40 seconds
**Visual:** Title card with "Mike Brady" + "RKL Secure Reasoning Brief", fade to architecture diagram

**Narration:**
> "Hi, I'm Mike Brady. I work with sensitive research data that can't leave local infrastructure - and I thought others might be in the same boat."
>
> "For the Kaggle AI Agents Capstone, I built an 18-agent system that monitors AI safety papers and generates daily briefs - while demonstrating Type III Secure Reasoning: a framework where raw data never leaves local control, but derived insights can be shared."
>
> "Full transparency: I used AI coding assistants - Claude Code and ChatGPT - to scaffold the implementation. I designed the architecture and telemetry schema; AI helped me build it faster than I could alone."

**On-screen text:**
- "Mike Brady"
- "RKL Secure Reasoning Brief"
- "18 Agents • Type III Secure Reasoning"
- "⚠️ Built with AI assistance"

---

### Problem & Solution (0:40 - 1:00) - 20 seconds
**Visual:** Screen recording showing ArXiv feed scrolling (overwhelming volume of papers)

**Narration:**
> "The problem: AI researchers face 280 papers per week. The solution: automated monitoring with provable security guarantees. Raw articles processed locally; only summaries sent to cloud models for analysis."

**On-screen text:**
- "280 papers/week → Daily 2-min briefs"
- "Local processing • Cloud analysis"

---

### Architecture Overview (1:00 - 1:25) - 25 seconds
**Visual:** Animated Mermaid diagram showing data flow

**Narration:**
> "Our system coordinates 18 specialized agents across four phases: discovery, processing, quality analysis, and publication. Local Ollama agents process raw content. Cloud Gemini agents see only summaries. This is Type III Secure Reasoning: local processing for sensitive data, cloud for analysis."

**On-screen text:**
- "Local: Ollama (raw content)"
- "Cloud: Gemini (summaries only)"
- "Type III: Provable data isolation"

---

### Demo - Daily Brief (1:25 - 1:45) - 20 seconds
**Visual:** Browser showing demo/daily_briefs.html, scroll through a daily brief

**Narration:**
> "The system runs twice daily. Each run produces a 2-3 minute executive brief highlighting breakthrough papers. Here's a morning brief showing 6 papers analyzed, with the top 2 must-reads highlighted."

**On-screen text:**
- "2x daily: 9 AM, 9 PM"
- "2-3 minute read"

---

### Demo - Weekly Synthesis (1:45 - 2:05) - 20 seconds
**Visual:** Browser showing demo/weekly_synthesis.html, scroll to citations section

**Narration:**
> "Every Sunday, a weekly synthesis aggregates the full week of data into a comprehensive analysis with IEEE-style citations. All claims are verifiable, and citations use only public metadata - not raw content - maintaining Type III compliance."

**On-screen text:**
- "Weekly: Sunday 10 PM"
- "IEEE citations"
- "Type III compliant"

---

### Telemetry Proof (2:05 - 2:30) - 25 seconds
**Visual:** Terminal showing:
1. Directory tree of data/research/
2. Quick cat of a governance_ledger file showing JSON with type3_verified: true

**Narration:**
> "How do we prove Type III compliance? Research telemetry. Every agent interaction generates telemetry artifacts - 441 files documenting 9 artifact types. Here's a governance ledger showing explicit verification: raw data exposed: false. This isn't just logging - it's provable compliance."

**On-screen text:**
- "375 telemetry files"
- "9 artifact types"
- "Provable compliance"

---

### Real-World Impact (2:30 - 2:45) - 15 seconds
**Visual:** Split screen: Daily brief on left, weekly blog on right

**Narration:**
> "This system is production-ready. Fully automated via cron, it transforms 280 papers per week into digestible updates. For practitioners: quick daily reads. For researchers: comprehensive analysis."

**On-screen text:**
- "280 papers/week → 2 formats"
- "Production ready"
- "Fully automated"

---

### Closing (2:45 - 3:05) - 20 seconds
**Visual:** Return to title card with RKL branding, show GitHub repo link

**Narration:**
> "Secure Reasoning Research Brief: proving that multi-agent AI systems can deliver real-world value with verifiable security guarantees."
>
> "This is an exploratory prototype built to learn. The deep code understanding will come through continued use. But the architecture works, the telemetry is real, and the transparency is honest. Thank you."

**On-screen text:**
- "Resonant Knowledge Lab"
- "Kaggle Datasets: bradyopenmaps/rkl-secure-reasoning-brief-telemetry"
- "Built with AI assistance • Honest prototype • Real learning"

**Fade to black**

---

## Production Notes

### Timing Breakdown
| Section | Duration | Cumulative |
|---------|----------|------------|
| Opening | 20s | 0:20 |
| Problem | 20s | 0:40 |
| Architecture | 30s | 1:10 |
| Daily Brief Demo | 25s | 1:35 |
| Weekly Synthesis Demo | 20s | 1:55 |
| Telemetry Proof | 30s | 2:25 |
| Impact | 20s | 2:45 |
| Closing | 15s | 3:00 |
| **TOTAL** | **180s** | **3:00** |

### Visual Assets Needed
1. **Title card** - RKL branding (navy/coral)
2. **Architecture diagram** - Mermaid diagram (animated if possible)
3. **Data flow animation** - Show local vs. cloud processing
4. **Screen recordings:**
   - ArXiv feed (for overwhelming volume)
   - demo/index.html (landing page)
   - demo/daily_briefs.html (scroll through one brief)
   - demo/weekly_synthesis.html (scroll to citations)
5. **Terminal recordings:**
   - `tree data/research/ -L 2` (show structure)
   - `cat data/research/governance_ledger/2025/11/22/governance_ledger_090045.parquet | head` (if readable) OR show JSON in text editor
   - `find data/research -name "*.parquet" | wc -l` (show count)
6. **Split screen** - Daily + weekly side-by-side

### Audio Notes
- **Pace:** Clear, moderate speed (not rushed)
- **Emphasis:** Type III compliance, provable, real-world
- **Pauses:** After "this is critical" and before showing telemetry JSON
- **Tone:** Professional but enthusiastic (this solves a real problem)

### Technical Recording Tips
1. **Screen resolution:** 1920x1080 (standard HD)
2. **Browser zoom:** 125% (readable text)
3. **Terminal:** Large font (18pt), high contrast theme
4. **Cursor:** Highlight cursor for screen recordings
5. **Audio:** Use quality microphone, quiet environment
6. **Editing:** Simple cuts, no fancy transitions (professional style)

---

## Detailed Shot List

### Shot 1: Title Card (0:00-0:05)
- Static title card with RKL logo
- Text: "Secure Reasoning Research Brief"
- Subtitle: "Kaggle AI Agents Capstone - November 2025"

### Shot 2: Architecture Diagram (0:05-0:20)
- Show full Mermaid diagram
- Optionally animate: RSS → Monitors → Local → Cloud → Output
- Highlight "Type III" labels

### Shot 3: ArXiv Feed Scroll (0:20-0:30)
- Screen recording: https://arxiv.org/list/cs.AI/recent
- Scroll quickly to show volume
- Optional: Overlay "100+ papers/week" text

### Shot 4: Simplified Flow Diagram (0:30-0:40)
- Show simplified Mermaid flowchart
- Zoom in on "Local Ollama" and "Cloud Gemini"

### Shot 5: Architecture Detail (0:40-1:10)
- Return to detailed architecture diagram
- Highlight each section as narrated:
  - Feed monitors (0:45)
  - Local Ollama (0:52)
  - Cloud Gemini (1:00)
- Show dashed line representing "no raw content crosses here"

### Shot 6: Demo Landing Page (1:10-1:15)
- Open demo/index.html in browser
- Show "Overview" section briefly

### Shot 7: Daily Brief (1:15-1:35)
- Click "Daily Briefs" navigation
- Scroll through 2025-11-22 morning brief
- Pause on "Must Read" section (show 2 papers)
- Scroll to footer (show metadata)

### Shot 8: Weekly Synthesis (1:35-1:50)
- Click "Weekly Synthesis" navigation
- Scroll through introduction
- Pause on a section with inline citations [1], [2]

### Shot 9: Citations (1:50-1:55)
- Scroll to "References" section at bottom
- Show IEEE-style citations with links
- Highlight "Online. Available: URL"

### Shot 10: Terminal - Directory Structure (1:55-2:05)
- Terminal command: `tree data/research/ -L 2 -d`
- Show 9 artifact type directories

### Shot 11: Terminal - Governance Ledger (2:05-2:20)
- Open governance ledger JSON in text editor (easier to read than parquet)
- Highlight:
  ```json
  "type3_verified": true,
  "raw_data_exposed": false,
  "cloud_api_receives": "summaries_only"
  ```
- Hold for 5 seconds (let judges read)

### Shot 12: Terminal - File Count (2:20-2:25)
- Command: `find data/research -name "*.parquet" | wc -l`
- Output: 375

### Shot 13: Split Screen (2:25-2:40)
- Left: Daily brief (scroll slowly)
- Right: Weekly blog (scroll slowly)
- Show contrast in length and depth

### Shot 14: Terminal - Cron (2:40-2:45)
- Command: `crontab -l | grep rkl`
- Show 3 cron lines (morning, evening, weekly)

### Shot 15: Closing Title Card (2:45-3:00)
- Same as opening title card
- Add:
  - "GitHub: [repository link]"
  - "resonantknowledgelab.org"
  - "Thank you"
- Fade to black

---

## Alternative: Screencast + Voice-Over

If recording yourself on camera isn't preferred, this script works perfectly as a **screencast with voice-over**:

1. Record all screen shots separately (easier to re-do if needed)
2. Record voice-over separately (better audio quality)
3. Edit together with simple cuts
4. Add text overlays for key points

**Tools:**
- **Screen recording:** OBS Studio (free, professional)
- **Audio recording:** Audacity (free) or built-in mic app
- **Video editing:** DaVinci Resolve (free), iMovie, or Kdenlive (Linux)

---

## Key Messages to Emphasize

1. **Real problem solved:** Information overload → automated briefs
2. **Type III compliance:** Raw data never leaves local infrastructure
3. **Provable security:** Phase-0 telemetry provides audit trail
4. **Production ready:** 5 days operational, fully automated
5. **Multi-agent coordination:** 18 agents working together
6. **Real-world value:** 280 papers/week → 2 digestible formats

---

## Call to Action (for Judges)

While not explicitly stated in the video, the implicit call to action is:

> "This demonstrates multi-agent systems can be both powerful AND secure. The telemetry proves it. The output validates it. The automation scales it."

---

## Submission Checklist

- [ ] Record all screen shots (estimate: 1-2 hours)
- [ ] Record voice-over (estimate: 30 minutes with retakes)
- [ ] Edit video (estimate: 1-2 hours)
- [ ] Add text overlays (estimate: 30 minutes)
- [ ] Export at 1080p, 30fps (H.264 codec)
- [ ] Keep file size under 100 MB if possible
- [ ] Test playback on different devices
- [ ] Upload to platform specified by competition

**Total estimated production time:** 3-5 hours (depending on experience)

---

## Bonus Points Strategy

Competition offers **+10 bonus points** for demo video. This is significant - potentially difference between top 10 and top 3.

**Why this script will score well:**
1. **Complete coverage** - Shows all key components in 3 minutes
2. **Technical credibility** - Shows actual telemetry files, not just claims
3. **Clear narrative** - Problem → Solution → Proof → Impact
4. **Professional production** - Clean, focused, no fluff
5. **Verifiable claims** - Shows actual system operation

---

*Demo video script for Kaggle 5-Day AI Agents Intensive Capstone Competition*
*Created: November 22, 2025*
