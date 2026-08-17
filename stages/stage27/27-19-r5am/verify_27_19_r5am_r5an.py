from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]


def sf(n: int) -> int:
    out = 1
    d = 2
    while d * d <= n:
        odd = False
        while n % d == 0:
            n //= d
            odd = not odd
        if odd:
            out *= d
        d += 1
    if n > 1:
        out *= n
    return out


def square(n: int) -> bool:
    if n < 0:
        return False
    z = math.isqrt(n)
    return z * z == n


# r5al L=1 completion remains exact.
def unique_completion(a, b, delta, c0, cs, cn, mu, nu, sigma):
    q1 = a * cs * cs * sigma * sigma + b * cn * cn * nu * nu
    kappa = sf(q1)
    c2 = q1 // kappa
    c = math.isqrt(c2)
    if c * c != c2 or c % c0:
        return None
    cp = c // c0
    q2 = b * c0 * c0 * mu * mu + a * delta * delta * sigma * sigma
    den = kappa * cn * cn
    if q2 % den:
        return None
    w2 = q2 // den
    wp = math.isqrt(w2)
    if wp * wp != w2:
        return None
    num = kappa * cs * cs * wp * wp + b * delta * delta * nu * nu
    den3 = a * c0 * c0
    if num % den3:
        return None
    rho2 = num // den3
    rho = math.isqrt(rho2)
    if rho * rho != rho2:
        return None
    return kappa, cp, wp, rho


assert unique_completion(17, 13, 2, 3, 7, 1, 1, 8, 1) == (185, 1, 1, 9)

# Exhaustive primitive-slope regression for the exact kappa divisibilities and
# the norm-form transformation used by r5am.
space_checked = 0
pell_checked = 0
for m in range(2, 32):
    for n in range(1, m):
        if math.gcd(m, n) != 1:
            continue
        for r in range(2, 32):
            for s in range(1, r):
                if math.gcd(r, s) != 1:
                    continue
                delta = math.gcd(n, s)
                n0, s0 = n // delta, s // delta
                c0 = math.gcd(m, r)
                cs = math.gcd(m, s0)
                cn = math.gcd(r, n0)
                assert math.gcd(c0, cs) == 1
                assert math.gcd(c0, cn) == 1
                assert math.gcd(cs, cn) == 1
                assert m % (c0 * cs) == 0
                assert r % (c0 * cn) == 0
                assert s0 % cs == 0
                assert n0 % cn == 0
                mu = m // (c0 * cs)
                rho = r // (c0 * cn)
                sigma = s0 // cs
                nu = n0 // cn

                M = m * m + n * n
                K = r * r - s * s
                h = math.gcd(M, K)
                a, b = M // h, K // h
                p, q = a * s0 * s0, b * n0 * n0
                assert math.gcd(p, q) == 1
                J = a * b * h + delta * delta * (p - q)
                if not square(J * (p + q)):
                    continue

                kappa = sf(p + q)
                assert sf(J) == kappa
                assert (m * m - n * n) % kappa == 0
                assert (r * r + s * s) % kappa == 0
                assert math.gcd(kappa, m * n * r * s) == 1
                for ell in range(2, int(math.isqrt(kappa)) + 2):
                    if kappa % ell == 0 and all(ell % d for d in range(2, int(math.isqrt(ell)) + 1)):
                        assert ell % 4 == 1
                space_checked += 1

                c2 = (p + q) // kappa
                w2 = J // kappa
                assert square(c2) and square(w2)
                c, w = math.isqrt(c2), math.isqrt(w2)
                assert c % c0 == 0
                assert w % (cs * cn) == 0
                cp = c // c0
                wp = w // (cs * cn)
                q1 = a * cs**2 * sigma**2 + b * cn**2 * nu**2
                q2 = b * c0**2 * mu**2 + a * delta**2 * sigma**2
                q3 = a * c0**2 * rho**2 - b * delta**2 * nu**2
                assert q1 == kappa * c0**2 * cp**2
                assert q2 == kappa * cn**2 * wp**2
                assert q3 == kappa * cs**2 * wp**2

                X = cn * wp
                Y = c0 * mu
                assert kappa * X * X - b * Y * Y == a * delta * delta * sigma * sigma
                assert (kappa * X) ** 2 - kappa * b * Y * Y == kappa * a * delta * delta * sigma * sigma
                pell_checked += 1

assert space_checked > 1000, space_checked
assert pell_checked == space_checked

# Explicit exactly-two Stage19 survivor with kappa=1 closes any unconditional
# growing-kappa shortcut.
m, n, r, s = 7, 4, 5, 3
delta = math.gcd(n, s)
n0, s0 = n // delta, s // delta
M, K = m*m+n*n, r*r-s*s
h = math.gcd(M, K)
a, b = M // h, K // h
p, q = a*s0*s0, b*n0*n0
J = a*b*h + delta*delta*(p-q)
assert sf(p+q) == sf(J) == 1
E = 4*m*n*r*s
XX = 2*r*s*(m*m-n*n)
YY = 2*m*n*(r*r-s*s)
Gamma = math.gcd(E, math.gcd(XX, YY))
e, x, y = E//Gamma, XX//Gamma, YY//Gamma
R2 = e*e+x*x+y*y
assert square(R2) and math.isqrt(R2) == 1073
assert not square(x*x+y*y)

contract = json.loads((ROOT / "stages/stage27/27-19-r5am/route-contract.json").read_text())
assert contract["task_id"] == "Stage27-19-r5am"
assert contract["status"] == "BATCH_SUBMITTED_PENDING_FRESH_AUDIT"
assert contract["proved"]["uniform_pell_count_lemma"] is True
assert contract["proved"]["kappa_paired_slope_residue_receiver"] is True
assert contract["not_proved"]["strict_sub_sqrt_upper"] is True

r5am = (ROOT / "stages/stage27/27-19-r5am/result.md").read_text()
r5an = (ROOT / "stages/stage27/27-19-r5an/result.md").read_text()
for marker in [
    "UNIFORM_PELL_COUNT_LEMMA_PROVED=true",
    "R5AL_NINE_VARIABLE_UNIQUENESS_STRENGTHENED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in r5am
for marker in [
    "KAPPA_DIVIDES_M2_MINUS_N2_PROVED=true",
    "KAPPA_DIVIDES_R2_PLUS_S2_PROVED=true",
    "KAPPA_COPRIME_TO_MNRS_PROVED=true",
    "KAPPA_EQ_1_STAGE19_WITNESS_RETAINED=true",
    "STRICT_SUB_SQRT_UPPER_PROVED=false",
]:
    assert marker in r5an

print(f"Stage27-19-r5am-r5an verification PASS; space squareclass tuples checked={space_checked}")
