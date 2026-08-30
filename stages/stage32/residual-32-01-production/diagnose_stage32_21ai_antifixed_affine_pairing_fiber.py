#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_decomp, smith_normal_form

from direct_picard_reynolds_lattice_diagnostic import (
    EXPECTED_FIXED_RANK,
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
    load_retained,
)
from direct_picard_reynolds_rank2_integral_projection_bound import build_reynolds_numerator
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_ANTI_RANK = PICARD_RANK - EXPECTED_FIXED_RANK
EXPECTED_ORBIT_COUNT = 14
EXPECTED_KNOWN_CURVE_COUNT = 140


def matrix_int_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def nonzero_smith_diagonal(d: Matrix) -> tuple[int, ...]:
    out = []
    for i in range(min(d.rows, d.cols)):
        v = abs(int(d[i, i]))
        if v:
            out.append(v)
    return tuple(out)


def integer_coordinate_matrix(numerator: Matrix, basis: Matrix) -> Matrix:
    """Coordinates of every numerator column in the exact im(N) Z-basis."""
    if basis.shape != (PICARD_RANK, EXPECTED_FIXED_RANK):
        raise ValueError(f"fixed-image basis shape regression: {basis.shape}")
    row_pivots = tuple(int(i) for i in basis.T.rref()[1])
    if len(row_pivots) != EXPECTED_FIXED_RANK:
        raise ValueError("fixed-image row-pivot regression")
    square = basis[list(row_pivots), :]
    inv_square = square.inv()
    cols = []
    for j in range(numerator.cols):
        rhs = Matrix([numerator[i, j] for i in row_pivots])
        x = inv_square * rhs
        if basis * x != numerator[:, j]:
            raise ValueError(f"fixed-image coordinate reconstruction regression at column {j}")
        if any(v.q != 1 for v in x):
            raise ValueError(f"nonintegral im(N) coordinate at column {j}")
        cols.append(Matrix([int(v) for v in x]))
    return Matrix.hstack(*cols)


def build_diagnostic(marking: dict, bundle: dict) -> dict:
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])

    N, subgroup, action_hashes_sha = build_reynolds_numerator(
        marking, adapter, gram, phi
    )
    B, module_stats = exact_column_lattice_basis_lowrank(N, EXPECTED_FIXED_RANK)
    if N * B != GROUP_ORDER * B:
        raise ValueError("fixed-image basis not Reynolds-fixed")

    # N=B*C with C integral and surjective Z^64 -> Z^5 because B is the
    # exact column-module basis of im(N). Smith on this small-row 5x64 map
    # therefore gives a saturated Z-basis for ker_Z(N) in the last 59 columns.
    C = integer_coordinate_matrix(N, B)
    if B * C != N:
        raise ValueError("N=B*C reconstruction regression")
    D, S, T = smith_normal_decomp(C, domain=ZZ)
    if S * C * T != D:
        raise ValueError("fixed-coordinate Smith reconstruction regression")
    cdiag = nonzero_smith_diagonal(D)
    if cdiag != (1,) * EXPECTED_FIXED_RANK:
        raise ValueError(f"im(N) coordinate map should be surjective, got Smith {cdiag}")
    K = T[:, EXPECTED_FIXED_RANK:]
    if K.shape != (PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError(f"anti-fixed integer kernel shape regression: {K.shape}")
    if C * K != Matrix.zeros(EXPECTED_FIXED_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("C anti-fixed kernel regression")
    if N * K != Matrix.zeros(PICARD_RANK, EXPECTED_ANTI_RANK):
        raise ValueError("N anti-fixed kernel regression")
    if phi * K != Matrix.zeros(3, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed kernel did not lie in slice kernel")

    pairing = adapter.pairing_matrix
    M = pairing * K
    if M.shape != (EXPECTED_KNOWN_CURVE_COUNT, EXPECTED_ANTI_RANK):
        raise ValueError(f"anti-fixed pairing map shape regression: {M.shape}")
    pairing_rank = int(M.rank())
    if pairing_rank != EXPECTED_ANTI_RANK:
        raise ValueError(f"anti-fixed pairing map lost rank: {pairing_rank}")

    # Stabilizer orbits. Any anti-fixed vector has zero total pairing on each
    # orbit because Reynolds averaging kills it. This exposes the fixed orbit
    # totals as exact affine invariants and puts the live variation in the
    # orbit-zero lattice of rank 140-14=126.
    unvisited = set(range(EXPECTED_KNOWN_CURVE_COUNT))
    orbits: list[tuple[int, ...]] = []
    while unvisited:
        seed = min(unvisited)
        orbit = tuple(sorted({g[seed] for g in subgroup}))
        orbits.append(orbit)
        unvisited.difference_update(orbit)
    if len(orbits) != EXPECTED_ORBIT_COUNT:
        raise ValueError(f"stabilizer orbit count regression: {len(orbits)}")

    orbit_sum = Matrix.zeros(EXPECTED_ORBIT_COUNT, EXPECTED_KNOWN_CURVE_COUNT)
    for oi, orbit in enumerate(orbits):
        for idx in orbit:
            orbit_sum[oi, idx] = 1
    if orbit_sum * M != Matrix.zeros(EXPECTED_ORBIT_COUNT, EXPECTED_ANTI_RANK):
        raise ValueError("anti-fixed pairing variation changed a stabilizer orbit total")

    pairing_B = pairing * B
    orbit_total_map_rows = []
    for orbit in orbits:
        seed = orbit[0]
        row = []
        for j in range(EXPECTED_FIXED_RANK):
            numerator = len(orbit) * int(pairing_B[seed, j])
            if numerator % GROUP_ORDER:
                raise ValueError(
                    f"projected orbit total is nonintegral on fixed basis: orbit={orbit}, col={j}"
                )
            row.append(numerator // GROUP_ORDER)
        orbit_total_map_rows.append(row)
    orbit_total_map = Matrix(orbit_total_map_rows)

    # Within-orbit differences remove the 14 fixed totals. Their rank tells us
    # whether all 59 anti-fixed degrees are already visible before any norm
    # inequality is applied.
    diff_rows = []
    for orbit in orbits:
        seed = orbit[0]
        for idx in orbit[1:]:
            diff_rows.append([int(M[idx, j] - M[seed, j]) for j in range(M.cols)])
    diff = Matrix(diff_rows)
    diff_rank = int(diff.rank())

    print(json.dumps({
        "phase": "pairing_image_smith_start",
        "shape": [M.rows, M.cols],
        "rank": pairing_rank,
    }, sort_keys=True), flush=True)
    Msmith = smith_normal_form(M, domain=ZZ)
    pairing_smith = nonzero_smith_diagonal(Msmith)
    print(json.dumps({
        "phase": "pairing_image_smith_complete",
        "nonzero_factor_count": len(pairing_smith),
        "nonunit_factor_count": sum(1 for v in pairing_smith if v != 1),
    }, sort_keys=True), flush=True)
    if len(pairing_smith) != EXPECTED_ANTI_RANK:
        raise ValueError("anti-fixed pairing Smith rank regression")
    saturation_index = math.prod(pairing_smith)

    cert = {
        "schema": "STAGE32_21AI_ANTIFIXED_AFFINE_PAIRING_FIBER_STRUCTURE_V1",
        "mode": "EXACT_SATURATED_REYNOLDS_ANTIFIXED_INTEGER_KERNEL_TO_ALL140_PAIRING_LATTICE",
        "slice_stabilizer_group_order": GROUP_ORDER,
        "picard_rank": PICARD_RANK,
        "fixed_rank": EXPECTED_FIXED_RANK,
        "anti_fixed_integer_rank": EXPECTED_ANTI_RANK,
        "known_curve_count": EXPECTED_KNOWN_CURVE_COUNT,
        "adapter_certificate_sha256": adapter.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_bridge_certificate_sha256": bridge.certificate[
            "canonical_sha256_without_this_field"
        ],
        "reynolds_numerator_sha256": csha(matrix_int_list(N)),
        "action_hashes_sha256": action_hashes_sha,
        "fixed_image_basis_sha256": csha(matrix_int_list(B)),
        "fixed_image_column_module_stats": module_stats,
        "fixed_coordinate_map": {
            "shape": [C.rows, C.cols],
            "sha256": csha(matrix_int_list(C)),
            "smith_nonzero_diagonal": list(cdiag),
            "surjective_to_Z5": True,
        },
        "anti_fixed_integer_kernel": {
            "shape": [K.rows, K.cols],
            "sha256": csha(matrix_int_list(K)),
            "rank": EXPECTED_ANTI_RANK,
            "saturated": True,
            "N_times_kernel_zero": True,
            "phi_times_kernel_zero": True,
        },
        "all140_pairing_image": {
            "shape": [M.rows, M.cols],
            "sha256": csha(matrix_int_list(M)),
            "rank": pairing_rank,
            "left_rational_relation_rank": EXPECTED_KNOWN_CURVE_COUNT - pairing_rank,
            "smith_nonzero_diagonal": list(pairing_smith),
            "nonunit_smith_factor_count": sum(1 for v in pairing_smith if v != 1),
            "maximum_smith_factor": max(pairing_smith),
            "saturation_index_in_rational_span": saturation_index,
            "has_nontrivial_modular_coupling": saturation_index > 1,
        },
        "stabilizer_orbit_decomposition": {
            "orbit_count": len(orbits),
            "orbit_sizes": sorted(len(o) for o in orbits),
            "orbit_sum_variation_zero_exact": True,
            "orbit_zero_ambient_rank": EXPECTED_KNOWN_CURVE_COUNT - len(orbits),
            "anti_fixed_rational_codimension_inside_orbit_zero_space": (
                EXPECTED_KNOWN_CURVE_COUNT - len(orbits) - pairing_rank
            ),
            "within_orbit_difference_row_count": diff.rows,
            "within_orbit_difference_rank": diff_rank,
            "all_anti_fixed_directions_visible_in_within_orbit_differences": (
                diff_rank == EXPECTED_ANTI_RANK
            ),
            "projected_orbit_total_map_shape": [orbit_total_map.rows, orbit_total_map.cols],
            "projected_orbit_total_map_rank": int(orbit_total_map.rank()),
            "projected_orbit_total_map_sha256": csha(matrix_int_list(orbit_total_map)),
            "projected_orbit_totals_integral_for_every_fixed_image_basis_generator": True,
        },
        "interpretation": {
            "historical_direct_integral_coset_bound_equivalent": False,
            "historical_orbit_coordinate_cauchy_bound_equivalent": False,
            "reason": (
                "those historical leaves bound one kernel coordinate at a time around a continuous center; "
                "this leaf identifies the exact simultaneous affine lattice of all 140 pairing deviations "
                "inside a fixed Reynolds fiber"
            ),
            "simultaneous_nonnegative_fiber_feasibility_solved": False,
            "self_intersection_threshold_solved_on_fiber": False,
            "next_if_modular_coupling_nontrivial": (
                "derive a compact exact modular/affine fiber membership filter before any norm search"
            ),
            "next_if_modular_coupling_trivial": (
                "use the 81 exact rational pairing relations and nonnegative orbit-composition constraints; "
                "do not spend a leaf on a modular sieve"
            ),
        },
        "safety": {
            "heavy_run_key_used": False,
            "full178_production_run": False,
            "legacy_prefix_dfs_run": False,
            "59d_cvp_run": False,
            "terminal_family_materialization_run": False,
            "unknown_is_not_unsat": True,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        },
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    return cert


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21ai_picard")
    marking = load_retained(args.marking, "s32_21ai_marking")
    cert = build_diagnostic(marking, bundle)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    p = cert["all140_pairing_image"]
    o = cert["stabilizer_orbit_decomposition"]
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AI_ANTIFIXED_AFFINE_PAIRING_FIBER_STRUCTURE",
        "anti_fixed_integer_rank": cert["anti_fixed_integer_rank"],
        "pairing_image_rank": p["rank"],
        "pairing_relation_rank": p["left_rational_relation_rank"],
        "nonunit_smith_factor_count": p["nonunit_smith_factor_count"],
        "saturation_index": str(p["saturation_index_in_rational_span"]),
        "orbit_count": o["orbit_count"],
        "orbit_zero_codimension": o["anti_fixed_rational_codimension_inside_orbit_zero_space"],
        "within_orbit_difference_rank": o["within_orbit_difference_rank"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
