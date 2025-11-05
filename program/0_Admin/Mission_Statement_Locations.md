# Mission Statement - Document Locations

This guide shows where the RKL mission statement is used throughout the organization.

**Last updated**: 2025-10-14

---

## Master Documents (Private Repo)

### Full Mission & Vision Statement
**Location**: `4_Programs_and_Research/Program_Design/Mission_and_Vision.md`
**Purpose**: Authoritative source document for all mission-related content
**Use for**: Strategic planning, program development, grant applications
**Format**: Markdown, comprehensive

### Board Summary (One-Page)
**Location**: `1_Governance/Board/Mission_Statement_Summary.md`
**Purpose**: Quick reference for board packets and governance documents
**Use for**: Board meetings, board recruitment, annual reports
**Format**: Markdown, one-page summary

### IRS Form 1023 Version
**Location**: `2_Compliance_and_Filings/IRS/Form_1023_Application/Mission_Statement.txt`
**Purpose**: Formatted specifically for 501(c)(3) application
**Use for**: IRS filings, tax-exempt status applications
**Format**: Plain text, IRS-compliant language
**Note**: Includes "exclusively for educational and scientific purposes" language

---

## Website (Public Repo)

### Home Page
**Location**: `rkl.org/content/_index.md`
**Contains**: Mission statement (one-sentence version) and welcome text
**URL**: https://resonantknowledgelab.org/

### About Page
**Location**: `rkl.org/content/about.md`
**Contains**: Full mission, vision, guiding principles, about section
**URL**: https://resonantknowledgelab.org/about/

### Programs Page
**Location**: `rkl.org/content/programs.md`
**Contains**: Core programs overview, current projects, goals
**URL**: https://resonantknowledgelab.org/programs/

### Site Configuration
**Location**: `rkl.org/config.toml`
**Contains**: Tagline ("Ethical AI for Living Knowledge") and site description

---

## README Files

### Main Project README
**Location**: `/home/mike/project/rkl/README.md`
**Contains**: Mission statement, organizational overview
**Audience**: Developers, collaborators accessing the project folder

### Private Repo README
**Location**: `rkl-program/README.md`
**Contains**: Reference to mission document locations
**Audience**: Board members, staff with repo access

---

## Key Versions

### Single-Sentence Mission (Most Concise)
> Our mission is to make human knowledge — in all its cultural, institutional, and environmental forms — discoverable, accessible, and securely interoperable with AI.

**Use for**: Email signatures, social media bios, quick introductions

### Tagline (Shortest)
> Ethical AI for Living Knowledge

**Use for**: Website header, business cards, promotional materials

### Two-Paragraph Mission (Medium)
> Resonant Knowledge Lab (RKL) is a nonprofit research and development organization dedicated to advancing ethical, community-governed artificial intelligence.
>
> We explore how local, indigenous, and organizational knowledge can be securely integrated into AI through transparent, auditable architectures that protect privacy, context, and data sovereignty.

**Use for**: Grant summaries, press releases, introductory materials

### Full Mission Statement (Complete)
See: `4_Programs_and_Research/Program_Design/Mission_and_Vision.md`

**Use for**: Comprehensive documentation, strategic planning, detailed presentations

---

## Usage Guidelines

### When to Use Each Version

| Context | Version to Use | Location |
|---------|---------------|----------|
| **IRS filings** | IRS-specific version | `2_Compliance_and_Filings/IRS/Form_1023_Application/Mission_Statement.txt` |
| **Board packets** | Board summary | `1_Governance/Board/Mission_Statement_Summary.md` |
| **Grant applications** | Full mission | `4_Programs_and_Research/Program_Design/Mission_and_Vision.md` |
| **Website content** | Website versions | `rkl.org/content/about.md` |
| **Email signature** | Single sentence | (Copy from any document) |
| **Social media bio** | Tagline | "Ethical AI for Living Knowledge" |
| **Elevator pitch** | Two paragraphs | (Copy from About page or Board summary) |
| **Strategic planning** | Full document | `4_Programs_and_Research/Program_Design/Mission_and_Vision.md` |

---

## Updating the Mission Statement

If the mission statement needs to be updated:

1. **Update the master document first**:
   - `4_Programs_and_Research/Program_Design/Mission_and_Vision.md`
   - Get board approval before making changes

2. **Then update all derivative documents**:
   - Board summary
   - IRS version (if significant changes)
   - Website content (About page, home page)
   - This location guide

3. **Update the website**:
   ```bash
   cd /home/mike/project/rkl/rkl.org
   # Edit content files
   git add content/
   git commit -m "Update mission statement"
   git push
   ```

4. **Document the change**:
   - Note date of update in each file
   - Record board approval in board meeting minutes
   - Update version history if maintained

---

## Notes

- The master document (`Mission_and_Vision.md`) is the authoritative source
- All other versions should be derived from the master
- Website versions are public; all others are private (in rkl-program repo)
- IRS version uses specific language required for 501(c)(3) compliance
- Keep this location guide updated when adding new documents

---

**Maintained by**: Board of Directors / Executive Leadership
**Review frequency**: Annually or as needed
**Last board review**: (Pending organizational meeting)
