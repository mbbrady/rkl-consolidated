# Resonant Knowledge Lab (RKL) - Consolidated Repository

This repository contains all Resonant Knowledge Lab projects, documentation, and resources in a unified structure.

## Repository Structure

```
rkl/
├── website/              Main RKL Hugo website (resonantknowledgelab.org)
├── placeholder/          Simple placeholder landing page
├── program/             Program documentation and organizational resources
├── demos/               Research demonstration projects
│   ├── marine-research-demo/
│   └── orp-marine-plastics-storymap/
└── docs/                General documentation and planning files
```

## Projects

### Website (`website/`)
The main RKL Hugo website with:
- About, Programs, Methods, Team pages
- Research areas and lines of effort
- Wiki with technical documentation
- Custom RKL theme

**Local development:**
```bash
cd website
hugo server -D
```

**Build:**
```bash
cd website
hugo
```

### Placeholder (`placeholder/`)
Simple static HTML landing page for early domain presence.

### Program (`program/`)
Organizational documentation including:
- Governance and compliance
- Program design documents
- Research project documentation (ORP prototype)
- Operations and communications

### Demos (`demos/`)
Interactive research demonstrations:
- **marine-research-demo**: Streamlit app for marine research visualization
- **orp-marine-plastics-storymap**: Story map for marine plastics research

## Deployment

### Main Website (Cloudflare Pages)
- **Repository**: This repo
- **Production branch**: main
- **Root directory**: `website`
- **Build command**: `hugo --minify`
- **Build output directory**: `public`
- **Environment variables**:
  - `HUGO_VERSION`: `0.138.0` (or latest)

### Placeholder Site (Cloudflare Pages)
- **Repository**: This repo
- **Production branch**: main
- **Root directory**: `placeholder`
- **Build command**: (empty)
- **Build output directory**: `/`

### Demos (Hugging Face Spaces)
- Deployed separately to Hugging Face Spaces
- See individual demo READMEs for deployment instructions

## Previous Repositories

This consolidated repository replaces:
- `mbbrady/rkl.org` → `website/`
- `mbbrady/rkl-placeholder` → `placeholder/`
- `mbbrady/rkl` → `program/`
- `mbbrady/marine-research-demo` → `demos/marine-research-demo/`
- `mbbrady/orp-marine-plastics-storymap` → `demos/orp-marine-plastics-storymap/`

Original repositories are archived but remain available for reference.

## Quick Start

**Clone repository:**
```bash
git clone https://github.com/mbbrady/rkl-consolidated.git
cd rkl-consolidated
```

**Run website locally:**
```bash
cd website
hugo server
```

**Run marine demo locally:**
```bash
cd demos/marine-research-demo
pip install -r requirements.txt
streamlit run app.py
```

## License

[To be determined]

## Contact

For inquiries: info@resonantknowledgelab.org
