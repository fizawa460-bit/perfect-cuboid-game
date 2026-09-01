#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

from sympy import Matrix, ZZ, diag
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

import diagnose_stage32_21al_nonnegative_orbit_composition as al
from direct_picard_reynolds_lattice_diagnostic import csha

SCHEMA = "STAGE32_21AM_EXACT_RESIDUAL_QUOTIENT_DP_V1"
UPSTREAM_21AL_RUN_ID = 33341871030
UPSTREAM_21AL_ARTIFACT_ID = 9740830620
UPSTREAM_21AL_CANONICAL_SHA256 = "7928a76837c2225505a4dbfe2b0794455b0c5f0410a52afdcf95647ecade45c3"
UPSTREAM_21AL_SAMPLED = 56
UPSTREAM_21AL_SAT = 42
UPSTREAM_21AL_UNSAT = 0
UPSTREAM_21AL_UNKNOWN = 14
RESIDUE_MODULUS = 8

_DECOMP_CACHE: dict[tuple, dict] = {}
_PROOF_ROWS: list[dict] = []


def _add_q(a: tuple[int, ...], b: tuple[int, ...], moduli: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % m for x, y, m in zip(a, b, moduli))


def _decomposition(
    *,
    selected_orbit_ids: tuple[int, ...],
    orbit_sizes: tuple[int, ...],
    constraint_rows: tuple[dict, ...],
    orbit_totals: tuple[int, ...],
) -> dict:
    moduli = tuple(int(row["modulus"]) for row in constraint_rows)
    counts = tuple(
        sum(1 for oid in selected_orbit_ids if oid == target)
        for target in range(al.EXPECTED_ORBIT_COUNT)
    )
    vacuous_orbits = tuple(
        oid
        for oid, (total, count) in enumerate(zip(orbit_totals, counts))
        if int(total) >= 7 * int(count)
    )
    key = (selected_orbit_ids, orbit_sizes, moduli, vacuous_orbits, csha(list(constraint_rows)))
    cached = _DECOMP_CACHE.get(key)
    if cached is not None:
        return cached

    A = Matrix(
        [
            [int(row["selected_pairing_coefficients"][j]) for j in range(al.EXPECTED_SELECTED_PAIRING_COUNT)]
            for row in constraint_rows
        ]
    )
    vacuous_set = set(vacuous_orbits)
    vacuous_columns = tuple(j for j, oid in enumerate(selected_orbit_ids) if int(oid) in vacuous_set)
    modulus_lattice = diag(*moduli)
    H = A.extract(list(range(len(constraint_rows))), list(vacuous_columns)).row_join(modulus_lattice)
    Hdm = DomainMatrix.from_Matrix(H).convert_to(ZZ)
    Ddm, Udm, Vdm = smith_normal_decomp(Hdm)
    if Udm * Hdm * Vdm != Ddm:
        raise ValueError("residual quotient Smith reconstruction regression")
    D = Ddm.to_Matrix()
    U = Udm.to_Matrix()
    V = Vdm.to_Matrix()
    smith_diagonal = tuple(abs(int(D[i, i])) for i in range(len(constraint_rows)))
    if any(v == 0 for v in smith_diagonal):
        raise ValueError("residual quotient lattice lost full rank")
    nonunit_indices = tuple(i for i, d in enumerate(smith_diagonal) if d != 1)
    quotient_moduli = tuple(smith_diagonal[i] for i in nonunit_indices)
    quotient_order = 1
    for d in quotient_moduli:
        quotient_order *= d

    cached = {
        "A": A,
        "H": H,
        "D": D,
        "U": U,
        "V": V,
        "smith_diagonal": smith_diagonal,
        "nonunit_indices": nonunit_indices,
        "quotient_moduli": quotient_moduli,
        "quotient_order": quotient_order,
        "vacuous_orbits": vacuous_orbits,
        "vacuous_columns": vacuous_columns,
        "counts": counts,
        "moduli": moduli,
        "H_sha256": csha([[int(H[i, j]) for j in range(H.cols)] for i in range(H.rows)]),
        "U_sha256": csha([[int(U[i, j]) for j in range(U.cols)] for i in range(U.rows)]),
    }
    _DECOMP_CACHE[key] = cached
    return cached


def solve_quotient_dp(
    *,
    z: tuple[int, ...],
    orbit_totals: tuple[int, ...],
    selected_curve_indices: tuple[int, ...],
    selected_orbit_ids: tuple[int, ...],
    orbit_sizes: tuple[int, ...],
    constraint_rows: tuple[dict, ...],
    timeout_ms: int,
) -> tuple[str, tuple[int, ...] | None]:
    del timeout_ms  # deterministic finite algorithm; no solver timeout exists here.
    if len(selected_curve_indices) != al.EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("selected pairing coordinate count regression")
    if len(selected_orbit_ids) != al.EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("selected orbit-id count regression")
    if len(orbit_totals) != al.EXPECTED_ORBIT_COUNT:
        raise ValueError("orbit total count regression")

    dec = _decomposition(
        selected_orbit_ids=selected_orbit_ids,
        orbit_sizes=orbit_sizes,
        constraint_rows=constraint_rows,
        orbit_totals=orbit_totals,
    )
    A: Matrix = dec["A"]
    U: Matrix = dec["U"]
    V: Matrix = dec["V"]
    smith_diagonal: tuple[int, ...] = dec["smith_diagonal"]
    nonunit_indices: tuple[int, ...] = dec["nonunit_indices"]
    quotient_moduli: tuple[int, ...] = dec["quotient_moduli"]
    vacuous_orbits = set(dec["vacuous_orbits"])
    vacuous_columns: tuple[int, ...] = dec["vacuous_columns"]

    b = Matrix(
        [
            sum(
                int(row["projection_z_offset_coefficients"][k]) * int(z[k])
                for k in range(len(z))
            )
            for row in constraint_rows
        ]
    )
    Ub = U * b
    target_q = tuple(
        int(Ub[i]) % smith_diagonal[i]
        for i in nonunit_indices
    )

    effects: dict[int, tuple[int, ...]] = {}
    for j in range(al.EXPECTED_SELECTED_PAIRING_COUNT):
        Ucol = U * A[:, j]
        effects[j] = tuple(
            int(Ucol[i]) % smith_diagonal[i]
            for i in nonunit_indices
        )

    # Only non-vacuous orbits need explicit bounded search.  For each such
    # orbit retain the minimum selected-coordinate sum that achieves each tiny
    # residual-quotient element.  The largest quotient observed by this
    # algorithm is a structural diagnostic, not an assumed bound.
    orbit_options: list[tuple[int, dict[tuple[int, ...], tuple[int, dict[int, int]]]]] = []
    zero_q = tuple(0 for _ in quotient_moduli)
    for oid in range(al.EXPECTED_ORBIT_COUNT):
        if oid in vacuous_orbits:
            continue
        positions = [j for j, x in enumerate(selected_orbit_ids) if int(x) == oid]
        if not positions:
            continue
        dp: dict[tuple[int, ...], tuple[int, dict[int, int]]] = {zero_q: (0, {})}
        for j in positions:
            nxt: dict[tuple[int, ...], tuple[int, dict[int, int]]] = {}
            for q, (cost, assignment) in dp.items():
                for value in range(8):
                    contribution = tuple(
                        (value * x) % m
                        for x, m in zip(effects[j], quotient_moduli)
                    )
                    q2 = _add_q(q, contribution, quotient_moduli)
                    cost2 = cost + value
                    old = nxt.get(q2)
                    if old is None or cost2 < old[0]:
                        a2 = dict(assignment)
                        a2[j] = value
                        nxt[q2] = (cost2, a2)
            dp = nxt
        limit = int(orbit_totals[oid])
        allowed = {q: pair for q, pair in dp.items() if pair[0] <= limit}
        orbit_options.append((oid, allowed))

    combined: dict[tuple[int, ...], dict[int, int]] = {zero_q: {}}
    for oid, options in orbit_options:
        nxt: dict[tuple[int, ...], dict[int, int]] = {}
        for q, assignment in combined.items():
            for qo, (_, orbit_assignment) in options.items():
                q2 = _add_q(q, qo, quotient_moduli)
                if q2 not in nxt:
                    a2 = dict(assignment)
                    a2.update(orbit_assignment)
                    nxt[q2] = a2
        combined = nxt

    if target_q not in combined:
        _PROOF_ROWS.append(
            {
                "status": "UNSAT",
                "vacuous_orbits": sorted(vacuous_orbits),
                "residual_quotient_moduli": list(quotient_moduli),
                "residual_quotient_order": dec["quotient_order"],
                "target_q": list(target_q),
                "reachable_q_count": len(combined),
                "H_sha256": dec["H_sha256"],
                "U_sha256": dec["U_sha256"],
            }
        )
        return "UNSAT", None

    witness = [0] * al.EXPECTED_SELECTED_PAIRING_COUNT
    for j, value in combined[target_q].items():
        witness[j] = int(value)

    residual = b - A * Matrix(witness)
    Ures = U * residual
    y = Matrix.zeros(V.rows, 1)
    for i, d in enumerate(smith_diagonal):
        value = int(Ures[i])
        if value % d:
            raise ValueError("DP target did not land in residual Smith lattice")
        y[i] = value // d
    coeff = V * y
    for pos, j in enumerate(vacuous_columns):
        witness[j] = int(coeff[pos]) % RESIDUE_MODULUS

    # Independent exact witness verification in the original 21al interface.
    for oid in range(al.EXPECTED_ORBIT_COUNT):
        subtotal = sum(
            witness[j]
            for j, x in enumerate(selected_orbit_ids)
            if int(x) == oid
        )
        if subtotal > int(orbit_totals[oid]):
            raise ValueError("reconstructed witness exceeded orbit total")
    for row in constraint_rows:
        modulus = int(row["modulus"])
        lhs = sum(
            int(row["selected_pairing_coefficients"][j]) * witness[j]
            for j in range(al.EXPECTED_SELECTED_PAIRING_COUNT)
        )
        offset = sum(
            int(row["projection_z_offset_coefficients"][k]) * int(z[k])
            for k in range(len(z))
        )
        if (lhs - offset) % modulus:
            raise ValueError("reconstructed witness violated affine congruence")

    _PROOF_ROWS.append(
        {
            "status": "SAT",
            "vacuous_orbits": sorted(vacuous_orbits),
            "residual_quotient_moduli": list(quotient_moduli),
            "residual_quotient_order": dec["quotient_order"],
            "target_q": list(target_q),
            "reachable_q_count": len(combined),
            "H_sha256": dec["H_sha256"],
            "U_sha256": dec["U_sha256"],
            "witness_sha256": csha(witness),
        }
    )
    return "SAT", tuple(witness)


def run_recomputed_al(args: argparse.Namespace, temp_output: Path) -> dict:
    original_solver = al.solve_selected_composition
    original_argv = sys.argv
    _PROOF_ROWS.clear()
    al.solve_selected_composition = solve_quotient_dp
    sys.argv = [
        "diagnose_stage32_21al_nonnegative_orbit_composition.py",
        "--manifest", str(args.manifest),
        "--retained", str(args.retained),
        "--marking", str(args.marking),
        "--row-shards", str(args.row_shards),
        "--shard-index", str(args.shard_index),
        "--sample-modulus", str(args.sample_modulus),
        "--sample-remainder", str(args.sample_remainder),
        "--solver-timeout-ms", "1",
        "--example-limit", str(args.example_limit),
        "--output", str(temp_output),
    ]
    try:
        al.main()
    finally:
        al.solve_selected_composition = original_solver
        sys.argv = original_argv
    return json.loads(temp_output.read_text())


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
    ap.add_argument("--example-limit", type=int, default=24)
    args = ap.parse_args()

    with tempfile.TemporaryDirectory(prefix="stage32-21am-qdp-") as td:
        recomputed = run_recomputed_al(args, Path(td) / "recomputed-21al.json")

    result = recomputed["result"]
    sampling = recomputed["sampling"]
    if sampling["sampled_continuous_kkt_survivors"] != UPSTREAM_21AL_SAMPLED:
        raise ValueError("representative sample population changed")
    if result["unknown_existing_witness_projection_states"] != 0:
        raise ValueError("deterministic quotient DP produced UNKNOWN")
    if result["sat_existing_witness_projection_states"] + result["unsat_existing_witness_projection_states"] != UPSTREAM_21AL_SAMPLED:
        raise ValueError("deterministic quotient DP accounting regression")
    if len(_PROOF_ROWS) != sampling["unique_sampled_projection_states"]:
        raise ValueError("proof-row count does not match unique projection states")

    max_quotient_order = max(int(row["residual_quotient_order"]) for row in _PROOF_ROWS)
    proof_stream_sha256 = csha(_PROOF_ROWS)
    zero_unsat = result["unsat_existing_witness_projection_states"] == 0
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21am",
        "mode": "EXACT_SMITH_RESIDUAL_QUOTIENT_PLUS_MINCOST_ORBIT_DP",
        "source_unknown_checkpoint": {
            "run_id": UPSTREAM_21AL_RUN_ID,
            "artifact_id": UPSTREAM_21AL_ARTIFACT_ID,
            "canonical_sha256": UPSTREAM_21AL_CANONICAL_SHA256,
            "sampled_states": UPSTREAM_21AL_SAMPLED,
            "sat": UPSTREAM_21AL_SAT,
            "unsat": UPSTREAM_21AL_UNSAT,
            "unknown": UPSTREAM_21AL_UNKNOWN,
        },
        "algorithm": {
            "canonical_residue_modulus": RESIDUE_MODULUS,
            "vacuous_orbit_rule": "fixed_orbit_total >= 7 * selected_coordinate_count",
            "vacuous_coordinates_generate_residual_lattice_with_modulus_columns": True,
            "residual_lattice_smith_reconstruction_exact": True,
            "nonvacuous_orbits_searched_by_minimum_sum_per_residual_quotient_element": True,
            "vacuous_integer_coefficients_reduced_mod8_after_smith_backsolve": True,
            "reduction_preserves_all_mod2_mod4_mod8_constraints": True,
            "vacuous_orbit_upper_bounds_preserved_after_mod8_reduction": True,
            "maximum_observed_residual_quotient_order": max_quotient_order,
            "generic_smt_used": False,
            "timeout_or_unknown_state_possible": False,
        },
        "representative_result": {
            "sampled_states": sampling["sampled_continuous_kkt_survivors"],
            "sat": result["sat_existing_witness_projection_states"],
            "unsat": result["unsat_existing_witness_projection_states"],
            "unknown": result["unknown_existing_witness_projection_states"],
            "zero_unsat": zero_unsat,
            "decision_stream_sha256": result["decision_stream_sha256"],
            "proof_stream_sha256": proof_stream_sha256,
            "recomputed_21al_payload_sha256": recomputed["canonical_sha256_without_this_field"],
            "proof_rows": _PROOF_ROWS,
        },
        "interpretation": {
            "pure_2adic_plus_orbit_total_filter_has_observed_pruning_opportunity": not zero_unsat,
            "full178_numerical_credit": False,
            "slice_prune_credit": False,
            "full_affine_pairing_fiber_feasibility_solved": False,
            "next_if_zero_unsat": (
                "32-21an: add the 67 independent rational affine-pairing relations beyond the 14 orbit sums; "
                "use them to reconstruct/enforce all 140 nonnegative pairings before any norm search"
            ),
            "next_if_unsat_found": (
                "32-21an: exhaust all relevant rank2 integer (u,v) projection states only for candidate slices before any prune promotion"
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
            "deterministic_hash_sample_only": True,
            "unknown_is_not_unsat": True,
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
        "verdict": "PASS_STAGE32_21AM_EXACT_RESIDUAL_QUOTIENT_DP",
        "sampled": payload["representative_result"]["sampled_states"],
        "sat": payload["representative_result"]["sat"],
        "unsat": payload["representative_result"]["unsat"],
        "unknown": payload["representative_result"]["unknown"],
        "max_residual_quotient_order": max_quotient_order,
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
