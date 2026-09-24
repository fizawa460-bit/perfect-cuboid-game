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
SUPPORT_WORKER_BLOB = "37e72735125c232e534d92c6e24c7afc0a0f4f24"
HPADJ22_SOURCE_HEAD = "4bd68dedffa9ca49b0fecc41a89e5e2bc39585a2"
V47_EXACT_HEAD = "620b90d1ca1f5316d55b88b2620f78eeba1949c7"
V47_HELPER_BLOB = "99eef03657b07eb5cf86be8d880050fd8aa2d13b"
V48_TOTAL = 128470212118313474449
V48_COVERED_TOTAL = 37911631052805557219
V48_AGGREGATE_CANON = "362461c281a60c3f7e94753ee4bce49dfd6e76cddb549f9440e5800ab2e052e2"
V48_RUN_ID = 35906475088
LEGACY_INELIGIBLE = {
    (22, 47): {
        "path": "local-support-qbc/row022-b047.json",
        "blob_sha1": "0f161fa0df18966a8bc38f0160edd76f4f9cc1fe",
        "canonical": "2bbc6957864fcb439dc991a26a3ea223d6f3169af7352df8b28966a058a8b47b",
        "worker_blob_sha1": "2c1abfd6d921122d9cf6a67a2f2251b95318e5fd",
        "reason": "legacy carried receipt predates the source-locked current support worker; leave V48 unchanged at this coordinate",
    }
}


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

    req(blob(MANIFEST) == MANIFEST_BLOB, "Generation4 manifest blob drift")
    manifest = json.loads(MANIFEST.read_text())
    req(canon(manifest) == MANIFEST_CANON == manifest["canonical_sha256_without_this_field"], "Generation4 manifest canonical drift")
    req(len(manifest["receipts"]) == 384, "Generation4 coordinate count drift")

    expected = {}
    raw_total = 0
    raw_current_total = 0
    for item in manifest["receipts"]:
        rel = item["path"]
        p = HERE / rel
        req(p.is_file(), "missing raw support receipt " + rel)
        o = json.loads(p.read_text())
        req(canon(o) == item["verified"]["canonical"] == o["canonical_sha256_without_this_field"], "raw support canonical drift " + rel)
        t = o["target"]
        row = int(t["row_index"])
        b0, b1 = map(int, t["b_interval"])
        req(b0 == b1 == int(item["verified"]["b"]), "raw support singleton b drift " + rel)
        key = (row, b0)
        req(key not in expected, "duplicate raw support coordinate " + str(key))
        sl = o["source_locks"]
        req(sl["hpadj22_source_head"] == HPADJ22_SOURCE_HEAD, "raw HPADJ22 source drift " + rel)
        legacy = LEGACY_INELIGIBLE.get(key)
        eligible = legacy is None
        if eligible:
            req(sl["local_worker_blob_sha1"] == SUPPORT_WORKER_BLOB, "raw support worker drift " + rel)
        else:
            req(rel == legacy["path"], "legacy ineligible path drift " + rel)
            req(blob(p) == legacy["blob_sha1"], "legacy ineligible blob drift " + rel)
            req(o["canonical_sha256_without_this_field"] == legacy["canonical"], "legacy ineligible canonical drift " + rel)
            req(sl["local_worker_blob_sha1"] == legacy["worker_blob_sha1"], "legacy ineligible worker drift " + rel)
        req(o["semantics"]["same_population_as_current_hpadj22"] is True, "raw population drift " + rel)
        req(o["semantics"]["same_current_x4_capacity_rule"] is True, "raw x4 capacity drift " + rel)
        current = int(o["result"]["current_row_band_survivors"])
        refined = int(o["result"]["support_qbc_refined_survivors"])
        req(0 <= refined <= current, "raw support count order drift " + rel)
        expected[key] = {
            "path": rel,
            "raw_current": current,
            "raw_full_support": refined,
            "raw_canonical": o["canonical_sha256_without_this_field"],
            "eligible_for_current_worker_replacement": eligible,
        }
        if eligible:
            raw_total += refined
        raw_current_total += current

    files = sorted(args.v48_dir.glob("row*-b*.json"))
    req(len(files) == 384, f"V48 unit receipt count {len(files)} != 384")
    seen = set()
    v48_total_covered = 0
    replacement_total = 0
    strict = []
    unchanged = 0

    for p in files:
        o = json.loads(p.read_text())
        req(canon(o) == o["canonical_sha256_without_this_field"], "V48 unit canonical drift " + p.name)
        req(o["schema"] == "STAGE32_32_01_178_V47_SUPPORT_QBC_INTERSECTION_UNIT_V1", "V48 unit schema drift " + p.name)
        t = o["target"]
        key = (int(t["row_index"]), int(t["b"]))
        req(key in expected and key not in seen, "V48 coordinate drift " + str(key))
        seen.add(key)
        sl = o["source_locks"]
        req(sl["hpadj22_source_head"] == HPADJ22_SOURCE_HEAD, "V48 HPADJ22 source drift " + p.name)
        req(sl["support_qbc_worker_blob_sha1"] == SUPPORT_WORKER_BLOB, "V48 support worker drift " + p.name)
        req(sl["v47_exact_head"] == V47_EXACT_HEAD, "V48 V47 head drift " + p.name)
        req(sl["v47_helper_blob_sha1"] == V47_HELPER_BLOB, "V48 helper drift " + p.name)
        req(o["semantics"]["same_population_v47_replacement"] is True, "V48 population drift " + p.name)

        current = int(o["result"]["v47_support_qbc_joint_survivors"])
        raw_entry = expected[key]
        raw = int(raw_entry["raw_full_support"])
        eligible = bool(raw_entry["eligible_for_current_worker_replacement"])
        replacement = min(current, raw) if eligible else current
        v48_total_covered += current
        replacement_total += replacement
        if replacement < current:
            strict.append({
                "row_index": key[0],
                "b": key[1],
                "v48_current": str(current),
                "raw_full_support_upper_bound": str(raw),
                "replacement_upper_bound": str(replacement),
                "tightening": str(current - replacement),
                "v48_canonical": o["canonical_sha256_without_this_field"],
                "raw_canonical": expected[key]["raw_canonical"],
            })
        else:
            unchanged += 1

    req(seen == set(expected), "V48/raw support coordinate coverage mismatch")
    req(v48_total_covered == V48_COVERED_TOTAL, f"V48 covered aggregate drift {v48_total_covered}")
    tightening = v48_total_covered - replacement_total
    candidate = V48_TOTAL - v48_total_covered + replacement_total
    req(candidate == V48_TOTAL - tightening, "candidate arithmetic drift")
    req(tightening >= 0 and candidate <= V48_TOTAL, "replacement failed to improve upper bound")

    strict.sort(key=lambda x: int(x["tightening"]), reverse=True)
    out = {
        "schema": "STAGE32_32_01_178_V48_FULL_SUPPORT_384_MIN_BOUND_V1",
        "status": "EXACT_SOURCE_MATCHED_384_COORDINATE_UPPER_BOUND_CANDIDATE__ZERO_MAIN_CREDIT",
        "authority": {
            "v48_certified_upper_bound": str(V48_TOTAL),
            "v48_covered_384_total": str(V48_COVERED_TOTAL),
            "v48_aggregate_canonical_sha256": V48_AGGREGATE_CANON,
            "v48_workflow_run_id": V48_RUN_ID,
        },
        "source_locks": {
            "generation4_manifest_blob_sha1": MANIFEST_BLOB,
            "generation4_manifest_canonical_sha256": MANIFEST_CANON,
            "support_qbc_worker_blob_sha1": SUPPORT_WORKER_BLOB,
            "hpadj22_source_head": HPADJ22_SOURCE_HEAD,
            "v47_exact_head": V47_EXACT_HEAD,
            "v47_helper_blob_sha1": V47_HELPER_BLOB,
        },
        "coverage": {
            "expected_coordinates": 384,
            "v48_receipts": 384,
            "raw_support_receipts": 384,
            "eligible_current_worker_coordinates": 384 - len(LEGACY_INELIGIBLE),
            "source_ineligible_coordinates": len(LEGACY_INELIGIBLE),
            "strict_replacement_coordinates": len(strict),
            "unchanged_coordinates": unchanged,
            "gaps": 0,
            "overlaps": 0,
        },
        "result": {
            "covered_v48_current": str(v48_total_covered),
            "covered_raw_full_support_sum_over_eligible_coordinates": str(raw_total),
            "covered_min_replacement_sum": str(replacement_total),
            "certified_tightening_vs_v48": str(tightening),
            "candidate_global_upper_bound_if_promoted": str(candidate),
        },
        "composition": {
            "rule": "PER_COORDINATE_MIN_OF_CERTIFIED_UPPER_BOUNDS_FOR_STRONGER_SAME_POPULATION_INTERSECTION",
            "mathematical_basis": "For each coordinate, the desired V47 x full-support survivor set is a subset of both the current V48 support-interval survivor set and the raw full-support survivor set, hence its cardinality is <= min of the two counts.",
            "additive_subtraction": False,
            "statistical_independence": False,
            "exact_intersection_identity_set_claimed": False,
            "uncovered_v48_population_unchanged": True,
        },
        "source_ineligible_coordinates": [
            {"row_index": k[0], "b": k[1], **v} for k, v in sorted(LEGACY_INELIGIBLE.items())
        ],
        "strict_coordinates": strict,
        "firewalls": {
            "main_credit_changed": False,
            "full178_numerical_census_changed": False,
            "effectivity_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "theorem_credit": False,
            "endpoint_credit": False,
            "stage32_closed": False,
            "merge": False,
            "hostile_audit_required_before_promotion": True,
        },
    }
    out["canonical_sha256_without_this_field"] = canon(out)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, sort_keys=True, indent=2) + "\n")
    print("V48_FULL_SUPPORT_384_MIN_BOUND=" + json.dumps({
        "strict_coordinates": len(strict),
        "covered_current": str(v48_total_covered),
        "replacement_sum": str(replacement_total),
        "tightening": str(tightening),
        "candidate_global": str(candidate),
        "top5": strict[:5],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
