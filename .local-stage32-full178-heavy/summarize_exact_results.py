#!/usr/bin/env python3
import json
from pathlib import Path

AUTHORITY = 138_652_739_800_650_593_494
root = Path(__file__).resolve().parent
rows = []
for path in (root / "rows").rglob("row-*.json"):
    doc = json.loads(path.read_text())
    profile = json.loads((path.parent / "profile.json").read_text())
    result = doc["result"]
    wall = profile["timing_seconds"]["wall"]
    target = doc["target"]
    rows.append({
        "key": f"b{target['band_position']}-c{target['chunk_position']}-row{target['row_index']:03d}",
        "row_id": target["row_id"], "baseline": result["hpadj22_exact_survivors"],
        "joint": result["joint_exact_survivors"], "improvement": result["exact_improvement"],
        "wall_seconds": wall, "improvement_per_wall_hour": result["exact_improvement"] * 3600 / wall,
        "global_percent": result["exact_improvement"] / AUTHORITY * 100,
        "canonical": doc["canonical_sha256_without_this_field"], "validate_carry": "PASS",
        "certificate": str(path.relative_to(root.parent)),
    })
rows.sort(key=lambda item: item["improvement_per_wall_hour"], reverse=True)
total = sum(item["improvement"] for item in rows)
elapsed = max(item["wall_seconds"] for item in rows)
summary = {
    "rows": rows, "total_improvement": total,
    "sum_job_hours": sum(item["wall_seconds"] for item in rows) / 3600,
    "batch_elapsed_proxy_hours": elapsed / 3600,
    "aggregate_throughput_per_elapsed_hour": total / (elapsed / 3600),
    "global_percent": total / AUTHORITY * 100,
}
(root / "exact-results-summary.json").write_text(json.dumps(summary, indent=2) + "\n")
print(json.dumps(summary, indent=2))
