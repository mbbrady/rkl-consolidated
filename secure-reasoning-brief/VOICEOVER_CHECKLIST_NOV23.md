# Voiceover Recording - Tomorrow (Nov 23)

**Time Needed:** 30-45 minutes
**Best Time:** Morning (fresher voice, less ambient noise)
**Location:** Quiet room with door closed

---

## 🎙️ Pre-Recording Setup (5 minutes)

### 1. Hardware Check
- [ ] Microphone connected (headset or USB mic preferred)
- [ ] Test audio levels in recording software
- [ ] Aim for -12dB to -6dB peak levels (not too quiet, not clipping)
- [ ] Headphones on to monitor your recording

### 2. Environment Setup
- [ ] Close windows (block outside noise)
- [ ] Close door
- [ ] Turn off fans, AC, or noisy appliances
- [ ] Silence phone notifications
- [ ] Have water nearby (prevent dry mouth clicks)

### 3. Software Setup
- [ ] Open Audacity (free) or your audio recorder
- [ ] Create new project
- [ ] Set sample rate: 48 kHz
- [ ] Set bit depth: 24-bit
- [ ] Test recording: Say "Testing 1, 2, 3" and play back

### 4. Script Preparation
- [ ] Open [DEMO_VIDEO_SCRIPT.md](DEMO_VIDEO_SCRIPT.md)
- [ ] Read through entire script 1-2 times (practice pacing)
- [ ] Mark any tricky words or phrases
- [ ] Have a pen to mark takes (Take 1, Take 2, etc.)

---

## 🎬 Recording Session (30 minutes)

### Recording Tips
- **Pace:** Slightly slower than normal conversation
- **Pauses:** Add 2-3 second silence between sections (easier to edit)
- **Energy:** Stay engaged - this is your competition submission!
- **Breathing:** Breathe through nose between sentences (quieter)
- **Posture:** Sit up straight (better breath support)
- **Distance:** 6-8 inches from mic (not too close = plosives)

### Record Each Section 2-3 Times

Hit record once and do all takes in a single recording (easier to organize):

#### Section 1: Opening (20 seconds)
**Line from script:**
> "AI practitioners face information overload - over 100 AI safety papers published weekly. We built an 18-agent system that solves this problem while demonstrating Type III compliance: provable secure reasoning where raw data never leaves local infrastructure."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence before next section**

#### Section 2: Problem Statement (20 seconds)
**Line from script:**
> "Busy researchers need daily updates, not hundreds of papers. But existing AI summarization tools don't prove they handle sensitive data securely. Our solution automates research monitoring with a complete audit trail."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence**

#### Section 3: Architecture (30 seconds)
**Lines from script:**
> "Our system coordinates 18 specialized agents. Three feed monitors collect papers from ArXiv, AI Alignment Forum, and Google AI Blog. Local Ollama agents process the raw content - this is critical. Raw articles never leave our infrastructure."
>
> *[Pause for emphasis]*
>
> "Cloud Gemini agents receive only derived summaries for expert analysis. This is Type III compliance: local processing for sensitive data, cloud processing for analysis."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence**

#### Section 4: Daily Brief Demo (25 seconds)
**Line from script:**
> "The system runs twice daily at 9 AM and 9 PM. Each run produces a 2-3 minute executive brief highlighting breakthrough papers and emerging trends. Here's today's morning brief showing 6 papers analyzed, with the top 2 highlighted."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence**

#### Section 5: Weekly Synthesis Demo (20 seconds)
**Line from script:**
> "Every Sunday, a weekly synthesis aggregates the full week of data into a comprehensive analysis with IEEE-style citations. All claims are verifiable, and citations use only public metadata - not raw content - maintaining Type III compliance."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence**

#### Section 6: Telemetry Proof (30 seconds)
**Lines from script:**
> "How do we prove Type III compliance? Phase-0 Research Telemetry. Every agent interaction generates telemetry artifacts - 375 files over 5 days of operation. Here's a governance ledger file showing explicit verification: raw data exposed: false. This is the governance ledger for one run."
>
> *[Pause to let judges see the JSON]*
>
> "Three core artifact types plus six enhancements document the complete system operation. This isn't just logging - it's provable compliance."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence**

#### Section 7: Real-World Impact (20 seconds)
**Line from script:**
> "This system is production-ready. Fully automated via cron, it transforms 280 papers per week into digestible updates. For practitioners: quick daily reads. For researchers: comprehensive weekly analysis. For organizations: a reference implementation for secure multi-agent systems."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **2-second silence**

#### Section 8: Closing (15 seconds)
**Line from script:**
> "Secure Reasoning Research Brief: proving that multi-agent AI systems can deliver real-world value with verifiable security guarantees. Thank you."

- [ ] Take 1 - **[mark best]**
- [ ] Take 2
- [ ] Take 3 (if needed)
- [ ] **Stop recording**

---

## 🔧 Post-Recording Processing (10 minutes)

### 1. Listen to Full Recording
- [ ] Play back entire recording
- [ ] Mark timestamps of best takes for each section
- [ ] Note any sections that need re-recording

### 2. Cut Best Takes
For each section, cut out the best take:
- [ ] Section 1 - Export as `01_opening.wav`
- [ ] Section 2 - Export as `02_problem.wav`
- [ ] Section 3 - Export as `03_architecture.wav`
- [ ] Section 4 - Export as `04_daily_brief.wav`
- [ ] Section 5 - Export as `05_weekly_synthesis.wav`
- [ ] Section 6 - Export as `06_telemetry.wav`
- [ ] Section 7 - Export as `07_impact.wav`
- [ ] Section 8 - Export as `08_closing.wav`

### 3. Basic Audio Cleanup (Optional - 5 minutes)

**In Audacity:**
1. Select 2 seconds of silence (room tone)
2. Effect → Noise Reduction → Get Noise Profile
3. Select all (Ctrl+A)
4. Effect → Noise Reduction → OK (removes background hum)
5. Effect → Normalize (ensure consistent volume)

### 4. Save Files
```bash
mkdir -p ~/video_assets/audio

# Save each section:
# ~/video_assets/audio/01_opening.wav
# ~/video_assets/audio/02_problem.wav
# ... etc.

# Also save the full raw recording as backup:
# ~/video_assets/audio/full_recording_raw.wav
```

---

## ✅ Success Criteria

You're done when you have:
- [ ] 8 separate audio files (one per section)
- [ ] Each file is clear and professional
- [ ] No background noise or distractions
- [ ] Pacing is comfortable (not rushed)
- [ ] Energy is consistent throughout
- [ ] Files saved to organized folder

---

## 🎞️ What Happens Next

**While traveling:**
1. Record silent screen captures (browser, terminal)
2. Create title card and static images
3. Import audio + visuals into video editor
4. Sync audio to visuals
5. Add on-screen text overlays
6. Export final video

**Benefit of recording audio first:**
- ✅ Best audio quality (in good environment)
- ✅ Visual recordings can be done anywhere (silent)
- ✅ Editing can happen on laptop anywhere
- ✅ Audio is the hardest part - get it done first!

---

## 📊 Time Budget

| Task | Time |
|------|------|
| Setup & test | 5 min |
| Record all sections (2-3 takes each) | 25 min |
| Listen & select best takes | 5 min |
| Cut & export 8 files | 5 min |
| Optional: Noise reduction | 5 min |
| **TOTAL** | **40-45 min** |

---

## 💡 Quick Tips

**If you make a mistake:**
- Don't stop! Just pause 2 seconds, then restart that sentence
- You'll cut out the mistake in editing

**If you need to sneeze/cough:**
- Pause recording, do your thing, resume
- Or keep recording and cut it out later

**Voice care:**
- Room temperature water (not ice cold)
- Avoid dairy right before (can create mouth noises)
- Do a few vocal warm-ups (hum, lip trills)

**Pacing guide:**
- Read slower than you think (video will feel better)
- Emphasize key terms: "Type III", "375 files", "18 agents"
- Pause briefly before important statements

---

## 🚀 Tomorrow's Agenda (Nov 23)

**Morning (Best time for voice):**
- [ ] 9:00 AM: Coffee, warm up voice
- [ ] 9:30 AM: Set up recording space
- [ ] 9:45 AM: Record voiceover (45 min)
- [ ] 10:30 AM: Review and export files
- [ ] 11:00 AM: **DONE** - Audio complete!

**Rest of day:**
- [ ] Pack for travel
- [ ] Prepare laptop with video editing software
- [ ] Copy [VIDEO_PRODUCTION_GUIDE.md](VIDEO_PRODUCTION_GUIDE.md) for reference

**While traveling (Nov 24-26):**
- Screen recordings (can do anywhere)
- Video editing (can do on laptop)
- Final assembly and upload

---

**Status:** Script ready, this checklist will guide you through tomorrow's recording session. Audio is the most important part - get it done in good environment!

---

*Generated with [Claude Code](https://claude.com/claude-code)*
*Last Updated: November 22, 2025 - 3:15 PM EST*
