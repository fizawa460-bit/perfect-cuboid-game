#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local-stage32-full178-heavy"
AUTHORITY = 138_652_739_800_650_593_494
WORKER_PATH = ROOT / "stages/stage32/management/grf04-hpadj22-joint/run_grf04_hpadj22_full178_parent.py"
WINDOWS = ((0, 59), (60, 119), (120, 177))


def load_worker():
    spec = importlib.util.spec_from_file_location("full178_roi_worker", WORKER_PATH)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def geometric_prediction(neighbors: list[tuple[float, dict]], field: str) -> tuple[float, float]:
    usable = [(weight, float(row[field])) for weight, row in neighbors if float(row[field]) > 0]
    if not usable:
        return 0.0, float("inf")
    total = sum(weight for weight, _ in usable)
    mean = sum(weight * math.log(value) for weight, value in usable) / total
    spread = math.sqrt(sum(weight * (math.log(value) - mean) ** 2 for weight, value in usable) / total)
    return math.exp(mean), spread


def main() -> None:
    worker = load_worker()
    docs = {}
    row_identity = {}
    paths = list((LOCAL / "artifacts").rglob("row-*.json"))
    paths.append(ROOT / "stages/stage32/management/grf04-hpadj22-joint/GRF04-HPADJ22-V46-FULL178-B4-C0-W1-ROW065.json")
    paths.extend((LOCAL / "rows").rglob("row-*.json") if (LOCAL / "rows").exists() else [])
    for path in paths:
        doc = json.loads(path.read_text())
        target, result = doc["target"], doc["result"]
        key = (int(target["band_position"]), int(target["chunk_position"]), int(target["row_index"]))
        docs[key] = {
            "band": key[0], "chunk": key[1], "row": key[2],
            "row_id": str(target["row_id"]), "g": int(target["g"]), "d": int(target["d"]),
            "baseline": int(result["hpadj22_exact_survivors"]),
            "improvement": int(result["exact_improvement"]),
            "runtime": float(doc["timing_seconds"]["row_total"]),
        }
        row_identity[key[2]] = (str(target["row_id"]), int(target["g"]), int(target["d"]))
    if set(row_identity) != set(range(178)):
        raise SystemExit("incomplete row identity map")

    candidates = []
    for band in range(8):
        for chunk in range(4):
            b0, b1 = worker.chunks_for_band(band)[chunk]
            midpoint = (b0 + b1) / 2
            for row in range(178):
                row_id, g, d = row_identity[row]
                if d // 2 < b0 or (band, chunk, row) in docs:
                    continue
                same_row = []
                same_spatial = []
                for known in docs.values():
                    kb0, kb1 = worker.chunks_for_band(known["band"])[known["chunk"]]
                    kmid = (kb0 + kb1) / 2
                    if known["row"] == row:
                        same_row.append((6.0 / (1.0 + abs(kmid - midpoint) / 3.0), known))
                    if known["band"] == band and known["chunk"] == chunk and known["g"] == g:
                        same_spatial.append((3.0 / (1.0 + abs(known["d"] - d) / 4.0), known))
                    elif known["band"] == band and known["g"] == g:
                        same_spatial.append((0.8 / (1.0 + abs(known["d"] - d) / 4.0 + abs(kmid - midpoint) / 3.0), known))
                same_row.sort(key=lambda item: -item[0])
                same_spatial.sort(key=lambda item: -item[0])
                neighbors = same_row[:8] + same_spatial[:12]
                baseline, baseline_spread = geometric_prediction(neighbors, "baseline")
                improvement, improvement_spread = geometric_prediction(neighbors, "improvement")
                runtime, runtime_spread = geometric_prediction(neighbors, "runtime")
                if not baseline or not improvement or not runtime:
                    continue
                rate = improvement / baseline
                roi = improvement * 3600 / runtime
                nearest_d = min((abs(item[1]["d"] - d) for item in same_spatial), default=999)
                if len(same_row) >= 5 and nearest_d <= 4 and max(improvement_spread, runtime_spread) <= 0.8:
                    confidence = "HIGH"
                elif len(same_row) >= 2 and nearest_d <= 12 and max(improvement_spread, runtime_spread) <= 1.2:
                    confidence = "MEDIUM"
                else:
                    confidence = "LOW"
                window = 0 if row <= 59 else 1 if row <= 119 else 2
                candidates.append({
                    "band": band, "chunk": chunk, "window": window, "row": row,
                    "row_id": row_id, "g": g, "d": d, "b_range": f"[{b0},{b1}]",
                    "expected_hpadj22_baseline": round(baseline),
                    "expected_reduction_rate": rate,
                    "expected_improvement": round(improvement),
                    "expected_wall_seconds": runtime,
                    "expected_wall_hours": runtime / 3600,
                    "expected_improvement_per_wall_hour": roi,
                    "expected_global_main_reduction_fraction": improvement / AUTHORITY,
                    "expected_global_main_reduction_percent": improvement / AUTHORITY * 100,
                    "confidence": confidence,
                    "same_row_exact_neighbors": len(same_row),
                    "nearest_same_spatial_d_distance": nearest_d,
                    "log_spread_improvement": improvement_spread,
                    "log_spread_runtime": runtime_spread,
                    "exact_accounting_possible": True,
                    "accounting_key": f"b{band}-c{chunk}-row{row:03d}",
                    "estimate_only_no_credit": True,
                })

    candidates.sort(key=lambda row: row["expected_improvement_per_wall_hour"], reverse=True)
    for rank, candidate in enumerate(candidates, 1):
        candidate["roi_rank"] = rank
    (LOCAL / "roi-inventory.json").write_text(json.dumps(candidates, indent=2, sort_keys=True) + "\n")
    with (LOCAL / "roi-inventory.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(candidates[0]))
        writer.writeheader()
        writer.writerows(candidates)
    print(json.dumps(candidates[:25], indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
