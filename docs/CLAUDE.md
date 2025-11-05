# CLAUDE.md - Resonant Knowledge Lab (Root)

**Project**: Resonant Knowledge Lab
**Organization**: Virginia 501(c)(3) Nonprofit (est. 2025)
**Mission**: Ethical AI for Living Knowledge
**Website**: https://resonantknowledgelab.org

---

## Project Structure

This folder contains **two separate git repositories** for the Resonant Knowledge Lab nonprofit:

```
/home/mike/project/rkl/
│
├── rkl.org/              📱 PUBLIC REPO - Website
│   ├── .git/             → github.com/mbbrady/rkl.org (public)
│   ├── content/          Hugo website content
│   ├── CLAUDE.md         Website-specific guidance
│   └── ...
│
├── rkl-program/          🔒 PRIVATE REPO - Organization
│   ├── .git/             → github.com/mbbrady/rkl (private)
│   ├── 0_Admin/          Admin & coordination
│   ├── 1_Governance/     Board, bylaws, policies
│   ├── 2_Compliance_and_Filings/  Legal documents
│   ├── 3_Operations/     Financials, HR, tech
│   ├── 4_Programs_and_Research/   Core mission
│   ├── 5_Communications_and_Outreach/  Public engagement
│   ├── CLAUDE.md         Org-specific guidance
│   └── ...
│
├── README.md             Main project overview
├── SETUP_COMPLETE.md     Setup completion report
└── QUICK_REFERENCE.md    Quick command reference
```

---

## Mission Statement

**Resonant Knowledge Lab (RKL)** is a nonprofit research and development organization creating **open, verifiable methods and reproducible infrastructure** that enable **large-scale reasoning systems (like GPT and Claude) and locally hosted models** to engage responsibly with **curated, locally governed knowledge domains**—without exposing or transferring them.

RKL provides the tools and methods that help institutions, practitioners, and communities **select, curate, and govern which knowledge domains** to make accessible to reasoning systems—whether **peer-reviewed literature, state-of-the-art research, institutional data, operational knowledge, or community experience**—through **secure, natural-language interaction**.

Users maintain full agency over what knowledge is exposed, how it can be accessed, and under what governance terms—allowing reasoning systems to work with the specific combination of authoritative and contextual knowledge each organization requires.

---

## Quick Navigation

### For Website Work
```bash
cd /home/mike/project/rkl/rkl.org
cat CLAUDE.md          # Website-specific guidance
hugo server -D         # Preview website
```

### For Organizational Work
```bash
cd /home/mike/project/rkl/rkl-program
cat CLAUDE.md          # Org-specific guidance
```

### Key Documents

**Mission Documents** (private repo):
- Master: `rkl-program/4_Programs_and_Research/Program_Design/Mission_and_Vision.md`
- Board: `rkl-program/1_Governance/Board/Mission_Statement_Summary.md`
- IRS: `rkl-program/2_Compliance_and_Filings/IRS/Form_1023_Application/Mission_Statement.txt`
- Guide: `rkl-program/0_Admin/Mission_Statement_Locations.md`

**Website Content** (public repo):
- Home: `rkl.org/content/_index.md`
- About: `rkl.org/content/about.md`
- Programs: `rkl.org/content/programs.md`

**Project Documentation**:
- **📋 Complete Checklist**: `rkl-program/0_Admin/RKL_Setup_Checklist.md` (🟢🟡🔴 status)
- **🚀 Quick Start**: `rkl-program/0_Admin/QUICK_START_GUIDE.md` (keep this handy!)
- Setup guide: `SETUP_COMPLETE.md`
- Quick reference: `QUICK_REFERENCE.md`
- Security policy: `rkl-program/SECURITY.md`
- GitHub setup: `rkl-program/SETUP_GITHUB.md`

**Board Meeting Setup**:
- First meeting agenda: `rkl-program/1_Governance/Organizational_Meeting/Agenda.md`
- Meeting packet status: Run `./assemble_packet.sh` in `Organizational_Meeting/Meeting_Packet/`
- Board meeting guide: `rkl-program/1_Governance/Board_Meeting_Guide.md`

---

## Repository Strategy

### Why Two Repos?

**PUBLIC** (`rkl.org`):
- Website needs to be public for visibility
- Easy for contributors to submit content
- Shows organizational legitimacy
- Standard for nonprofit websites

**PRIVATE** (`rkl-program`):
- Organizational structure contains sensitive data
- Board materials, financial templates, compliance docs
- Even with `.gitignore`, private is safer
- Can be made public later if desired

### Working with Both Repos

Each repository is **independent**:
- They have separate `.git/` folders
- Separate GitHub remotes
- Separate commit histories
- Separate `.gitignore` files

**Content relationship**:
- Website uses *public versions* of mission content
- Full organizational docs live in private repo
- When updating mission: update both repos

---

## Core Programs

RKL operates six interconnected program areas:

1. **Open Protocols for Contextual AI**
   - Model Context Protocol (MCP) implementation, policy-aware retrieval architectures (RAG+)

2. **Reference Implementations & Toolkits**
   - MCP service nodes, audit logging systems, reproducible on-prem stacks

3. **Decision Support & Knowledge Access Pilots**
   - Healthcare copilots, municipal planning assistants, environmental data synthesis

4. **Governance & Stewardship Frameworks**
   - Community consent templates, institutional data-trust frameworks

5. **Research & Applied Inquiry**
   - NSF-funded experiments on reasoning within context, AI-supported organizational learning

6. **Education & Public Engagement**
   - Workshops, curricula, red/blue-team privacy labs

See full details in `rkl-program/1_Governance/Board/Mission_Statement_Summary.md`

---

## Common Tasks

### Update Website Content
```bash
cd /home/mike/project/rkl/rkl.org
vim content/about.md
hugo server -D              # Preview
git add content/about.md
git commit -m "Update about page"
git push
```

### Update Mission Statement
```bash
cd /home/mike/project/rkl/rkl-program

# 1. Update master document
vim 4_Programs_and_Research/Program_Design/Mission_and_Vision.md

# 2. Update board document
vim 1_Governance/Board/Mission_Statement_Summary.md

# 3. Update website (separate repo)
cd ../rkl.org
vim content/about.md

# 4. Commit both repos separately
```

### Add New Program Documentation
```bash
cd /home/mike/project/rkl/rkl-program
vim 4_Programs_and_Research/Research_Projects/New_Project/README.md
```

---

## Security & Privacy

### Private Repo (.gitignore protects)
- Financial records
- Board member personal info
- Donor lists
- Signed legal documents
- Tax returns
- Credentials

### Public Repo (all visible)
- Website source code
- Public mission content
- Program descriptions
- Blog posts

**Rule of thumb**: If you wouldn't put it on the website, it goes in the private repo.

---

## Current Status (2025-10-14)

**Organizational**:
- ✅ Incorporated in Virginia (SCC819)
- ✅ Articles of Incorporation filed
- ✅ Mission and vision documented
- ⏳ EIN application pending
- ⏳ 501(c)(3) application in preparation
- ⏳ Board formation in progress

**Technical**:
- ✅ Folder structure organized
- ✅ Git repositories set up
- ✅ Website built (Hugo)
- ✅ Mission content completed
- ✅ Security policies documented
- ⏳ Website deployment (pending hosting setup)
- ⏳ Private repo pushed to GitHub (pending)

**Infrastructure**:
- ✅ Betty cluster operational
- 🔄 Closed RAG Initiative (planning phase)
- 🔄 Arctic AI collaboration (active)

---

## Project Context

RKL is part of the **Betty cluster infrastructure** at `/home/mike/project/cluster/`.

**Related projects**:
- Arctic AI collaboration (`/home/mike/project/cluster/projects/arctic-ai/`)
- Dissertation research on AI and knowledge systems
- Secure cluster computing infrastructure

**Main cluster docs**: `/home/mike/project/cluster/shared/docs/CLAUDE.md`

---

## Key Principles

When working with RKL:

1. **Mission-Driven**: Every decision aligns with ethical AI and knowledge sovereignty
2. **Security-First**: Protect sensitive data, respect privacy
3. **Transparency**: Document decisions, make processes visible (where appropriate)
4. **Community-Governed**: Partner with communities, don't extract from them
5. **Open Infrastructure**: Build auditable, reproducible systems
6. **Nonprofit Compliance**: Follow 501(c)(3) rules and best practices

---

## Next Steps

### Immediate
- [ ] Push private repo to GitHub (create private repo first)
- [ ] Deploy website to hosting (Netlify/GitHub Pages/Vercel)
- [ ] Set up domain DNS (resonantknowledgelab.org)

### Short-term (Q1 2025)
- [ ] Complete EIN application
- [ ] Draft Form 1023 (501c3 application)
- [ ] Form initial board
- [ ] Hold organizational meeting
- [ ] Adopt bylaws

### Medium-term (2025-2026)
- [ ] Launch Closed RAG Initiative pilot
- [ ] Establish first partnerships
- [ ] Apply for seed grants
- [ ] Publish RKL Code of Ethics

---

## For AI Assistants

### When working with RKL:

**Understand the dual-repo structure**:
- Two separate repositories with different purposes
- Content flows: private (master) → public (website)
- Always work in correct repo for the task

**Respect the mission**:
- Ethical AI, community governance, data sovereignty
- Not just AI adoption - ethical integration
- Support communities, don't extract from them

**Security awareness**:
- Private repo has sensitive data (even with .gitignore)
- Public repo is truly public
- When in doubt, keep it private

**Nonprofit context**:
- 501(c)(3) requires specific language and practices
- Board approval needed for significant changes
- IRS compliance is critical

### Helpful context files:
- `rkl.org/CLAUDE.md` - Website work
- `rkl-program/CLAUDE.md` - Organizational work
- `rkl-program/0_Admin/Mission_Statement_Locations.md` - Mission docs
- `QUICK_REFERENCE.md` - Common commands

---

**Last updated**: 2025-10-15
**Maintained by**: RKL founding team
**Questions**: See documentation in each repo's CLAUDE.md
