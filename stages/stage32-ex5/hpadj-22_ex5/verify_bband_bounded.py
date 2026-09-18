#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
WORKER = HERE / "run_full_bband.py"
WORKER_BLOB = "2c998a190baaf5f29b33a91fd9efedbb036cef46"
BOUNDED = HERE / "BOUNDED-RESULT.json"
BOUNDED_BLOB = "837ae21d2ef80a58d5d61bbfbedf5e4277ff5d0e"
BOUNDED_CANON = "b3387e3f07a02a30bfc5558ad72859c72c25a5289320abd22ac1947bf53b3d77"


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canonical(obj: dict) -> str:
    body = dict(obj)
    body.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(body, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def load_worker():
    req(WORKER.is_file() and git_blob(WORKER) == WORKER_BLOB, "band worker blob drift")
    spec = importlib.util.spec_from_file_location("hpadj22_band_bounded_equiv", WORKER)
    req(spec is not None and spec.loader is not None, "cannot load band worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    w = load_worker()
    req(BOUNDED.is_file() and git_blob(BOUNDED) == BOUNDED_BLOB, "bounded result blob drift")
    bounded = json.loads(BOUNDED.read_text())
    req(bounded.get("canonical_sha256_without_this_field") == BOUNDED_CANON, "bounded stored canonical drift")
    req(canonical(bounded) == BOUNDED_CANON, "bounded canonical drift")
    expected = {r["row_id"]: r for r in bounded["rows"] if int(r["d"]) <= 16}
    req(len(expected) == 10, "expected ten d<=16 bounded rows")

    ctx = w.source_context()
    bc, _, _, _, _, _, _, _, rows, _, _, _, _ = ctx
    joint = bc.build_joint_bc_shard(11, 0, 11)
    tested = []
    for idx, (row_id, _, d) in enumerate(rows):
        if int(d) > 16:
            continue
        rec = w.compute_row_cell(ctx, joint, 0, idx)
        t = rec["totals"]
        e = expected[row_id]
        req(int(t["rejected_mass"]) == int(e["hpadj08_exact_square_rejected_terminals"]),
            f"HPADJ08 bounded mismatch {row_id}")
        req(int(t["hpadj21_floor"]) == int(e["hpadj21_floor_sum"]),
            f"HPADJ21 bounded mismatch {row_id}")
        req(int(t["hpadj22_exact_survivors"]) == int(e["hpadj22_exact_survivor_sum"]),
            f"HPADJ22 bounded mismatch {row_id}")
        req(int(t["improvement"]) == int(e["improvement"]), f"gain mismatch {row_id}")
        req(bool(t["strict"]) is True, f"strictness mismatch {row_id}")
        tested.append({
            "row_id": row_id,
            "row_index": idx,
            "canonical": rec["canonical_sha256_without_this_field"],
            "gain": int(t["improvement"]),
        })
    req(len(tested) == 10, "tested row count drift")
    out = {
        "schema": "STAGE32EX5_HPADJ22_BAND_WORKER_BOUNDED_EQUIVALENCE_V1",
        "status": "EXACT_BAND_WORKER_BOUNDED_EQUIVALENCE_PASS",
        "source_locks": {
            "band_worker_blob_sha1": WORKER_BLOB,
            "bounded_result_blob_sha1": BOUNDED_BLOB,
            "bounded_result_canonical_sha256": BOUNDED_CANON,
        },
        "band_position": 0,
        "b_interval": [0, 11],
        "test_H": 11,
        "tested_rows": tested,
        "checks": {
            "row_count": len(tested),
            "hpadj08_rejection_reproduced": True,
            "hpadj21_floor_reproduced": True,
            "hpadj22_exact_reproduced": True,
            "all_rows_strict": True,
        },
        "firewalls": {
            "full178_complete": False,
            "stage32_main_credit": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
