#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

PREFIX_JSON_SHA256 = "42336e170a2b7fa34372c5efe194c8c8d66e6297e22d1ae79963146bd6858442"
PREFIX_CANONICAL = "cc17cb1405095d7f9d855a21043388f4830ba611d69dc22af15b88c75287ef0c"
PREFIX_STREAM = "f21ac9d28ec94645b1af2c7f1b5ca431e790d6c94a4bd12144f0c2bd895c236b"
SUFFIX_JSON_SHA256 = "b9f9c9998293e820acc08f366904510f25e0a35cb698ae4f21a99361bde32aff"
SUFFIX_CANONICAL = "6188b14c13ad49bf62e1eaee1fb4723d7d4fbc03ab680d53f65666757d7e6ff3"
SUFFIX_STREAM = "ddb01880a4aac9710e7d0063509a3fbffdffe8857ca86f6c6d0a17ad0e7d23e7"
COMBINED_MANIFEST = "fd5261bfea0384bce540bba039f755adfada1623b1aa21e686c52be470af3958"
EXPECTED_TRIPLES = 3234
EXPECTED_FEASIBLE = 124856
EXPECTED_BASELINE = 151998
EXPECTED_PRUNED = 27142
SCHEMA = "STAGE32_21BB_EXACT_R51_INTERVAL_FORMULA_COMPRESSION_V1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def raw_sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_claimed(path: Path, raw_expected: str, canonical_expected: str) -> dict:
    if raw_sha(path) != raw_expected:
        raise ValueError(f"raw SHA regression: {path}")
    raw = json.loads(path.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if claimed != canonical_expected or csha(raw) != claimed:
        raise ValueError(f"canonical regression: {path}")
    raw["canonical_sha256_without_this_field"] = claimed
    return raw


def prism_triples():
    for r50 in range(69, 80):
        for r55 in range(-60, -49):
            if r55 > r50 - 129:
                continue
            for r27 in range(-96, -47):
                yield [r50, r55, r27]


def lower_formula(r50: int, r55: int, r27: int) -> int:
    return max(r27 - 103, -176 - ((r50 - r55 - 129) // 4))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--prefix", type=Path, required=True)
    ap.add_argument("--suffix", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    prefix = load_claimed(args.prefix, PREFIX_JSON_SHA256, PREFIX_CANONICAL)
    suffix = load_claimed(args.suffix, SUFFIX_JSON_SHA256, SUFFIX_CANONICAL)

    pcov = prefix["coverage"]
    pres = prefix["result"]
    spart = suffix["partition"]
    sres = suffix["result"]

    if pcov["processed_triples"] != 2709 or pcov["complete"]:
        raise ValueError("prefix coverage regression")
    if pres["interval_stream_sha256"] != PREFIX_STREAM:
        raise ValueError("prefix interval stream regression")
    if pres["qflra_unknown_triple_count"] != 0 or pres["integer_empty_triple_count"] != 0 or pres["source_replay_unsat_triple_count"] != 0:
        raise ValueError("prefix unresolved/regression state")
    if pres["rationally_feasible_integer_r51_index_count"] != 104607:
        raise ValueError("prefix feasible count regression")

    if not spart["complete_suffix"] or not spart["complete_full_partition"]:
        raise ValueError("suffix partition incomplete")
    if spart["suffix_expected_triples"] != 525 or spart["suffix_processed_triples"] != 525:
        raise ValueError("suffix coverage regression")
    if sres["suffix_interval_stream_sha256"] != SUFFIX_STREAM:
        raise ValueError("suffix stream regression")
    if sres["combined_two_stream_manifest_sha256"] != COMBINED_MANIFEST:
        raise ValueError("combined manifest regression")
    if sres["suffix_qflra_unknown_triple_count"] != 0 or sres["suffix_integer_empty_triple_count"] != 0 or sres["suffix_source_replay_unsat_count"] != 0:
        raise ValueError("suffix unresolved/regression state")

    records = pres["interval_records"] + sres["suffix_interval_records"]
    expected_triples = list(prism_triples())
    if len(records) != EXPECTED_TRIPLES or len(expected_triples) != EXPECTED_TRIPLES:
        raise ValueError("full interval record count regression")

    formula_failures = []
    feasible = 0
    width_min = None
    width_max = None
    band_counts = {"0": 0, "1": 0, "2": 0}
    for idx, (record, triple) in enumerate(zip(records, expected_triples)):
        r50, r55, r27, lo, hi = map(int, record)
        if [r50, r55, r27] != triple:
            raise ValueError(f"partition ordering regression at {idx}")
        expected_lo = lower_formula(r50, r55, r27)
        expected_hi = -132
        if lo != expected_lo or hi != expected_hi:
            formula_failures.append({"index": idx, "record": record, "expected": [expected_lo, expected_hi]})
        width = hi - lo + 1
        feasible += width
        width_min = width if width_min is None else min(width_min, width)
        width_max = width if width_max is None else max(width_max, width)
        band = (r50 - r55 - 129) // 4
        if str(band) not in band_counts:
            raise ValueError(f"unexpected plateau band {band}")
        band_counts[str(band)] += 1

    if formula_failures:
        raise ValueError(f"formula replay failures: {formula_failures[:3]}")
    if feasible != EXPECTED_FEASIBLE:
        raise ValueError(f"feasible count regression: {feasible}")
    pruned = EXPECTED_BASELINE - feasible
    if pruned != EXPECTED_PRUNED:
        raise ValueError(f"pruned count regression: {pruned}")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21bb",
        "mode": "EXACT_REPLAY_COMPRESSION_OF_COMPLETE_21BA_R51_INTERVAL_STREAMS",
        "sources": {
            "prefix_run_id": 33353157553,
            "prefix_artifact_id": 9744385933,
            "prefix_json_sha256": PREFIX_JSON_SHA256,
            "prefix_canonical_sha256": PREFIX_CANONICAL,
            "prefix_interval_stream_sha256": PREFIX_STREAM,
            "suffix_run_id": 33354345083,
            "suffix_artifact_id": 9744671392,
            "suffix_json_sha256": SUFFIX_JSON_SHA256,
            "suffix_canonical_sha256": SUFFIX_CANONICAL,
            "suffix_interval_stream_sha256": SUFFIX_STREAM,
            "combined_two_stream_manifest_sha256": COMBINED_MANIFEST
        },
        "coverage": {
            "triple_count": EXPECTED_TRIPLES,
            "formula_failures": 0,
            "qflra_unknown_triples_in_sources": 0,
            "integer_empty_triples_in_sources": 0,
            "source_replay_unsat_triples": 0
        },
        "compressed_region": {
            "base_prism": [
                "69 <= r50 <= 79",
                "-60 <= r55 <= -50",
                "r55 <= r50 - 129",
                "-96 <= r27 <= -48"
            ],
            "r51_upper": -132,
            "r51_lower_formula": "max(r27 - 103, -176 - floor((r50-r55-129)/4))",
            "equivalent_plateau_bands": [
                {"difference_range": [129, 132], "plateau": -176},
                {"difference_range": [133, 136], "plateau": -177},
                {"difference_range": [137, 139], "plateau": -178}
            ],
            "plateau_band_triple_counts": band_counts,
            "integer_r51_width_min": width_min,
            "integer_r51_width_max": width_max,
            "rationally_feasible_integer_r51_index_count": feasible,
            "baseline_3234_x_47_index_count": EXPECTED_BASELINE,
            "exact_rationally_pruned_integer_r51_index_count": pruned
        },
        "interpretation": {
            "raw_3234_interval_list_not_needed_for_live_controller": True,
            "surviving_r51_integer_index_is_not_integer_sat": True,
            "fixed_projection_remains_unknown": True,
            "fixed_projection_unsat_is_not_slice_unsat": True,
            "representative_sample_only": True,
            "not_full178_numerical_credit": True
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "integer_solver_used": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False
        }
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"status": "PASS_EXACT_COMPRESSION", "canonical": payload["canonical_sha256_without_this_field"], "feasible_indices": feasible, "pruned_indices": pruned, "width_min": width_min, "width_max": width_max}), flush=True)


if __name__ == "__main__":
    main()
