#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import pathlib

from direct_picard_orbit_sum_qp_bound import DirectPicardOrbitSumQPBound

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PRIOR_IMAGE_QUADRATIC_SLICES = 2018569
EXPECTED_FIXED_ORBIT_SURVIVORS = 1248007
SCHEMA = "STAGE32_RESIDUAL32_01_DIRECT_PICARD_ORBIT_SUM_EXACT_KKT_QP_CENSUS_V1"


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

    bundle = load_module_payload(args.retained, "stage32_orbit_qp_picard")
    marking = load_module_payload(args.marking, "stage32_orbit_qp_marking")
    model = DirectPicardOrbitSumQPBound.from_retained(marking, bundle)
    bound = model.bound
    bridge = bound.bridge

    rows: list[str] = []
    for _, ids in sorted(
        manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])
    ):
        rows.extend(str(v) for v in ids)
    assert len(rows) == 178 and len(set(rows)) == 178

    prior = 0
    fixed_pruned = 0
    fixed_survivors = 0
    qp_infeasible = 0
    qp_selfsq_pruned = 0
    survivors = 0
    zero_rows = 0
    zero_e_strata = 0
    candidate_usage = [0] * len(model.candidates)
    candidate_selfsq_prunes = [0] * len(model.candidates)
    row_summaries = []

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g

        row_prior = 0
        row_fixed_pruned = 0
        row_qp_infeasible = 0
        row_qp_selfsq_pruned = 0
        row_survivors = 0
        row_zero_e = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(
                d=d, e=e, upper=upper, lower=lower
            )
            e_prior = 0
            e_survivors = 0

            if interval is not None:
                lo, hi = interval
                for a in range(lo, hi + 1):
                    if not bridge.target_in_image(d, e, a):
                        continue

                    prior += 1
                    row_prior += 1
                    e_prior += 1

                    if model.orbit_model.first_negative_fixed_orbit(
                        d, e, a
                    ) is not None:
                        fixed_pruned += 1
                        row_fixed_pruned += 1
                        continue

                    fixed_survivors += 1
                    candidate = model.solve_candidate(d, e, a)
                    if candidate is None:
                        qp_infeasible += 1
                        row_qp_infeasible += 1
                        continue

                    candidate_usage[candidate.candidate_id] += 1
                    if not candidate.can_reach_selfsq(d, e, a, lower):
                        qp_selfsq_pruned += 1
                        row_qp_selfsq_pruned += 1
                        candidate_selfsq_prunes[candidate.candidate_id] += 1
                        continue

                    survivors += 1
                    row_survivors += 1
                    e_survivors += 1

            if e_prior > 0 and e_survivors == 0:
                zero_e_strata += 1
                row_zero_e += 1

        if row_prior > 0 and row_survivors == 0:
            zero_rows += 1

        row_summaries.append({
            "row_id": row_id,
            "prior_image_quadratic_slices": row_prior,
            "fixed_orbit_sum_pruned_slices": row_fixed_pruned,
            "orbit_qp_infeasible_slices": row_qp_infeasible,
            "orbit_qp_selfsq_pruned_slices": row_qp_selfsq_pruned,
            "orbit_qp_surviving_slices": row_survivors,
            "zero_e_strata_after_orbit_qp": row_zero_e,
        })

    assert prior == EXPECTED_PRIOR_IMAGE_QUADRATIC_SLICES, prior
    assert fixed_survivors == EXPECTED_FIXED_ORBIT_SURVIVORS, fixed_survivors
    assert (
        fixed_pruned
        + qp_infeasible
        + qp_selfsq_pruned
        + survivors
        == prior
    )

    active_usage = []
    for candidate in model.candidates:
        used = candidate_usage[candidate.candidate_id]
        pruned = candidate_selfsq_prunes[candidate.candidate_id]
        if used:
            active_usage.append({
                "candidate_id": candidate.candidate_id,
                "active_orbit_ids": list(candidate.active_orbit_ids),
                "active_size": len(candidate.active_orbit_ids),
                "selected_slice_count": used,
                "selfsq_pruned_slice_count": pruned,
                "surviving_slice_count": used - pruned,
            })
    active_usage.sort(
        key=lambda rec: (-rec["selected_slice_count"], rec["candidate_id"])
    )

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "FULL178_EXACT_BASE_SLICE_PLUS_STABILIZER_ORBIT_SUM_EXACT_KKT_QP",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "orbit_sum_qp_certificate_sha256": model.certificate[
            "canonical_sha256_without_this_field"
        ],
        "row_count": len(rows),
        "e_strata": int(manifest["coarse_strata_count"]),
        "orbit_sum_quotient_rank_mod_phi": model.quotient_rank,
        "kkt_candidate_count": len(model.candidates),
        "prior_image_and_continuous_quadratic_feasible_slices": prior,
        "fixed_orbit_sum_pruned_slices": fixed_pruned,
        "fixed_orbit_sum_surviving_slices": fixed_survivors,
        "orbit_qp_infeasible_slices": qp_infeasible,
        "orbit_qp_selfsq_pruned_slices": qp_selfsq_pruned,
        "orbit_qp_surviving_slices": survivors,
        "new_zero_e_strata": zero_e_strata,
        "new_zero_rows": zero_rows,
        "candidate_usage": active_usage,
        "row_summaries": row_summaries,
        "semantics": {
            "all14_stabilizer_orbit_sum_nonnegativity_used_simultaneously": True,
            "orbit_sum_continuous_qp_exact": True,
            "all140_individual_nonnegativity_still_stronger": True,
            "individual_within_orbit_nonnegativity_not_yet_used": True,
            "integral_640_coset_correction_not_used": True,
            "numerical_picard_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n"
    )

    print(json.dumps({
        "verdict": "PASS_DIRECT_PICARD_ORBIT_SUM_EXACT_KKT_QP_CENSUS",
        "prior_slices": prior,
        "fixed_pruned": fixed_pruned,
        "fixed_survivors": fixed_survivors,
        "qp_infeasible": qp_infeasible,
        "qp_selfsq_pruned": qp_selfsq_pruned,
        "surviving_slices": survivors,
        "zero_e_strata": zero_e_strata,
        "zero_rows": zero_rows,
        "kkt_candidates": len(model.candidates),
        "bound_sha256": model.certificate[
            "canonical_sha256_without_this_field"
        ],
        "canonical_sha256": payload[
            "canonical_sha256_without_this_field"
        ],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
