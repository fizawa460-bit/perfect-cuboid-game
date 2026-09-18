#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_full_bband.py"
WORKER_BLOB = "2c998a190baaf5f29b33a91fd9efedbb036cef46"
EXPECTED_BANDS = 8
EXPECTED_ROWS = 178


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(body, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def load_worker():
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "band worker blob drift")
    spec = importlib.util.spec_from_file_location("hpadj22_band_locked_for_recovery", WORKER)
    req(spec is not None and spec.loader is not None, "cannot load band worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--artifacts-root", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    w = load_worker()
    ctx = w.source_context()
    bc, bnd, h21, _, _, _, p14, _, rows, _, _, _, _ = ctx
    locks = w.row_source_locks(bc, bnd, h21, p14)

    bands = []
    complete_count = 0
    total_valid_rows = 0
    discovered_artifacts = 0
    for pos in range(EXPECTED_BANDS):
        candidates = [
            p for p in args.artifacts_root.rglob(f"hpadj22-band-{pos}")
            if p.is_dir()
        ]
        req(len(candidates) <= 1, f"duplicate artifact directory for band {pos}")
        if not candidates:
            bands.append({
                "band_position": pos,
                "artifact_discovered": False,
                "validated_rows": 0,
                "complete": False,
                "missing_rows": list(range(EXPECTED_ROWS)),
            })
            continue
        discovered_artifacts += 1
        root = candidates[0]
        valid = {}
        for rp in sorted(root.rglob("row-*.json")):
            raw = json.loads(rp.read_text())
            if raw.get("schema") != w.SCHEMA_ROW or int(raw.get("band_position", -1)) != pos:
                continue
            idx = int(raw.get("row", {}).get("index", -1))
            req(0 <= idx < EXPECTED_ROWS, f"row index out of range band {pos}")
            req(idx not in valid, f"duplicate row checkpoint band {pos} row {idx}")
            valid[idx] = w.validate_row_obj(raw, pos, idx, rows, locks)
        total_valid_rows += len(valid)
        complete = False
        marker_canonical = None
        marker = root / "BAND-COMPLETE.json"
        if marker.is_file():
            m, rows_data = w.validate_complete_dir(root, pos, ctx)
            req(len(rows_data) == EXPECTED_ROWS, f"complete band row count {pos}")
            complete = True
            complete_count += 1
            marker_canonical = m["canonical_sha256_without_this_field"]
        bands.append({
            "band_position": pos,
            "artifact_discovered": True,
            "validated_rows": len(valid),
            "complete": complete,
            "complete_canonical": marker_canonical,
            "missing_rows": [i for i in range(EXPECTED_ROWS) if i not in valid],
        })

    out = {
        "schema": "STAGE32EX5_HPADJ22_RECOVERY_SNAPSHOT_V1",
        "route_id": "HPADJ-22_ex5",
        "source_locks": {"band_worker_git_blob": WORKER_BLOB},
        "artifact_enumeration": {
            "expected_band_artifacts": EXPECTED_BANDS,
            "discovered_artifact_count": discovered_artifacts,
            "artifact_population_below_100": True,
        },
        "validated_carried_row_units": total_valid_rows,
        "complete_band_count": complete_count,
        "all_bands_complete": complete_count == EXPECTED_BANDS,
        "bands": bands,
        "credit": {
            "partial_output_credit": False,
            "full178_completion_credit": False,
            "stage32_main_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, separators=(",", ":")) + "\n")
    print(json.dumps({
        "discovered_artifacts": discovered_artifacts,
        "validated_rows": total_valid_rows,
        "complete_bands": complete_count,
        "all_complete": out["all_bands_complete"],
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
