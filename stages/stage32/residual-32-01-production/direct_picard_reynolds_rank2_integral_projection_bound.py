#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_decomp

from direct_picard_orbit_sum_qp_bound import DirectPicardOrbitSumQPBound
from direct_picard_reynolds_lattice_diagnostic import (
    EXPECTED_FIXED_RANK,
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
    load_retained,
)
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import (
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)
from pairing_prefix_engine import close_permutation_group

EXPECTED_FIXED_SLICE_KERNEL_RANK = 2
EXPECTED_PROJECTION_CLASS_COUNT = 16384
EXPECTED_STABILIZER_ORBIT_COUNT = 14
EXPECTED_DISTINCT_FIXED_PAIRING_ROW_COUNT = 12


def matrix_int_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def build_reynolds_numerator(
    marking: dict,
    adapter: HperpIntegralPairingAdapter,
    gram: Matrix,
    phi: Matrix,
) -> tuple[Matrix, list[tuple[int, ...]], str]:
    coords = adapter.class_coordinates_in_retained_basis
    full_group = close_permutation_group(marking["aut_action"]["permutations_1based"])
    first_half = frozenset(range(46))
    normal = frozenset(range(92))
    exceptional = frozenset(range(92, 140))
    subgroup = [
        g for g in full_group
        if frozenset(g[i] for i in first_half) == first_half
        and frozenset(g[i] for i in normal) == normal
        and frozenset(g[i] for i in exceptional) == exceptional
    ]
    if len(subgroup) != GROUP_ORDER:
        raise ValueError(f"slice stabilizer order regression: {len(subgroup)}")

    N = Matrix.zeros(PICARD_RANK, PICARD_RANK)
    action_hashes: list[str] = []
    for g in subgroup:
        cols = [
            coords[g[label - 1], :].T
            for label in RETAINED_BASIS_KNOWN_LABELS_1BASED
        ]
        T = Matrix.hstack(*cols)
        if T.T * gram * T != gram:
            raise ValueError("slice stabilizer action is not a Picard isometry")
        if phi * T != phi:
            raise ValueError("slice stabilizer action does not preserve phi")
        N += T
        action_hashes.append(csha(matrix_int_list(T)))

    if N * N != GROUP_ORDER * N:
        raise ValueError("Reynolds numerator idempotence regression")
    if N.T * gram != gram * N:
        raise ValueError("Reynolds numerator Gram self-adjointness regression")
    if phi * N != GROUP_ORDER * phi:
        raise ValueError("Reynolds numerator slice preservation regression")
    if int(N.rank()) != EXPECTED_FIXED_RANK:
        raise ValueError(f"Reynolds fixed-rank regression: {N.rank()}")
    return N, subgroup, csha(sorted(action_hashes))


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_reynolds_rank2_picard")
    marking = load_retained(args.marking, "s32_reynolds_rank2_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    orbit_qp = DirectPicardOrbitSumQPBound.from_retained(marking, bundle)
    if not orbit_qp.certificate["proof"]["slice_kernel_strictly_negative_definite"]:
        raise ValueError("upstream strict negative-definiteness certificate regression")

    gram = Matrix(bundle["picard_gram_64x64"])
    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])
    if phi.rank() != 3:
        raise ValueError("slice functional rank regression")

    N, subgroup, action_hashes_sha = build_reynolds_numerator(
        marking, adapter, gram, phi
    )
    B, module_stats = exact_column_lattice_basis_lowrank(N, EXPECTED_FIXED_RANK)
    if B.shape != (PICARD_RANK, EXPECTED_FIXED_RANK):
        raise ValueError(f"fixed image basis shape regression: {B.shape}")
    if N * B != GROUP_ORDER * B:
        raise ValueError("im(N) basis is not Reynolds-fixed")

    # Exact projected integral lattice:
    #   P(Pic_Z) = (1/64) im(N) = {B z / 64 : z in Z^5}.
    # B is a Z-basis of im(N), so z is unique and every z occurs.
    phi_B = phi * B
    if any(int(v) % GROUP_ORDER for v in phi_B):
        raise ValueError("phi(B) is not divisible by Reynolds group order")
    Psi = phi_B.applyfunc(lambda v: int(v) // GROUP_ORDER)
    if Psi.shape != (3, EXPECTED_FIXED_RANK) or int(Psi.rank()) != 3:
        raise ValueError(f"projected slice matrix regression: {Psi.shape}, rank={Psi.rank()}")

    # Tiny Smith decomposition provides an exact affine rank-2 integer solver:
    # S Psi T=D, z=T y, D y=S t. The last two T-columns are ker_Z(Psi).
    D, S, T = smith_normal_decomp(Psi, domain=ZZ)
    if S * Psi * T != D:
        raise ValueError("projected slice Smith decomposition regression")
    if abs(int(S.det())) != 1 or abs(int(T.det())) != 1:
        raise ValueError("projected slice Smith transforms are not unimodular")
    smith_diag = tuple(abs(int(D[i, i])) for i in range(3))
    if any(v == 0 for v in smith_diag):
        raise ValueError(f"projected slice Smith rank regression: {smith_diag}")
    kernel = T[:, 3:]
    if kernel.shape != (EXPECTED_FIXED_RANK, EXPECTED_FIXED_SLICE_KERNEL_RANK):
        raise ValueError(f"projected integer kernel shape regression: {kernel.shape}")
    if Psi * kernel != Matrix.zeros(3, EXPECTED_FIXED_SLICE_KERNEL_RANK):
        raise ValueError("projected integer kernel regression")

    # For p=Bz/64, all140 pairings have numerator pairing_B*z. A nonnegative
    # integral x averages to a nonnegative p. Because p is stabilizer-fixed,
    # the 140 rows are constant on each of the 14 stabilizer orbits. Two orbit
    # pairs collapse further on the fixed subspace, leaving only 12 distinct
    # halfspaces; this is an exact redundancy, not a relaxation.
    H = B.T * gram * B
    pairing_B = adapter.pairing_matrix * B
    row_tuples = [
        tuple(int(pairing_B[i, j]) for j in range(EXPECTED_FIXED_RANK))
        for i in range(pairing_B.rows)
    ]
    distinct_pairing_rows = sorted(set(row_tuples))

    unvisited = set(range(140))
    stabilizer_orbits: list[tuple[int, ...]] = []
    orbit_rows: list[tuple[int, ...]] = []
    while unvisited:
        seed = min(unvisited)
        orbit = tuple(sorted({g[seed] for g in subgroup}))
        base_row = row_tuples[seed]
        if any(row_tuples[i] != base_row for i in orbit):
            raise ValueError("fixed projected pairing is not constant on a stabilizer orbit")
        stabilizer_orbits.append(orbit)
        orbit_rows.append(base_row)
        unvisited.difference_update(orbit)
    if len(stabilizer_orbits) != EXPECTED_STABILIZER_ORBIT_COUNT:
        raise ValueError(f"stabilizer orbit count regression: {len(stabilizer_orbits)}")
    if len(distinct_pairing_rows) != EXPECTED_DISTINCT_FIXED_PAIRING_ROW_COUNT:
        raise ValueError(
            f"distinct fixed pairing halfspace count regression: {len(distinct_pairing_rows)}"
        )
    if set(orbit_rows) != set(distinct_pairing_rows):
        raise ValueError("orbit rows do not cover exactly the distinct fixed halfspaces")

    row_to_orbits: dict[tuple[int, ...], list[int]] = {}
    for orbit_id, row in enumerate(orbit_rows):
        row_to_orbits.setdefault(row, []).append(orbit_id)
    collapsed_orbit_groups = [
        ids for _, ids in sorted(row_to_orbits.items()) if len(ids) > 1
    ]
    if sum(len(ids) - 1 for ids in collapsed_orbit_groups) != (
        EXPECTED_STABILIZER_ORBIT_COUNT - EXPECTED_DISTINCT_FIXED_PAIRING_ROW_COUNT
    ):
        raise ValueError("fixed-halfspace orbit-collapse accounting regression")

    reduced_H = kernel.T * H * kernel
    if reduced_H.shape != (2, 2) or reduced_H != reduced_H.T:
        raise ValueError("rank-2 projected Hessian shape/symmetry regression")
    if not (int(reduced_H[0, 0]) < 0 and int(reduced_H.det()) > 0):
        raise ValueError(f"rank-2 projected Hessian is not negative definite: {reduced_H}")

    # P=N/64 is a Gram-self-adjoint idempotent. Thus x=p+q orthogonally,
    # phi(q)=0, and the locked exact slice-kernel negative-definiteness gives
    # q^2<=0. Therefore x^2<=p^2. Maximizing p^2 over the exact projected
    # rank-2 integral lattice is a safe upper bound; no 59D anti-fixed CVP is
    # required merely for safety.
    objective_denominator = GROUP_ORDER * GROUP_ORDER

    cert = {
        "schema": "STAGE32_RESIDUAL32_01_REYNOLDS_RANK2_INTEGRAL_PROJECTION_BOUND_V2_12_HALFSPACES",
        "mode": "EXACT_INTEGRAL_PROJECTED_LATTICE_PARAMETERIZATION_AND_SAFE_RANK2_SELF_INTERSECTION_UPPER_BOUND",
        "adapter_certificate_sha256": adapter.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_bridge_certificate_sha256": bridge.certificate[
            "canonical_sha256_without_this_field"
        ],
        "orbit_qp_certificate_sha256": orbit_qp.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_stabilizer_group_order": GROUP_ORDER,
        "picard_rank": PICARD_RANK,
        "fixed_rank": EXPECTED_FIXED_RANK,
        "fixed_slice_kernel_rank": EXPECTED_FIXED_SLICE_KERNEL_RANK,
        "projection_class_count_crosscheck": EXPECTED_PROJECTION_CLASS_COUNT,
        "reynolds_numerator_sha256": csha(matrix_int_list(N)),
        "action_hashes_sha256": action_hashes_sha,
        "fixed_image_basis": {
            "shape": [B.rows, B.cols],
            "sha256": csha(matrix_int_list(B)),
            "column_module_stats": module_stats,
        },
        "exact_projected_parameterization": {
            "formula": "p=B*z/64 with z in Z^5",
            "projection_denominator": GROUP_ORDER,
            "surjective_onto_P_of_integral_Picard_lattice": True,
            "injective_in_z": True,
        },
        "projected_slice_system": {
            "coordinates": ["degree", "exceptional_total", "first_normal_half_total"],
            "Psi": matrix_int_list(Psi),
            "Psi_sha256": csha(matrix_int_list(Psi)),
            "smith_diagonal": list(smith_diag),
            "smith_left_unimodular": matrix_int_list(S),
            "smith_right_unimodular": matrix_int_list(T),
            "integer_kernel_basis": matrix_int_list(kernel),
            "integer_kernel_basis_sha256": csha(matrix_int_list(kernel)),
            "solution_rule": "for t=(d,e,a), let u=S*t; require D_ii|u_i (i=0..2), set y_i=u_i/D_ii and y_3,y_4 free integers, then z=T*y",
        },
        "projected_feasibility": {
            "all140_pairing_numerator_matrix_sha256": csha(matrix_int_list(pairing_B)),
            "stabilizer_orbit_count": len(stabilizer_orbits),
            "distinct_fixed_halfspace_count": len(distinct_pairing_rows),
            "distinct_pairing_rows": [list(row) for row in distinct_pairing_rows],
            "stabilizer_orbit_sizes": sorted(len(o) for o in stabilizer_orbits),
            "collapsed_orbit_groups_0based": collapsed_orbit_groups,
            "criterion": "pairing_B*z >= 0; division by 64 is positive and omitted",
            "two_orbit_redundancies_on_fixed_subspace_exact": True,
        },
        "projected_objective": {
            "formula": "p^2=(z^T H z)/4096",
            "denominator": objective_denominator,
            "H": matrix_int_list(H),
            "H_sha256": csha(matrix_int_list(H)),
            "rank2_kernel_H": matrix_int_list(reduced_H),
            "rank2_kernel_H_sha256": csha(matrix_int_list(reduced_H)),
            "rank2_kernel_negative_definite": True,
        },
        "safe_bound_proof": {
            "P_equals_N_over_64": True,
            "P_idempotent": True,
            "P_gram_self_adjoint": True,
            "x_equals_p_plus_q_orthogonal": True,
            "phi_q_equals_zero": True,
            "upstream_slice_kernel_strictly_negative_definite": True,
            "q_square_nonpositive": True,
            "x_square_le_p_square": True,
            "all140_nonnegative_x_implies_all140_nonnegative_p_by_stabilizer_averaging": True,
            "projected_integrality_exact_not_relaxed": True,
            "anti_fixed_59dimensional_cvp_required_for_safety": False,
            "remaining_integer_optimization_dimension_after_slice": 2,
        },
        "next_leaf": "implement exact 2D integer concave-QP evaluator for each (d,e,a) slice using the Smith affine solution and 12 constant fixed-halfspace inequalities; benchmark it against the measured FULL178 52-unit tail before any heavy production re-arm",
        "numerical_row_complete": False,
        "theorem_credit": False,
        "receiver_credit": False,
        "route_credit": False,
        "perfect_cuboid_existence_claim": False,
        "perfect_cuboid_nonexistence_claim": False,
    }
    cert["canonical_sha256_without_this_field"] = csha(cert)
    args.output.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "verdict": "PASS_REYNOLDS_RANK2_INTEGRAL_PROJECTION_BOUND",
        "fixed_rank": EXPECTED_FIXED_RANK,
        "slice_rank": 3,
        "integer_free_rank": EXPECTED_FIXED_SLICE_KERNEL_RANK,
        "projected_slice_smith": list(smith_diag),
        "stabilizer_orbit_count": len(stabilizer_orbits),
        "distinct_fixed_halfspace_count": len(distinct_pairing_rows),
        "rank2_hessian_det": int(reduced_H.det()),
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
