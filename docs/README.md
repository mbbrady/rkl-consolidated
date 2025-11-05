# Resonant Knowledge Lab - Main Project Folder

**Organization**: Resonant Knowledge Lab (RKL)
**Location**: Virginia, USA
**Status**: 501(c)(3) Nonprofit (est. 2025)
**Website**: [resonantknowledgelab.org](https://resonantknowledgelab.org)
**Tagline**: Ethical AI for Living Knowledge

## Mission

**Resonant Knowledge Lab (RKL)** is a nonprofit research and development organization creating **open, verifiable methods and reproducible infrastructure** that enable **large-scale reasoning systems (like GPT and Claude) and locally hosted models** to engage responsibly with **curated, locally governed knowledge domains**—without exposing or transferring them.

RKL provides the tools and methods that help institutions, practitioners, and communities **select, curate, and govern which knowledge domains** to make accessible to reasoning systems—whether **peer-reviewed literature, state-of-the-art research, institutional data, operational knowledge, or community experience**—through **secure, natural-language interaction**.

Users maintain full agency over what knowledge is exposed, how it can be accessed, and under what governance terms—allowing reasoning systems to work with the specific combination of authoritative and contextual knowledge each organization requires.

---

## Folder Structure

This folder contains TWO separate git repositories:

```
/home/mike/project/rkl/
│
├── rkl.org/              # PUBLIC repo - Website only
│   ├── .git/             # → github.com/mbbrady/rkl.org (public)
│   ├── content/          # Hugo content
│   ├── themes/           # Hugo themes
│   ├── config.toml       # Site configuration
│   └── ...
│
└── rkl-program/          # PRIVATE repo - Organizational structure
    ├── .git/             # → github.com/mbbrady/rkl (private)
    ├── 0_Admin/          # Central coordination
    ├── 1_Governance/     # Board, bylaws, policies
    ├── 2_Compliance_and_Filings/  # Legal documents
    ├── 3_Operations/     # Day-to-day management
    ├── 4_Programs_and_Research/   # Core mission work
    └── 5_Communications_and_Outreach/  # Public engagement
```

---

## Quick Start

### Working on the Website
```bash
cd /home/mike/project/rkl/rkl.org
hugo server -D          # Preview with drafts
hugo                    # Build for production

# Commit and push
git add .
git commit -m "Update website content"
git push origin main
```

### Working on Organizational Docs
```bash
cd /home/mike/project/rkl/rkl-program

# Make changes to any organizational files
vim 4_Programs_and_Research/Program_Design/Mission_and_Vision.md

# Commit and push to PRIVATE repo
git add .
git commit -m "Update mission statement"
git push origin main
```

---

## Repository Details

### 1. Public Website Repository: `rkl.org/`

**GitHub**: https://github.com/mbbrady/rkl.org (PUBLIC)
**Purpose**: Public website for resonantknowledgelab.org
**Technology**: Hugo static site generator
**Theme**: Clarity (light variant)

**Contains:**
- Website source code
- Content pages (About, Data Ethics, etc.)
- Hugo themes and configuration
- Build artifacts

**Deployment Options:**
- GitHub Pages
- Netlify
- Vercel
- Any static hosting

### 2. Private Organizational Repository: `rkl-program/`

**GitHub**: https://github.com/mbbrady/rkl (PRIVATE - to be created)
**Purpose**: Full nonprofit organizational structure and management
**Access**: Private (you + trusted collaborators only)

**Contains:**
- Organizational structure and documentation
- Governance materials (board, bylaws, policies)
- Compliance and filings (with sensitive data gitignored)
- Operations (HR, financials - with sensitive data gitignored)
- Programs and research project management
- Communications assets (drafts, logos, backups)

**Security:**
- Comprehensive `.gitignore` prevents sensitive data from being committed
- Even in private repo, sensitive files (financial records, personal info, credentials) are excluded
- See [rkl-program/SECURITY.md](rkl-program/SECURITY.md) for detailed security policy

---

## Documentation

- **[rkl-program/README.md](rkl-program/README.md)** - Detailed organizational structure
- **[rkl-program/SECURITY.md](rkl-program/SECURITY.md)** - Security and privacy guidelines
- **[rkl-program/0_Admin/File_Organization_Notes.md](rkl-program/0_Admin/File_Organization_Notes.md)** - File organization details
- **[rkl-program/5_Communications_and_Outreach/Website/README.md](rkl-program/5_Communications_and_Outreach/Website/README.md)** - Website management guide

---

## Next Steps

### 1. Rotate GitHub Personal Access Token ⚠️

Your GitHub PAT was exposed in the git remote URL. Please:
1. Go to https://github.com/settings/tokens
2. Delete or regenerate the exposed token: `github_pat_11AXFDDNA0HMLti...`
3. Git will prompt for credentials on next push (use new token or SSH)

### 2. Set Up Private GitHub Repository

```bash
# On GitHub.com:
# 1. Go to https://github.com/new
# 2. Repository name: "rkl" or "rkl-internal"
# 3. Set to PRIVATE ✓
# 4. Don't initialize with README
# 5. Create repository

# Then initialize locally:
cd /home/mike/project/rkl/rkl-program
git init
git add .gitignore README.md SECURITY.md 0_Admin/*.md
git commit -m "Initial commit: RKL organizational structure"
git branch -M main
git remote add origin git@github.com:mbbrady/rkl.git  # Use your repo URL
git push -u origin main
```

### 3. Consider Using SSH for GitHub

More secure than HTTPS with tokens:
```bash
# Generate SSH key if you don't have one
ssh-keygen -t ed25519 -C "your_email@example.com"

# Add to GitHub: https://github.com/settings/keys

# Update rkl.org remote to use SSH (optional)
cd /home/mike/project/rkl/rkl.org
git remote set-url origin git@github.com:mbbrady/rkl.org.git
```

---

## Project Context

This RKL project is part of the Betty cluster infrastructure located at `/home/mike/project/cluster/`.

**Related Projects:**
- Arctic AI collaboration
- Dissertation research on AI and knowledge systems
- Secure cluster computing infrastructure

**Main cluster docs**: `/home/mike/project/cluster/shared/docs/CLAUDE.md`

---

**Last updated**: 2025-10-15
**Structure reorganized**: 2025-10-14
