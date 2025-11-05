# Website Folder Structure

This folder contains all website-related assets for **Resonant Knowledge Lab**.

## Folder Organization

## Hugo Website Location

**The main Hugo website has been moved to:** `/home/mike/project/rkl/rkl.org/`

This is a separate public GitHub repository at: `https://github.com/mbbrady/rkl.org`

**Current Configuration:**
- Base URL: https://resonantknowledgelab.org/
- Theme: Clarity (light variant)
- Accent Color: #0F4C81

**Development Commands:**
```bash
cd /home/mike/project/rkl/rkl.org
hugo server -D          # Run local dev server with drafts
hugo                    # Build production site
```

**Current Pages:**
- Home page (_index.md)
- About page
- Data Ethics page
- Projects (planned)
- Contact (planned)

### `Draft_Content/`
Work-in-progress content, blog posts, and page drafts before adding to Hugo

### `Images_and_Logos/`
Brand assets, logos, graphics for website and promotional materials

### `Web_Backups/`
Periodic backups of the live site and configuration files

## Repository Structure

- **Public Website Repo**: `/home/mike/project/rkl/rkl.org/` → `github.com/mbbrady/rkl.org`
- **Private Org Repo**: `/home/mike/project/rkl/rkl-program/` → `github.com/mbbrady/rkl` (private)

## Deployment

The Hugo site in `/home/mike/project/rkl/rkl.org/public/` can be deployed to:
- GitHub Pages (from rkl.org repo)
- Netlify
- Vercel
- Any static hosting service

## Related Folders

See also:
- `../Press_and_Media/` for press releases and media coverage
- `../Reports_and_Publications/` for downloadable reports
- `../../4_Programs_and_Research/Program_Design/Mission_and_Vision.md` for organizational messaging

---

Last updated: 2025-10-14
