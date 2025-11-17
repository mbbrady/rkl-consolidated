"""Phase 0 Artifact 3: Type-III Boundary Enforcement Log"""

BOUNDARY_EVENTS_SCHEMA = {
    "version": "v1.0",
    "artifact_type": "boundary_events",
    "description": "Log of Type III secure reasoning boundary enforcement events",

    "required_fields": [
        "event_id", "timestamp", "agent_id", "rule_id",
        "trigger_tag", "action"
    ],

    "optional_fields": [
        "session_id", "t", "context_tag", "reviewer", "severity", "blocked_content_hash"
    ],

    "field_types": {
        "event_id": str, "timestamp": str, "t": int, "session_id": str,
        "agent_id": str, "rule_id": str, "trigger_tag": str, "context_tag": str,
        "action": str, "reviewer": str, "severity": str,
        "blocked_content_hash": str
    },

    "example": {
        "event_id": "boundary-evt-001",
        "timestamp": "2025-11-11T09:15:23Z",
        "agent_id": "summarizer",
        "rule_id": "processing_boundary",
        "trigger_tag": "external_api_attempted",
        "context_tag": "test_mode",
        "action": "blocked",
        "reviewer": "governance_auditor",
        "severity": "critical",
        "blocked_content_hash": "sha256:ghi789..."
    }
}
