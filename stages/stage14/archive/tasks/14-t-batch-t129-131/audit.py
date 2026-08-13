from pathlib import Path
from fractions import Fraction
from math import isqrt, pi, cos, sin

ROOT = Path(__file__).resolve().parents[3]
files = {
    "t128": ROOT / "stages/stage14/14-t128/result.md",
    "brx30": ROOT / "stages/stage14/14-Work-brX30/result.md",
    "t129": ROOT / "stages/stage14/14-t129/result.md",
    "t130": ROOT / "stages/stage14/14-t130/result.md",
    "t131": ROOT / "stages/stage14/14-t131/result.md",
}
texts = {k: p.read_text() for k, p in files.items()}

assert "NEXT=Stage14-t129" in texts["t128"]
assert "NEXT_REVISIT_CONDITION=4fj+s7-92+t131" in texts["brx30"]

required = {
    "t129": [
        "ENDPOINT_HEADROOM_LAYER_TRANSPOSED_EXACTLY=true",
        "ENDPOINT_LOG_WEDGE_EXACT=true",
        "ENDPOINT_LOG_WEDGE_REGION=0<u<=v<theta",
        "ENDPOINT_GEOMETRY_ALONE_FIXED_POWER_SAVING=false",
        "NEXT=Stage14-t130",
    ],
    "t130": [
        "REAL_PROJECTIVE_CHARACTER_CONJUGATION_INVARIANT=true",
        "REAL_PROJECTIVE_CHARACTER_GENERIC_ORIENTATION_BLIND=true",
        "REAL_PROJECTIVE_CHARACTER_SCALAR_NORM_PHASE_DEFINED=true",
        "REAL_BRANCH_GAUSSIAN_ORIENTATION_CORRELATION_REMAINS=false",
        "NEXT=Stage14-t131",
    ],
    "t131": [
        "NONREAL_COFACTOR_NORM_FIBER_COEFFICIENT_DEFINED=true",
        "NONREAL_HYPERBOLA_SCALAR_NORM_COMPRESSION_EXACT=true",
        "NONREAL_ORIENTATION_DEPENDENCE_SURVIVES=true",
        "FIXED_U_ALL_LIVE_BRANCHES_SCALAR_NORM_OUTER_COORDINATE=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "NEXT=Stage14-t132",
    ],
}
for key, tokens in required.items():
    for token in tokens:
        assert token in texts[key], (key, token)

# t129 endpoint wedge: edge n plus hyperbola forces the global endpoint prime band.
B = 10**8
sqrtB = isqrt(B)
hk0 = 2
LB = 2 * sqrtB
NUmax = Fraction(sqrtB, hk0)
XU = LB * NUmax
Btheta = 10  # theta=1/8 for B=10^8
for n in range(501, 5000, 137):
    R = NUmax / n
    if not (1 < R < Btheta):
        continue
    for ell in range(LB + 1, LB * Btheta + 1000, 997):
        if n * ell <= XU:
            assert ell < LB * Btheta
            # u<=v is equivalent to ell/LB <= NUmax/n.
            assert Fraction(ell, LB) <= R

# t130: an order-two character is invariant under inversion, while a nonreal
# character need not be. Model a cyclic projective group C_8 by exponent k.
def chi_real(k):
    return 1 if k % 2 == 0 else -1

for k in range(8):
    assert chi_real((-k) % 8) == chi_real(k)

# A nonreal order-8 character distinguishes k and -k for generic k.
def chi_nonreal(k):
    a = 2 * pi * (k % 8) / 8
    return complex(cos(a), sin(a))

assert abs(chi_nonreal(1) - chi_nonreal(-1)) > 1e-9

# Real-character orientation blindness on a toy norm with two split primes.
# Choosing exponent sign +/-e does not change chi_real.
for e1 in (1, 2, 3):
    for e2 in (1, 2):
        vals = set()
        for s1 in (-1, 1):
            for s2 in (-1, 1):
                vals.add(chi_real(s1 * e1) * chi_real(s2 * e2))
        assert len(vals) == 1

# t131 regrouping by scalar norm is exact on a synthetic hyperbola.
X = 100
L = 10
# (norm n, projective exponent k) for physical cofactors
cofactors = [(2, 1), (2, 3), (4, 2), (5, 1), (5, 6)]
# (prime ell, projective exponent k)
primes = [(11, 1), (13, 2), (17, 3), (19, 5), (23, 7), (29, 1), (31, 4), (37, 6)]

def root8(k):
    return chi_nonreal(k)

direct = 0j
for n, kg in cofactors:
    for ell, kp in primes:
        if ell > L and n * ell <= X:
            direct += root8(kg) * root8(kp)

A = {}
for n, kg in cofactors:
    A[n] = A.get(n, 0j) + root8(kg)
compressed = 0j
for n, coeff in A.items():
    P = sum(root8(kp) for ell, kp in primes if ell > L and n * ell <= X)
    compressed += coeff * P
assert abs(direct - compressed) < 1e-9

for text in (texts["t129"], texts["t130"], texts["t131"]):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in text
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in text
    assert "T_ROUTE_H_NEEDED=false" in text

print("Stage14-t-batch t129-t131 audit: OK")
