# RKL Website - Current Status & Workflow Summary

## What Actually Works (From Screenshot 8)

✅ **Navy color scheme is working** - Header, menu, and service titles are navy
✅ **Hugo static site builds successfully**
✅ **Content is correct** - Subtitle, contact info, 6 service cards all display

## What's NOT Working

❌ **Gray background (#f9f9fb)** - Still showing white despite CSS being in the files
❌ **Browser caching** - Extreme caching issues prevent seeing changes
❌ **Live reload** - None of the attempted workflows solved the instant-preview problem

## Current File Locations

**Website files**: `/home/mike/project/rkl/rkl.org/`
**CSS file**: `/home/mike/project/rkl/rkl.org/static/css/rkl-navy-coral.css`
**Config**: `/home/mike/project/rkl/rkl.org/config.toml`

## Colors Configured (But Gray Background Not Showing)

```css
Navy: #0a2342 (for text, headers, menu)
Coral: #ff8b7b (for accents, buttons, links)
Gray background: #f9f9fb (CONFIGURED but not displaying)
White cards: #ffffff (for service cards)
```

## Recommended Next Steps

### Option 1: Use Figma for Design First
- Design mockup in Figma (https://figma.com)
- Export CSS when happy with design
- Then implement in Hugo once

### Option 2: Deploy to Netlify/Vercel
- Push to GitHub
- Deploy to real URL
- Test on actual web server (eliminates local caching issues)

### Option 3: Use WordPress/Webflow
- Visual page builder
- WYSIWYG editing
- Export static HTML when done

## Hugo Build Command (When Ready)

```bash
cd /home/mike/project/rkl/rkl.org
/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo
# Builds to public/ folder
```

## CSS File Status

The gray background CSS IS in the file at lines 265-277:

```css
/* Light gray base background - Research Institute aesthetic */
body,
.hero,
section,
.services {
  background-color: #f9f9fb !important;
}

/* Keep cards white for contrast against gray background */
.services .service {
  background-color: #ffffff !important;
  box-shadow: 0 1px 3px rgba(10, 35, 66, 0.05);
}
```

But it's not showing in any browser due to caching or CSS specificity issues.

## Cleanup Needed

Multiple Hugo servers running on different ports - need to kill all and start fresh when you return to this.

```bash
# Kill all servers
pkill -9 hugo
pkill -9 python

# Start one clean server
cd /home/mike/project/rkl/rkl.org
/opt/miniforge3/pkgs/hugo-0.151.0-hc83c272_0/bin/hugo server
# Then visit http://localhost:1313/
```

## What We Learned

Hugo + Brave browser + Linux = Severe caching issues that make rapid design iteration impractical without:
1. Different browser
2. Production deployment
3. Alternative visual design tools

Better to design visually first, then implement in Hugo once the design is finalized.
