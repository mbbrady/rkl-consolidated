SYSTEM_STATE_SCHEMA = {
    "required_fields": [
        "session_id",
        "stage",
        "host",
        "platform",
        "cpu_percent",
        "load1",
        "load5",
        "load15",
        "mem_total_bytes",
        "mem_used_bytes",
        "mem_free_bytes",
        "mem_percent"
    ],
    "field_types": {
        "session_id": str,
        "stage": str,
        "host": str,
        "platform": str,
        "cpu_percent": (int, float),
        "load1": (int, float),
        "load5": (int, float),
        "load15": (int, float),
        "mem_total_bytes": int,
        "mem_used_bytes": int,
        "mem_free_bytes": int,
        "mem_percent": (int, float),
        "gpus": list,
        "gpu_count": int,
        "driver_version": str,
        "disk_io": dict,
        "net_io": dict,
        "proc_cpu_percent": (int, float),
        "proc_mem_bytes": (dict, int)
    }
}
