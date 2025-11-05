#!/bin/bash
# Start RKL Dashboard

echo "========================================"
echo "  RKL Dashboard Startup"
echo "========================================"
echo ""

# Check if in correct directory
if [ ! -f "app.py" ]; then
    echo "Error: Must run from dashboard directory"
    echo "cd to: /home/mike/project/rkl/rkl-program/dashboard"
    exit 1
fi

# Check if Flask is installed
if ! python3 -c "import flask" 2>/dev/null; then
    echo "Installing dependencies..."
    pip3 install -r requirements.txt
fi

echo "Starting dashboard..."
echo ""
echo "Dashboard will be available at:"
echo "  http://localhost:5000"
echo ""
echo "Press Ctrl+C to stop"
echo ""

python3 app.py
