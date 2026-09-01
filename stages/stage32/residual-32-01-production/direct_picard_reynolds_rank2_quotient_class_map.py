#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from pathlib import Path

from sympy import Matrix

from direct_picard_reynolds_antifixed_coset_penalty import (
    ReynoldsAntiFixedCosetPenalty,
    add_mod,
    extend_subgroup,
)
from direct_picard_reynolds_lattice_diagnostic import (
    GROUP_ORDER,
    PICARD_RANK,
    csha,
    load_retained,
)
from direct_picard_reynolds_rank2_integer_qp import ReynoldsRank2IntegerQP

EXPECTED_FIXED_RANK = 5
EXPECTED_PROJECTION_CLASS_COUNT = 16384


def matrix_int_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def residue_stream_sha256(reps: tuple[tuple[int, ...], ...]) -> str:
    h = hashlib.sha256()
    for rep in reps:
        if len(rep) != PICARD_RANK or any(not 0 <= v < GROUP_ORDER for v in rep):
            raise ValueError("noncanonical projection residue in stream")
        h.update(bytes(rep))
    return h.hexdigest()


def enumerate_generated_residues(
    generators: tuple[tuple[int, ...], ...],
) -> tuple[set[tuple[int, ...]], tuple[int, ...], tuple[int, ...]]:
    subgroup: set[tuple[int, ...]] = {(0,) * PICARD_RANK}
    relative_orders: list[int] = []
    sizes = [1]
    for generator in generators:
        subgroup, order = extend_subgroup(subgroup, generator)
        relative_orders.append(order)
        sizes.append(len(subgroup))
    return subgroup, tuple(relative_orders), tuple(sizes)


@dataclass(frozen=True)
class ReynoldsRank2QuotientClassMap:
    rank2: ReynoldsRank2IntegerQP
    penalty: ReynoldsAntiFixedCosetPenalty
    map_columns: tuple[tuple[int, ...], ...]
    sorted_projection_residues: tuple[tuple[int, ...], ...]
    residue_to_class_id: dict[tuple[int, ...], int]
    free_subgroup: frozenset[tuple[int, ...]]
    residue_to_coset_id: dict[tuple[int, ...], int]
    coset_representatives: tuple[tuple[int, ...], ...]
    certificate: dict

    def smith_y(
        self, d: int, e: int, a: int, u: int = 0, v: int = 0
    ) -> tuple[int, int, int, int, int] | None:
        target = (int(d), int(e), int(a))
        transformed = tuple(
            sum(self.rank2.smith_left[i][j] * target[j] for j in range(3))
            for i in range(3)
        )
        locked: list[int] = []
        for value, diag in zip(transformed, self.rank2.smith_diagonal_signed):
            if value % diag:
                return None
            locked.append(value // diag)
        return locked[0], locked[1], locked[2], int(u), int(v)

    def residue_from_y(self, y: tuple[int, ...]) -> tuple[int, ...]:
        if len(y) != EXPECTED_FIXED_RANK:
            raise ValueError("rank2 Smith quotient map expects five y coordinates")
        return tuple(
            sum(self.map_columns[j][i] * int(y[j]) for j in range(EXPECTED_FIXED_RANK))
            % GROUP_ORDER
            for i in range(PICARD_RANK)
        )

    def residue(
        self, d: int, e: int, a: int, u: int = 0, v: int = 0
    ) -> tuple[int, ...] | None:
        y = self.smith_y(d, e, a, u, v)
        if y is None:
            return None
        return self.residue_from_y(y)

    def class_id(
        self, d: int, e: int, a: int, u: int = 0, v: int = 0
    ) -> int | None:
        residue = self.residue(d, e, a, u, v)
        if residue is None:
            return None
        return self.residue_to_class_id[residue]

    def coset_id(self, d: int, e: int, a: int) -> int | None:
        residue = self.residue(d, e, a, 0, 0)
        if residue is None:
            return None
        return self.residue_to_coset_id[residue]

    @classmethod
    def from_retained(
        cls, marking: dict, bundle: dict
    ) -> "ReynoldsRank2QuotientClassMap":
        rank2 = ReynoldsRank2IntegerQP.from_retained(marking, bundle)
        penalty = ReynoldsAntiFixedCosetPenalty.from_retained(marking, bundle)

        fixed_basis_sha = penalty.certificate["fixed_image_basis_sha256"]
        if rank2.certificate["fixed_image_basis_sha256"] != fixed_basis_sha:
            raise ValueError("rank2 and 32-21aa fixed-image basis hash mismatch")

        B = Matrix(penalty.fixed_image_basis)
        T = Matrix(rank2.smith_right)
        if B.shape != (PICARD_RANK, EXPECTED_FIXED_RANK):
            raise ValueError(f"fixed basis shape regression: {B.shape}")
        if T.shape != (EXPECTED_FIXED_RANK, EXPECTED_FIXED_RANK):
            raise ValueError(f"Smith-right shape regression: {T.shape}")
        if abs(int(T.det())) != 1:
            raise ValueError("rank2 Smith-right transform is not unimodular")

        map_matrix = (B * T).applyfunc(lambda z: int(z) % GROUP_ORDER)
        map_columns = tuple(
            tuple(int(map_matrix[i, j]) for i in range(PICARD_RANK))
            for j in range(EXPECTED_FIXED_RANK)
        )
        basis_generators = tuple(
            tuple(int(B[i, j]) % GROUP_ORDER for i in range(PICARD_RANK))
            for j in range(EXPECTED_FIXED_RANK)
        )

        basis_image, basis_orders, basis_sizes = enumerate_generated_residues(
            basis_generators
        )
        mapped_image, mapped_orders, mapped_sizes = enumerate_generated_residues(
            map_columns
        )
        if basis_image != mapped_image:
            raise ValueError("unimodular Smith coordinate change altered projection image")
        if len(mapped_image) != EXPECTED_PROJECTION_CLASS_COUNT:
            raise ValueError(
                f"projection image count regression: {len(mapped_image)}"
            )

        sorted_reps = tuple(sorted(mapped_image))
        residue_to_class_id = {rep: i for i, rep in enumerate(sorted_reps)}

        free_generators = (map_columns[3], map_columns[4])
        free_subgroup_set, free_orders, free_sizes = enumerate_generated_residues(
            free_generators
        )
        free_subgroup = frozenset(free_subgroup_set)
        if not free_subgroup or len(mapped_image) % len(free_subgroup):
            raise ValueError("rank2 free subgroup does not divide projection image")

        unassigned = set(mapped_image)
        residue_to_canonical_coset: dict[tuple[int, ...], tuple[int, ...]] = {}
        canonical_cosets: list[tuple[int, ...]] = []
        while unassigned:
            seed = min(unassigned)
            coset = {add_mod(seed, h) for h in free_subgroup}
            if len(coset) != len(free_subgroup) or not coset <= mapped_image:
                raise ValueError("rank2 free coset size/image regression")
            canonical = min(coset)
            canonical_cosets.append(canonical)
            for rep in coset:
                residue_to_canonical_coset[rep] = canonical
            unassigned.difference_update(coset)

        coset_representatives = tuple(sorted(set(canonical_cosets)))
        expected_cosets = EXPECTED_PROJECTION_CLASS_COUNT // len(free_subgroup)
        if len(coset_representatives) != expected_cosets:
            raise ValueError(
                f"rank2 free quotient coset count regression: {len(coset_representatives)} != {expected_cosets}"
            )
        canonical_to_coset_id = {
            rep: i for i, rep in enumerate(coset_representatives)
        }
        residue_to_coset_id = {
            rep: canonical_to_coset_id[canonical]
            for rep, canonical in residue_to_canonical_coset.items()
        }
        if len(residue_to_coset_id) != EXPECTED_PROJECTION_CLASS_COUNT:
            raise ValueError("not every projection residue received a rank2 free coset id")

        # Exact compatibility check with the original z-coordinate convention.
        # y -> z=T*y and residue=B*z mod 64, hence residue=(B*T)*y mod 64.
        # Checking the five standard y generators is sufficient by linearity;
        # full finite-image equality above additionally checks the quotient image.
        for j in range(EXPECTED_FIXED_RANK):
            y = tuple(1 if i == j else 0 for i in range(EXPECTED_FIXED_RANK))
            z = tuple(int(T[i, j]) for i in range(EXPECTED_FIXED_RANK))
            via_map = tuple(
                sum(map_columns[k][i] * y[k] for k in range(EXPECTED_FIXED_RANK))
                % GROUP_ORDER
                for i in range(PICARD_RANK)
            )
            via_aa = penalty.projection_residue_from_z(z)
            if via_map != via_aa:
                raise ValueError(f"Smith quotient map generator regression at column {j}")

        cert = {
            "schema": "STAGE32_21AB_EXACT_QUOTIENT_CLASS_MAP_V1",
            "mode": "EXACT_RANK2_SMITH_AFFINE_COORDINATES_TO_32_21AA_REYNOLDS_PROJECTION_RESIDUE",
            "group_order": GROUP_ORDER,
            "picard_rank": PICARD_RANK,
            "fixed_rank": EXPECTED_FIXED_RANK,
            "projection_class_count": len(sorted_reps),
            "rank2_model_sha256": rank2.certificate[
                "canonical_sha256_without_this_field"
            ],
            "anti_fixed_penalty_model_sha256": penalty.certificate[
                "canonical_sha256_without_this_field"
            ],
            "fixed_image_basis_sha256": fixed_basis_sha,
            "smith_right_sha256": csha(matrix_int_list(T)),
            "quotient_map_formula": "for y=(y0,y1,y2,u,v), residue=(B*T*y) mod 64",
            "quotient_map_matrix_sha256": csha(matrix_int_list(map_matrix)),
            "basis_generator_relative_orders": list(basis_orders),
            "basis_generator_subgroup_sizes": list(basis_sizes),
            "smith_generator_relative_orders": list(mapped_orders),
            "smith_generator_subgroup_sizes": list(mapped_sizes),
            "canonical_projection_residue_stream_sha256": residue_stream_sha256(
                sorted_reps
            ),
            "class_id_convention": "lexicographic index of canonical 64-byte residue in the complete 16384-element image",
            "rank2_free_generator_relative_orders": list(free_orders),
            "rank2_free_generator_subgroup_sizes": list(free_sizes),
            "rank2_free_subgroup_order": len(free_subgroup),
            "rank2_free_quotient_coset_count": len(coset_representatives),
            "rank2_free_subgroup_stream_sha256": residue_stream_sha256(
                tuple(sorted(free_subgroup))
            ),
            "rank2_free_coset_representative_stream_sha256": residue_stream_sha256(
                coset_representatives
            ),
            "proof": {
                "rank2_and_32_21aa_use_identical_fixed_image_basis": True,
                "smith_right_transform_unimodular": True,
                "B_times_T_map_exact": True,
                "smith_coordinate_image_equals_32_21aa_projection_image": True,
                "all_16384_projection_classes_covered": True,
                "rank2_free_uv_directions_generate_exact_subgroup": True,
                "rank2_affine_slice_maps_to_one_exact_free_subgroup_coset": True,
                "five_generator_compatibility_checked_against_32_21aa_residue_method": True,
                "terminal_family_materialization_run": False,
            },
            "safe_semantics": {
                "map_is_representation_only": True,
                "map_does_not_by_itself_prune": True,
                "numerical_row_complete": False,
                "theorem_credit": False,
                "receiver_credit": False,
                "route_credit": False,
                "perfect_cuboid_existence_claim": False,
                "perfect_cuboid_nonexistence_claim": False,
            },
            "next_leaf": "32-21ac: take the exact minimum 32-21aa penalty on each rank2 free-subgroup coset and use it as a safe cheap pruning threshold",
        }
        cert["canonical_sha256_without_this_field"] = csha(cert)
        return cls(
            rank2=rank2,
            penalty=penalty,
            map_columns=map_columns,
            sorted_projection_residues=sorted_reps,
            residue_to_class_id=residue_to_class_id,
            free_subgroup=free_subgroup,
            residue_to_coset_id=residue_to_coset_id,
            coset_representatives=coset_representatives,
            certificate=cert,
        )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--retained", type=Path, required=True)
    ap.add_argument("--marking", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    bundle = load_retained(args.retained, "s32_21ab_picard")
    marking = load_retained(args.marking, "s32_21ab_marking")
    model = ReynoldsRank2QuotientClassMap.from_retained(marking, bundle)
    args.output.write_text(json.dumps(model.certificate, indent=2, sort_keys=True) + "\n")
    cert = model.certificate
    print(json.dumps({
        "verdict": "PASS_STAGE32_21AB_EXACT_QUOTIENT_CLASS_MAP",
        "projection_class_count": cert["projection_class_count"],
        "free_subgroup_order": cert["rank2_free_subgroup_order"],
        "free_quotient_coset_count": cert["rank2_free_quotient_coset_count"],
        "canonical_sha256": cert["canonical_sha256_without_this_field"],
    }, sort_keys=True))


if __name__ == "__main__":
    main()
