#!/bin/bash
set -e

# Activate conda environment for ffmpeg
source ~/miniforge3/etc/profile.d/conda.sh
conda activate rkl-briefs

SCREENSHOTS_DIR="screenshots"
AUDIO_DIR="audio/FINAL"
TEMP_DIR="temp_video_v5"
OUTPUT_DIR="."

# Create temp directory
mkdir -p "$TEMP_DIR"

echo "=========================================="
echo "RKL Video Assembly Script v5"
echo "Filter Complex + Updated Diagrams"
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

# Section 3: Architecture Flow with NEW v5 diagram (use exact audio duration)
echo "Section 3: Architecture Flow..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/architecture_v5_test.png" \
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

# Section 6: Telemetry with NEW v3 slide (use exact audio duration)
echo "Section 6: Telemetry..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/telemetry_slide_v3.png" \
    -i "$AUDIO_DIR/06-telemetry_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section6.mp4" -y

# Section 7: System Impact with NEW comprehensive slide (use exact audio duration)
echo "Section 7: System Impact..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/system_impact_slide.png" \
    -i "$AUDIO_DIR/07-impact_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section7.mp4" -y

# Section 8: Closing (use exact audio duration)
echo "Section 8: Closing..."
ffmpeg -loop 1 -i "$SCREENSHOTS_DIR/title-card.png" \
    -i "$AUDIO_DIR/08-closing_v1.wav" \
    -c:v libx264 -tune stillimage -c:a aac -b:a 192k -pix_fmt yuv420p \
    -shortest \
    "$TEMP_DIR/section8.mp4" -y

# Use filter_complex for seamless concatenation (eliminates gaps between sections)
# Scale all videos to 1920x1080 before concatenating to ensure consistent dimensions
echo ""
echo "Concatenating all sections with filter_complex for seamless playback..."
ffmpeg -i "$TEMP_DIR/section1.mp4" \
       -i "$TEMP_DIR/section2.mp4" \
       -i "$TEMP_DIR/section3.mp4" \
       -i "$TEMP_DIR/section4.mp4" \
       -i "$TEMP_DIR/section5.mp4" \
       -i "$TEMP_DIR/section6.mp4" \
       -i "$TEMP_DIR/section7.mp4" \
       -i "$TEMP_DIR/section8.mp4" \
       -filter_complex "\
[0:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v0];\
[1:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v1];\
[2:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v2];\
[3:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v3];\
[4:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v4];\
[5:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v5];\
[6:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v6];\
[7:v]scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,setsar=1[v7];\
[v0][0:a][v1][1:a][v2][2:a][v3][3:a][v4][4:a][v5][5:a][v6][6:a][v7][7:a]concat=n=8:v=1:a=1[outv][outa]" \
       -map "[outv]" -map "[outa]" \
       -c:v libx264 -c:a aac -b:a 192k \
       "$OUTPUT_DIR/demo_video_v5.mp4" -y

echo ""
echo "=========================================="
echo "Video v5 Assembly Complete!"
echo "=========================================="
ls -lh "$OUTPUT_DIR/demo_video_v5.mp4"
