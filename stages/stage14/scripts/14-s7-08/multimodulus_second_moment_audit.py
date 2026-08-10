#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-08.

Checks:
- merged s7-07 predecessor boundary;
- exact exponent optimisation for the direct inert-prime quadratic detector;
- validity of the R^2<=min(U,V) range at the optimiser;
- separate-side Cauchy exponent-one ceiling;
- exact hypercube Fourier countermodel: all nonprincipal marginal characters
  vanish while cross-scale support overlap is maximal;
- current 20/21 / required 1/21 ledger.
"""
from fractions import Fraction
from itertools import product
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S707 = ROOT / "stages/stage14/scripts/14-s7-07/balanced_strip_inert_trace_audit.py"
R707 = ROOT / "stages/stage14/14-s7-07/result.md"


def audit_predecessor():
    txt = R707.read_text()
    required = [
        "STAGE14_S7_07=COMPLETE_FIXED_QUARTIC_BALANCED_STRIP_AND_INERT_TRACE_RECEIVER",
        "CRITICAL_DENOMINATOR_EXPONENT=10/21",
        "BALANCED_DENOMINATOR_STRIP_UPPER=11/21",
        "INERT_PRIME_COMPLETE_CHARACTER_SUM_ZERO=true",
        "MULTI_MODULUS_INERT_LARGE_SIEVE_REQUIRED=true",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21",
    ]
    for flag in required:
        assert flag in txt, flag

    mod = runpy.run_path(str(S707))
    assert mod["audit_predecessor"]()
    mod["audit_inert_prime_zero_trace"]()
    mod["audit_inert_composite_zero_trace"]()
    return True


def audit_direct_square_sieve_exponents():
    # On UV=B, with primes p~B^rho and L~B^rho:
    # diagonal U^2 V^2/L -> exponent 2-rho
    # off diagonal UV R^4 -> exponent 1+4rho.
    # Balance: 2-rho = 1+4rho -> rho=1/5, exponent=9/5.
    rho = Fraction(1, 5)
    diagonal = Fraction(2, 1) - rho
    offdiag = Fraction(1, 1) + 4 * rho
    assert diagonal == offdiag == Fraction(9, 5)

    # The s7-07 incomplete-box theorem for m=pq requires R^2<=min(U,V).
    # The smallest critical denominator exponent is 10/21.
    assert 2 * rho == Fraction(2, 5)
    assert 2 * rho < Fraction(10, 21)

    current = Fraction(20, 21)
    assert diagonal > current
    return rho, diagonal


def audit_separate_side_cauchy_ledger():
    # Let U=B^alpha, V=B^beta.  On the central hard block alpha=beta=1/2.
    alpha = beta = Fraction(1, 2)
    self_u = 2 * alpha
    self_v = 2 * beta
    cauchy = (self_u + self_v) / 2
    assert self_u == 1
    assert self_v == 1
    assert cauchy == 1

    current = Fraction(20, 21)
    required = cauchy - current
    assert required == Fraction(1, 21)
    return cauchy, required


def char_value(signature, subset):
    out = 1
    for i in subset:
        out *= signature[i]
    return out


def audit_perfect_marginal_cancellation_countermodel(bits=8):
    # G=(Z/2)^bits represented as sign vectors.  Put one point on every
    # signature at both scales.  Every nonprincipal Fourier coefficient is
    # exactly zero, yet the two supports coincide completely.
    G = list(product((-1, 1), repeat=bits))
    N = len(G)

    principal_u = N
    principal_v = N
    assert principal_u == principal_v

    nonprincipal_checked = 0
    # Check every nonempty character/subset.
    for mask in range(1, 1 << bits):
        subset = [i for i in range(bits) if (mask >> i) & 1]
        su = sum(char_value(g, subset) for g in G)
        sv = sum(char_value(g, subset) for g in G)
        assert su == 0
        assert sv == 0
        nonprincipal_checked += 1

    # Direct overlap: one common point at every signature.
    overlap = N

    # Fourier Parseval cross-check.
    fourier_sum = principal_u * principal_v
    fourier_overlap = fourier_sum // N
    assert fourier_overlap == overlap == N

    return N, nonprincipal_checked, overlap


def audit_self_energy_diagonal_floor():
    # Abstract representation multiplicities.  The integer inequality
    # sum r(n)^2 >= sum r(n) is the diagonal obstruction behind any
    # separate-side L2 argument.
    samples = [
        [1, 1, 1, 1],
        [2, 1, 3],
        [4, 2, 1, 1, 5],
    ]
    for rs in samples:
        mass = sum(rs)
        energy = sum(r * r for r in rs)
        assert energy >= mass
    return len(samples)


def main():
    assert audit_predecessor()
    rho, raw = audit_direct_square_sieve_exponents()
    cauchy, required = audit_separate_side_cauchy_ledger()
    N, chars, overlap = audit_perfect_marginal_cancellation_countermodel()
    floor_cases = audit_self_energy_diagonal_floor()

    print(f"DIRECT_SQUARE_SIEVE_OPTIMAL_R_EXPONENT={rho}")
    print(f"DIRECT_SQUARE_SIEVE_OPTIMAL_RAW_EXPONENT={raw}")
    print(f"SEPARATE_SIDE_CAUCHY_EXPONENT={cauchy}")
    print(f"CROSS_SCALE_SAVING_REQUIRED_AT_CENTER={required}")
    print(f"COUNTERMODEL_SIGNATURES={N}")
    print(f"COUNTERMODEL_NONPRINCIPAL_CHARACTERS_CHECKED={chars}")
    print(f"COUNTERMODEL_SUPPORT_OVERLAP={overlap}")
    print(f"SELF_ENERGY_DIAGONAL_FLOOR_CASES={floor_cases}")
    print("MERGED_S7_07_PREDECESSOR_AUDIT=true")
    print("DIRECT_INERT_SQUARE_SIEVE_9_5_AUDIT=true")
    print("DIRECT_INERT_SQUARE_SIEVE_RANGE_VALID=true")
    print("SEPARATE_SIDE_CAUCHY_EXPONENT_ONE_AUDIT=true")
    print("PERFECT_MARGINAL_CANCELLATION_COUNTERMODEL=true")
    print("MARGINAL_EQUIDISTRIBUTION_DOES_NOT_FORCE_TRANSVERSALITY=true")
    print("CROSS_SCALE_RECURRENCE_REQUIRED=true")
    print("CURRENT_WHOLE_FAMILY_EXPONENT=20/21")
    print("NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
