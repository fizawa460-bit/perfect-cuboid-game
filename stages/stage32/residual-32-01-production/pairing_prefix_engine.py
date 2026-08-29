#!/usr/bin/env python3
from __future__ import annotations

import hashlib
import json
import math
from dataclasses import dataclass
from typing import Iterable, Sequence

import sympy
from sympy import Matrix
from sympy.matrices.normalforms import hermite_normal_form

INDLIST = [
    1,2,3,4,5,6,7,9,10,11,12,13,14,15,17,18,19,20,21,22,23,25,26,27,29,
    33,34,35,37,38,41,45,49,53,69,
    93,94,95,96,97,98,99,101,102,103,104,105,106,107,109,110,111,113,
    117,118,119,120,121,125,126,127,129,133,135,
]
assert len(INDLIST) == 64 and len(set(INDLIST)) == 64
EXCEPTIONAL_BASIS_POSITIONS = [i for i, j in enumerate(INDLIST) if j > 92]
CURVE_BASIS_POSITIONS = [i for i, j in enumerate(INDLIST) if j <= 92]
assert len(EXCEPTIONAL_BASIS_POSITIONS) == 29
assert len(CURVE_BASIS_POSITIONS) == 35
RETAINED_BUNDLE_SHA256 = "d1deeb3b0cb65fd52563355cd5497a2319ddd7bc9fe4aaeaca91449f155c998c"
EXPECTED_SOURCE_BLOB = "0422b69847f2afb97cb7b3ed02ebef91279f61b1"


def csha(value: object) -> str:
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def matrix_list(m: Matrix) -> list[list[int]]:
    return [[int(m[i, j]) for j in range(m.cols)] for i in range(m.rows)]


@dataclass(frozen=True)
class RetainedBasisPairingTransform:
    """Exact pairing-image coordinates from the retained primitive Picard basis.

    Rows are only permuted: the 29 exceptional basis classes come first,
    followed by the 35 curve basis classes. Hence selected=P*Gram is
    nonsingular and y=selected*x is an exact full-rank pairing coordinate
    system for Pic(S). No online Magma computation is needed.
    """
    den: int
    selected: Matrix
    inverse_integer: Matrix
    certificate: dict

    @classmethod
    def from_bundle(cls, bundle: dict) -> "RetainedBasisPairingTransform":
        assert bundle["canonical_sha256"] == RETAINED_BUNDLE_SHA256
        assert bundle["upstream_git_blob_sha1"] == EXPECTED_SOURCE_BLOB
        gram = Matrix(bundle["picard_gram_64x64"])
        assert gram.shape == (64, 64)
        assert gram == gram.T
        order = EXCEPTIONAL_BASIS_POSITIONS + CURVE_BASIS_POSITIONS
        selected = Matrix([[int(gram[i, j]) for j in range(64)] for i in order])
        det = int(selected.det())
        assert det != 0

        inv = selected.inv()
        den = 1
        for value in inv:
            den = math.lcm(den, int(sympy.denom(value)))
        inv_int = inv * den
        assert all(sympy.denom(v) == 1 for v in inv_int)
        inv_int = Matrix(
            [[int(inv_int[i, j]) for j in range(64)] for i in range(64)]
        )
        assert selected * inv_int == den * Matrix.eye(64)

        cert = {
            "coordinate_model": "RETAINED_PRIMITIVE_BASIS_PAIRINGS_EXCEPTIONALS_FIRST",
            "retained_bundle_sha256": RETAINED_BUNDLE_SHA256,
            "upstream_git_blob_sha1": EXPECTED_SOURCE_BLOB,
            "basis_known_indices_1based": INDLIST,
            "selected_basis_positions_0based": order,
            "selected_known_indices_1based": [INDLIST[i] for i in order],
            "exceptional_basis_coordinate_count": len(EXCEPTIONAL_BASIS_POSITIONS),
            "curve_basis_coordinate_count": len(CURVE_BASIS_POSITIONS),
            "selected_matrix_determinant": det,
            "inverse_denominator": den,
            "selected_matrix_sha256": csha(matrix_list(selected)),
            "inverse_integer_sha256": csha(matrix_list(inv_int)),
        }
        return cls(den, selected, inv_int, cert)

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
    """Exact extendability of partial pairing assignments.

    For assigned coordinates A and unassigned U, a partial vector y_A extends
    to y=Sx with x integral iff -B_A y_A lies in the column lattice generated
    by B_U and den*I, where B=den*S^{-1}. HNF gives an exact congruence test.
    """
    def __init__(self, transform: RetainedBasisPairingTransform, assignment_order: Sequence[int]):
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
        inv_int = Matrix(
            [[int(inv_int[i, j]) for j in range(64)] for i in range(64)]
        )
        coeff = inv_int * B[:, list(assigned)]
        coeff_rows = tuple(
            tuple(int(coeff[i, j]) % modulus for j in range(depth))
            for i in range(64)
            if modulus != 1
            and any(int(coeff[i, j]) % modulus for j in range(depth))
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
