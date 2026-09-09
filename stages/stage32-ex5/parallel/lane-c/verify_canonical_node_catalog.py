#!/usr/bin/env python3
from __future__ import annotations

import argparse
import hashlib
import json
from collections import Counter
from fractions import Fraction
from pathlib import Path

EXPECTED_SCHEMA = "STAGE32EX5_BC2_01B_CANONICAL_SINGULAR_NODE_CATALOG_V1"
EXPECTED_COUNT = 48
EXPECTED_FAMILIES = {"A1": 8, "A2": 8, "A3": 8, "C0B1": 8, "C0B2": 8, "C0B3": 8}


class GI:
    """Exact element of Q(i), represented as re + im*i."""

    __slots__ = ("re", "im")

    def __init__(self, re=0, im=0):
        self.re = Fraction(re)
        self.im = Fraction(im)

    def __add__(self, other):
        other = as_gi(other)
        return GI(self.re + other.re, self.im + other.im)

    def __sub__(self, other):
        other = as_gi(other)
        return GI(self.re - other.re, self.im - other.im)

    def __neg__(self):
        return GI(-self.re, -self.im)

    def __mul__(self, other):
        other = as_gi(other)
        return GI(
            self.re * other.re - self.im * other.im,
            self.re * other.im + self.im * other.re,
        )

    def __truediv__(self, other):
        other = as_gi(other)
        den = other.re * other.re + other.im * other.im
        if den == 0:
            raise ZeroDivisionError
        return GI(
            (self.re * other.re + self.im * other.im) / den,
            (self.im * other.re - self.re * other.im) / den,
        )

    def __eq__(self, other):
        other = as_gi(other)
        return self.re == other.re and self.im == other.im

    def __bool__(self):
        return self.re != 0 or self.im != 0

    def key(self):
        return (
            self.re.numerator,
            self.re.denominator,
            self.im.numerator,
            self.im.denominator,
        )


def as_gi(value):
    return value if isinstance(value, GI) else GI(value)


def parse_atom(token: str) -> GI:
    table = {
        "0": GI(0),
        "1": GI(1),
        "-1": GI(-1),
        "i": GI(0, 1),
        "-i": GI(0, -1),
    }
    if token not in table:
        raise ValueError(f"unsupported coordinate token: {token!r}")
    return table[token]


def canonical_projective_key(coords):
    pivot = next((x for x in coords[:3] if x), None)
    if pivot is None:
        raise ValueError("no nonzero a-coordinate")
    normalized = [x / pivot for x in coords]
    first = next(i for i, x in enumerate(normalized[:3]) if x)
    if normalized[first] != GI(1):
        raise ValueError("projective normalization regression")
    return tuple(x.key() for x in normalized)


def rank_exact(matrix):
    a = [[as_gi(x) for x in row] for row in matrix]
    rows = len(a)
    cols = len(a[0]) if rows else 0
    r = 0
    for c in range(cols):
        pivot = next((q for q in range(r, rows) if a[q][c]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        pv = a[r][c]
        a[r] = [x / pv for x in a[r]]
        for q in range(rows):
            if q == r or not a[q][c]:
                continue
            factor = a[q][c]
            a[q] = [a[q][j] - factor * a[r][j] for j in range(cols)]
        r += 1
        if r == rows:
            break
    return r


def csha(value):
    return hashlib.sha256(
        json.dumps(value, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()


def verify_node(node):
    a1, a2, a3, b1, b2, b3, c = [parse_atom(x) for x in node["coordinates"]]
    equations = [
        a1 * a1 + a2 * a2 - b3 * b3,
        a2 * a2 + a3 * a3 - b1 * b1,
        a1 * a1 + a3 * a3 - b2 * b2,
        a1 * a1 + a2 * a2 + a3 * a3 - c * c,
    ]
    if any(equations):
        raise ValueError(f"{node['canonical_id']}: surface equation regression")

    two = GI(2)
    jac = [
        [two*a1, two*a2, GI(0), GI(0), GI(0), -two*b3, GI(0)],
        [GI(0), two*a2, two*a3, -two*b1, GI(0), GI(0), GI(0)],
        [two*a1, GI(0), two*a3, GI(0), -two*b2, GI(0), GI(0)],
        [two*a1, two*a2, two*a3, GI(0), GI(0), GI(0), -two*c],
    ]
    rank = rank_exact(jac)
    if rank != 3:
        raise ValueError(f"{node['canonical_id']}: Jacobian rank {rank}, expected 3")
    return canonical_projective_key([a1, a2, a3, b1, b2, b3, c])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "catalog",
        nargs="?",
        type=Path,
        default=Path(__file__).with_name("canonical-node-catalog.json"),
    )
    args = ap.parse_args()

    raw = json.loads(args.catalog.read_text())
    claimed = raw.pop("canonical_sha256_without_this_field")
    if raw.get("schema") != EXPECTED_SCHEMA:
        raise ValueError("schema regression")
    if csha(raw) != claimed:
        raise ValueError("canonical catalog SHA regression")
    nodes = raw["nodes"]
    if len(nodes) != EXPECTED_COUNT or raw.get("node_count") != EXPECTED_COUNT:
        raise ValueError("node count regression")
    if Counter(n["family"] for n in nodes) != Counter(EXPECTED_FAMILIES):
        raise ValueError("family count regression")
    expected_ids = [f"N{k:02d}" for k in range(EXPECTED_COUNT)]
    if [n["canonical_id"] for n in nodes] != expected_ids:
        raise ValueError("canonical id ordering regression")

    keys = [verify_node(node) for node in nodes]
    collision_count = len(keys) - len(set(keys))
    if collision_count:
        raise ValueError(f"projective collision count: {collision_count}")

    print(json.dumps({
        "status": "PASS_CANONICAL_48_NODE_CATALOG",
        "node_count": len(nodes),
        "projective_collision_count": collision_count,
        "all_surface_equations_exact": True,
        "all_jacobian_ranks_equal_3": True,
        "canonical_sha256_without_this_field": claimed,
        "historical_runtime_index_binding_proved": False,
    }, sort_keys=True))


if __name__ == "__main__":
    main()
