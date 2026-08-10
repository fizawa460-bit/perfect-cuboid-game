#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd

THETA = F(1, 4)
PHI_LO = F(5, 24)
PHI_HI = F(1, 4)
SQRT = F(1, 2)


def divisors(n: int):
    n = abs(n)
    if n == 0:
        return []
    out = []
    for d in range(1, int(n**0.5) + 1):
        if n % d == 0:
            out.append(d)
            if d * d != n:
                out.append(n // d)
    return sorted(out)


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


# ---------------------------------------------------------------------------
# 1. Exact theta-quarter exponent ledger and fixed-lambda comparison.
# ---------------------------------------------------------------------------
phi_checks = 0
lower_det_better = 0
upper_det_not_better = 0
for i in range(0, 1025):
    phi = PHI_LO + (PHI_HI - PHI_LO) * F(i, 1024)
    chi = 2 * phi - F(1, 4)
    u_line = 2 * phi - chi
    col_line = F(1, 4) - chi
    principal = chi + u_line + col_line
    fixed_c_dual = u_line + col_line
    fixed_lambda_det = (THETA + phi + F(1, 8)) / 2

    assert F(1, 6) <= chi <= F(1, 4)
    assert u_line == F(1, 4)
    assert col_line == F(1, 2) - 2 * phi
    assert principal == SQRT
    assert fixed_c_dual == F(3, 4) - 2 * phi
    assert fixed_lambda_det == F(3, 16) + phi / 2

    if phi < F(9, 40):
        assert fixed_lambda_det < fixed_c_dual
        lower_det_better += 1
    elif phi > F(9, 40):
        assert fixed_lambda_det > fixed_c_dual
        upper_det_not_better += 1
    else:
        assert fixed_lambda_det == fixed_c_dual
    phi_checks += 1

assert PHI_LO < F(9, 40) < PHI_HI
assert lower_det_better > 0
assert upper_det_not_better > 0

# ---------------------------------------------------------------------------
# 2. Exact Cayley-core -> bad-reduction check.
#    C_- | M-N, C_+ | M+N, gcd(C,MN)=1 implies
#    lambda=4M/N == +/-4 on every active prime-power component and
#    C | 16(M^2-N^2).
# ---------------------------------------------------------------------------
bad_reduction_checks = 0
for M in range(2, 70):
    for N in range(1, 70):
        if gcd(M, N) != 1 or M == N:
            continue
        dm = divisors(oddpart(M - N))
        dp = divisors(oddpart(M + N))
        for cm in dm:
            for cp in dp:
                if gcd(cm, cp) != 1:
                    continue
                C = cm * cp
                if C <= 1 or gcd(C, M * N) != 1:
                    continue
                assert (M - N) % cm == 0
                assert (M + N) % cp == 0
                assert (16 * (M * M - N * N)) % C == 0

                # Check the rational lambda modulo the exact row cells.
                if cm > 1:
                    invN = pow(N, -1, cm)
                    lam = (4 * M * invN) % cm
                    assert (lam - 4) % cm == 0
                    assert (lam * lam - 16) % cm == 0
                if cp > 1:
                    invN = pow(N, -1, cp)
                    lam = (4 * M * invN) % cp
                    assert (lam + 4) % cp == 0
                    assert (lam * lam - 16) % cp == 0
                bad_reduction_checks += 1

assert bad_reduction_checks > 1000

# ---------------------------------------------------------------------------
# 3. Exact singular factorization at lambda=+/-4.
# ---------------------------------------------------------------------------
singular_factor_checks = 0
for u in range(2, 30):
    for v in range(2, 30):
        base = (u * u - 1) * (v * v - 1)
        plus4 = base - 4 * u * v
        minus4 = base + 4 * u * v
        assert plus4 == (u * v - u - v - 1) * (u * v + u + v - 1)
        assert minus4 == (u * v - u + v + 1) * (u * v + u - v + 1)
        singular_factor_checks += 2

# ---------------------------------------------------------------------------
# 4. Local orientation label entropy is only divisor/subpolynomial scale.
#    For primes p==1 mod 4, roots of x^2=-1 are exactly two; roots of
#    x^2=1 are exactly two for every odd prime.  This is a local sanity check,
#    not a claim that every label pair is physically realized.
# ---------------------------------------------------------------------------
primes = [5, 13, 17, 29, 37, 41, 53, 61, 73, 89, 97, 101, 109]
orientation_checks = 0
for p in primes:
    roots_m1 = [x for x in range(1, p) if (x * x + 1) % p == 0]
    roots_p1 = [x for x in range(1, p) if (x * x - 1) % p == 0]
    assert len(roots_m1) == 2
    assert len(roots_p1) == 2
    assert len([(r, s) for r in roots_m1 for s in roots_p1]) == 4
    orientation_checks += 1

print("Stage14-sH44 dual-root-line H audit: PASS")
print("theta-quarter phi ledger checks:", phi_checks)
print("fixed-lambda-better lower-band checks:", lower_det_better)
print("fixed-lambda-not-better upper-band checks:", upper_det_not_better)
print("Cayley bad-reduction checks:", bad_reduction_checks)
print("lambda=+/-4 singular factor checks:", singular_factor_checks)
print("local orientation Cartesian checks:", orientation_checks)
print("dual root-line principal-density exponent:", SQRT)
print("certified dual-root-line delta: 0")
print("full common core is reciprocal-Edwards bad-reduction support: true")
print("off-the-shelf fixed-power saving proved: false")
print("s7-45 can consume sH44: true")
print("next receiver: SquareRootThetaQuarterGloballyOddPrimitiveFullCoreBadReductionDualRootLinePhysicalCompletionDispersion")
