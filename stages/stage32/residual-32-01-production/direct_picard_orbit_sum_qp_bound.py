#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import itertools
import json
import math
from dataclasses import dataclass

import sympy
from sympy import Matrix

from direct_picard_slice_stabilizer_orbit_bound import DirectPicardSliceStabilizerOrbitBound
from hperp_integral_adapter import HperpIntegralPairingAdapter


EXPECTED_QUOTIENT_RANK = 2
EXPECTED_NONFIXED_ORBIT_COUNT = 10


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def rational_linear_payload(v: Matrix) -> tuple[int, tuple[int, int, int]]:
    if v.shape == (3, 1):
        v = v.T
    if v.shape != (1, 3):
        raise ValueError(f"expected 1x3 linear form, got {v.shape}")
    den = 1
    for x in v:
        den = math.lcm(den, int(sympy.denom(x)))
    nums = tuple(int(v[0, j] * den) for j in range(3))
    g = den
    for n in nums:
        g = math.gcd(g, abs(n))
    if g > 1:
        den //= g
        nums = tuple(n // g for n in nums)
    if den <= 0:
        raise ValueError("linear denominator must be positive")
    return den, nums


def rational_quadratic_payload(m: Matrix) -> tuple[int, tuple[tuple[int, int, int], ...]]:
    if m.shape != (3, 3) or m != m.T:
        raise ValueError(f"expected symmetric 3x3 matrix, got {m.shape}")
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
    if den <= 0:
        raise ValueError("quadratic denominator must be positive")
    return den, rows


def eval_linear(nums: tuple[int, int, int], t: tuple[int, int, int]) -> int:
    return sum(nums[i] * t[i] for i in range(3))


def eval_quadratic(rows: tuple[tuple[int, int, int], ...], t: tuple[int, int, int]) -> int:
    return sum(t[i] * rows[i][j] * t[j] for i in range(3) for j in range(3))


@dataclass(frozen=True)
class OrbitQPKKTCandidate:
    candidate_id: int
    active_orbit_ids: tuple[int, ...]
    feasibility_forms: tuple[tuple[int, tuple[int, int, int]], ...]
    multiplier_forms: tuple[tuple[int, tuple[int, int, int]], ...]
    objective_denominator: int
    objective_integer_matrix: tuple[tuple[int, int, int], ...]

    def valid_for(self, d: int, e: int, a: int) -> bool:
        t = (int(d), int(e), int(a))
        if any(eval_linear(nums, t) < 0 for _, nums in self.feasibility_forms):
            return False
        if any(eval_linear(nums, t) > 0 for _, nums in self.multiplier_forms):
            return False
        return True

    def can_reach_selfsq(self, d: int, e: int, a: int, lower: int) -> bool:
        t = (int(d), int(e), int(a))
        numerator = eval_quadratic(self.objective_integer_matrix, t)
        return numerator >= int(lower) * self.objective_denominator

    def objective_numerator(self, d: int, e: int, a: int) -> int:
        return eval_quadratic(
            self.objective_integer_matrix,
            (int(d), int(e), int(a)),
        )


@dataclass(frozen=True)
class DirectPicardOrbitSumQPBound:
    orbit_model: DirectPicardSliceStabilizerOrbitBound
    nonfixed_orbit_ids: tuple[int, ...]
    quotient_rank: int
    candidates: tuple[OrbitQPKKTCandidate, ...]
    certificate: dict

    @property
    def bound(self):
        return self.orbit_model.bound

    def solve_candidate(self, d: int, e: int, a: int) -> OrbitQPKKTCandidate | None:
        if self.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
            return None
        for candidate in self.candidates:
            if candidate.valid_for(d, e, a):
                return candidate
        return None

    def can_reach_after_orbit_qp(
        self, d: int, e: int, a: int, lower: int
    ) -> tuple[bool, str, OrbitQPKKTCandidate | None]:
        if self.orbit_model.first_negative_fixed_orbit(d, e, a) is not None:
            return False, "FIXED_ORBIT_SUM_NEGATIVE", None
        candidate = None
        for cand in self.candidates:
            if cand.valid_for(d, e, a):
                candidate = cand
                break
        if candidate is None:
            return False, "NONFIXED_ORBIT_POLYHEDRON_INFEASIBLE", None
        if not candidate.can_reach_selfsq(d, e, a, lower):
            return False, "ORBIT_SUM_QP_SELF_INTERSECTION_TOO_LOW", candidate
        return True, "ORBIT_SUM_QP_SURVIVES", candidate

    @classmethod
    def from_retained(
        cls, marking: dict, bundle: dict
    ) -> "DirectPicardOrbitSumQPBound":
        orbit_model = DirectPicardSliceStabilizerOrbitBound.from_retained(marking, bundle)
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        bound = orbit_model.bound
        bridge = bound.bridge

        phi = Matrix([
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ])
        if int(phi.rank()) != 3:
            raise ValueError("slice functional rank regression")
        gram = Matrix(bundle["picard_gram_64x64"])
        gram_inv = gram.inv()

        nonfixed_rules = [r for r in orbit_model.rules if not r.fixed_on_slice]
        if len(nonfixed_rules) != EXPECTED_NONFIXED_ORBIT_COUNT:
            raise ValueError(
                f"nonfixed orbit count regression: {len(nonfixed_rules)} "
                f"!= {EXPECTED_NONFIXED_ORBIT_COUNT}"
            )

        orbit_rows: list[Matrix] = []
        for rule in nonfixed_rules:
            idx = [label - 1 for label in rule.known_curve_labels_1based]
            row = Matrix([[
                sum(int(adapter.pairing_matrix[i, j]) for i in idx)
                for j in range(64)
            ]])
            orbit_rows.append(row)
        L = Matrix.vstack(*orbit_rows)

        quotient_rank = int(phi.col_join(L).rank()) - 3
        if quotient_rank != EXPECTED_QUOTIENT_RANK:
            raise ValueError(
                f"orbit-sum quotient rank regression: {quotient_rank} "
                f"!= {EXPECTED_QUOTIENT_RANK}"
            )

        candidates: list[OrbitQPKKTCandidate] = []
        dependent_active_sets = 0
        candidate_id = 0

        for active_size in range(quotient_rank + 1):
            for active_positions in itertools.combinations(
                range(len(nonfixed_rules)), active_size
            ):
                active_rows = [orbit_rows[i] for i in active_positions]
                psi = phi
                if active_rows:
                    psi = phi.col_join(Matrix.vstack(*active_rows))
                expected_rank = 3 + active_size
                if int(psi.rank()) != expected_rank:
                    dependent_active_sets += 1
                    continue

                N = psi * gram_inv * psi.T
                if N.det() == 0:
                    raise ValueError(
                        f"active set unexpectedly singular: {active_positions}"
                    )
                N_inv = N.inv()
                xmap = gram_inv * psi.T * N_inv[:, :3]
                if xmap.shape != (64, 3):
                    raise ValueError("KKT xmap shape regression")
                if phi * xmap != Matrix.eye(3):
                    raise ValueError(
                        f"active set {active_positions}: slice reconstruction failed"
                    )
                for r in active_rows:
                    if r * xmap != Matrix.zeros(1, 3):
                        raise ValueError(
                            f"active set {active_positions}: active boundary failed"
                        )

                feasibility = tuple(
                    rational_linear_payload(row * xmap)
                    for row in orbit_rows
                )
                multipliers = tuple(
                    rational_linear_payload(N_inv[3 + k, :3])
                    for k in range(active_size)
                )
                qden, qrows = rational_quadratic_payload(N_inv[:3, :3])

                candidates.append(OrbitQPKKTCandidate(
                    candidate_id=candidate_id,
                    active_orbit_ids=tuple(
                        nonfixed_rules[i].orbit_id for i in active_positions
                    ),
                    feasibility_forms=feasibility,
                    multiplier_forms=multipliers,
                    objective_denominator=qden,
                    objective_integer_matrix=qrows,
                ))
                candidate_id += 1

        expected_subset_upper = sum(
            math.comb(len(nonfixed_rules), k)
            for k in range(quotient_rank + 1)
        )
        if len(candidates) + dependent_active_sets != expected_subset_upper:
            raise ValueError("active-set accounting regression")

        cert_candidates = [{
            "candidate_id": c.candidate_id,
            "active_orbit_ids": list(c.active_orbit_ids),
            "active_size": len(c.active_orbit_ids),
            "feasibility_forms": [{
                "denominator": den,
                "integer_coefficients_d_e_a": list(nums),
            } for den, nums in c.feasibility_forms],
            "active_multiplier_forms_must_be_nonpositive": [{
                "denominator": den,
                "integer_coefficients_d_e_a": list(nums),
            } for den, nums in c.multiplier_forms],
            "objective_upper_quadratic": {
                "denominator": c.objective_denominator,
                "integer_matrix": [list(row) for row in c.objective_integer_matrix],
            },
        } for c in candidates]

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_ORBIT_SUM_EXACT_KKT_QP_BOUND_V1",
            "mode": "EXACT_CONTINUOUS_MAX_SELF_INTERSECTION_UNDER_ALL_14_STABILIZER_ORBIT_SUM_NONNEGATIVITY_CONSTRAINTS",
            "stabilizer_orbit_certificate_sha256": orbit_model.certificate[
                "canonical_sha256_without_this_field"
            ],
            "adapter_certificate_sha256": adapter.certificate[
                "canonical_sha256_without_this_field"
            ],
            "nonfixed_orbit_count": len(nonfixed_rules),
            "nonfixed_orbit_ids": [r.orbit_id for r in nonfixed_rules],
            "orbit_sum_quotient_rank_mod_phi": quotient_rank,
            "active_set_size_complete_through": quotient_rank,
            "active_set_subset_upper_count": expected_subset_upper,
            "independent_kkt_candidate_count": len(candidates),
            "dependent_active_set_count": dependent_active_sets,
            "candidates": cert_candidates,
            "proof": {
                "slice_kernel_strictly_negative_definite": True,
                "objective_strictly_concave_on_each_d_e_a_slice": True,
                "feasible_region": "intersection of ten nonfixed orbit-sum halfspaces after four fixed orbit-sum gates",
                "kkt_sufficient": True,
                "active_multiplier_sign": "for Lx>=0 at a maximum, the equality coefficient on an active L row is -mu/2 <= 0",
                "quotient_normal_space_dimension": quotient_rank,
                "conic_caratheodory_active_bound": quotient_rank,
                "enumeration_complete": True,
                "all140_nonnegative_implies_all_orbit_sums_nonnegative": True,
                "orbit_sum_qp_is_safe_relaxation_of_all140_nonnegative_cone": True,
                "individual_within_orbit_nonnegativity_not_yet_imposed": True,
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
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            orbit_model=orbit_model,
            nonfixed_orbit_ids=tuple(r.orbit_id for r in nonfixed_rules),
            quotient_rank=quotient_rank,
            candidates=tuple(candidates),
            certificate=cert,
        )
