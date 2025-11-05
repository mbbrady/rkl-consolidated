# RKL Methods Page - For GPT-5 Review

This document shows the current Methods page content for white paper alignment.

---

## CONTEXT

The Methods page is Phase 2, Priority 3 in the website update project (after Homepage and About).

**Goal:** Simplify and tighten the Methods page for a general audience while staying technically accurate and aligned with the white paper.

**Key requirements:**
- Make content accessible to non-technical readers
- Tighten all explanations (currently quite verbose)
- Maintain technical accuracy
- Preserve the three-layer framework (Governance, Reasoning, Access)
- Keep the detailed three-mode table (important technical reference)
- Align language with white paper

---

## CURRENT METHODS PAGE CONTENT

File: `/home/mike/project/rkl/rkl.org/content/methods.md`

```markdown
---
title: "Methods"
description: "How RKL operationalizes ethical governance for secure reasoning"
---

RKL's methods turn ethical governance into **practical infrastructure** — so organizations can engage advanced reasoning systems with their own data **without losing control or custody**. We use **open protocols** and **verifiable components** *(not open data)* to make governance enforceable.

We build from the **CARE principles** — Collective Benefit, Authority to Control, Responsibility, and Ethics (Global Indigenous Data Alliance). CARE defines how knowledge should be governed; RKL defines **how AI respects that governance**.

---

## Modes of Practice

RKL frameworks support a continuum of governance and openness, depending on each organization's objectives and risk posture.

| Type | Description | Governance Focus | Example Use Case | RKL's Role |
|------|-------------|------------------|------------------|-----------|
| **Type I — CARE-Focused / Private Reasoning** | Reasoning occurs internally or on secure local infrastructure; no external data exposure. | **CARE-dominant:** internal cataloging may aid discovery; external sharing is restricted. | A regional health authority uses RKL's MCP framework to reason over PHI locally, producing aggregate insights for policy **without transferring underlying data**. | Provide on-prem MCP, secure reasoning environments, and governance templates ensuring authority, auditability, and privacy. |
| **Type II — Open Knowledge Sharing** | Datasets or narratives are made public to support education and collaboration. | **Openness by choice with CARE governance.** | **Ocean Research Project (ORP):** open marine-plastics data + transparent reasoning results for educators and policymakers. | Provide structured metadata, attribution standards, and responsible reasoning interfaces that preserve provenance and credit. |
| **Type III — CARE-Enabled Insight Exchange** | Local control is preserved; **derived knowledge** is shared externally via secure interfaces. | **CARE enables exchange** — insights travel, raw data do not. | A coastal community hosts environmental sensors and oral histories locally; RKL's layer publishes anonymized trend summaries for national planning. | Design and certify governance-linked reasoning systems; embed CARE rules in derivation pipelines. |

> Governance is rarely uniform. Different domains may operate across multiple modes simultaneously. RKL's architecture supports this diversity through a common **CARE-based** layer and **verifiable** reasoning control.

---

## Why Secure Reasoning Matters

Most valuable knowledge remains unused — not because it is too sensitive, but because organizations lack the **governance and tools** to reason with it safely. RKL provides that missing layer: **secure reasoning under local authority**. By embedding governance directly into AI interaction, protection becomes participation and **trust becomes the core compute resource**.

---

## How the Method Works

### 1) Governance Layer — CARE Rules & Metadata
Define who controls the data, for what purpose, and under what ethical conditions. Implemented via the **Model Context Protocol (MCP)** for secure, auditable context exchange.

### 2) Reasoning Layer — Secure Derivation
AI operates **inside** defined governance boundaries, producing new knowledge or insights **without revealing underlying data**. Local or hybrid deployments keep reasoning close to the data source.

### 3) Access Layer — Optional Interoperability
When a partner chooses to share derived outputs, RKL supports structured metadata and attribution so results can circulate responsibly.

These layers create the conditions for **Type III — local control with shared understanding**.

---

## Technical Architecture

- **Model Context Protocol (MCP)** — open protocol for secure AI–context interaction with **verifiable governance**
- **Policy-Aware Retrieval (RAG+)** — knowledge access that enforces governance constraints
- **Vector Indexes** — semantic search within governed domains
- **Audit Logging** — transparent provenance and consent tracking
- **Local Deployment** — on-prem and hybrid options that preserve sovereignty

Together, these ensure reasoning systems respect both the **content** and the **governance** of every knowledge domain.

---

## Ethical & Governance Commitments

Every RKL deployment includes:

- Transparent auditability of reasoning operations
- Reciprocity and attribution built into metadata
- Ethical review checkpoints within technical workflows
- Mechanisms for local veto, consent renewal, and continuous community oversight

Ethical governance is not a constraint — it is what makes reasoning **trustworthy**.

---

## In Practice

For case studies, implementation patterns, and research notes, visit our [Methods Wiki](/wiki).

---

*Resonant Knowledge Lab (RKL) is a 501(c)(3) nonprofit research and implementation organization developing open, verifiable methods that enable people and institutions to engage AI reasoning systems with their own knowledge — without transferring control or custody.*
```

---

## STRUCTURE TO PRESERVE

The Methods page has 7 main sections:
1. **Opening statement** - Brief intro to RKL's methods approach
2. **Modes of Practice** - Detailed table with Type I, II, III (this is important technical reference)
3. **Why Secure Reasoning Matters** - Value proposition
4. **How the Method Works** - Three-layer framework (Governance, Reasoning, Access)
5. **Technical Architecture** - Bullet list of technical components
6. **Ethical & Governance Commitments** - Ethical principles
7. **In Practice** - Link to wiki + closing statement

**Keep this structure** - GPT-5 should tighten and simplify content within each section.

---

## WHAT NEEDS REVIEW

**Priority areas:**
1. **Simplify for general audience** - Currently quite technical/verbose
2. **Tighten all sections** - Make content more concise
3. **Align terminology** - Match white paper language
4. **Maintain technical accuracy** - Don't oversimplify to the point of losing meaning

**What to preserve:**
- Detailed three-mode table (this is valuable technical reference)
- Three-layer framework (Governance, Reasoning, Access)
- Technical Architecture section (but can be tightened)
- CARE principles foundation
- Examples (healthcare, ORP, coastal community)

**What can be simplified:**
- Opening paragraphs
- "Why Secure Reasoning Matters" section
- "How the Method Works" explanations
- "Ethical & Governance Commitments" section

---

## FOR GPT-5: REQUESTED OUTPUT

Please review the Methods page content and provide:

1. **Simplified, tightened version** in complete markdown format
2. **Rationale** for significant changes (how it aligns with white paper)
3. **Word count** targets: Keep each section tight
4. **Maintain accessibility** - Explain technical concepts clearly for general readers

**Tone requirements:**
- Professional, pithy, and clean
- Accessible to general readers (not just technical experts)
- Faithful to white paper's ethical and technical framing
- Plain, inviting language while staying technically accurate

**Output format:**
Provide the complete updated markdown content for `methods.md` that can be directly copied into the file.

---

## NOTES

- The detailed three-mode table is a key technical reference - keep it detailed
- The three-layer framework (Governance, Reasoning, Access) is core to RKL's approach
- Examples (healthcare PHI, ORP, coastal community) help make concepts concrete
- Cross-references to other pages ([Methods Wiki](/wiki)) should be preserved
- Balance: accessible to general readers but technically accurate for practitioners
