#!/usr/bin/env python3
"""Exact verifier for the Stage33-12 degenerate Clifford q-fingerprint adapter."""

from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


HERE = Path(__file__).resolve().parent
CERT = HERE / "j2-degenerate-clifford-q-fingerprint-adapter.json"


def trim(p):
    p = [Fraction(x) for x in p]
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return p


def sub(a, b):
    n = max(len(a), len(b))
    return trim([
        (a[i] if i < len(a) else 0) - (b[i] if i < len(b) else 0)
        for i in range(n)
    ])


def mul(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return trim(out)


def deriv(a):
    if len(a) <= 1:
        return [Fraction(0)]
    return trim([i * a[i] for i in range(1, len(a))])


def divmod_poly(a, b):
    a = trim(a)
    b = trim(b)
    if b == [0]:
        raise ZeroDivisionError
    if len(a) < len(b):
        return [Fraction(0)], a
    quotient = [Fraction(0)] * (len(a) - len(b) + 1)
    remainder = a[:]
    while remainder != [0] and len(remainder) >= len(b):
        k = len(remainder) - len(b)
        c = remainder[-1] / b[-1]
        quotient[k] += c
        remainder = sub(remainder, [Fraction(0)] * k + [c * x for x in b])
    return trim(quotient), trim(remainder)


def monic(a):
    a = trim(a)
    if a == [0]:
        return a
    lead = a[-1]
    return trim([x / lead for x in a])


def gcd_poly(a, b):
    a, b = trim(a), trim(b)
    while b != [0]:
        _, remainder = divmod_poly(a, b)
        a, b = b, remainder
    return monic(a)


def main():
    data = json.loads(CERT.read_text(encoding="utf-8"))

    # Coefficients are ascending in t.
    t2 = [0, 0, 1]
    one = [1]
    tm1 = sub(t2, one)
    r = mul(tm1, tm1)                    # (t^2-1)^2
    q = [1, 0, -6, 0, 1]               # t^4-6t^2+1
    four_t2 = [0, 0, 4]

    assert sub(r, q) == four_t2
    assert gcd_poly(q, deriv(q)) == [Fraction(1)]
    assert len(q) > 1  # squarefree nonconstant => not a square in Qbar(t)

    defs = data["definitions"]
    assert defs["r"] == "(t^2-1)^2"
    assert defs["q"] == "t^4-6*t^2+1"
    assert defs["identity"] == "r-q=4*t^2"

    rep = data["split_symmetric_determinantal_representation"]
    assert rep["matrix"] == "diag(X, X-r, X-q)"
    assert rep["determinant"] == "X*(X-r)*(X-q)"
    assert rep["determinant_exact"] is True
    assert rep["even_clifford_quaternion"] == "(-X*(X-r), -X*(X-q))"

    covers = {
        item["component"]: item["geometric_squareclass"]
        for item in data["branch_component_ruling_covers"]
    }
    assert covers == {"C0": "q", "Cr": "1", "Cq": "q"}
    assert data["geometric_component_cover_fingerprint"] == ["q", "1", "q"]
    assert data["q_squarefree"] is True
    assert data["q_geometrically_nonsquare"] is True
    assert data["named_j2_branch_normalization"] == "z^2=q(t)=t^4-6*t^2+1"

    fw = data["semantic_firewalls"]
    required_false = [
        "global_admissible_double_cover_identified",
        "global_theta_characteristic_identified",
        "named_cv_j2_equals_split_clifford_class_certified",
        "j2_hermite_inverse_selected",
        "j2_explicit_torsor_surface_materialized",
        "j2_marked_brauer_coordinate_selected",
        "stage33_12_closed_exact",
        "stage33_13_release",
        "theorem_credit",
        "receiver_credit",
        "endpoint_credit",
        "perfect_cuboid_existence_claim",
        "perfect_cuboid_nonexistence_claim",
    ]
    assert all(fw[key] is False for key in required_false)

    assert data["status"] == "PASS_EXACT_GEOMETRIC_FINGERPRINT_NOT_YET_GLOBAL_THETA_GLUE"
    print("PASS: exact degenerate Clifford q-fingerprint [q,1,q]; global theta/J2 identification remains open.")


if __name__ == "__main__":
    main()
