#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import importlib.util
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
BCHUNK = HERE / "run_full_bchunk.py"
BCHUNK_BLOB = "3fc6e7e4aff539be5b60528d1d1b2e41529ddc03"
ASSEMBLER = HERE / "assemble_full_row_from_bchunks.py"
ASSEMBLER_BLOB = "16c204bc64ed1cf7f30571fb6987eab9f0a13b38"
RESULT = HERE / "BOUNDED-RESULT.json"
RESULT_BLOB = "837ae21d2ef80a58d5d61bbfbedf5e4277ff5d0e"
RESULT_CANON = "b3387e3f07a02a30bfc5558ad72859c72c25a5289320abd22ac1947bf53b3d77"
TARGETS = ("g0-d016", "g1-d016")


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


def load(path: Path, blob_sha: str, name: str):
    req(path.is_file() and git_blob(path) == blob_sha, f"{name} blob drift")
    spec = importlib.util.spec_from_file_location(name, path)
    req(spec is not None and spec.loader is not None, f"cannot load {name}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def main() -> None:
    bc = load(BCHUNK, BCHUNK_BLOB, "hpadj22_bchunk_equiv")
    asm = load(ASSEMBLER, ASSEMBLER_BLOB, "hpadj22_assembler_equiv")
    req(RESULT.is_file() and git_blob(RESULT) == RESULT_BLOB, "bounded result blob drift")
    bounded = json.loads(RESULT.read_text())
    req(bounded.get("canonical_sha256_without_this_field") == RESULT_CANON, "bounded canonical stored drift")
    req(canonical(bounded) == RESULT_CANON, "bounded canonical drift")
    by_id = {r["row_id"]: r for r in bounded["rows"]}

    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "hpadj21_for_hpadj22_equiv")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_for_hpadj22_equiv")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    index_by_id = {row_id: i for i, (row_id, _, _) in enumerate(rows)}

    receipts = []
    for row_id in TARGETS:
        req(row_id in index_by_id and row_id in by_id, f"missing target {row_id}")
        i = index_by_id[row_id]
        h = int(rows[i][2]) // 2

        direct_chunk = bc.compute_chunk(i, 0, h)
        direct = asm.assemble_chunks(i, [direct_chunk])

        split_chunks = []
        start = 0
        while start <= h:
            stop = min(start + 3, h)
            split_chunks.append(bc.compute_chunk(i, start, stop))
            start = stop + 1
        split = asm.assemble_chunks(i, split_chunks)
        req(direct == split, f"direct/split row dictionary mismatch {row_id}")

        retained = by_id[row_id]
        totals = direct["totals"]
        req(totals["hpadj21_cellwise_floor_sum"] == int(retained["hpadj21_floor_sum"]),
            f"bounded HPADJ21 mismatch {row_id}")
        req(totals["hpadj22_exact_survivor_sum"] == int(retained["hpadj22_exact_survivor_sum"]),
            f"bounded HPADJ22 mismatch {row_id}")
        req(totals["floor_improvement"] == int(retained["improvement"]),
            f"bounded gain mismatch {row_id}")
        req(totals["rejected_mass"] == int(retained["hpadj08_exact_square_rejected_terminals"]),
            f"bounded HPADJ08 rejection mismatch {row_id}")
        receipts.append({
            "row_id": row_id,
            "row_index": i,
            "h": h,
            "split_chunk_count": len(split_chunks),
            "row_canonical": direct["canonical_sha256_without_this_field"],
            "hpadj21_floor": totals["hpadj21_cellwise_floor_sum"],
            "hpadj22_exact": totals["hpadj22_exact_survivor_sum"],
            "gain": totals["floor_improvement"],
        })

    out = {
        "schema": "STAGE32EX5_HPADJ22_BCHUNK_EQUIVALENCE_BOUNDED_V1",
        "route_id": "HPADJ-22_ex5",
        "status": "EXACT_DIRECT_VS_BCHUNK_EQUIVALENCE_PASS",
        "source_locks": {
            "bchunk_worker_blob_sha1": BCHUNK_BLOB,
            "assembler_blob_sha1": ASSEMBLER_BLOB,
            "bounded_result_blob_sha1": RESULT_BLOB,
            "bounded_result_canonical_sha256": RESULT_CANON,
        },
        "targets": receipts,
        "checks": {
            "single_full_b_chunk_vs_split_chunks_dictionary_equal": True,
            "exact_contiguous_b_coverage_required": True,
            "retained_bounded_rows_reproduced": True,
            "partial_output_credit": False,
        },
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "full178_complete": False,
            "heavy_run_armed": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    print(json.dumps(out, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
