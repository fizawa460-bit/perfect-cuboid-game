#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_orbit_sum_integral_coordinate_bound import (
    DirectPicardOrbitSumKKTIntegralCoordinateBound,
)

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PRIOR_SLICES = 2018569
EXPECTED_KKT_SURVIVORS = 679337
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_ORBIT_KKT_INTEGRAL_COORDINATE_CENSUS_V1"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_module_payload(path: pathlib.Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=pathlib.Path, required=True)
    ap.add_argument("--retained", type=pathlib.Path, required=True)
    ap.add_argument("--marking", type=pathlib.Path, required=True)
    ap.add_argument("--output", type=pathlib.Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    assert csha(manifest) == claimed == EXPECTED_MANIFEST_SHA256

    bundle = load_module_payload(args.retained, "stage32_kkt_int_picard")
    marking = load_module_payload(args.marking, "stage32_kkt_int_marking")
    model = DirectPicardOrbitSumKKTIntegralCoordinateBound.from_retained(marking, bundle)
    kkt = model.kkt
    bound = kkt.bound
    bridge = bound.bridge

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    prior = 0
    kkt_survivors = 0
    integral_pruned = 0
    survivors = 0
    zero_rows = 0
    zero_e_strata = 0
    candidate_prior = [0] * len(kkt.candidates)
    candidate_pruned = [0] * len(kkt.candidates)
    row_summaries = []

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_kkt = 0
        row_pruned = 0
        row_survivors = 0
        row_zero_e = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            e_kkt = 0
            e_survivors = 0
            if interval is None:
                continue
            lo, hi = interval
            for a in range(lo, hi + 1):
                if not bridge.target_in_image(d, e, a):
                    continue
                prior += 1
                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                candidate = kkt.solve_candidate(d, e, a)
                if candidate is None:
                    continue
                if not candidate.can_reach_selfsq(d, e, a, lower):
                    continue

                kkt_survivors += 1
                row_kkt += 1
                e_kkt += 1
                candidate_prior[candidate.candidate_id] += 1
                penalty = model.penalty_for(candidate.candidate_id)
                if not penalty.can_reach_after_coordinate_integrality_lb(
                    candidate, d, e, a, lower
                ):
                    integral_pruned += 1
                    row_pruned += 1
                    candidate_pruned[candidate.candidate_id] += 1
                    continue
                survivors += 1
                row_survivors += 1
                e_survivors += 1

            if e_kkt > 0 and e_survivors == 0:
                zero_e_strata += 1
                row_zero_e += 1

        if row_kkt > 0 and row_survivors == 0:
            zero_rows += 1
        row_summaries.append({
            "row_id": row_id,
            "orbit_kkt_surviving_slices": row_kkt,
            "coordinate_integrality_pruned_slices": row_pruned,
            "coordinate_integrality_surviving_slices": row_survivors,
            "zero_e_strata_after_coordinate_integrality": row_zero_e,
        })

    assert prior == EXPECTED_PRIOR_SLICES, prior
    assert kkt_survivors == EXPECTED_KKT_SURVIVORS, kkt_survivors
    assert integral_pruned + survivors == kkt_survivors

    usage = []
    for candidate in kkt.candidates:
        n = candidate_prior[candidate.candidate_id]
        if not n:
            continue
        p = candidate_pruned[candidate.candidate_id]
        usage.append({
            "candidate_id": candidate.candidate_id,
            "active_orbit_ids": list(candidate.active_orbit_ids),
            "kkt_surviving_slices": n,
            "coordinate_integrality_pruned_slices": p,
            "coordinate_integrality_surviving_slices": n - p,
        })
    usage.sort(key=lambda r: (-r["kkt_surviving_slices"], r["candidate_id"]))

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "FULL178_EXACT_ALL140_CONTINUOUS_KKT_PLUS_SAFE_INTEGER_COORDINATE_LOSS",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "integral_coordinate_bound_sha256": model.certificate[
            "canonical_sha256_without_this_field"
        ],
        "row_count": len(rows),
        "e_strata": int(manifest["coarse_strata_count"]),
        "prior_image_and_unconstrained_quadratic_slices": prior,
        "exact_all140_continuous_kkt_surviving_slices": kkt_survivors,
        "coordinate_integrality_pruned_slices": integral_pruned,
        "coordinate_integrality_surviving_slices": survivors,
        "zero_e_strata_from_kkt_survivor_population": zero_e_strata,
        "zero_rows_from_kkt_survivor_population": zero_rows,
        "candidate_usage": usage,
        "row_summaries": row_summaries,
        "semantics": {
            "all140_continuous_problem_exact_via_stabilizer_averaging": True,
            "integral_coordinate_penalty_safe_lower_bound": True,
            "closest_vector_search_run": False,
            "surviving_slices_are_not_integral_picard_solutions": True,
            "numerical_picard_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_ORBIT_KKT_INTEGRAL_COORDINATE_CENSUS",
        "prior_slices": prior,
        "kkt_survivors": kkt_survivors,
        "integral_pruned": integral_pruned,
        "surviving_slices": survivors,
        "zero_e_strata": zero_e_strata,
        "zero_rows": zero_rows,
        "bound_sha256": model.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
