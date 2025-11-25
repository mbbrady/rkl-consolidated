# Audacity Visual Guide - Selecting and Deleting Audio

## Understanding What You See After Recording

### Your Audacity Window Layout

When you record twice, you should see something like this:

```
┌─────────────────────────────────────────────────────────────────────┐
│ File  Edit  Select  View  Transport  Tracks  Generate  Effect  ...  │
├─────────────────────────────────────────────────────────────────────┤
│ ⏸️ ▶️ ⏹️ ⏮️ ⏭️ 🔴 | [Tools] | [🎤 Recording Device ▼] | [••••] 🎤 │
├─────────────────────────────────────────────────────────────────────┤
│                                                                       │
│ Audio Track ────────────────────────────────────────── [X] [▼] [-]  │
│ ─────────────────────────────────────────────────────────────────── │
│ ▂▃▅▇█▇▅▃▂     (flat/silent)     ▂▃▅▇█▇▅▃▂                          │
│ ▂▃▅▇█▇▅▃▂     (flat/silent)     ▂▃▅▇█▇▅▃▂                          │
│ └─Take 1──┘                      └─Take 2──┘                         │
│ ─────────────────────────────────────────────────────────────────── │
│ 0:00      0:10      0:20      0:30      0:40      0:50      1:00    │
│                                                                       │
└─────────────────────────────────────────────────────────────────────┘
```

**What you're seeing:**
- The **wavy pattern** (waveform) represents your voice
- **Tall waves** = louder sound (you speaking)
- **Flat/nearly flat** = silence (the 2 seconds between takes)
- **Timeline** at bottom shows time in seconds

---

## How to Select Audio (Click and Drag)

### Method 1: Select Everything (Both Takes)

Press `Ctrl+A` (Select All)
- The entire track turns **lighter/highlighted**
- This is useful for exporting everything

### Method 2: Select Just One Take (Click and Drag)

**To select Take 1 (first recording):**

1. **Click** at the very beginning (near 0:00)
2. **Hold down mouse button**
3. **Drag** to the right until you reach the silent part (before Take 2)
4. **Release mouse button**

Visual:
```
Click here ↓              Drag to here ↓
[█████████████████████] (silence) [═══════════]
    SELECTED (lighter)              NOT selected
```

**To select Take 2 (second recording):**

1. **Click** at the start of the silent gap (after Take 1)
2. **Drag** to the very end
3. **Release**

Visual:
```
                      Click here ↓            Drag to here ↓
[═══════════] (silence) [█████████████████████]
NOT selected                SELECTED (lighter)
```

### Method 3: Double-Click Between Silences

If you have clear silence between takes:
1. **Double-click** on Take 1's waveform
2. Audacity will select just that take (up to the silence)

**Note:** This works best if you left 2+ seconds of silence between takes

---

## How to Delete Audio You Don't Want

### After selecting the audio you DON'T want:

1. **Select the take you want to delete** (click and drag)
2. Press **Delete** key (or `Ctrl+K` to cut)
3. That section disappears

**Example:** You want to keep Take 2 and delete Take 1

1. Click at 0:00, drag to end of Take 1 (including silence)
2. Press `Delete` key
3. Take 1 disappears, Take 2 moves to the left

Now you only have Take 2, and you can export it!

---

## Visual Selection Tutorial

### Scenario: You recorded twice, want to keep Take 2

**What you see:**
```
Track: ▂▃▅▇█ (silence) ▂▃▅▇█
       Take1            Take2
```

**Step 1: Select Take 1 (the one you DON'T want)**
```
[Click] ──────────> [Drag to here]
   ▂▃▅▇█     (silence)     ▂▃▅▇█
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ░░░░░
   SELECTED                NOT selected
```

**Step 2: Press Delete key**
```
Before: ▓▓▓▓▓▓▓▓▓▓ (silence) ▂▃▅▇█

After:  ▂▃▅▇█
        Take2 (moved to start)
```

**Step 3: Export what's left**
- Press `Ctrl+A` (select all)
- Press `Ctrl+Shift+E` (export)
- Save as `01-opening.wav`

---

## Alternative: Keep Both Takes, Select for Export

**Don't delete anything - just select the take you want to export:**

**To export Take 1 only:**
1. Click at beginning, drag to end of Take 1
2. **File → Export → Export Selected Audio**
3. Save as `01-opening.wav`

**To export Take 2 only:**
1. Click at start of Take 2, drag to end
2. **File → Export → Export Selected Audio**
3. Save as `01-opening-take2.wav` (if you want to compare later)

**Benefit:** You keep both takes in Audacity, can decide later

---

## Tips for Easier Selection

### Zoom In to See Better

If the waveform is too small to see clearly:
- Press `Ctrl+1` (zoom in) - do this several times
- Press `Ctrl+3` (zoom out)
- Press `Ctrl+F` (fit entire track in window)

**After zooming in, you'll see:**
```
Much more detail - easier to see where silence starts/ends
▁▂▃▄▅▆▇█▇▆▅▄▃▂▁▁▁▁▁▁▁▁▁▁▁▂▃▄▅▆▇█▇▆▅▄▃▂▁
└──────Speaking───────┘└─Silence─┘└─Speaking──┘
```

### Use the Timeline

Look at the time markers at the bottom:
- Take 1 might be from 0:00 to 0:25
- Silence from 0:25 to 0:27
- Take 2 from 0:27 to 0:52

Click at 0:00, drag to 0:25 = Take 1 selected

---

## Common Questions

### Q: How do I know which take is which?

**Listen first:**
1. Press `Home` (rewind to start)
2. Press `Spacebar` (play)
3. Listen: "First take starts... silence... second take starts..."
4. Note the times when each take starts (watch the playback cursor)

Then you can click at those time points to select.

### Q: I selected the wrong section, how do I undo?

- Click anywhere in empty space (deselects)
- Or press `Ctrl+Shift+A` (deselect all)
- Or just click and drag again to select correctly

### Q: I accidentally deleted the wrong take!

- Press `Ctrl+Z` (undo)
- The deleted audio comes back
- Audacity has unlimited undo, so press `Ctrl+Z` multiple times if needed

### Q: What if I can't see two separate takes?

If you only see one continuous waveform with no clear break:
- You didn't leave enough silence between takes
- **Solution:** Just export everything as one file, it's fine
- You can use Take 1, ignore Take 2 during editing on laptop

### Q: Should I delete before exporting or just select?

**Recommendation for tomorrow:**
- **Don't delete** - just select the better take
- Use **Export Selected Audio** (only exports what's selected)
- This keeps both takes in case you change your mind

**OR:**
- Listen to both takes
- Delete the bad one
- Export everything that's left (simpler)

Both methods work - choose what feels easier!

---

## Practice Exercise (Do This Tonight)

1. **Record two test takes:**
   - Press `R`, say "Test one", wait 2 seconds, `Spacebar`
   - Press `R`, say "Test two", wait 2 seconds, `Spacebar`

2. **Play back** (listen to both)

3. **Zoom in** (`Ctrl+1` a few times)

4. **Select Take 1:**
   - Click at very beginning
   - Drag to the silent part (before "Test two")
   - You should see Take 1 highlighted

5. **Export just Take 1:**
   - `Ctrl+Shift+E`
   - Save as `test1.wav`

6. **Select Take 2:**
   - Click at start of "Test two"
   - Drag to end
   - Should see Take 2 highlighted

7. **Export just Take 2:**
   - `Ctrl+Shift+E`
   - Save as `test2.wav`

8. **Verify both files saved:**
   ```bash
   ls -lh video_production/audio/test*.wav
   ```

If you can do this successfully, you're 100% ready for tomorrow! 🎯

---

## Quick Reference: Mouse Actions

| Action | What It Does |
|--------|--------------|
| **Click** anywhere | Place cursor (playback starts here) |
| **Click and drag** | Select a region of audio |
| **Double-click** on waveform | Select section (up to silence) |
| **Ctrl+A** | Select all |
| **Ctrl+Shift+A** | Deselect all |
| **Delete key** | Delete selected audio |
| **Ctrl+Z** | Undo last action |

---

*Visual selection guide for RKL Secure Reasoning Brief demo video*
*Recording date: November 25, 2025*
