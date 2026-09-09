#!/usr/bin/env python3
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE / "stage32ex5-a-node-target.json"

# Exact Q(i) arithmetic as pairs (real, imag) of Fractions.
def q(a=0, b=0):
    return (Fraction(a), Fraction(b))

ZERO = q()
ONE = q(1)
I = q(0, 1)

def add(x, y):
    return (x[0] + y[0], x[1] + y[1])

def neg(x):
    return (-x[0], -x[1])

def sub(x, y):
    return add(x, neg(y))

def mul(x, y):
    return (x[0] * y[0] - x[1] * y[1],
            x[0] * y[1] + x[1] * y[0])

def inv(x):
    if x == ZERO:
        raise ZeroDivisionError
    d = x[0] * x[0] + x[1] * x[1]
    return (x[0] / d, -x[1] / d)

def div(x, y):
    return mul(x, inv(y))

def parse(s):
    table = {
        "0": ZERO,
        "1": ONE,
        "-1": neg(ONE),
        "i": I,
        "-i": neg(I),
    }
    return table[s]

def rank(mat):
    a = [[v for v in row] for row in mat]
    if not a:
        return 0
    m, n = len(a), len(a[0])
    r = 0
    for c in range(n):
        pivot = next((i for i in range(r, m) if a[i][c] != ZERO), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        p = a[r][c]
        a[r] = [div(v, p) for v in a[r]]
        for i in range(m):
            if i == r or a[i][c] == ZERO:
                continue
            f = a[i][c]
            a[i] = [sub(a[i][j], mul(f, a[r][j])) for j in range(n)]
        r += 1
        if r == m:
            break
    return r

def surface_residuals(p):
    x1, x2, x3, y1, y2, y3, z = p
    sq = lambda x: mul(x, x)
    return [
        sub(sq(y1), add(sq(x2), sq(x3))),
        sub(sq(y2), add(sq(x3), sq(x1))),
        sub(sq(y3), add(sq(x1), sq(x2))),
        sub(sq(z), add(add(sq(x1), sq(x2)), sq(x3))),
    ]

def jacobian(p):
    x1, x2, x3, y1, y2, y3, z = p
    two = q(2)
    mtwo = q(-2)
    return [
        [ZERO, mul(mtwo, x2), mul(mtwo, x3), mul(two, y1), ZERO, ZERO, ZERO],
        [mul(mtwo, x1), ZERO, mul(mtwo, x3), ZERO, mul(two, y2), ZERO, ZERO],
        [mul(mtwo, x1), mul(mtwo, x2), ZERO, ZERO, ZERO, mul(two, y3), ZERO],
        [mul(mtwo, x1), mul(mtwo, x2), mul(mtwo, x3), ZERO, ZERO, ZERO, mul(two, z)],
    ]

def canonical_tuple(p):
    # Normalize first nonzero x-coordinate in order x1,x2,x3 to 1.
    for idx in range(3):
        if p[idx] != ZERO:
            s = inv(p[idx])
            return tuple(mul(s, v) for v in p)
    raise AssertionError("node has no nonzero x-coordinate")

def main():
    data = json.loads(TARGET.read_text(encoding="utf-8"))
    assert data["schema"] == "STAGE32EX5_A_BTVA_SOURCE_NODE_TARGET_V1"
    assert data["coordinate_order"] == ["x1", "x2", "x3", "y1", "y2", "y3", "z"]
    assert data["field"] == "Q(i)"
    assert data["count"] == 48
    assert sum(f["count"] for f in data["families"]) == 48

    labels = []
    canonical = []
    family_counts = {}
    for row in data["nodes"]:
        labels.append(row["label"])
        family_counts[row["family"]] = family_counts.get(row["family"], 0) + 1
        p = tuple(parse(v) for v in row["coords"])
        assert len(p) == 7
        assert all(v == ZERO for v in surface_residuals(p)), row["label"]
        # X_pc is a codimension-4 complete intersection in this presentation.
        # Rank 3 therefore certifies each listed point is singular.
        assert rank(jacobian(p)) == 3, row["label"]
        cp = canonical_tuple(p)
        assert cp == p, row["label"]
        canonical.append(cp)

    assert len(labels) == 48
    assert len(set(labels)) == 48
    assert len(set(canonical)) == 48
    expected = {f["id"]: f["count"] for f in data["families"]}
    assert family_counts == expected

    print("PASS stage32ex5-a source-node target")
    print("count=48 distinct_projective=48 jacobian_rank=3_all=true")
    print("families=" + ",".join(f"{k}:{family_counts[k]}" for k in sorted(family_counts)))

if __name__ == "__main__":
    main()
