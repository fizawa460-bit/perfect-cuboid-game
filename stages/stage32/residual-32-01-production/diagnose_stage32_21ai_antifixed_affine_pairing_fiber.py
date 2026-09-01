#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

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
from hperp_integral_adapter import (
    EXPECTED_PICARD_DETERMINANT,
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)

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


def gf2_rank(m: Matrix) -> int:
    """Exact row rank over F_2 using Python integer bitsets."""
    pivots: dict[int, int] = {}
    rank = 0
    for i in range(m.rows):
        bits = 0
        for j in range(m.cols):
            if int(m[i, j]) & 1:
                bits |= 1 << j
        while bits:
            pivot = bits.bit_length() - 1
            prior = pivots.get(pivot)
            if prior is None:
                pivots[pivot] = bits
                rank += 1
                break
            bits ^= prior
    return rank


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
    # gives a saturated Z-basis K for ker_Z(N) in the last 59 columns.
    C = integer_coordinate_matrix(N, B)
    if B * C != N:
        raise ValueError("N=B*C reconstruction regression")
    C_dm = DomainMatrix.from_Matrix(C).convert_to(ZZ)
    D_dm, S_dm, T_dm = smith_normal_decomp(C_dm)
    if S_dm * C_dm * T_dm != D_dm:
        raise ValueError("fixed-coordinate Smith reconstruction regression")
    D = D_dm.to_Matrix()
    S = S_dm.to_Matrix()
    T = T_dm.to_Matrix()
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
    coords = adapter.class_coordinates_in_retained_basis
    M = pairing * K
    if M.shape != (EXPECTED_KNOWN_CURVE_COUNT, EXPECTED_ANTI_RANK):
        raise ValueError(f"anti-fixed pairing map shape regression: {M.shape}")

    # The retained 64 curves are an integral Picard basis. Therefore their
    # anti-fixed pairing block is exactly G*K, every all140 row is an integral
    # combination of these retained rows, and those 64 rows occur inside M.
    # Hence the row lattice of M equals the row lattice of G*K exactly.
    retained_pairing = gram * K
    if coords * retained_pairing != M:
        raise ValueError("all140 pairing rows are not reconstructed from retained64 rows")
    retained_idx = [label - 1 for label in RETAINED_BASIS_KNOWN_LABELS_1BASED]
    if M.extract(retained_idx, list(range(EXPECTED_ANTI_RANK))) != retained_pairing:
        raise ValueError("retained64 generator block is not embedded identically in all140 pairing rows")

    # No wide HNF/SNF is needed to decide whether the pairing-image lattice is
    # saturated in its rational span. Let R=(G*K)^T : Z^64 -> Z^59.
    #
    # K is a saturated kernel basis obtained from the unimodular Smith-right
    # transform, so K^T is surjective. Since det(G)=-2^28, adj(G) proves that
    # coker(R) is killed by 2^28: for any y choose x with K^T x=y and set
    # z=adj(G)x, then K^T G z=det(G)y. Thus the finite cokernel is 2-primary.
    # It is trivial iff R has full rank mod 2.
    if abs(int(EXPECTED_PICARD_DETERMINANT)) != 1 << 28:
        raise ValueError("Picard determinant lock is no longer 2^28")
    retained_restriction = retained_pairing.T
    mod2_rank = gf2_rank(retained_restriction)
    mod2_defect = EXPECTED_ANTI_RANK - mod2_rank
    if not 0 <= mod2_defect <= EXPECTED_ANTI_RANK:
        raise ValueError("mod2 rank defect regression")
    has_modular_coupling = mod2_defect > 0
    exact_saturation_index_if_trivial = 1 if not has_modular_coupling else None

    # Stabilizer orbits. Any anti-fixed vector has zero total pairing on each
    # orbit because Reynolds averaging kills it.
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

    # The within-orbit difference map is injective on the anti-fixed space:
    # if all differences vanish then pairings are constant on each orbit;
    # zero orbit sums force every constant to vanish; the retained64 basis
    # pairings then vanish, and nondegeneracy of G forces the class to be zero.
    within_orbit_difference_row_count = sum(len(orbit) - 1 for orbit in orbits)
    pairing_rank = EXPECTED_ANTI_RANK
    relation_rank = EXPECTED_KNOWN_CURVE_COUNT - pairing_rank

    cert = {
        "schema": "STAGE32_21AI_ANTIFIXED_AFFINE_PAIRING_FIBER_STRUCTURE_V2_MOD2_GATE",
        "mode": "EXACT_SATURATED_REYNOLDS_ANTIFIXED_PAIRING_LATTICE_WITH_2PRIMARY_COKERNEL_GATE",
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
            "basis_from_smith_right_kernel_columns": True,
            "N_times_kernel_zero": True,
            "phi_times_kernel_zero": True,
        },
        "all140_pairing_image": {
            "shape": [M.rows, M.cols],
            "sha256": csha(matrix_int_list(M)),
            "rank": pairing_rank,
            "left_rational_relation_rank": relation_rank,
            "retained64_generator_block_sha256": csha(matrix_int_list(retained_pairing)),
            "all140_rows_are_integral_combinations_of_retained64_rows": True,
            "retained64_rows_occur_identically_inside_all140": True,
            "all140_row_lattice_equals_retained64_row_lattice": True,
            "wide_hnf_or_snf_run": False,
            "cokernel_annihilator": abs(int(EXPECTED_PICARD_DETERMINANT)),
            "cokernel_annihilator_factorization": "2^28",
            "cokernel_only_2_primary": True,
            "retained_restriction_mod2_rank": mod2_rank,
            "retained_restriction_mod2_rank_defect": mod2_defect,
            "has_nontrivial_modular_coupling": has_modular_coupling,
            "saturation_index_if_mod2_full_rank": exact_saturation_index_if_trivial,
        },
        "stabilizer_orbit_decomposition": {
            "orbit_count": len(orbits),
            "orbit_sizes": sorted(len(o) for o in orbits),
            "orbit_sum_variation_zero_exact": True,
            "orbit_zero_ambient_rank": EXPECTED_KNOWN_CURVE_COUNT - len(orbits),
            "anti_fixed_rational_codimension_inside_orbit_zero_space": (
                EXPECTED_KNOWN_CURVE_COUNT - len(orbits) - pairing_rank
            ),
            "within_orbit_difference_row_count": within_orbit_difference_row_count,
            "within_orbit_difference_rank": EXPECTED_ANTI_RANK,
            "within_orbit_difference_injectivity_proved_without_wide_rank_elimination": True,
            "all_anti_fixed_directions_visible_in_within_orbit_differences": True,
            "projected_orbit_total_map_shape": [orbit_total_map.rows, orbit_total_map.cols],
            "projected_orbit_total_map_rank": int(orbit_total_map.rank()),
            "projected_orbit_total_map_sha256": csha(matrix_int_list(orbit_total_map)),
            "projected_orbit_totals_integral_for_every_fixed_image_basis_generator": True,
        },
        "proof": {
            "retained64_are_integral_picard_basis": True,
            "pairing_matrix_equals_all140_integral_coordinates_times_gram": True,
            "anti_kernel_is_saturated": True,
            "K_transpose_surjective": True,
            "adjugate_argument_kills_pairing_cokernel_by_abs_det_gram": True,
            "abs_det_gram": abs(int(EXPECTED_PICARD_DETERMINANT)),
            "abs_det_gram_is_power_of_two": True,
            "mod2_full_rank_iff_pairing_image_saturated": True,
            "wide_59x64_or_140x59_hnf_snf_required": False,
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
                "derive exact mod-2 affine pairing-image membership constraints, then test them against "
                "nonnegative orbit compositions before any norm search"
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
        "mod2_rank": p["retained_restriction_mod2_rank"],
        "mod2_rank_defect": p["retained_restriction_mod2_rank_defect"],
        "has_nontrivial_modular_coupling": p["has_nontrivial_modular_coupling"],
        "orbit_count": o["orbit_count"],
        "orbit_zero_codimension": o["anti_fixed_rational_codimension_inside_orbit_zero_space"],
        "within_orbit_difference_rank": o["within_orbit_difference_rank"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
