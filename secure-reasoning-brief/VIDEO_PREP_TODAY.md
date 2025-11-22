# Video Prep - Today & Tomorrow Plan

**REVISED PLAN:**
- **Today (Nov 22):** Review script, test audio setup
- **Tomorrow (Nov 23):** Record voiceover BEFORE travel (30-45 min)
- **While traveling:** Silent screen recordings and editing (can do anywhere)

This is the BETTER approach - get audio done in good environment first!

---

## ✅ Tasks You Can Do Today (No Audio Needed)

### 1. Screen Recordings (Silent - 30 min)

These don't need audio, just capture the visuals:

#### Recording A: Demo Landing Page
```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
# Open in browser
firefox demo/index.html
# Or: open demo/index.html (Mac)
# Or: xdg-open demo/index.html (Linux)

# Record 5-10 seconds: fade in, hold on page
```

#### Recording B: Daily Brief Demo
```bash
# Open daily briefs
firefox demo/daily_briefs.html

# Record 30 seconds: smooth scroll through one complete brief
# Practice the scroll a few times first to get smooth motion
```

#### Recording C: Weekly Synthesis Demo
```bash
# Open weekly synthesis
firefox demo/weekly_synthesis.html

# Record 25 seconds: scroll through, pause on citations section
```

#### Recording D: ArXiv Feed (Optional)
```bash
# Open ArXiv AI in browser
firefox https://arxiv.org/list/cs.AI/recent

# Record 10 seconds: scroll to show volume of papers
# This is for the "Problem Statement" section
```

### 2. Terminal Recordings (Silent - 20 min)

#### Recording E: Telemetry Directory Structure
```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief

# Set terminal to large, readable font (16pt+)
# Record this command:
tree data/research/ -L 2

# If tree not installed:
find data/research -maxdepth 2 -type d | sort
```

#### Recording F: Governance Ledger JSON
```bash
# Pretty-print a governance ledger file
python3 << 'EOF'
import pandas as pd
import json

# Read one governance ledger file
df = pd.read_parquet('data/research/governance_ledger/2025/11/21/governance_ledger_090045.parquet')

# Show first row as formatted JSON
row = df.iloc[0].to_dict()
print(json.dumps(row, indent=2, default=str))
EOF

# Record: Show JSON output, pause 5 seconds on screen
# Make sure "type3_verified": true is visible
```

#### Recording G: File Count
```bash
# Simple file count
find data/research -name '*.parquet' | wc -l

# Record: Show the number (should be 375 or similar)
```

### 3. Create Title Card (15 min)

**Option A: PowerPoint/Keynote**
```
1. Create new slide (16:9 aspect ratio)
2. Background: Navy (#1a2332)
3. Add text:
   - Main title: "Secure Reasoning Research Brief"
   - Subtitle: "18 Agents • Type III Compliance • Phase-0 Telemetry"
4. Add RKL branding/logo if available
5. Export as PNG (1920x1080)
```

**Option B: Simple Image Editor**
```bash
# Use GIMP, Photoshop, or even Google Slides
# Same colors and text as above
# Export as title_card.png
```

### 4. Screenshot Architecture Diagram (10 min)

```bash
# Option A: Render Mermaid diagram online
# 1. Open https://mermaid.live
# 2. Copy diagram from ARCHITECTURE_DIAGRAM.md
# 3. Paste into editor
# 4. Take screenshot or export PNG

# Option B: VS Code with Mermaid extension
# 1. Open ARCHITECTURE_DIAGRAM.md in VS Code
# 2. Use Mermaid preview
# 3. Take screenshot
```

---

## 📁 Organize Your Recordings

Create a folder structure:

```bash
mkdir -p ~/video_assets/recordings
mkdir -p ~/video_assets/images

# Move recordings here:
# ~/video_assets/recordings/01_landing_page.mov
# ~/video_assets/recordings/02_daily_brief.mov
# ~/video_assets/recordings/03_weekly_synthesis.mov
# ~/video_assets/recordings/04_arxiv_feed.mov (optional)
# ~/video_assets/recordings/05_telemetry_tree.mov
# ~/video_assets/recordings/06_governance_json.mov
# ~/video_assets/recordings/07_file_count.mov

# Images:
# ~/video_assets/images/title_card.png
# ~/video_assets/images/architecture_diagram.png
```

---

## 🎙️ Voiceover - Save for Later

**When:** When you're back in a quiet environment with good audio setup

**What to bring:**
- Headset or USB microphone (better than laptop mic)
- Copy of [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)
- Audacity or recording app installed

**Time needed:** 30-45 minutes
- Read through script 2-3 times (10 min)
- Record all 8 sections (20 min)
- Review and re-record any mistakes (10-15 min)

---

## 📋 Today's Checklist

Screen Recordings (Silent):
- [ ] Landing page (demo/index.html) - 5s
- [ ] Daily brief scroll (demo/daily_briefs.html) - 30s
- [ ] Weekly synthesis scroll (demo/weekly_synthesis.html) - 25s
- [ ] ArXiv feed scroll (optional) - 10s

Terminal Recordings (Silent):
- [ ] Tree command showing telemetry structure - 10s
- [ ] Governance ledger JSON output - 15s
- [ ] Parquet file count - 5s

Static Assets:
- [ ] Title card created (PNG)
- [ ] Architecture diagram screenshot (PNG)

Organization:
- [ ] All recordings saved to organized folder
- [ ] All images exported to folder
- [ ] DEMO_VIDEO_SCRIPT.md accessible for later
- [ ] Video editing software installed (DaVinci Resolve, iMovie, etc.)

---

## 🎬 When You're Ready to Record Voiceover

1. **Preparation:**
   - Find quiet space
   - Test microphone
   - Have water nearby
   - Read script out loud once

2. **Recording:**
   - Follow [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)
   - Record each section 2-3 times
   - Speak slightly slower than normal
   - Stay energetic and engaged

3. **Processing:**
   - Remove long pauses
   - Normalize audio levels
   - Remove background noise if needed
   - Export as WAV or high-quality MP3

---

## 🎞️ Final Assembly (After Voiceover)

1. **Import all assets** to video editor
2. **Sync voiceover** to visual recordings
3. **Add on-screen text** overlays (from script)
4. **Add transitions** between sections (1-2s fades)
5. **Review timing** (must be exactly 3:00)
6. **Export** at 1920x1080, H.264, 30fps

---

## 📊 Progress Tracking

**Today (Nov 22):**
- ✅ Video production guide created
- ⏳ Silent recordings (can do today)
- ⏳ Static assets (can do today)

**Later (When back from travel):**
- ⏳ Voiceover recording (30-45 min)
- ⏳ Video editing (2-3 hours)
- ⏳ Upload to YouTube/Drive

**Deadline Flexibility:**
- Required submission: Nov 30
- Video is optional (+10 bonus)
- Can submit without video, add video later if time allows

---

## 💡 Tips for Screen Recording

### Software Recommendations

**Mac:**
- QuickTime (built-in, simple)
- CMD+Shift+5 (screenshot toolbar, has screen recording)

**Linux:**
- SimpleScreenRecorder
- OBS Studio
- Kazam

**Windows:**
- Xbox Game Bar (Win+G)
- OBS Studio

### Recording Settings
- **Resolution:** Match your display (1920x1080 ideal)
- **Frame rate:** 30fps
- **Audio:** Mute system audio (we'll add voiceover later)
- **Cursor:** Show cursor in demos, hide in terminal close-ups

### Best Practices
- **Clean desktop:** Close unnecessary windows/tabs
- **Browser:** Full screen mode (F11) for clean demos
- **Terminal:** Large font, high contrast theme
- **Mouse:** Smooth, deliberate movements
- **Timing:** Record 5-10 seconds extra on each end (easy to trim)

---

## 🚀 What This Achieves

By doing the silent recordings today, you'll have:
- ✅ All visual content captured
- ✅ ~80% of video prep complete
- ✅ Only voiceover + editing remaining

This makes the final assembly much faster when you're back in a good recording environment.

**Estimated remaining time after today:**
- Voiceover: 30-45 minutes
- Video editing: 2-3 hours
- **Total remaining: 3-4 hours**

---

## 📅 Suggested Timeline

**Today (Nov 22):**
- Screen recordings (30 min)
- Terminal recordings (20 min)
- Create title card (15 min)
- Screenshot diagram (10 min)
- **Total: ~75 minutes**

**Sunday (Nov 24):**
- Automated weekly blog runs at 10 PM
- Review output Monday morning

**Monday-Tuesday (Nov 25-26) - When back:**
- Record voiceover (45 min)
- Edit video (2-3 hours)
- Upload to YouTube

**Wednesday (Nov 27):**
- Buffer day for revisions

**Saturday (Nov 30):**
- Final Kaggle submission

---

**Current Status:** All required competition elements complete. Video is optional +10 bonus points.

**Your Plan:** ✅ Prep visuals today (silent), voiceover when back from travel

---

*Generated with [Claude Code](https://claude.com/claude-code)*
*Last Updated: November 22, 2025 - 3:00 PM EST*
