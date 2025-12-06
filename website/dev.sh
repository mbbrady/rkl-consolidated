#!/bin/bash
# RKL Website Development Server
# Uses rkl-web conda environment for Hugo + Browser-Sync

cd /home/mike/project/rkl-consolidated/website

# Set conda environment paths
CONDA_ENV="/opt/conda-envs/envs/rkl-web"
export PATH="$CONDA_ENV/bin:$PATH"

# Kill any existing processes
echo "🧹 Cleaning up old processes..."
pkill -9 hugo 2>/dev/null
pkill -9 browser-sync 2>/dev/null
pkill -9 node 2>/dev/null
sleep 1

# Clean build artifacts
rm -rf public/ resources/ .hugo_build.lock

echo ""
echo "🚀 Starting RKL Website Development Environment"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Edit files in VS Code"
echo "🌐 Preview at: http://localhost:3000"
echo "🔄 Changes auto-reload instantly"
echo ""
echo "📂 Watch folders:"
echo "   • content/   (Markdown files)"
echo "   • static/    (CSS, images)"
echo "   • layouts/   (Hugo templates)"
echo ""
echo "⏹️  Press Ctrl+C to stop"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Hugo server in background
echo "🏗️  Starting Hugo server..."
$CONDA_ENV/bin/hugo server \
  --disableFastRender \
  --noHTTPCache \
  --cleanDestinationDir \
  --port 1313 \
  --bind 0.0.0.0 \
  > /tmp/hugo-server.log 2>&1 &

HUGO_PID=$!

# Wait for Hugo to start
sleep 3

# Check if Hugo started successfully
if ! kill -0 $HUGO_PID 2>/dev/null; then
  echo "❌ Hugo failed to start. Check /tmp/hugo-server.log"
  cat /tmp/hugo-server.log
  exit 1
fi

echo "✅ Hugo running on http://localhost:1313"
echo ""

# Start browser-sync proxy
echo "🔄 Starting Browser-Sync (live reload)..."
echo ""
$CONDA_ENV/bin/browser-sync start \
  --proxy "localhost:1313" \
  --port 3000 \
  --files "content/**/*,static/**/*,layouts/**/*,config.toml" \
  --no-notify \
  --no-open \
  --reload-delay 200 \
  --reload-debounce 200 \
  --no-inject-changes \
  --middleware "function(req, res, next) { res.setHeader('Cache-Control', 'no-cache, no-store, must-revalidate'); next(); }"

# Cleanup on exit
trap "echo ''; echo '🛑 Shutting down...'; kill $HUGO_PID 2>/dev/null; pkill browser-sync 2>/dev/null; exit" INT TERM
