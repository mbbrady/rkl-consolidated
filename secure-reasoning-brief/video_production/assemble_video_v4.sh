#!/bin/bash

# Video Assembly Script v4 - Fixed Timing and Updated Diagrams
# November 25, 2025

set -e

# Activate conda environment for ffmpeg
source ~/miniforge3/etc/profile.d/conda.sh
conda activate rkl-briefs

AUDIO_DIR="audio/FINAL"
SCREENSHOTS_DIR="screenshots"
OUTPUT_DIR="."
TEMP_DIR="temp_video_v4"

# Create temp directory
mkdir -p "$TEMP_DIR"

echo "=========================================="
echo "RKL Video Assembly Script v4"
echo "Fixed Timing + Updated Diagrams"
echo "=========================================="

# Section 1: Opening (use exact audio duration)
echo "Section 1: Opening..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/title-card.png" \
    -i "$AUDIO_DIR/01-opening_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section1.mp4" -y

# Section 2: Type III Compliance (use exact audio duration)
echo "Section 2: Type III Compliance..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/type3_compliance_final.png" \
    -i "$AUDIO_DIR/02-problem_v2.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section2.mp4" -y

# Section 3: Architecture Flow (use exact audio duration)
echo "Section 3: Architecture Flow..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/architecture_flow_v3.png" \
    -i "$AUDIO_DIR/03-architecture_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section3.mp4" -y

# Section 4: Daily Brief Demo (slow video to match audio)
echo "Section 4: Daily Brief Demo..."
ffmpeg -i "$SCREENSHOTS_DIR/daily_demo.webm" \
    -i "$AUDIO_DIR/04-daily-brief_v1.wav" \
    -filter:v "setpts=1.195*PTS" \
    -c:v libx264 -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section4.mp4" -y

# Section 5: Weekly Synthesis Demo (slow video to match audio)
echo "Section 5: Weekly Synthesis Demo..."
ffmpeg -i "$SCREENSHOTS_DIR/weekly_blog_demo.webm" \
    -i "$AUDIO_DIR/05-weekly-synthesis_v1.wav" \
    -filter:v "setpts=1.095*PTS" \
    -c:v libx264 -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section5.mp4" -y

# Section 6: Telemetry (use exact audio duration)
echo "Section 6: Telemetry..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/telemetry_slide_v2.png" \
    -i "$AUDIO_DIR/06-telemetry_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section6.mp4" -y

# Section 7: System Impact (use exact audio duration)
echo "Section 7: System Impact..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/impact_slide.png" \
    -i "$AUDIO_DIR/07-impact_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section7.mp4" -y

# Section 8: Closing (use exact audio duration)
echo "Section 8: Closing..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/closing_slide.png" \
    -i "$AUDIO_DIR/08-closing_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section8.mp4" -y

# Create concat demuxer file
echo "=== Creating concatenation list ==="
cat > "$TEMP_DIR/concat.txt" << EOF
file 'section1.mp4'
file 'section2.mp4'
file 'section3.mp4'
file 'section4.mp4'
file 'section5.mp4'
file 'section6.mp4'
file 'section7.mp4'
file 'section8.mp4'
EOF

# Concatenate all sections with re-encoding to avoid timestamp issues
echo "=== Concatenating sections ==="
ffmpeg -f concat -safe 0 -i "$TEMP_DIR/concat.txt" \
    -c:v libx264 -c:a aac -b:a 192k \
    "$OUTPUT_DIR/demo_video_v4.mp4" -y

echo "=========================================="
echo "Video Assembly Complete!"
echo "Output: demo_video_v4.mp4"
echo "=========================================="

# Cleanup
echo "Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

echo "Done!"
