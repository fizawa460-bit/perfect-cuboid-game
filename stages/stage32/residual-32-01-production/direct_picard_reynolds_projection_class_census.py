#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path

from sympy import Matrix

from direct_picard_reynolds_lattice_diagnostic import (
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
    load_retained,
    smith_nonzero_diagonal_via_lowrank_column_module,
)
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import (
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)
from pairing_prefix_engine import close_permutation_group

EXPECTED_FIXED_RANK = 5
EXPECTED_FIXED_SMITH = (4, 8, 8, 16, 16)
EXPECTED_QUOTIENT_FACTORS = (16, 8, 8, 4, 4)
EXPECTED_QUOTIENT_ORDER = 16384
MODULUS = GROUP_ORDER


def add_mod(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % MODULUS for x, y in zip(a, b))


def generator_residue(column: Matrix) -> tuple[int, ...]:
    return tuple(int(column[i, 0]) % MODULUS for i in range(column.rows))


def extend_subgroup(
    subgroup: set[tuple[int, ...]], generator: tuple[int, ...]
) -> tuple[set[tuple[int, ...]], int]:
    """Adjoin one generator and return the exact relative cyclic order."""
    zero = (0,) * len(generator)
    if generator in subgroup:
        return subgroup, 1

    multiples = [zero]
    current = zero
    relative_order = None
    for k in range(1, MODULUS + 1):
        current = add_mod(current, generator)
        if current in subgroup:
            relative_order = k
            break
        multiples.append(current)
    if relative_order is None:
        raise ValueError("generator order did not divide Reynolds modulus")

    old = tuple(subgroup)
    enlarged = {
        add_mod(h, multiple)
        for h in old
        for multiple in multiples
    }
    expected = len(subgroup) * relative_order
    if len(enlarged) != expected:
        raise ValueError(
            f"subgroup extension collision regression: {len(enlarged)} != {expected}"
        )
    return enlarged, relative_order


def residue_stream_sha256(reps: list[tuple[int, ...]]) -> str:
    h = hashlib.sha256()
    for rep in reps:
        if any(not 0 <= value < MODULUS for value in rep):
            raise ValueError("residue outside canonical range")
        h.update(bytes(rep))
    return h.hexdigest()


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_reynolds_class_picard")
    marking = load_retained(args.marking, "s32_reynolds_class_marking")
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
        action_hashes.append(csha([[int(T[i, j]) for j in range(64)] for i in range(64)]))

    if N * N != GROUP_ORDER * N:
        raise ValueError("Reynolds numerator idempotence regression")
    if phi * N != GROUP_ORDER * phi:
        raise ValueError("Reynolds numerator slice preservation regression")
    fixed_rank = int(N.rank())
    if fixed_rank != EXPECTED_FIXED_RANK:
        raise ValueError(f"fixed rank regression: {fixed_rank}")

    fixed_smith, fixed_basis, module_stats = smith_nonzero_diagonal_via_lowrank_column_module(
        N, fixed_rank
    )
    if fixed_smith != EXPECTED_FIXED_SMITH:
        raise ValueError(f"fixed Smith regression: {fixed_smith}")
    quotient_factors = tuple(GROUP_ORDER // s for s in fixed_smith)
    quotient_order = math.prod(quotient_factors)
    if quotient_factors != EXPECTED_QUOTIENT_FACTORS:
        raise ValueError(f"projection quotient factor regression: {quotient_factors}")
    if quotient_order != EXPECTED_QUOTIENT_ORDER:
        raise ValueError(f"projection quotient order regression: {quotient_order}")

    # im(N)/64*Pic_Z^G is exactly the reduction of im(N) modulo 64.
    # Indeed im(N) is fixed because N^2=64N; if y=Nx is divisible by 64,
    # y=64z, then Nz=64z, so z is integral fixed. Thus the kernel of
    # im(N) -> (Z/64)^64 is precisely 64*Pic_Z^G.
    generators = [generator_residue(fixed_basis[:, j]) for j in range(fixed_basis.cols)]
    residues: set[tuple[int, ...]] = {(0,) * PICARD_RANK}
    relative_orders = []
    subgroup_sizes = [1]
    for generator in generators:
        residues, relative_order = extend_subgroup(residues, generator)
        relative_orders.append(relative_order)
        subgroup_sizes.append(len(residues))

    if len(residues) != quotient_order:
        raise ValueError(f"enumerated projection class count regression: {len(residues)}")
    if math.prod(relative_orders) != quotient_order:
        raise ValueError("relative generator orders do not multiply to quotient order")

    # Each fixed-basis generator is actually fixed and has slice functionals
    # divisible by 64. By linearity the same properties hold for every class.
    generator_checks = []
    for j in range(fixed_basis.cols):
        b = fixed_basis[:, j]
        if N * b != GROUP_ORDER * b:
            raise ValueError(f"fixed-basis generator {j} is not Reynolds-fixed")
        phi_b = phi * b
        if any(int(value) % GROUP_ORDER for value in phi_b):
            raise ValueError(f"fixed-basis generator {j} has nonintegral projected slice residue")
        generator_checks.append({
            "generator_index": j,
            "relative_order_in_enumeration": relative_orders[j],
            "slice_functionals_divided_by_64": [int(value) // GROUP_ORDER for value in phi_b],
        })

    sorted_reps = sorted(residues)
    residue_sha = residue_stream_sha256(sorted_reps)
    basis_sha = csha([
        [int(fixed_basis[i, j]) for j in range(fixed_basis.cols)]
        for i in range(fixed_basis.rows)
    ])

    cert = {
        "schema": "STAGE32_RESIDUAL32_01_REYNOLDS_PROJECTION_CLASS_CENSUS_V1",
        "mode": "EXACT_ENUMERATION_OF_IM_REYNOLDS_MOD_64_FINITE_PROJECTION_CLASSES",
        "hperp_integral_adapter_certificate_sha256": adapter.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_bridge_certificate_sha256": bridge.certificate[
            "canonical_sha256_without_this_field"
        ],
        "slice_stabilizer_group_order": GROUP_ORDER,
        "picard_rank": PICARD_RANK,
        "fixed_rank": fixed_rank,
        "fixed_slice_kernel_rank": fixed_rank - 3,
        "fixed_smith_nonzero_diagonal": list(fixed_smith),
        "projection_quotient_invariant_orders": list(quotient_factors),
        "projection_quotient_order": quotient_order,
        "enumerated_projection_class_count": len(sorted_reps),
        "enumeration_generator_count": len(generators),
        "enumeration_relative_generator_orders": relative_orders,
        "enumeration_subgroup_sizes": subgroup_sizes,
        "fixed_image_basis_sha256": basis_sha,
        "fixed_image_column_module_stats": module_stats,
        "action_hashes_sha256": csha(sorted(action_hashes)),
        "canonical_sorted_residue_stream_sha256": residue_sha,
        "canonical_residue_encoding": "lexicographically sorted 64-byte vectors with entries 0..63; concatenate with no separator",
        "generator_checks": generator_checks,
        "proof": {
            "N_squared_equals_64N": True,
            "imN_is_integral_fixed": True,
            "kernel_of_imN_mod64_equals_64_times_integral_fixed_lattice": True,
            "projection_quotient_identified_with_imN_mod64": True,
            "five_exact_integral_image_basis_generators_enumerated": True,
            "relative_orders_multiply_to_quotient_order": True,
            "all_projection_classes_enumerated_exactly_once_after_set_canonicalization": True,
            "projection_classes_preserve_integral_slice_functionals": True,
            "class_representatives_regenerable_from_retained_sources": True,
        },
        "next_leaf": "combine each finite projection residue with the rank-2 fixed-slice lattice and derive a safe anti-fixed/integrality penalty; do not arm 52-unit heavy production",
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
        "verdict": "PASS_REYNOLDS_PROJECTION_CLASS_CENSUS",
        "projection_class_count": len(sorted_reps),
        "quotient_factors": list(quotient_factors),
        "relative_generator_orders": relative_orders,
        "subgroup_sizes": subgroup_sizes,
        "residue_stream_sha256": residue_sha,
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
