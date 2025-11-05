#!/bin/bash
# Quick preview script - forces Chrome to reload with no cache

# Build the site
cd /home/mike/project/rkl/rkl.org
hugo --quiet

# Open in Chrome with no cache (incognito mode)
google-chrome --incognito --new-window "http://localhost:1313/?nocache=$(date +%s)" 2>/dev/null &

echo "Opening preview in Chrome incognito..."
echo "URL: http://localhost:1313/?nocache=$(date +%s)"
