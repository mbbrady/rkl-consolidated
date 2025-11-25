# How to Save Your Recordings in Audacity

## Quick Save Method (Recommended for Tomorrow)

### After recording each section:

1. **Select the audio you want to save**
   - If you just recorded it, it's already selected (highlighted)
   - Or click and drag on the waveform to select it
   - Or press `Ctrl+A` to select all

2. **Export as WAV file**
   - Go to **File → Export → Export Audio** (or `Ctrl+Shift+E`)
   - Or **File → Export → Export Selected Audio** (if you only want part)

3. **Choose save location**
   - Navigate to: `/home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/audio/`
   - Or type the path in the "Location" field

4. **Name your file**
   - Enter filename: `01-opening.wav` (or `02-problem.wav`, etc.)
   - **Important:** Include the `.wav` extension

5. **Set format**
   - **Format:** WAV (Microsoft)
   - **Encoding:** Signed 16-bit PCM (default is fine)
   - Click **Save**

6. **Edit Metadata dialog appears** (optional)
   - You can skip this - just click **OK**

7. **Done!** Your file is saved.

---

## Two-Take Workflow (What You'll Do Tomorrow)

### Recording both takes before saving:

```
Recording Track Layout:
════════════════════════════════════════════════════════
Take 1: ▂▃▅▇█▇▅▃▂   (silence)   ▂▃▅▇█▇▅▃▂
        └──────────────────┘       └─ Take 2
```

### Steps:

1. **Record Take 1**
   - Press `R` to start recording
   - Wait 2 seconds (silence)
   - Read the section
   - Wait 2 seconds (silence)
   - Press `Spacebar` to stop

2. **Immediately Record Take 2** (without stopping)
   - Press `R` again (continues on same track)
   - Wait 2 seconds (silence)
   - Read the section again
   - Wait 2 seconds (silence)
   - Press `Spacebar` to stop

3. **Listen to both takes**
   - Press `Home` to rewind to start
   - Press `Spacebar` to play through both
   - Decide which one is better

4. **Select ONLY the better take**
   - Click at the start of the take you want
   - Drag to the end of that take (including 2 seconds silence after)
   - The selected part will be highlighted (lighter color)

5. **Export the selected audio**
   - **File → Export → Export Selected Audio**
   - Save as `01-opening.wav`, `02-problem.wav`, etc.

6. **Start fresh for next section**
   - **File → New** (or `Ctrl+N`)
   - This gives you a clean slate for the next recording

---

## File Naming Convention

Save files in this exact format:

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

**Important:**
- Always include the `.wav` extension
- Use leading zeros (01, 02, not 1, 2) - keeps files sorted correctly
- Use hyphens, not spaces (makes file handling easier)

---

## Visual Guide: Selecting Audio to Export

### If you want the FIRST take:
```
Click here ↓                     Drag to here ↓
[═══════TAKE 1═══════]  silence  [═══TAKE 2═══]
          SELECTED
```

### If you want the SECOND take:
```
                             Click here ↓        Drag to here ↓
[═══TAKE 1═══]  silence  [═══════TAKE 2═══════]
                                  SELECTED
```

**Tip:** Selected audio appears lighter/highlighted in Audacity

---

## Export Settings (One-Time Setup)

### First time you export, verify these settings:

**File Format Settings:**
- **Format:** WAV (Microsoft) ✅
  - NOT MP3 (loses quality)
  - NOT Ogg Vorbis
  - NOT FLAC

- **Encoding:** Signed 16-bit PCM ✅
  - This is CD quality
  - Good balance of quality and file size
  - Perfect for video editing

**Where to set:**
- These appear in the "Export Audio" dialog
- Bottom of the dialog has dropdown menus

---

## Common Questions

### Q: Do I need to "Save Project" in Audacity?

**No, not for this workflow.**

- **File → Save Project** creates `.aup3` files (Audacity project files)
- These are only useful if you want to edit the recording later in Audacity
- For video production, you only need the **WAV exports**

**Workflow:**
1. Record in Audacity
2. Export as WAV (this is what video editor needs)
3. File → New (start fresh for next section)
4. Don't save the Audacity project

### Q: Can I edit mistakes before exporting?

**Yes, but don't spend time on it now:**
- You can cut out mistakes using the selection tool
- You can use Effects → Noise Reduction
- **BUT:** It's faster to just do Take 2 and pick the better one
- Save detailed editing for the laptop video editing phase

### Q: What if I accidentally close Audacity before exporting?

If you didn't export to WAV, **the recording is lost.**

**Prevention:**
- Export immediately after recording each section
- Don't wait until you've recorded everything

### Q: Where do my exported files go?

- Wherever you navigated to in the "Export Audio" dialog
- For this project: `/home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/audio/`
- Double-check the location before clicking Save!

### Q: How do I know the file was saved successfully?

After exporting, check in the terminal:
```bash
ls -lh /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/audio/
```

You should see your WAV file(s) with file sizes like:
```
-rw-r--r-- 1 mike mike 8.5M Nov 25 07:30 01-opening.wav
```

If the file size is 0 bytes or missing, something went wrong.

---

## Keyboard Shortcuts for Faster Workflow

| Action | Shortcut |
|--------|----------|
| Export Audio | `Ctrl + Shift + E` |
| Select All | `Ctrl + A` |
| New Project | `Ctrl + N` |
| Play/Stop | `Spacebar` |
| Record | `R` |
| Rewind to Start | `Home` |

---

## Tomorrow's Streamlined Workflow

### For each of 8 sections:

1. Press `R` → record Take 1 → `Spacebar`
2. Press `R` → record Take 2 → `Spacebar`
3. Press `Home` → `Spacebar` → listen to both
4. Click/drag to select better take
5. `Ctrl+Shift+E` → navigate to audio/ folder → type filename → Save → OK
6. `Ctrl+N` (new project) → repeat for next section

**Time estimate:** 5-7 minutes per section = 40-60 minutes total

---

## Checklist After Each Export

- ✅ Saved to correct location (`video_production/audio/`)
- ✅ Correct filename (matches section number)
- ✅ File has `.wav` extension
- ✅ File size is reasonable (2-15 MB depending on length)

---

## Test This Tonight

**Before bed, save your test recording:**

1. Record a 10-second test
2. Select all (`Ctrl+A`)
3. Export (`Ctrl+Shift+E`)
4. Navigate to `video_production/audio/`
5. Name it `00-test-recording.wav`
6. Save → OK
7. Verify it saved:
   ```bash
   ls -lh video_production/audio/00-test-recording.wav
   ```

If you can successfully complete this test save, you're ready for tomorrow! 🎙️

---

*File saving guide for RKL Secure Reasoning Brief demo video*
*Recording date: November 25, 2025*
