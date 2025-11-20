FAILURE_SNAPSHOTS_SCHEMA = {
    "required_fields": [
        "session_id",
        "reason",
        "failed_count",
        "failed_titles"
    ],
    "field_types": {
        "session_id": str,
        "reason": str,
        "failed_count": int,
        "failed_titles": list
    }
}
