#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

from direct_picard_reynolds_rank2_antifixed_coset_bound import (
    ReynoldsRank2AntiFixedCosetBound,
)

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_PRIOR_SLICES = 2018569
EXPECTED_CONTINUOUS_KKT_SURVIVORS = 679337
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
SCHEMA = "STAGE32_21AD_FULL178_ANTIFIXED_COSET_NUMERICAL_CENSUS_V1"


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


def fraction_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--row-shards", type=int, default=1)
    ap.add_argument("--shard-index", type=int, default=0)
    args = ap.parse_args()

    if args.row_shards <= 0:
        raise ValueError("--row-shards must be positive")
    if not 0 <= args.shard_index < args.row_shards:
        raise ValueError("--shard-index must lie in [0,row-shards)")

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed or claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_21ad_picard")
    marking = load_module_payload(args.marking, "stage32_21ad_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    rank2 = model.rank2
    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge = rank2.bridge

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != 178 or len(set(all_rows)) != 178:
        raise ValueError("FULL178 row population regression")

    selected_rows = [
        row_id
        for index, row_id in enumerate(all_rows)
        if index % args.row_shards == args.shard_index
    ]
    if not selected_rows:
        raise ValueError("selected row shard is empty")

    full_run = args.row_shards == 1 and args.shard_index == 0
    prior = 0
    continuous_survivors = 0
    antifixed_pruned = 0
    antifixed_survivors = 0
    zero_rows = 0
    zero_e_strata = 0
    checked_u_total = 0
    checked_u_max = 0
    reason_counts: Counter[str] = Counter()
    coset_counts: Counter[int] = Counter()
    penalty_counts: Counter[str] = Counter()
    witness_stream = hashlib.sha256()
    decision_stream = hashlib.sha256()
    row_summaries = []

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_prior = 0
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
                row_prior += 1

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

                survives, reason, checked_u, witness, penalty = model.can_reach_selfsq(
                    d=d, e=e, a=a, lower=lower
                )
                if penalty is None:
                    raise ValueError("continuous survivor missing exact anti-fixed coset penalty")
                coset_id = model.mapping.coset_id(d, e, a)
                if coset_id is None:
                    raise ValueError("continuous survivor missing exact quotient coset id")
                if penalty != model.coset_lower_bounds[coset_id]:
                    raise ValueError("returned penalty disagrees with exact coset table")

                checked_u_total += checked_u
                checked_u_max = max(checked_u_max, checked_u)
                reason_counts[reason] += 1
                coset_counts[coset_id] += 1
                penalty_counts[fraction_key(penalty)] += 1
                decision_stream.update(
                    (
                        f"{row_id}|{e}|{a}|{coset_id}|{fraction_key(penalty)}|"
                        f"{int(survives)}|{reason}|{checked_u}\n"
                    ).encode()
                )

                if not survives:
                    antifixed_pruned += 1
                    row_pruned += 1
                    continue

                antifixed_survivors += 1
                row_surv += 1
                e_surv += 1
                if witness is None:
                    raise ValueError("surviving anti-fixed coset slice missing rank2 witness")
                witness_stream.update(
                    (
                        f"{row_id}|{e}|{a}|{witness[0]}|{witness[1]}|"
                        f"{fraction_key(penalty)}\n"
                    ).encode()
                )

            if e_cont > 0 and e_surv == 0:
                zero_e_strata += 1
                row_zero_e += 1

        if row_cont > 0 and row_surv == 0:
            zero_rows += 1
        row_summaries.append(
            {
                "row_id": row_id,
                "prior_image_and_unconstrained_quadratic_slices": row_prior,
                "continuous_kkt_surviving_slices": row_cont,
                "antifixed_coset_pruned_slices": row_pruned,
                "antifixed_coset_surviving_slices": row_surv,
                "zero_e_strata_from_continuous_survivor_population": row_zero_e,
            }
        )

    if antifixed_pruned + antifixed_survivors != continuous_survivors:
        raise ValueError("32-21ad census accounting regression")
    if full_run:
        if prior != EXPECTED_PRIOR_SLICES:
            raise ValueError(f"prior slice regression: {prior}")
        if continuous_survivors != EXPECTED_CONTINUOUS_KKT_SURVIVORS:
            raise ValueError(
                f"continuous KKT survivor regression: {continuous_survivors}"
            )

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ad",
        "mode": (
            "FULL178_EXACT_CONTINUOUS_KKT_THEN_AUDITED_32_21AC_ANTIFIXED_COSET_BOUND"
            if full_run
            else "DETERMINISTIC_ROW_SHARD_PREFLIGHT_OF_AUDITED_32_21AC_ANTIFIXED_COSET_BOUND"
        ),
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "rank2_model_sha256": rank2.certificate[
            "canonical_sha256_without_this_field"
        ],
        "row_shards": args.row_shards,
        "shard_index": args.shard_index,
        "full_run": full_run,
        "full_population_row_count": len(all_rows),
        "selected_row_count": len(selected_rows),
        "selected_rows": selected_rows,
        "prior_image_and_unconstrained_quadratic_slices": prior,
        "exact_continuous_kkt_surviving_slices": continuous_survivors,
        "antifixed_coset_pruned_slices": antifixed_pruned,
        "antifixed_coset_surviving_slices": antifixed_survivors,
        "zero_e_strata_from_continuous_survivor_population": zero_e_strata,
        "zero_rows_from_continuous_survivor_population": zero_rows,
        "checked_integer_u_total": checked_u_total,
        "checked_integer_u_max_per_slice": checked_u_max,
        "decision_reason_counts": dict(sorted(reason_counts.items())),
        "quotient_coset_population_counts": {
            str(k): v for k, v in sorted(coset_counts.items())
        },
        "coset_penalty_population_counts": dict(sorted(penalty_counts.items())),
        "decision_stream_sha256": decision_stream.hexdigest(),
        "surviving_witness_stream_sha256": witness_stream.hexdigest(),
        "row_summaries": row_summaries,
        "semantics": {
            "continuous_kkt_problem_exact_under_stabilizer_averaging": True,
            "audited_32_21ac_evaluator_used_without_formula_change": True,
            "antifixed_coset_false_decision_safe_for_original_integral_picard_slice": True,
            "antifixed_coset_true_decision_only_necessary_condition": True,
            "terminal_family_materialization_run": False,
            "legacy_prefix_DFS_run": False,
            "anti_fixed_59d_closest_vector_search_run": False,
            "unknown_is_unsat": False,
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

    print(
        json.dumps(
            {
                "verdict": (
                    "PASS_STAGE32_21AD_FULL178_ANTIFIXED_COSET_NUMERICAL_CENSUS"
                    if full_run
                    else "PASS_STAGE32_21AD_DETERMINISTIC_SHARD_PREFLIGHT"
                ),
                "selected_rows": len(selected_rows),
                "prior_slices": prior,
                "continuous_kkt_survivors": continuous_survivors,
                "antifixed_pruned": antifixed_pruned,
                "antifixed_survivors": antifixed_survivors,
                "zero_e_strata": zero_e_strata,
                "zero_rows": zero_rows,
                "checked_u_total": checked_u_total,
                "checked_u_max": checked_u_max,
                "canonical_sha256": payload[
                    "canonical_sha256_without_this_field"
                ],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
