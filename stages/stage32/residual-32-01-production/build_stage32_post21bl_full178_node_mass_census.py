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
EXPECTED_PREFLIGHT_SHA256 = "1654ef385558c606623f81bfbaf7c68063141a5be39d9b692d58567f011a6c65"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_COARSE_STRATA_BEFORE = 64111
EXPECTED_COARSE_STRATA_ELIMINATED = 3620
EXPECTED_COARSE_STRATA_AFTER = 60491
EXPECTED_AFFECTED_ROWS = 168
SCHEMA = "STAGE32_POST21BL_FULL178_NODE_MASS_CENSUS_SHARD_V1"


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


def ceil_div(a: int, b: int) -> int:
    if b <= 0:
        raise ValueError("ceil_div requires positive denominator")
    return -((-a) // b)


def load_preflight(path: Path) -> dict:
    raw = json.loads(path.read_text())
    claimed = raw.get("canonical_sha256_without_this_field")
    body = dict(raw)
    body.pop("canonical_sha256_without_this_field", None)
    if claimed != EXPECTED_PREFLIGHT_SHA256 or csha(body) != claimed:
        raise ValueError("node-support preflight canonical regression")
    cut = raw.get("exact_cut", {})
    if cut.get("full178_cheap_necessary_form") != "e >= ceil((d-16g+16)/4)":
        raise ValueError("node-mass cut formula regression")
    strata = raw.get("full178_coarse_strata", {})
    expected = (
        strata.get("original_coarse_e_strata"),
        strata.get("eliminated_coarse_e_strata"),
        strata.get("after_cheap_node_mass_cut"),
        strata.get("affected_rows"),
    )
    if expected != (
        EXPECTED_COARSE_STRATA_BEFORE,
        EXPECTED_COARSE_STRATA_ELIMINATED,
        EXPECTED_COARSE_STRATA_AFTER,
        EXPECTED_AFFECTED_ROWS,
    ):
        raise ValueError(f"preflight coarse-strata regression: {expected}")
    return raw


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--preflight", type=Path, required=True)
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
    manifest_claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != manifest_claimed or manifest_claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")
    preflight = load_preflight(args.preflight)

    bundle = load_module_payload(args.retained, "stage32_post21bl_node_mass_picard")
    marking = load_module_payload(args.marking, "stage32_post21bl_node_mass_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("audited 32-21ac evaluator certificate regression")

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
    coarse_before = coarse_after = coarse_eliminated = affected_rows = 0
    postcut_prior = postcut_cont = postcut_pruned = postcut_survivors = 0
    zero_e_strata = zero_rows = checked_u_total = checked_u_max = 0
    reason_counts: Counter[str] = Counter()
    coset_counts: Counter[int] = Counter()
    penalty_counts: Counter[str] = Counter()
    witness_stream = hashlib.sha256()
    decision_stream = hashlib.sha256()
    row_summaries = []

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        legacy_emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        required_e = ceil_div(d - 16 * g + 16, 4)
        effective_emin = max(legacy_emin, required_e)

        row_before = max(0, emax - legacy_emin + 1)
        row_after = max(0, emax - effective_emin + 1)
        row_eliminated = row_before - row_after
        coarse_before += row_before
        coarse_after += row_after
        coarse_eliminated += row_eliminated
        if row_eliminated:
            affected_rows += 1

        lower = -d - 2 + 2 * g
        row_prior = row_cont = row_pruned = row_surv = row_zero_e = 0

        for e in range(effective_emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            e_cont = e_surv = 0

            for a in range(lo, hi + 1):
                if not bridge.target_in_image(d, e, a):
                    continue
                postcut_prior += 1
                row_prior += 1

                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                candidate = kkt.solve_candidate(d, e, a)
                if candidate is None:
                    continue
                if not candidate.can_reach_selfsq(d, e, a, lower):
                    continue

                postcut_cont += 1
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
                    postcut_pruned += 1
                    row_pruned += 1
                    continue

                postcut_survivors += 1
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
                "legacy_e_min": legacy_emin,
                "node_mass_required_e_min": required_e,
                "effective_e_min": effective_emin,
                "e_max": emax,
                "coarse_e_strata_before_cut": row_before,
                "coarse_e_strata_eliminated_by_node_mass_cut": row_eliminated,
                "coarse_e_strata_after_cut": row_after,
                "postcut_image_and_unconstrained_quadratic_slices": row_prior,
                "postcut_continuous_kkt_surviving_slices": row_cont,
                "postcut_antifixed_coset_pruned_slices": row_pruned,
                "postcut_antifixed_coset_surviving_slices": row_surv,
                "postcut_zero_e_strata_from_continuous_survivor_population": row_zero_e,
            }
        )

    if coarse_before != coarse_eliminated + coarse_after:
        raise ValueError("coarse node-mass accounting regression")
    if postcut_pruned + postcut_survivors != postcut_cont:
        raise ValueError("postcut anti-fixed census accounting regression")
    if full_run:
        if coarse_before != EXPECTED_COARSE_STRATA_BEFORE:
            raise ValueError(f"FULL178 coarse-before regression: {coarse_before}")
        if coarse_eliminated != EXPECTED_COARSE_STRATA_ELIMINATED:
            raise ValueError(f"FULL178 cut elimination regression: {coarse_eliminated}")
        if coarse_after != EXPECTED_COARSE_STRATA_AFTER:
            raise ValueError(f"FULL178 coarse-after regression: {coarse_after}")
        if affected_rows != EXPECTED_AFFECTED_ROWS:
            raise ValueError(f"FULL178 affected-row regression: {affected_rows}")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "POST_21BL_FULL178_NODE_MASS_CENSUS",
        "mode": (
            "FULL178_EXACT_NODE_MASS_CUT_THEN_UNCHANGED_21AD_EVALUATORS"
            if full_run
            else "DETERMINISTIC_ROW_SHARD_OF_EXACT_NODE_MASS_CUT_THEN_UNCHANGED_21AD_EVALUATORS"
        ),
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "node_support_preflight_canonical_sha256": EXPECTED_PREFLIGHT_SHA256,
        "node_support_certificate_canonical_sha256": preflight["source"][
            "node_support_certificate_canonical_sha256"
        ],
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "rank2_model_sha256": rank2.certificate["canonical_sha256_without_this_field"],
        "row_shards": args.row_shards,
        "shard_index": args.shard_index,
        "full_run": full_run,
        "full_population_row_count": len(all_rows),
        "selected_row_count": len(selected_rows),
        "selected_rows": selected_rows,
        "node_mass_cut": {
            "formula": "e >= ceil((d-16g+16)/4)",
            "inserted_before_feasible_a_interval": True,
            "inserted_before_target_image": True,
            "inserted_before_kkt": True,
            "inserted_before_antifixed": True,
        },
        "coarse_e_strata_before_cut": coarse_before,
        "coarse_e_strata_eliminated_by_node_mass_cut": coarse_eliminated,
        "coarse_e_strata_after_cut": coarse_after,
        "rows_affected_by_node_mass_cut": affected_rows,
        "postcut_image_and_unconstrained_quadratic_slices": postcut_prior,
        "postcut_exact_continuous_kkt_surviving_slices": postcut_cont,
        "postcut_antifixed_coset_pruned_slices": postcut_pruned,
        "postcut_antifixed_coset_surviving_slices": postcut_survivors,
        "postcut_zero_e_strata_from_continuous_survivor_population": zero_e_strata,
        "postcut_zero_rows_from_continuous_survivor_population": zero_rows,
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
            "node_mass_cut_exact_necessary_for_bijective_normalization_branch": True,
            "strong_48bit_node_support_not_inferred_from_exceptional_mass": True,
            "legacy_21ad_evaluators_used_without_formula_change_after_cut": True,
            "continuous_kkt_problem_exact_under_stabilizer_averaging": True,
            "antifixed_coset_false_decision_safe_for_original_integral_picard_slice": True,
            "antifixed_coset_true_decision_only_necessary_condition": True,
            "terminal_family_materialization_run": False,
            "legacy_prefix_DFS_run": False,
            "anti_fixed_59d_closest_vector_search_run": False,
            "old_679337_survivors_materialized": False,
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
                    "PASS_STAGE32_POST21BL_FULL178_NODE_MASS_CENSUS"
                    if full_run
                    else "PASS_STAGE32_POST21BL_NODE_MASS_SHARD"
                ),
                "selected_rows": len(selected_rows),
                "coarse_before": coarse_before,
                "coarse_eliminated": coarse_eliminated,
                "coarse_after": coarse_after,
                "affected_rows": affected_rows,
                "postcut_prior_slices": postcut_prior,
                "postcut_continuous_kkt_survivors": postcut_cont,
                "postcut_antifixed_pruned": postcut_pruned,
                "postcut_antifixed_survivors": postcut_survivors,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
