"""Phase 0 Artifact 4: Governance Traceability Ledger"""

GOVERNANCE_LEDGER_SCHEMA = {
    "version": "v1.0",
    "artifact_type": "governance_ledger",
    "description": "Immutable ledger of publication events with full traceability",

    "required_fields": [
        "publish_id", "timestamp", "artifact_ids",
        "contributing_agent_ids", "verification_hashes"
    ],

    "optional_fields": [
        "human_signoff_id", "release_commit_sha", "quality_score",
        "type3_verified", "care_compliance_verified"
    ],

    "field_types": {
        "publish_id": str, "timestamp": str, "artifact_ids": list,
        "contributing_agent_ids": list, "verification_hashes": list,
        "human_signoff_id": str, "release_commit_sha": str,
        "quality_score": float, "type3_verified": bool,
        "care_compliance_verified": bool
    },

    "example": {
        "publish_id": "pub-2025-11-11-001",
        "timestamp": "2025-11-11T10:00:00Z",
        "artifact_ids": ["brief-2025-11-11"],
        "contributing_agent_ids": [
            "feed_monitor", "summarizer", "qa_reviewer", "brief_composer"
        ],
        "verification_hashes": [
            "sha256:input_hash...",
            "sha256:output_hash..."
        ],
        "human_signoff_id": "reviewer-01",
        "release_commit_sha": "abc123def456",
        "quality_score": 8.5,
        "type3_verified": True,
        "care_compliance_verified": True
    }
}
