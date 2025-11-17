"""
Schema definitions for all log artifacts.

Each artifact type has a versioned schema defining:
- Required fields
- Optional fields
- Field types
- Deprecated fields (for migration)
"""

from .execution_context import EXECUTION_CONTEXT_SCHEMA
from .agent_graph import AGENT_GRAPH_SCHEMA
from .boundary_events import BOUNDARY_EVENTS_SCHEMA
from .governance_ledger import GOVERNANCE_LEDGER_SCHEMA

# Master schema registry
# Note: Keys match artifact_type logged by agents
SCHEMAS = {
    "execution_context": EXECUTION_CONTEXT_SCHEMA,
    "reasoning_graph_edge": AGENT_GRAPH_SCHEMA,  # Maps to agent_graph schema
    "boundary_event": BOUNDARY_EVENTS_SCHEMA,    # Singular to match agent logging
    "governance_ledger": GOVERNANCE_LEDGER_SCHEMA
}

# Aliases for backward compatibility with config
SCHEMAS["agent_graph"] = AGENT_GRAPH_SCHEMA
SCHEMAS["boundary_events"] = BOUNDARY_EVENTS_SCHEMA


def validate_record(artifact_type: str, record: dict) -> tuple[bool, list[str]]:
    """
    Validate a log record against its schema.

    Args:
        artifact_type: Type of artifact (e.g., "execution_context")
        record: Record to validate

    Returns:
        Tuple of (is_valid, list_of_errors)

    Example:
        >>> valid, errors = validate_record("execution_context", my_record)
        >>> if not valid:
        ...     print(f"Validation errors: {errors}")
    """
    if artifact_type not in SCHEMAS:
        return False, [f"Unknown artifact type: {artifact_type}"]

    schema = SCHEMAS[artifact_type]
    errors = []

    # Check required fields
    for field in schema["required_fields"]:
        if field not in record:
            errors.append(f"Missing required field: {field}")

    # Check field types (basic validation)
    for field, value in record.items():
        if field in schema.get("field_types", {}):
            expected_type = schema["field_types"][field]
            if not isinstance(value, expected_type):
                errors.append(
                    f"Field '{field}' has wrong type. "
                    f"Expected {expected_type.__name__}, got {type(value).__name__}"
                )

    return len(errors) == 0, errors


__all__ = ["SCHEMAS", "validate_record"]
