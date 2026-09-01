#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass

import sympy
from sympy import Matrix

from direct_picard_slice_quadratic_bound import DirectPicardSliceQuadraticBound
from hperp_integral_adapter import HperpIntegralPairingAdapter, KNOWN_CURVE_COUNT
from pairing_prefix_engine import close_permutation_group


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def rational_vector_payload(v: Matrix) -> tuple[int, tuple[int, int, int]]:
    if v.shape != (1, 3):
        raise ValueError(f"expected 1x3 vector, got {v.shape}")
    den = 1
    for value in v:
        den = math.lcm(den, int(sympy.denom(value)))
    nums = tuple(int(v[0, j] * den) for j in range(3))
    g = den
    for n in nums:
        g = math.gcd(g, abs(n))
    if g > 1:
        den //= g
        nums = tuple(n // g for n in nums)
    return den, nums


@dataclass(frozen=True)
class OrbitSumRule:
    orbit_id: int
    known_curve_labels_1based: tuple[int, ...]
    fixed_on_slice: bool
    fixed_denominator: int | None
    fixed_numerators: tuple[int, int, int] | None

    def fixed_value_nonnegative(self, d: int, e: int, a: int) -> bool:
        if not self.fixed_on_slice:
            return True
        assert self.fixed_numerators is not None
        t = (int(d), int(e), int(a))
        return sum(self.fixed_numerators[i] * t[i] for i in range(3)) >= 0


@dataclass(frozen=True)
class DirectPicardSliceStabilizerOrbitBound:
    bound: DirectPicardSliceQuadraticBound
    subgroup_order: int
    rules: tuple[OrbitSumRule, ...]
    certificate: dict

    def fixed_orbit_sums_nonnegative(self, d: int, e: int, a: int) -> bool:
        return all(rule.fixed_value_nonnegative(d, e, a) for rule in self.rules)

    def first_negative_fixed_orbit(self, d: int, e: int, a: int) -> OrbitSumRule | None:
        for rule in self.rules:
            if rule.fixed_on_slice and not rule.fixed_value_nonnegative(d, e, a):
                return rule
        return None

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "DirectPicardSliceStabilizerOrbitBound":
        bound = DirectPicardSliceQuadraticBound.from_retained(marking, bundle)
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        full_group = close_permutation_group(marking["aut_action"]["permutations_1based"])
        if len(full_group) != 1536:
            raise ValueError(f"full Aut group order regression: {len(full_group)}")

        first_half = frozenset(range(46))
        normal = frozenset(range(92))
        exceptional = frozenset(range(92, 140))

        def preserves_slice_partition(g: tuple[int, ...]) -> bool:
            return (
                frozenset(g[i] for i in first_half) == first_half
                and frozenset(g[i] for i in normal) == normal
                and frozenset(g[i] for i in exceptional) == exceptional
            )

        subgroup = [g for g in full_group if preserves_slice_partition(g)]
        if not subgroup or tuple(range(KNOWN_CURVE_COUNT)) not in set(subgroup):
            raise ValueError("slice stabilizer subgroup regression")

        unseen = set(range(KNOWN_CURVE_COUNT))
        orbits: list[tuple[int, ...]] = []
        while unseen:
            seed = min(unseen)
            orbit = tuple(sorted({g[seed] for g in subgroup}))
            for i in orbit:
                if i not in unseen:
                    raise ValueError("stabilizer orbit overlap regression")
            unseen.difference_update(orbit)
            orbits.append(orbit)
        orbits.sort(key=lambda o: o[0])

        phi = Matrix([
            list(bound.bridge.degree_functional),
            list(bound.bridge.exceptional_mass_functional),
            list(bound.bridge.first_normal_half_functional),
        ])
        gram = Matrix(bundle["picard_gram_64x64"])
        gram_inv = gram.inv()
        M = phi * gram_inv * phi.T
        x0_map = gram_inv * phi.T * M.inv()

        rules = []
        fixed_count = 0
        for orbit_id, orbit in enumerate(orbits):
            orbit_sum = Matrix([[sum(int(adapter.pairing_matrix[i, j]) for i in orbit) for j in range(64)]])
            rank = int(phi.col_join(orbit_sum).rank())
            if rank == 3:
                fixed_count += 1
                alpha = orbit_sum * x0_map
                if orbit_sum != alpha * phi:
                    raise ValueError(f"orbit {orbit_id}: fixed-functional reconstruction failed")
                den, nums = rational_vector_payload(alpha)
                fixed = True
            elif rank == 4:
                den, nums = None, None
                fixed = False
            else:
                raise ValueError(f"orbit {orbit_id}: unexpected augmented rank {rank}")
            rules.append(OrbitSumRule(
                orbit_id=orbit_id,
                known_curve_labels_1based=tuple(i + 1 for i in orbit),
                fixed_on_slice=fixed,
                fixed_denominator=den,
                fixed_numerators=nums,
            ))

        cert_rules = [{
            "orbit_id": r.orbit_id,
            "known_curve_labels_1based": list(r.known_curve_labels_1based),
            "orbit_size": len(r.known_curve_labels_1based),
            "fixed_on_d_e_a_slice": r.fixed_on_slice,
            "fixed_orbit_sum": None if not r.fixed_on_slice else {
                "denominator": r.fixed_denominator,
                "integer_coefficients_d_e_a": list(r.fixed_numerators or ()),
            },
        } for r in rules]

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_SLICE_STABILIZER_ORBIT_BOUND_V1",
            "mode": "EXACT_AUT_STABILIZER_ORBIT_AVERAGING_AND_FIXED_ORBIT_SUM_NECESSARY_CONDITIONS",
            "quadratic_bound_certificate_sha256": bound.certificate["canonical_sha256_without_this_field"],
            "adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "full_aut_group_order": len(full_group),
            "slice_stabilizer_group_order": len(subgroup),
            "slice_partition": {
                "first_normal_half_labels_1based": [1, 46],
                "second_normal_half_labels_1based": [47, 92],
                "exceptional_labels_1based": [93, 140],
            },
            "stabilizer_subgroup_closure_exact": True,
            "known_curve_orbit_count": len(orbits),
            "orbit_sizes": [len(o) for o in orbits],
            "fixed_orbit_sum_count": fixed_count,
            "nonfixed_orbit_sum_count": len(orbits) - fixed_count,
            "all_orbit_sums_fixed_on_slice": fixed_count == len(orbits),
            "orbits": cert_rules,
            "proof": {
                "aut_action_preserves_intersection_form": True,
                "stabilizer_preserves_degree_exceptional_firsthalf_slice": True,
                "all140_nonnegative_implies_each_orbit_sum_nonnegative": True,
                "fixed_orbit_sum_negative_implies_no_all140_nonnegative_class_on_slice": True,
                "averaging_note": "averaging over the stabilizer preserves the slice and the all140 nonnegative cone; strict concavity on the slice means a continuous optimum may be chosen stabilizer-invariant",
                "full_simultaneous_orbit_qp_solved": False,
            },
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        if sum(cert["orbit_sizes"]) != KNOWN_CURVE_COUNT:
            raise ValueError("orbit partition size regression")
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(bound=bound, subgroup_order=len(subgroup), rules=tuple(rules), certificate=cert)
