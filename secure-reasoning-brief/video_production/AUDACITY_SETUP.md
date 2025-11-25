# Audacity Setup Guide - Complete Configuration

## Step 1: Connect Your Headphones/Mic

### Physical Connection
1. **Plug in your noise-cancelling headphones/mic** to your thin client
   - USB connection: Just plug in (should auto-detect)
   - 3.5mm audio jack: Plug into the **microphone/headset port** (usually pink or with headphone icon)

2. **Turn on noise-cancelling** if your headphones have a power button/switch

3. **Wait 5 seconds** for the system to detect the device

---

## Step 2: Verify System Recognizes Your Mic

### Check in System Audio Settings

**Option A: Using PulseAudio Volume Control (Recommended)**
```bash
# Open PulseAudio control panel
pavucontrol &
```

Then:
1. Click the **"Input Devices"** tab
2. Look for your headphones/mic in the list (e.g., "USB Audio Device", "Headset", or brand name)
3. **Make sure it's NOT muted** (unmute icon should show speaker, not crossed-out speaker)
4. Set the volume slider to about **80%** to start
5. When you speak, you should see the **level meter move** (green bars)

**Option B: Using ALSA Mixer (Alternative)**
```bash
alsamixer
```
- Press `F6` to select your sound card (choose your headphones)
- Press `F4` to show capture devices
- Use arrow keys to navigate, `M` to unmute
- Press `Esc` to exit

---

## Step 3: Launch Audacity

```bash
audacity &
```

**First-time launch notes:**
- You might see a welcome dialog - just click through it
- If asked about updates, you can skip

---

## Step 4: Configure Audacity for Recording

### A. Set Input Device

Look at the **Audacity toolbar** (top of window):

```
┌─────────────────────────────────────────────────────────┐
│ [🎵] [Recording Device ▼] [Channels ▼] [••••••••] 🎤 🔊 │
└─────────────────────────────────────────────────────────┘
```

1. **Find the "Recording Device" dropdown** (should say something like "Default" or show a device name)
2. **Click the dropdown arrow**
3. **Select your noise-cancelling headphones/mic** from the list
   - Look for USB Audio Device, Headset, or your brand name
   - **NOT "Pulse" or "Default"** - select the actual device name

4. **Set Channels to "1 (Mono)"** in the next dropdown
   - Voiceover only needs mono, not stereo

### B. Set Recording Level

In the same toolbar, find the **microphone icon** with a slider:
- Click and drag the slider to about **0.7** (70%)
- Or click the dropdown and type: `0.7`

### C. Enable Click-to-Start Monitoring

1. Click the **microphone icon dropdown** (small arrow next to mic icon)
2. Select **"Start Monitoring"**
3. Now you should see the **input level meter moving** when you speak
   - Meter should be green/yellow when speaking
   - **Should NOT go into red** (that's clipping/distortion)
   - If too quiet (barely moves): increase level to 0.8-0.9
   - If too loud (red bars): decrease level to 0.5-0.6

---

## Step 5: Configure Audio Quality Settings

### Recording Quality
1. Go to **Edit → Preferences** (or `Ctrl+P`)
2. Click **"Quality"** in the left sidebar
3. Set:
   - **Default Sample Rate:** `44100 Hz` (CD quality)
   - **Default Sample Format:** `32-bit float` (best quality)
4. Click **OK**

### Recording Behavior
1. Go to **Edit → Preferences** again
2. Click **"Recording"** in the left sidebar
3. **Enable these:**
   - ☑ **"Always allow pausing and restarting"**
   - ☑ **"Play other tracks while recording"** (optional, but useful)
4. **Disable these:**
   - ☐ **"Software playthrough"** (you'll hear yourself in headphones otherwise - can be distracting)
   - ☐ **"Sound Activated Recording"** (not needed for voiceover)
5. Click **OK**

---

## Step 6: Test Your Setup

### Quick Recording Test

1. **Press the red Record button** (or press `R` key)
2. **Wait 2 seconds of silence**
3. **Speak clearly** for 10 seconds:
   > "Testing, one, two, three. This is a test recording for the RKL Secure Reasoning Brief demo video. I'm checking my audio levels and microphone quality."
4. **Wait 2 seconds of silence**
5. **Press Spacebar** to stop recording

### Listen to Your Test

1. **Press Home key** to rewind to start
2. **Press Spacebar** to play
3. **Listen carefully** and check:

**Good audio should have:**
- ✅ **Clear speech** - every word is understandable
- ✅ **Consistent volume** - doesn't fade in/out
- ✅ **No background noise** - noise-cancelling is working
- ✅ **Natural sound** - not muffled or tinny

**Problems and fixes:**

| Problem | Fix |
|---------|-----|
| **Too quiet** | Increase recording level to 0.8-0.9 |
| **Too loud / distorted** | Decrease recording level to 0.5-0.6 |
| **Muffled** | Check mic isn't covered; move closer to mouth |
| **Pops on P/B sounds** | Position mic slightly to side, not directly in front |
| **Background noise** | Check noise-cancelling is on; close windows; move to quieter room |
| **Echo / hollow sound** | Move closer to mic (4-6 inches ideal) |
| **Breathing sounds** | Move mic slightly farther away; position below nose level |

### Save Your Test File

1. **Select all:** `Ctrl+A`
2. **File → Export → Export as WAV**
3. **Save to:**
   ```
   /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/audio/00-test-recording.wav
   ```
4. In the dialog:
   - **Format:** WAV (Microsoft) signed 16-bit PCM (default is fine)
5. Click **Save**

---

## Step 7: Optimize Your Recording Position

### Ideal Setup

```
        YOU
         👤
         👄 ← mouth
         |
    4-6 inches
         |
         🎤 ← mic
    (slightly to side)
```

**Best practices:**
- **Distance:** 4-6 inches from mouth to mic
- **Angle:** Mic slightly to the side (not directly in front) to avoid pops
- **Height:** Mic at mouth level or slightly below
- **Posture:** Sit up straight, don't slouch (affects voice quality)
- **Environment:**
  - Close door/windows
  - Turn off fans, AC, refrigerator noise if possible
  - Record in smallest room available (less echo)
  - Avoid hard surfaces (tile/hardwood) - carpet/furniture absorbs sound

---

## Step 8: Final Sound Check

### The Voice Test

Record yourself saying the **first 30 seconds of your script**:

> "Hi, I'm Mike Brady. I work with sensitive research data that can't leave local infrastructure - and I thought others might be in the same boat. For the Kaggle AI Agents Capstone, I built an 18-agent system demonstrating Type III Secure Reasoning - my framework where raw data stays local, but derived insights can be reasoned over by cloud AI."

**Play it back and ask:**
- ✅ Would I want to listen to this for 3 minutes?
- ✅ Is every word clear?
- ✅ Does it sound professional?

If you answer YES to all three → **You're ready to record tomorrow!**

If NO → Review the "Problems and fixes" table above and adjust

---

## Troubleshooting Common Issues

### "Audacity doesn't see my microphone"

```bash
# Check if system sees the device
arecord -l

# Should show your USB device or headset
# If not listed, try unplugging and replugging
```

Then in Audacity:
- **Transport → Rescan Audio Devices**
- Check the recording device dropdown again

### "I hear myself with a delay (latency)"

This is called "software playthrough" - disable it:
- **Edit → Preferences → Recording**
- **Uncheck:** "Software playthrough of input"

### "Recording sounds choppy/robotic"

Your system is overloaded:
- Close web browsers, video players, other apps
- **Edit → Preferences → Recording**
- Increase **Audio to buffer:** from 100ms to 200ms

### "No sound on playback"

Check output device:
- In Audacity toolbar, find **Playback Device** dropdown
- Select your headphones (should match your recording device)
- Check system volume isn't muted: `pavucontrol` → Output Devices

### "Can't find the record button"

Look for these icons in the top toolbar:
- ⏸️ Pause
- ▶️ Play
- ⏹️ Stop
- ⏮️ Skip to start
- ⏭️ Skip to end
- 🔴 **Record** ← This one!

---

## Quick Reference for Tomorrow

### Recording Workflow (Per Section)

1. **Open RECORDING_TRANSCRIPT.txt** (for reading)
2. **Open Audacity** (already configured)
3. **For each section:**
   - Press `R` (start recording)
   - Wait 2 seconds (silence)
   - Read the section
   - Wait 2 seconds (silence)
   - Press `Spacebar` (stop)
   - *(Immediately do Take 2)*
   - Press `R` again
   - Wait 2 seconds
   - Read section again
   - Press `Spacebar`
   - Listen to both takes
   - Select the better one (click/drag on waveform)
   - **File → Export → Export Selected Audio**
   - Save as `01-opening.wav`, `02-problem.wav`, etc.
   - **File → New** (start fresh for next section)

### Keyboard Shortcuts

| Action | Key |
|--------|-----|
| Record | `R` |
| Stop/Play | `Spacebar` |
| Pause | `P` |
| Rewind to Start | `Home` |
| Zoom In | `Ctrl + 1` |
| Zoom Out | `Ctrl + 3` |
| Fit to Window | `Ctrl + F` |
| Select All | `Ctrl + A` |

---

## Success Checklist

Before you finish tonight's test session, verify:

- ✅ Audacity recognizes your mic
- ✅ Input level meter moves when you speak (green/yellow, not red)
- ✅ Test recording sounds clear and professional
- ✅ Saved test file to `video_production/audio/00-test-recording.wav`
- ✅ You know how to record, stop, and export
- ✅ Recording environment is quiet
- ✅ Mic positioning is comfortable

**If all checked** → You're ready for tomorrow morning! 🎙️

---

*Audacity setup guide for RKL Secure Reasoning Brief demo video*
*Recording date: November 25, 2025*
