"""
Schema for Phase 0 Artifact 1: Execution Context & Hyperparameters

Captures model execution details, hyperparameters, and performance metrics
for every agent inference.
"""

EXECUTION_CONTEXT_SCHEMA = {
    "version": "v1.0",
    "artifact_type": "execution_context",
    "description": "Model execution context and hyperparameters for agent inferences",

    "required_fields": [
        "session_id",
        "turn_id",
        "agent_id",
        "model_id",
        "timestamp"
    ],

    "optional_fields": [
        "model_rev",
        "quant",
        "temp",
        "top_p",
        "seed",
        "ctx_tokens_used",
        "gen_tokens",
        "tool_lat_ms",
        "cache_hit",
        "prompt_id_hash",
        # RKL-specific
        "rkl_version",
        "type3_compliant",
        "pipeline_phase",
        "care_metadata"
    ],

    "field_types": {
        "session_id": str,
        "turn_id": int,
        "agent_id": str,
        "model_id": str,
        "model_rev": str,
        "quant": str,
        "temp": float,
        "top_p": float,
        "seed": int,
        "ctx_tokens_used": int,
        "gen_tokens": int,
        "tool_lat_ms": int,
        "cache_hit": bool,
        "prompt_id_hash": str,
        "timestamp": str,
        # RKL fields
        "rkl_version": str,
        "type3_compliant": bool,
        "pipeline_phase": str,
        "care_metadata": dict
    },

    "deprecated_fields": [],

    "field_descriptions": {
        "session_id": "Unique identifier for the entire brief generation session",
        "turn_id": "Sequential turn number within session",
        "agent_id": "Which agent performed this inference (e.g., 'summarizer')",
        "model_id": "Model identifier (e.g., 'llama3.2:8b')",
        "model_rev": "Model revision or variant (e.g., '8B-q4')",
        "quant": "Quantization level (e.g., 'q4', 'fp16')",
        "temp": "Temperature parameter (0.0-2.0)",
        "top_p": "Nucleus sampling parameter (0.0-1.0)",
        "seed": "Random seed for reproducibility",
        "ctx_tokens_used": "Context tokens consumed",
        "gen_tokens": "Tokens generated in response",
        "tool_lat_ms": "Latency in milliseconds",
        "cache_hit": "Whether inference used cached result",
        "prompt_id_hash": "SHA-256 hash of prompt template used",
        "timestamp": "ISO 8601 timestamp",
        "rkl_version": "RKL system version",
        "type3_compliant": "Whether this operation maintained Type III boundaries",
        "pipeline_phase": "Which phase of pipeline (discovery/processing/governance/etc)",
        "care_metadata": "CARE principles compliance metadata"
    },

    "example": {
        "session_id": "brief-2025-11-11-001",
        "turn_id": 42,
        "agent_id": "summarizer",
        "model_id": "llama3.2:8b",
        "model_rev": "8B-q4",
        "quant": "q4",
        "temp": 0.3,
        "top_p": 0.95,
        "seed": 42,
        "ctx_tokens_used": 2048,
        "gen_tokens": 150,
        "tool_lat_ms": 1234,
        "cache_hit": False,
        "prompt_id_hash": "sha256:abc123...",
        "timestamp": "2025-11-11T09:15:23Z",
        "rkl_version": "1.0",
        "type3_compliant": True,
        "pipeline_phase": "processing",
        "care_metadata": {
            "collective_benefit": True,
            "authority_to_control": "local",
            "responsibility": "audit-2025-11-11-001",
            "ethics": "consent_verified"
        }
    }
}
