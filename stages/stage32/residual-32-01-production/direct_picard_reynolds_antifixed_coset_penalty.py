#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
import math
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

import sympy
from sympy import Matrix, ZZ
from sympy.polys.matrices import DomainMatrix
from sympy.polys.matrices.normalforms import smith_normal_decomp

from direct_picard_reynolds_lattice_diagnostic import (
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    exact_column_lattice_basis_lowrank,
    load_retained,
)
from direct_picard_reynolds_rank2_integral_projection_bound import (
    build_reynolds_numerator,
)
from direct_picard_slice_bridge import DirectPicardSliceBridge
from hperp_integral_adapter import HperpIntegralPairingAdapter

EXPECTED_FIXED_RANK = 5
EXPECTED_SLICE_RANK = 3
EXPECTED_SLICE_KERNEL_RANK = 61
EXPECTED_PROJECTION_CLASS_COUNT = 16384
EXPECTED_SLICE_SMITH_DIAGONAL = (1, 2, 2)


def as_fraction(value: sympy.Expr) -> Fraction:
    return Fraction(int(sympy.numer(value)), int(sympy.denom(value)))


def matrix_int_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def add_mod(a: tuple[int, ...], b: tuple[int, ...]) -> tuple[int, ...]:
    return tuple((x + y) % GROUP_ORDER for x, y in zip(a, b))


def generator_residue(column: Matrix) -> tuple[int, ...]:
    return tuple(int(column[i, 0]) % GROUP_ORDER for i in range(column.rows))


def extend_subgroup(
    subgroup: set[tuple[int, ...]], generator: tuple[int, ...]
) -> tuple[set[tuple[int, ...]], int]:
    zero = (0,) * len(generator)
    if generator in subgroup:
        return subgroup, 1

    multiples = [zero]
    current = zero
    relative_order = None
    for k in range(1, GROUP_ORDER + 1):
        current = add_mod(current, generator)
        if current in subgroup:
            relative_order = k
            break
        multiples.append(current)
    if relative_order is None:
        raise ValueError("projection-class generator order did not divide Reynolds modulus")

    old = tuple(subgroup)
    enlarged = {
        add_mod(h, multiple)
        for h in old
        for multiple in multiples
    }
    expected = len(subgroup) * relative_order
    if len(enlarged) != expected:
        raise ValueError(
            f"projection-class subgroup collision regression: {len(enlarged)} != {expected}"
        )
    return enlarged, relative_order


def penalty_stream_sha256(
    reps: list[tuple[int, ...]], penalties: list[Fraction]
) -> str:
    if len(reps) != len(penalties):
        raise ValueError("penalty stream length mismatch")
    h = hashlib.sha256()
    for rep, penalty in zip(reps, penalties):
        h.update(bytes(rep))
        h.update(str(penalty.numerator).encode())
        h.update(b"/")
        h.update(str(penalty.denominator).encode())
        h.update(b"\n")
    return h.hexdigest()


@dataclass(frozen=True)
class ReynoldsAntiFixedCosetPenalty:
    fixed_image_basis: tuple[tuple[int, ...], ...]
    coordinate_dual_norms: tuple[Fraction, ...]
    certificate: dict

    def projection_residue_from_z(self, z: tuple[int, ...]) -> tuple[int, ...]:
        if len(z) != EXPECTED_FIXED_RANK:
            raise ValueError(f"expected {EXPECTED_FIXED_RANK} projected coordinates")
        return tuple(
            sum(self.fixed_image_basis[i][j] * int(z[j]) for j in range(EXPECTED_FIXED_RANK))
            % GROUP_ORDER
            for i in range(PICARD_RANK)
        )

    def lower_bound_from_residue(self, residue: tuple[int, ...]) -> Fraction:
        if len(residue) != PICARD_RANK:
            raise ValueError(f"expected {PICARD_RANK}-coordinate projection residue")
        best = Fraction(0, 1)
        for i, raw in enumerate(residue):
            r = int(raw)
            if not 0 <= r < GROUP_ORDER:
                raise ValueError("projection residue outside canonical range 0..63")
            distance_numerator = min(r, GROUP_ORDER - r)
            if distance_numerator == 0:
                continue
            dual_norm = self.coordinate_dual_norms[i]
            if dual_norm <= 0:
                raise ValueError(
                    "nonzero fractional anti-fixed coordinate has zero slice-kernel dual norm"
                )
            candidate = (
                Fraction(distance_numerator * distance_numerator, GROUP_ORDER * GROUP_ORDER)
                / dual_norm
            )
            if candidate > best:
                best = candidate
        return best

    @classmethod
    def from_retained(
        cls, marking: dict, bundle: dict
    ) -> "ReynoldsAntiFixedCosetPenalty":
        adapter = HperpIntegralPairingAdapter.from_retained(marking, bundle)
        bridge = DirectPicardSliceBridge.from_retained(marking, bundle)
        gram = Matrix(bundle["picard_gram_64x64"])
        phi = Matrix([
            list(bridge.degree_functional),
            list(bridge.exceptional_mass_functional),
            list(bridge.first_normal_half_functional),
        ])
        if phi.shape != (EXPECTED_SLICE_RANK, PICARD_RANK) or int(phi.rank()) != EXPECTED_SLICE_RANK:
            raise ValueError(f"slice functional rank/shape regression: {phi.shape}, rank={phi.rank()}")

        N, _, action_hashes_sha = build_reynolds_numerator(marking, adapter, gram, phi)
        if N.T * gram != gram * N:
            raise ValueError("Reynolds numerator Gram self-adjointness regression")
        if phi * N != GROUP_ORDER * phi:
            raise ValueError("Reynolds numerator slice preservation regression")

        fixed_basis, fixed_module_stats = exact_column_lattice_basis_lowrank(
            N, EXPECTED_FIXED_RANK
        )
        if fixed_basis.shape != (PICARD_RANK, EXPECTED_FIXED_RANK):
            raise ValueError(f"fixed image basis shape regression: {fixed_basis.shape}")
        if N * fixed_basis != GROUP_ORDER * fixed_basis:
            raise ValueError("fixed image basis is not Reynolds-fixed")

        generators = [
            generator_residue(fixed_basis[:, j])
            for j in range(fixed_basis.cols)
        ]
        residues: set[tuple[int, ...]] = {(0,) * PICARD_RANK}
        relative_orders: list[int] = []
        subgroup_sizes = [1]
        for generator in generators:
            residues, relative_order = extend_subgroup(residues, generator)
            relative_orders.append(relative_order)
            subgroup_sizes.append(len(residues))
        if len(residues) != EXPECTED_PROJECTION_CLASS_COUNT:
            raise ValueError(
                f"projection class count regression: {len(residues)} != {EXPECTED_PROJECTION_CLASS_COUNT}"
            )
        if math.prod(relative_orders) != EXPECTED_PROJECTION_CLASS_COUNT:
            raise ValueError("projection generator orders do not multiply to class count")

        phi_dm = DomainMatrix.from_Matrix(phi).convert_to(ZZ)
        D_dm, S_dm, T_dm = smith_normal_decomp(phi_dm)
        if S_dm * phi_dm * T_dm != D_dm:
            raise ValueError("slice Smith decomposition reconstruction regression")
        D = D_dm.to_Matrix()
        S = S_dm.to_Matrix()
        T = T_dm.to_Matrix()
        if abs(int(S.det())) != 1 or abs(int(T.det())) != 1:
            raise ValueError("slice Smith transforms are not unimodular")
        slice_smith = tuple(abs(int(D[i, i])) for i in range(EXPECTED_SLICE_RANK))
        if slice_smith != EXPECTED_SLICE_SMITH_DIAGONAL:
            raise ValueError(f"slice Smith diagonal drift: {slice_smith}")

        kernel = T[:, EXPECTED_SLICE_RANK:]
        if kernel.shape != (PICARD_RANK, EXPECTED_SLICE_KERNEL_RANK):
            raise ValueError(f"slice kernel basis shape regression: {kernel.shape}")
        if phi * kernel != Matrix.zeros(EXPECTED_SLICE_RANK, EXPECTED_SLICE_KERNEL_RANK):
            raise ValueError("slice kernel basis regression")

        positive_kernel_gram = -(kernel.T * gram * kernel)
        if positive_kernel_gram.shape != (
            EXPECTED_SLICE_KERNEL_RANK,
            EXPECTED_SLICE_KERNEL_RANK,
        ):
            raise ValueError("slice-kernel Gram shape regression")
        if positive_kernel_gram != positive_kernel_gram.T:
            raise ValueError("slice-kernel Gram symmetry regression")
        L, Dldl = positive_kernel_gram.LDLdecomposition(hermitian=False)
        if L * Dldl * L.T != positive_kernel_gram:
            raise ValueError("slice-kernel LDL reconstruction regression")
        ldl_pivots = [Dldl[i, i] for i in range(Dldl.rows)]
        if any(v <= 0 for v in ldl_pivots):
            raise ValueError("slice-kernel positive-definiteness regression")

        kernel_gram_inv = positive_kernel_gram.inv()
        dual_norms: list[Fraction] = []
        for i in range(PICARD_RANK):
            row = kernel[i, :]
            value = (row * kernel_gram_inv * row.T)[0]
            dual_norm = as_fraction(value)
            if dual_norm < 0:
                raise ValueError(f"negative coordinate dual norm at retained coordinate {i}")
            dual_norms.append(dual_norm)

        model = cls(
            fixed_image_basis=tuple(
                tuple(int(fixed_basis[i, j]) for j in range(EXPECTED_FIXED_RANK))
                for i in range(PICARD_RANK)
            ),
            coordinate_dual_norms=tuple(dual_norms),
            certificate={},
        )

        sorted_reps = sorted(residues)
        penalties = [model.lower_bound_from_residue(rep) for rep in sorted_reps]
        zero_rep = (0,) * PICARD_RANK
        zero_count = sum(1 for value in penalties if value == 0)
        if zero_count != 1:
            raise ValueError(f"expected exactly one zero anti-fixed penalty class, got {zero_count}")
        if model.lower_bound_from_residue(zero_rep) != 0:
            raise ValueError("zero projection class penalty regression")
        positive_penalties = [value for value in penalties if value > 0]
        if len(positive_penalties) != EXPECTED_PROJECTION_CLASS_COUNT - 1:
            raise ValueError("positive anti-fixed penalty class count regression")

        # Every residue in im(N) mod 64 is the fractional coordinate vector of
        # p=P(x)=N*x/64 modulo the integral fixed lattice. For q=x-p, x is
        # integral, so q_i == -residue_i/64 (mod Z). Since phi(q)=0 and
        # -G is positive definite on ker(phi), exact Cauchy-Schwarz on each
        # coordinate functional gives
        #
        #   -q^2 >= dist(residue_i/64, Z)^2 / ||coord_i||_*^2.
        #
        # Taking the maximum over retained coordinates is therefore a safe
        # class-dependent lower bound on the information lost by Reynolds
        # averaging. No 59-dimensional closest-vector search is used.
        cert = {
            "schema": "STAGE32_21AA_ANTI_FIXED_COSET_PENALTY_V1",
            "mode": "EXACT_FINITE_REYNOLDS_PROJECTION_CLASS_TO_SAFE_ANTI_FIXED_NORM_PENALTY",
            "slice_stabilizer_group_order": GROUP_ORDER,
            "picard_rank": PICARD_RANK,
            "fixed_rank": EXPECTED_FIXED_RANK,
            "anti_fixed_rank": PICARD_RANK - EXPECTED_FIXED_RANK,
            "slice_rank": EXPECTED_SLICE_RANK,
            "slice_kernel_rank": EXPECTED_SLICE_KERNEL_RANK,
            "projection_class_count": len(sorted_reps),
            "projection_generator_relative_orders": relative_orders,
            "projection_subgroup_sizes": subgroup_sizes,
            "fixed_image_basis_sha256": csha(matrix_int_list(fixed_basis)),
            "fixed_image_column_module_stats": fixed_module_stats,
            "reynolds_numerator_sha256": csha(matrix_int_list(N)),
            "action_hashes_sha256": action_hashes_sha,
            "slice_smith_diagonal": list(slice_smith),
            "slice_kernel_basis_sha256": csha(matrix_int_list(kernel)),
            "slice_kernel_positive_gram_sha256": csha(matrix_int_list(positive_kernel_gram)),
            "slice_kernel_ldl_positive_exact": True,
            "slice_kernel_ldl_diagonal_sha256": csha([str(v) for v in ldl_pivots]),
            "coordinate_dual_norm_count": len(dual_norms),
            "coordinate_dual_norm_sha256": csha(
                [[v.numerator, v.denominator] for v in dual_norms]
            ),
            "zero_dual_norm_coordinate_count": sum(1 for v in dual_norms if v == 0),
            "zero_penalty_class_count": zero_count,
            "positive_penalty_class_count": len(positive_penalties),
            "distinct_penalty_count": len(set(penalties)),
            "minimum_positive_penalty": [
                min(positive_penalties).numerator,
                min(positive_penalties).denominator,
            ],
            "maximum_coordinate_cauchy_penalty": [
                max(positive_penalties).numerator,
                max(positive_penalties).denominator,
            ],
            "canonical_penalty_stream_sha256": penalty_stream_sha256(
                sorted_reps, penalties
            ),
            "canonical_penalty_stream_encoding": (
                "lexicographically sorted 64-byte projection residue, followed by "
                "ASCII numerator/denominator and newline"
            ),
            "proof": {
                "P_equals_N_over_64": True,
                "P_gram_self_adjoint_idempotent": True,
                "x_equals_p_plus_q_gram_orthogonal": True,
                "phi_q_equals_zero": True,
                "slice_kernel_negative_definite_exact": True,
                "projection_residue_is_fractional_part_of_p_in_retained_basis": True,
                "anti_fixed_fractional_coordinate_is_negative_projection_residue_over_64_mod_Z": True,
                "coordinate_dual_norms_computed_exactly_on_slice_kernel": True,
                "coordinate_cauchy_lower_bound_exact": True,
                "maximum_coordinate_lower_bound_safe": True,
                "all_projection_classes_enumerated_from_exact_imN_column_module": True,
                "anti_fixed_59d_closest_vector_search_run": False,
                "terminal_family_materialization_run": False,
            },
            "safe_semantics": {
                "penalty_is_lower_bound_on_minus_q_square": True,
                "therefore_x_square_le_p_square_minus_penalty": True,
                "positive_penalty_does_not_by_itself_prune_without_projected_slack_comparison": True,
                "numerical_row_complete": False,
                "theorem_credit": False,
                "receiver_credit": False,
                "route_credit": False,
                "perfect_cuboid_existence_claim": False,
                "perfect_cuboid_nonexistence_claim": False,
            },
            "next_leaf": (
                "32-21ab: derive the exact quotient-class map from the rank-2 "
                "Smith affine coordinates to the 16,384 Reynolds projection classes"
            ),
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            fixed_image_basis=model.fixed_image_basis,
            coordinate_dual_norms=model.coordinate_dual_norms,
            certificate=cert,
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21aa_picard")
    marking = load_retained(args.marking, "s32_21aa_marking")
    model = ReynoldsAntiFixedCosetPenalty.from_retained(marking, bundle)
    args.output.write_text(json.dumps(model.certificate, indent=2, sort_keys=True) + "\n")
    cert = model.certificate
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AA_ANTI_FIXED_COSET_PENALTY_REPRESENTATION",
        "projection_class_count": cert["projection_class_count"],
        "zero_penalty_class_count": cert["zero_penalty_class_count"],
        "positive_penalty_class_count": cert["positive_penalty_class_count"],
        "distinct_penalty_count": cert["distinct_penalty_count"],
        "minimum_positive_penalty": cert["minimum_positive_penalty"],
        "maximum_coordinate_cauchy_penalty": cert["maximum_coordinate_cauchy_penalty"],
        "canonical_penalty_stream_sha256": cert["canonical_penalty_stream_sha256"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
