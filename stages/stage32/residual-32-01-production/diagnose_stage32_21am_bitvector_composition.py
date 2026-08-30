#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
import tempfile
from pathlib import Path

from z3 import BitVec, BitVecVal, Extract, Solver, ULE, ZeroExt, get_version_string, sat, unknown, unsat

import diagnose_stage32_21al_nonnegative_orbit_composition as al
from direct_picard_reynolds_lattice_diagnostic import csha

SCHEMA = "STAGE32_21AM_BITVECTOR_RESIDUE_ORBIT_COMPOSITION_V1"
UPSTREAM_21AL_RUN_ID = 33341871030
UPSTREAM_21AL_ARTIFACT_ID = 9740830620
UPSTREAM_21AL_CANONICAL_SHA256 = "7928a76837c2225505a4dbfe2b0794455b0c5f0410a52afdcf95647ecade45c3"
UPSTREAM_21AL_SAMPLED = 56
RESIDUE_MODULUS = 8
RESIDUE_BITS = 3
ORBIT_SUM_BITS = 7  # max selected subtotal is 10*7=70 < 2^7


def solve_bitvector_composition(
    *,
    z: tuple[int, ...],
    orbit_totals: tuple[int, ...],
    selected_curve_indices: tuple[int, ...],
    selected_orbit_ids: tuple[int, ...],
    orbit_sizes: tuple[int, ...],
    constraint_rows: tuple[dict, ...],
    timeout_ms: int,
) -> tuple[str, tuple[int, ...] | None]:
    if len(selected_curve_indices) != al.EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("selected pairing coordinate count regression")
    if len(selected_orbit_ids) != al.EXPECTED_SELECTED_PAIRING_COUNT:
        raise ValueError("selected orbit-id count regression")
    if len(orbit_totals) != al.EXPECTED_ORBIT_COUNT:
        raise ValueError("orbit total count regression")

    moduli = tuple(int(row["modulus"]) for row in constraint_rows)
    if not moduli or max(moduli) != RESIDUE_MODULUS:
        raise ValueError(f"unexpected current maximum modulus: {moduli}")
    if any(RESIDUE_MODULUS % modulus for modulus in moduli):
        raise ValueError(f"constraint modulus does not divide 8: {moduli}")

    selected_positions_by_orbit: list[list[int]] = [[] for _ in range(al.EXPECTED_ORBIT_COUNT)]
    for j, oid in enumerate(selected_orbit_ids):
        selected_positions_by_orbit[int(oid)].append(j)
    fully_selected = tuple(
        oid for oid, positions in enumerate(selected_positions_by_orbit)
        if len(positions) == int(orbit_sizes[oid])
    )
    if fully_selected:
        raise ValueError(
            "mod8 least-residue reduction is not equality-preserving for fully selected orbits: "
            f"{fully_selected}"
        )

    # Three bits represent exactly the canonical residues 0,...,7.  This is
    # equivalent to the unbounded 21al CSP because every 21ak modulus divides
    # 8 and every current orbit condition is only an upper bound.
    r = [BitVec(f"r_{j}", RESIDUE_BITS) for j in range(al.EXPECTED_SELECTED_PAIRING_COUNT)]
    solver = Solver()
    solver.set(timeout=timeout_ms)

    for oid, positions in enumerate(selected_positions_by_orbit):
        total = int(orbit_totals[oid])
        if total < 0:
            raise ValueError("negative fixed orbit total reached 21am")
        max_possible = 7 * len(positions)
        if total >= max_possible or not positions:
            continue
        subtotal = BitVecVal(0, ORBIT_SUM_BITS)
        for j in positions:
            subtotal = subtotal + ZeroExt(ORBIT_SUM_BITS - RESIDUE_BITS, r[j])
        # No wrap is possible because max_possible <= 70 < 128.
        solver.add(ULE(subtotal, BitVecVal(total, ORBIT_SUM_BITS)))

    for row in constraint_rows:
        modulus = int(row["modulus"])
        coeffs = tuple(int(v) for v in row["selected_pairing_coefficients"])
        offsets = tuple(int(v) for v in row["projection_z_offset_coefficients"])
        if len(coeffs) != al.EXPECTED_SELECTED_PAIRING_COUNT or len(offsets) != len(z):
            raise ValueError("21ak affine constraint shape regression")
        lhs = BitVecVal(0, RESIDUE_BITS)
        for j, coeff in enumerate(coeffs):
            lhs = lhs + BitVecVal(coeff % RESIDUE_MODULUS, RESIDUE_BITS) * r[j]
        offset = sum(offsets[k] * int(z[k]) for k in range(len(z)))
        if modulus == 8:
            solver.add(lhs == BitVecVal(offset % 8, RESIDUE_BITS))
        elif modulus == 4:
            solver.add(Extract(1, 0, lhs) == BitVecVal(offset % 4, 2))
        elif modulus == 2:
            solver.add(Extract(0, 0, lhs) == BitVecVal(offset % 2, 1))
        else:
            raise ValueError(f"unexpected 21ak modulus: {modulus}")

    result = solver.check()
    if result == unknown:
        return "UNKNOWN", None
    if result == unsat:
        return "UNSAT", None
    if result != sat:
        raise ValueError(f"unexpected z3 result: {result}")

    model = solver.model()
    witness = tuple(int(model.eval(var, model_completion=True).as_long()) for var in r)
    if any(value < 0 or value >= RESIDUE_MODULUS for value in witness):
        raise ValueError("bitvector witness escaped canonical residue range")

    for oid, positions in enumerate(selected_positions_by_orbit):
        if sum(witness[j] for j in positions) > int(orbit_totals[oid]):
            raise ValueError("bitvector witness exceeded partial-orbit total")
    for row in constraint_rows:
        modulus = int(row["modulus"])
        lhs_int = sum(
            int(row["selected_pairing_coefficients"][j]) * witness[j]
            for j in range(al.EXPECTED_SELECTED_PAIRING_COUNT)
        )
        offset = sum(
            int(row["projection_z_offset_coefficients"][k]) * int(z[k])
            for k in range(len(z))
        )
        if (lhs_int - offset) % modulus:
            raise ValueError("bitvector witness violated 21ak affine congruence")
    return "SAT", witness


def run_recomputed_al(args: argparse.Namespace, temp_output: Path) -> dict:
    original_solver = al.solve_selected_composition
    original_argv = sys.argv
    al.solve_selected_composition = solve_bitvector_composition
    sys.argv = [
        "diagnose_stage32_21al_nonnegative_orbit_composition.py",
        "--manifest", str(args.manifest),
        "--retained", str(args.retained),
        "--marking", str(args.marking),
        "--row-shards", str(args.row_shards),
        "--shard-index", str(args.shard_index),
        "--sample-modulus", str(args.sample_modulus),
        "--sample-remainder", str(args.sample_remainder),
        "--solver-timeout-ms", str(args.solver_timeout_ms),
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
    ap.add_argument("--solver-timeout-ms", type=int, default=30000)
    ap.add_argument("--example-limit", type=int, default=24)
    args = ap.parse_args()

    with tempfile.TemporaryDirectory(prefix="stage32-21am-bv-") as td:
        recomputed = run_recomputed_al(args, Path(td) / "recomputed-21al.json")

    interface = recomputed["interface"]
    sampling = recomputed["sampling"]
    result = recomputed["result"]
    if interface["fully_selected_orbit_ids_0based"] != []:
        raise ValueError("current interface unexpectedly acquired a fully selected orbit")
    if sampling["sampled_continuous_kkt_survivors"] != UPSTREAM_21AL_SAMPLED:
        raise ValueError("representative sample population changed")
    if result["unknown_existing_witness_projection_states"] != 0:
        raise ValueError("bitvector solver returned UNKNOWN; no 21am PASS is allowed")
    if (
        result["sat_existing_witness_projection_states"]
        + result["unsat_existing_witness_projection_states"]
        != UPSTREAM_21AL_SAMPLED
    ):
        raise ValueError("bitvector decision accounting regression")

    zero_unsat = result["unsat_existing_witness_projection_states"] == 0
    payload = {
        "schema": SCHEMA,
        "stage": 32,
        "leaf": "32-21am",
        "mode": "PURE_QF_BV_EXACT_MOD8_REDUCTION_OF_21AL_COMPOSITION_CSP",
        "source_unknown_checkpoint": {
            "run_id": UPSTREAM_21AL_RUN_ID,
            "artifact_id": UPSTREAM_21AL_ARTIFACT_ID,
            "canonical_sha256": UPSTREAM_21AL_CANONICAL_SHA256,
            "sampled_states": UPSTREAM_21AL_SAMPLED,
            "sat": 42,
            "unsat": 0,
            "unknown": 14,
        },
        "recomputed_interface_locks": {
            "manifest_canonical_sha256": recomputed["manifest_canonical_sha256"],
            "audited_32_21ac_certificate_sha256": recomputed["audited_32_21ac_certificate_sha256"],
            "upstream_32_21ak_certificate_sha256": recomputed["upstream_32_21ak_certificate_sha256"],
            "upstream_32_21ak_constraint_rows_sha256": recomputed["upstream_32_21ak_constraint_rows_sha256"],
            "fully_selected_orbit_ids_0based": interface["fully_selected_orbit_ids_0based"],
            "constraint_moduli": interface["constraint_moduli"],
            "selected_pairing_coordinate_count": interface["selected_pairing_coordinate_count"],
        },
        "equivalence_proof": {
            "canonical_residue_modulus": RESIDUE_MODULUS,
            "all_constraint_moduli_divide_8": all(
                RESIDUE_MODULUS % int(m) == 0 for m in interface["constraint_moduli"]
            ),
            "no_fully_selected_orbit_equalities": True,
            "forward_map": "r_j=s_j mod 8 as least nonnegative residue",
            "congruences_preserved": True,
            "partial_orbit_upper_bounds_preserved": True,
            "reverse_map": "bounded residue witness is itself a nonnegative integer witness",
            "bounded_and_unbounded_feasibility_equivalent": True,
        },
        "solver": {
            "z3_version": get_version_string(),
            "logic": "QF_BV",
            "variables": interface["selected_pairing_coordinate_count"],
            "bits_per_variable": RESIDUE_BITS,
            "variable_domain": "0..7 by representation",
            "orbit_sum_bits": ORBIT_SUM_BITS,
            "affine_congruences": len(interface["constraint_moduli"]),
            "per_state_timeout_ms_fail_closed": args.solver_timeout_ms,
        },
        "representative_result": {
            "sampled_states": sampling["sampled_continuous_kkt_survivors"],
            "sat": result["sat_existing_witness_projection_states"],
            "unsat": result["unsat_existing_witness_projection_states"],
            "unknown": result["unknown_existing_witness_projection_states"],
            "decision_stream_sha256": result["decision_stream_sha256"],
            "recomputed_21al_payload_sha256": recomputed["canonical_sha256_without_this_field"],
            "zero_unsat": zero_unsat,
        },
        "interpretation": {
            "representative_filter_has_observed_pruning_opportunity": not zero_unsat,
            "full178_numerical_credit": False,
            "slice_prune_credit": False,
            "full_affine_pairing_fiber_feasibility_solved": False,
            "next_if_zero_unsat": (
                "32-21an: add the 67 independent rational affine-pairing relations left after "
                "the 14 orbit-sum relations, before considering any full 59D affine solver"
            ),
            "next_if_unsat_found": (
                "32-21an: exhaust all relevant rank2 integer (u,v) projection states only for "
                "candidate slices before promoting any prune"
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
        "verdict": "PASS_STAGE32_21AM_EXACT_BITVECTOR_COMPOSITION",
        "sampled": payload["representative_result"]["sampled_states"],
        "sat": payload["representative_result"]["sat"],
        "unsat": payload["representative_result"]["unsat"],
        "unknown": payload["representative_result"]["unknown"],
        "canonical_sha256": payload["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
