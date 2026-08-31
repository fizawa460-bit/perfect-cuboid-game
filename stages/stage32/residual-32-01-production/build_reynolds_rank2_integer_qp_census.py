#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from pathlib import Path

from direct_picard_reynolds_rank2_integer_qp import ReynoldsRank2IntegerQP


EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PRIOR_SLICES = 2018569
EXPECTED_CONTINUOUS_KKT_SURVIVORS = 679337
SCHEMA = "STAGE32_RESIDUAL32_01_REYNOLDS_RANK2_EXACT_INTEGER_QP_CENSUS_V1"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def load_module_payload(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed or claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_reynolds_rank2_qp_picard")
    marking = load_module_payload(args.marking, "stage32_reynolds_rank2_qp_marking")
    model = ReynoldsRank2IntegerQP.from_retained(marking, bundle)
    kkt = model.orbit_qp
    bound = model.bound
    bridge = model.bridge

    rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        rows.extend(str(v) for v in ids)
    if len(rows) != 178 or len(set(rows)) != 178:
        raise ValueError("FULL178 row population regression")

    prior = 0
    continuous_survivors = 0
    projection_pruned = 0
    projection_survivors = 0
    zero_rows = 0
    zero_e_strata = 0
    checked_u_total = 0
    checked_u_max = 0
    reason_counts: Counter[str] = Counter()
    witness_stream = hashlib.sha256()
    row_summaries = []

    for row_id in rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_cont = 0
        row_pruned = 0
        row_surv = 0
        row_zero_e = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            e_cont = 0
            e_surv = 0

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

                continuous_survivors += 1
                row_cont += 1
                e_cont += 1

                survives, reason, checked_u, witness = model.can_reach_selfsq(
                    d=d, e=e, a=a, lower=lower
                )
                checked_u_total += checked_u
                checked_u_max = max(checked_u_max, checked_u)
                reason_counts[reason] += 1

                if not survives:
                    projection_pruned += 1
                    row_pruned += 1
                    continue

                projection_survivors += 1
                row_surv += 1
                e_surv += 1
                if witness is None:
                    raise ValueError("surviving projected slice missing witness")
                witness_stream.update(
                    f"{row_id}|{e}|{a}|{witness[0]}|{witness[1]}\n".encode()
                )

            if e_cont > 0 and e_surv == 0:
                zero_e_strata += 1
                row_zero_e += 1

        if row_cont > 0 and row_surv == 0:
            zero_rows += 1
        row_summaries.append({
            "row_id": row_id,
            "continuous_kkt_surviving_slices": row_cont,
            "rank2_integer_qp_pruned_slices": row_pruned,
            "rank2_integer_qp_surviving_slices": row_surv,
            "zero_e_strata_from_continuous_survivor_population": row_zero_e,
        })

    if prior != EXPECTED_PRIOR_SLICES:
        raise ValueError(f"prior slice regression: {prior}")
    if continuous_survivors != EXPECTED_CONTINUOUS_KKT_SURVIVORS:
        raise ValueError(f"continuous KKT survivor regression: {continuous_survivors}")
    if projection_pruned + projection_survivors != continuous_survivors:
        raise ValueError("projection census accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "item": "RESIDUAL_32_01_PRODUCTION",
        "mode": "FULL178_EXACT_CONTINUOUS_KKT_THEN_EXACT_REYNOLDS_PROJECTED_RANK2_INTEGER_QP_NECESSARY_CONDITION",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "rank2_integer_qp_model_sha256": model.certificate[
            "canonical_sha256_without_this_field"
        ],
        "row_count": len(rows),
        "coarse_e_strata": int(manifest["coarse_strata_count"]),
        "prior_image_and_unconstrained_quadratic_slices": prior,
        "exact_continuous_kkt_surviving_slices": continuous_survivors,
        "rank2_integer_qp_pruned_slices": projection_pruned,
        "rank2_integer_qp_surviving_slices": projection_survivors,
        "zero_e_strata_from_continuous_survivor_population": zero_e_strata,
        "zero_rows_from_continuous_survivor_population": zero_rows,
        "checked_integer_u_total": checked_u_total,
        "checked_integer_u_max_per_slice": checked_u_max,
        "decision_reason_counts": dict(sorted(reason_counts.items())),
        "surviving_witness_stream_sha256": witness_stream.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "continuous_kkt_problem_exact_under_stabilizer_averaging": True,
            "projected_integral_lattice_parameterization_exact": True,
            "rank2_integer_qp_decision_exact": True,
            "rank2_false_decision_safe_for_original_integral_picard_slice": True,
            "rank2_true_decision_only_necessary_condition": True,
            "anti_fixed_lift_not_solved": True,
            "prefix_DFS_not_run": True,
            "numerical_row_complete": False,
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
        "verdict": "PASS_REYNOLDS_RANK2_EXACT_INTEGER_QP_CENSUS",
        "prior_slices": prior,
        "continuous_kkt_survivors": continuous_survivors,
        "projection_pruned": projection_pruned,
        "projection_survivors": projection_survivors,
        "zero_e_strata": zero_e_strata,
        "zero_rows": zero_rows,
        "checked_u_total": checked_u_total,
        "checked_u_max": checked_u_max,
        "model_sha256": model.certificate["canonical_sha256_without_this_field"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
