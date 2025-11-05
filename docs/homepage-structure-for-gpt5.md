# RKL Homepage Structure - For GPT-5 Review

This document shows how the RKL homepage is structured in Hugo.

---

## How Hugo Combines Content + Layout

The homepage consists of **two files that work together**:

1. **Content file** (`content/_index.md`) - Contains the actual text/words
2. **Layout file** (`layouts/index.html`) - Defines how the page is structured

Hugo combines these: the layout file pulls in the content using `{{ .Content }}` and wraps it in the HTML structure.

---

## CONTENT FILE: content/_index.md

This is the actual text that appears on the homepage hero section:

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

## LAYOUT FILE: layouts/index.html

This defines the page structure (simplified view):

```html
{{ define "main" }}
<div class="intro">
  <div class="container">
    <div class="row justify-content-start">
      <div class="col-12 col-md-7 col-lg-6 order-2 order-md-1">
        {{ .Content }}
        <!-- This is where the content from _index.md gets inserted -->
      </div>
      <!-- Decorative intro image currently commented out -->
    </div>
  </div>
</div>

<!-- Lines of Effort Section -->
{{ partial "lines-of-effort.html" . }}
<!-- This pulls in a separate section below the hero -->

{{ end }}
```

**Key structural elements:**
- Hero section takes up 7/12 columns on medium screens, 6/12 on large screens
- Content is left-aligned
- "Lines of Effort" section appears below the hero (this is separate, not part of the hero content)
- Mobile-first responsive design using Bootstrap grid

---

## WHAT GPT-5 SHOULD FOCUS ON

**Rewrite the CONTENT FILE** (`_index.md`) to align with the white paper while:
- Keeping the YAML front matter structure (title and description)
- Expanding the hero section beyond just the tagline
- Maintaining professional, pithy, clean tone
- Using clear, accessible language for general readers
- Staying faithful to white paper's ethical and technical framing

**Keep the same LAYOUT structure** - GPT-5 doesn't need to change the layout file, just provide updated content that fits into the existing structure.

---

## CURRENT VISUAL LAYOUT

```
┌─────────────────────────────────────────────┐
│ [Logo] Resonant Knowledge Lab    [Nav Menu] │ ← Header (separate file)
├─────────────────────────────────────────────┤
│                                             │
│   Status & Disclaimer banner                │
│                                             │
│   # Secure reasoning with AI                │ ← Hero section
│                                             │  (content from _index.md)
│   Introductory paragraph...                 │
│                                             │
│   Secure reasoning. Local control.          │
│                                             │
│   info@resonantknowledgelab.org            │
│                                             │
├─────────────────────────────────────────────┤
│   Lines of Effort Section                   │ ← Separate partial
│   (3-column grid with program areas)        │  (below the fold)
└─────────────────────────────────────────────┘
```

---

## FOR GPT-5: REQUESTED OUTPUT

Please provide updated content for `content/_index.md` that includes:

- **Headline** (H1) - 5-10 words, clear and compelling
- **Subheadline** (if needed) - 10-15 words
- **Introductory paragraph** - 2-3 sentences (~50 words), explains RKL's mission clearly
- **Tagline** - Short, memorable (can keep current or suggest alternative)
- **Contact email** - Keep as is

The content should:
- Be faithful to the white paper's vision and mission
- Use plain, inviting language for public audiences
- Remain professional and clean
- Provide clearer value proposition than current version
- Work within the existing layout structure (left column, responsive design)
