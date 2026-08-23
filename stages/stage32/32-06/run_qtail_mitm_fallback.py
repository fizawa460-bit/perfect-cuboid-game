#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import itertools
import json
import pathlib
import sys
from typing import Any

import numpy as np

HERE = pathlib.Path(__file__).resolve().parent
STAGE32_05 = HERE.parent / "32-05"
sys.path.insert(0, str(STAGE32_05))

import cap_certificate  # type: ignore
import run_exact_mitm_closure as base  # type: ignore

PRIMARY_SCHEMA = "STAGE32_EXACT_MITM_DEGREE4_CLOSURE_V1"
SCHEMA = "STAGE32_D4_QTAIL_MITM_FALLBACK_V1"
DEGREE = 4
GENUS = 0
NORMAL_CAP = 2
EXCEPTIONAL_CAP = 1
EXPECTED_CAP_SHA = "75224aee543dcd4a56e814503765d1e1e69514b237fb900688243546ea6b4d03"


def canonical_sha256(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def mask_vector(mask: int) -> list[int]:
    return [(mask >> j) & 1 for j in range(48)]


def state_signature(matrix: np.ndarray, columns: list[int], values: tuple[int, ...]) -> bytes:
    if not columns:
        return bytes(64)
    vector = np.array(values, dtype=np.int64)
    return ((matrix[:, columns] @ vector) % 8).astype(np.uint8).tobytes()


def exact_full_check(
    transform: dict[str, Any], selected_values: list[int], e: int, a: int
) -> tuple[bool, str, list[int] | None]:
    selected = np.array(selected_values, dtype=object)
    inv = transform["inv"].astype(object)
    pair = transform["pair"].astype(object)
    hform = transform["h"].astype(object)
    gram = transform["gram"].astype(object)

    image = inv @ selected
    if any(int(value) % 8 for value in image):
        return False, "lattice_congruence", None
    numerator = pair @ selected
    if any(int(value) % 8 for value in numerator):
        return False, "pairing_divisibility", None
    intersections = [int(value) // 8 for value in numerator]
    if any(value < 0 or value > NORMAL_CAP for value in intersections[:92]):
        return False, "normal_cap", None
    if any(value < 0 or value > EXCEPTIONAL_CAP for value in intersections[92:]):
        return False, "exceptional_cap", None
    if sum(intersections[92:]) != e:
        return False, "exceptional_mass", None
    if sum(intersections[:46]) != a:
        return False, "curve_group_mass", None
    if int(hform @ selected) != 8 * DEGREE:
        return False, "degree", None
    if sum(intersections[:92]) + 5 * sum(intersections[92:]) != 19 * DEGREE:
        return False, "weighted_identity", None
    square = int(selected @ gram @ selected)
    if square < 64 * (-DEGREE - 2 + 2 * GENUS):
        return False, "adjunction", None
    return True, "survivor", intersections


def solve_unknown_candidate(
    transform: dict[str, Any], candidate: dict[str, Any], candidate_index: int, e: int, a: int
) -> dict[str, Any]:
    inv_mod8 = (transform["inv"] % 8).astype(np.int64)
    exceptional = mask_vector(int(candidate["exceptional_mask"]))
    qhead_sum = int(candidate["qhead_sum"])

    left_cols = list(range(52, 58))
    right_cols = list(range(58, 64))
    left_map: dict[bytes, list[tuple[int, ...]]] = {}
    for values in itertools.product(range(NORMAL_CAP + 1), repeat=6):
        sig = state_signature(inv_mod8, left_cols, values)
        left_map.setdefault(sig, []).append(values)
    right_states = [
        (values, state_signature(inv_mod8, right_cols, values))
        for values in itertools.product(range(NORMAL_CAP + 1), repeat=6)
    ]
    assert sum(map(len, left_map.values())) == 3**6
    assert len(right_states) == 3**6

    qhead_assignments = [
        values
        for values in itertools.product(range(NORMAL_CAP + 1), repeat=4)
        if sum(values) == qhead_sum
    ]
    transcript = hashlib.sha256()
    congruence_join_count = 0
    exact_checked_count = 0
    rejection_counts: dict[str, int] = {}
    survivors: list[dict[str, Any]] = []

    for qhead in qhead_assignments:
        prefix = np.array(exceptional + list(qhead), dtype=np.int64)
        target = (-(inv_mod8[:, :52] @ prefix)) % 8
        for right_values, right_sig_bytes in right_states:
            right_sig = np.frombuffer(right_sig_bytes, dtype=np.uint8).astype(np.int64)
            need = ((target - right_sig) % 8).astype(np.uint8).tobytes()
            left_values_list = left_map.get(need)
            if not left_values_list:
                continue
            for left_values in left_values_list:
                congruence_join_count += 1
                qtail = list(left_values) + list(right_values)
                selected = exceptional + list(qhead) + qtail
                ok, reason, intersections = exact_full_check(transform, selected, e, a)
                exact_checked_count += 1
                rejection_counts[reason] = rejection_counts.get(reason, 0) + 1
                transcript.update(
                    (json.dumps([qhead, qtail, reason], separators=(",", ":")) + "\n").encode()
                )
                if ok:
                    survivors.append(
                        {
                            "selected_coordinates": selected,
                            "intersection_vector_sha256": canonical_sha256(intersections),
                        }
                    )

    deterministic = {
        "candidate_index": candidate_index,
        "exceptional_mask_hex": hex(int(candidate["exceptional_mask"])),
        "qhead_sum": qhead_sum,
        "qhead_assignment_count": len(qhead_assignments),
        "qtail_left_state_count": 3**6,
        "qtail_right_state_count": 3**6,
        "qtail_full_state_space_per_qhead": 3**12,
        "congruence_join_count": congruence_join_count,
        "exact_checked_count": exact_checked_count,
        "rejection_counts": rejection_counts,
        "survivor_count": len(survivors),
        "survivors": survivors,
        "enumeration_transcript_sha256": transcript.hexdigest(),
        "complete": True,
        "result": "sat" if survivors else "unsat_exhaustive_qtail_mitm",
    }
    deterministic["fallback_certificate_sha256"] = canonical_sha256(deterministic)
    return deterministic


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--core", type=pathlib.Path, required=True)
    parser.add_argument("--cap-certificate", type=pathlib.Path, required=True)
    parser.add_argument("--primary-manifest", type=pathlib.Path, required=True)
    parser.add_argument("--candidates", type=pathlib.Path, required=True)
    parser.add_argument("--output", type=pathlib.Path, required=True)
    args = parser.parse_args()

    primary = json.loads(args.primary_manifest.read_text())
    assert primary["schema"] == PRIMARY_SCHEMA
    assert primary["parameters"]["degree"] == DEGREE
    assert primary["parameters"]["genus"] == GENUS
    assert primary["survivor_count"] == 0
    e = int(primary["parameters"]["exceptional_mass"])
    a = int(primary["parameters"]["curve_group_mass"])
    candidates = json.loads(args.candidates.read_text())
    assert len(candidates) == primary["candidate_count"]

    core, _, cap_summary = cap_certificate.load_and_verify(args.core, args.cap_certificate)
    assert cap_summary["certificate_canonical_sha256"] == EXPECTED_CAP_SHA
    transform = base.build_transform(core)

    unknown_indices = [
        int(row["candidate_index"])
        for row in primary["solver_rows"]
        if row["solver_result"] == "unknown"
    ]
    assert unknown_indices
    assert all(
        row["solver_result"] in {"unsat", "unknown"} for row in primary["solver_rows"]
    )

    fallback_rows = [
        solve_unknown_candidate(transform, candidates[index], index, e, a)
        for index in unknown_indices
    ]
    all_fallback_unsat = all(row["result"] == "unsat_exhaustive_qtail_mitm" for row in fallback_rows)
    all_primary_resolved = all(
        row["solver_result"] == "unsat" or int(row["candidate_index"]) in unknown_indices
        for row in primary["solver_rows"]
    )
    closed = bool(all_primary_resolved and all_fallback_unsat)

    report = {
        "schema": SCHEMA,
        "algorithm_id": "D4_QTAIL_6PLUS6_MOD8_MITM_EXACT_ENUM_V1",
        "parameters": {"degree": DEGREE, "genus": GENUS, "exceptional_mass": e, "curve_group_mass": a},
        "primary_candidate_count": len(candidates),
        "primary_unsat_count": sum(row["solver_result"] == "unsat" for row in primary["solver_rows"]),
        "primary_unknown_count": len(unknown_indices),
        "fallback_rows": fallback_rows,
        "parent_exactly_closed": closed,
        "survivor_count": sum(row["survivor_count"] for row in fallback_rows),
        "exact_arithmetic_final_checks": True,
        "floating_point_credit": False,
        "theorem_credit": False,
        "audit_status": "PENDING",
        "receiver_credit": False,
        "low_degree_prefix_complete": False,
        "full_d176_d192_numerical_orbit_census": False,
        "R29_LG2": "NOT_DISCHARGED",
        "R29_LG2_EFF": "NOT_DISCHARGED",
        "R29_LG2_MB": "NOT_DISCHARGED",
        "G10_LOWGENUS_PICARD": "AMBER",
    }
    report["canonical_sha256_without_this_field"] = canonical_sha256(report)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({"unknown": len(unknown_indices), "closed": closed, "survivors": report["survivor_count"]}))
    if not closed:
        raise SystemExit("q-tail MITM fallback did not close all primary UNKNOWN candidates")


if __name__ == "__main__":
    main()
