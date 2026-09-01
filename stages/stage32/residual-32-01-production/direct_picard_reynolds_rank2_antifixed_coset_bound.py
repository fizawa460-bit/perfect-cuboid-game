#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

from direct_picard_reynolds_lattice_diagnostic import csha, load_retained
from direct_picard_reynolds_rank2_integer_qp import (
    OBJECTIVE_DENOMINATOR,
    ceil_div,
    dot,
    integer_nonnegative_interval,
    quad,
)
from direct_picard_reynolds_rank2_quotient_class_map import (
    ReynoldsRank2QuotientClassMap,
)


def fraction_stream_sha256(values: tuple[Fraction, ...]) -> str:
    h = hashlib.sha256()
    for value in values:
        h.update(str(value.numerator).encode())
        h.update(b"/")
        h.update(str(value.denominator).encode())
        h.update(b"\n")
    return h.hexdigest()


@dataclass(frozen=True)
class ReynoldsRank2AntiFixedCosetBound:
    mapping: ReynoldsRank2QuotientClassMap
    coset_lower_bounds: tuple[Fraction, ...]
    certificate: dict

    @property
    def rank2(self):
        return self.mapping.rank2

    def coset_lower_bound(self, d: int, e: int, a: int) -> Fraction | None:
        coset_id = self.mapping.coset_id(d, e, a)
        if coset_id is None:
            return None
        return self.coset_lower_bounds[coset_id]

    def can_reach_selfsq(
        self, d: int, e: int, a: int, lower: int
    ) -> tuple[bool, str, int, tuple[int, int] | None, Fraction | None]:
        """Exact necessary condition using a safe anti-fixed penalty per rank2 coset.

        The fixed rank2 coordinates vary by u,v. Their projection residues vary
        inside one exact subgroup coset. Let lambda_coset be the minimum 32-21aa
        penalty on that coset. Every integral lift then satisfies

            x^2 <= p^2 - lambda(residue) <= p^2 - lambda_coset.

        We therefore solve the same exact 2D concave integer QP as the existing
        rank2 evaluator, but raise the required projected self-intersection by
        the exact rational lambda_coset. False safely prunes the original slice;
        True remains only a necessary-condition survivor.
        """
        rank2 = self.rank2
        z0 = rank2.affine_origin(d, e, a)
        if z0 is None:
            return False, "PROJECTED_SLICE_NOT_IN_INTEGER_IMAGE", 0, None, None

        coset_id = self.mapping.coset_id(d, e, a)
        if coset_id is None:
            raise ValueError("affine origin exists but quotient coset id is missing")
        penalty = self.coset_lower_bounds[coset_id]
        scale = penalty.denominator
        penalty_numerator = penalty.numerator

        dlin = 2 * dot(z0, rank2.kernel_h0)
        elin = 2 * dot(z0, rank2.kernel_h1)
        base_const = quad(rank2.hessian, z0) - int(lower) * OBJECTIVE_DENOMINATOR

        # Multiply the full projected objective by the positive penalty
        # denominator, then subtract 4096*penalty_numerator. This keeps every
        # coefficient integral and avoids floating-point/rational root logic.
        A = rank2.objective_uu * scale
        B = rank2.objective_uv_twice * scale
        C = rank2.objective_vv * scale
        D = dlin * scale
        E = elin * scale
        F = base_const * scale - OBJECTIVE_DENOMINATOR * penalty_numerator
        if not (A < 0 and C < 0 and 4 * A * C - B * B > 0):
            raise ValueError("anti-fixed coset rank2 objective lost strict concavity")

        delta2 = B * B - 4 * C * A
        delta1 = 2 * B * E - 4 * C * D
        delta0 = E * E - 4 * C * F
        urange = integer_nonnegative_interval(delta2, delta1, delta0)
        if urange is None:
            return (
                False,
                "ANTIFIXED_COSET_PROJECTED_CONTINUOUS_TOO_LOW",
                0,
                None,
                penalty,
            )

        gammas = tuple(dot(row, z0) for row in rank2.fixed_halfspace_rows)
        u_lo, u_hi = urange
        center_den = -2 * delta2
        center_floor = delta1 // center_den
        center = min(max(center_floor, u_lo), u_hi)
        checked = 0

        def try_u(u: int) -> tuple[bool, tuple[int, int] | None]:
            nonlocal checked
            checked += 1
            v_lo: int | None = None
            v_hi: int | None = None
            for alpha, beta, gamma in zip(
                rank2.halfspace_u, rank2.halfspace_v, gammas
            ):
                s = alpha * u + gamma
                if beta > 0:
                    bound = ceil_div(-s, beta)
                    v_lo = bound if v_lo is None else max(v_lo, bound)
                elif beta < 0:
                    bound = s // (-beta)
                    v_hi = bound if v_hi is None else min(v_hi, bound)
                elif s < 0:
                    return False, None
                if v_lo is not None and v_hi is not None and v_lo > v_hi:
                    return False, None

            linear_v = B * u + E
            const_v = A * u * u + D * u + F
            vertex_den = -2 * C
            vf = linear_v // vertex_den
            candidates = {vf, vf + 1}
            if v_lo is not None:
                candidates.add(v_lo)
            if v_hi is not None:
                candidates.add(v_hi)

            for v in tuple(candidates):
                if v_lo is not None and v < v_lo:
                    v = v_lo
                if v_hi is not None and v > v_hi:
                    v = v_hi
                if v_lo is not None and v_hi is not None and v_lo > v_hi:
                    continue
                q = C * v * v + linear_v * v + const_v
                if q >= 0:
                    return True, (u, v)
            return False, None

        ok, witness = try_u(center)
        if ok:
            return True, "ANTIFIXED_COSET_BOUND_SURVIVES", checked, witness, penalty
        step = 1
        while center - step >= u_lo or center + step <= u_hi:
            if center - step >= u_lo:
                ok, witness = try_u(center - step)
                if ok:
                    return True, "ANTIFIXED_COSET_BOUND_SURVIVES", checked, witness, penalty
            if center + step <= u_hi:
                ok, witness = try_u(center + step)
                if ok:
                    return True, "ANTIFIXED_COSET_BOUND_SURVIVES", checked, witness, penalty
            step += 1

        return False, "ANTIFIXED_COSET_BOUND_EXHAUSTED", checked, None, penalty

    @classmethod
    def from_retained(
        cls, marking: dict, bundle: dict
    ) -> "ReynoldsRank2AntiFixedCosetBound":
        mapping = ReynoldsRank2QuotientClassMap.from_retained(marking, bundle)
        coset_count = len(mapping.coset_representatives)
        buckets: list[list[Fraction]] = [[] for _ in range(coset_count)]

        for residue in mapping.sorted_projection_residues:
            coset_id = mapping.residue_to_coset_id[residue]
            penalty = mapping.penalty.lower_bound_from_residue(residue)
            buckets[coset_id].append(penalty)

        expected_coset_size = len(mapping.free_subgroup)
        if any(len(bucket) != expected_coset_size for bucket in buckets):
            raise ValueError("rank2 free quotient coset size regression in penalty table")
        lower_bounds = tuple(min(bucket) for bucket in buckets)

        # Exhaustive 16,384-state safety check: the coset minimum is no larger
        # than the exact 32-21aa coordinate-Cauchy penalty for every residue.
        for residue in mapping.sorted_projection_residues:
            coset_id = mapping.residue_to_coset_id[residue]
            penalty = mapping.penalty.lower_bound_from_residue(residue)
            if lower_bounds[coset_id] > penalty:
                raise ValueError("coset lower bound exceeded a member penalty")

        zero_cosets = sum(1 for value in lower_bounds if value == 0)
        if zero_cosets != 1:
            raise ValueError(f"expected exactly one zero-minimum free coset, got {zero_cosets}")
        positive = tuple(value for value in lower_bounds if value > 0)
        if len(positive) != coset_count - 1:
            raise ValueError("positive free-coset lower-bound count regression")

        cert = {
            "schema": "STAGE32_21AC_CHEAP_EXACT_ANTIFIXED_COSET_BOUND_V1",
            "mode": "EXACT_MINIMUM_32_21AA_PENALTY_ON_EACH_RANK2_UV_QUOTIENT_COSET",
            "quotient_class_map_sha256": mapping.certificate[
                "canonical_sha256_without_this_field"
            ],
            "anti_fixed_penalty_model_sha256": mapping.penalty.certificate[
                "canonical_sha256_without_this_field"
            ],
            "rank2_model_sha256": mapping.rank2.certificate[
                "canonical_sha256_without_this_field"
            ],
            "projection_class_count": len(mapping.sorted_projection_residues),
            "rank2_free_subgroup_order": len(mapping.free_subgroup),
            "rank2_free_quotient_coset_count": coset_count,
            "zero_minimum_coset_count": zero_cosets,
            "positive_minimum_coset_count": len(positive),
            "distinct_coset_lower_bound_count": len(set(lower_bounds)),
            "minimum_positive_coset_lower_bound": [
                min(positive).numerator,
                min(positive).denominator,
            ],
            "maximum_coset_lower_bound": [
                max(positive).numerator,
                max(positive).denominator,
            ],
            "coset_lower_bound_stream_sha256": fraction_stream_sha256(lower_bounds),
            "pruning_rule": (
                "for a projected slice t, all rank2 (u,v) residues lie in one exact free-subgroup coset C; "
                "lambda_C=min_{r in C} lambda_32_21aa(r), so every integral lift satisfies "
                "x^2<=p^2-lambda_C; exhaust the same exact rank2 integer QP against lower+lambda_C"
            ),
            "proof": {
                "every_rank2_affine_slice_occupies_one_exact_uv_coset": True,
                "all_16384_projection_residues_partitioned_exactly": True,
                "each_coset_size_equals_free_subgroup_order": True,
                "coset_minimum_checked_against_every_member_penalty": True,
                "lambda_coset_le_lambda_residue_le_minus_q_square": True,
                "therefore_x_square_le_p_square_minus_lambda_coset": True,
                "rank2_integer_qp_with_rational_threshold_scaled_to_exact_integers": True,
                "floating_point_used": False,
                "terminal_family_materialization_run": False,
                "anti_fixed_59d_closest_vector_search_run": False,
            },
            "safe_semantics": {
                "false_decision_prunes_original_integral_picard_slice": True,
                "true_decision_only_necessary_condition": True,
                "this_certificate_does_not_run_full178_census": True,
                "numerical_row_complete": False,
                "theorem_credit": False,
                "receiver_credit": False,
                "route_credit": False,
                "perfect_cuboid_existence_claim": False,
                "perfect_cuboid_nonexistence_claim": False,
            },
            "boundary": "32-21aa_to_32-21ac_work_package_ready_for_fresh_audit_after_exact_CI",
            "next_after_audit": "32-21ad FULL178 compressed numerical census in a separate execution phase/PR",
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            mapping=mapping,
            coset_lower_bounds=lower_bounds,
            certificate=cert,
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21ac_picard")
    marking = load_retained(args.marking, "s32_21ac_marking")
    model = ReynoldsRank2AntiFixedCosetBound.from_retained(marking, bundle)
    args.output.write_text(json.dumps(model.certificate, indent=2, sort_keys=True) + "\n")
    cert = model.certificate
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AC_CHEAP_EXACT_ANTIFIXED_COSET_BOUND",
        "projection_class_count": cert["projection_class_count"],
        "free_subgroup_order": cert["rank2_free_subgroup_order"],
        "free_quotient_coset_count": cert["rank2_free_quotient_coset_count"],
        "zero_minimum_coset_count": cert["zero_minimum_coset_count"],
        "positive_minimum_coset_count": cert["positive_minimum_coset_count"],
        "minimum_positive_coset_lower_bound": cert["minimum_positive_coset_lower_bound"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
