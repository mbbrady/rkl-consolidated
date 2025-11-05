# RKL Dashboard

**A simple web interface for managing your Resonant Knowledge Lab nonprofit setup**

![Dashboard Status](https://img.shields.io/badge/status-ready-green)
![Python](https://img.shields.io/badge/python-3.8+-blue)
![Flask](https://img.shields.io/badge/flask-3.0-lightgrey)

---

## What is This?

The RKL Dashboard is a local web application that helps you manage your nonprofit setup by:

- 📊 **Tracking Progress** - Visual display of completion status (🟢🟡🔴)
- 📋 **Managing Tasks** - View and filter all tasks from your checklist
- 📦 **Meeting Packet Status** - See which documents are ready for your board meeting
- ⚡ **Quick Actions** - One-click buttons for common tasks
- 📁 **File Access** - Links to open documents in VS Code

**No data leaves your computer** - everything runs locally!

---

## Quick Start

### 1. Install Dependencies (First Time Only)

```bash
cd /home/mike/project/rkl/rkl-program/dashboard
pip3 install -r requirements.txt
```

### 2. Start the Dashboard

```bash
./start_dashboard.sh
```

Or manually:
```bash
python3 app.py
```

### 3. Open in Browser

Navigate to: **http://localhost:5000**

---

## Features

### 📊 Status Overview
- **Overall Progress**: See completion percentage at a glance
- **Color-Coded Tasks**: 🟢 Done, 🟡 In Progress, 🔴 To Do
- **Category Breakdown**: Progress by Legal, Governance, Website, etc.

### 🚨 Critical Next Steps
- Prioritized list of most important tasks
- Pulled automatically from your checklist
- Shows what blocks other work

### 📦 Meeting Packet Status
- Real-time status of your organizational meeting documents
- Shows which of the 9 required documents are ready
- Click to refresh status
- Links to open the meeting packet folder

### 📋 Task Management
- View all tasks organized by category
- Filter by status (All, To Do, In Progress, Done)
- Click file paths to open in VS Code
- Tasks sync with your `RKL_Setup_Checklist.md`

### ⚡ Quick Actions
- **Preview Website** - Starts Hugo server and opens site
- **Assemble Meeting Packet** - Runs the packet assembly script
- **Open Meeting Folder** - Opens folder in VS Code
- **Refresh Data** - Updates all status information

### 📄 Recent Files
- See the 10 most recently modified files
- Click to open in VS Code
- Shows modification time and file path

---

## How It Works

The dashboard is a Python Flask web application that:

1. **Reads your checklist** (`0_Admin/RKL_Setup_Checklist.md`)
2. **Parses tasks and status** (looks for 🟢🟡🔴 emojis)
3. **Runs assembly script** to check meeting packet status
4. **Scans recent files** in the rkl-program folder
5. **Provides API** for refreshing and quick actions

**No database needed** - all data comes from your existing markdown files!

---

## File Structure

```
dashboard/
├── app.py                    # Main Flask application
├── requirements.txt          # Python dependencies
├── start_dashboard.sh        # Startup script
├── README.md                # This file
├── templates/
│   └── dashboard.html        # HTML template
└── static/
    ├── css/
    │   └── dashboard.css     # Styling
    └── js/
        └── dashboard.js      # Interactive features
```

---

## API Endpoints

For automation or custom integrations:

| Endpoint | Description | Response |
|----------|-------------|----------|
| `GET /` | Main dashboard page | HTML |
| `GET /api/status` | JSON status data | JSON |
| `GET /api/refresh_packet` | Refresh meeting packet | JSON |
| `GET /open_file/<path>` | Open file in VS Code | JSON |
| `GET /quick_action/<action>` | Execute quick action | JSON |

---

## Configuration

The dashboard automatically detects:
- Base directory: `../` (rkl-program folder)
- Checklist: `0_Admin/RKL_Setup_Checklist.md`
- Meeting Packet: `1_Governance/Organizational_Meeting/Meeting_Packet/`

### Custom Port

To use a different port:
```python
# In app.py, change the last line:
app.run(debug=True, host='0.0.0.0', port=8080)  # Your port here
```

### Remote Access

To access from other devices on your network:
```python
# Already enabled by default with host='0.0.0.0'
# Access at: http://your-computer-ip:5000
```

---

## Troubleshooting

### "Module not found" errors
```bash
pip3 install -r requirements.txt
```

### Dashboard won't start
- Check you're in the `dashboard/` directory
- Verify Python 3.8+ is installed: `python3 --version`
- Check if port 5000 is already in use

### Tasks not showing
- Verify `RKL_Setup_Checklist.md` exists at `0_Admin/`
- Check file format matches expected table structure
- Look for 🟢🟡🔴 emojis in the checklist

### Meeting packet status not updating
- Check that `assemble_packet.sh` is executable
- Run manually to test: `cd Meeting_Packet && ./assemble_packet.sh`
- Verify script exists and has correct permissions

### VS Code won't open files
- Ensure `code` command is in your PATH
- Test manually: `code /path/to/file.md`
- On Linux: `sudo update-alternatives --set editor /usr/bin/code`

---

## Customization

### Change Colors

Edit `static/css/dashboard.css`:
```css
/* Primary color (currently #0F4C81) */
.header {
    background: linear-gradient(135deg, #YOUR_COLOR 0%, #YOUR_COLOR_DARK 100%);
}
```

### Add New Quick Actions

Edit `app.py`:
```python
@app.route('/quick_action/<action>')
def quick_action(action):
    if action == 'your_action':
        # Your code here
        return jsonify({'status': 'ok', 'message': 'Done!'})
```

### Modify Task Display

Edit `templates/dashboard.html` to change how tasks are shown.

---

## Security Notes

- Dashboard runs **locally only** by default
- No authentication (assumes single-user local machine)
- If exposing to network, add authentication
- Doesn't modify any files (read-only except quick actions)

---

## Future Enhancements

Potential additions:
- [ ] Edit tasks directly in dashboard
- [ ] Mark tasks complete from UI
- [ ] Git integration (commit, push, status)
- [ ] Email reminders for upcoming deadlines
- [ ] Mobile-responsive improvements
- [ ] Dark mode
- [ ] Export reports (PDF, CSV)

---

## Support

**Questions?**
- Read: `CLAUDE.md` in this folder
- Check: `0_Admin/QUICK_START_GUIDE.md`
- Review: `0_Admin/RKL_Setup_Checklist.md`

**Issues?**
- Verify all paths in `app.py` are correct
- Check console output for error messages
- Ensure Flask is properly installed

---

## Credits

Built for Resonant Knowledge Lab
- **Organization**: Virginia 501(c)(3) in formation
- **Mission**: Ethical AI for Living Knowledge
- **Website**: resonantknowledgelab.org

---

**Version**: 1.0.0
**Last Updated**: 2025-10-14
**Python**: 3.8+
**License**: Internal use for RKL
