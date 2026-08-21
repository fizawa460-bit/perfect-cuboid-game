#!/usr/bin/env python3
"""Exact standard-library audit for the Stage28-60-r3 Saunderson M-degree-6 adapter.

The script verifies polynomial identities only. The geometric identification
M_face = (phi o pi_face)^* O_{P^2}(1) is documented separately in split B.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction
from pathlib import Path


def clean(p):
    return {k: v for k, v in p.items() if v}


def add(a, b):
    out = dict(a)
    for k, v in b.items():
        out[k] = out.get(k, 0) + v
    return clean(out)


def neg(a):
    return {k: -v for k, v in a.items()}


def sub(a, b):
    return add(a, neg(b))


def scale(c, a):
    return clean({k: c * v for k, v in a.items()})


def mul(a, b):
    out = {}
    for (i, j), x in a.items():
        for (k, l), y in b.items():
            key = (i + k, j + l)
            out[key] = out.get(key, 0) + x * y
    return clean(out)


def power(a, n):
    out = {(0, 0): 1}
    for _ in range(n):
        out = mul(out, a)
    return out


def homogeneous_degrees(a):
    return sorted({i + j for (i, j), c in a.items() if c})


def to_affine_t(a):
    """Set r=1 and return coefficients in t=s/r, low degree first."""
    if not a:
        return [Fraction(0)]
    deg = max(j for (_, j) in a)
    out = [Fraction(0) for _ in range(deg + 1)]
    for (_, j), c in a.items():
        out[j] += Fraction(c)
    while len(out) > 1 and out[-1] == 0:
        out.pop()
    return out


def uni_trim(a):
    a = list(a)
    while len(a) > 1 and a[-1] == 0:
        a.pop()
    return a


def uni_divmod(a, b):
    a = uni_trim(a)
    b = uni_trim(b)
    if len(b) == 1 and b[0] == 0:
        raise ZeroDivisionError
    q = [Fraction(0)] * max(1, len(a) - len(b) + 1)
    r = list(a)
    while not (len(r) == 1 and r[0] == 0) and len(r) >= len(b):
        d = len(r) - len(b)
        c = r[-1] / b[-1]
        q[d] += c
        for i, bi in enumerate(b):
            r[i + d] -= c * bi
        r = uni_trim(r)
    return uni_trim(q), uni_trim(r)


def uni_gcd(a, b):
    a, b = uni_trim(a), uni_trim(b)
    while not (len(b) == 1 and b[0] == 0):
        _, r = uni_divmod(a, b)
        a, b = b, r
    lc = a[-1]
    return uni_trim([x / lc for x in a])


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    args = ap.parse_args()

    r = {(1, 0): 1}
    s = {(0, 1): 1}
    r2, s2 = power(r, 2), power(s, 2)
    u = sub(r2, s2)
    v = scale(2, mul(r, s))
    w = add(r2, s2)
    u2, v2, w2 = power(u, 2), power(v, 2), power(w, 2)

    A = mul(u, sub(scale(4, v2), w2))
    B = mul(v, sub(scale(4, u2), w2))
    C = scale(4, mul(mul(u, v), w))
    D = power(w, 3)
    E = mul(u, add(scale(4, v2), w2))
    F = mul(v, add(scale(4, u2), w2))

    forms = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}
    degree_map = {k: homogeneous_degrees(p) for k, p in forms.items()}
    assert all(vv == [6] for vv in degree_map.values())

    # Euler-brick face-square identities.
    assert add(power(A, 2), power(B, 2)) == power(D, 2)
    assert add(power(A, 2), power(C, 2)) == power(E, 2)
    assert add(power(B, 2), power(C, 2)) == power(F, 2)

    # Exact rational inverse on the dense open r*w != 0.
    assert sub(E, A) == scale(2, mul(u, w2))
    assert sub(F, B) == scale(2, mul(v, w2))
    denominator = add(scale(2, D), sub(E, A))
    assert denominator == scale(4, mul(r2, w2))
    assert sub(F, B) == scale(4, mul(mul(r, s), w2))
    assert mul(r, sub(F, B)) == mul(s, denominator)

    # The edge map [A:B:C] has no common factor on r != 0.
    # A common homogeneous factor other than r would survive after r=1.
    g = uni_gcd(to_affine_t(A), to_affine_t(B))
    g = uni_gcd(g, to_affine_t(C))
    gcd_degree = len(g) - 1
    assert gcd_degree == 0
    # The missing projective point r=0 is not a base point because A(0,1)=1.
    a_at_r0_s1 = A.get((0, 6), 0)
    assert a_at_r0_s1 != 0

    result = {
        "status": "PASS",
        "all_six_coordinate_forms_homogeneous_degree": 6,
        "edge_map_ABC_common_factor_degree": gcd_degree,
        "edge_map_basepoint_free_on_P1": True,
        "euler_brick_three_face_square_identities": True,
        "inverse_identity": "s/r=(F-B)/(2D+E-A)",
        "parameterization_generically_birational": True,
        "pullback_edge_O1_degree": 6,
        "physical_M_degree_given_split_B_adapter": 6,
        "fixed_curve_height_exponent": "2/6=1/3",
        "degree_map": degree_map,
    }
    Path(args.out).write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
