# RKL Website - Development Workflow (GPT's Recommendations)

## 🚀 Quick Start (When You Come Back)

```bash
cd /home/mike/project/rkl/rkl.org
./start-hugo-dev.sh
```

Then open **http://localhost:9000** in Chrome/Firefox with:
- **DevTools open** (F12)
- **"Disable cache" checkbox ENABLED** in Network tab

## 📝 Edit CSS and See Changes

1. Edit: `/home/mike/project/rkl/rkl.org/static/css/rkl-navy-coral.css`
2. Save (Ctrl+S)
3. Browser should auto-refresh within 1 second

## 🎨 Current Design Status

### ✅ Working:
- Navy (#0a2342) headers, menu, titles
- Coral (#ff8b7b) links and buttons
- Content structure and service cards
- Hugo builds successfully

### ❌ Not Yet Working:
- Gray background (#f9f9fb) - CSS is in the file but not displaying
- Might be CSS specificity issue or need `!important` on more selectors

## 🔧 Troubleshooting

### If you don't see changes:
1. Check DevTools → Network tab → Verify "Disable cache" is checked
2. Hard refresh: Ctrl+Shift+R
3. Check CSS file timestamp: `stat static/css/rkl-navy-coral.css`
4. Look at Network tab - CSS should show "(from disk cache: false)"

### If port 9000 is in use:
```bash
sudo lsof -i :9000
sudo kill -9 <PID>
./start-hugo-dev.sh
```

### If gray background still doesn't show:
The CSS rule is at lines 265-277 in `static/css/rkl-navy-coral.css`:
```css
body,
.hero,
section,
.services {
  background-color: #f9f9fb !important;
}
```

May need to add more `!important` overrides or inspect with DevTools to see what's actually being applied.

## 📦 What We Created

- **rkl-web conda env** at `/opt/conda-envs/envs/rkl-web` (has Node.js, Python, livereload)
- **start-hugo-dev.sh** - Clean startup script with GPT's recommended flags
- **WORKFLOW-SUMMARY.md** - Summary of current status
- **Custom CSS** at `static/css/rkl-navy-coral.css` with navy/coral theme

## 🤝 VS Code + Hugo Workflow

GPT recommends:
1. You run Hugo server (via start-hugo-dev.sh)
2. Claude Code edits files in VS Code
3. You preview in browser with DevTools cache disabled
4. Hugo auto-rebuilds and browser auto-refreshes

This should give you the instant feedback loop you need for design iteration.

## 📚 Alternative Tools (If Hugo Workflow Still Frustrating)

- **Figma** (https://figma.com) - Design mockups visually first
- **Deploy to Netlify** - Test on real URL, no local caching issues
- **VS Code Live Server extension** - Right-click HTML → Open with Live Server

## 🧹 Clean Slate Command

If you want to start completely fresh:
```bash
cd /home/mike/project/rkl/rkl.org
pkill -9 hugo
pkill -9 python
rm -rf public/ resources/ .hugo_build.lock
./start-hugo-dev.sh
```

Good luck! The gray background mystery awaits... 🕵️
