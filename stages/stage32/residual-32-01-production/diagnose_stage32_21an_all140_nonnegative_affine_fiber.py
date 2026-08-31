#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix
from z3 import Int, Solver, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from diagnose_stage32_21al_nonnegative_orbit_composition import deterministic_sample, parse_row_id
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from direct_picard_reynolds_rank2_antifixed_coset_bound import (
    ReynoldsRank2AntiFixedCosetBound,
)

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_21AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_21AK_CONSTRAINT_ROWS_SHA256 = "1c8ea0443dcf80dcaec80964618eac97385d85bfa7d009e60d471cd70f3a5169"
EXPECTED_21AK_FACTORS = (1,) * 45 + (2,) * 4 + (4,) * 8 + (8,) * 2
EXPECTED_SELECTED_PAIRING_COUNT = 59
EXPECTED_ALL_PAIRING_COUNT = 140
EXPECTED_ORBIT_COUNT = 14
EXPECTED_LEFT_RATIONAL_RELATION_RANK = 81
EXPECTED_ADDITIONAL_RELATION_RANK_BEYOND_ORBIT_SUMS = 67
EXPECTED_REPRESENTATIVE_SAMPLE_COUNT = 56
SCHEMA = "STAGE32_21AN_ALL140_NONNEGATIVE_AFFINE_PAIRING_FIBER_DIAGNOSTIC_V1"


def solve_full_nonnegative_fiber(
    *,
    z: tuple[int, ...],
    translation_pairing: Matrix,
    pairing_x0_map: Matrix,
    selected_curve_indices: tuple[int, ...],
    constraint_rows: tuple[dict, ...],
    timeout_ms: int,
) -> tuple[str, tuple[int, ...] | None, tuple[int, ...] | None]:
    if translation_pairing.shape != (EXPECTED_ALL_PAIRING_COUNT, EXPECTED_SELECTED_PAIRING_COUNT):
        raise ValueError("21an translation pairing shape regression")
    if pairing_x0_map.shape != (EXPECTED_ALL_PAIRING_COUNT, len(z)):
        raise ValueError("21an affine pairing offset shape regression")

    t = [Int(f"t_{j}") for j in range(EXPECTED_SELECTED_PAIRING_COUNT)]
    solver = Solver()
    solver.set(timeout=timeout_ms)

    y0 = pairing_x0_map * Matrix(z)
    expressions = []
    for i in range(EXPECTED_ALL_PAIRING_COUNT):
        expr = int(y0[i, 0]) + sum(
            int(translation_pairing[i, j]) * t[j]
            for j in range(EXPECTED_SELECTED_PAIRING_COUNT)
        )
        expressions.append(expr)
        solver.add(expr >= 0)

    result = solver.check()
    if result == unknown:
        return "UNKNOWN", None, None
    if result == unsat:
        return "UNSAT", None, None
    if result != sat:
        raise ValueError(f"unexpected z3 result: {result}")

    model = solver.model()
    tw = tuple(int(model.eval(var, model_completion=True).as_long()) for var in t)
    pairings = tuple(
        int(y0[i, 0])
        + sum(int(translation_pairing[i, j]) * tw[j] for j in range(EXPECTED_SELECTED_PAIRING_COUNT))
        for i in range(EXPECTED_ALL_PAIRING_COUNT)
    )
    if any(v < 0 for v in pairings):
        raise ValueError("21an SAT witness violated all140 nonnegativity")

    selected_pairings = tuple(pairings[i] for i in selected_curve_indices)
    if len(selected_pairings) != EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("21an selected pairing extraction regression")

    for row in constraint_rows:
        modulus = int(row["modulus"])
        coeffs = tuple(int(v) for v in row["selected_pairing_coefficients"])
        offsets = tuple(int(v) for v in row["projection_z_offset_coefficients"])
        lhs = sum(coeffs[j] * selected_pairings[j] for j in range(len(coeffs)))
        offset = sum(offsets[k] * int(z[k]) for k in range(len(z)))
        if (lhs - offset) % modulus:
            raise ValueError("21an SAT witness violated upstream 21ak affine congruence")

    return "SAT", tw, pairings


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--manifest", type=Path, required=True)
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    ap.add_argument("--row-shards", type=int, default=16)
    ap.add_argument("--shard-index", type=int, default=0)
    ap.add_argument("--sample-modulus", type=int, default=1024)
    ap.add_argument("--sample-remainder", type=int, default=0)
    ap.add_argument("--solver-timeout-ms", type=int, default=5000)
    ap.add_argument("--example-limit", type=int, default=12)
    args = ap.parse_args()

    if args.row_shards <= 0 or not 0 <= args.shard_index < args.row_shards:
        raise ValueError("invalid deterministic row shard")
    if args.sample_modulus <= 0 or not 0 <= args.sample_remainder < args.sample_modulus:
        raise ValueError("invalid deterministic sample congruence")
    if args.solver_timeout_ms <= 0:
        raise ValueError("solver timeout must be positive")

    manifest = json.loads(args.manifest.read_text())
    claimed_manifest = manifest.pop("canonical_sha256_without_this_field")
    if csha(manifest) != claimed_manifest or claimed_manifest != EXPECTED_MANIFEST_SHA256:
        raise ValueError("FULL178 manifest hash regression")

    bundle = load_retained(args.retained, "s32_21an_picard")
    marking = load_retained(args.marking, "s32_21an_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_21AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    data = reconstruct_translation_data(marking, bundle)
    if tuple(int(v) for v in data["factors"]) != EXPECTED_21AK_FACTORS:
        raise ValueError("32-21ak Smith factor regression")
    constraint_rows = tuple(data["constraint_rows"])
    if csha(list(constraint_rows)) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("32-21ak affine constraint-row hash regression")
    selected_curve_indices = tuple(int(v) for v in data["pivot_rows"])
    if len(selected_curve_indices) != EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("21an selected pairing count regression")

    translation_pairing = data["M"]
    pairing_x0_map = data["pairing_x0_map"]
    orbits = tuple(tuple(int(v) for v in orbit) for orbit in data["orbits"])
    if len(orbits) != EXPECTED_ORBIT_COUNT:
        raise ValueError("21an orbit count regression")
    if EXPECTED_ALL_PAIRING_COUNT - EXPECTED_SELECTED_PAIRING_COUNT != EXPECTED_LEFT_RATIONAL_RELATION_RANK:
        raise ValueError("21an left relation rank arithmetic regression")
    if EXPECTED_LEFT_RATIONAL_RELATION_RANK - EXPECTED_ORBIT_COUNT != EXPECTED_ADDITIONAL_RELATION_RANK_BEYOND_ORBIT_SUMS:
        raise ValueError("21an additional relation rank arithmetic regression")

    for orbit in orbits:
        for j in range(translation_pairing.cols):
            if sum(int(translation_pairing[i, j]) for i in orbit):
                raise ValueError("21an translation pairing violated an orbit-sum relation")

    all_rows: list[str] = []
    for _, ids in sorted(manifest["m_class_rows"].items(), key=lambda kv: int(kv[0])):
        all_rows.extend(str(v) for v in ids)
    if len(all_rows) != 178 or len(set(all_rows)) != 178:
        raise ValueError("FULL178 row population regression")
    selected_rows = [
        row for idx, row in enumerate(all_rows)
        if idx % args.row_shards == args.shard_index
    ]
    if not selected_rows:
        raise ValueError("selected row shard empty")

    rank2 = model.rank2
    kkt = rank2.orbit_qp
    bound = rank2.bound
    bridge = rank2.bridge
    k0, k1 = rank2.kernel_columns

    hashed_points = sampled = sat_count = unsat_count = unknown_count = 0
    cache: dict[tuple[int, ...], tuple[str, tuple[int, ...] | None, tuple[int, ...] | None]] = {}
    sat_examples: list[dict] = []
    unsat_examples: list[dict] = []
    unknown_examples: list[dict] = []
    row_summaries: list[dict] = []
    decision_stream = hashlib.sha256()
    minimum_pairing_seen: int | None = None
    maximum_pairing_seen: int | None = None

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_hashed = row_sampled = row_sat = row_unsat = row_unknown = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            for a in range(lo, hi + 1):
                if not deterministic_sample(
                    row_id, e, a, args.sample_modulus, args.sample_remainder
                ):
                    continue
                hashed_points += 1
                row_hashed += 1

                if not bridge.target_in_image(d, e, a):
                    continue
                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                candidate = kkt.solve_candidate(d, e, a)
                if candidate is None or not candidate.can_reach_selfsq(d, e, a, lower):
                    continue

                survives, _, _, witness, _ = model.can_reach_selfsq(d, e, a, lower)
                if not survives or witness is None:
                    raise ValueError("32-21ad zero-prune witness regression on deterministic sample")
                u, v = witness
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("rank2 affine origin missing")
                z = tuple(
                    int(z0[i] + k0[i] * u + k1[i] * v)
                    for i in range(len(z0))
                )

                sampled += 1
                row_sampled += 1
                cached = cache.get(z)
                if cached is None:
                    cached = solve_full_nonnegative_fiber(
                        z=z,
                        translation_pairing=translation_pairing,
                        pairing_x0_map=pairing_x0_map,
                        selected_curve_indices=selected_curve_indices,
                        constraint_rows=constraint_rows,
                        timeout_ms=args.solver_timeout_ms,
                    )
                    cache[z] = cached
                status, tw, pairings = cached

                if status == "SAT":
                    sat_count += 1
                    row_sat += 1
                    if tw is None or pairings is None:
                        raise ValueError("21an SAT missing exact witness")
                    pmin = min(pairings)
                    pmax = max(pairings)
                    minimum_pairing_seen = pmin if minimum_pairing_seen is None else min(minimum_pairing_seen, pmin)
                    maximum_pairing_seen = pmax if maximum_pairing_seen is None else max(maximum_pairing_seen, pmax)
                    if len(sat_examples) < args.example_limit:
                        sat_examples.append({
                            "row_id": row_id,
                            "e": e,
                            "a": a,
                            "u": u,
                            "v": v,
                            "z": list(z),
                            "translation_witness_sha256": csha(list(tw)),
                            "all140_pairings_sha256": csha(list(pairings)),
                            "minimum_pairing": pmin,
                            "maximum_pairing": pmax,
                        })
                elif status == "UNSAT":
                    unsat_count += 1
                    row_unsat += 1
                    if len(unsat_examples) < args.example_limit:
                        unsat_examples.append({
                            "row_id": row_id,
                            "e": e,
                            "a": a,
                            "u": u,
                            "v": v,
                            "z": list(z),
                        })
                elif status == "UNKNOWN":
                    unknown_count += 1
                    row_unknown += 1
                    if len(unknown_examples) < args.example_limit:
                        unknown_examples.append({
                            "row_id": row_id,
                            "e": e,
                            "a": a,
                            "u": u,
                            "v": v,
                            "z": list(z),
                        })
                else:
                    raise ValueError(f"unexpected 21an status: {status}")

                decision_stream.update(
                    f"{row_id}|{e}|{a}|{u}|{v}|{','.join(map(str, z))}|{status}\n".encode()
                )

        row_summaries.append({
            "row_id": row_id,
            "hash_selected_feasible_interval_points": row_hashed,
            "sampled_continuous_kkt_survivors": row_sampled,
            "all140_nonnegative_fiber_sat": row_sat,
            "all140_nonnegative_fiber_unsat": row_unsat,
            "all140_nonnegative_fiber_unknown": row_unknown,
        })

    if sampled != sat_count + unsat_count + unknown_count:
        raise ValueError("21an sampled decision accounting regression")
    if sampled != EXPECTED_REPRESENTATIVE_SAMPLE_COUNT:
        raise ValueError(
            f"21an representative sample count regression: {sampled} != {EXPECTED_REPRESENTATIVE_SAMPLE_COUNT}"
        )
    if len(cache) != EXPECTED_REPRESENTATIVE_SAMPLE_COUNT:
        raise ValueError(
            f"21an unique projection-state count regression: {len(cache)} != {EXPECTED_REPRESENTATIVE_SAMPLE_COUNT}"
        )

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21an",
        "mode": "EXACT_FULL_ALL140_NONNEGATIVE_AFFINE_PAIRING_FIBER_FEASIBILITY_ON_REPRESENTATIVE_PROJECTION_STATES",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_21AC_CERTIFICATE_SHA256,
        "upstream_32_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
        "z3_version": get_version_string(),
        "interface": {
            "all_pairing_count": EXPECTED_ALL_PAIRING_COUNT,
            "anti_fixed_translation_rank": EXPECTED_SELECTED_PAIRING_COUNT,
            "left_rational_relation_rank": EXPECTED_LEFT_RATIONAL_RELATION_RANK,
            "orbit_sum_relation_rank": EXPECTED_ORBIT_COUNT,
            "additional_independent_rational_relation_rank_beyond_orbit_sums": EXPECTED_ADDITIONAL_RELATION_RANK_BEYOND_ORBIT_SUMS,
            "affine_formula": "y(z,t)=pairing_x0_map*z + M*t, t in Z^59",
            "all140_nonnegative_constraints_enforced": True,
            "all_81_left_rational_relations_enforced_implicitly_by_affine_image_parameterization": True,
            "the_67_non_orbit_relations_are_not_dropped": True,
            "integrality_enforced_by_integer_translation_coordinates": True,
            "upstream_14_2adic_congruences_rechecked_on_every_sat_witness": True,
        },
        "sampling": {
            "row_shards": args.row_shards,
            "shard_index": args.shard_index,
            "selected_row_count": len(selected_rows),
            "selected_rows": selected_rows,
            "sample_modulus": args.sample_modulus,
            "sample_remainder": args.sample_remainder,
            "selection_rule": "same deterministic sha256(row|e|a) sample as 32-21al, applied before expensive slice predicates",
            "hash_selected_feasible_interval_points": hashed_points,
            "sampled_continuous_kkt_survivors": sampled,
            "unique_sampled_projection_states": len(cache),
            "solver_timeout_ms_per_unique_projection_state": args.solver_timeout_ms,
            "this_is_representative_not_full178_credit": True,
        },
        "result": {
            "sat_projection_states": sat_count,
            "unsat_projection_states": unsat_count,
            "unknown_projection_states": unknown_count,
            "unsat_is_exact_for_this_fixed_projection_all140_nonnegative_affine_fiber": True,
            "unsat_is_not_yet_a_slice_prune": True,
            "slice_prune_requires_exhausting_all_relevant_rank2_integer_projection_states": True,
            "unknown_is_not_unsat": True,
            "minimum_pairing_seen_on_sat_witnesses": minimum_pairing_seen,
            "maximum_pairing_seen_on_sat_witnesses": maximum_pairing_seen,
            "decision_stream_sha256": decision_stream.hexdigest(),
            "row_summaries": row_summaries,
            "sat_examples": sat_examples,
            "unsat_examples": unsat_examples,
            "unknown_examples": unknown_examples,
        },
        "interpretation": {
            "full_affine_pairing_fiber_nonnegative_feasibility_solved_for_tested_projection_states": unknown_count == 0,
            "self_intersection_threshold_solved_on_fiber": False,
            "next_if_unsat_found": (
                "32-21ao: exhaust rank2 integer (u,v) projection states only for candidate slices; "
                "promote a slice prune only when every relevant projection state has all140 fiber UNSAT"
            ),
            "next_if_zero_unsat_and_zero_unknown": (
                "32-21ao: the full all140 nonnegative affine-fiber filter is empirically dominated on the "
                "representative existing-witness projections; add the exact self-intersection threshold / "
                "anti-fixed norm optimization on this already-restored affine fiber before any FULL178 pass"
            ),
            "next_if_unknown": (
                "decompose the bounded all140 QF_LIA fiber solver; UNKNOWN receives no prune credit"
            ),
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "terminal_family_materialization_run": False,
            "59d_cvp_run": False,
            "representative_row_shard_only": True,
            "deterministic_sample_only": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "unknown_is_not_unsat": True,
            "planned_effective_heavy_concurrency": 0,
            "artifact_storage_preflight": "single compact JSON; expected <<1 MB; retention 3 days; far below 500 MB operating budget",
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AN_ALL140_NONNEGATIVE_AFFINE_PAIRING_FIBER_DIAGNOSTIC",
        "sampled": sampled,
        "sat": sat_count,
        "unsat": unsat_count,
        "unknown": unknown_count,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
