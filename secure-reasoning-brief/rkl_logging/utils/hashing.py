"""
Hashing utilities for cross-referencing without exposing content.

All hashing uses SHA-256 for consistency and security.
"""

import hashlib
import json
from typing import Any, Dict


def sha256_text(text: str) -> str:
    """
    Generate SHA-256 hash of text content.

    Args:
        text: Text to hash

    Returns:
        Hex-encoded SHA-256 hash with 'sha256:' prefix

    Example:
        >>> sha256_text("Hello, world!")
        'sha256:315f5bdb76d078c43b8ac0064e4a0164612b1fce77c869345bfc94c75894edd3'
    """
    if not isinstance(text, str):
        text = str(text)

    hash_obj = hashlib.sha256(text.encode('utf-8'))
    return f"sha256:{hash_obj.hexdigest()}"


def sha256_dict(data: Dict[str, Any]) -> str:
    """
    Generate SHA-256 hash of dictionary content.

    Args:
        data: Dictionary to hash

    Returns:
        Hex-encoded SHA-256 hash with 'sha256:' prefix

    Note:
        Dictionary is serialized to JSON with sorted keys for consistency.
    """
    # Sort keys for consistent hashing
    json_str = json.dumps(data, sort_keys=True)
    return sha256_text(json_str)


def sha256_file(file_path: str, chunk_size: int = 8192) -> str:
    """
    Generate SHA-256 hash of file content.

    Args:
        file_path: Path to file
        chunk_size: Size of chunks to read (for large files)

    Returns:
        Hex-encoded SHA-256 hash with 'sha256:' prefix
    """
    hash_obj = hashlib.sha256()

    with open(file_path, 'rb') as f:
        while chunk := f.read(chunk_size):
            hash_obj.update(chunk)

    return f"sha256:{hash_obj.hexdigest()}"


def hash_prompt(prompt_text: str, version: str = "v1") -> str:
    """
    Generate versioned hash for prompts.

    Args:
        prompt_text: Prompt template text
        version: Prompt version identifier

    Returns:
        Versioned hash like 'prompt:v1:sha256:abc123...'
    """
    hash_part = sha256_text(prompt_text).replace('sha256:', '')
    return f"prompt:{version}:{hash_part}"


def hash_document(doc_content: str, source: str = "") -> str:
    """
    Generate hash for source documents.

    Args:
        doc_content: Document text content
        source: Source identifier (e.g., URL, filename)

    Returns:
        Hash with source context
    """
    combined = f"{source}|{doc_content}"
    hash_part = sha256_text(combined).replace('sha256:', '')
    return f"doc:{hash_part}"
