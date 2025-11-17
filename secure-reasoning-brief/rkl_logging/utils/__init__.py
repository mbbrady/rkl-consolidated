"""Utility functions for RKL logging"""

from .hashing import (
    sha256_text, sha256_dict, sha256_json, sha256_file,
    hmac_sha256_text, hash_prompt, hash_document, pseudonymize_id
)
from .privacy import (
    sanitize_for_research, anonymize_for_public,
    pseudonymize_ids, PrivacyLevel
)

__all__ = [
    "sha256_text",
    "sha256_dict",
    "sha256_json",
    "sha256_file",
    "hmac_sha256_text",
    "hash_prompt",
    "hash_document",
    "pseudonymize_id",
    "sanitize_for_research",
    "anonymize_for_public",
    "pseudonymize_ids",
    "PrivacyLevel"
]
