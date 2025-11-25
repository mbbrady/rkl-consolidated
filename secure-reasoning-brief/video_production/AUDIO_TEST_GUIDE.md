# Audio Test Guide - Noise-Cancelling Headphones/Mic

## Quick Test Procedure

### 1. Launch Audacity (on your thin client)
```bash
# From your thin client terminal (not SSH session)
audacity &
```

### 2. Configure Input Device
1. Click **Transport** → **Rescan Audio Devices** (if needed)
2. In the toolbar, find the **microphone dropdown** (second toolbar)
3. Select your noise-cancelling headphones/mic from the list
4. Set input level to around **70-80%** to start

### 3. Record a Test Clip (30 seconds)
**Test Script:**
> "Hi, I'm Mike Brady. I work with sensitive research data that can't leave local infrastructure - and I thought others might be in the same boat. For the Kaggle AI Agents Capstone, I built an 18-agent system demonstrating Type III Secure Reasoning."

**Recording Steps:**
1. Press **Red Record Button** (or press `R`)
2. Read the test script at your natural speaking pace
3. Press **Spacebar** to stop recording
4. Play back (press **Spacebar** again)

### 4. Check Audio Quality

Listen for:
- ✅ **Clear speech** (no muffling)
- ✅ **Consistent volume** (not too quiet or clipping)
- ✅ **Minimal background noise** (noise-cancelling working)
- ✅ **No pops or clicks** (mic positioning good)
- ❌ **Breathing sounds** (adjust mic distance if present)
- ❌ **Room echo** (get closer to mic if present)

### 5. Adjust If Needed

**If too quiet:**
- Increase input level in Audacity toolbar (try 85-90%)
- Move closer to mic (4-6 inches ideal)
- Check system volume: `pavucontrol` → Input Devices tab

**If too loud (clipping/distortion):**
- Decrease input level (try 60-70%)
- Move slightly farther from mic

**If too much background noise:**
- Close windows/doors
- Turn off fans, AC, or other noise sources
- Check noise-cancelling is enabled on headphones
- Use **Effect** → **Noise Reduction** in Audacity (as backup)

**If pops on P/B sounds (plosives):**
- Position mic slightly to the side (not directly in front of mouth)
- Or move back 1-2 inches

### 6. Save Test File
```
File → Export → Export as WAV
Location: /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/audio/
Filename: 00-test-recording.wav
```

### 7. Optimal Recording Settings (Audacity Preferences)

**Quality Settings** (Edit → Preferences → Quality):
- Default Sample Rate: **44100 Hz**
- Default Sample Format: **32-bit float**

**Recording Settings** (Edit → Preferences → Recording):
- ✅ Enable: "Software playthrough of input" (if you want to hear yourself)
- ✅ Enable: "Overdub" (for multi-take recording)
- ❌ Disable: "Sound Activated Recording" (not needed for voiceover)

**Devices** (Edit → Preferences → Devices):
- Recording Device: Your noise-cancelling headphones/mic
- Channels: **1 (Mono)** (voiceover doesn't need stereo)

## Tomorrow's Recording Workflow

Once your test sounds good:

### Recording Procedure (per section)
1. **Open RECORDING_TRANSCRIPT.txt** (for reading)
2. **Open Audacity**
3. **For each section:**
   - Press `R` to start recording
   - Wait 2 seconds (silence)
   - Read the section clearly
   - Wait 2 seconds (silence)
   - Press `Spacebar` to stop
   - **Immediately record Take 2** (without listening):
     - Press `R` again
     - Wait 2 seconds
     - Read section again
     - Press `Spacebar`
   - Listen to both takes
   - Keep the better one, delete the other
   - Export: `File → Export → Export Selected Audio → WAV`
   - Save as `01-opening.wav`, `02-problem.wav`, etc.

### File Naming Convention
```
00-test-recording.wav       # Tonight's test
01-opening.wav              # Section 1 (50s)
02-problem.wav              # Section 2 (15s)
03-architecture.wav         # Section 3 (25s)
04-daily-brief.wav          # Section 4 (20s)
05-weekly-synthesis.wav     # Section 5 (20s)
06-telemetry.wav            # Section 6 (25s)
07-impact.wav               # Section 7 (15s)
08-closing.wav              # Section 8 (20s)
```

## Troubleshooting

### Audacity doesn't see your mic
```bash
# Check system audio devices
pavucontrol &
# Or
alsamixer
```

### Can't hear playback
- Check headphones are set as output device in Audacity
- Check system volume isn't muted

### Recording sounds robotic/glitchy
- Close other apps (especially browsers, video players)
- Increase buffer size: Edit → Preferences → Recording → Latency

### Want to remove a mistake mid-recording
- Don't! Just pause 3 seconds, then continue
- You can cut out mistakes during editing on laptop
- Or just do Take 2 if you mess up

## Quick Reference

| Action | Shortcut |
|--------|----------|
| Record | `R` |
| Stop/Play | `Spacebar` |
| Pause | `P` |
| Rewind to Start | `Home` |
| Zoom In | `Ctrl + 1` |
| Zoom Out | `Ctrl + 3` |
| Fit to Window | `Ctrl + F` |

---

## After Testing Tonight

Update the video production README with your confirmed settings:
- Microphone name (so you remember tomorrow)
- Optimal input level (%)
- Any specific positioning notes

**Target:** Get a clean 30-second test recording that sounds professional and clear.

---

*Audio test guide for RKL Secure Reasoning Brief demo video*
*Recording date: November 25, 2025*
