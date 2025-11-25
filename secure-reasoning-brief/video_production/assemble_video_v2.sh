#!/bin/bash
# Video Assembly Script v2 - With Section-Specific Visuals
# November 25, 2025

set -e  # Exit on error

cd /home/mike/project/rkl-consolidated/secure-reasoning-brief/video_production

# Activate conda environment for ffmpeg
source ~/miniforge3/etc/profile.d/conda.sh
conda activate rkl-briefs

echo "=========================================="
echo "RKL Video Assembly Script v2"
echo "With Section-Specific Visuals"
echo "=========================================="

# Create temp directory for intermediate files
mkdir -p temp

# ==============================================
# STEP 1: Create video for each section with matching visual
# ==============================================
echo ""
echo "Step 1: Creating section videos with audio + visuals..."

# Section 1: Opening
ffmpeg -loop 1 -i title-card.png -i audio/FINAL/01-opening_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_01.mp4 -y
echo "✓ Section 1: Opening (title card)"

# Section 2: Problem
ffmpeg -loop 1 -i screenshots/type3_compliance.png -i audio/FINAL/02-problem_v2.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_02.mp4 -y
echo "✓ Section 2: Problem (Type III diagram)"

# Section 3: Architecture
ffmpeg -loop 1 -i screenshots/architecture_flow.png -i audio/FINAL/03-architecture_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_03.mp4 -y
echo "✓ Section 3: Architecture (flow diagram)"

# Section 4: Daily Brief
ffmpeg -loop 1 -i screenshots/daily-brief-screenshot.png -i audio/FINAL/04-daily-brief_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_04.mp4 -y
echo "✓ Section 4: Daily Brief (screenshot)"

# Section 5: Weekly Synthesis
ffmpeg -loop 1 -i screenshots/weekly-blog-screenshot.png -i audio/FINAL/05-weekly-synthesis_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_05.mp4 -y
echo "✓ Section 5: Weekly Synthesis (screenshot)"

# Section 6: Telemetry
ffmpeg -loop 1 -i screenshots/telemetry_slide.png -i audio/FINAL/06-telemetry_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_06.mp4 -y
echo "✓ Section 6: Telemetry (slide)"

# Section 7: Impact
ffmpeg -loop 1 -i screenshots/impact_slide.png -i audio/FINAL/07-impact_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_07.mp4 -y
echo "✓ Section 7: Impact (stats slide)"

# Section 8: Closing
ffmpeg -loop 1 -i screenshots/closing_slide.png -i audio/FINAL/08-closing_v1.wav \
  -vf "scale=1920:1080" -pix_fmt yuv420p \
  -c:v libx264 -tune stillimage -c:a aac -b:a 192k -ar 44100 \
  -shortest temp/section_08.mp4 -y
echo "✓ Section 8: Closing (thank you slide)"

# ==============================================
# STEP 2: Concatenate all sections
# ==============================================
echo ""
echo "Step 2: Concatenating all sections..."

cat > temp/sections_list.txt << 'EOF'
file 'section_01.mp4'
file 'section_02.mp4'
file 'section_03.mp4'
file 'section_04.mp4'
file 'section_05.mp4'
file 'section_06.mp4'
file 'section_07.mp4'
file 'section_08.mp4'
EOF

ffmpeg -f concat -safe 0 -i temp/sections_list.txt -c copy demo_video_v2.mp4 -y

echo ""
echo "=========================================="
echo "✓ VIDEO ASSEMBLY COMPLETE - V2"
echo "=========================================="
echo ""
echo "Output: demo_video_v2.mp4"
echo ""
echo "Sections:"
echo "  1. Opening - Title Card"
echo "  2. Problem - Type III Compliance Diagram"
echo "  3. Architecture - System Flow"
echo "  4. Daily Brief - Screenshot"
echo "  5. Weekly Synthesis - Blog Screenshot"
echo "  6. Telemetry - Phase-0 Artifacts"
echo "  7. Impact - System Stats"
echo "  8. Closing - Thank You"
echo ""
echo "Ready to review!"
echo ""
