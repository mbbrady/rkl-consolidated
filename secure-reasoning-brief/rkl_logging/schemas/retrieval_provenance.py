RETRIEVAL_PROVENANCE_SCHEMA = {
    "required_fields": [
        "session_id",
        "feed_name",
        "feed_url_hash",
        "candidate_count",
        "selected_count",
        "candidate_hashes",
        "selected_hashes",
        "cutoff_date",
        "category"
    ],
    "field_types": {
        "session_id": str,
        "feed_name": str,
        "feed_url_hash": str,
        "candidate_count": int,
        "selected_count": int,
        "candidate_hashes": list,
        "selected_hashes": list,
        "cutoff_date": str,
        "category": str
    }
}
