# Demo Video Production Guide

**Target:** 3-minute demo video for Kaggle AI Agents Competition (+10 bonus points)
**Script:** [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)
**Status:** Script complete, recording pending

---

## 📋 Pre-Production Checklist

### Software Requirements

| Tool | Purpose | Recommended |
|------|---------|-------------|
| **Screen Recorder** | Capture browser/terminal | OBS Studio (free), QuickTime, or ScreenFlow |
| **Audio Recorder** | Record voiceover | Audacity (free), GarageBand, or built-in |
| **Video Editor** | Combine clips | DaVinci Resolve (free), iMovie, or Premiere |
| **Browser** | Demo HTML files | Chrome/Firefox (latest) |
| **Terminal** | Show telemetry | Terminal.app, iTerm2, or similar |

### Visual Assets Checklist

- ✅ Title card needed (RKL branding - navy/coral colors)
- ✅ Architecture diagram ready: [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md)
- ✅ HTML demos ready: [demo/](demo/)
  - ✅ index.html (landing page)
  - ✅ daily_briefs.html (daily brief example)
  - ✅ weekly_synthesis.html (weekly synthesis)
- ✅ Telemetry data available: `data/research/`
- ✅ Script ready: [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)

---

## 🎬 Recording Plan

### Session 1: Visual Recordings (30-45 minutes)

#### 1. Title Card (5 minutes)
```bash
# Create simple title card in PowerPoint/Keynote:
# - Navy background (#1a2332)
# - Coral accent (#ff6b6b)
# - Title: "Secure Reasoning Research Brief"
# - Subtitle: "18 Agents • Type III Compliance • Phase-0 Telemetry"
# - RKL logo or text
# Export as PNG/JPG
```

#### 2. Architecture Diagram (10 minutes)
- Open [ARCHITECTURE_DIAGRAM.md](ARCHITECTURE_DIAGRAM.md) in VS Code with Mermaid preview
- OR: Use https://mermaid.live to render diagram
- Screen record 10-15 seconds of diagram display
- Optional: Add simple animation (pan/zoom)

#### 3. Browser Screen Recordings (15 minutes)

**Recording A: Landing Page (5s)**
```bash
# Open demo/index.html in browser
# Record: Fade in, pause 5 seconds on landing page
```

**Recording B: Daily Brief (30s)**
```bash
# Open demo/daily_briefs.html
# Record: Smooth scroll through one complete daily brief
# Timing: 25 seconds (as per script 1:10-1:35)
```

**Recording C: Weekly Synthesis (25s)**
```bash
# Open demo/weekly_synthesis.html
# Record: Scroll through synthesis, pause on citations section
# Timing: 20 seconds (as per script 1:35-1:55)
```

#### 4. Terminal Recordings (15 minutes)

**Recording D: Telemetry Structure (10s)**
```bash
# Set terminal to readable font size (14-16pt)
# Run: tree data/research/ -L 2
# Record: Show directory structure clearly
```

**Recording E: Governance Ledger (15s)**
```bash
# Run: cat data/research/governance_ledger/2025/11/21/governance_ledger_090045.parquet | head -20
# OR use Python to pretty-print:
python3 -c "
import pandas as pd
df = pd.read_parquet('data/research/governance_ledger/2025/11/21/governance_ledger_090045.parquet')
print(df.head(1).to_json(indent=2))
"
# Record: Show JSON with type3_verified field
# Pause 5 seconds to let judges read
```

**Recording F: File Count (5s)**
```bash
# Run: find data/research -name '*.parquet' | wc -l
# Show: 375 files (or current count)
```

### Session 2: Voiceover Recording (20-30 minutes)

#### Setup
1. Find quiet environment (close doors/windows)
2. Use quality microphone (headset or USB mic better than laptop mic)
3. Test audio levels (aim for -12dB to -6dB peak)
4. Have water nearby (prevent mouth clicks)

#### Recording Tips
- **Pace:** Slightly slower than normal conversation
- **Pauses:** Add 1-2 second pauses between sections for editing
- **Retakes:** Record each section 2-3 times, pick best
- **Energy:** Stay engaged, this is your competition submission!

#### Script Sections to Record
Follow [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md):

1. **Opening** (20s) - Lines 14-15
2. **Problem** (20s) - Lines 26-27
3. **Architecture** (30s) - Lines 38-43
4. **Daily Brief** (25s) - Lines 56-57
5. **Weekly Synthesis** (20s) - Lines 68-69
6. **Telemetry** (30s) - Lines 84-88
7. **Impact** (20s) - Lines 101-102
8. **Closing** (15s) - Lines 114-115

**Total narration:** ~180 seconds (3 minutes)

#### Audio Processing (Optional)
- Remove background noise (Audacity: Effect > Noise Reduction)
- Normalize audio levels (Effect > Normalize)
- Add slight compression for consistency
- Export as WAV or high-quality MP3

---

## 🎞️ Post-Production: Video Editing

### Timeline Structure (3:00 total)

| Time | Section | Visual | Audio |
|------|---------|--------|-------|
| 0:00-0:20 | Opening | Title card → Architecture diagram | Voiceover 1 |
| 0:20-0:40 | Problem | ArXiv scroll OR continue diagram | Voiceover 2 |
| 0:40-1:10 | Architecture | Animated diagram with labels | Voiceover 3 |
| 1:10-1:35 | Daily Demo | Browser: daily_briefs.html | Voiceover 4 |
| 1:35-1:55 | Weekly Demo | Browser: weekly_synthesis.html | Voiceover 5 |
| 1:55-2:25 | Telemetry | Terminal: tree + JSON + count | Voiceover 6 |
| 2:25-2:45 | Impact | Split screen: Daily + Weekly | Voiceover 7 |
| 2:45-3:00 | Closing | Title card with links | Voiceover 8 |

### Editing Checklist

#### Visual Elements
- ✅ Sync voiceover to visuals
- ✅ Add on-screen text overlays (as per script)
- ✅ Smooth transitions between sections (1-2s fades)
- ✅ Ensure all text is readable (14pt+ font size)
- ✅ Highlight key elements (arrows/boxes on telemetry JSON)

#### Audio Elements
- ✅ Remove long pauses/mistakes
- ✅ Consistent audio levels throughout
- ✅ Optional: Add subtle background music (very low volume)
- ✅ Ensure narration is clear and professional

#### Final Polish
- ✅ Add title safe margins (10% from edges)
- ✅ Export at 1920x1080 (1080p) or 1280x720 (720p)
- ✅ Export at 30fps or 60fps
- ✅ H.264 codec for compatibility
- ✅ Final file size: Aim for < 100 MB

---

## 📤 Export Settings

### Recommended Export Settings

**Resolution:** 1920x1080 (1080p)
**Frame Rate:** 30 fps
**Format:** MP4 (H.264)
**Bitrate:** 5-10 Mbps (VBR)
**Audio:** AAC, 192 kbps, 48 kHz stereo
**Total Duration:** Exactly 3:00 (180 seconds)
**File Size Target:** 50-100 MB

### Quality Check Before Upload
- ✅ Play video start to finish (no glitches)
- ✅ Audio and video in sync
- ✅ All text overlays visible and readable
- ✅ Volume levels consistent
- ✅ No awkward cuts or jumps
- ✅ Timing matches script (3:00 exactly)

---

## 📊 Effort Estimate

| Phase | Time Estimate | Difficulty |
|-------|---------------|------------|
| Asset preparation | 30 minutes | Easy |
| Screen recordings | 45 minutes | Easy |
| Voiceover recording | 30 minutes | Medium |
| Video editing | 2-3 hours | Medium-Hard |
| Review & revisions | 30 minutes | Easy |
| **TOTAL** | **4-5 hours** | **Medium** |

**Worth it?** +10 bonus points for ~4-5 hours of work

---

## 🎯 Quick Start: Minimal Version

If time is limited, create a simpler version:

### Minimal Recording (2 hours)

1. **Use slides instead of live recordings** (30 min)
   - Screenshot each demo page
   - Screenshot terminal outputs
   - Create 8-10 slides in PowerPoint/Keynote

2. **Record slide show with voiceover** (30 min)
   - Use Zoom/Meet "Record" feature
   - Share screen with slides
   - Read script while advancing slides
   - Automatic sync!

3. **Basic editing** (1 hour)
   - Trim beginning/end
   - Add title card
   - Export

This approach is **much faster** and still worth +10 points.

---

## 📝 Upload Instructions

### Where to Upload

**Option 1: YouTube** (Recommended)
- Upload as "Unlisted" (not public, only those with link)
- Add to video description:
  - "Kaggle AI Agents Capstone Competition Submission"
  - Link to GitHub repository
  - Brief description

**Option 2: Kaggle**
- Upload directly if platform supports it
- Check competition submission guidelines

**Option 3: Google Drive / Dropbox**
- Upload video file
- Set sharing to "Anyone with link can view"
- Add link to README.md and SUBMISSION_PACKAGE.md

### Add Link to Repository

After uploading, add video link to:
- **README.md** (top section)
- **COMPETITION_SUBMISSION.md** (at end)
- **SUBMISSION_PACKAGE.md** (in checklist)

Example:
```markdown
**🎥 Demo Video:** [3-minute walkthrough](https://youtube.com/watch?v=...)
```

---

## ✅ Final Checklist

### Pre-Recording
- [ ] Read script out loud 2-3 times (practice)
- [ ] Test screen recording software
- [ ] Test microphone audio quality
- [ ] Open all demo files in browser
- [ ] Prepare terminal commands

### Recording
- [ ] Record title card
- [ ] Record architecture diagram
- [ ] Record browser demos (3 clips)
- [ ] Record terminal outputs (3 clips)
- [ ] Record voiceover (8 sections)

### Editing
- [ ] Import all clips and audio
- [ ] Sync audio to visuals
- [ ] Add on-screen text overlays
- [ ] Add transitions
- [ ] Review timing (3:00 exactly)
- [ ] Export at high quality

### Submission
- [ ] Upload to hosting platform
- [ ] Test video plays correctly
- [ ] Add link to README.md
- [ ] Add link to COMPETITION_SUBMISSION.md
- [ ] Add link to SUBMISSION_PACKAGE.md
- [ ] Update SUBMISSION_PACKAGE.md status (pending → complete)

---

## 🎬 When to Record

### Recommended Timeline

**Option A: Record Now (Nov 22-23)**
- Pros: Have video ready early, can refine before submission
- Cons: Won't include Sunday's weekly blog data

**Option B: Record After Weekly Blog (Nov 25-26)**
- Pros: Can show fresh weekly blog in demo
- Cons: Less time before Nov 30 deadline

**Option C: Skip Video**
- Pros: Save 4-5 hours
- Cons: Miss +10 bonus points

**Recommendation:** **Option B** - Wait for Sunday's weekly blog (Nov 24), then record video Nov 25-26. This gives the freshest demo content while leaving time for submission.

---

## 🚀 Next Steps

1. **Today (Nov 22):** Review this guide, test recording software
2. **Sunday (Nov 24):** Wait for automated weekly blog generation
3. **Monday (Nov 25):** Record screen captures and voiceover
4. **Tuesday (Nov 26):** Edit video and upload
5. **Wednesday (Nov 27-29):** Buffer for revisions if needed
6. **Saturday (Nov 30):** Final submission to Kaggle

**Status:** Script complete, production guide ready, awaiting weekly blog for fresh demo content.

---

*Generated with [Claude Code](https://claude.com/claude-code)*
*Last Updated: November 22, 2025*
