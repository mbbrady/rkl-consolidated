#!/bin/bash
# RKL Website Development Server - Simple Hugo LiveReload
# Uses Hugo's native live reload without Browser-Sync

cd /home/mike/project/rkl/rkl.org

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
echo "🌐 Preview at: http://localhost:1313"
echo "🔄 Hugo LiveReload enabled - changes auto-refresh"
echo ""
echo "📂 Watching all files in:"
echo "   • content/"
echo "   • static/"
echo "   • layouts/"
echo "   • themes/"
echo "   • config.toml"
echo ""
echo "⏹️  Press Ctrl+C to stop"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Hugo server with LiveReload
# Key flags for cache busting:
#   --disableFastRender: Full rebuilds every time
#   --noHTTPCache: Disables HTTP caching
#   --cleanDestinationDir: Clean public/ on rebuild
#   --forceSyncStatic: Force sync of static files
#   --poll 300ms: Poll for changes (more reliable than inotify)
$CONDA_ENV/bin/hugo server \
  --disableFastRender \
  --noHTTPCache \
  --cleanDestinationDir \
  --forceSyncStatic \
  --poll 300ms \
  --port 1313 \
  --bind 0.0.0.0 \
  --navigateToChanged \
  --templateMetrics \
  --templateMetricsHints

# The server runs in foreground, so this handles Ctrl+C automatically
