# RKL Website Development Workflow

## The Problem We Solved

Browser caching was preventing instant visual feedback during development. Multiple competing Hugo servers caused "page not found" errors.

## The Solution

A robust development workflow with:
- **Single-instance guarantee** via PID lock file
- **Aggressive cache-busting** in Hugo server
- **Instant LiveReload** without manual refresh
- **Clean startup/shutdown** scripts

## Commands

### Start Development Server

```bash
cd /home/mike/project/rkl/rkl.org
./dev-start.sh
```

**What it does:**
1. Kills ANY existing Hugo servers (via PID file, port 1313, process name)
2. Cleans build artifacts (`public/`, `resources/`, `.hugo_build.lock`)
3. Starts ONE Hugo server with aggressive cache-busting
4. Saves PID to `.hugo-server.pid` for tracking
5. Runs Hugo LiveReload on http://localhost:1313

**Key Hugo flags:**
- `--disableFastRender` - Full rebuilds every time
- `--noHTTPCache` - Disables HTTP caching
- `--cleanDestinationDir` - Clean public/ on rebuild
- `--forceSyncStatic` - Force sync of static files
- `--poll 300ms` - Poll for changes (reliable file watching)

### Stop Development Server

```bash
cd /home/mike/project/rkl/rkl.org
./dev-stop.sh
```

**What it does:**
1. Kills server by PID file
2. Kills any remaining Hugo processes
3. Kills anything on port 1313
4. Removes PID lock file

### The Workflow

1. **Start server ONCE:** `./dev-start.sh`
2. **Edit files in VS Code:** Changes to CSS, content, layouts auto-refresh
3. **View in browser:** http://localhost:1313
4. **Stop when done:** `./dev-stop.sh` (or Ctrl+C)

## What Auto-Refreshes

Hugo LiveReload watches:
- `/content/` - Markdown content files
- `/static/` - CSS, images, JS
- `/layouts/` - HTML templates
- `/themes/` - Theme files
- `config.toml` - Site configuration

**Refresh time:** ~300ms after saving file

## Browser Setup

**Recommended:** Use http://localhost:1313 directly (no proxy needed)

**If you see old content:**
1. Hard refresh: `Ctrl + Shift + R` (or `Cmd + Shift + R`)
2. Or open new incognito/private window

**Cache-busting is built into the site:**
```html
<link rel="stylesheet" href="/css/rkl-custom.css?t={{ now.Unix }}">
```

## Troubleshooting

### "Page not found"
Multiple servers are running. Stop everything:
```bash
./dev-stop.sh
./dev-start.sh
```

### Changes not appearing
1. Check Hugo output - should see "Change detected, rebuilding site"
2. Hard refresh browser: `Ctrl + Shift + R`
3. Check file saved correctly: `ls -l static/css/rkl-custom.css`

### Port 1313 already in use
```bash
lsof -ti :1313 | xargs kill -9
./dev-start.sh
```

## Files

- **`dev-start.sh`** - Start development server (use this)
- **`dev-stop.sh`** - Stop development server
- **`.hugo-server.pid`** - PID lock file (auto-managed)
- **`dev-simple.sh`** - Old script (deprecated, use dev-start.sh instead)
- **`dev.sh`** - Old Browser-Sync script (deprecated)

## Git Workflow

When you have working changes:

```bash
git add -A
git commit -m "Description of changes"
git push origin main
```

The site is backed up in 3 places:
1. **Local git** - `/home/mike/project/rkl/rkl.org/.git`
2. **Remote git** - https://github.com/mbbrady/rkl.org.git
3. **NAS backups** - `/mnt/nas/cluster/backups/client_backup/` (restic)

## Summary

**Start server ONCE, edit files in VS Code, see changes instantly in browser.**

No manual refresh needed. No cache clearing needed. No multiple servers competing.

If you ever see "page not found" → Run `./dev-stop.sh` then `./dev-start.sh`
