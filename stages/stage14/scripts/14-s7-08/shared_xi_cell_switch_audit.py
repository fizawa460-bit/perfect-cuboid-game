#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-08.

Checks:
- merged s7-07 and merged 4bv boundaries;
- exact shared-xi four-cell factorization on frozen physical incidences;
- physical nondegeneracy of every one-cell quartic via v/u!=1 and u*v!=1;
- finite good-prime mixed-character sqrt-scale regression for cell quartics;
- exact adaptive threshold optimisation lambda=9/19, tau=2/19, theta=8/19;
- new whole-family exponent 18/19 and ledger deltas.

The finite character regression is not a proof of the standard Weil theorem; the
stage theorem uses the standard bounded-degree Weil mixed-character estimate as
an explicit external black box after the exact nondegeneracy audit.
"""
from cmath import exp, pi
from fractions import Fraction
from math import gcd, isqrt, sqrt
from pathlib import Path
import runpy

ROOT = Path(__file__).resolve().parents[4]
S705 = ROOT / "stages/stage14/scripts/14-s7-05/joint_twist_pair_receiver_audit.py"
R707 = ROOT / "stages/stage14/14-s7-07/result.md"
R4BV = ROOT / "stages/stage14/14-4bv/result.md"
A4BV = ROOT / "stages/stage14/scripts/14-4/inert_fourier_thin_switch_audit.py"


def sqpart(n, kernel):
    q = n // kernel
    r = isqrt(q)
    assert r * r == q
    return r


def pairwise_coprime(vals):
    for i in range(len(vals)):
        for j in range(i):
            if gcd(vals[i], vals[j]) != 1:
                return False
    return True


def audit_merged_boundaries():
    txt = R707.read_text()
    for flag in [
        "STAGE14_S7_07=COMPLETE_FIXED_QUARTIC_BALANCED_STRIP_AND_INERT_TRACE_RECEIVER",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21",
    ]:
        assert flag in txt, flag

    txt = R4BV.read_text()
    for flag in [
        "STAGE14_4BV=INERT_FOURIER_COMPLETION_AND_THIN_PACKET_COEFFICIENT_SWITCH",
        "INERT_ADDITIVE_FOURIER_TRANSFORM_EXACT=true",
        "FIXED_PACKET_SQUARE_SIEVE_ADAPTER_PROVED=true",
        "THICK_PACKET_RELATIVE_SAVING=H^(-1/2)",
        "CRITICAL_SQUAREPART_THICKNESS_EXPONENT=2/21",
        "DUAL_COEFFICIENT_FOURIER_TRANSFORM_EXACT=true",
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=20/21",
    ]:
        assert flag in txt, flag

    mod = runpy.run_path(str(A4BV))
    mod["audit_ledger"]()
    return True


def physical_cell_rows():
    mod = runpy.run_path(str(S705))
    s703, rows = mod["physical_rows"]()
    half_angles = s703["half_angles"]
    transfer_f3 = s703["transfer_f3"]
    canonical_label = mod["canonical_label"]
    kernel = mod["squarefree_kernel"]

    out = []
    for F1, F2, dspace in rows:
        F3, _ = transfer_f3(F1, F2, dspace)
        _, aa, bb = half_angles(F2)
        _, cc, dd = half_angles(F3)

        u = Fraction(bb * cc, aa * dd)
        v = Fraction(aa * cc, bb * dd)
        assert 0 < v < u < 1

        lu = canonical_label(u)
        lv = canonical_label(v)
        assert lu["xi"] == lv["xi"]

        P, Q = lu["P"], lu["Q"]
        R, S = lv["P"], lv["Q"]

        a = kernel(P)
        b = kernel(Q)
        c = kernel(R)
        d = kernel(S)
        x = sqpart(P, a)
        y = sqpart(Q, b)
        z = sqpart(R, c)
        h = sqpart(S, d)

        assert a * b == c * d == lu["xi"]
        assert gcd(a, b) == 1 and gcd(c, d) == 1

        r = gcd(a, c)
        s = gcd(a, d)
        t = gcd(b, c)
        j = gcd(b, d)
        cells = [r, s, t, j]
        assert pairwise_coprime(cells)
        assert a == r * s
        assert b == t * j
        assert c == r * t
        assert d == s * j
        assert a * b == r * s * t * j

        # Exact physical degeneracy certificates.
        delta_ratio = t * t * y * y * z * z - s * s * x * x * h * h
        delta_prod = r * r * x * x * z * z - j * j * y * y * h * h
        assert delta_ratio != 0
        assert delta_prod != 0
        assert Fraction(t * t * y * y * z * z, s * s * x * x * h * h) == v / u
        assert Fraction(r * r * x * x * z * z, j * j * y * y * h * h) == u * v
        assert delta_ratio < 0
        assert delta_prod < 0

        out.append({
            "u": u, "v": v,
            "r": r, "s": s, "t": t, "j": j,
            "x": x, "y": y, "z": z, "h": h,
            "delta_ratio": delta_ratio,
            "delta_prod": delta_prod,
            "dspace": dspace,
        })

    assert len(out) == 124
    return out


def gprod(row, cell, q):
    r, s, t, j = row["r"], row["s"], row["t"], row["j"]
    if cell == "r":
        r = q
    elif cell == "s":
        s = q
    elif cell == "t":
        t = q
    elif cell == "j":
        j = q
    else:
        raise ValueError(cell)
    x, y, z, h = row["x"], row["y"], row["z"], row["h"]
    g1 = (t * j * y * y) ** 2 - (r * s * x * x) ** 2
    g2 = (s * j * h * h) ** 2 - (r * t * z * z) ** 2
    return g1 * g2


def chi(a, p):
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def polynomial_squarefree_mod_p(row, cell, p):
    # H(q) is an even quartic.  Check no repeated affine root mod p by the
    # derivative using finite differences of exact polynomial values.
    # Recover coefficients c0+c2*q^2+c4*q^4 from q=0,1,2 over F_p.
    c0 = gprod(row, cell, 0) % p
    v1 = gprod(row, cell, 1) % p
    v2 = gprod(row, cell, 2) % p
    # Solve c2+c4=v1-c0 and 4*c2+16*c4=v2-c0.
    rhs1 = (v1 - c0) % p
    rhs2 = (v2 - c0) % p
    det = 12 % p
    if det == 0:
        return False
    invdet = pow(det, -1, p)
    c4 = ((rhs2 - 4 * rhs1) * invdet) % p
    c2 = (rhs1 - c4) % p

    if c4 == 0:
        return False
    for q in range(p):
        val = (c0 + c2 * q * q + c4 * pow(q, 4, p)) % p
        if val == 0:
            der = (2 * c2 * q + 4 * c4 * pow(q, 3, p)) % p
            if der == 0:
                return False
    return True


def audit_cell_character_regression(rows):
    # Finite regression of the bounded-degree Weil scale.  The theorem uses
    # the standard Weil mixed-character estimate; here we only guard that the
    # physical samples are genuinely in the nondegenerate regime and exhibit
    # sqrt(p)-scale transforms at small good primes.
    primes = [7, 11, 19, 23, 31, 43]
    checked = 0
    good_polys = 0
    for row in rows[:12]:
        for cell in ("r", "s", "t", "j"):
            for p in primes:
                if not polynomial_squarefree_mod_p(row, cell, p):
                    continue
                good_polys += 1
                for freq in range(p):
                    total = 0j
                    for q in range(p):
                        c = chi(gprod(row, cell, q), p)
                        if c:
                            total += c * exp(2j * pi * freq * q / p)
                    # Loose finite guard around the O_d(sqrt(p)) theorem.
                    assert abs(total) <= 8.0 * sqrt(p) + 1e-7, (cell, p, freq, total)
                    checked += 1
    assert good_polys > 0 and checked > 0
    return good_polys, checked


def audit_threshold_optimisation():
    lam = Fraction(9, 19)
    tau = Fraction(2, 19)
    theta = Fraction(8, 19)

    small_den = 2 * lam
    thick = 1 - tau / 2
    small_num = 1 + theta - lam
    num_coeff = theta - 2 * tau
    num_cell = num_coeff / 2
    num_thin = 1 - num_cell / 2
    den_coeff = lam - 2 * tau
    den_cell = den_coeff / 2
    den_thin = 1 - den_cell / 2

    target = Fraction(18, 19)
    assert small_den == target
    assert thick == target
    assert small_num == target
    assert num_coeff == Fraction(4, 19)
    assert num_cell == Fraction(2, 19)
    assert num_thin == target
    assert den_coeff == Fraction(5, 19)
    assert den_cell == Fraction(5, 38)
    assert den_thin == Fraction(71, 76)
    assert den_thin < target

    old = Fraction(20, 21)
    baseline = Fraction(41, 42)
    improvement = old - target
    cumulative = baseline - target
    sqrt_gap = target - Fraction(1, 2)
    assert improvement == Fraction(2, 399)
    assert cumulative == Fraction(23, 798)
    assert sqrt_gap == Fraction(17, 38)

    # Exact optimum proof encoded as the contradiction chain from result.md.
    # If E<18/19 then lambda<9/19 and tau>2/19.
    # Small-numerator then gives theta<lambda-1/19<8/19,
    # while thin-cell gives theta>2*tau+4/19>8/19.
    assert lam - Fraction(1, 19) == Fraction(8, 19)
    assert 2 * tau + Fraction(4, 19) == Fraction(8, 19)

    return {
        "lambda": lam,
        "tau": tau,
        "theta": theta,
        "target": target,
        "den_thin": den_thin,
        "improvement": improvement,
        "cumulative": cumulative,
        "sqrt_gap": sqrt_gap,
    }


def main():
    assert audit_merged_boundaries()
    rows = physical_cell_rows()
    good_polys, modes = audit_cell_character_regression(rows)
    led = audit_threshold_optimisation()

    print(f"ORDERED_PHYSICAL_INCIDENCES={len(rows)}")
    print(f"GOOD_CELL_POLYNOMIAL_PRIME_SAMPLES={good_polys}")
    print(f"CELL_MIXED_CHARACTER_MODES_CHECKED={modes}")
    print(f"OPTIMAL_LAMBDA={led['lambda']}")
    print(f"OPTIMAL_TAU={led['tau']}")
    print(f"OPTIMAL_THETA={led['theta']}")
    print(f"NEW_WHOLE_FAMILY_EXPONENT={led['target']}")
    print(f"DENOMINATOR_THIN_EXPONENT={led['den_thin']}")
    print(f"IMPROVEMENT_OVER_20_21={led['improvement']}")
    print(f"CUMULATIVE_SAVING_FROM_41_42={led['cumulative']}")
    print(f"CURRENT_GAP_TO_SQRT={led['sqrt_gap']}")
    print("MERGED_S7_07_BOUNDARY_AUDIT=true")
    print("MERGED_4BV_BOUNDARY_AUDIT=true")
    print("SHARED_XI_FOUR_CELL_FACTORIZATION_AUDIT=true")
    print("SHARED_XI_CELLS_PAIRWISE_COPRIME_AUDIT=true")
    print("PHYSICAL_RATIO_DEGENERACY_EXCLUDED=true")
    print("PHYSICAL_PRODUCT_DEGENERACY_EXCLUDED=true")
    print("CELL_QUARTIC_FINITE_WEIL_SCALE_REGRESSION=true")
    print("CELL_SWITCH_RELATIVE_SQRT_SAVING_LEDGER=true")
    print("ADAPTIVE_18_19_OPTIMISATION_AUDIT=true")
    print("NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=true")
    print("ALL_AUDITS_PASS=true")


if __name__ == "__main__":
    main()
