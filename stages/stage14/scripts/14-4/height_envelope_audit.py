#!/usr/bin/env python3
"""Stage14-4ac deterministic audit for the rational-slope height envelope.

This audit checks three Stage14-intrinsic claims:

1. the exact number a(S) of oriented primitive Pythagorean face data with
   distinguished shared leg S;
2. the rational-slope/height identities on the independent face-pair-first
   census through B=10000;
3. the frozen finite N2/sqrt(B) diagnostic without promoting it to an
   asymptotic theorem.

It does not fit or prove a true Stage14 growth law.
"""

from math import gcd, isqrt, log, sqrt

FACE_LEG_AUDIT_MAX = 1000
CENSUS_AUDIT_B = 10000
LOCKED_FINITE = [
    (1000, 2, 2, 0, 0),
    (2000, 5, 2, 2, 1),
    (5000, 15, 6, 6, 3),
    (10000, 25, 9, 11, 5),
    (20000, 42, 16, 16, 10),
    (50000, 62, 24, 24, 14),
    (100000, 89, 33, 33, 23),
    (200000, 116, 42, 50, 24),
    (500000, 188, 70, 78, 40),
    (1000000, 255, 98, 101, 56),
    (2000000, 356, 142, 134, 80),
]
EXPECTED_10K = (9, 11, 5, 0)


def omega(n: int) -> int:
    """Number of distinct prime divisors."""
    out = 0
    p = 2
    while p * p <= n:
        if n % p == 0:
            out += 1
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out += 1
    return out


def face_multiplicity_formula(S: int) -> int:
    """Number of primitive oriented Pythagorean faces with shared leg S."""
    if S <= 1 or S % 4 == 2:
        return 0
    return 1 << (omega(S) - 1)


def enumerate_face_leg_multiplicities(limit: int) -> list[int]:
    counts = [0] * (limit + 1)
    # For an odd difference leg S, m <= (S+1)/2; for an even product leg
    # 2mn=S, m<=S/2. m<=limit is therefore a safe finite audit bound.
    for m in range(2, limit + 1):
        for n in range(1, m):
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            D = m * m - n * n
            P = 2 * m * n
            if D <= limit:
                counts[D] += 1
            if P <= limit:
                counts[P] += 1
    return counts


def primitive_oriented_faces(B: int):
    out = []
    m = 2
    while m * m + 1 <= B:
        for n in range(1, m):
            H = m * m + n * n
            if H > B:
                continue
            if gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            D = m * m - n * n
            P = 2 * m * n
            out.append((D, P, H))
            out.append((P, D, H))
        m += 1
    return out


def is_square(v: int) -> bool:
    r = isqrt(v)
    return r * r == v


def slope_height_census(B: int):
    faces = primitive_oriented_faces(B)
    exact = [0, 0, 0]
    triple = 0
    identity_checks = 0

    for S1, X1, H1 in faces:
        for S2, X2, H2 in faces:
            g = gcd(S1, S2)
            alpha = S1 // g
            beta = S2 // g
            L = g * alpha * beta
            x = beta * X1
            y = alpha * X2
            if not x < y:
                continue

            u = beta * H1
            d2 = u * u + y * y
            d = isqrt(d2)
            if d * d != d2 or d > B:
                continue

            # Exact rational-slope identities, checked without floating point.
            assert x * S1 == L * X1
            assert y * S2 == L * X2
            assert u * S1 == L * H1
            assert L * L + x * x + y * y == d * d

            # M=L*max(1,t2)=max(e,y), because x<y.
            M = max(L, y)
            assert M < d
            assert d * d < 3 * M * M

            # Chamber is position of 1 relative to t1<t2.
            if L < x:
                direction = 0
            elif L < y:
                direction = 1
            else:
                direction = 2

            if is_square(x * x + y * y):
                triple += 1
            else:
                exact[direction] += 1
            identity_checks += 1

    return {
        "oriented_primitive_face_data": len(faces),
        "accepted_raw_pair_incidences": identity_checks,
        "exactly_two": exact,
        "triple_incidences": triple,
    }


def finite_sqrt_diagnostic():
    rows = []
    for B, N2, a, b, c in LOCKED_FINITE:
        root = sqrt(B)
        rows.append(
            {
                "B": B,
                "N2": N2,
                "N2_over_sqrtB": N2 / root,
                "a_over_sqrtB": a / root,
                "b_over_sqrtB": b / root,
                "c_over_sqrtB": c / root,
            }
        )

    late = [r["N2_over_sqrtB"] for r in rows if r["B"] >= 200000]
    mean = sum(late) / len(late)
    sd = sqrt(sum((x - mean) ** 2 for x in late) / len(late))

    effective = []
    late_raw = [(B, N2) for B, N2, *_ in LOCKED_FINITE if B >= 100000]
    for (B1, N1), (B2, N2) in zip(late_raw, late_raw[1:]):
        effective.append(
            {
                "B1": B1,
                "B2": B2,
                "pure_power_effective_exponent": log(N2 / N1) / log(B2 / B1),
            }
        )

    return {
        "rows": rows,
        "late_range_B_min": 200000,
        "late_range_mean_N2_over_sqrtB": mean,
        "late_range_population_sd": sd,
        "late_range_coefficient_of_variation": sd / mean,
        "late_range_min_N2_over_sqrtB": min(late),
        "late_range_max_N2_over_sqrtB": max(late),
        "effective_power_exponents": effective,
        "sqrtB_asymptotic_claimed": False,
    }


def main():
    counts = enumerate_face_leg_multiplicities(FACE_LEG_AUDIT_MAX)
    mismatches = [
        (S, counts[S], face_multiplicity_formula(S))
        for S in range(1, FACE_LEG_AUDIT_MAX + 1)
        if counts[S] != face_multiplicity_formula(S)
    ]
    if mismatches:
        raise SystemExit(f"face multiplicity mismatch: {mismatches[:10]}")

    census = slope_height_census(CENSUS_AUDIT_B)
    got = (*census["exactly_two"], census["triple_incidences"])
    if got != EXPECTED_10K:
        raise SystemExit(f"slope-height census mismatch: {got} != {EXPECTED_10K}")

    # For c(n)=2^omega(n), the p-local lcm pair series has exact max-k
    # coefficient (1+2k)^2-(2k-1)^2=8k, hence
    # F_p(x)=1+sum_{k>=1}8k x^k = 1+8x/(1-x)^2.
    print("FACE_MULTIPLICITY_FORMULA_AUDIT=PASS")
    print("SLOPE_HEIGHT_IDENTITY_AUDIT=PASS")
    print("LCM_MAJORANT_LOCAL_FACTOR=1+8x/(1-x)^2")
    print("LCM_MAJORANT_POLE_ORDER=8")
    print("CENSUS_10K=", got)
    print("FINITE_SQRT_DIAGNOSTIC=", finite_sqrt_diagnostic())


if __name__ == "__main__":
    main()
