HALLUCINATION_MATRIX_SCHEMA = {
    "required_fields": [
        "session_id",
        "artifact_id",
        "verdict",
        "method"
    ],
    "field_types": {
        "session_id": str,
        "artifact_id": str,
        "verdict": str,
        "method": str,
        "confidence": (int, float),
        "evidence_doc_hashes": list,
        "error_type": str,
        "notes": str
    }
}
