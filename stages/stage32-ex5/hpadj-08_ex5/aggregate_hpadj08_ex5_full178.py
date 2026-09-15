#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PLANNED = ((0,11),(12,23),(24,35),(36,47),(48,59),(60,71),(72,83),(84,96))
EXPECTED_ROWS = 178


def req(v: bool, msg: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + msg)


def canon(obj: dict) -> str:
    cp = dict(obj)
    cp.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(json.dumps(cp, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--input-dir", action="append", required=True)
    ap.add_argument("--output", required=True)
    ns = ap.parse_args()

    found: dict[tuple[int,int], dict] = {}
    for raw_dir in ns.input_dir:
        root = Path(raw_dir)
        if not root.exists():
            continue
        for path in sorted(root.rglob("*.json")):
            try:
                obj = json.loads(path.read_text(encoding="utf-8"))
            except Exception:
                continue
            if obj.get("schema") != "STAGE32EX5_HPADJ08_FULL178_B_SHARD_RESULT_V1":
                continue
            interval = tuple(obj.get("b_interval", []))
            req(interval in PLANNED, f"unexpected shard interval {interval}")
            req(interval not in found, f"duplicate shard interval {interval}")
            req(obj.get("route_id") == "HPADJ-08_ex5", f"route drift {interval}")
            req(obj.get("q_cap") == 4992, f"q cap drift {interval}")
            req(obj.get("row_count") == EXPECTED_ROWS, f"row count drift {interval}")
            req(obj.get("canonical_sha256_without_this_field") == canon(obj), f"canonical drift {interval}")
            fw = obj.get("firewalls", {})
            req(fw.get("stage32_main_pruning_credit") is False, f"MAIN firewall {interval}")
            req(fw.get("current_main_incremental_credit") is False, f"incremental firewall {interval}")
            req(fw.get("full178_complete") is False, f"premature FULL178 credit {interval}")
            req(fw.get("merge_authorized") is False, f"merge firewall {interval}")
            found[interval] = obj

    req(set(found) == set(PLANNED), f"coverage mismatch found={sorted(found)}")

    row_acc: dict[tuple[int,int], dict[str,int]] = {}
    old_total = 0
    exact_total = 0
    shard_canonicals = []
    for interval in PLANNED:
        obj = found[interval]
        old_total += int(obj["old_group_cauchy_candidate_rejected_terminals"])
        exact_total += int(obj["stored_exact_square_candidate_rejected_terminals"])
        shard_canonicals.append(obj["canonical_sha256_without_this_field"])
        for rec in obj["records"]:
            key = (int(rec["g"]), int(rec["d"]))
            slot = row_acc.setdefault(key, {"old": 0, "exact": 0})
            slot["old"] += int(rec["old_group_cauchy_candidate_rejected_terminals"])
            slot["exact"] += int(rec["stored_exact_square_candidate_rejected_terminals"])

    req(len(row_acc) == EXPECTED_ROWS, "aggregate FULL178 row count")
    records = []
    for (g,d), val in sorted(row_acc.items()):
        req(val["exact"] >= val["old"], f"negative exact-square gain {(g,d)}")
        records.append({
            "g": g,
            "d": d,
            "old_group_cauchy_candidate_rejected_terminals": val["old"],
            "stored_exact_square_candidate_rejected_terminals": val["exact"],
            "incremental_candidate_over_group_cauchy": val["exact"] - val["old"],
        })

    stream = hashlib.sha256()
    for rec in records:
        stream.update(json.dumps(rec, sort_keys=True, separators=(",", ":")).encode() + b"\n")

    out = {
        "schema": "STAGE32EX5_HPADJ08_FULL178_AGGREGATE_CANDIDATE_V1",
        "route_id": "HPADJ-08_ex5",
        "coverage": {"planned_shards": [list(x) for x in PLANNED], "complete": True, "row_count": EXPECTED_ROWS},
        "old_group_cauchy_candidate_rejected_terminals": old_total,
        "stored_exact_square_candidate_rejected_terminals": exact_total,
        "incremental_candidate_over_group_cauchy": exact_total - old_total,
        "row_stream_sha256": stream.hexdigest(),
        "shard_canonicals": shard_canonicals,
        "records": records,
        "firewalls": {
            "stage32_main_pruning_credit": False,
            "current_main_incremental_credit": False,
            "full178_candidate_only": True,
            "full178_complete": False,
            "theorem_credit": False,
            "merge_authorized": False,
        },
    }
    req(exact_total >= old_total, "aggregate exact-square gain")
    out["canonical_sha256_without_this_field"] = canon(out)
    Path(ns.output).write_text(json.dumps(out, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({
        "old": old_total,
        "exact": exact_total,
        "incremental": exact_total - old_total,
        "row_stream_sha256": out["row_stream_sha256"],
        "canonical": out["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
