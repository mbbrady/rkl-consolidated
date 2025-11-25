# Video Production - RKL Secure Reasoning Brief Demo

This directory contains all assets and files for producing the 3-minute demo video for the Kaggle AI Agents Capstone competition.

## Directory Structure

```
video_production/
├── README.md                    # This file
├── DEMO_VIDEO_SCRIPT.md        # Complete production script with timing and visuals
├── RECORDING_TRANSCRIPT.txt    # Clean narration-only transcript for recording
├── audio/                      # Recorded voiceover files
│   ├── 01-opening.wav
│   ├── 02-problem.wav
│   ├── 03-architecture.wav
│   ├── 04-daily-brief.wav
│   ├── 05-weekly-synthesis.wav
│   ├── 06-telemetry.wav
│   ├── 07-impact.wav
│   └── 08-closing.wav
├── screen_captures/            # Recorded screen footage
│   ├── 01-title-card.mp4
│   ├── 02-architecture-diagram.mp4
│   ├── 03-arxiv-scroll.mp4
│   ├── 04-daily-brief-demo.mp4
│   ├── 05-weekly-synthesis-demo.mp4
│   ├── 06-telemetry-terminal.mp4
│   ├── 07-split-screen.mp4
│   └── 08-cron-demo.mp4
├── assets/                     # Static visual assets
│   ├── title-card.png
│   ├── architecture-diagram.png
│   └── closing-card.png
└── final/                      # Final rendered video
    └── rkl-secure-reasoning-demo.mp4
```

## Recording Workflow

### Phase 1: Audio Recording (Nov 25 morning - thin client)
1. Install Audacity on thin client
2. Record each section from `RECORDING_TRANSCRIPT.txt`
3. Use 2-take rule (maximum 2 takes per section)
4. Save as individual WAV files in `audio/` directory
5. Transfer to laptop via scp when done

### Phase 2: Screen Capture (Nov 25 - thin client/laptop)
1. Install SimpleScreenRecorder
2. Record screen captures per shot list in `DEMO_VIDEO_SCRIPT.md`
3. Save as individual MP4 files in `screen_captures/` directory
4. Transfer to laptop for editing

### Phase 3: Asset Creation (Nov 25)
1. Create title card image (navy/coral RKL branding)
2. Export architecture diagram as PNG from Mermaid
3. Save in `assets/` directory

### Phase 4: Video Editing (Nov 25-26 - laptop)
1. Import all audio and video files
2. Edit according to `DEMO_VIDEO_SCRIPT.md` timeline
3. Add text overlays for key points
4. Export as H.264 1080p 30fps
5. Save final video in `final/` directory

## File Transfer Commands

### From thin client to laptop:
```bash
# Transfer audio files
scp -r /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/audio/ \
    mike@laptop:/path/to/video_production/

# Transfer screen captures
scp -r /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/screen_captures/ \
    mike@laptop:/path/to/video_production/
```

### From laptop back to thin client (final video):
```bash
scp /path/to/video_production/final/rkl-secure-reasoning-demo.mp4 \
    mike@thin-client:/home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production/final/
```

## Production Timeline

- **Nov 25 (morning)**: Record voiceover audio before travel
- **Nov 25 (travel)**: Record screen captures on thin client
- **Nov 25-26**: Edit video on laptop
- **Nov 26**: Upload final video
- **Nov 30**: Submit to Kaggle competition

## Software Requirements

### Thin Client (Recording):
- Audacity (audio recording)
- SimpleScreenRecorder (screen capture)
- Firefox/Chromium (demo page navigation)

### Laptop (Editing):
- DaVinci Resolve (free) / Kdenlive / OpenShot
- 1080p export capability
- ~2GB disk space for working files

## Target Specifications

- **Duration**: 3:00-3:10 (180-190 seconds)
- **Resolution**: 1920x1080 (Full HD)
- **Frame Rate**: 30 fps
- **Codec**: H.264
- **Audio**: AAC 44.1kHz stereo
- **File Size**: Under 100 MB (if possible)

## Key Emphasis Points

From `RECORDING_TRANSCRIPT.txt`:
- **Type III Secure Reasoning** (mention 3+ times)
- **Provable compliance** (telemetry proof)
- **Honest prototype** (AI assistance transparency)
- **Real-world value** (production-ready, automated)

---

*Demo video for Kaggle AI Agents Capstone Competition*
*Target submission: November 30, 2025*
