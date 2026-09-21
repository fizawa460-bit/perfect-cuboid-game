#!/usr/bin/env python3
from __future__ import annotations

import csv
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOCAL = ROOT / ".local-stage32-full178-heavy"
ARTIFACTS = LOCAL / "artifacts"
WORKER = ROOT / "stages/stage32/management/grf04-hpadj22-joint/run_grf04_hpadj22_full178_parent.py"
WINDOWS = ((0, 59), (60, 119), (120, 177))
GENS = ("g10", "g11", "g12", "g13")


def load_worker():
    spec = importlib.util.spec_from_file_location("full178_worker_inventory", WORKER)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def artifact_dir(gen: str, band: int, chunk: int, window: int) -> Path:
    name = f"stage32-main-v46-grf04-hpadj22-full178-window-{band}-{chunk}-{window}"
    return ARTIFACTS / gen / name


def main() -> None:
    worker = load_worker()
    row_identity: dict[int, tuple[str, int, int]] = {}
    docs: dict[tuple[int, int, int], dict[int, tuple[str, dict]]] = {}
    complete_by_gen: dict[tuple[int, int, int], list[str]] = {}

    for gen in GENS:
        for path in (ARTIFACTS / gen).rglob("row-*.json"):
            doc = json.loads(path.read_text())
            target = doc["target"]
            ri = int(target["row_index"])
            key = (int(target["band_position"]), int(target["chunk_position"]),
                   0 if ri <= 59 else 1 if ri <= 119 else 2)
            row_identity[ri] = (str(target["row_id"]), int(target["g"]), int(target["d"]))
            docs.setdefault(key, {})[ri] = (gen, doc)
        for manifest in (ARTIFACTS / gen).rglob("PARENT-WINDOW-COMPLETE.json"):
            doc = json.loads(manifest.read_text())
            parent = doc["parent"]
            key = (int(parent["band_position"]), int(parent["chunk_position"]),
                   int(parent["row_window_position"]))
            complete_by_gen.setdefault(key, []).append(gen)

    local_seed = ROOT / "stages/stage32/management/grf04-hpadj22-joint/GRF04-HPADJ22-V46-FULL178-B4-C0-W1-ROW065.json"
    seed_doc = json.loads(local_seed.read_text())
    seed_target = seed_doc["target"]
    row_identity[65] = (str(seed_target["row_id"]), int(seed_target["g"]), int(seed_target["d"]))
    docs.setdefault((4, 0, 1), {})[65] = ("local", seed_doc)

    if set(row_identity) != set(range(178)):
        missing = sorted(set(range(178)) - set(row_identity))
        raise SystemExit(f"row identity map incomplete: {missing}")

    records = []
    for band in range(8):
        for chunk in range(4):
            b0, b1 = worker.chunks_for_band(band)[chunk]
            for window, (r0, r1) in enumerate(WINDOWS):
                expected = [ri for ri in range(r0, r1 + 1) if row_identity[ri][2] // 2 >= b0]
                carried = sorted(docs.get((band, chunk, window), {}))
                missing = sorted(set(expected) - set(carried))
                recent = max(carried) if carried else None
                recent_doc = docs.get((band, chunk, window), {}).get(recent) if recent is not None else None
                recent_runtime = (recent_doc[1].get("timing_seconds", {}).get("row_total")
                                  if recent_doc else None)
                recent_gen = recent_doc[0] if recent_doc else None
                if recent_runtime is None:
                    difficulty, risk = "unknown", "unknown"
                elif recent_runtime >= 4680:
                    difficulty, risk = "extreme", "HIGH: >=78m soft wall"
                elif recent_runtime >= 3600:
                    difficulty, risk = "very-heavy", "HIGH: next row may exceed 78m"
                elif recent_runtime >= 1800:
                    difficulty, risk = "heavy", "MEDIUM"
                elif recent_runtime >= 600:
                    difficulty, risk = "moderate", "LOW-MEDIUM"
                else:
                    difficulty, risk = "light", "LOW"
                records.append({
                    "band": band, "chunk": chunk, "window": window,
                    "b_range": f"[{b0},{b1}]", "expected_rows": len(expected),
                    "carried_completed_rows": len(carried),
                    "next_missing_rows": ",".join(map(str, missing[:12])),
                    "missing_row_count": len(missing),
                    "recent_row": recent, "recent_row_runtime_seconds": recent_runtime,
                    "recent_generation": recent_gen,
                    "estimated_difficulty": difficulty, "actions_timeout_risk": risk,
                    "complete_manifest_generations": ",".join(complete_by_gen.get((band, chunk, window), [])),
                })

    with (LOCAL / "partial-window-inventory.csv").open("w", newline="", encoding="utf-8") as fh:
        writer = csv.DictWriter(fh, fieldnames=list(records[0]))
        writer.writeheader()
        writer.writerows(records)
    (LOCAL / "partial-window-inventory.json").write_text(
        json.dumps(records, indent=2, sort_keys=True) + "\n", encoding="utf-8")

    partial = [r for r in records if r["missing_row_count"]]
    candidates = sorted(partial, key=lambda r: (
        -(r["recent_row_runtime_seconds"] or -1), r["missing_row_count"],
        r["band"], r["chunk"], r["window"]))
    (LOCAL / "heavy-candidates.json").write_text(
        json.dumps(candidates, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps({
        "windows": len(records), "partial_windows": len(partial),
        "complete_windows": len(records) - len(partial),
        "carried_row_certificates": sum(r["carried_completed_rows"] for r in records),
        "missing_row_certificates": sum(r["missing_row_count"] for r in records),
        "top_candidates": candidates[:20],
    }, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
