#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import importlib.util
import json
import math
from pathlib import Path

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

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


def smith_nonzero_diagonal(m: Matrix) -> tuple[int, ...]:
    D = smith_normal_form(m, domain=ZZ)
    vals = []
    for i in range(min(D.rows, D.cols)):
        v = abs(int(D[i, i]))
        if v:
            vals.append(v)
    return tuple(vals)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

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

    fixed_smith = smith_nonzero_diagonal(N)
    if len(fixed_smith) != fixed_rank:
        raise ValueError("fixed Smith rank regression")
    if any(GROUP_ORDER % s for s in fixed_smith):
        raise ValueError(f"fixed Smith invariant does not divide group order: {fixed_smith}")
    fixed_saturation_index = math.prod(fixed_smith)
    projected_quotient_factors = tuple(GROUP_ORDER // s for s in fixed_smith)
    projected_quotient_order = math.prod(projected_quotient_factors)
    if projected_quotient_order * fixed_saturation_index != GROUP_ORDER ** fixed_rank:
        raise ValueError("fixed projection quotient order identity regression")

    A = GROUP_ORDER * Matrix.eye(PICARD_RANK) - N
    anti_rank = int(A.rank())
    if anti_rank != PICARD_RANK - fixed_rank:
        raise ValueError("anti-fixed rank regression")
    anti_smith = smith_nonzero_diagonal(A)
    if len(anti_smith) != anti_rank:
        raise ValueError("anti-fixed Smith rank regression")
    if any(GROUP_ORDER % s for s in anti_smith):
        raise ValueError("anti-fixed Smith invariant does not divide group order")
    anti_saturation_index = math.prod(anti_smith)
    anti_projected_quotient_factors = tuple(GROUP_ORDER // s for s in anti_smith if s != GROUP_ORDER)
    anti_projected_quotient_order = (GROUP_ORDER ** anti_rank) // anti_saturation_index
    if anti_projected_quotient_order != projected_quotient_order:
        raise ValueError(
            f"fixed/anti projected quotient order mismatch: {projected_quotient_order} != {anti_projected_quotient_order}"
        )

    cert = {
        "schema": "STAGE32_RESIDUAL32_01_REYNOLDS_PROJECTED_INTEGRAL_LATTICE_DIAGNOSTIC_V1",
        "mode": "EXACT_FIXED_ANTI_FIXED_PICARD_LATTICE_DECOMPOSITION_UNDER_SLICE_STABILIZER",
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
            "smith_nonzero_diagonal": list(fixed_smith),
            "saturation_index_imN_in_PicZ_fixed": fixed_saturation_index,
            "projection_quotient_invariant_orders": list(projected_quotient_factors),
            "projection_quotient_order": projected_quotient_order,
            "interpretation": "P(Pic_Z)/Pic_Z^G where P=(1/64)N",
        },
        "anti_fixed_image_lattice": {
            "smith_nonzero_diagonal_non64": [s for s in anti_smith if s != GROUP_ORDER],
            "smith_nonzero_diagonal_64_count": sum(1 for s in anti_smith if s == GROUP_ORDER),
            "saturation_index": anti_saturation_index,
            "projection_quotient_invariant_orders_nontrivial": list(anti_projected_quotient_factors),
            "projection_quotient_order": anti_projected_quotient_order,
        },
        "proof": {
            "N_squared_equals_group_order_times_N": True,
            "N_gram_self_adjoint": True,
            "phi_N_equals_group_order_phi": True,
            "imN_saturates_to_integral_fixed_lattice": True,
            "64_times_fixed_lattice_contained_in_imN_contained_in_fixed_lattice": True,
            "projected_integral_classes_finite": True,
            "fixed_and_anti_projected_quotient_orders_match": True,
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
