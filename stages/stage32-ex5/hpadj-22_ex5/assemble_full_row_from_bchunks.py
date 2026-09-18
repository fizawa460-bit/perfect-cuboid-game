#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
BCHUNK = HERE / "run_full_bchunk.py"
BCHUNK_BLOB = "3fc6e7e4aff539be5b60528d1d1b2e41529ddc03"
SCHEMA = "STAGE32EX5_HPADJ22_FULL_ROW_CERT_V1"


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


def load_bchunk():
    req(BCHUNK.is_file() and git_blob(BCHUNK) == BCHUNK_BLOB, "bchunk worker drift")
    spec = importlib.util.spec_from_file_location("hpadj22_bchunk_locked_for_assembler", BCHUNK)
    req(spec is not None and spec.loader is not None, "cannot load bchunk worker")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def add_caps(dst, records):
    for s, B, m in records:
        dst[(int(s), int(B))] += int(m)


def assemble_chunks(row_index: int, chunks: list[dict]) -> dict:
    bc = load_bchunk()
    bnd = bc.load_bound()
    h21 = bnd.load_module(bnd.H21, bnd.H21_BLOB, "hpadj21_bounded_locked_for_hpadj22_assembler")
    h20 = h21.load_parent()
    h19 = h20.load_parent()
    h18 = h19.load_parent()
    h17 = h18.load_parent()
    h16 = h17.load_parent()
    p15 = h16.load_module(h16.PARENT, h16.PARENT_BLOB, "hpadj15_locked_for_hpadj22_assembler")
    p14 = p15.load_parent()
    counter = p14.load_counter()
    manifest = counter.load_locked_json(
        p14.MANIFEST, p14.LOCKS["manifest_blob"], p14.LOCKS["manifest_canonical"], "FULL178 manifest"
    )
    rows = counter.manifest_rows(manifest)
    req(len(rows) == 178 and 0 <= row_index < 178, "row index/coverage drift")
    row_id, g0, d0 = rows[row_index]
    g, d = int(g0), int(d0)
    h = d // 2

    checked = []
    for dct in chunks:
        checked.append(bc.validate_obj(
            dct, row_index, int(dct["b_range"]["start"]), int(dct["b_range"]["stop"])
        ))
    checked.sort(key=lambda x: int(x["b_range"]["start"]))
    cursor = 0
    for x in checked:
        start, stop = int(x["b_range"]["start"]), int(x["b_range"]["stop"])
        req(start == cursor, f"b coverage gap/overlap at {cursor}")
        cursor = stop + 1
        req(x["row"]["row_id"] == row_id and int(x["row"]["g"]) == g and int(x["row"]["d"]) == d,
            "chunk row identity drift")
    req(cursor == h + 1, "b coverage incomplete")

    acc = {
        i: {"pre": 0, "reject": 0, "h22": 0, "h21_caps": defaultdict(int)}
        for i in range(len(p15.PLANNED))
    }
    for x in checked:
        for rec in x["interval_records"]:
            i = int(rec["interval_position"])
            acc[i]["pre"] += int(rec["pre_mass"])
            acc[i]["reject"] += int(rec["rejected_mass"])
            acc[i]["h22"] += int(rec["hpadj22_exact_survivors"])
            add_caps(acc[i]["h21_caps"], rec["hpadj21_caps"])

    retained_rejected = p15.load_certificate(p14)
    pre_total = reject_total = post_total = h21_total = h22_total = strict_cells = 0
    cell_records = []
    for i, interval in enumerate(p15.PLANNED):
        got = acc[i]
        P = int(got["pre"])
        R = int(got["reject"])
        retained_R = int(retained_rejected[(interval, g, d)])
        req(R == retained_R, f"retained HPADJ08 rejected mass mismatch {(interval,g,d)}")
        Mpost = P - R
        req(Mpost >= 0, f"negative post mass {(interval,g,d)}")
        req(sum(got["h21_caps"].values()) == P, f"HPADJ21 capacity mass mismatch {(interval,g,d)}")
        h21_obj, _, _, _ = h18.optimize_cell_exact_predomain(got["h21_caps"], Mpost)
        h21_floor = h21_obj.numerator // h21_obj.denominator
        h22_exact = int(got["h22"])
        req(h22_exact <= h21_floor, f"HPADJ22 weakened HPADJ21 {(interval,g,d)}")
        strict = h22_exact < h21_floor
        strict_cells += int(strict)
        pre_total += P
        reject_total += R
        post_total += Mpost
        h21_total += h21_floor
        h22_total += h22_exact
        cell_records.append({
            "interval_position": i,
            "b_interval": list(interval),
            "pre_mass": P,
            "rejected_mass": R,
            "post_mass": Mpost,
            "hpadj21_num": h21_obj.numerator,
            "hpadj21_den": h21_obj.denominator,
            "hpadj21_floor": h21_floor,
            "hpadj22_exact_survivors": h22_exact,
            "strict": strict,
        })

    req(pre_total - reject_total == post_total, "row mass conservation")
    req(h22_total <= h21_total, "row weakened HPADJ21")
    out = {
        "schema": SCHEMA,
        "route_id": "HPADJ-22_ex5",
        "status": "EXACT_HPADJ22_ROW_COMPLETE_HOSTILE_AUDIT_REQUIRED",
        "row": {"index": row_index, "row_id": row_id, "g": g, "d": d},
        "source_locks": {
            "bchunk_worker_git_blob": BCHUNK_BLOB,
            "bounded_gate_git_blob": bc.BOUND_BLOB,
            "hpadj21_bounded_git_blob": bnd.H21_BLOB,
            "hpadj20_parent_git_blob": h21.PARENT_BLOB,
            "full178_manifest_blob_sha1": p14.LOCKS["manifest_blob"],
            "hpadj10_counter_blob_sha1": p14.LOCKS["hpadj10_counter_blob"],
        },
        "totals": {
            "pre_mass": pre_total,
            "rejected_mass": reject_total,
            "post_mass": post_total,
            "hpadj21_cellwise_floor_sum": h21_total,
            "hpadj22_exact_survivor_sum": h22_total,
            "strict_cell_count": strict_cells,
            "floor_improvement": h21_total - h22_total,
        },
        "cell_records": cell_records,
        "semantics": {
            "complete_b_coverage_exactly_once": True,
            "b_partition_is_execution_only": True,
            "retained_hpadj08_rejected_mass_replayed_cellwise": True,
            "same_population_as_hpadj21": True,
            "same_picard_qA_rule_as_hpadj21": True,
            "additive_subtraction_used": False,
        },
        "credit_firewall": {
            "partial_output_credit": False,
            "stage32_main_credit": False,
            "full178_completion_credit": False,
            "theorem_credit": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "endpoint_credit": False,
            "perfect_cuboid_credit": False,
            "merge_authorized": False,
        },
    }
    out["canonical_sha256_without_this_field"] = canonical(out)
    return out


def assemble_files(row_index: int, paths: list[Path]) -> dict:
    bc = load_bchunk()
    chunks = []
    for p in paths:
        req(p.is_file(), f"missing chunk {p}")
        d = json.loads(p.read_text())
        chunks.append(bc.validate_obj(d, row_index, int(d["b_range"]["start"]), int(d["b_range"]["stop"])))
    return assemble_chunks(row_index, chunks)


def validate_obj(d: dict, row_index: int) -> dict:
    req(d.get("schema") == SCHEMA, "row schema drift")
    req(int(d["row"]["index"]) == row_index, "row index drift")
    req(d["source_locks"]["bchunk_worker_git_blob"] == BCHUNK_BLOB, "bchunk source drift")
    req(d.get("canonical_sha256_without_this_field") == canonical(d), "row canonical drift")
    req(all(v is False for v in d["credit_firewall"].values()), "row credit firewall")
    return d


def validate(path: Path, row_index: int) -> dict:
    req(path.is_file(), "missing row certificate")
    return validate_obj(json.loads(path.read_text()), row_index)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--row-index", type=int, required=True)
    ap.add_argument("--chunks-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()
    paths = sorted(args.chunks_dir.rglob(f"hpadj22-bchunk-{args.row_index}-*.json"))
    req(paths, "no chunk certificates")
    d = assemble_files(args.row_index, paths)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(d, sort_keys=True, separators=(",", ":")) + "\n")
    validate(args.output, args.row_index)
    print(json.dumps({
        "row_index": args.row_index,
        "row_id": d["row"]["row_id"],
        "chunks": len(paths),
        "hpadj21_floor": d["totals"]["hpadj21_cellwise_floor_sum"],
        "hpadj22_exact": d["totals"]["hpadj22_exact_survivor_sum"],
        "gain": d["totals"]["floor_improvement"],
        "canonical": d["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
