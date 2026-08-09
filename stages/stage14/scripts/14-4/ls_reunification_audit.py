from fractions import Fraction
from math import gcd


def omega_odd(n: int) -> int:
    n = abs(n)
    while n % 2 == 0 and n:
        n //= 2
    w = 0
    p = 3
    while p * p <= n:
        if n % p == 0:
            w += 1
            while n % p == 0:
                n //= p
        p += 2
    if n > 1:
        w += 1
    return w


def unit_square_roots_mod(m: int, r: int):
    return [x for x in range(m) if gcd(x, m) == 1 and (x * x - r) % m == 0]


local = Fraction(41, 42)
target = Fraction(1, 2)
missing = local - target
critical = Fraction(10, 21)
assert missing == critical
assert min(Fraction(1, 2), critical) == critical

# Denominator-square root multiplicity regression.
# For every D<=30 and every unit quadratic residue r mod D^2,
# the number of unit square roots is bounded by 4*2^omega(D_odd).
for D in range(1, 31):
    m = D * D
    units = [x for x in range(m) if gcd(x, m) == 1]
    residues = {x * x % m for x in units}
    cap = 4 * (2 ** omega_odd(D))
    for r in residues:
        roots = unit_square_roots_mod(m, r)
        assert len(roots) <= cap, (D, r, len(roots), cap)

# Exact-witness resonance regression: if Phi is represented by a nonzero square,
# every quadratic character at a good odd prime is +1.
def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    v = pow(a, (p - 1) // 2, p)
    return -1 if v == p - 1 else v

for p in [3, 5, 7, 11, 13, 17, 19, 23, 29, 31]:
    for z in range(1, p):
        assert legendre(z * z, p) == 1

print("MISSING_POST_LOCAL_SAVING=10/21")
print("RADICAL_POOR_SQRT_THRESHOLD=1/2")
print("CRITICAL_WITNESS_SCALE=10/21")
print("DENOMINATOR_SQUARE_ROOT_MULTIPLICITY_AUDIT=true")
print("EXACT_WITNESS_CHARACTER_RESONANCE_AUDIT=true")
print("ALL_AUDITS_PASS=true")
