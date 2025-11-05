# RKL Website Update Package for GPT-5
## White Paper Alignment Project

---

## CONTEXT

I've completed the **RKL Secure Reasoning White Paper v1.0 (Oct 2025)**, which now serves as the authoritative reference for Resonant Knowledge Lab's messaging, mission, and technical approach.

**Goal:** Use the white paper to update and unify the RKL website's language across all pages.

**Tone Requirements:**
- Clear, mission-driven, accessible to general readers
- Professional, pithy, and clean
- Plain, inviting language for public audiences
- Faithful to the white paper's ethical and technical framing
- Keep the cover page (homepage hero) approach, but align with white paper

---

## CURRENT WEBSITE STRUCTURE

### Main Pages:
1. **Homepage** (`content/_index.md`) - Hero section + intro
2. **About** (`content/about.md`) - Mission, vision, principles, organization
3. **Methods** (`content/methods.md`) - How RKL operationalizes ethical governance
4. **Programs** (`content/programs.md`) - Six program areas and applications
5. **Wiki** - Technical implementation details (separate from public site)

### Key Elements to Preserve:
- Three-mode framework (Type I, II, III)
- CARE principles as foundation
- MCP as core technical protocol
- 501(c)(3) nonprofit status
- Contact: info@resonantknowledgelab.org

---

## CURRENT WEBSITE CONTENT

### HOMEPAGE (content/_index.md)

```markdown
---
title: "Resonant Knowledge Lab"
description: "Secure reasoning. Local control."
---

> **Status & Disclaimer:** This draft page is shared for internal review. See [About](/about) for organizational status.

# Secure reasoning with AI

Open **protocols** and **verifiable infrastructure** that enable advanced reasoning systems to work with curated, locally governed knowledge — **without exposing or transferring sensitive data**.

**Secure reasoning. Local control.**

[info@resonantknowledgelab.org](mailto:info@resonantknowledgelab.org)
```

**What needs improvement:**
- Expand beyond just the tagline
- Better reflect white paper's mission and vision
- More inviting while staying professional
- Clearer value proposition

---

### ABOUT PAGE (content/about.md)

**Current sections:**
- Vision
- Mission
- Guiding Principles (5 principles)
- Modes of Practice (Type I, II, III table)
- Approach (CARE + MCP + Interoperability)
- Organization (501(c)(3) details)

**What needs review:**
- Align vision/mission with white paper
- Check if principles match white paper framing
- Tighten language throughout
- Ensure professional, pithy tone

---

### METHODS PAGE (content/methods.md)

**Current sections:**
- Introduction (CARE foundation)
- Modes of Practice table (Type I, II, III detailed)
- Why Secure Reasoning Matters
- How the Method Works (3 layers)
- Technical Architecture (MCP, RAG+, etc.)
- Ethical & Governance Commitments

**What needs review:**
- Align technical descriptions with white paper
- Simplify for general audience while staying accurate
- Tighten explanations

---

### PROGRAMS PAGE (content/programs.md)

**Current sections:**
- Our Approach
- Six Core Programs:
  1. Open Protocols for Contextual AI
  2. Reference Implementations & Toolkits
  3. Decision Support & Knowledge Access Pilots
  4. Governance & Stewardship Frameworks
  5. Research & Applied Inquiry
  6. Education & Public Engagement
- Year 1 Operational Focus
- Illustrative Sector Applications table
- Get Involved

**What needs review:**
- Ensure program descriptions match white paper
- Tighten all program descriptions
- Clear, action-oriented language

---

## REQUESTED OUTPUT FORMAT

For each page/section, please provide:

1. **Specific edits** in markdown format that can be directly copied into Hugo content files
2. **Word count** for each section (keep tight - ~250 words for About, etc.)
3. **Rationale** explaining how the edit aligns with white paper
4. **Highlight** any significant departures from current content

---

## PRIORITY ORDER

**Phase 1 (Immediate):**
1. Homepage hero section rewrite
2. About page alignment (mission, vision, principles)

**Phase 2 (Next):**
3. Methods page simplification
4. Programs page tightening

**Phase 3 (Later):**
5. Wiki technical pages (separate session)

---

## STARTER PROMPT FOR GPT-5

```
Context: I've completed the RKL Secure Reasoning White Paper v1.0 (April 2025).
It defines Resonant Knowledge Lab's mission, CARE-based governance framework,
and long-term vision for secure reasoning infrastructure.

Goal: Use the white paper to update and unify the website's language.

First task: Rewrite the homepage headline, subheadline, and short introductory
paragraph so they clearly reflect RKL's mission and the concept of "Secure Reasoning."
Use clear, accessible language while staying faithful to the white paper's tone.

Current homepage content:
[paste homepage content from above]

White paper Abstract and Executive Summary:
[I will paste the relevant white paper sections]

Please produce concise copy for the homepage hero section that:
- Headline (5-10 words)
- Subheadline (10-15 words)
- Introductory paragraph (2-3 sentences, ~50 words)
- Maintains professional, pithy, clean tone
```

---

## NOTES

- I like the current cover page approach - keep that structure
- All other pages need tightening for public audience
- Remove "Status & Disclaimer" banner once content is finalized
- Website files are Hugo markdown with YAML front matter
- Changes will be reviewed by Claude Code before implementation

---

## FILE LOCATIONS (for reference)

- Homepage: `/home/mike/project/rkl/rkl.org/content/_index.md`
- About: `/home/mike/project/rkl/rkl.org/content/about.md`
- Methods: `/home/mike/project/rkl/rkl.org/content/methods.md`
- Programs: `/home/mike/project/rkl/rkl.org/content/programs.md`

All content files use standard markdown with YAML front matter.

---

**Ready to begin! Please start with the homepage hero section.**
