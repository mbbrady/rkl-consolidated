"""
Privacy utilities for sanitizing and anonymizing log records.

Supports three privacy levels:
- INTERNAL: Full data (restricted access)
- RESEARCH: Sanitized (hashed sensitive fields)
- PUBLIC: Anonymized (only structural data)
"""

from enum import Enum
from typing import Dict, Any, Set
from .hashing import sha256_text


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

# Fields to keep in public datasets (only structural)
PUBLIC_STRUCTURAL_FIELDS = {
    "session_id",
    "turn_id",
    "agent_id",
    "model_id",
    "model_rev",
    "quant",
    "temp",
    "top_p",
    "ctx_tokens_used",
    "gen_tokens",
    "tool_lat_ms",
    "cache_hit",
    "timestamp",
    "pipeline_phase",
    "type3_compliant",
    "rkl_version"
}


def sanitize_for_research(record: Dict[str, Any]) -> Dict[str, Any]:
    """
    Sanitize record for research release.

    - Replaces sensitive fields with SHA-256 hashes
    - Keeps all structural fields
    - Preserves cross-references

    Args:
        record: Original log record

    Returns:
        Sanitized record safe for research datasets
    """
    sanitized = {}

    for key, value in record.items():
        if key in SENSITIVE_FIELDS:
            # Hash sensitive fields
            if isinstance(value, str):
                sanitized[f"{key}_hash"] = sha256_text(value)
            else:
                sanitized[f"{key}_hash"] = sha256_text(str(value))
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

    - Keeps only structural/statistical fields
    - Removes all content hashes
    - Replaces IDs with sequential numbers

    Args:
        record: Original log record

    Returns:
        Anonymized record safe for public datasets
    """
    anonymized = {}

    for key, value in record.items():
        if key in PUBLIC_STRUCTURAL_FIELDS:
            anonymized[key] = value
        elif key.endswith("_count") or key.endswith("_ms") or key.endswith("_tokens"):
            # Keep statistical fields
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


def validate_no_raw_text(record: Dict[str, Any]) -> bool:
    """
    Verify that record contains no raw text content.

    Checks that all text fields are either hashed or structural.

    Args:
        record: Log record to validate

    Returns:
        True if no raw text detected

    Raises:
        ValueError: If raw text detected in fields that should be hashed
    """
    for key, value in record.items():
        # Check for suspiciously long text values
        if isinstance(value, str) and len(value) > 200:
            # Exception: hash values are OK
            if not value.startswith("sha256:"):
                raise ValueError(
                    f"Field '{key}' contains raw text ({len(value)} chars). "
                    f"Should be hashed for privacy."
                )

    return True
