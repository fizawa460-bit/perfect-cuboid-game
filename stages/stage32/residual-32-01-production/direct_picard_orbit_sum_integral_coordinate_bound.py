#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction

import sympy
from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from direct_picard_orbit_sum_qp_bound import DirectPicardOrbitSumQPBound, OrbitQPKKTCandidate
from hperp_integral_adapter import HperpIntegralPairingAdapter


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def as_fraction(value: sympy.Expr) -> Fraction:
    return Fraction(int(sympy.numer(value)), int(sympy.denom(value)))


def affine_row_payload(row: Matrix) -> tuple[int, tuple[int, int, int]]:
    if row.shape == (3, 1):
        row = row.T
    if row.shape != (1, 3):
        raise ValueError(f"expected 1x3 row, got {row.shape}")
    den = 1
    for v in row:
        den = sympy.ilcm(den, int(sympy.denom(v)))
    nums = tuple(int(row[0, j] * den) for j in range(3))
    g = den
    for n in nums:
        g = sympy.igcd(g, abs(n))
    if g > 1:
        den //= g
        nums = tuple(n // g for n in nums)
    return int(den), nums


@dataclass(frozen=True)
class CoordinatePenaltyRow:
    affine_denominator: int
    affine_numerators: tuple[int, int, int]
    inverse_diagonal_numerator: int
    inverse_diagonal_denominator: int

    def distance_numerator(self, d: int, e: int, a: int) -> int:
        raw = sum(
            self.affine_numerators[i] * (int(d), int(e), int(a))[i]
            for i in range(3)
        )
        r = raw % self.affine_denominator
        return min(r, self.affine_denominator - r)

    def exceeds_slack(
        self,
        d: int,
        e: int,
        a: int,
        *,
        slack_numerator: int,
        slack_denominator: int,
    ) -> bool:
        r = self.distance_numerator(d, e, a)
        if r == 0:
            return False
        # lb = (r/den)^2 / (B^-1)_ii
        #     = r^2 * invdiag_den / (den^2 * invdiag_num).
        lhs = (
            r * r
            * self.inverse_diagonal_denominator
            * int(slack_denominator)
        )
        rhs = (
            int(slack_numerator)
            * self.affine_denominator
            * self.affine_denominator
            * self.inverse_diagonal_numerator
        )
        return lhs > rhs


@dataclass(frozen=True)
class KKTCandidateIntegralPenalty:
    candidate_id: int
    active_orbit_ids: tuple[int, ...]
    rows: tuple[CoordinatePenaltyRow, ...]
    coordinate_affine_sha256: str

    def can_reach_after_coordinate_integrality_lb(
        self,
        candidate: OrbitQPKKTCandidate,
        d: int,
        e: int,
        a: int,
        lower: int,
    ) -> bool:
        objective_num = candidate.objective_numerator(d, e, a)
        slack_num = objective_num - int(lower) * candidate.objective_denominator
        if slack_num < 0:
            return False
        for row in self.rows:
            if row.exceeds_slack(
                d, e, a,
                slack_numerator=slack_num,
                slack_denominator=candidate.objective_denominator,
            ):
                return False
        return True


@dataclass(frozen=True)
class DirectPicardOrbitSumKKTIntegralCoordinateBound:
    kkt: DirectPicardOrbitSumQPBound
    penalties: tuple[KKTCandidateIntegralPenalty, ...]
    certificate: dict

    def penalty_for(self, candidate_id: int) -> KKTCandidateIntegralPenalty:
        return self.penalties[int(candidate_id)]

    @classmethod
    def from_retained(
        cls, marking: dict, bundle: dict
    ) -> "DirectPicardOrbitSumKKTIntegralCoordinateBound":
        kkt = DirectPicardOrbitSumQPBound.from_retained(marking, bundle)
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        bound = kkt.bound
        bridge = bound.bridge
        gram = Matrix(bundle["picard_gram_64x64"])
        gram_inv = gram.inv()
        phi = Matrix([
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ])

        # Saturated integral Smith coordinates for every fixed-(d,e,a) slice.
        phi_dm = DomainMatrix.from_Matrix(phi).convert_to(ZZ)
        D_dm, S_dm, T_dm = smith_normal_decomp(phi_dm)
        if S_dm * phi_dm * T_dm != D_dm:
            raise ValueError("Smith decomposition reconstruction regression")
        D = D_dm.to_Matrix()
        S = S_dm.to_Matrix()
        T = T_dm.to_Matrix()
        diagonal = tuple(int(D[i, i]) for i in range(3))
        if diagonal != (1, 2, 2):
            raise ValueError(f"direct-slice Smith diagonal regression: {diagonal}")
        if abs(int(T.det())) != 1 or abs(int(S.det())) != 1:
            raise ValueError("Smith transforms are not unimodular")
        T_inv = T.inv()
        transformed = T.T * gram * T
        B = -transformed[3:, 3:]
        if B.shape != (61, 61) or B != B.T:
            raise ValueError("slice-kernel positive Gram regression")
        B_inv = B.inv()
        inv_diag = tuple(as_fraction(B_inv[i, i]) for i in range(61))
        if any(v <= 0 for v in inv_diag):
            raise ValueError("slice-kernel inverse diagonal is not positive")

        diag3 = Matrix.diag(*diagonal)
        zfirst_map = diag3.inv() * S

        nonfixed_row_by_orbit: dict[int, Matrix] = {}
        for rule in kkt.orbit_model.rules:
            if rule.fixed_on_slice:
                continue
            idx = [label - 1 for label in rule.known_curve_labels_1based]
            nonfixed_row_by_orbit[rule.orbit_id] = Matrix([[
                sum(int(adapter.pairing_matrix[i, j]) for i in idx)
                for j in range(64)
            ]])

        penalties: list[KKTCandidateIntegralPenalty] = []
        row_payload_hashes = []
        for candidate in kkt.candidates:
            active_rows = [
                nonfixed_row_by_orbit[orbit_id]
                for orbit_id in candidate.active_orbit_ids
            ]
            psi = phi if not active_rows else phi.col_join(Matrix.vstack(*active_rows))
            N = psi * gram_inv * psi.T
            if N.det() == 0:
                raise ValueError(f"candidate {candidate.candidate_id}: singular active Gram")
            xmap = gram_inv * psi.T * N.inv()[:, :3]
            if phi * xmap != Matrix.eye(3):
                raise ValueError(f"candidate {candidate.candidate_id}: slice map regression")
            for r in active_rows:
                if r * xmap != Matrix.zeros(1, 3):
                    raise ValueError(f"candidate {candidate.candidate_id}: active boundary regression")

            zmap = T_inv * xmap
            if zmap[:3, :] != zfirst_map:
                raise ValueError(f"candidate {candidate.candidate_id}: Smith fixed-coordinate regression")
            vmap = zmap[3:, :]
            if vmap.shape != (61, 3):
                raise ValueError("candidate kernel-center shape regression")

            rows: list[CoordinatePenaltyRow] = []
            payload = []
            for i in range(61):
                den, nums = affine_row_payload(vmap[i, :])
                invd = inv_diag[i]
                rows.append(CoordinatePenaltyRow(
                    affine_denominator=den,
                    affine_numerators=nums,
                    inverse_diagonal_numerator=invd.numerator,
                    inverse_diagonal_denominator=invd.denominator,
                ))
                payload.append({
                    "coordinate": i,
                    "affine_denominator": den,
                    "affine_numerators_d_e_a": list(nums),
                    "B_inv_diagonal": [invd.numerator, invd.denominator],
                })
            digest = csha(payload)
            row_payload_hashes.append({
                "candidate_id": candidate.candidate_id,
                "active_orbit_ids": list(candidate.active_orbit_ids),
                "coordinate_affine_sha256": digest,
            })
            penalties.append(KKTCandidateIntegralPenalty(
                candidate_id=candidate.candidate_id,
                active_orbit_ids=candidate.active_orbit_ids,
                rows=tuple(rows),
                coordinate_affine_sha256=digest,
            ))

        if [p.candidate_id for p in penalties] != list(range(len(kkt.candidates))):
            raise ValueError("candidate penalty indexing regression")

        cert = {
            "schema": "STAGE32_RESIDUAL32_01_DIRECT_PICARD_ORBIT_KKT_INTEGRAL_COORDINATE_BOUND_V1",
            "mode": "EXACT_COORDINATE_CAUCHY_INTEGRALITY_LOSS_FROM_EACH_ALL140_CONTINUOUS_KKT_MAXIMIZER",
            "orbit_kkt_certificate_sha256": kkt.certificate[
                "canonical_sha256_without_this_field"
            ],
            "hperp_integral_adapter_certificate_sha256": adapter.certificate[
                "canonical_sha256_without_this_field"
            ],
            "smith_diagonal": list(diagonal),
            "slice_kernel_rank": 61,
            "kkt_candidate_count": len(kkt.candidates),
            "penalty_candidate_count": len(penalties),
            "candidate_coordinate_hashes": row_payload_hashes,
            "proof": {
                "smith_last61_are_saturated_integral_kernel_coordinates": True,
                "each_kkt_center_is_exact_affine_function_of_d_e_a": True,
                "for_feasible_integral_displacement_active_pairings_are_nonnegative": True,
                "kkt_active_equality_coefficients_are_nonpositive": True,
                "linear_cross_term_from_active_constraints_is_nonpositive": True,
                "self_intersection_at_integral_feasible_point_at_most_kkt_optimum_minus_kernel_quadratic_distance": True,
                "coordinate_cauchy_lower_bound": "dist(v*_i,Z)^2/(B^-1)_ii <= (v-v*)^T B (v-v*)",
                "closest_vector_search_run": False,
                "safe_prune_if_any_coordinate_lower_bound_exceeds_kkt_slack": True,
            },
            "numerical_row_complete": False,
            "theorem_credit": False,
            "receiver_credit": False,
            "route_credit": False,
            "perfect_cuboid_existence_claim": False,
            "perfect_cuboid_nonexistence_claim": False,
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(kkt=kkt, penalties=tuple(penalties), certificate=cert)
