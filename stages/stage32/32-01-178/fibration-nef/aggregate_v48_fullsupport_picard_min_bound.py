#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

HERE = Path(__file__).resolve().parent
MANIFEST = HERE / "local-support-qbc/GENERATION4-COMPLETE.json"
MANIFEST_BLOB = "a917f6a98e8f4db57d0ada5193fe263f52162732"
MANIFEST_CANON = "3f1ebc76ef519949ef9d5c497a363f216159387d6857c081d7c1867319e3b242"

V47_EXACT_HEAD = "620b90d1ca1f5316d55b88b2620f78eeba1949c7"
V47_HELPER_BLOB = "99eef03657b07eb5cf86be8d880050fd8aa2d13b"
SUPPORT_WORKER_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
HPADJ22_SOURCE_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"

V47_TOTAL = 128645575147764659235
V48_TOTAL = 128470212118313474449
EXPECTED_COVERED_V47 = 38086994082256742005
EXPECTED_COVERED_V48 = 37911631052805557219
EXPECTED_V48_SAVING = 175363029451184786


def req(v: bool, m: str) -> None:
    if not v:
        raise SystemExit("FAIL: " + m)


def blob(p: Path) -> str:
    raw = p.read_bytes()
    return hashlib.sha1(b"blob " + str(len(raw)).encode() + b"\0" + raw).hexdigest()


def canon(o: dict) -> str:
    x = dict(o)
    x.pop("canonical_sha256_without_this_field", None)
    return hashlib.sha256(
        json.dumps(x, sort_keys=True, separators=(",", ":"), ensure_ascii=False).encode()
    ).hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--v48-dir", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    req(MANIFEST.is_file() and blob(MANIFEST) == MANIFEST_BLOB, "Generation4 manifest blob drift")
    man = json.loads(MANIFEST.read_text())
    req(canon(man) == MANIFEST_CANON == man["canonical_sha256_without_this_field"], "Generation4 manifest canonical drift")
    req(len(man["receipts"]) == 384, "Generation4 coordinate count drift")

    expected = {}
    for item in man["receipts"]:
        v = item["verified"]
        key = (int(v["row_index"]), int(v["b"]))
        req(key not in expected, f"duplicate Generation4 coordinate {key}")
        req(v["status"] == "PASS", f"non-PASS Generation4 coordinate {key}")
        expected[key] = {
            "raw_current": int(v["current"]),
            "raw_full_support": int(v["refined"]),
            "raw_saving": int(v["saving"]),
            "canonical": v["canonical"],
            "path": item["path"],
        }
    req(len(expected) == 384, "Generation4 unique coordinate count drift")

    files = sorted(args.v48_dir.glob("row*-b*.json"))
    req(len(files) == 384, f"V48 receipt count {len(files)} != 384")

    seen = set()
    covered_v47 = 0
    covered_v48 = 0
    covered_full_support = 0
    strict_coords = 0
    equal_coords = 0
    incremental = 0
    stream = hashlib.sha256()
    coordinate_rows = []

    for p in files:
        o = json.loads(p.read_text())
        req(canon(o) == o["canonical_sha256_without_this_field"], f"V48 canonical drift {p.name}")
        req(o["schema"] == "STAGE32_32_01_178_V47_SUPPORT_QBC_INTERSECTION_UNIT_V1", f"V48 schema drift {p.name}")
        req(o["status"] == "EXACT_UNIT_COMPLETE_ZERO_MAIN_CREDIT", f"V48 status drift {p.name}")

        t = o["target"]
        key = (int(t["row_index"]), int(t["b"]))
        req(key in expected and key not in seen, f"unexpected/duplicate V48 coordinate {key}")
        seen.add(key)

        sl = o["source_locks"]
        req(sl["v47_exact_head"] == V47_EXACT_HEAD, f"V47 head drift {key}")
        req(sl["v47_helper_blob_sha1"] == V47_HELPER_BLOB, f"V47 helper drift {key}")
        req(sl["support_qbc_worker_blob_sha1"] == SUPPORT_WORKER_BLOB, f"support worker drift {key}")
        req(sl["hpadj22_source_head"] == HPADJ22_SOURCE_HEAD, f"HPADJ22 source drift {key}")

        r = o["result"]
        v47 = int(r["v47_joint_survivors"])
        v48 = int(r["v47_support_qbc_joint_survivors"])
        req(int(r["exact_incremental_saving_vs_v47"]) == v47 - v48 >= 0, f"V48 unit arithmetic drift {key}")

        raw = expected[key]
        req(raw["raw_current"] >= raw["raw_full_support"] >= 0, f"raw receipt arithmetic drift {key}")
        req(raw["raw_saving"] == raw["raw_current"] - raw["raw_full_support"], f"raw saving drift {key}")

        # Uniform dominance contract:
        # V48 and the retained raw support worker use the same support_t_interval,
        # qA/qBC population, x4 capacity rule and eligible-e multiplicities.
        # The raw full-support qcut additionally subtracts the nonnegative retained
        # Picard parity penalty p0/2+p1/10 from the same radius budget.
        # Therefore its coordinate upper bound must be <= the V48 coordinate count.
        full_support = raw["raw_full_support"]
        req(full_support <= v48, f"full-support bound failed to dominate V48 {key}: {full_support}>{v48}")

        delta = v48 - full_support
        strict_coords += int(delta > 0)
        equal_coords += int(delta == 0)
        incremental += delta
        covered_v47 += v47
        covered_v48 += v48
        covered_full_support += full_support
        stream.update((f"{key}:{o['canonical_sha256_without_this_field']}:{raw['canonical']}\n").encode())
        coordinate_rows.append({
            "row_index": key[0],
            "b": key[1],
            "v48": str(v48),
            "full_support": str(full_support),
            "incremental": str(delta),
        })

    req(seen == set(expected), "V48/Generation4 coordinate coverage mismatch")
    req(covered_v47 == EXPECTED_COVERED_V47, f"covered V47 total drift {covered_v47}")
    req(covered_v48 == EXPECTED_COVERED_V48, f"covered V48 total drift {covered_v48}")
    req(covered_v47 - covered_v48 == EXPECTED_V48_SAVING, "V48 covered saving drift")
    req(incremental == covered_v48 - covered_full_support >= 0, "full-support incremental arithmetic drift")

    candidate = V48_TOTAL - covered_v48 + covered_full_support
    req(candidate == V48_TOTAL - incremental, "candidate replacement arithmetic drift")
    req(candidate <= V48_TOTAL, "candidate bound weakened V48")

    coordinate_rows.sort(key=lambda x: int(x["incremental"]), reverse=True)
    out = {
        "schema": "STAGE32_32_01_178_V48_FULLSUPPORT_PICARD_MIN_BOUND_AGGREGATE_V1",
        "status": "EXACT_384_COORDINATE_SAME_POPULATION_UPPER_BOUND_REPLACEMENT__ZERO_MAIN_CREDIT",
        "coverage": {
            "expected_coordinates": 384,
            "completed_coordinates": 384,
            "strict_coordinates": strict_coords,
            "equal_coordinates": equal_coords,
            "uncovered_v48_population_unchanged": True,
        },
        "source_locks": {
            "generation4_manifest_blob_sha1": MANIFEST_BLOB,
            "generation4_manifest_canonical_sha256": MANIFEST_CANON,
            "v47_exact_head": V47_EXACT_HEAD,
            "v47_helper_blob_sha1": V47_HELPER_BLOB,
            "support_qbc_worker_blob_sha1": SUPPORT_WORKER_BLOB,
            "hpadj22_source_head": HPADJ22_SOURCE_HEAD,
        },
        "result": {
            "v47_total_upper_bound": str(V47_TOTAL),
            "v48_total_upper_bound": str(V48_TOTAL),
            "covered_v47_joint_survivors": str(covered_v47),
            "covered_v48_joint_survivors": str(covered_v48),
            "covered_full_support_picard_upper_bound": str(covered_full_support),
            "exact_incremental_tightening_vs_v48": str(incremental),
            "same_population_replacement_upper_bound": str(candidate),
        },
        "accounting": {
            "composition": "SAME_POPULATION_MINIMUM_OF_CERTIFIED_COORDINATE_UPPER_BOUNDS__NO_ADDITIVE_SUBTRACTION",
            "raw_generation4_saving_added_to_v48": False,
            "statistical_independence": False,
            "double_charge": False,
            "replacement_formula": "V48_total - covered_V48 + covered_full_support_picard",
        },
        "top_incremental_coordinates": coordinate_rows[:24],
        "coordinate_stream_sha256": stream.hexdigest(),
        "firewalls": {
            "main_credit_changed": False,
            "full178_numerical_census_changed": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge_authorized": False,
            "hostile_audit_required": True,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print("V48_FULLSUPPORT_PICARD_MIN_AGGREGATE=" + json.dumps(out["result"], sort_keys=True))
    print("V48_FULLSUPPORT_PICARD_MIN_STRICT_COORDS=" + str(strict_coords))
    print("V48_FULLSUPPORT_PICARD_MIN_TOP24=" + json.dumps(out["top_incremental_coordinates"], sort_keys=True))


if __name__ == "__main__":
    main()
