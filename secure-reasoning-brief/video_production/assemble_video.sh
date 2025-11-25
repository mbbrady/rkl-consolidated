#!/bin/bash
# Video Assembly Script for RKL Secure Reasoning Brief Capstone Demo
# November 25, 2025

set -e  # Exit on error

cd /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production

# Activate conda environment for ffmpeg
source ~/miniforge3/etc/profile.d/conda.sh
conda activate rkl-briefs

echo "=========================================="
echo "RKL Video Assembly Script"
echo "=========================================="

# Create temp directory for intermediate files
mkdir -p temp

# ==============================================
# STEP 1: Concatenate selected audio takes
# ==============================================
echo ""
echo "Step 1: Concatenating audio tracks..."

# Using FINAL selected audio takes
cat > temp/audio_list.txt << 'EOF'
file '../audio/FINAL/01-opening_v1.wav'
file '../audio/FINAL/02-problem_v2.wav'
file '../audio/FINAL/03-architecture_v1.wav'
file '../audio/FINAL/04-daily-brief_v1.wav'
file '../audio/FINAL/05-weekly-synthesis_v1.wav'
file '../audio/FINAL/06-telemetry_v1.wav'
file '../audio/FINAL/07-impact_v1.wav'
file '../audio/FINAL/08-closing_v1.wav'
EOF

ffmpeg -f concat -safe 0 -i temp/audio_list.txt -c copy temp/narration.wav -y
echo "✓ Audio concatenated: temp/narration.wav"

# ==============================================
# STEP 2: Get audio duration
# ==============================================
AUDIO_DURATION=$(ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 temp/narration.wav)
echo "✓ Total audio duration: ${AUDIO_DURATION}s"

# ==============================================
# STEP 3: Create video segments
# ==============================================
echo ""
echo "Step 2: Creating video segments..."

# Title card - 5 seconds with silent audio track (mono to match recordings)
ffmpeg -f lavfi -i anullsrc=channel_layout=mono:sample_rate=44100 -loop 1 -i title-card.png -t 5 \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/01_title.mp4 -y
echo "✓ Title card created (5s)"

# Placeholder slides for sections without specific screenshots
# Using title card with slight blur as placeholder
ffmpeg -loop 1 -i title-card.png -vf "scale=1920:1080,boxblur=10:1" -t 1 -pix_fmt yuv420p temp/placeholder.mp4 -y

# For simplicity in v1: Use title card as background for all narration
# In v2, we'll add specific screenshots per section
echo "Creating narration video with title card background..."
ffmpeg -loop 1 -i title-card.png -i temp/narration.wav \
  -vf "scale=1920:1080" \
  -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage \
  -c:a aac -b:a 192k -ar 44100 \
  -shortest \
  temp/02_narration.mp4 -y
echo "✓ Narration video created"

# ==============================================
# STEP 4: Concatenate title + narration
# ==============================================
echo ""
echo "Step 3: Assembling final video..."

cat > temp/video_list.txt << 'EOF'
file '01_title.mp4'
file '02_narration.mp4'
EOF

ffmpeg -f concat -safe 0 -i temp/video_list.txt -c copy demo_video_draft_v1.mp4 -y

echo ""
echo "=========================================="
echo "✓ VIDEO ASSEMBLY COMPLETE"
echo "=========================================="
echo ""
echo "Output: demo_video_draft_v1.mp4"
echo "Duration: ~$((5 + ${AUDIO_DURATION%.*}))s (~$((5 + ${AUDIO_DURATION%.*} / 60))m $((5 + ${AUDIO_DURATION%.*} % 60))s)"
echo ""
echo "Preview with: ffplay demo_video_draft_v1.mp4"
echo "Or open in browser: file://$(pwd)/demo_video_draft_v1.mp4"
echo ""
echo "NEXT STEPS:"
echo "1. Review the draft video"
echo "2. Add section-specific screenshots"
echo "3. Add text overlays for key terms"
echo "4. Add transitions between sections"
echo ""
