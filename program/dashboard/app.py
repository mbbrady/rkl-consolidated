#!/usr/bin/env python3
"""
RKL Dashboard - Resonant Knowledge Lab Management Dashboard
A simple web interface for tracking tasks and managing RKL nonprofit setup
"""

from flask import Flask, render_template, jsonify, request
import os
import re
import subprocess
from datetime import datetime
from pathlib import Path

app = Flask(__name__)

# Base paths
BASE_DIR = Path(__file__).parent.parent
CHECKLIST_PATH = BASE_DIR / "0_Admin" / "RKL_Setup_Checklist.md"
MEETING_PACKET_PATH = BASE_DIR / "1_Governance" / "Organizational_Meeting" / "Meeting_Packet"

def parse_checklist():
    """Parse the RKL_Setup_Checklist.md file and extract tasks with status"""
    tasks = []
    current_section = None

    with open(CHECKLIST_PATH, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    for line in lines:
        # Detect section headers
        if line.startswith('## ') and not line.startswith('## '):
            current_section = line.strip('# \n')
            continue

        # Parse task lines in tables
        if '|' in line and ('🟢' in line or '🟡' in line or '🔴' in line):
            parts = [p.strip() for p in line.split('|')]
            if len(parts) >= 4:
                status_icon = parts[1]
                task_name = parts[2]
                notes = parts[3] if len(parts) > 3 else ''
                location = parts[4] if len(parts) > 4 else ''

                # Determine status
                if '🟢' in status_icon:
                    status = 'done'
                elif '🟡' in status_icon:
                    status = 'in_progress'
                else:
                    status = 'todo'

                # Clean up location - remove backticks and extra formatting
                clean_location = location.strip('`').strip()

                tasks.append({
                    'section': current_section,
                    'name': task_name,
                    'status': status,
                    'notes': notes,
                    'location': clean_location
                })

    return tasks

def get_status_summary():
    """Calculate overall status summary"""
    tasks = parse_checklist()
    total = len(tasks)
    done = len([t for t in tasks if t['status'] == 'done'])
    in_progress = len([t for t in tasks if t['status'] == 'in_progress'])
    todo = len([t for t in tasks if t['status'] == 'todo'])

    percentage = int((done / total * 100)) if total > 0 else 0

    return {
        'total': total,
        'done': done,
        'in_progress': in_progress,
        'todo': todo,
        'percentage': percentage
    }

def get_meeting_packet_status():
    """Get status of meeting packet documents"""
    script_path = MEETING_PACKET_PATH / "assemble_packet.sh"

    if not script_path.exists():
        return {'status': 'error', 'message': 'Script not found'}

    try:
        result = subprocess.run(
            [str(script_path)],
            cwd=str(MEETING_PACKET_PATH),
            capture_output=True,
            text=True,
            timeout=10
        )

        # Parse output for document status
        output = result.stdout
        documents = []
        for line in output.split('\n'):
            if '✓ Found:' in line:
                doc_name = line.split('Found:')[1].strip()
                documents.append({'name': doc_name, 'status': 'ready'})
            elif '⚠' in line and ('Empty:' in line or 'Not ready:' in line):
                doc_name = line.split(':')[1].split('(')[0].strip()
                documents.append({'name': doc_name, 'status': 'missing'})

        ready = len([d for d in documents if d['status'] == 'ready'])
        total = len(documents)

        return {
            'status': 'ok',
            'documents': documents,
            'ready': ready,
            'total': total,
            'percentage': int((ready / total * 100)) if total > 0 else 0
        }
    except Exception as e:
        return {'status': 'error', 'message': str(e)}

def get_recent_files():
    """Get recently modified files"""
    files = []
    for root, dirs, filenames in os.walk(BASE_DIR):
        # Skip hidden and generated folders
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['__pycache__', 'node_modules']]

        for filename in filenames:
            if filename.endswith(('.md', '.pdf', '.xlsx')):
                filepath = Path(root) / filename
                mtime = filepath.stat().st_mtime
                files.append({
                    'name': filename,
                    'path': str(filepath.relative_to(BASE_DIR)),
                    'modified': datetime.fromtimestamp(mtime),
                    'size': filepath.stat().st_size
                })

    # Sort by modification time, most recent first
    files.sort(key=lambda x: x['modified'], reverse=True)
    return files[:10]  # Top 10 most recent

def get_critical_next_steps():
    """Extract critical next steps from checklist"""
    steps = []
    with open(CHECKLIST_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the Critical Path section
    match = re.search(r'## Critical Path.*?\n\n(.*?)(?=\n##|\Z)', content, re.DOTALL)
    if match:
        section = match.group(1)
        # Extract numbered items with emoji status
        for line in section.split('\n'):
            if re.match(r'^\d+\.', line.strip()):
                # Extract status and task
                status_match = re.search(r'(🟢|🟡|🔴)\s*(.+?)(?:\s*-\s*(.+))?$', line)
                if status_match:
                    status_icon = status_match.group(1)
                    task = status_match.group(2).strip()
                    note = status_match.group(3).strip() if status_match.group(3) else ''

                    status = 'done' if '🟢' in status_icon else 'in_progress' if '🟡' in status_icon else 'todo'
                    steps.append({'task': task, 'status': status, 'note': note})

    return steps

@app.route('/')
def index():
    """Main dashboard page"""
    summary = get_status_summary()
    tasks = parse_checklist()
    meeting_status = get_meeting_packet_status()
    recent_files = get_recent_files()
    critical_steps = get_critical_next_steps()

    return render_template('dashboard.html',
                         summary=summary,
                         tasks=tasks,
                         meeting_status=meeting_status,
                         recent_files=recent_files,
                         critical_steps=critical_steps)

@app.route('/api/status')
def api_status():
    """API endpoint for status data"""
    return jsonify({
        'summary': get_status_summary(),
        'meeting_packet': get_meeting_packet_status(),
        'critical_steps': get_critical_next_steps()
    })

@app.route('/api/refresh_packet')
def refresh_packet():
    """Refresh meeting packet status"""
    status = get_meeting_packet_status()
    return jsonify(status)

@app.route('/open_file/<path:filepath>')
def open_file(filepath):
    """Open file in VS Code"""
    full_path = BASE_DIR / filepath
    if full_path.exists():
        try:
            subprocess.Popen(['code', str(full_path)])
            return jsonify({'status': 'ok', 'message': f'Opening {filepath} in VS Code'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})
    return jsonify({'status': 'error', 'message': 'File not found'})

@app.route('/quick_action/<action>')
def quick_action(action):
    """Handle quick actions"""
    if action == 'preview_website':
        try:
            website_path = BASE_DIR.parent / 'rkl.org'
            subprocess.Popen(['hugo', 'server', '-D'], cwd=str(website_path))
            return jsonify({'status': 'ok', 'message': 'Starting Hugo server at http://localhost:1313'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    elif action == 'assemble_packet':
        script_path = MEETING_PACKET_PATH / 'assemble_packet.sh'
        try:
            result = subprocess.run([str(script_path)],
                                  cwd=str(MEETING_PACKET_PATH),
                                  capture_output=True,
                                  text=True)
            return jsonify({'status': 'ok', 'message': 'Packet assembled', 'output': result.stdout})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    elif action == 'open_folder':
        try:
            subprocess.Popen(['code', str(MEETING_PACKET_PATH)])
            return jsonify({'status': 'ok', 'message': 'Opening Meeting_Packet folder'})
        except Exception as e:
            return jsonify({'status': 'error', 'message': str(e)})

    return jsonify({'status': 'error', 'message': 'Unknown action'})

if __name__ == '__main__':
    print("=" * 60)
    print("RKL Dashboard Starting...")
    print("=" * 60)
    print(f"Base directory: {BASE_DIR}")
    print(f"Checklist: {CHECKLIST_PATH.exists() and 'Found' or 'Not found'}")
    print(f"Meeting Packet: {MEETING_PACKET_PATH.exists() and 'Found' or 'Not found'}")
    print("=" * 60)
    print("\n🚀 Dashboard running at: http://localhost:5000")
    print("Press Ctrl+C to stop\n")

    app.run(debug=True, host='0.0.0.0', port=5000)
