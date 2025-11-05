#!/bin/bash
# RKL Website Development Server - Robust Single-Instance
# Ensures ONLY ONE Hugo server runs at a time using PID lock file

set -e  # Exit on error

PROJECT_DIR="/home/mike/project/rkl/rkl.org"
PIDFILE="$PROJECT_DIR/.hugo-server.pid"
CONDA_ENV="/opt/conda-envs/envs/rkl-web"

cd "$PROJECT_DIR"

# Function to kill existing server
kill_existing_server() {
  echo "🧹 Checking for existing Hugo servers..."

  # Kill by PID file if exists
  if [ -f "$PIDFILE" ]; then
    OLD_PID=$(cat "$PIDFILE")
    if kill -0 "$OLD_PID" 2>/dev/null; then
      echo "   Killing old server (PID: $OLD_PID)"
      kill -9 "$OLD_PID" 2>/dev/null || true
    fi
    rm -f "$PIDFILE"
  fi

  # Kill any Hugo servers on port 1313
  PIDS=$(lsof -ti :1313 2>/dev/null || true)
  if [ -n "$PIDS" ]; then
    echo "   Killing servers on port 1313: $PIDS"
    echo "$PIDS" | xargs kill -9 2>/dev/null || true
  fi

  # Kill all Hugo processes (aggressive cleanup)
  pkill -9 -f "hugo server" 2>/dev/null || true

  sleep 2
}

# Clean up function on exit
cleanup() {
  echo ""
  echo "🛑 Stopping Hugo server..."
  if [ -f "$PIDFILE" ]; then
    PID=$(cat "$PIDFILE")
    kill -9 "$PID" 2>/dev/null || true
    rm -f "$PIDFILE"
  fi
  exit 0
}

trap cleanup EXIT INT TERM

# Kill any existing servers
kill_existing_server

# Clean build artifacts
echo "🧹 Cleaning build artifacts..."
rm -rf public/ resources/ .hugo_build.lock

echo ""
echo "🚀 Starting RKL Website Development Environment"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo "📝 Edit files in VS Code"
echo "🌐 Preview at: http://localhost:1313"
echo "🔄 Hugo LiveReload enabled - instant updates"
echo ""
echo "⏹️  Press Ctrl+C to stop"
echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""

# Start Hugo server in background and save PID
"$CONDA_ENV/bin/hugo" server \
  --disableFastRender \
  --noHTTPCache \
  --cleanDestinationDir \
  --forceSyncStatic \
  --poll 300ms \
  --port 1313 \
  --bind 0.0.0.0 &

HUGO_PID=$!
echo $HUGO_PID > "$PIDFILE"

echo "✅ Hugo server started (PID: $HUGO_PID)"
echo "   PID file: $PIDFILE"
echo ""

# Wait for Hugo process
wait $HUGO_PID
