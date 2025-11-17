"""
Privacy utilities for sanitizing and anonymizing log records.

Supports three privacy levels:
- INTERNAL: Full data (restricted access)
- RESEARCH: Sanitized (HMAC-hashed sensitive fields)
- PUBLIC: Anonymized (only structural data + pseudonymized IDs)
"""

import os
from enum import Enum
from typing import Dict, Any, Set, List
from .hashing import sha256_text, hmac_sha256_text, pseudonymize_id


class PrivacyLevel(Enum):
    """Privacy levels for data release"""
    INTERNAL = "internal"      # Full data, restricted access
    RESEARCH = "research"      # Sanitized, for researchers
    PUBLIC = "public"          # Anonymized, for public benchmarks


# Fields that contain sensitive information
SENSITIVE_FIELDS = {
    "prompt_text",
    "input_text",
    "output_text",
    "raw_content",
    "user_id",
    "email",
    "api_key",
    "token",
    "password"
}

# Fields to keep in public datasets (structural + essential cross-refs)
PUBLIC_STRUCTURAL_FIELDS = {
    # IDs and tracing
    "session_id", "turn_id", "agent_id", "publish_id", "edge_id", "event_id",
    # Model configuration
    "model_id", "model_rev", "quant", "temp", "top_p",
    # Metrics
    "ctx_tokens_used", "gen_tokens", "tool_lat_ms", "cache_hit",
    "latency_ms", "retry_count",
    # Metadata
    "timestamp", "t", "pipeline_phase", "type3_compliant", "rkl_version",
    # Boundary/graph structural
    "rule_id", "trigger_tag", "context_tag", "action",
    "from_agent", "to_agent", "msg_type", "intent_tag",
    # Hashed cross-references (needed for joins)
    "prompt_id_hash", "system_prompt_hash", "content_hash",
    "doc_hash", "url_hash", "parent_edge_id",
    # Arrays of hashes (ledger/verification)
    "verification_hashes", "artifact_ids", "contributing_agent_ids",
    # Governance
    "schema_version", "raw_data_exposed", "derived_insights_only",
    "human_signoff_id", "release_commit_sha"
}


def sanitize_for_research(record: Dict[str, Any], use_hmac: bool = True) -> Dict[str, Any]:
    """
    Sanitize record for research release.

    - Replaces sensitive fields with HMAC-SHA256 hashes (preferred) or SHA-256
    - Keeps all structural fields
    - Preserves cross-references

    Args:
        record: Original log record
        use_hmac: If True, use HMAC with RKL_PRIVACY_PEPPER env var (default: True)

    Returns:
        Sanitized record safe for research datasets

    Example:
        >>> rec = {"prompt_text": "secret prompt", "model_id": "llama3.2:8b"}
        >>> sanitize_for_research(rec)
        {'prompt_text_hash': 'a3f2b8...', 'model_id': 'llama3.2:8b', ...}
    """
    sanitized = {}
    pepper = os.getenv("RKL_PRIVACY_PEPPER", "") if use_hmac else ""

    for key, value in record.items():
        if key in SENSITIVE_FIELDS:
            # Hash sensitive fields with HMAC if enabled
            if isinstance(value, str):
                hash_val = hmac_sha256_text(value, pepper) if use_hmac else sha256_text(value)
                sanitized[f"{key}_hash"] = hash_val
            else:
                hash_val = hmac_sha256_text(str(value), pepper) if use_hmac else sha256_text(str(value))
                sanitized[f"{key}_hash"] = hash_val
        else:
            # Keep non-sensitive fields
            sanitized[key] = value

    # Add privacy metadata
    sanitized["_privacy_level"] = PrivacyLevel.RESEARCH.value
    sanitized["_sanitized"] = True

    return sanitized


def anonymize_for_public(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Anonymize record for public benchmark release.

    - Keeps structural/statistical fields + hashed cross-refs
    - Preserves arrays of hashes for graph topology
    - Removes raw content but keeps verification hashes

    Args:
        record: Original log record

    Returns:
        Anonymized record safe for public datasets

    Example:
        >>> rec = {"session_id": "s1", "prompt_text": "secret", "ctx_tokens": 100}
        >>> anonymize_for_public(rec)
        {'session_id': 's1', 'ctx_tokens': 100, ...}
    """
    anonymized = {}

    for key, value in record.items():
        if key in PUBLIC_STRUCTURAL_FIELDS:
            # Keep allowed structural fields
            anonymized[key] = value
        elif key.endswith("_count") or key.endswith("_ms") or key.endswith("_tokens"):
            # Keep statistical fields
            anonymized[key] = value
        elif isinstance(value, list) and key in {"artifact_ids", "verification_hashes", "contributing_agent_ids"}:
            # Keep arrays of hashes/IDs for topology
            anonymized[key] = value
        elif isinstance(value, (int, float, bool)):
            # Keep numeric/boolean values
            anonymized[key] = value

    # Add privacy metadata
    anonymized["_privacy_level"] = PrivacyLevel.PUBLIC.value
    anonymized["_anonymized"] = True

    return anonymized


def strip_pii(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Remove any potential PII from record.

    More aggressive than sanitization - removes entire fields
    that might contain PII.

    Args:
        record: Original log record

    Returns:
        Record with PII fields removed
    """
    pii_fields = {
        "user_id", "email", "name", "phone", "address",
        "ip_address", "user_agent", "cookie"
    }

    return {
        k: v for k, v in record.items()
        if k not in pii_fields
    }


def pseudonymize_ids(record: Dict[str, Any], fields: List[str] = None, salt: str = "") -> Dict[str, Any]:
    """
    Replace sensitive IDs with deterministic pseudonyms.

    Creates stable pseudonyms per release while protecting identity.
    Preserves cross-file joins through deterministic mapping.

    Args:
        record: Original log record
        fields: List of ID fields to pseudonymize (defaults to session_id, agent_id, publish_id)
        salt: Optional salt for this release (defaults to RKL_PSEUDO_SALT env var)

    Returns:
        Record with pseudonymized IDs

    Example:
        >>> rec = {"session_id": "s-abc-123", "model_id": "llama3.2:8b"}
        >>> pseudonymize_ids(rec)
        {'session_id': 'f3a8b2c1d4e5f6a7', 'model_id': 'llama3.2:8b'}
    """
    fields = fields or ["session_id", "agent_id", "publish_id", "user_id"]
    salt = salt or os.getenv("RKL_PSEUDO_SALT", "")

    pseudonymized = record.copy()

    for field in fields:
        if field in pseudonymized and isinstance(pseudonymized[field], str):
            pseudonymized[field] = pseudonymize_id(pseudonymized[field], salt)

    return pseudonymized


def validate_no_raw_text(record: Dict[str, Any], threshold: int = 1024) -> bool:
    """
    Verify that record contains no raw text content.

    Checks that all text fields are either hashed or structural.
    Uses improved detection that recognizes hex hashes without prefixes.

    Args:
        record: Log record to validate
        threshold: Maximum chars for non-hash text (default: 1024)

    Returns:
        True if no raw text detected

    Raises:
        ValueError: If raw text detected in fields that should be hashed

    Example:
        >>> validate_no_raw_text({"content_hash": "a3f2b8c1...", "model_id": "llama3.2:8b"})
        True
    """
    import re
    hex_pattern = re.compile(r'^[a-f0-9]{64}$')  # SHA-256 hex digest

    for key, value in record.items():
        # Skip if not string or if it's an allowed structural field
        if not isinstance(value, str):
            continue
        if key in PUBLIC_STRUCTURAL_FIELDS:
            continue

        # Check for suspiciously long text values
        if len(value) > threshold:
            # Exception 1: Fields ending with _hash are OK
            if key.endswith("_hash"):
                continue
            # Exception 2: Values matching hex hash pattern are OK
            if hex_pattern.match(value):
                continue
            # Exception 3: Values with sha256: or hmac: prefix are OK
            if value.startswith(("sha256:", "hmac:", "prompt:", "doc:")):
                continue

            raise ValueError(
                f"Field '{key}' contains raw text ({len(value)} chars). "
                f"Should be hashed for privacy."
            )

    return True
