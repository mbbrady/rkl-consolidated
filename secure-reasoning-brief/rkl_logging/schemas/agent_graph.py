"""Phase 0 Artifact 2: Multi-Agent Reasoning Graph (structural)"""

AGENT_GRAPH_SCHEMA = {
    "version": "v1.0",
    "artifact_type": "agent_graph",
    "description": "Structural representation of agent-to-agent message passing",

    "required_fields": [
        "edge_id", "session_id", "timestamp", "from_agent",
        "to_agent", "msg_type", "content_hash"
    ],

    "optional_fields": [
        "t", "intent_tag", "parent_edge_id", "role_tags",
        "latency_ms", "retry_count"
    ],

    "field_types": {
        "edge_id": str, "session_id": str, "timestamp": str,
        "t": int, "from_agent": str, "to_agent": str, "msg_type": str,
        "intent_tag": str, "content_hash": str, "parent_edge_id": str,
        "role_tags": list, "latency_ms": int, "retry_count": int
    },

    "example": {
        "edge_id": "edge-001",
        "session_id": "brief-2025-11-11-001",
        "timestamp": "2025-11-11T09:15:23Z",
        "from_agent": "summarizer",
        "to_agent": "qa_reviewer",
        "msg_type": "summary_for_review",
        "intent_tag": "quality_check",
        "content_hash": "sha256:def456...",
        "parent_edge_id": "edge-000",
        "role_tags": ["processing", "quality_assurance"],
        "latency_ms": 45,
        "retry_count": 0
    }
}
