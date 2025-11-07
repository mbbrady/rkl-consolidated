# RKL Deployment Status

**Date:** November 5, 2025

## Repository Migration Complete ✅

All RKL projects have been consolidated into this single repository: **rkl-consolidated**

## Current Setup

### Active Deployments:

1. **Board Review Site (Old):**
   - URL: `https://rkl-org.pages.dev/`
   - Repository: `mbbrady/rkl.org` (old repo)
   - Status: Active for board member review
   - Action: Keep active until board review complete

2. **Development Site (New - Password Protected):**
   - URL: `https://15298256.rkl-org.pages.dev/`
   - Repository: `mbbrady/rkl-consolidated` (THIS REPO)
   - Status: Active, protected by Cloudflare Access
   - Purpose: Development and updates
   - Access: Email-based authentication required

3. **Live Domain:**
   - Domain: `resonantknowledgelab.org`
   - Status: Not yet configured (placeholder site pending)

## Repository Structure

```
rkl-consolidated/
├── website/              # Main Hugo website
├── placeholder/          # Simple landing page
├── program/             # Organizational documents
├── demos/               # Research demonstrations
│   ├── marine-research-demo/
│   └── orp-marine-plastics-storymap/
└── docs/                # General documentation
```

## Important Notes

### ⚠️ ALL FUTURE UPDATES GO TO THIS REPO (rkl-consolidated)

- **DO NOT** update `mbbrady/rkl.org` (old repo)
- **DO NOT** update `mbbrady/rkl-placeholder` (old repo)
- **ALL changes** should be committed to `mbbrady/rkl-consolidated`

### Git Workflow

When making website changes:
```bash
cd /home/mike/project/rkl-consolidated
# Make your changes to files in website/ directory
git add .
git commit -m "Your commit message"
git push
```

Cloudflare Pages will automatically deploy changes to `https://15298256.rkl-org.pages.dev/`

## Build Configuration

The site successfully builds with:
- **Hugo Version:** `extended_0.151.2` (must be extended for SCSS support)
- **Build Command:** `hugo --gc --minify`
- **Root Directory:** `website`
- **Environment Variables:**
  - `HUGO_VERSION` = `extended_0.151.2`
  - `HUGO_ENV` = `production`

### Important: Cloudflare Project Type
- **MUST use "Pages"** (not "Workers") when creating Cloudflare projects
- Workers are for serverless functions, Pages are for static sites
- Hugo sites require Pages deployment

## Next Steps

1. ✅ Consolidate repositories
2. ✅ Deploy from consolidated repo
3. ✅ Password protect development site
4. ⏳ Board review on old site
5. ⏳ Create and deploy placeholder to resonantknowledgelab.org
6. ⏳ After board approval, point resonantknowledgelab.org to main site
7. ⏳ Archive old repositories

## Old Repositories (DO NOT UPDATE)

These will be archived after migration is complete:
- `mbbrady/rkl.org`
- `mbbrady/rkl-placeholder`
- `mbbrady/rkl` (already consolidated into program/)
- `mbbrady/marine-research-demo` (already consolidated into demos/)
- `mbbrady/orp-marine-plastics-storymap` (already consolidated into demos/)
