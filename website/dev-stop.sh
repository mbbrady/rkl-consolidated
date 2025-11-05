#!/bin/bash
# Stop RKL Development Server

PROJECT_DIR="/home/mike/project/rkl/rkl.org"
PIDFILE="$PROJECT_DIR/.hugo-server.pid"

echo "🛑 Stopping Hugo development server..."

# Kill by PID file
if [ -f "$PIDFILE" ]; then
  PID=$(cat "$PIDFILE")
  if kill -0 "$PID" 2>/dev/null; then
    echo "   Killing server (PID: $PID)"
    kill -9 "$PID" 2>/dev/null
    echo "   ✅ Server stopped"
  else
    echo "   ⚠️  PID $PID not running"
  fi
  rm -f "$PIDFILE"
  echo "   Removed PID file"
else
  echo "   ⚠️  No PID file found"
fi

# Kill any remaining Hugo processes
PIDS=$(pgrep -f "hugo server" 2>/dev/null || true)
if [ -n "$PIDS" ]; then
  echo "   Killing remaining Hugo processes: $PIDS"
  echo "$PIDS" | xargs kill -9 2>/dev/null || true
fi

# Kill anything on port 1313
PORT_PIDS=$(lsof -ti :1313 2>/dev/null || true)
if [ -n "$PORT_PIDS" ]; then
  echo "   Killing processes on port 1313: $PORT_PIDS"
  echo "$PORT_PIDS" | xargs kill -9 2>/dev/null || true
fi

echo ""
echo "✅ All Hugo servers stopped"
