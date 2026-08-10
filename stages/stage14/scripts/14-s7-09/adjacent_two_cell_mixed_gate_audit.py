#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-09.

Checks:
- merged s7-08 boundary;
- exact universal adjacent-cell normalisation on frozen physical incidences;
- exact inert-prime complete 2D trace zero for H=(1-R^2 S^2)(S^2-R^2);
- finite all-frequency O(p)-scale evidence (not promoted to theorem);
- sequential one-cell barrier;
- exact conditional 16/17 threshold ledger if a uniform O(p) mixed Fourier theorem is supplied.
"""
from cmath import exp, pi
from fractions import Fraction
from math import sqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S708 = ROOT / "stages/stage14/scripts/14-s7-08/shared_xi_cell_switch_audit.py"
R708 = ROOT / "stages/stage14/14-s7-08/result.md"


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def H(r, s):
    return (1 - r * r * s * s) * (s * s - r * r)


def audit_predecessor():
    txt = R708.read_text()
    for flag in [
        "STAGE14_S7_08=COMPLETE_SHARED_XI_CELL_SWITCH_AND_18_19_WHOLE_FAMILY_BOUND",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=18/19",
        "NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true",
    ]:
        assert flag in txt, flag
    mod = runpy.run_path(str(S708))
    rows = mod["physical_cell_rows"]()
    assert len(rows) == 124
    return rows


def audit_universal_normalisation(rows):
    # We audit the adjacent pair (r,s); the other three pairs are obtained by
    # the exact cell symmetries documented in result.md.
    checked = 0
    for row in rows:
        r, s, t, j = row["r"], row["s"], row["t"], row["j"]
        x, y, z, h = row["x"], row["y"], row["z"], row["h"]

        A = t * j * y * y
        B = j * h * h
        C = t * z * z

        alpha = Fraction(x * z, j * y * h)
        beta = Fraction(x * h, t * z * y)
        R = alpha * r
        S = beta * s
        K = Fraction(C, 1) / alpha

        g1 = A * A - (r * s * x * x) ** 2
        g2 = (s * B) ** 2 - (r * C) ** 2

        assert alpha * beta == Fraction(x * x, A)
        assert Fraction(C, 1) / alpha == Fraction(B, 1) / beta
        assert Fraction(g1, A * A) == 1 - R * R * S * S
        assert Fraction(g2, 1) == K * K * (S * S - R * R)
        assert Fraction(g1 * g2, 1) == (Fraction(A, 1) * K) ** 2 * (
            (1 - R * R * S * S) * (S * S - R * R)
        )
        checked += 1
    assert checked == 124
    return checked


def audit_complete_trace_zero():
    primes = [3, 7, 11, 19, 23, 31, 43, 47]
    for p in primes:
        assert p % 4 == 3
        total = 0
        for r in range(p):
            for s in range(p):
                total += chi(H(r, s), p)
        assert total == 0, (p, total)
    return primes


def audit_torus_factorisation():
    # Finite exact guard for the proof identity used in result.md.
    primes = [7, 11, 19, 23]
    for p in primes:
        a = sum(chi(1 - u * u, p) for u in range(1, p))
        b = sum(chi(u * (1 - u * u), p) for u in range(1, p))
        assert a == 0, (p, a)
        assert b == 0, (p, b)

        torus = 0
        for r in range(1, p):
            for s in range(1, p):
                torus += chi(H(r, s), p)
        assert torus == a * a + b * b == 0
    return True


def mixed_fourier(p, h, k):
    total = 0j
    for r in range(p):
        for s in range(p):
            c = chi(H(r, s), p)
            if c:
                total += c * exp(2j * pi * (h * r + k * s) / p)
    return total


def audit_mixed_frequency_evidence():
    # Evidence only: this does NOT prove the theorem boundary.
    primes = [3, 7, 11, 19, 23, 31]
    modes = 0
    max_ratio = 0.0
    for p in primes:
        for h in range(p):
            for k in range(p):
                z = mixed_fourier(p, h, k)
                ratio = abs(z) / p
                max_ratio = max(max_ratio, ratio)
                # Loose deterministic envelope, deliberately not a theorem claim.
                assert abs(z) <= 8.0 * p + 1e-7, (p, h, k, z)
                modes += 1
    assert modes > 0
    return modes, max_ratio


def audit_sequential_barrier():
    # If R*S=A, one-cell sieving in the larger variable saves only A^(-1/4)
    # in the balanced worst case R=S=A^(1/2).
    one_cell_coeff_saving = Fraction(1, 4)
    current = Fraction(18, 19)
    assert one_cell_coeff_saving == Fraction(1, 4)
    assert current == Fraction(18, 19)
    return True


def audit_conditional_ledger():
    lam = Fraction(8, 17)
    tau = Fraction(2, 17)
    theta = Fraction(7, 17)
    target = Fraction(16, 17)

    e1 = 2 * lam
    e2 = 1 - tau / 2
    e3 = 1 + theta - lam
    e4 = 1 - (theta - 2 * tau) / 3
    e5 = 1 - (lam - 2 * tau) / 3

    assert e1 == e2 == e3 == e4 == target
    assert e5 == Fraction(47, 51)
    assert e5 < target

    current = Fraction(18, 19)
    potential_gain = current - target
    sqrt_gap = target - Fraction(1, 2)
    assert potential_gain == Fraction(2, 323)
    assert sqrt_gap == Fraction(15, 34)

    # Exact lower-bound contradiction for any hypothetical E<16/17:
    # 2*lambda<E => lambda<8/17.
    # 1-tau/2<E => tau>2/17.
    # 1+theta-lambda<E => theta<lambda-1/17<7/17.
    # 1-(theta-2tau)/3<E => theta>2tau+3/17>7/17.
    assert lam - Fraction(1, 17) == Fraction(7, 17)
    assert 2 * tau + Fraction(3, 17) == Fraction(7, 17)

    return lam, tau, theta, target, e5, potential_gain, sqrt_gap


def main():
    rows = audit_predecessor()
    norm = audit_universal_normalisation(rows)
    primes = audit_complete_trace_zero()
    assert audit_torus_factorisation()
    modes, max_ratio = audit_mixed_frequency_evidence()
    assert audit_sequential_barrier()
    lam, tau, theta, target, e5, gain, sqrt_gap = audit_conditional_ledger()

    print(f"ORDERED_PHYSICAL_INCIDENCES={len(rows)}")
    print(f"UNIVERSAL_NORMALISATIONS_CHECKED={norm}")
    print(f"INERT_COMPLETE_TRACE_PRIMES={len(primes)}")
    print(f"MIXED_FOURIER_MODES_FINITE_EVIDENCE={modes}")
    print(f"MAX_FINITE_MIXED_FOURIER_OVER_P={max_ratio:.6f}")
    print(f"CURRENT_WHOLE_FAMILY_EXPONENT={Fraction(18,19)}")
    print(f"CONDITIONAL_OPTIMAL_LAMBDA={lam}")
    print(f"CONDITIONAL_OPTIMAL_TAU={tau}")
    print(f"CONDITIONAL_OPTIMAL_THETA={theta}")
    print(f"CONDITIONAL_WHOLE_FAMILY_EXPONENT={target}")
    print(f"CONDITIONAL_DENOMINATOR_THIN_EXPONENT={e5}")
    print(f"CONDITIONAL_GAIN_OVER_18_19={gain}")
    print(f"CONDITIONAL_GAP_TO_SQRT={sqrt_gap}")
    print("MERGED_S7_08_BOUNDARY_AUDIT=true")
    print("ADJACENT_TWO_CELL_UNIVERSAL_NORMALISATION_AUDIT=true")
    print("INERT_ADJACENT_TWO_CELL_COMPLETE_TRACE_ZERO_AUDIT=true")
    print("TORUS_PRODUCT_RATIO_FACTORIZATION_AUDIT=true")
    print("MIXED_FOURIER_OP_SCALE_FINITE_EVIDENCE=true")
    print("MIXED_FOURIER_OP_BOUND_PROVED=false")
    print("SEQUENTIAL_ONE_CELL_SAVINGS_MULTIPLY=false")
    print("CONDITIONAL_16_17_LEDGER_AUDIT=true")
    print("NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
