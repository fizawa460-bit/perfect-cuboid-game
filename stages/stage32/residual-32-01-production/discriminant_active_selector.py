#!/usr/bin/env python3
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Sequence

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

from pairing_prefix_engine import RetainedBasisPairingTransform, csha, matrix_list


@dataclass(frozen=True)
class CandidateScore:
    candidate: int
    depth: int
    modulus: int
    active_congruence_rows: int
    quotient_index: int
    hnf_sha256: str

    @property
    def score(self) -> tuple[int, int, int, int, int]:
        # Prefer an actually active quotient character first.  Then prefer more
        # explicit congruence rows, larger exact quotient index, larger modulus,
        # and finally the lower coordinate index for deterministic tie breaking.
        return (
            int(self.active_congruence_rows > 0),
            self.active_congruence_rows,
            self.quotient_index,
            self.modulus,
            -self.candidate,
        )


def build_check_for_assigned(
    transform: RetainedBasisPairingTransform,
    assigned_indices: Sequence[int],
) -> CandidateScore:
    assigned = tuple(int(i) for i in assigned_indices)
    if len(set(assigned)) != len(assigned):
        raise ValueError("assigned_indices must be distinct")
    if any(i < 0 or i >= 64 for i in assigned):
        raise ValueError("assigned index outside 0..63")

    assigned_set = set(assigned)
    unassigned = [j for j in range(64) if j not in assigned_set]
    B = transform.inverse_integer
    suffix = B[:, unassigned] if unassigned else Matrix.zeros(64, 0)
    lattice = suffix.row_join(transform.den * Matrix.eye(64))
    hnf = hermite_normal_form(lattice)
    assert hnf.shape == (64, 64) and hnf.det() != 0

    inv = hnf.inv()
    modulus = 1
    for value in inv:
        modulus = math.lcm(modulus, int(sympy.denom(value)))
    inv_int = inv * modulus
    assert all(sympy.denom(v) == 1 for v in inv_int)
    inv_int = Matrix(
        [[int(inv_int[i, j]) for j in range(64)] for i in range(64)]
    )
    coeff = inv_int * B[:, list(assigned)]
    active_rows = sum(
        1
        for i in range(64)
        if modulus != 1
        and any(int(coeff[i, j]) % modulus for j in range(len(assigned)))
    )
    return CandidateScore(
        candidate=assigned[-1],
        depth=len(assigned),
        modulus=modulus,
        active_congruence_rows=active_rows,
        quotient_index=abs(int(hnf.det())),
        hnf_sha256=csha(matrix_list(hnf)),
    )


def select_discriminant_active_order(
    transform: RetainedBasisPairingTransform,
    depth_limit: int = 11,
) -> tuple[list[int], list[dict]]:
    """Greedily choose raw pairing coordinates that expose Picard congruences.

    This is deliberately *not* an arbitrary reshuffle.  At each depth every
    remaining raw coordinate is tested with the exact HNF extension lattice.
    The selected coordinate maximizes whether a nonzero quotient character is
    already visible, then the number of active exact congruence rows and the
    quotient index.  Because only raw pairing coordinates are selected, the
    calibration branch-value semantics remain unchanged; linear quotient
    characters are used only to score/select the raw coordinates.
    """
    if depth_limit < 1 or depth_limit > 64:
        raise ValueError("depth_limit must be in 1..64")

    chosen: list[int] = []
    trace: list[dict] = []
    remaining = set(range(64))
    for depth in range(1, depth_limit + 1):
        scores = [
            build_check_for_assigned(transform, chosen + [candidate])
            for candidate in sorted(remaining)
        ]
        best = max(scores, key=lambda s: s.score)
        chosen.append(best.candidate)
        remaining.remove(best.candidate)
        active_candidates = sum(s.active_congruence_rows > 0 for s in scores)
        trace.append(
            {
                "depth": depth,
                "selected_coordinate": best.candidate,
                "selected_modulus": best.modulus,
                "selected_active_congruence_rows": best.active_congruence_rows,
                "selected_quotient_index": best.quotient_index,
                "selected_hnf_sha256": best.hnf_sha256,
                "candidate_count": len(scores),
                "active_candidate_count": active_candidates,
                "selection_rule": "ACTIVE_ROWS_THEN_COUNT_THEN_QUOTIENT_INDEX_THEN_MODULUS_THEN_LOW_INDEX",
            }
        )
    return chosen, trace
