# RKL Secure Reasoning Brief - Dataset Releases

This directory contains prepared datasets for publication to Kaggle and HuggingFace.

## Directory Structure

```
datasets/
├── README.md (this file)
├── telemetry-v1.0/
│   ├── README.md                              # Dataset documentation
│   ├── dataset-metadata.json                  # Kaggle metadata
│   ├── RKL-Secure-Reasoning-White-Paper-v1.0.pdf
│   ├── TELEMETRY_SCHEMA_DOCUMENTATION.md
│   ├── PHASE1_IMPROVEMENTS_COMPLETE.md
│   ├── PHASE2_IMPROVEMENTS_COMPLETE.md
│   ├── ENHANCED_TELEMETRY_LOCATIONS.md
│   └── telemetry_data/                        # 441 telemetry files (5.41 MB)
│       ├── boundary_event/
│       ├── execution_context/
│       ├── governance_ledger/
│       ├── hallucination_matrix/
│       ├── manifests/
│       ├── quality_trajectories/
│       ├── reasoning_graph_edge/
│       ├── retrieval_provenance/
│       ├── secure_reasoning_trace/
│       └── system_state/
└── rkl-secure-reasoning-brief-telemetry-v1.0.tar.gz  # Compressed (971 KB)
```

## Version History

### v1.0 (November 24, 2025)
- **Date Range**: Nov 17-26, 2025
- **Files**: 441 telemetry files
- **Size**: 5.41 MB uncompressed, 971 KB compressed
- **Formats**: Parquet (baseline) + NDJSON (Phase 1+ & Phase 2)
- **Features**:
  - Phase 1+: Chain-of-thought prompts, decision rationale, 4D quality dimensions
  - Phase 2: Artifact ID linking, step-level timing (Unix ms precision)
- **Published**:
  - Kaggle: https://www.kaggle.com/datasets/bradyopenmaps/rkl-secure-reasoning-brief-telemetry
  - HuggingFace: https://huggingface.co/datasets/rkl-org/rkl-secure-reasoning-brief-telemetry

## Usage

### Regenerate Dataset

To regenerate the dataset from current telemetry:

```bash
cd /home/mike/project/rkl-consolidated/secure-reasoning-brief
python3 scripts/prepare_dataset.py
```

This will:
1. Clean and recreate `datasets/telemetry-v1.0/`
2. Copy all telemetry data from `data/research/`
3. Copy documentation and white paper
4. Generate README and metadata
5. Create compressed archive

### Upload to Kaggle

1. Go to: https://www.kaggle.com/datasets
2. Click "New Dataset"
3. Upload: `datasets/rkl-secure-reasoning-brief-telemetry-v1.0.tar.gz`
4. Fill in metadata from `datasets/telemetry-v1.0/dataset-metadata.json`

### Upload to HuggingFace

```bash
huggingface-cli upload mbbrady/rkl-secure-reasoning-brief-telemetry \
  datasets/telemetry-v1.0/ \
  --repo-type dataset
```

## Git Configuration

The `.gitignore` is configured to:
- ✅ **Include**: Documentation files (*.md, *.pdf, *.json)
- ❌ **Exclude**: Telemetry data files (too large for git)
- ❌ **Exclude**: Compressed archives (*.tar.gz)

This allows tracking of dataset structure and metadata while keeping the repo size manageable.

---

*Last updated: November 24, 2025*
