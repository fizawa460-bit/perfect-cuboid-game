#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path

from sympy import Matrix
from z3 import Int, Solver, get_version_string, sat, unknown, unsat

from diagnose_stage32_21ak_affine_2adic_membership import reconstruct_translation_data
from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from direct_picard_reynolds_rank2_antifixed_coset_bound import (
    ReynoldsRank2AntiFixedCosetBound,
)

EXPECTED_MANIFEST_SHA256 = "46809e2cb9851434b56778369beac131771902c026f10d49b2c0328680383e23"
EXPECTED_21AC_CERTIFICATE_SHA256 = "2c227d773aaf6a6543ae89419c468d85fd4ebd42422eb6f4c8ac60b2e7227c8e"
EXPECTED_21AK_CERTIFICATE_SHA256 = "51effd04ea195831a3bf1859710716910e5ef0945caab94c36c1c03840b1d6ee"
EXPECTED_21AK_CONSTRAINT_ROWS_SHA256 = "1c8ea0443dcf80dcaec80964618eac97385d85bfa7d009e60d471cd70f3a5169"
EXPECTED_21AK_FACTORS = (1,) * 45 + (2,) * 4 + (4,) * 8 + (8,) * 2
EXPECTED_SELECTED_PAIRING_COUNT = 59
EXPECTED_ORBIT_COUNT = 14
SCHEMA = "STAGE32_21AL_NONNEGATIVE_ORBIT_COMPOSITION_2ADIC_DIAGNOSTIC_V1"


def parse_row_id(row_id: str) -> tuple[int, int]:
    g, d = row_id.split("-d")
    return int(g[1:]), int(d)


def deterministic_sample(
    row_id: str,
    e: int,
    a: int,
    u: int,
    v: int,
    sample_modulus: int,
    sample_remainder: int,
) -> bool:
    raw = f"{row_id}|{e}|{a}|{u}|{v}".encode()
    value = int.from_bytes(hashlib.sha256(raw).digest()[:8], "big")
    return value % sample_modulus == sample_remainder


def solve_selected_composition(
    *,
    z: tuple[int, ...],
    orbit_totals: tuple[int, ...],
    selected_curve_indices: tuple[int, ...],
    selected_orbit_ids: tuple[int, ...],
    orbit_sizes: tuple[int, ...],
    constraint_rows: tuple[dict, ...],
    timeout_ms: int,
) -> tuple[str, tuple[int, ...] | None]:
    if len(selected_curve_indices) != EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("selected pairing coordinate count regression")
    if len(selected_orbit_ids) != EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("selected orbit-id count regression")
    if len(orbit_totals) != EXPECTED_ORBIT_COUNT:
        raise ValueError("orbit total count regression")

    s = [Int(f"s_{j}") for j in range(EXPECTED_SELECTED_PAIRING_COUNT)]
    solver = Solver()
    solver.set(timeout=timeout_ms)
    for var in s:
        solver.add(var >= 0)

    selected_positions_by_orbit: list[list[int]] = [[] for _ in range(EXPECTED_ORBIT_COUNT)]
    for j, oid in enumerate(selected_orbit_ids):
        selected_positions_by_orbit[int(oid)].append(j)

    for oid, positions in enumerate(selected_positions_by_orbit):
        total = int(orbit_totals[oid])
        if total < 0:
            raise ValueError("negative fixed orbit total reached 21al")
        selected_sum = sum((s[j] for j in positions), 0)
        if len(positions) == int(orbit_sizes[oid]):
            solver.add(selected_sum == total)
        else:
            solver.add(selected_sum <= total)

    for row in constraint_rows:
        modulus = int(row["modulus"])
        coeffs = tuple(int(v) for v in row["selected_pairing_coefficients"])
        offsets = tuple(int(v) for v in row["projection_z_offset_coefficients"])
        if len(coeffs) != EXPECTED_SELECTED_PAIRING_COUNT or len(offsets) != len(z):
            raise ValueError("21ak affine constraint shape regression")
        lhs = sum((coeffs[j] * s[j] for j in range(len(coeffs))), 0)
        offset = sum(offsets[k] * int(z[k]) for k in range(len(z)))
        solver.add((lhs - offset) % modulus == 0)

    result = solver.check()
    if result == unknown:
        return "UNKNOWN", None
    if result == unsat:
        return "UNSAT", None
    if result != sat:
        raise ValueError(f"unexpected z3 result: {result}")

    model = solver.model()
    witness = tuple(int(model.eval(var, model_completion=True).as_long()) for var in s)

    if any(value < 0 for value in witness):
        raise ValueError("SAT composition witness became negative")
    for oid, positions in enumerate(selected_positions_by_orbit):
        subtotal = sum(witness[j] for j in positions)
        total = int(orbit_totals[oid])
        if len(positions) == int(orbit_sizes[oid]):
            if subtotal != total:
                raise ValueError("SAT witness violated fully-selected orbit total")
        elif subtotal > total:
            raise ValueError("SAT witness exceeded partially-selected orbit total")
    for row in constraint_rows:
        modulus = int(row["modulus"])
        lhs = sum(
            int(row["selected_pairing_coefficients"][j]) * witness[j]
            for j in range(EXPECTED_SELECTED_PAIRING_COUNT)
        )
        offset = sum(
            int(row["projection_z_offset_coefficients"][k]) * int(z[k])
            for k in range(len(z))
        )
        if (lhs - offset) % modulus:
            raise ValueError("SAT witness violated 21ak affine congruence")
    return "SAT", witness


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
    ap.add_argument("--solver-timeout-ms", type=int, default=250)
    ap.add_argument("--example-limit", type=int, default=24)
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

    bundle = load_retained(args.retained, "s32_21al_picard")
    marking = load_retained(args.marking, "s32_21al_marking")

    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    if model.certificate["canonical_sha256_without_this_field"] != EXPECTED_21AC_CERTIFICATE_SHA256:
        raise ValueError("32-21ac audited evaluator certificate regression")

    # Reconstruct the exact 21ak interface once. 21ak itself has a successful
    # source-locked certificate at EXPECTED_21AK_CERTIFICATE_SHA256; here we
    # additionally lock the exact 14 published constraint rows used below.
    data = reconstruct_translation_data(marking, bundle)
    if tuple(int(v) for v in data["factors"]) != EXPECTED_21AK_FACTORS:
        raise ValueError("32-21ak Smith factor regression")
    constraint_rows = tuple(data["constraint_rows"])
    if len(constraint_rows) != 14:
        raise ValueError("21ak nonunit affine constraint count regression")
    if csha(list(constraint_rows)) != EXPECTED_21AK_CONSTRAINT_ROWS_SHA256:
        raise ValueError("32-21ak affine constraint-row hash regression")

    selected_curve_indices = tuple(int(v) for v in data["pivot_rows"])
    selected_orbit_ids = tuple(int(v) for v in data["selected_orbit_ids"])
    orbits = tuple(tuple(int(v) for v in orbit) for orbit in data["orbits"])
    if len(orbits) != EXPECTED_ORBIT_COUNT:
        raise ValueError("stabilizer orbit count regression")
    orbit_sizes = tuple(len(orbit) for orbit in orbits)
    pairing_x0_map = data["pairing_x0_map"]

    selected_counts_by_orbit = tuple(
        sum(1 for oid in selected_orbit_ids if oid == target)
        for target in range(EXPECTED_ORBIT_COUNT)
    )
    fully_selected_orbits = tuple(
        oid for oid in range(EXPECTED_ORBIT_COUNT)
        if selected_counts_by_orbit[oid] == orbit_sizes[oid]
    )

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

    continuous = sampled = sat_count = unsat_count = unknown_count = 0
    cache: dict[tuple[int, ...], tuple[str, tuple[int, ...] | None, tuple[int, ...]]] = {}
    sat_examples: list[dict] = []
    unsat_examples: list[dict] = []
    unknown_examples: list[dict] = []
    row_summaries: list[dict] = []
    decision_stream = hashlib.sha256()
    minimum_orbit_total: int | None = None
    maximum_orbit_total = 0

    for row_id in selected_rows:
        g, d = parse_row_id(row_id)
        emin = 8 if g == 0 else 4
        emax = (19 * d) // 5
        lower = -d - 2 + 2 * g
        row_cont = row_sampled = row_sat = row_unsat = row_unknown = 0

        for e in range(emin, emax + 1):
            upper = 19 * d - 5 * e
            interval = bound.feasible_a_interval(d=d, e=e, upper=upper, lower=lower)
            if interval is None:
                continue
            lo, hi = interval
            for a in range(lo, hi + 1):
                if not bridge.target_in_image(d, e, a):
                    continue
                if kkt.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
                    continue
                candidate = kkt.solve_candidate(d, e, a)
                if candidate is None or not candidate.can_reach_selfsq(d, e, a, lower):
                    continue

                continuous += 1
                row_cont += 1
                survives, _, _, witness, _ = model.can_reach_selfsq(d, e, a, lower)
                if not survives or witness is None:
                    raise ValueError("32-21ad zero-prune witness regression")
                u, v = witness
                if not deterministic_sample(
                    row_id, e, a, u, v, args.sample_modulus, args.sample_remainder
                ):
                    continue

                sampled += 1
                row_sampled += 1
                z0 = rank2.affine_origin(d, e, a)
                if z0 is None:
                    raise ValueError("rank2 affine origin missing")
                z = tuple(
                    int(z0[i] + k0[i] * u + k1[i] * v)
                    for i in range(len(z0))
                )

                cached = cache.get(z)
                if cached is None:
                    y0 = pairing_x0_map * Matrix(z)
                    orbit_totals = tuple(
                        sum(int(y0[i, 0]) for i in orbit)
                        for orbit in orbits
                    )
                    if any(total < 0 for total in orbit_totals):
                        raise ValueError("existing rank2 witness has negative fixed orbit total")
                    for total in orbit_totals:
                        minimum_orbit_total = total if minimum_orbit_total is None else min(minimum_orbit_total, total)
                        maximum_orbit_total = max(maximum_orbit_total, total)

                    status, composition = solve_selected_composition(
                        z=z,
                        orbit_totals=orbit_totals,
                        selected_curve_indices=selected_curve_indices,
                        selected_orbit_ids=selected_orbit_ids,
                        orbit_sizes=orbit_sizes,
                        constraint_rows=constraint_rows,
                        timeout_ms=args.solver_timeout_ms,
                    )
                    cached = (status, composition, orbit_totals)
                    cache[z] = cached
                status, composition, orbit_totals = cached

                if status == "SAT":
                    sat_count += 1
                    row_sat += 1
                    if composition is None:
                        raise ValueError("SAT status missing selected composition witness")
                    if len(sat_examples) < args.example_limit:
                        sat_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "z": list(z),
                                "orbit_totals": list(orbit_totals),
                                "selected_composition_sha256": csha(list(composition)),
                            }
                        )
                elif status == "UNSAT":
                    unsat_count += 1
                    row_unsat += 1
                    if len(unsat_examples) < args.example_limit:
                        unsat_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "z": list(z),
                                "orbit_totals": list(orbit_totals),
                            }
                        )
                elif status == "UNKNOWN":
                    unknown_count += 1
                    row_unknown += 1
                    if len(unknown_examples) < args.example_limit:
                        unknown_examples.append(
                            {
                                "row_id": row_id,
                                "e": e,
                                "a": a,
                                "u": u,
                                "v": v,
                                "z": list(z),
                                "orbit_totals": list(orbit_totals),
                            }
                        )
                else:
                    raise ValueError(f"unexpected 21al status: {status}")

                decision_stream.update(
                    f"{row_id}|{e}|{a}|{u}|{v}|{','.join(map(str, z))}|{status}\n".encode()
                )

        row_summaries.append(
            {
                "row_id": row_id,
                "continuous_kkt_survivors": row_cont,
                "deterministically_sampled_existing_witnesses": row_sampled,
                "composition_sat": row_sat,
                "composition_unsat": row_unsat,
                "composition_unknown": row_unknown,
            }
        )

    if sampled != sat_count + unsat_count + unknown_count:
        raise ValueError("21al sampled decision accounting regression")

    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21al",
        "mode": "EXACT_21AK_AFFINE_2ADIC_CONGRUENCES_PLUS_FIXED_ORBIT_TOTAL_NONNEGATIVE_COMPOSITION_FEASIBILITY",
        "manifest_canonical_sha256": EXPECTED_MANIFEST_SHA256,
        "audited_32_21ac_certificate_sha256": EXPECTED_21AC_CERTIFICATE_SHA256,
        "upstream_32_21ak_certificate_sha256": EXPECTED_21AK_CERTIFICATE_SHA256,
        "upstream_32_21ak_constraint_rows_sha256": EXPECTED_21AK_CONSTRAINT_ROWS_SHA256,
        "z3_version": get_version_string(),
        "interface": {
            "selected_pairing_coordinate_count": len(selected_curve_indices),
            "affine_congruence_count": len(constraint_rows),
            "constraint_moduli": [int(row["modulus"]) for row in constraint_rows],
            "orbit_count": len(orbits),
            "orbit_sizes": list(orbit_sizes),
            "selected_coordinate_counts_by_orbit": list(selected_counts_by_orbit),
            "fully_selected_orbit_ids_0based": list(fully_selected_orbits),
            "logic": (
                "selected pairing coordinates are nonnegative integers satisfying the 14 exact 21ak "
                "affine congruences; their sum equals the fixed orbit total when an orbit is fully "
                "selected and is at most that total otherwise, because omitted nonnegative coordinates "
                "can absorb exactly the remaining orbit mass"
            ),
            "this_is_exact_for_21ak_congruences_plus_orbit_totals": True,
            "this_does_not_enforce_81_additional_rational_pairing_relations": True,
        },
        "sampling": {
            "row_shards": args.row_shards,
            "shard_index": args.shard_index,
            "selected_row_count": len(selected_rows),
            "selected_rows": selected_rows,
            "continuous_kkt_survivors": continuous,
            "sample_modulus": args.sample_modulus,
            "sample_remainder": args.sample_remainder,
            "selection_rule": "sha256(row|e|a|u|v)[0:8]_big_endian mod sample_modulus == sample_remainder",
            "sampled_existing_witnesses": sampled,
            "unique_sampled_projection_states": len(cache),
            "solver_timeout_ms_per_unique_projection_state": args.solver_timeout_ms,
        },
        "result": {
            "sat_existing_witness_projection_states": sat_count,
            "unsat_existing_witness_projection_states": unsat_count,
            "unknown_existing_witness_projection_states": unknown_count,
            "unsat_is_exact_for_21ak_plus_orbit_composition_filter": True,
            "unsat_is_not_yet_a_slice_prune": True,
            "slice_prune_requires_exhausting_all_relevant_rank2_integer_pairs": True,
            "unknown_is_not_unsat": True,
            "minimum_observed_fixed_orbit_total": minimum_orbit_total,
            "maximum_observed_fixed_orbit_total": maximum_orbit_total,
            "decision_stream_sha256": decision_stream.hexdigest(),
            "row_summaries": row_summaries,
            "sat_examples": sat_examples,
            "unsat_examples": unsat_examples,
            "unknown_examples": unknown_examples,
        },
        "interpretation": {
            "nonnegative_orbit_composition_filter_implemented": True,
            "full_affine_pairing_fiber_feasibility_solved": False,
            "self_intersection_threshold_solved_on_fiber": False,
            "next_if_unsat_found": (
                "32-21am: exhaust rank2 integer (u,v) projection states only for UNSAT candidate slices; "
                "promote a prune only when every relevant projection state fails"
            ),
            "next_if_zero_unsat_and_zero_unknown": (
                "32-21am: this pure 2-adic plus orbit-total filter is empirically dominated on the "
                "representative sample; add the 67 independent rational affine-fiber relations before "
                "considering any full 59D affine solver"
            ),
            "next_if_unknown": (
                "decompose the exact small modular-composition solver; UNKNOWN receives no prune credit"
            ),
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "terminal_family_materialization_run": False,
            "59d_cvp_run": False,
            "full_59d_affine_integer_solver_run": False,
            "representative_row_shard_only": True,
            "deterministic_sample_only": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
            "unknown_is_not_unsat": True,
        },
    }
    payload["canonical_sha256_without_this_field"] = csha(payload)
    args.output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
    print(
        json.dumps(
            {
                "verdict": "PASS_STAGE32_21AL_NONNEGATIVE_ORBIT_COMPOSITION_DIAGNOSTIC",
                "sampled": sampled,
                "sat": sat_count,
                "unsat": unsat_count,
                "unknown": unknown_count,
                "canonical_sha256": payload["canonical_sha256_without_this_field"],
            },
            sort_keys=True,
        )
    )


if __name__ == "__main__":
    main()
