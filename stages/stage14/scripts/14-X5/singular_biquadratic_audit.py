#!/usr/bin/env python3
"""Deterministic audit for Stage14-X5 singular-locus classification.

The singular-locus theorem is proved algebraically in result.md. This script
regresses the exact merged s7-27 ratio receiver, checks the universal
normalization and lambda=4 factorization, and records finite physical lambda=4
hits only as diagnostics.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path

HERE = Path(__file__).resolve()
S27_AUDIT = HERE.parents[1] / "14-s7-27" / "full_signed_quotient_curve_audit.py"
spec = spec_from_file_location("stage14_s727_audit", S27_AUDIT)
assert spec is not None and spec.loader is not None
s27 = module_from_spec(spec)
spec.loader.exec_module(s27)


def audit_pair(a: dict[str, int], b: dict[str, int]):
    # First retain every merged s7-27 exact check.
    s27.audit_pair(a, b)

    cells, triple, _, hs = s27.ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    _, hk_minus, _, hx_minus = hs

    r = a["r"] * b["r"]
    s = a["s"] * b["s"]
    X = a["x"] * b["x"]
    Y = a["y"] * b["y"]

    A = alpha * r
    D = delta * s
    P = R * X
    Q = J * Y
    assert D > A > 0
    assert Q > P > 0
    assert hk_minus == D * D - A * A
    assert hx_minus == Q * Q - P * P

    # The coefficient-invariant physical lambda.
    lam = Fraction(16 * A * D * P * Q, hk_minus * hx_minus)
    assert lam > 0

    # Universal normalized physical point.
    u = Fraction(D + A, D - A)
    v = Fraction(Q + P, Q - P)
    assert u > 1 and v > 1
    assert (u * u - 1) * (v * v - 1) == lam * u * v

    singular = lam == 4
    if singular:
        f_plus = u * v + u + v - 1
        f_phys = u * v - u - v - 1
        assert f_plus > 0
        assert f_phys == 0
        assert (u - 1) * (v - 1) == 2

        t = Fraction(A, D)
        z = Fraction(P, Q)
        assert t + z + t * z == 1
        assert D * (Q - P) == A * (Q + P)
        assert Q * (D - A) == P * (D + A)

    return singular, lam, triple


def universal_factor_audit() -> None:
    # At lambda=4 the normalized polynomial factors exactly. Test the
    # coefficient identity on a deterministic rational grid.
    vals = [Fraction(-3, 2), Fraction(-1, 2), Fraction(1, 3), Fraction(2), Fraction(5, 2)]
    for u in vals:
        for v in vals:
            lhs = (u * u - 1) * (v * v - 1) - 4 * u * v
            rhs = (u * v + u + v - 1) * (u * v - u - v - 1)
            assert lhs == rhs

    # Positive physical component witness: u=2 -> v=3.
    u = Fraction(2)
    v = Fraction(3)
    assert (u * u - 1) * (v * v - 1) == 4 * u * v
    assert u * v - u - v - 1 == 0
    assert u * v + u + v - 1 > 0


def finite_physical_audit(limit: int = 600):
    groups = s27.ch.make_groups(limit)
    checked = 0
    singular_hits = 0
    singular_triples = set()
    lambdas = set()

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                singular, lam, triple = audit_pair(a, b)
                checked += 1
                lambdas.add(lam)
                if singular:
                    singular_hits += 1
                    singular_triples.add(triple)

    assert checked > 0
    return checked, singular_hits, len(singular_triples), len(lambdas)


def boundary_audit() -> None:
    root = HERE.parents[4]
    s27_text = (root / "stages/stage14/14-s7-27/result.md").read_text()
    assert "STAGE14_S7_27=COMPLETE_FULL_SIGNED_QUOTIENT_DIVISOR_COLLAPSE_AND_RECIPROCAL_BIQUADRATIC_REDUCTION" in s27_text
    assert "RECIPROCAL_RATIO_BIDEGREE_2_2_CURVE_PROVED=true" in s27_text
    assert "TOP_THETA_RECIPROCAL_BIQUADRATIC_MODULUS_RATIO_INCIDENCE_PROVED=false" in s27_text


def main() -> None:
    boundary_audit()
    universal_factor_audit()
    checked, singular_hits, singular_triples, distinct_lambdas = finite_physical_audit()

    print("Stage14-X5 singular biquadratic audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"distinct finite physical lambda values: {distinct_lambdas}")
    print(f"finite physical lambda=4 hits: {singular_hits}")
    print(f"finite residual triples with lambda=4: {singular_triples}")
    print("nonzero singular lambda values over char 0: +/-4 (algebraic theorem in result.md)")
    print("physical singular lambda: 4 only")
    print("lambda=4 factorization: exact")
    print("physical positive component: uv-u-v-1=0")
    print("smooth positive lambda !=4 fibers: genus one")
    print("singular Mobius incidence: UNPROVED")
    print("smooth physical height/lift transfer: UNPROVED")


if __name__ == "__main__":
    main()
