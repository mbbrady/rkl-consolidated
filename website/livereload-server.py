#!/usr/bin/env python3
"""
Live reload server for RKL website development
Run this and it will automatically refresh your browser when CSS/HTML changes
"""

from livereload import Server
import subprocess
import os

# Change to project directory
os.chdir('/home/mike/project/rkl/rkl.org')

# Build Hugo site once at startup
print("Building Hugo site...")
subprocess.run(['/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo'], check=True)

# Create server
server = Server()

# Watch for CSS changes
server.watch('static/css/*.css', lambda: subprocess.run(['/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo'], check=True))

# Watch for layout changes
server.watch('layouts/**/*.html', lambda: subprocess.run(['/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo'], check=True))

# Watch for content changes
server.watch('content/**/*.md', lambda: subprocess.run(['/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo'], check=True))

# Serve from public directory
print("\n✅ Live reload server starting!")
print("🌐 Open http://localhost:5501 in your browser")
print("📝 Edit CSS in static/css/rkl-navy-coral.css and see INSTANT changes!\n")

server.serve(root='public/', host='0.0.0.0', port=5501)
