#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

from hperp_integral_adapter import (
    HperpIntegralPairingAdapter,
    PICARD_RANK,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
    _parse_hperp,
)

NORMAL_COUNT = 92
EXCEPTIONAL_COUNT = 48
FIRST_NORMAL_HALF_COUNT = 46


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def vector_list(v: Matrix) -> list[int]:
    if v.rows == 1:
        return [int(v[0, j]) for j in range(v.cols)]
    if v.cols == 1:
        return [int(v[i, 0]) for i in range(v.rows)]
    raise ValueError("expected vector")


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


@dataclass(frozen=True)
class DirectPicardSliceBridge:
    hyperplane_coordinates: tuple[int, ...]
    degree_functional: tuple[int, ...]
    exceptional_mass_functional: tuple[int, ...]
    first_normal_half_functional: tuple[int, ...]
    target_image_modulus: int
    target_image_coefficients: tuple[tuple[int, int, int], ...]
    certificate: dict

    def target_in_image(self, d: int, e: int, a: int) -> bool:
        q = int(self.target_image_modulus)
        if q == 1:
            return True
        target = (int(d), int(e), int(a))
        return all(sum(row[j] * target[j] for j in range(3)) % q == 0 for row in self.target_image_coefficients)

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "DirectPicardSliceBridge":
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        gram = Matrix(bundle["picard_gram_64x64"])
        if gram.shape != (PICARD_RANK, PICARD_RANK) or gram != gram.T:
            raise ValueError("retained Picard Gram regression")

        hperp_text = marking.get("hperp_text")
        if not isinstance(hperp_text, str):
            raise ValueError("retained marking missing hperp_text")
        _, known_degree, _, _, hmeta = _parse_hperp(hperp_text)

        basis_degree = Matrix([
            int(known_degree[label - 1])
            for label in RETAINED_BASIS_KNOWN_LABELS_1BASED
        ])
        hq = gram.inv() * basis_degree
        if any(sympy.denom(v) != 1 for v in hq):
            raise ValueError("hyperplane is not integral in retained Picard basis")
        h = Matrix([int(v) for v in hq])
        if int((h.T * gram * h)[0]) != 16:
            raise ValueError("hyperplane square regression")

        recovered_degree = adapter.class_coordinates_in_retained_basis * gram * h
        if recovered_degree != known_degree:
            raise ValueError("all140 degree reconstruction regression")

        pairing = adapter.pairing_matrix
        normal = Matrix([[sum(int(pairing[k, j]) for k in range(0, NORMAL_COUNT)) for j in range(PICARD_RANK)]])
        exceptional = Matrix([[sum(int(pairing[k, j]) for k in range(NORMAL_COUNT, NORMAL_COUNT + EXCEPTIONAL_COUNT)) for j in range(PICARD_RANK)]])
        first_half = Matrix([[sum(int(pairing[k, j]) for k in range(0, FIRST_NORMAL_HALF_COUNT)) for j in range(PICARD_RANK)]])
        second_half = normal - first_half
        degree_fn = h.T * gram

        if normal + 5 * exceptional != 19 * degree_fn:
            raise ValueError("normal + 5*exceptional = 19*degree functional identity failed")
        if first_half + second_half != normal:
            raise ValueError("normal-half decomposition regression")

        phi = degree_fn.col_join(exceptional).col_join(first_half)
        rank = int(phi.rank())
        if rank != 3:
            raise ValueError(f"direct-slice functional rank regression: {rank}")

        # Image(phi: Z^64 -> Z^3) is an exact full-rank column lattice.  The
        # historical Magma `tar in Image(phi)` gate therefore reduces to three
        # fixed integer congruences, certified here by the column HNF.
        image_hnf = hermite_normal_form(phi)
        if image_hnf.shape != (3, 3) or image_hnf.det() == 0:
            raise ValueError(f"direct-slice image HNF regression: {image_hnf.shape}")
        image_index = abs(int(image_hnf.det()))
        image_inv = image_hnf.inv()
        modulus = 1
        for value in image_inv:
            modulus = math.lcm(modulus, int(sympy.denom(value)))
        image_inv_int = image_inv * modulus
        if any(sympy.denom(v) != 1 for v in image_inv_int):
            raise ValueError("direct-slice HNF inverse scaling regression")
        image_inv_int = Matrix([[int(image_inv_int[i, j]) for j in range(3)] for i in range(3)])
        active_coefficients = tuple(
            tuple(int(image_inv_int[i, j]) % modulus for j in range(3))
            for i in range(3)
            if modulus != 1 and any(int(image_inv_int[i, j]) % modulus for j in range(3))
        )

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_SLICE_BRIDGE_V1",
            "mode": "CURRENT_RETAINED_PICARD64_TO_EXACT_D_E_A_PARTITION",
            "retained_bundle_sha256": bundle["canonical_sha256"],
            "hperp_text_sha256": hmeta["hperp_text_sha256"],
            "hperp_core_sha256": hmeta["core_sha256"],
            "adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "picard_rank": PICARD_RANK,
            "known_curve_count": NORMAL_COUNT + EXCEPTIONAL_COUNT,
            "normal_curve_count": NORMAL_COUNT,
            "exceptional_curve_count": EXCEPTIONAL_COUNT,
            "first_normal_half_count": FIRST_NORMAL_HALF_COUNT,
            "second_normal_half_count": NORMAL_COUNT - FIRST_NORMAL_HALF_COUNT,
            "hyperplane_coordinates": vector_list(h),
            "hyperplane_square": 16,
            "degree_functional": vector_list(degree_fn),
            "exceptional_mass_functional": vector_list(exceptional),
            "first_normal_half_functional": vector_list(first_half),
            "second_normal_half_functional": vector_list(second_half),
            "mass_identity": "normal_total + 5*exceptional_total = 19*degree",
            "mass_identity_exact_on_picard64": True,
            "slice_functional_rank": rank,
            "slice_kernel_rank": PICARD_RANK - rank,
            "slice_coordinates": ["degree", "exceptional_total", "first_normal_half_total"],
            "target_image": {
                "hnf": matrix_list(image_hnf),
                "hnf_sha256": csha(matrix_list(image_hnf)),
                "image_index": image_index,
                "congruence_modulus": modulus,
                "active_congruence_rows": len(active_coefficients),
                "congruence_coefficients": [list(v) for v in active_coefficients],
                "historical_magma_gate_equivalent": "tar in Image(phi)",
            },
            "candidate_partition_semantics": {
                "if_all140_pairings_nonnegative": True,
                "exceptional_total_nonnegative": True,
                "normal_total_equals_19d_minus_5e": True,
                "first_normal_half_a_bounds": "0 <= a <= 19*d - 5*e",
                "slice_assignment_unique": True,
                "terminal_prefix_materialization_required_for_partition": False,
                "target_image_gate_exact_before_closevectors": True,
            },
            "numerical_closevectors_complete": False,
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            hyperplane_coordinates=tuple(vector_list(h)),
            degree_functional=tuple(vector_list(degree_fn)),
            exceptional_mass_functional=tuple(vector_list(exceptional)),
            first_normal_half_functional=tuple(vector_list(first_half)),
            target_image_modulus=modulus,
            target_image_coefficients=active_coefficients,
            certificate=cert,
        )
