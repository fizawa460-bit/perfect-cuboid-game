#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONTRACT = HERE / "FULL178-SCALEOUT-CONTRACT.json"
CONTRACT_BLOB = "ca1b195a3ee8e786707e1ef50b404ee8c19f1429"
CONTRACT_CANON = "02a350a4c4c9b5c999767386be499edfa4e635189ff8f0e37db0bece7a00f660"
WORKER = HERE / "td01_full178_b_shard.py"
WORKER_BLOB = "7f160f3db3300a6f089064167394635e3e88a2e5"
PLANNED = ((0, 11), (12, 23), (24, 35), (36, 47), (48, 59), (60, 71), (72, 83), (84, 96))
EXPECTED_OLD = 20_713_268_924_714_183_714_810
EXPECTED_EXACT = 40_886_299_509_963_924_857_401
EXPECTED_HPADJ08_ROW_STREAM = "d5d8ab364d122c4b3138d577442b383290ab7878e11629b3673058073690e5a1"
FIELDS = (
    "population",
    "old_group_cauchy_rejected",
    "hpadj08_exact_square_rejected",
    "hpadj08_exact_square_survivors",
    "grf02_plus_hpadj08_survivors",
    "grf02_additional_rejected_among_hpadj08_survivors",
)


def req(value: bool, message: str) -> None:
    if not value:
        raise SystemExit("FAIL: " + message)


def git_blob(path: Path) -> str:
    raw = path.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def expected_row_keys():
    return [(0, d) for d in range(8, 177, 2)] + [(1, d) for d in range(8, 193, 2)]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--inputs", nargs=8, required=True)
    ap.add_argument("--output", required=True)
    ns = ap.parse_args()

    req(git_blob(CONTRACT) == CONTRACT_BLOB, "scaleout contract blob drift")
    contract = json.loads(CONTRACT.read_text())
    req(contract.get("canonical_sha256_without_this_field") == CONTRACT_CANON and canon(contract) == CONTRACT_CANON, "scaleout contract canonical drift")
    req(git_blob(WORKER) == WORKER_BLOB, "worker blob drift")

    seen = set()
    aggregate_rows = {key: {field: 0 for field in FIELDS} for key in expected_row_keys()}
    shard_canonicals = []
    for raw_path in ns.inputs:
        path = Path(raw_path)
        obj = json.loads(path.read_text())
        req(obj.get("schema") == "STAGE32_32_01_178_TD01_FULL178_B_SHARD_RESULT_V1", f"bad shard schema: {path}")
        req(obj.get("route_id") == "TD01_GRF02_HPADJ08_TOPDOWN_COMPOSITION", f"wrong route: {path}")
        interval = tuple(obj.get("b_interval", []))
        req(interval in PLANNED, f"unexpected b interval: {interval}")
        req(interval not in seen, f"duplicate b interval: {interval}")
        seen.add(interval)
        req(obj.get("row_count") == 178, f"bad row_count: {path}")
        req(obj.get("canonical_sha256_without_this_field") == canon(obj), f"bad canonical: {path}")
        records = obj.get("records")
        req(isinstance(records, list) and len(records) == 178, f"bad records: {path}")
        for record in records:
            key = (int(record["g"]), int(record["d"]))
            req(key in aggregate_rows, f"unexpected row key: {key}")
            for field in FIELDS:
                aggregate_rows[key][field] += int(record[field])
        shard_canonicals.append({"b_interval": list(interval), "canonical_sha256": obj["canonical_sha256_without_this_field"]})

    req(seen == set(PLANNED), "not all planned shards supplied")

    totals = {field: 0 for field in FIELDS}
    rows = []
    old_stream = hashlib.sha256()
    for g, d in expected_row_keys():
        row = aggregate_rows[(g, d)]
        req(row["population"] == row["hpadj08_exact_square_rejected"] + row["hpadj08_exact_square_survivors"], f"HPADJ08 partition mismatch {(g,d)}")
        req(row["hpadj08_exact_square_survivors"] == row["grf02_plus_hpadj08_survivors"] + row["grf02_additional_rejected_among_hpadj08_survivors"], f"GRF02 partition mismatch {(g,d)}")
        req(row["grf02_plus_hpadj08_survivors"] <= row["hpadj08_exact_square_survivors"], f"combined survivor monotonicity failure {(g,d)}")
        for field in FIELDS:
            totals[field] += row[field]
        rows.append({"g": g, "d": d, **row})
        old_row = {
            "g": g,
            "d": d,
            "old_group_cauchy_candidate_rejected_terminals": row["old_group_cauchy_rejected"],
            "stored_exact_square_candidate_rejected_terminals": row["hpadj08_exact_square_rejected"],
            "incremental_candidate_over_group_cauchy": row["hpadj08_exact_square_rejected"] - row["old_group_cauchy_rejected"],
        }
        old_stream.update(json.dumps(old_row, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    req(totals["old_group_cauchy_rejected"] == EXPECTED_OLD, "aggregate old Cauchy total does not reproduce retained HPADJ08")
    req(totals["hpadj08_exact_square_rejected"] == EXPECTED_EXACT, "aggregate exact-square total does not reproduce retained HPADJ08")
    req(old_stream.hexdigest() == EXPECTED_HPADJ08_ROW_STREAM, "aggregate HPADJ08 row stream mismatch")
    req(totals["population"] == totals["hpadj08_exact_square_rejected"] + totals["hpadj08_exact_square_survivors"], "aggregate HPADJ08 partition mismatch")
    req(totals["hpadj08_exact_square_survivors"] == totals["grf02_plus_hpadj08_survivors"] + totals["grf02_additional_rejected_among_hpadj08_survivors"], "aggregate GRF02 partition mismatch")

    result = {
        "schema": "STAGE32_32_01_178_TD01_FULL178_AGGREGATE_CANDIDATE_V1",
        "stage": 32,
        "route_id": "TD01_GRF02_HPADJ08_TOPDOWN_COMPOSITION",
        "status": "FULL178_AGGREGATE_CANDIDATE_NO_CREDIT_PENDING_AUDIT_AND_MAIN_COMPOSITION",
        "coverage": {"all_planned_shards_present": True, "shard_count": 8, "row_count": 178},
        "baseline_reproduction": {
            "old_group_cauchy_rejected": totals["old_group_cauchy_rejected"],
            "hpadj08_exact_square_rejected": totals["hpadj08_exact_square_rejected"],
            "retained_hpadj08_row_stream_sha256": old_stream.hexdigest(),
            "exact_match": True,
        },
        "combined_result": {
            "population": totals["population"],
            "hpadj08_exact_square_survivors": totals["hpadj08_exact_square_survivors"],
            "grf02_additional_rejected_among_hpadj08_survivors": totals["grf02_additional_rejected_among_hpadj08_survivors"],
            "grf02_plus_hpadj08_survivors": totals["grf02_plus_hpadj08_survivors"],
            "strict_gain": totals["grf02_additional_rejected_among_hpadj08_survivors"] > 0,
        },
        "source": {
            "contract_blob_sha1": CONTRACT_BLOB,
            "contract_canonical_sha256": CONTRACT_CANON,
            "worker_blob_sha1": WORKER_BLOB,
            "shards": sorted(shard_canonicals, key=lambda x: tuple(x["b_interval"])),
        },
        "rows": rows,
        "credit_firewall": {
            "main_pruning_credit": False,
            "main_authority_changed": False,
            "full178_complete": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
        },
        "main_accounting": {
            "additive_subtraction_forbidden": True,
            "candidate_is_independent_combined_survivor_bound_only": True,
            "promotion_requires_hostile_audit_and_main_composition": True,
        },
    }
    result["canonical_sha256_without_this_field"] = canon(result)
    Path(ns.output).write_text(json.dumps(result, sort_keys=True, indent=2) + "\n")
    print(json.dumps({
        "baseline_reproduction": result["baseline_reproduction"],
        "combined_result": result["combined_result"],
        "canonical_sha256_without_this_field": result["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
