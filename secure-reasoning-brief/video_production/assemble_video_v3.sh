#!/bin/bash

# Video Assembly Script v3 - With Screen Recordings
# Creates demo video with all improved visuals

set -e

# Activate conda environment for ffmpeg
source ~/miniforge3/etc/profile.d/conda.sh
conda activate rkl-briefs

AUDIO_DIR="audio/FINAL"
SCREENSHOTS_DIR="screenshots"
OUTPUT_DIR="."
TEMP_DIR="temp_video_v3"

# Create temp directory
mkdir -p "$TEMP_DIR"

echo "=== Creating Video Sections ==="

# Section 1: Opening (104.7s) - Title card
echo "Section 1: Opening..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/title-card.png" \
    -i "$AUDIO_DIR/01-opening_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 104.7 \
    "$TEMP_DIR/section1.mp4" -y

# Section 2: Problem/Type III Compliance (27.6s) - NEW diagram
echo "Section 2: Type III Compliance..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/type3_compliance_final.png" \
    -i "$AUDIO_DIR/02-problem_v2.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 27.6 \
    "$TEMP_DIR/section2.mp4" -y

# Section 3: Architecture (22.8s) - NEW flow diagram
echo "Section 3: Architecture Flow..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/architecture_flow_v2.png" \
    -i "$AUDIO_DIR/03-architecture_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 22.8 \
    "$TEMP_DIR/section3.mp4" -y

# Section 4: Daily Brief Demo (19.0s) - Screen recording slowed by 20%
echo "Section 4: Daily Brief Demo..."
ffmpeg -i "$SCREENSHOTS_DIR/daily_demo.webm" \
    -i "$AUDIO_DIR/04-daily-brief_v1.wav" \
    -filter:v "setpts=1.195*PTS" \
    -c:v libx264 -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 19.0 \
    "$TEMP_DIR/section4.mp4" -y

# Section 5: Weekly Synthesis Demo (23.0s) - Screen recording slowed by 10%
echo "Section 5: Weekly Synthesis Demo..."
ffmpeg -i "$SCREENSHOTS_DIR/weekly_blog_demo.webm" \
    -i "$AUDIO_DIR/05-weekly-synthesis_v1.wav" \
    -filter:v "setpts=1.095*PTS" \
    -c:v libx264 -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 23.0 \
    "$TEMP_DIR/section5.mp4" -y

# Section 6: Telemetry (21.2s)
echo "Section 6: Telemetry..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/telemetry_slide.png" \
    -i "$AUDIO_DIR/06-telemetry_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 21.2 \
    "$TEMP_DIR/section6.mp4" -y

# Section 7: System Impact (18.5s)
echo "Section 7: System Impact..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/impact_slide.png" \
    -i "$AUDIO_DIR/07-impact_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 18.5 \
    "$TEMP_DIR/section7.mp4" -y

# Section 8: Closing (23.5s)
echo "Section 8: Closing..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/closing_slide.png" \
    -i "$AUDIO_DIR/08-closing_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest -t 23.5 \
    "$TEMP_DIR/section8.mp4" -y

# Create concat file
echo "=== Creating concat file ==="
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

# Concatenate all sections
echo "=== Concatenating sections ==="
ffmpeg -f concat -safe 0 -i "$TEMP_DIR/concat.txt" \
    -c copy \
    "$OUTPUT_DIR/demo_video_v3.mp4" -y

# Calculate total duration
TOTAL_DURATION=$(echo "104.7 + 27.6 + 22.8 + 19.0 + 23.0 + 21.2 + 18.5 + 23.5" | bc)
echo "=== Video Assembly Complete ==="
echo "Total duration: $TOTAL_DURATION seconds"
echo "Output: demo_video_v3.mp4"

# Cleanup
echo "Cleaning up temporary files..."
rm -rf "$TEMP_DIR"

echo "Done!"
