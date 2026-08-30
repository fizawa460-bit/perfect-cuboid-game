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


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def rational_vector_payload(v: Matrix) -> tuple[int, tuple[int, int, int]]:
    values = [v[0, j] if v.rows == 1 else v[j, 0] for j in range(3)]
    den = 1
    for x in values:
        den = math.lcm(den, int(sympy.denom(x)))
    nums = tuple(int(x * den) for x in values)
    g = den
    for n in nums:
        g = math.gcd(g, abs(n))
    if g > 1:
        den //= g
        nums = tuple(n // g for n in nums)
    return den, nums


def rational_matrix_payload_3(m: Matrix) -> tuple[int, tuple[tuple[int, int, int], ...]]:
    if m.shape != (3, 3):
        raise ValueError(f"expected 3x3 matrix, got {m.shape}")
    den = 1
    for x in m:
        den = math.lcm(den, int(sympy.denom(x)))
    rows = tuple(
        tuple(int(m[i, j] * den) for j in range(3))
        for i in range(3)
    )
    g = den
    for row in rows:
        for n in row:
            g = math.gcd(g, abs(n))
    if g > 1:
        den //= g
        rows = tuple(tuple(n // g for n in row) for row in rows)
    return den, rows


@dataclass(frozen=True)
class FacetRule:
    rule_id: int
    known_curve_labels_1based: tuple[int, ...]
    fixed_on_slice: bool
    trigger_denominator: int
    trigger_numerators: tuple[int, int, int]
    boundary_denominator: int | None
    boundary_integer_matrix: tuple[tuple[int, int, int], ...] | None

    def violated_by_unconstrained_maximizer(self, d: int, e: int, a: int) -> bool:
        t = (int(d), int(e), int(a))
        return sum(self.trigger_numerators[i] * t[i] for i in range(3)) < 0

    def boundary_can_reach(self, d: int, e: int, a: int, lower: int) -> bool:
        if self.fixed_on_slice:
            return not self.violated_by_unconstrained_maximizer(d, e, a)
        if not self.violated_by_unconstrained_maximizer(d, e, a):
            return True
        assert self.boundary_denominator is not None
        assert self.boundary_integer_matrix is not None
        t = (int(d), int(e), int(a))
        n = sum(
            t[i] * self.boundary_integer_matrix[i][j] * t[j]
            for i in range(3)
            for j in range(3)
        )
        return n >= int(lower) * self.boundary_denominator


@dataclass(frozen=True)
class DirectPicardAll140SingleFacetBound:
    bound: DirectPicardSliceQuadraticBound
    rules: tuple[FacetRule, ...]
    certificate: dict

    def first_pruning_rule(self, d: int, e: int, a: int, lower: int) -> FacetRule | None:
        if not self.bound.can_reach_selfsq(d, e, a, lower):
            raise ValueError("single-facet bound called outside the base quadratic feasible set")
        for rule in self.rules:
            if not rule.boundary_can_reach(d, e, a, lower):
                return rule
        return None

    def can_reach_after_all_single_facets(self, d: int, e: int, a: int, lower: int) -> bool:
        return self.first_pruning_rule(d, e, a, lower) is None

    @classmethod
    def from_retained(cls, marking: dict, bundle: dict) -> "DirectPicardAll140SingleFacetBound":
        bound = DirectPicardSliceQuadraticBound.from_retained(marking, bundle)
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        gram = Matrix(bundle["picard_gram_64x64"])
        gram_inv = gram.inv()
        phi = Matrix([
            list(bound.bridge.degree_functional),
            list(bound.bridge.exceptional_mass_functional),
            list(bound.bridge.first_normal_half_functional),
        ])
        M = phi * gram_inv * phi.T
        if M.shape != (3, 3) or M.det() == 0:
            raise ValueError("base direct-slice target Gram regression")
        M_inv = M.inv()
        x0_map = gram_inv * phi.T * M_inv
        if x0_map.shape != (64, 3):
            raise ValueError("unconstrained maximizer map shape regression")

        grouped: dict[tuple, list[int]] = {}
        rule_payloads: dict[tuple, dict] = {}
        dependent_count = 0
        independent_count = 0

        for k in range(KNOWN_CURVE_COUNT):
            l = adapter.pairing_matrix[k, :]
            q = l * x0_map
            q_den, q_num = rational_vector_payload(q)
            psi = phi.col_join(l)
            rank = int(psi.rank())
            if rank == 3:
                dependent_count += 1
                signature = ("fixed", q_den, q_num)
                payload = {
                    "fixed_on_slice": True,
                    "trigger_denominator": q_den,
                    "trigger_numerators": q_num,
                    "boundary_denominator": None,
                    "boundary_integer_matrix": None,
                }
            elif rank == 4:
                independent_count += 1
                N = psi * gram_inv * psi.T
                if N.shape != (4, 4) or N.det() == 0:
                    raise ValueError(f"curve {k+1}: augmented target Gram is singular")
                H = N.inv()[:3, :3]
                h_den, h_rows = rational_matrix_payload_3(H)
                signature = ("facet", q_den, q_num, h_den, h_rows)
                payload = {
                    "fixed_on_slice": False,
                    "trigger_denominator": q_den,
                    "trigger_numerators": q_num,
                    "boundary_denominator": h_den,
                    "boundary_integer_matrix": h_rows,
                }
            else:
                raise ValueError(f"curve {k+1}: unexpected augmented rank {rank}")
            grouped.setdefault(signature, []).append(k + 1)
            rule_payloads[signature] = payload

        rules = []
        for rule_id, signature in enumerate(sorted(grouped, key=repr)):
            payload = rule_payloads[signature]
            rules.append(FacetRule(
                rule_id=rule_id,
                known_curve_labels_1based=tuple(grouped[signature]),
                fixed_on_slice=bool(payload["fixed_on_slice"]),
                trigger_denominator=int(payload["trigger_denominator"]),
                trigger_numerators=tuple(int(v) for v in payload["trigger_numerators"]),
                boundary_denominator=(None if payload["boundary_denominator"] is None else int(payload["boundary_denominator"])),
                boundary_integer_matrix=(
                    None if payload["boundary_integer_matrix"] is None else tuple(
                        tuple(int(v) for v in row) for row in payload["boundary_integer_matrix"]
                    )
                ),
            ))

        cert_rules = [{
            "rule_id": r.rule_id,
            "known_curve_labels_1based": list(r.known_curve_labels_1based),
            "multiplicity": len(r.known_curve_labels_1based),
            "fixed_on_slice": r.fixed_on_slice,
            "trigger_linear_form": {
                "denominator": r.trigger_denominator,
                "integer_coefficients_d_e_a": list(r.trigger_numerators),
            },
            "boundary_upper_quadratic": None if r.fixed_on_slice else {
                "denominator": r.boundary_denominator,
                "integer_matrix": [list(row) for row in r.boundary_integer_matrix or ()],
            },
        } for r in rules]

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_ALL140_SINGLE_FACET_BOUND_V1",
            "mode": "EXACT_MINIMUM_OF_140_SINGLE_HALFSPACE_CONTINUOUS_QUADRATIC_UPPER_BOUNDS",
            "quadratic_bound_certificate_sha256": bound.certificate["canonical_sha256_without_this_field"],
            "adapter_certificate_sha256": adapter.certificate["canonical_sha256_without_this_field"],
            "known_curve_count": KNOWN_CURVE_COUNT,
            "augmented_rank3_fixed_functional_count": dependent_count,
            "augmented_rank4_true_facet_count": independent_count,
            "unique_exact_facet_rule_count": len(rules),
            "rule_multiplicity_sum": sum(len(r.known_curve_labels_1based) for r in rules),
            "rules": cert_rules,
            "proof": {
                "unconstrained_slice_maximizer": "x0=G^-1*phi^T*(phi*G^-1*phi^T)^-1*t",
                "facet_trigger": "if <x0,K_i> >= 0 the one-facet bound equals the base bound",
                "violated_facet_boundary": "if <x0,K_i> < 0, strict concavity on ker(phi) forces the maximum over <x,K_i>>=0 to the boundary <x,K_i>=0",
                "boundary_max": "[t,0]^T*(Psi_i*G^-1*Psi_i^T)^-1*[t,0]",
                "intersection_upper_bound": "max over all140 halfspaces <= min_i(max over the i-th halfspace)",
                "safe_necessary_prune": True,
                "integrality_not_used": True,
                "closest_vector_search_run": False,
            },
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        if cert["rule_multiplicity_sum"] != KNOWN_CURVE_COUNT:
            raise ValueError("facet rule multiplicity regression")
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(bound=bound, rules=tuple(rules), certificate=cert)
