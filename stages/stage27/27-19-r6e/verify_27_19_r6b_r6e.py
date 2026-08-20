import math


def tau(n: int) -> int:
    out = 1
    d = 2
    while d * d <= n:
        if n % d == 0:
            a = 0
            while n % d == 0:
                n //= d
                a += 1
            out *= a + 1
        d += 1
    if n > 1:
        out *= 2
    return out


def factor(n: int):
    fs = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            fs.append(d)
            n //= d
        d += 1
    if n > 1:
        fs.append(n)
    return fs


def toric_check(m, n, r, s):
    E = 4 * m * n * r * s
    X = 2 * r * s * (m * m - n * n)
    Y = 2 * m * n * (r * r - s * s)
    G = math.gcd(E, math.gcd(X, Y))
    e, x, y = E // G, X // G, Y // G
    Dx_num = 2 * r * s * (m * m + n * n)
    Dy_num = 2 * m * n * (r * r + s * s)
    assert Dx_num % G == 0 and Dy_num % G == 0
    Dx, Dy = Dx_num // G, Dy_num // G
    A0 = m * m * r * r + n * n * s * s
    B0 = m * m * s * s + n * n * r * r
    P = Dx * Dy - x * y
    Q = Dx * Dy + x * y
    # Avoid rational-factor arithmetic: cross-multiply the exact identities.
    assert P * G * G == 2 * E * B0
    assert Q * G * G == 2 * E * A0
    # Valuation parity differences therefore agree prime-by-prime.
    for ell in set(factor(P) + factor(Q) + factor(A0) + factor(B0)):
        def vp(z):
            a = 0
            while z % ell == 0:
                z //= ell
                a += 1
            return a
        assert (vp(P) - vp(Q) - vp(B0) + vp(A0)) == 0
    return e, x, y


def count_fixed_core(p, q, g):
    N = p * g
    total = 0
    for s in range(1, math.isqrt(N) + 1):
        if N % (s * s):
            continue
        M = N // (s * s)
        for m in range(1, math.isqrt(M) + 1):
            n2 = M - m * m
            if n2 <= 0:
                continue
            n = math.isqrt(n2)
            if n * n != n2:
                continue
            if (q * g) % (n * n):
                continue
            r2 = s * s + (q * g) // (n * n)
            r = math.isqrt(r2)
            if r * r == r2:
                total += 1
    return total


for t in [(2, 1, 3, 1), (3, 2, 5, 2), (5, 2, 7, 3), (8, 3, 14, 5), (21, 16, 27, 14)]:
    toric_check(*t)

# Known occupied-R witnesses obey the primitive split-prime support theorem.
for R in (1073, 7585, 13325, 14365):
    assert R % 2 == 1
    assert all(p % 4 == 1 for p in factor(R))

# Exhaustive small fixed-core checks against the proved divisor bound.
for p in range(1, 10):
    for q in range(1, 10):
        if math.gcd(p, q) != 1:
            continue
        for g in range(1, 40):
            c = count_fixed_core(p, q, g)
            assert c <= 4 * tau(p * g) ** 2

print("Stage27-19-r6b-r6e verifier: PASS")
