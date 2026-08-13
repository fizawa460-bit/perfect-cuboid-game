from pathlib import Path
from fractions import Fraction
from math import isqrt

ROOT = Path(__file__).resolve().parents[3]

files = {
    "t125": ROOT / "stages/stage14/14-t125/result.md",
    "t126": ROOT / "stages/stage14/14-t126/result.md",
    "t127": ROOT / "stages/stage14/14-t127/result.md",
    "target": ROOT / "stages/stage14/14-t127/th29-target.md",
    "th29": ROOT / "stages/stage14/14-tH29/result.md",
    "t128": ROOT / "stages/stage14/14-t128/result.md",
}

texts = {k: p.read_text() for k, p in files.items()}

required = {
    "t125": [
        "LIVE_PRIME_INTERVALS_NESTED=true",
        "GENERIC_ORIENTATION_SELECTED_CLASS_SUBSET_PRODUCT_EXACT=true",
        "r_p=[varpi_p]^(2*e_p)",
        "NEXT=Stage14-t126",
    ],
    "t126": [
        "SELECTED_CLASS_COUNT_HYPERBOLA_TRANSPOSITION_EXACT=true",
        "PRINCIPAL_BASELINE_TRANSPOSES_EXACTLY=true",
        "NEXT=Stage14-t127",
    ],
    "t127": [
        "PROJECTIVE_HYPERBOLA_FINITE_FOURIER_EXPANSION_EXACT=true",
        "T_ROUTE_H_NEEDED=true",
        "NEXT=Stage14-tH29",
    ],
    "target": [
        "SOURCE_SNAPSHOT_SHA=38ac82435315979d3d0493090d153b4b36163be1",
        "TARGET_FROZEN=true",
    ],
    "th29": [
        "DIRECT_THEOREM_APPLICABLE=false",
        "ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true",
        "REAL_EXCEPTIONAL_CHARACTER_UNIFORMLY_EXCLUDED=false",
        "NEXT_H_NEEDED=false",
    ],
    "t128": [
        "PROJECTIVE_DEPLETION_HEADROOM_SPLIT_EXACT=true",
        "PROJECTIVE_CHARACTERS_REAL_NONREAL_SPLIT_EXACT=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "NEXT=Stage14-t129",
    ],
}

for key, tokens in required.items():
    for token in tokens:
        assert token in texts[key], (key, token)

# t125: every nonempty original interval has common lower endpoint 2*sqrt(B).
B = 10**8
sB = isqrt(B)
hk0 = 3
for n in range(1, 10000):
    lower = max(2 * sB, 2 * hk0 * n)
    upper = Fraction(2 * B, hk0 * n)
    if Fraction(lower, 1) < upper:
        assert hk0 * n < sB
        assert lower == 2 * sB

# t125 orientation inversion: in a cyclic test group written by exponents,
# gamma orientation flip changes +e -> -e, hence gamma changes by -2e;
# selected class c=gamma^{-1} therefore changes by +2e.
order = 17
e = 3
gamma_base = e % order
gamma_flip = (-e) % order
c_base = (-gamma_base) % order
c_flip = (-gamma_flip) % order
assert (gamma_flip - gamma_base) % order == (-2 * e) % order
assert (c_flip - c_base) % order == (2 * e) % order

# t126: direct class-matched count equals hyperbola transposition.
g = 3
X = 100
L = 10
cofactors = [(2, 0), (3, 1), (5, 0)]
primes = [(11, 0), (13, 1), (17, 0), (19, 2), (23, 1), (29, 0), (31, 2), (37, 0)]

def eligible_primes(n):
    return [(ell, c) for ell, c in primes if ell > L and n * ell <= X]

direct_T = sum(1 for n, c in cofactors for ell, pc in eligible_primes(n) if pc == c)
transposed_T = sum(
    1
    for ell, pc in primes
    if ell > L
    for n, c in cofactors
    if n * ell <= X and c == pc
)
assert direct_T == transposed_T

direct_M = sum(Fraction(len(eligible_primes(n)), g) for n, _ in cofactors)
transposed_M = sum(
    Fraction(sum(1 for n, _ in cofactors if n * ell <= X), g)
    for ell, _ in primes
    if ell > L
)
assert direct_M == transposed_M

# Centered class-count form equals T-M.
centered = Fraction(0, 1)
for ell, pc in primes:
    if ell <= L:
        continue
    cutoff_count = sum(1 for n, _ in cofactors if n * ell <= X)
    class_count = sum(1 for n, c in cofactors if n * ell <= X and c == pc)
    centered += Fraction(class_count, 1) - Fraction(cutoff_count, g)
assert Fraction(direct_T, 1) - direct_M == centered

# t128: a depleted total localizes to at least one depleted nonzero headroom branch.
M_edge, T_edge = 20, 1
M_long, T_long = 80, 7
threshold = Fraction(1, 10)
assert Fraction(T_edge + T_long, M_edge + M_long) <= threshold
assert min(Fraction(T_edge, M_edge), Fraction(T_long, M_long)) <= threshold

# Character pigeonhole: if g-1 contributions sum to principal scale,
# one individual contribution has at least the average absolute scale.
char_g = 5
D_terms = [-100, -90, -80, -80]
assert len(D_terms) == char_g - 1
assert abs(sum(D_terms)) >= 300
assert max(abs(x) for x in D_terms) >= Fraction(abs(sum(D_terms)), char_g - 1)

for text in (texts["t125"], texts["t126"], texts["t127"], texts["th29"], texts["t128"]):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in text
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in text

print("Stage14-t-batch t125-t128+tH29 audit: OK")
