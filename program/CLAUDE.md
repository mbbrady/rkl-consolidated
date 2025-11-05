# CLAUDE.md - Resonant Knowledge Lab (Private Repo)

**Project**: Resonant Knowledge Lab - Organizational Structure
**Repository**: Private organizational management repo
**Type**: Nonprofit 501(c)(3) organizational documents
**Location**: Virginia, USA

---

## Project Overview

This is the **private organizational repository** for Resonant Knowledge Lab (RKL), a Virginia-based 501(c)(3) nonprofit.

**Mission**: RKL creates **open, verifiable methods and reproducible infrastructure** that enable **large-scale reasoning systems (like GPT and Claude) and locally hosted models** to engage responsibly with **curated, locally governed knowledge domains**—without exposing or transferring them. Organizations maintain full agency over what knowledge is exposed, how it can be accessed, and under what governance terms.

---

## Repository Structure

```
rkl-program/
├── 0_Admin/                          # Coordination & management
│   ├── Mission_Statement_Locations.md    # Where all mission docs are
│   ├── File_Organization_Notes.md        # Organization history
│   └── Git_Repository_Strategy.md        # Repo setup guide
│
├── 1_Governance/                     # Legal foundation
│   ├── Board/
│   │   └── Mission_Statement_Summary.md  # FULL board version (9 sections)
│   ├── Bylaws/
│   ├── Organizational_Meeting/
│   └── Policies/
│
├── 2_Compliance_and_Filings/         # Legal & regulatory
│   ├── Incorporation/
│   │   └── Articles_of_Incorporation_SCC819.pdf  # Virginia SCC filing
│   ├── IRS/
│   │   └── Form_1023_Application/
│   │       └── Mission_Statement.txt     # IRS-compliant version
│   └── Virginia/
│
├── 3_Operations/                     # Day-to-day
│   ├── Financials/
│   ├── HR_and_Volunteers/
│   └── Technology/
│
├── 4_Programs_and_Research/          # Core mission work
│   ├── Program_Design/
│   │   └── Mission_and_Vision.md         # MASTER mission document
│   ├── Research_Projects/
│   │   └── Arctic_AI/
│   └── Ethics_and_Data_Governance/
│
└── 5_Communications_and_Outreach/    # Public engagement
    ├── Website/
    │   └── README.md                     # Website in ../rkl.org/
    ├── Fundraising/
    └── Press_and_Media/
```

---

## Key Files & Their Purpose

### Mission & Vision Documents

**Master Document** (most comprehensive):
- `4_Programs_and_Research/Program_Design/Mission_and_Vision.md`
- Use for: Grant applications, strategic planning, comprehensive reference

**Board Document** (full operational detail):
- `1_Governance/Board/Mission_Statement_Summary.md`
- Contains: 10 sections including all program areas, Year 1 scope, use cases, organizational role
- Use for: Board packets, governance materials, strategic discussions

**IRS Document** (compliance language):
- `2_Compliance_and_Filings/IRS/Form_1023_Application/Mission_Statement.txt`
- Contains: IRS-compliant language for 501(c)(3) application
- Use for: Tax filings, IRS correspondence

### Key Admin Documents

- `0_Admin/Mission_Statement_Locations.md` - Quick reference guide for all mission docs
- `SECURITY.md` - Data classification and security policy
- `SETUP_GITHUB.md` - GitHub initialization guide (if not yet pushed)

---

## Important Context

### This is a PRIVATE Repository

**What's in git**:
- Organizational structure and documentation
- Template files and README files
- Mission and program documentation
- Folder structure

**What's NOT in git** (protected by .gitignore):
- Financial records (bank statements, budgets, receipts)
- Board member personal information
- Donor lists and fundraising data
- Signed legal documents
- Tax returns and IRS correspondence
- Any files with sensitive personal or financial data

### Related Repositories

**Public Website** (separate repo):
- Location: `/home/mike/project/rkl/rkl.org/`
- GitHub: `github.com/mbbrady/rkl.org` (public)
- Purpose: Hugo static site for resonantknowledgelab.org
- Contains: Public-facing content, mission statement (public version)

**Betty Cluster** (parent infrastructure):
- Location: `/home/mike/project/cluster/`
- This RKL project is part of the Betty cluster infrastructure
- See: `/home/mike/project/cluster/shared/docs/CLAUDE.md`

---

## Working with This Repository

### Mission Statement Edits

When updating the mission statement:

1. **Always start with the master document**:
   ```bash
   vim 4_Programs_and_Research/Program_Design/Mission_and_Vision.md
   ```

2. **Get board approval** before finalizing changes

3. **Update derivative documents**:
   - Board summary (`1_Governance/Board/Mission_Statement_Summary.md`)
   - IRS version (if significant changes)
   - Website content (in separate `rkl.org` repo)

4. **Document locations guide**:
   ```bash
   vim 0_Admin/Mission_Statement_Locations.md
   ```

### Adding Organizational Documents

Before committing any file, ask:
- ❌ Does it contain personal information?
- ❌ Does it contain financial data?
- ❌ Does it contain donor information?
- ❌ Does it contain credentials or passwords?
- ✅ Is it a template, structure, or documentation file?

**When in doubt, don't commit it.** The `.gitignore` protects most sensitive patterns, but review carefully.

### File Naming Conventions

- Use placeholder filenames: `Budget_[YYYY].xlsx`, `Bylaws_[date].pdf`
- Replace `[YYYY]` and `[date]` with actual dates when files are created
- Keep consistent naming across similar documents
- Use underscores, not spaces (for command-line compatibility)

---

## Core Programs (For Context)

RKL operates six interconnected program areas:

1. **Open Protocols for Contextual AI** - MCP implementation, policy-aware retrieval architectures (RAG+)
2. **Reference Implementations & Toolkits** - MCP service nodes, audit logging, reproducible on-prem stacks
3. **Decision Support & Knowledge Access Pilots** - Healthcare copilots, municipal planning assistants, environmental data synthesis
4. **Governance & Stewardship Frameworks** - Consent templates, institutional data-trust frameworks
5. **Research & Applied Inquiry** - NSF-funded experiments on reasoning within context, AI-supported learning
6. **Education & Public Engagement** - Workshops, curricula, red/blue-team privacy labs

See full details in `1_Governance/Board/Mission_Statement_Summary.md`

---

## Current Status (2025)

- **Incorporation**: ✅ Complete (Virginia SCC, 2025)
- **Articles of Incorporation**: ✅ Filed (SCC819)
- **EIN**: ⏳ Pending
- **501(c)(3) Application**: ⏳ In preparation
- **Board Formation**: ⏳ In progress
- **Website**: ✅ Live (resonantknowledgelab.org)
- **Core Infrastructure**: 🔄 Betty cluster operational

---

## 🖥️ Dashboard (NEW!)

### Quick Management Interface
**Location**: `dashboard/`
**Purpose**: Web-based task and file management for daily RKL work

### For Users: Just Ask Me!
**To start the dashboard, simply say:**
> "Start the RKL dashboard"

I'll run the command and give you the URL to open in your browser.

### For AI Assistants: How to Start It
When user requests to start the dashboard, run:
```bash
cd /home/mike/project/rkl/rkl-program/dashboard && python3 app.py
```

**What happens:**
- Starts Flask web server on port 5000
- Dashboard available at http://localhost:5000
- User can open in browser to see visual interface
- Leave it running in background

**Alternative startup** (with install check):
```bash
cd /home/mike/project/rkl/rkl-program/dashboard && ./start_dashboard.sh
```

### Dashboard Features
- 📊 Visual progress tracking (🟢🟡🔴 status)
- 📋 Interactive task list with filtering
- 📦 Meeting packet assembly status (live refresh)
- ⚡ One-click quick actions (preview website, assemble packet)
- 📁 Open files in VS Code from browser
- 📄 Recent file browser (10 most recently edited)
- 🚨 Critical next steps highlighted

### Safety Notes
- **Read-only**: Dashboard only reads your files, doesn't edit them
- **Local only**: Runs on your computer, no cloud/network access
- **User-controlled actions**: Quick actions only run when user clicks buttons
- **VS Code integration**: File links open in VS Code for safe editing

**See**: `dashboard/README.md` for full documentation
**See**: `dashboard/DASHBOARD_SUMMARY.md` for quick visual overview

---

## Inaugural Board Meeting Setup

### Meeting Location
**First meeting documents**: `1_Governance/Organizational_Meeting/`
**Future meetings**: `1_Governance/Board/Board_Meeting_Minutes/`

### Key Files for First Meeting

1. **Agenda**: `Organizational_Meeting/Agenda.md` ✅
   - GPT-5's comprehensive 12-item agenda
   - Ready to customize with date/time/names

2. **Meeting Packet**: `Organizational_Meeting/Meeting_Packet/`
   - Staging area for gathering board materials
   - Run `./assemble_packet.sh` to collect documents
   - Current status: Agenda ✅, Mission ✅, Certificate ✅

3. **Assembly Script**: `Meeting_Packet/assemble_packet.sh` ✅
   - Automatically copies documents from across rkl-program
   - Shows what's ready vs. what needs creation
   - Run anytime to update packet

### What the Organizational Meeting Does
- Officially forms the board
- Elects officers (Chair, Secretary, Treasurer)
- Adopts bylaws and mission
- Authorizes bank account and EIN
- Required for IRS Form 1023

### After First Meeting
- Minutes go here: `Organizational_Meeting/Minutes_[date].pdf`
- Regular meetings go here: `Board/Board_Meeting_Minutes/YYYY-MM_Month/`
- See: `Board_Meeting_Guide.md` for full workflow

---

## Key Principles for AI Assistants

When working with this repository:

1. **Respect Privacy**: Never suggest committing sensitive files
2. **Maintain Structure**: Follow the established folder organization
3. **Reference Master Docs**: Always point to authoritative mission documents
4. **Security First**: When in doubt about a file, assume it's sensitive
5. **Board Approval**: Significant changes (especially mission/bylaws) require board review
6. **Nonprofit Compliance**: Remember IRS 501(c)(3) requires specific language and practices

---

## Helpful Commands

### View mission statement
```bash
cat 4_Programs_and_Research/Program_Design/Mission_and_Vision.md
```

### Check what would be committed (dry run)
```bash
git add -n .
git status
```

### Find all mission-related documents
```bash
grep -r "discoverable, accessible, and securely interoperable" .
```

---

## Questions & Support

- **Mission statement questions**: See `0_Admin/Mission_Statement_Locations.md`
- **Security policy**: See `SECURITY.md`
- **GitHub setup**: See `SETUP_GITHUB.md` (if not yet pushed)
- **File organization**: See `0_Admin/File_Organization_Notes.md`

---

## Recent Major Updates (2025-10-15)

### Mission Statement Comprehensive Revision
- **Complete mission overhaul** based on GPT-5 input and user refinements
- **Key architectural clarification**: Organizations choose what knowledge to expose; RKL provides infrastructure
- **Updated focus**: From "ethical AI values" to "open infrastructure for trusted reasoning"
- **Concrete examples**: GPT and Claude mentioned as reasoning systems
- **New emphasis**: MCP, RAG+, policy-aware retrieval, governance by design

**Documents Updated:**
- `4_Programs_and_Research/Program_Design/Mission_and_Vision.md` (master document)
- `4_Programs_and_Research/Program_Design/Mission_Overview_One_Page.md` (board/grants)
- `4_Programs_and_Research/Program_Design/Mission_Overview_One_Page_Compact.md` (PDF versions)
- Website: _index.md, about.md, programs.md

### Compute Infrastructure Documentation (New)
Major addition establishing RKL's independent computational infrastructure:

**New Policy Document:**
- `1_Governance/Policies/RKL_Compute_Use_Policy.md` (11 sections)
  - Permitted and prohibited uses
  - Federal collaborator framework (personal capacity participation)
  - Energy efficiency and sustainability principles
  - Security and data governance requirements
  - Quarterly board reporting obligations
  - Annual transparency reporting requirements

**New Infrastructure Document:**
- `4_Programs_and_Research/Infrastructure/RKL_Compute_Capacity.md`
  - Mission alignment justification
  - Technical and operational objectives (Year 1-3)
  - Hardware/software stack planning
  - Security and access governance
  - Risk mitigation strategies
  - Funding strategy (CapEx/OpEx breakdown)
  - Success metrics by year

**New Transparency Framework:**
- `5_Operations_and_Admin/Transparency_Reports/Infrastructure_Transparency_Report_Template.md`
  - 9-section comprehensive annual report template
  - Hardware inventory and depreciation tracking
  - Usage statistics (anonymized)
  - Energy consumption and sustainability metrics
  - Security and compliance reporting
  - Financial summary format
  - Open publication commitment

**Mission Integration:**
- Added compute infrastructure reference to Mission_and_Vision.md
- Updated Year 1 operational scope to include compute environment build
- Added infrastructure section to website programs page

### Key Benefits of Infrastructure Documentation
1. **Legal Protection**: 501(c)(3) compliance safeguards for equipment acquisition
2. **Federal Collaboration**: Framework for government researchers (personal capacity)
3. **Transparency Leadership**: Public reporting of hardware, energy, usage, outcomes
4. **Research Independence**: Justifies compute build as mission-critical infrastructure
5. **Funder Confidence**: Demonstrates responsible capital asset management

### Statistics
- **35 files** added/updated in program repo
- **4,509 insertions** committed
- **4 website files** updated and deployed
- **3 new governance sections** established (Policies, Infrastructure, Transparency Reports)

---

## Next Steps (Recommended)

### Immediate (Next Board Meeting)
1. **Board Approval**: Present RKL Compute Use Policy for formal adoption
2. **Review Mission Changes**: Ensure board understands and approves new mission framing
3. **Infrastructure Budget**: Discuss capital needs for GPU nodes and networking equipment

### Short Term (Next 3 Months)
1. **Hardware Acquisition**: Begin grant applications or donor outreach for compute equipment
2. **Collaboration Agreements**: Develop Appendix A template referenced in Compute Use Policy
3. **First Transparency Report**: Start tracking infrastructure data for 2025/2026 annual report
4. **Website Launch**: Review updated website and enable GitHub Pages when ready

### Medium Term (6-12 Months)
1. **Pilot Project Selection**: Identify first partner for field pilot deployment
2. **NSF Proposal**: Submit research grant proposal leveraging infrastructure capacity
3. **Governance Toolkit v1**: Develop consent templates and policy frameworks
4. **MCP Reference Stack**: Begin building reproducible implementation

### Long Term (Year 2+)
1. **Expand Capacity**: Add GPU nodes based on demand and funding
2. **Distributed Compute**: Implement federated architecture with partner sites
3. **Standards Contribution**: Share infrastructure learnings with emerging standards bodies
4. **Carbon Neutral**: Achieve sustainability goals through efficiency and renewables

---

**Last updated**: 2025-10-15
**Status**: Mission revised, infrastructure documented, ready for board review
**Next milestone**: Board approval of mission and compute policy, begin Year 1 implementation
