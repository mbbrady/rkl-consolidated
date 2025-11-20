### Telemetry Export Instructions

- Run pipeline on work (rkl-briefs env). Gems optional via ENABLE_GEMINI_QA/GOOGLE_API_KEY/GEMINI_THEME_THRESHOLD.
- Export telemetry bundle (for HuggingFace/Kaggle):
  python scripts/export_telemetry.py --output /tmp/telemetry_export.zip [--since YYYY-MM-DD]
- Contents: data/research/* parquet/ndjson + manifest.json.
- Do not commit data/ or content/briefs/ to git; publish the zip to HF/Kaggle with README/schema.

