#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

SELECTED_ROWS = list(range(92, 140)) + [0, 1, 2, 3, 4, 8, 9, 12, 16, 17, 24, 32, 44, 48, 52, 68]
EXPECTED_DET = 274877906944
EXPECTED_DEN = 8
EXPECTED_SNF = [1] * 40 + [2] * 14 + [4] * 6 + [8] * 4
EXPECTED_CORE_SHA = "de84f4511ea2ea747fd712e2f5f09c7f8d94ae3633e55678b81cfe63f6ed2870"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def csha(value: object) -> str:
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


def verify_core(core: dict) -> None:
    unsigned = dict(core)
    claimed = unsigned.pop("canonical_sha256_without_this_field")
    assert claimed == EXPECTED_CORE_SHA == csha(unsigned)
    assert core["source"]["git_blob_sha1"] == EXPECTED_SOURCE_BLOB
    assert int(core["rank"]) == 64 and int(core["known_class_count"]) == 140


@dataclass(frozen=True)
class PairingTransform:
    den: int
    selected: Matrix
    inverse_integer: Matrix
    transformed_pairings: Matrix
    transformed_gram: Matrix
    hform: Matrix
    certificate: dict

    @classmethod
    def from_core(cls, core: dict) -> "PairingTransform":
        verify_core(core)
        rows = Matrix(core["raw_cross_pairings_with_basis"])
        gram = Matrix(core["basis_gram"])
        selected = Matrix([core["raw_cross_pairings_with_basis"][i] for i in SELECTED_ROWS])
        det = int(selected.det())
        assert abs(det) == EXPECTED_DET
        inv = selected.inv()
        den = 1
        for value in inv:
            den = math.lcm(den, int(sympy.denom(value)))
        assert den == EXPECTED_DEN
        inv_int = inv * den
        assert all(sympy.denom(v) == 1 for v in inv_int)
        inv_int = Matrix([[int(inv_int[i, j]) for j in range(64)] for i in range(64)])
        assert selected * inv_int == den * Matrix.eye(64)
        pair = rows * inv_int
        assert all(sympy.denom(v) == 1 for v in pair)
        pair = Matrix([[int(pair[i, j]) for j in range(64)] for i in range(140)])
        h = Matrix(core["hyperplane"]).T * gram * inv_int
        h = Matrix([[int(h[0, j]) for j in range(64)]])
        tgram = inv_int.T * gram * inv_int
        tgram = Matrix([[int(tgram[i, j]) for j in range(64)] for i in range(64)])
        diagonal = smith_normal_form(selected, domain=sympy.ZZ)
        snf = sorted(abs(int(diagonal[i, i])) for i in range(64))
        assert snf == EXPECTED_SNF
        cert = {
            "selected_rows_0based": SELECTED_ROWS,
            "selected_matrix_determinant": det,
            "inverse_denominator": den,
            "snf_invariants": snf,
            "selected_matrix_sha256": csha(matrix_list(selected)),
            "inverse_integer_sha256": csha(matrix_list(inv_int)),
            "transformed_pairings_sha256": csha(matrix_list(pair)),
            "transformed_gram_sha256": csha(matrix_list(tgram)),
        }
        return cls(den, selected, inv_int, pair, tgram, h, cert)

    def full_membership(self, selected_pairings: Sequence[int]) -> bool:
        assert len(selected_pairings) == 64
        y = Matrix([int(v) for v in selected_pairings])
        return all(int(v) % self.den == 0 for v in self.inverse_integer * y)

    def reconstruct_picard_basis(self, selected_pairings: Sequence[int]) -> list[int]:
        y = Matrix([int(v) for v in selected_pairings])
        num = self.inverse_integer * y
        if any(int(v) % self.den for v in num):
            raise ValueError("selected pairing vector is outside the Picard image lattice")
        return [int(v) // self.den for v in num]

    def full_pairings(self, selected_pairings: Sequence[int]) -> list[int]:
        y = Matrix([int(v) for v in selected_pairings])
        num = self.transformed_pairings * y
        if any(int(v) % self.den for v in num):
            raise ValueError("nonintegral full pairing vector")
        return [int(v) // self.den for v in num]


@dataclass(frozen=True)
class MembershipCheck:
    depth: int
    assigned_indices: tuple[int, ...]
    modulus: int
    coefficients: tuple[tuple[int, ...], ...]
    quotient_index: int
    hnf_sha256: str

    def feasible(self, values: Sequence[int]) -> bool:
        assert len(values) == self.depth
        if self.modulus == 1:
            return True
        q = self.modulus
        for row in self.coefficients:
            if sum(a * int(v) for a, v in zip(row, values)) % q:
                return False
        return True


class PrefixMembershipOracle:
    """Exact extendability of partial selected-pairing assignments.

    For assigned selected coordinates A and unassigned U, a partial vector y_A
    extends to y=Sx with x integral iff -B_A y_A lies in the column lattice
    generated by B_U and 8I, where B=8*S^{-1}. HNF makes this an exact finite
    congruence test. No floating arithmetic participates.
    """

    def __init__(self, transform: PairingTransform, assignment_order: Sequence[int]):
        order = tuple(int(i) for i in assignment_order)
        if len(set(order)) != len(order) or any(i < 0 or i >= 64 for i in order):
            raise ValueError("assignment_order must contain distinct selected-coordinate indices")
        self.transform = transform
        self.order = order
        self.checks = [self._build_check(k) for k in range(1, len(order) + 1)]

    def _build_check(self, depth: int) -> MembershipCheck:
        assigned = self.order[:depth]
        assigned_set = set(assigned)
        unassigned = [j for j in range(64) if j not in assigned_set]
        B = self.transform.inverse_integer
        suffix = B[:, unassigned] if unassigned else Matrix.zeros(64, 0)
        lattice = suffix.row_join(self.transform.den * Matrix.eye(64))
        hnf = hermite_normal_form(lattice)
        assert hnf.shape == (64, 64) and hnf.det() != 0
        inv = hnf.inv()
        modulus = 1
        for value in inv:
            modulus = math.lcm(modulus, int(sympy.denom(value)))
        inv_int = inv * modulus
        assert all(sympy.denom(v) == 1 for v in inv_int)
        inv_int = Matrix([[int(inv_int[i, j]) for j in range(64)] for i in range(64)])
        coeff = inv_int * B[:, list(assigned)]
        coeff_rows = tuple(
            tuple(int(coeff[i, j]) % modulus for j in range(depth))
            for i in range(64)
            if modulus != 1 and any(int(coeff[i, j]) % modulus for j in range(depth))
        )
        qindex = abs(int(hnf.det()))
        return MembershipCheck(
            depth=depth,
            assigned_indices=assigned,
            modulus=modulus,
            coefficients=coeff_rows,
            quotient_index=qindex,
            hnf_sha256=csha(matrix_list(hnf)),
        )

    def feasible(self, values: Sequence[int]) -> bool:
        if not values:
            return True
        return self.checks[len(values) - 1].feasible(values)

    def certificate(self) -> dict:
        return {
            "assignment_order": list(self.order),
            "checks": [
                {
                    "depth": c.depth,
                    "assigned_indices": list(c.assigned_indices),
                    "modulus": c.modulus,
                    "active_congruence_rows": len(c.coefficients),
                    "quotient_index": c.quotient_index,
                    "hnf_sha256": c.hnf_sha256,
                }
                for c in self.checks
            ],
        }


def compose_perm(p: tuple[int, ...], q: tuple[int, ...]) -> tuple[int, ...]:
    return tuple(p[q[i]] for i in range(len(p)))


def close_permutation_group(permutations_1based: Iterable[Sequence[int]]) -> list[tuple[int, ...]]:
    gens = [tuple(int(v) - 1 for v in p) for p in permutations_1based]
    n = len(gens[0])
    assert all(len(g) == n and sorted(g) == list(range(n)) for g in gens)
    identity = tuple(range(n))
    seen = {identity}
    queue = [identity]
    while queue:
        cur = queue.pop()
        for gen in gens:
            nxt = compose_perm(gen, cur)
            if nxt not in seen:
                seen.add(nxt)
                queue.append(nxt)
    return sorted(seen)


def permute_pairings(pairings: Sequence[int], permutation: Sequence[int]) -> tuple[int, ...]:
    n = len(permutation)
    inv = [0] * n
    for i, j in enumerate(permutation):
        inv[int(j)] = i
    return tuple(int(pairings[inv[j]]) for j in range(n))


def canonical_pairing_key(pairings: Sequence[int], group: Iterable[Sequence[int]]) -> tuple[int, ...]:
    base = tuple(int(v) for v in pairings)
    return min(permute_pairings(base, g) for g in group)
