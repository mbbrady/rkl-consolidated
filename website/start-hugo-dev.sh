#!/bin/bash
# Clean Hugo development server startup script
# Based on GPT's recommendations for reliable live-reload

cd /home/mike/project/rkl/rkl.org

# Kill any existing Hugo servers
pkill -9 hugo 2>/dev/null
sleep 2

# Clean everything
rm -rf public/ resources/ .hugo_build.lock

echo "🚀 Starting Hugo with aggressive cache-busting..."
echo "📍 URL: http://localhost:9000"
echo "💡 Keep Chrome DevTools open with 'Disable cache' checked"
echo ""

# Start Hugo with GPT's recommended flags
/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo server \
  --disableFastRender \
  --noHTTPCache \
  --cleanDestinationDir \
  --renderToDisk \
  --bind 0.0.0.0 \
  --port 9000

# Flags explained:
# --disableFastRender = rebuild everything, not just changed files
# --noHTTPCache = force browsers to refetch CSS/JS
# --cleanDestinationDir = clear /public before each rebuild
# --renderToDisk = keep generated HTML in public/ (not memory)
# --bind 0.0.0.0 = allow access from any network interface
# --port 9000 = use port 9000
