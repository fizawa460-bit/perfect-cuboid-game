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
from direct_picard_reynolds_rank2_integer_qp import OBJECTIVE_DENOMINATOR, dot, quad

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
SCHEMA = "STAGE32_21AE_ACTUAL_RESIDUE_WITNESS_PREFLIGHT_V1"


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


def frac_key(value: Fraction) -> str:
    return f"{value.numerator}/{value.denominator}"


def projected_margin_numerator(rank2, z0: tuple[int, ...], lower: int, u: int, v: int) -> int:
    dlin = 2 * dot(z0, rank2.kernel_h0)
    elin = 2 * dot(z0, rank2.kernel_h1)
    fconst = quad(rank2.hessian, z0) - int(lower) * OBJECTIVE_DENOMINATOR
    return (
        rank2.objective_uu * u * u
        + rank2.objective_uv_twice * u * v
        + rank2.objective_vv * v * v
        + dlin * u
        + elin * v
        + fconst
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--row-shards", type=int, default=16)
    ap.add_argument("--shard-index", type=int, default=0)
    ap.add_argument("--example-limit", type=int, default=24)
    args = ap.parse_args()

    if args.row_shards <= 0 or not 0 <= args.shard_index < args.row_shards:
        raise ValueError("invalid deterministic row shard")
    if args.example_limit < 0:
        raise ValueError("--example-limit must be nonnegative")

    manifest = json.loads(args.manifest.read_text())
    claimed = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed or claimed != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_module_payload(args.retained, "stage32_21ae_picard")
    marking = load_module_payload(args.marking, "stage32_21ae_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    rank2 = model.rank2
    mapping = model.mapping
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

    prior = 0
    continuous_survivors = 0
    coset_survivors = 0
    actual_witness_pass = 0
    actual_witness_fail = 0
    actual_penalty_equal_coset = 0
    actual_penalty_stronger = 0
    checked_u_total = 0
    checked_u_max = 0
    actual_penalty_counts: Counter[str] = Counter()
    coset_penalty_counts: Counter[str] = Counter()
    uplift_counts: Counter[str] = Counter()
    decision_stream = hashlib.sha256()
    fail_examples: list[dict] = []
    row_summaries: list[dict] = []

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_cont = 0
        row_pass = 0
        row_fail = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
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
                if candidate is None or not candidate.can_reach_selfsq(d, e, a, lower):
                    continue

                continuous_survivors += 1
                row_cont += 1
                survives, reason, checked_u, witness, coset_penalty = model.can_reach_selfsq(
                    d=d, e=e, a=a, lower=lower
                )
                if not survives or witness is None or coset_penalty is None:
                    raise ValueError(
                        "32-21ad audited zero-prune invariant regressed on representative shard"
                    )
                if reason != "ANTIFIXED_COSET_BOUND_SURVIVES":
                    raise ValueError(f"unexpected 32-21ac survivor reason: {reason}")
                coset_survivors += 1
                checked_u_total += checked_u
                checked_u_max = max(checked_u_max, checked_u)

                u, v = witness
                residue = mapping.residue(d, e, a, u, v)
                if residue is None:
                    raise ValueError("rank2 witness did not map to a projection residue")
                actual_penalty = mapping.penalty.lower_bound_from_residue(residue)
                if actual_penalty < coset_penalty:
                    raise ValueError("actual residue penalty fell below its exact coset minimum")

                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("continuous survivor lost affine origin")
                margin_num = projected_margin_numerator(rank2, z0, lower, u, v)
                coset_ok = margin_num * coset_penalty.denominator >= (
                    OBJECTIVE_DENOMINATOR * coset_penalty.numerator
                )
                if not coset_ok:
                    raise ValueError("returned 32-21ac witness does not satisfy coset penalty")
                actual_ok = margin_num * actual_penalty.denominator >= (
                    OBJECTIVE_DENOMINATOR * actual_penalty.numerator
                )

                if actual_penalty == coset_penalty:
                    actual_penalty_equal_coset += 1
                else:
                    actual_penalty_stronger += 1
                uplift = actual_penalty - coset_penalty
                actual_penalty_counts[frac_key(actual_penalty)] += 1
                coset_penalty_counts[frac_key(coset_penalty)] += 1
                uplift_counts[frac_key(uplift)] += 1

                if actual_ok:
                    actual_witness_pass += 1
                    row_pass += 1
                else:
                    actual_witness_fail += 1
                    row_fail += 1
                    if len(fail_examples) < args.example_limit:
                        fail_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "coset_penalty": frac_key(coset_penalty),
                                "actual_penalty": frac_key(actual_penalty),
                                "projected_margin": f"{margin_num}/{OBJECTIVE_DENOMINATOR}",
                                "projection_class_id": mapping.residue_to_class_id[residue],
                                "coset_id": mapping.residue_to_coset_id[residue],
                            }
                        )

                decision_stream.update(
                    (
                        f"{row_id}|{e}|{a}|{u}|{v}|{margin_num}|"
                        f"{frac_key(coset_penalty)}|{frac_key(actual_penalty)}|{int(actual_ok)}\n"
                    ).encode()
                )

        row_summaries.append(
            {
                "row_id": row_id,
                "continuous_kkt_survivors": row_cont,
                "existing_coset_witness_passes_actual_residue_penalty": row_pass,
                "existing_coset_witness_fails_actual_residue_penalty": row_fail,
            }
        )

    if continuous_survivors != coset_survivors:
        raise ValueError("representative shard no longer reproduces 32-21ad zero-prune state")
    if actual_witness_pass + actual_witness_fail != coset_survivors:
        raise ValueError("actual-residue witness accounting regression")
    if actual_penalty_equal_coset + actual_penalty_stronger != coset_survivors:
        raise ValueError("penalty comparison accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21ae",
        "mode": "DETERMINISTIC_REPRESENTATIVE_SHARD_ONE_SIDED_ACTUAL_RESIDUE_WITNESS_DIAGNOSTIC",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_AC_CERTIFICATE_SHA256,
        "rank2_model_sha256": rank2.certificate["canonical_sha256_without_this_field"],
        "row_shards": args.row_shards,
        "shard_index": args.shard_index,
        "selected_rows": selected_rows,
        "selected_row_count": len(selected_rows),
        "prior_image_slices_seen": prior,
        "continuous_kkt_survivors": continuous_survivors,
        "existing_coset_survivors": coset_survivors,
        "existing_coset_witness_passes_actual_residue_penalty": actual_witness_pass,
        "existing_coset_witness_fails_actual_residue_penalty": actual_witness_fail,
        "actual_penalty_equals_coset_minimum_at_existing_witness": actual_penalty_equal_coset,
        "actual_penalty_strictly_stronger_than_coset_minimum_at_existing_witness": actual_penalty_stronger,
        "checked_integer_u_total_in_existing_32_21ac_evaluator": checked_u_total,
        "checked_integer_u_max_per_slice_in_existing_32_21ac_evaluator": checked_u_max,
        "actual_penalty_population_counts": dict(sorted(actual_penalty_counts.items())),
        "coset_penalty_population_counts": dict(sorted(coset_penalty_counts.items())),
        "penalty_uplift_population_counts": dict(sorted(uplift_counts.items())),
        "witness_fail_examples": fail_examples,
        "decision_stream_sha256": decision_stream.hexdigest(),
        "row_summaries": row_summaries,
        "interpretation": {
            "existing_witness_actual_pass_proves_slice_survives_any_actual_residue_penalty_test": True,
            "existing_witness_actual_fail_does_not_prove_slice_prunable": True,
            "witness_fail_requires_exact_search_over_other_rank2_integer_pairs": True,
            "diagnostic_is_one_sided_strategy_preflight_not_full178_numerical_credit": True,
            "no_actual_residue_full_search_run": True,
            "no_terminal_family_materialization_run": True,
            "no_legacy_prefix_DFS_run": True,
            "no_59d_antifixed_CVP_run": True,
        },
        "firewalls": {
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
                "verdict": "PASS_STAGE32_21AE_ACTUAL_RESIDUE_WITNESS_PREFLIGHT",
                "selected_rows": len(selected_rows),
                "continuous_survivors": continuous_survivors,
                "witness_actual_pass": actual_witness_pass,
                "witness_actual_fail": actual_witness_fail,
                "actual_penalty_stronger_at_witness": actual_penalty_stronger,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
