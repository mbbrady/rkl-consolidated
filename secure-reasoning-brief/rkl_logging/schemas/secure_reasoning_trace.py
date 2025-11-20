SECURE_REASONING_TRACE_SCHEMA = {
    "required_fields": [
        "session_id",
        "task_id",
        "turn_id",
        "steps"
    ],
    "field_types": {
        "session_id": str,
        "task_id": str,
        "turn_id": int,
        "steps": list
    }
}
