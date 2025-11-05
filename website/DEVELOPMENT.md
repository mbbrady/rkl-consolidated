# RKL Website - Development Workflow

## Quick Start

```bash
cd /home/mike/project/rkl/rkl.org
./dev-simple.sh
```

Then open **http://localhost:1313** in your browser.

## The Workflow

1. **Start development server**: `./dev-simple.sh` (run once, leave it running)
2. **Edit files in VS Code**: content, CSS, layouts
3. **Save file** (Ctrl+S)
4. **Hugo auto-rebuilds and LiveReload refreshes browser** within 1 second

That's it! No manual rebuilds, no cache clearing, no refresh button.

## What Gets Watched

The dev server automatically watches and rebuilds when you change:
- ✅ `content/**/*` - All Markdown content files
- ✅ `static/**/*` - CSS, images, JavaScript
- ✅ `layouts/**/*` - Hugo templates
- ✅ `config.toml` - Site configuration

## URL

- **Development server**: http://localhost:1313 ← Hugo with LiveReload

## Common Tasks

### Edit Page Content
```bash
# Edit in VS Code, save, see changes instantly
vim content/about.md
vim content/programs.md
vim content/_index.md
```

### Edit Styling
```bash
# Edit CSS, save, see changes instantly
vim static/css/rkl-custom.css
```

### Edit Page Layout
```bash
# Edit Hugo templates, save, see changes instantly
vim layouts/_default/baseof.html
```

### Stop Development Server
Press `Ctrl+C` in the terminal where `./dev-simple.sh` is running.

## Environment

Uses the **rkl-web** conda environment at `/opt/conda-envs/envs/rkl-web`

Tools installed:
- Hugo 0.151.2 (with native LiveReload)

## Troubleshooting

### Port 1313 already in use
```bash
# Find and kill the process
sudo lsof -i :1313
sudo kill -9 <PID>

# Or just run ./dev-simple.sh again (it kills old processes)
```

### Changes not showing
1. Check terminal - Hugo should show "Change detected, rebuilding site"
2. Check browser console - Hugo injects LiveReload script automatically
3. The CSS has cache-busting timestamps in baseof.html, so no manual refresh needed

## Building for Production

When ready to deploy:

```bash
cd /home/mike/project/rkl/rkl.org
/opt/conda-envs/envs/rkl-web/bin/hugo

# Site builds to public/ folder
# Upload public/ folder to hosting
```

## Technology Stack

- **Hugo**: Static site generator with native LiveReload
- **Serif Theme**: Hugo theme (customized)
- **Conda**: Environment management

## How It Works

The key to instant updates without cache issues:

1. **Hugo LiveReload**: Built-in WebSocket connection that triggers browser refresh
2. **Cache-busting CSS**: `/css/rkl-custom.css?t={{ now.Unix }}` in baseof.html forces fresh CSS load
3. **Aggressive rebuild flags**: `--disableFastRender`, `--noHTTPCache`, `--cleanDestinationDir`, `--forceSyncStatic`
4. **File polling**: `--poll 300ms` ensures changes are detected reliably

## File Structure

```
rkl.org/
├── content/          # Markdown content (edit these)
├── static/           # CSS, images (edit these)
├── layouts/          # HTML templates (rarely edit)
├── themes/           # Base theme (don't edit)
├── config.toml       # Site config
├── dev.sh           # Start development server
└── public/           # Generated site (don't commit)
```

## Tips

1. **Keep dev-simple.sh running** - Leave it in a terminal, minimize it
2. **Use VS Code** - Best editor experience
3. **Use real browser** - Not VS Code preview
4. **Edit, save, see** - That's the whole workflow!
5. **Watch the terminal** - Hugo logs every rebuild and file sync

---

**Last Updated**: 2025-10-21
