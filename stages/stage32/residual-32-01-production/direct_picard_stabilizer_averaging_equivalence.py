#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass

import sympy
from sympy import Matrix

from direct_picard_slice_stabilizer_orbit_bound import DirectPicardSliceStabilizerOrbitBound
from hperp_integral_adapter import (
    HperpIntegralPairingAdapter,
    RETAINED_BASIS_KNOWN_LABELS_1BASED,
)
from pairing_prefix_engine import close_permutation_group


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_string_sha(m: Matrix) -> str:
    return csha([[str(m[i, j]) for j in range(m.cols)] for i in range(m.rows)])


@dataclass(frozen=True)
class DirectPicardStabilizerAveragingEquivalence:
    orbit_model: DirectPicardSliceStabilizerOrbitBound
    certificate: dict

    @classmethod
    def from_retained(
        cls, marking: dict, bundle: dict
    ) -> "DirectPicardStabilizerAveragingEquivalence":
        orbit_model = DirectPicardSliceStabilizerOrbitBound.from_retained(marking, bundle)
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        bound = orbit_model.bound

        gram = Matrix(bundle["picard_gram_64x64"])
        curve_coords = adapter.class_coordinates_in_retained_basis
        if curve_coords.shape != (140, 64):
            raise ValueError("saturated all140 coordinate shape regression")
        if any(sympy.denom(v) != 1 for v in curve_coords):
            raise ValueError("known-curve Picard coordinates are not integral")

        full_group = close_permutation_group(marking["aut_action"]["permutations_1based"])
        if len(full_group) != 1536:
            raise ValueError(f"full Aut group order regression: {len(full_group)}")
        first_half = frozenset(range(46))
        normal = frozenset(range(92))
        exceptional = frozenset(range(92, 140))
        subgroup = [
            g for g in full_group
            if frozenset(g[i] for i in first_half) == first_half
            and frozenset(g[i] for i in normal) == normal
            and frozenset(g[i] for i in exceptional) == exceptional
        ]
        if len(subgroup) != orbit_model.subgroup_order or len(subgroup) != 64:
            raise ValueError("slice stabilizer order regression")

        phi = Matrix([
            list(bound.bridge.degree_functional),
            list(bound.bridge.exceptional_mass_functional),
            list(bound.bridge.first_normal_half_functional),
        ])

        actions: list[Matrix] = []
        for g in subgroup:
            cols = []
            for basis_label in RETAINED_BASIS_KNOWN_LABELS_1BASED:
                image_label = g[basis_label - 1]
                cols.append(curve_coords[image_label, :].T)
            T = Matrix.hstack(*cols)
            if any(sympy.denom(v) != 1 for v in T):
                raise ValueError("stabilizer linear action is not integral")
            if T.T * gram * T != gram:
                raise ValueError("stabilizer linear action is not a Picard isometry")
            if phi * T != phi:
                raise ValueError("stabilizer linear action does not preserve d/e/a slice")
            actions.append(T)

        Psum = Matrix.zeros(64, 64)
        for T in actions:
            Psum += T
        P = Psum / len(actions)
        if P * P != P:
            raise ValueError("Reynolds averaging operator is not idempotent")
        if P.T * gram != gram * P:
            raise ValueError("Reynolds operator is not Gram-self-adjoint")
        if phi * P != phi:
            raise ValueError("Reynolds operator does not preserve slice target")
        fixed_dimension_q = P.trace()
        if sympy.denom(fixed_dimension_q) != 1:
            raise ValueError("fixed-subspace trace is not integral")
        fixed_dimension = int(fixed_dimension_q)
        if fixed_dimension <= 0 or fixed_dimension > 64:
            raise ValueError("invalid fixed-subspace dimension")

        orbit_checks = []
        checked_pairings = 0
        for rule in orbit_model.rules:
            orbit = [label - 1 for label in rule.known_curve_labels_1based]
            orbit_sum = Matrix([[
                sum(int(adapter.pairing_matrix[i, j]) for i in orbit)
                for j in range(64)
            ]])
            expected = orbit_sum / len(orbit)
            multiplicity = len(subgroup) // len(orbit)
            if multiplicity * len(orbit) != len(subgroup):
                raise ValueError("orbit size does not divide stabilizer order")
            for target in orbit:
                got = adapter.pairing_matrix[target, :] * P
                if got != expected:
                    raise ValueError(
                        f"orbit-average pairing identity failed for label {target + 1}"
                    )
                checked_pairings += 1
            orbit_checks.append({
                "orbit_id": rule.orbit_id,
                "orbit_size": len(orbit),
                "stabilizer_preimage_multiplicity": multiplicity,
                "average_pairing_identity_exact": True,
            })
        if checked_pairings != 140:
            raise ValueError("all140 averaging identity coverage regression")

        if bound.certificate.get("slice_kernel_negative_definite_exact") is not True:
            raise ValueError("missing exact negative-definite slice-kernel certificate")

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_STABILIZER_AVERAGING_EQUIVALENCE_V2_SATURATED_BASIS",
            "mode": "EXACT_REYNOLDS_AVERAGING_EQUIVALENCE_OF_ALL140_AND_ORBIT_SUM_CONTINUOUS_MAXIMA",
            "stabilizer_orbit_certificate_sha256": orbit_model.certificate[
                "canonical_sha256_without_this_field"
            ],
            "hperp_integral_adapter_certificate_sha256": adapter.certificate[
                "canonical_sha256_without_this_field"
            ],
            "quadratic_bound_certificate_sha256": bound.certificate[
                "canonical_sha256_without_this_field"
            ],
            "basis_semantics": "SATURATED_RETAINED_PICARD_BASIS_REALIZED_BY_RETAINED_BASIS_KNOWN_LABELS",
            "full_aut_group_order": len(full_group),
            "slice_stabilizer_group_order": len(subgroup),
            "picard_rank": 64,
            "fixed_subspace_dimension": fixed_dimension,
            "reynolds_operator_sha256": matrix_string_sha(P),
            "reynolds_idempotent_exact": True,
            "reynolds_gram_self_adjoint_exact": True,
            "reynolds_preserves_d_e_a_slice_exact": True,
            "stabilizer_integral_isometry_count": len(actions),
            "all140_orbit_average_pairing_identities_checked": checked_pairings,
            "orbits": orbit_checks,
            "proof": {
                "hperp_adapter_independently_checks_all_aut_generators_are_all140_intersection_isometries": True,
                "orbit_sum_nonnegative_point_averages_to_all140_nonnegative_point": True,
                "for_each_curve_averaged_pairing_equals_its_orbit_sum_divided_by_orbit_size": True,
                "average_minus_original_lies_in_slice_kernel": True,
                "slice_kernel_negative_definite_exact": True,
                "finite_isometry_average_never_decreases_self_intersection_on_fixed_slice": True,
                "all140_cone_subset_of_orbit_sum_cone": True,
                "continuous_feasibility_equivalent": True,
                "continuous_max_self_intersection_equal": True,
                "orbit_sum_kkt_bound_is_exact_for_all140_continuous_problem": True,
                "integral_equivalence_not_claimed": True,
                "reason_integral_equivalence_not_claimed": "Reynolds averaging divides by stabilizer order and need not preserve Picard_Z",
            },
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(orbit_model=orbit_model, certificate=cert)
