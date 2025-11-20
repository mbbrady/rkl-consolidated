HUMAN_INTERVENTIONS_SCHEMA = {
    "required_fields": [
        "session_id",
        "event_id",
        "t",
        "human_role",
        "intervention_type"
    ],
    "field_types": {
        "session_id": str,
        "event_id": str,
        "t": int,
        "human_role": str,
        "intervention_type": str,
        "target_turn_id": int,
        "delta_metrics": dict,
        "rationale_tag": str
    }
}
