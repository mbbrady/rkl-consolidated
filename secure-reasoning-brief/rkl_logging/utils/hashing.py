"""
Hashing utilities for cross-referencing without exposing content.

All hashing uses SHA-256 for consistency and security.
Supports HMAC for dataset-scoped pseudonymization.
"""

import hashlib
import hmac
import json
import os
from typing import Any, Dict


def sha256_text(text: str, prefix: bool = False) -> str:
    """
    Generate SHA-256 hash of text content.

    Args:
        text: Text to hash
        prefix: If True, add 'sha256:' prefix (default: False for compatibility)

    Returns:
        Hex-encoded SHA-256 hash (optionally with prefix)

    Example:
        >>> sha256_text("Hello, world!")
        '315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3'
        >>> sha256_text("Hello, world!", prefix=True)
        'sha256:315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3'
    """
    if not isinstance(text, str):
        text = str(text)

    hash_obj = hashlib.sha256(text.encode('utf-8'))
    hex_hash = hash_obj.hexdigest()
    return f"sha256:{hex_hash}" if prefix else hex_hash


def hmac_sha256_text(text: str, pepper: str = "", prefix: bool = False) -> str:
    """
    Generate HMAC-SHA256 hash with optional pepper for pseudonymization.

    Uses HMAC for dataset-scoped, non-reversible identifiers that are
    more secure than raw SHA-256 for sensitive fields.

    Args:
        text: Text to hash
        pepper: Secret pepper value (defaults to RKL_PRIVACY_PEPPER env var)
        prefix: If True, add 'hmac:' prefix

    Returns:
        Hex-encoded HMAC-SHA256 hash

    Example:
        >>> hmac_sha256_text("session-123", "secret_pepper")
        'a3f2b8c1d4e5f6...'
    """
    if not isinstance(text, str):
        text = str(text)

    pepper = pepper or os.getenv("RKL_PRIVACY_PEPPER", "")
    key = pepper.encode('utf-8') if pepper else b''

    hmac_obj = hmac.new(key, text.encode('utf-8'), hashlib.sha256)
    hex_hash = hmac_obj.hexdigest()
    return f"hmac:{hex_hash}" if prefix else hex_hash


def sha256_dict(data: Dict[str, Any], prefix: bool = False) -> str:
    """
    Generate SHA-256 hash of dictionary content.

    Args:
        data: Dictionary to hash
        prefix: If True, add 'sha256:' prefix

    Returns:
        Hex-encoded SHA-256 hash (optionally with prefix)

    Note:
        Dictionary is serialized to JSON with sorted keys for consistency.
    """
    # Sort keys for consistent hashing
    json_str = json.dumps(data, sort_keys=True)
    return sha256_text(json_str, prefix=prefix)


def sha256_json(data: Any, prefix: bool = False) -> str:
    """
    Alias for sha256_dict for compatibility.

    Args:
        data: Data structure to hash (will be JSON-serialized)
        prefix: If True, add 'sha256:' prefix

    Returns:
        Hex-encoded SHA-256 hash
    """
    json_str = json.dumps(data, sort_keys=True)
    return sha256_text(json_str, prefix=prefix)


def sha256_file(file_path: str, chunk_size: int = 8192, prefix: bool = False) -> str:
    """
    Generate SHA-256 hash of file content.

    Args:
        file_path: Path to file
        chunk_size: Size of chunks to read (for large files)
        prefix: If True, add 'sha256:' prefix

    Returns:
        Hex-encoded SHA-256 hash (optionally with prefix)
    """
    hash_obj = hashlib.sha256()

    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hash_obj.update(chunk)

    hex_hash = hash_obj.hexdigest()
    return f"sha256:{hex_hash}" if prefix else hex_hash


def hash_prompt(prompt_text: str, version: str = "v1") -> str:
    """
    Generate versioned hash for prompts.

    Args:
        prompt_text: Prompt template text
        version: Prompt version identifier

    Returns:
        Versioned hash like 'prompt:v1:abc123...'
    """
    hash_part = sha256_text(prompt_text)
    return f"prompt:{version}:{hash_part}"


def hash_document(doc_content: str, source: str = "") -> str:
    """
    Generate hash for source documents.

    Args:
        doc_content: Document text content
        source: Source identifier (e.g., URL, filename)

    Returns:
        Hash with source context like 'doc:abc123...'
    """
    combined = f"{source}|{doc_content}"
    hash_part = sha256_text(combined)
    return f"doc:{hash_part}"


def pseudonymize_id(original_id: str, salt: str = "") -> str:
    """
    Generate deterministic pseudonym for IDs.

    Creates stable pseudonyms per release while protecting original identity.
    Useful for session_id, agent_id, publish_id in public datasets.

    Args:
        original_id: Original identifier to pseudonymize
        salt: Optional salt for this release (defaults to RKL_PSEUDO_SALT env var)

    Returns:
        Pseudonymized ID (first 16 chars of HMAC hash)

    Example:
        >>> pseudonymize_id("session-abc-123", "release-2025-Q1")
        'f3a8b2c1d4e5f6a7'
    """
    salt = salt or os.getenv("RKL_PSEUDO_SALT", "")
    hmac_hash = hmac_sha256_text(original_id, pepper=salt)
    return hmac_hash[:16]  # Short pseudonym for readability
