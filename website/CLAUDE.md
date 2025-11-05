# CLAUDE.md - Resonant Knowledge Lab Website (Public Repo)

**Project**: Resonant Knowledge Lab - Public Website
**Repository**: Public website repo
**Type**: Hugo static site
**URL**: https://resonantknowledgelab.org

---

## Project Overview

This is the **public website repository** for Resonant Knowledge Lab (RKL), a Virginia-based 501(c)(3) nonprofit.

**Mission**: RKL creates **open, verifiable methods and reproducible infrastructure** that enable **large-scale reasoning systems (like GPT and Claude) and locally hosted models** to engage responsibly with **curated, locally governed knowledge domains**—without exposing or transferring them.

**Tagline**: Ethical AI for Living Knowledge

---

## Technology Stack

- **Static Site Generator**: Hugo
- **Theme**: Clarity (light variant)
- **Language**: English (en-us)
- **Accent Color**: #0F4C81 (blue)
- **Deployment**: GitHub Pages / Netlify / Vercel (TBD)

---

## Repository Structure

```
rkl.org/
├── archetypes/          # Hugo content templates
├── content/             # Website content (Markdown)
│   ├── _index.md           # Home page
│   ├── about.md            # Mission, vision, principles
│   ├── programs.md         # Core program areas
│   ├── data-ethics.md      # Data ethics page
│   └── projects/           # Future project pages
│
├── static/              # Static assets (images, files)
├── themes/clarity/      # Hugo Clarity theme
├── public/              # Built site (DO NOT commit - gitignored)
├── config.toml          # Site configuration
└── .gitignore           # Excludes build artifacts
```

---

## Key Content Pages

### Home Page (`content/_index.md`)
- Hero title: "Secure Co-Design Between Frontier AI and Human Knowledge"
- Mission statement (one-sentence version)
- Welcome text

### About Page (`content/about.md`)
- Full mission and vision
- Guiding principles (6 core principles)
- Core purpose
- Organizational role
- About RKL section

### Programs Page (`content/programs.md`)
- Six core program areas
- Year 1 focus (2025-2026)
- Illustrative use cases across sectors
- Call to action for collaboration

### Data Ethics Page (`content/data-ethics.md`)
- (Existing content - may need updating)

---

## Mission Statement (Website Version)

### One-Sentence (Elevator Pitch)
> RKL provides open infrastructure that enables reasoning systems like GPT and Claude to work with knowledge domains organizations choose to expose—from peer-reviewed research to institutional data—without transferring or compromising sensitive information.

### One-Paragraph (Website/Summary)
> Resonant Knowledge Lab (RKL) is a nonprofit creating open, verifiable methods that enable large-scale reasoning systems (like GPT and Claude) and locally hosted models to engage responsibly with curated, locally governed knowledge domains—without exposing or transferring them. We provide tools and methods that help organizations select, curate, and govern which knowledge to make accessible to reasoning systems, maintaining full agency over what is exposed and how it can be used.

### Tagline (Shortest)
> Ethical AI for Living Knowledge

---

## Core Programs (Brief)

1. **Open Protocols for Contextual AI**
2. **Reference Implementations & Toolkits**
3. **Decision Support & Knowledge Access Pilots**
4. **Governance & Stewardship Frameworks**
5. **Research & Applied Inquiry**
6. **Education & Public Engagement**

See `/content/programs.md` for full details.

---

## Development Workflow

### Local Development
```bash
cd /home/mike/project/rkl/rkl.org

# Preview with drafts
hugo server -D

# Preview without drafts (production mode)
hugo server

# View at: http://localhost:1313
```

### Building for Production
```bash
hugo

# Output goes to /public/ directory
# Deploy contents of /public/ to hosting provider
```

### Git Workflow
```bash
# After making content changes
git status
git add content/
git commit -m "Update about page with new mission statement"
git push origin main
```

---

## Configuration (`config.toml`)

Key settings:
- **baseURL**: `https://resonantknowledgelab.org/`
- **title**: Resonant Knowledge Lab
- **theme**: clarity
- **description**: Full mission statement for SEO
- **tagline**: "Ethical AI for Living Knowledge"

Navigation menu order:
1. About
2. Programs
3. Data Ethics
4. Contact

---

## Related Repositories

### Private Organizational Repo
- **Location**: `/home/mike/project/rkl/rkl-program/`
- **GitHub**: `github.com/mbbrady/rkl` (private)
- **Purpose**: Full nonprofit organizational structure
- **Contains**: Board documents, compliance filings, detailed mission docs

**Content relationship**:
- This website uses *public versions* of mission content
- Full mission documents live in private repo
- When mission changes, update both repos

---

## Content Guidelines

### This is a PUBLIC repository

Everything here is visible to the world. Guidelines:

✅ **DO include**:
- Mission, vision, and values
- Program descriptions
- Blog posts and updates
- Public research findings
- Contact information
- Educational content

❌ **DO NOT include**:
- Board member personal details
- Financial information
- Donor lists
- Internal strategy documents
- Anything not intended for public view

### Writing Style

- Clear and accessible language
- Focus on impact and values
- Avoid jargon where possible
- When using technical terms, explain them
- Emphasize ethics, community, and transparency
- Use active voice

### Tone

- Professional but approachable
- Passionate about ethical AI
- Respectful of diverse knowledge systems
- Transparent about methods and principles
- Invitation to collaborate

---

## Hugo Tips

### Creating New Pages
```bash
hugo new content/contact.md
hugo new content/blog/first-post.md
```

### Working with Drafts
```markdown
---
title: "New Page"
draft: true
---
```
Drafts only show with `hugo server -D`

### Front Matter
Each content file starts with YAML front matter:
```yaml
---
title: "Page Title"
description: "SEO description"
date: 2025-10-14
---
```

### Markdown Formatting
- Headers: `## Header`, `### Subheader`
- Bold: `**text**`
- Links: `[text](url)`
- Lists: `- item` or `1. item`

---

## Deployment Options

### GitHub Pages (Free)
```bash
# In repository settings on GitHub:
# Settings → Pages → Source: gh-pages branch
```

### Netlify (Recommended for Hugo)
- Connect GitHub repo
- Build command: `hugo`
- Publish directory: `public`
- Auto-deploy on push

### Vercel
- Import GitHub repo
- Framework preset: Hugo
- Auto-deploy on push

---

## SEO & Analytics

### Current SEO Setup
- Site description in `config.toml`
- Page descriptions in front matter
- `robots.txt` enabled
- Sitemap auto-generated

### Future Enhancements
- Add Google Analytics (pending board approval)
- Set up Google Search Console
- Add social media meta tags
- Create Open Graph images

---

## Maintenance Tasks

### Regular Updates
- Update mission content when changed in private repo
- Add new blog posts about projects and research
- Update program descriptions as initiatives launch
- Add case studies and impact stories

### Before Publishing
- Run `hugo` to check for build errors
- Preview locally with `hugo server`
- Check all links work
- Review for typos
- Ensure content aligns with nonprofit mission

---

## Current Status

### Completed ✅
- ✅ Hugo site configured with Clarity theme
- ✅ Mission and vision content updated
- ✅ Core pages created (Home, About, Programs)
- ✅ Enhanced home page with comprehensive sections
- ✅ RKL logo integrated (concentric circles design)
- ✅ Custom home layout created (`layouts/index.html`)
- ✅ GitHub Actions deployment pipeline configured
- ✅ CNAME file created for custom domain
- ✅ Automatic deployment to `gh-pages` branch working

### In Progress ⏳
- ⏳ **DNS Configuration** - Need to add DNS records at domain registrar
- ⏳ **Enable GitHub Pages** - Ready to enable when site is polished
- ⏳ Contact page (needs creation)
- ⏳ Blog setup (future)

### Site Ready But NOT LIVE
The site is built and ready at the `gh-pages` branch, but **NOT publicly accessible** until you enable GitHub Pages in repository settings.

---

## Deployment Setup (GitHub Pages)

### Current Deployment Status
- **Pipeline**: ✅ Working (auto-deploys on push to `main`)
- **Built Site**: ✅ Available in `gh-pages` branch
- **Custom Domain**: ✅ Configured (`resonantknowledgelab.org`)
- **Public Site**: ❌ NOT live (GitHub Pages disabled)

### GitHub Actions Workflow
Location: `.github/workflows/deploy.yml`

**What it does:**
1. Triggers on every push to `main` branch
2. Checks out code with submodules
3. Sets up Hugo (latest extended version)
4. Builds site with `hugo --minify`
5. Deploys to `gh-pages` branch

**Monitor workflow**: https://github.com/mbbrady/rkl.org/actions

### To Make Site Live (When Ready)

**Step 1: Enable GitHub Pages**
1. Go to: https://github.com/mbbrady/rkl.org/settings/pages
2. Under "Source", select: **Deploy from a branch**
3. Choose branch: **gh-pages** / **/ (root)**
4. Custom domain should show: **resonantknowledgelab.org**
5. Check "Enforce HTTPS" (recommended)

**Step 2: Configure DNS at Domain Registrar**

For apex domain (`resonantknowledgelab.org`), add these **A records**:
```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

For www subdomain (optional), add **CNAME record**:
```
www.resonantknowledgelab.org → mbbrady.github.io
```

**Step 3: Wait for DNS Propagation**
- DNS changes take 24-48 hours to propagate
- Check DNS status: `dig resonantknowledgelab.org`
- GitHub will auto-issue SSL certificate once DNS is configured

### To Take Site Down
1. Go to: https://github.com/mbbrady/rkl.org/settings/pages
2. Change "Source" to **"None"**
3. Site immediately goes offline

---

## Helpful Commands

### Preview the site locally
```bash
# Using conda environment with Hugo (environments stored in /opt/conda-envs/)
/opt/conda-envs/envs/rkl-web/bin/hugo server -D

# Or activate the environment first:
source /home/mike/miniforge3/bin/activate /opt/conda-envs/envs/rkl-web
cd /home/mike/project/rkl/rkl.org
hugo server -D

# View at: http://localhost:1313
```

### Build for production
```bash
cd /home/mike/project/rkl/rkl.org && hugo
```

### Deploy changes
```bash
cd /home/mike/project/rkl/rkl.org
git add .
git commit -m "Update content"
git push origin main
# GitHub Actions will auto-deploy to gh-pages
```

### Check deployment status
```bash
# View recent workflow runs
gh run list --limit 5

# View specific run
gh run view <run-id>
```

### Check for broken links
```bash
hugo server &
wget --spider -r -nd -nv -l 3 http://localhost:1313/ 2>&1 | grep -B1 'broken link'
```

### Search content
```bash
grep -r "keyword" content/
```

---

## Website Structure

### Custom Files Created
- `layouts/index.html` - Custom home page layout (overrides theme's post archive)
- `static/logos/rkl-logo.png` - RKL logo with concentric circles
- `static/CNAME` - Custom domain configuration for GitHub Pages
- `.gitignore` - Excludes build artifacts and sensitive files

### Key Content Files
- `content/_index.md` - Enhanced home page with 7 sections
- `content/about.md` - Mission, vision, guiding principles
- `content/programs.md` - Detailed program areas with objectives
- `config.toml` - Site configuration with logo and custom domain

### Hugo Environment
- **Conda Environment**: `rkl-web`
- **Location**: `/opt/conda-envs/envs/rkl-web` (all conda environments moved to /opt)
- **Hugo Version**: v0.151.0+extended
- **Activate**: `source /home/mike/miniforge3/bin/activate /opt/conda-envs/envs/rkl-web`
- **Direct Path**: `/opt/conda-envs/envs/rkl-web/bin/hugo`

---

## Next Steps

### Immediate (Before Going Live)
1. **Test the live site** once DNS is configured
2. **Review all pages** for content accuracy and typos
3. **Test on mobile devices** to ensure responsive design
4. **Add contact page** with email and social links
5. **Review SEO metadata** on all pages

### Short Term (1-2 Weeks)
1. **Set up Google Analytics** (pending board approval)
2. **Create blog section** for updates and announcements
3. **Add team/board page** with appropriate public information
4. **Create project showcase pages** for Closed RAG Initiative and other programs
5. **Add newsletter signup** (if desired)

### Medium Term (1-3 Months)
1. **Publish first blog post** about RKL launch
2. **Add case studies** and success stories
3. **Create resources section** with downloadable materials
4. **Integrate social media feeds** (if accounts exist)
5. **Set up search functionality** (Clarity theme supports it)

---

## Key Principles for AI Assistants

When working with this website:

1. **Public Content Only**: Everything here is visible to the world
2. **Mission Alignment**: All content should reflect RKL's ethical AI mission
3. **Accessibility**: Write clearly for diverse audiences
4. **Consistency**: Match tone and style of existing content
5. **SEO-Friendly**: Use descriptive titles and meta descriptions
6. **Build Before Deploy**: Always test with `hugo` before pushing
7. **Hugo Environment**: Always activate `rkl-web` conda environment before running Hugo
8. **Auto-Deploy**: Remember that pushing to `main` triggers automatic deployment

---

## Questions & Support

- **Hugo Documentation**: https://gohugo.io/documentation/
- **Clarity Theme**: https://github.com/chipzoller/hugo-clarity
- **GitHub Pages Docs**: https://docs.github.com/en/pages
- **Mission Content**: See private repo `rkl-program/` for full versions
- **Organizational Context**: See `../rkl-program/CLAUDE.md`
- **GitHub Repository**: https://github.com/mbbrady/rkl.org
- **GitHub Actions**: https://github.com/mbbrady/rkl.org/actions

---

## Recent Updates (2025-10-15)

### Mission Statement Revision
- **Complete mission overhaul** - Changed from values-focused to infrastructure-focused
- **Key clarification**: Organizations choose what knowledge to expose; RKL provides infrastructure
- **GPT/Claude examples added** for general audience clarity
- **Updated tagline**: "Trusted Reasoning for Living Knowledge"
- **New architecture emphasis**: MCP, RAG+, policy-aware retrieval

### Compute Infrastructure Addition
- Added "Independent Computational Infrastructure" section to programs page
- Documents RKL's local GPU nodes, secure networking, monitoring systems
- Emphasizes research independence from commercial cloud providers
- Links to annual Infrastructure Transparency Report

### Content Updates
- **Home page** (_index.md): New mission, 6 revised program areas, updated principles
- **About page** (about.md): Full mission/vision replacement with organizational role
- **Programs page** (programs.md): Complete rewrite with use cases table and Year 1 focus
- **Config** (config.toml): Updated description and tagline for SEO

### Files Changed
- 4 content files updated
- All changes committed and deployed via GitHub Actions
- Website auto-rebuilt and available (not yet publicly live)

---

## CSS Styling Notes

### Lines of Effort Section Card Normalization

The homepage "Lines of Effort" section uses equal-height cards with normalized heading heights to ensure consistent alignment across the grid. This is critical for visual consistency when card titles have different lengths.

**Location**: `/static/css/rkl-custom.css`

**Key CSS for Card Heading Alignment**:
```css
/* Normalize card heading height for alignment */
.effort-card h4 {
  font-family: var(--bs-font-serif, 'Libre Baskerville', serif);
  font-size: 1.1rem;
  font-weight: 600;
  line-height: 1.3;
  color: #0B2545;
  min-height: 3.5rem;   /* ensures even vertical rhythm */
  margin-bottom: 0.75rem;
}
```

**Why this matters**:
- Cards have 1-2 word titles (e.g., "Open Protocols", "Field Pilots")
- `min-height: 3.5rem` reserves consistent space for all titles
- This prevents body text from starting at different heights
- Creates professional, aligned grid layout across all 6 cards
- Works with flexbox equal-height cards (`.d-flex` + `.flex-fill`)

**Card Animation**:
- Scroll-triggered fade-in using IntersectionObserver (vanilla JS, no dependencies)
- CSS transitions with staggered delays (0.1s, 0.2s between cards)
- Cards start at `opacity: 0` and `translateY(10px)`, animate to visible on scroll
- Script location: `/layouts/_default/baseof.html` (before closing `</body>`)

**Implementation Note - Title Strategy**:

The Lines of Effort cards use **short, scannable titles** on the homepage for clarity and visual rhythm:
- Active Programs: "Open Protocols", "Reference Toolkits", "Field Pilots"
- Emerging Areas: "Governance Frameworks", "Applied Research", "Education & Outreach"

**For detailed pages** (About, Programs, documentation), use the **extended descriptive forms**:
- "Open Protocols for Contextual AI"
- "Reference Implementations & Toolkits"
- "Decision Support & Field Pilots"
- "Governance & Stewardship Frameworks"
- "Research & Applied Inquiry"
- "Education & Public Engagement"

This keeps the public front page concise while internal pages remain authoritative—exactly the tone a research-driven nonprofit like RKL should project.

---

**Last updated**: 2025-10-22
**Status**: Lines of Effort section complete with animations and normalized card heights
**Next milestone**: Review updated content, then configure DNS and enable GitHub Pages when ready to go live
