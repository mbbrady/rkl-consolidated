QUALITY_TRAJECTORIES_SCHEMA = {
    "required_fields": [
        "session_id",
        "artifact_id",
        "version",
        "score_name",
        "score",
        "evaluator_id",
        "reason_tag",
        "time_to_next_version"
    ],
    "field_types": {
        "session_id": str,
        "artifact_id": str,
        "version": int,
        "score_name": str,
        "score": (int, float),
        "evaluator_id": str,
        "reason_tag": str,
        "time_to_next_version": (int, float)
    }
}
