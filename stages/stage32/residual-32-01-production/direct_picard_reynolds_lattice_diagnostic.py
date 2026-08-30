#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

from sympy import Matrix, Rational, ZZ, eye, ilcm
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import (
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)
from pairing_prefix_engine import close_permutation_group

GROUP_ORDER = 64
PICARD_RANK = 64
EXPECTED_FIXED_RANK = 5


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def load_retained(path: Path, name: str) -> dict:
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot import {path}")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.load()


def nonzero_smith_diagonal(d: Matrix) -> tuple[int, ...]:
    vals = []
    for i in range(min(d.rows, d.cols)):
        v = abs(int(d[i, i]))
        if v:
            vals.append(v)
    return tuple(vals)


def _coordinate_solver(basis: Matrix) -> tuple[tuple[int, ...], Matrix]:
    rank = basis.cols
    row_pivots = tuple(int(i) for i in basis.T.rref()[1])
    if len(row_pivots) != rank:
        raise ValueError(f"basis row-pivot regression: {len(row_pivots)} != {rank}")
    square = basis[list(row_pivots), :]
    return row_pivots, square.inv()


def exact_column_lattice_basis_lowrank(
    m: Matrix, expected_rank: int
) -> tuple[Matrix, dict]:
    """Build a Z-basis of the column module using only rank-sized HNFs.

    Start from any Q-independent set of `expected_rank` source columns. If B is
    the current integral basis and a new source column is v=B*x with rational
    x, write d*x=a in Z^r. The enlarged coordinate lattice is

        Z^r + Z*x = (1/d) (d Z^r + Z*a).

    A column HNF of the tiny r x (r+1) matrix [d I | a] is therefore an exact
    basis of the enlarged coordinate lattice. Multiplying B by H/d gives the
    new integral basis. Repeating over all source columns yields exactly im(m)
    without ever computing HNF/SNF on the original wide matrix.
    """
    pivot_cols = tuple(int(i) for i in m.rref()[1])
    if len(pivot_cols) != expected_rank:
        raise ValueError(
            f"column rank regression: pivots={len(pivot_cols)} expected={expected_rank}"
        )
    basis = m[:, list(pivot_cols)]
    row_pivots, inv_square = _coordinate_solver(basis)
    update_count = 0
    coordinate_denominators: list[int] = []

    for j in range(m.cols):
        v = m[:, j]
        rhs = Matrix([v[i, 0] for i in row_pivots])
        x = inv_square * rhs
        if basis * x != v:
            raise ValueError(f"coordinate reconstruction regression at column {j}")
        d = 1
        for value in x:
            d = ilcm(d, int(value.q))
        coordinate_denominators.append(d)
        if d == 1:
            continue

        a = Matrix([int(value * d) for value in x])
        tiny = (d * eye(expected_rank)).row_join(a)
        h = hermite_normal_form(tiny)
        if h.shape != (expected_rank, expected_rank):
            raise ValueError(f"tiny HNF shape regression: {h.shape}")
        transform = h.applyfunc(lambda z: Rational(int(z), d))
        enlarged = basis * transform
        if any(value.q != 1 for value in enlarged):
            raise ValueError(f"nonintegral enlarged basis at source column {j}")
        basis = enlarged.applyfunc(lambda z: int(z))
        update_count += 1
        row_pivots, inv_square = _coordinate_solver(basis)

    # Final exact membership check: every source column must have integral
    # coordinates in the resulting basis.
    row_pivots, inv_square = _coordinate_solver(basis)
    for j in range(m.cols):
        v = m[:, j]
        rhs = Matrix([v[i, 0] for i in row_pivots])
        x = inv_square * rhs
        if basis * x != v or any(value.q != 1 for value in x):
            raise ValueError(f"final integral column-module membership regression at {j}")

    stats = {
        "pivot_source_columns_0based": list(pivot_cols),
        "source_column_count": m.cols,
        "basis_update_count": update_count,
        "maximum_coordinate_denominator_seen": max(coordinate_denominators, default=1),
        "coordinate_denominators_sha256": csha(coordinate_denominators),
    }
    return basis, stats


def smith_nonzero_diagonal_via_lowrank_column_module(
    m: Matrix, expected_rank: int
) -> tuple[tuple[int, ...], Matrix, dict]:
    basis, stats = exact_column_lattice_basis_lowrank(m, expected_rank)
    d = smith_normal_form(basis, domain=ZZ)
    return nonzero_smith_diagonal(d), basis, stats


def lowrank_smith_selftest() -> None:
    toy = Matrix([
        [2, 0, 2, 4],
        [0, 4, 4, 8],
        [2, 4, 6, 12],
        [0, 0, 0, 0],
    ])
    direct = nonzero_smith_diagonal(smith_normal_form(toy, domain=ZZ))
    compressed, basis, _ = smith_nonzero_diagonal_via_lowrank_column_module(
        toy, int(toy.rank())
    )
    if compressed != direct or basis.cols != toy.rank():
        raise ValueError(
            f"lowrank column-module Smith regression: direct={direct}, compressed={compressed}, bshape={basis.shape}"
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    lowrank_smith_selftest()
    bundle = load_retained(args.retained, "s32_reynolds_lattice_picard")
    marking = load_retained(args.marking, "s32_reynolds_lattice_marking")
    adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
    bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
    gram = Matrix(bundle["picard_gram_64x64"])
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

    phi = Matrix([
        list(bridge.degree_functional),
        list(bridge.exceptional_mass_functional),
        list(bridge.first_normal_half_functional),
    ])

    N = Matrix.zeros(PICARD_RANK, PICARD_RANK)
    action_hashes = []
    for g in subgroup:
        cols = []
        for basis_label in RETAINED_BASIS_KNOWN_LABELS_1BASED:
            cols.append(coords[g[basis_label - 1], :].T)
        T = Matrix.hstack(*cols)
        if T.T * gram * T != gram:
            raise ValueError("slice stabilizer action is not a Picard isometry")
        if phi * T != phi:
            raise ValueError("slice stabilizer action does not preserve phi")
        N += T
        action_hashes.append(csha([[int(T[i,j]) for j in range(64)] for i in range(64)]))

    if N * N != GROUP_ORDER * N:
        raise ValueError("Reynolds numerator idempotence regression")
    if N.T * gram != gram * N:
        raise ValueError("Reynolds numerator Gram self-adjointness regression")
    if phi * N != GROUP_ORDER * phi:
        raise ValueError("Reynolds numerator slice preservation regression")
    fixed_rank = int(N.rank())
    if fixed_rank != EXPECTED_FIXED_RANK:
        raise ValueError(f"fixed rank regression: {fixed_rank}")

    print(json.dumps({
        "phase": "fixed_lowrank_column_module_start",
        "ambient_shape": [N.rows, N.cols],
        "exact_rank": fixed_rank,
    }, sort_keys=True), flush=True)
    fixed_smith, fixed_basis, module_stats = smith_nonzero_diagonal_via_lowrank_column_module(
        N, fixed_rank
    )
    print(json.dumps({
        "phase": "fixed_lowrank_column_module_complete",
        "compressed_shape": [fixed_basis.rows, fixed_basis.cols],
        "basis_update_count": module_stats["basis_update_count"],
        "fixed_smith": list(fixed_smith),
    }, sort_keys=True), flush=True)
    if fixed_basis.rows != PICARD_RANK or fixed_basis.cols != fixed_rank:
        raise ValueError(f"fixed basis shape regression: {fixed_basis.shape}")
    if len(fixed_smith) != fixed_rank:
        raise ValueError("fixed Smith rank regression")
    if any(GROUP_ORDER % s for s in fixed_smith):
        raise ValueError(f"fixed Smith invariant does not divide group order: {fixed_smith}")
    fixed_saturation_index = math.prod(fixed_smith)
    projected_quotient_factors = tuple(GROUP_ORDER // s for s in fixed_smith)
    projected_quotient_order = math.prod(projected_quotient_factors)
    if projected_quotient_order * fixed_saturation_index != GROUP_ORDER ** fixed_rank:
        raise ValueError("fixed projection quotient order identity regression")

    # For P=N/64 and Q=I-P, the two finite projection quotients are canonically
    # isomorphic. Both are the image of Pic_Z modulo Pic_Z^G + Pic_Z^anti:
    # x -> P(x) mod Pic_Z^G and x -> Q(x) mod Pic_Z^anti have the same kernel.
    # Hence no separate 59-dimensional Smith computation is mathematically needed.
    anti_rank = PICARD_RANK - fixed_rank
    anti_projected_quotient_factors = projected_quotient_factors
    anti_projected_quotient_order = projected_quotient_order

    cert = {
        "schema": "STAGE32_RESIDUAL32_01_REYNOLDS_PROJECTED_INTEGRAL_LATTICE_DIAGNOSTIC_V3_RANK5_COLUMN_MODULE",
        "mode": "EXACT_RANK5_COLUMN_MODULE_SMITH_PLUS_CANONICAL_COMPLEMENTARY_PROJECTION_QUOTIENT",
        "hperp_integral_adapter_certificate_sha256": adapter.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_bridge_certificate_sha256": bridge.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_stabilizer_group_order": GROUP_ORDER,
        "picard_rank": PICARD_RANK,
        "fixed_rank": fixed_rank,
        "anti_fixed_rank": anti_rank,
        "fixed_slice_kernel_rank": fixed_rank - 3,
        "reynolds_numerator_sha256": csha([[int(N[i,j]) for j in range(64)] for i in range(64)]),
        "action_hashes_sha256": csha(sorted(action_hashes)),
        "fixed_image_lattice": {
            "smith_method": "INCREMENTAL_RANK5_COLUMN_MODULE_USING_ONLY_5x6_HNF_THEN_SMITH_ON_64x5_BASIS",
            "column_module_stats": module_stats,
            "basis_shape": [fixed_basis.rows, fixed_basis.cols],
            "basis_sha256": csha([
                [int(fixed_basis[i, j]) for j in range(fixed_basis.cols)]
                for i in range(fixed_basis.rows)
            ]),
            "smith_nonzero_diagonal": list(fixed_smith),
            "saturation_index_imN_in_PicZ_fixed": fixed_saturation_index,
            "projection_quotient_invariant_orders": list(projected_quotient_factors),
            "projection_quotient_order": projected_quotient_order,
            "interpretation": "P(Pic_Z)/Pic_Z^G where P=(1/64)N",
        },
        "anti_fixed_projection_quotient": {
            "derived_via_canonical_isomorphism": True,
            "projection_quotient_invariant_orders": list(anti_projected_quotient_factors),
            "projection_quotient_order": anti_projected_quotient_order,
            "interpretation": "(I-P)(Pic_Z)/Pic_Z^anti is canonically isomorphic to P(Pic_Z)/Pic_Z^G via Pic_Z/(Pic_Z^G+Pic_Z^anti)",
        },
        "proof": {
            "N_squared_equals_group_order_times_N": True,
            "N_gram_self_adjoint": True,
            "phi_N_equals_group_order_phi": True,
            "incremental_column_module_equals_imN": True,
            "only_rank5_coordinate_algebra_and_5x6_HNF_used_before_final_64x5_smith": True,
            "imN_saturates_to_integral_fixed_lattice": True,
            "64_times_fixed_lattice_contained_in_imN_contained_in_fixed_lattice": True,
            "projected_integral_classes_finite": True,
            "fixed_and_anti_projected_quotients_canonically_isomorphic": True,
            "anti_59dimensional_smith_not_required": True,
        },
        "next_if_quotient_manageable": "enumerate finite Reynolds projection classes; reduce surviving Stage32 leaf to rank-2 fixed-slice lattice plus one anti-fixed penalty per projection class",
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
        "verdict": "PASS_REYNOLDS_PROJECTED_INTEGRAL_LATTICE_DIAGNOSTIC",
        "fixed_rank": fixed_rank,
        "anti_fixed_rank": anti_rank,
        "fixed_slice_kernel_rank": fixed_rank - 3,
        "fixed_smith": list(fixed_smith),
        "projection_quotient_factors": list(projected_quotient_factors),
        "projection_quotient_order": projected_quotient_order,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
