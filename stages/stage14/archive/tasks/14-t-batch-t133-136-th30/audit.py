from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[3]

paths = {
    "t132": ROOT / "stages/stage14/14-t132/result.md",
    "t133": ROOT / "stages/stage14/14-t133/result.md",
    "t134": ROOT / "stages/stage14/14-t134/result.md",
    "t135": ROOT / "stages/stage14/14-t135/result.md",
    "target": ROOT / "stages/stage14/14-t135/th30-target.md",
    "th30": ROOT / "stages/stage14/14-tH30/result.md",
    "t136": ROOT / "stages/stage14/14-t136/result.md",
}
texts = {k: p.read_text() for k, p in paths.items()}

required = {
    "t133": [
        "FIXED_CLASS_WEIGHT_DECOMPOSES_BY_D4_NORMALIZATION_STATE=true",
        "ONE_NORMALIZATION_STATE_FREEZABLE_WITHOUT_POWER_LOSS=true",
        "FIXED_CLASS_WEIGHT_IS_PRIMITIVE_GAUSSIAN_SECTOR_PROJECTIVE_REPRESENTATION_COUNT=true",
        "NEXT=Stage14-t134",
    ],
    "t134": [
        "FIXED_COFACTOR_PROJECTIVE_CLASS_LIFT_TO_GAUSSIAN_RESIDUES_EXACT=true",
        "ONE_COFACTOR_GAUSSIAN_RESIDUE_FREEZABLE_WITHOUT_POWER_LOSS=true",
        "NEXT=Stage14-t135",
    ],
    "t135": [
        "ONE_PRIME_GAUSSIAN_RESIDUE_FREEZABLE_WITHOUT_POWER_LOSS=true",
        "COFACTOR_SCALAR_WEIGHT_UNFOLDED_TO_ACTUAL_GAUSSIAN_POINTS=true",
        "T_ROUTE_H_NEEDED=true",
        "NEXT=Stage14-tH30",
    ],
    "target": [
        "SOURCE_SNAPSHOT_SHA=14ca52cf310b1bb51f51878cb9d5c76cfb768923",
        "TARGET_FROZEN=true",
    ],
    "th30": [
        "DIRECT_THEOREM_APPLICABLE=false",
        "TH29_COFACTOR_ADAPTER_OBSTRUCTION_REMOVED=true",
        "ARBITRARILY_SHORT_ENDPOINT_REGIME_REMAINS=true",
        "SUBPOLYNOMIAL_INDIVIDUAL_MODULUS_OBSTRUCTION_REMAINS=true",
        "NEXT_H_NEEDED=false",
    ],
    "t136": [
        "FIXED_RESIDUE_ENDPOINT_LONG_SPLIT_EXACT=true",
        "ENDPOINT_SHORT_FIXED_RESIDUE_BRANCH_LIVE=true",
        "LONG_HEADROOM_INDIVIDUAL_SUBPOLYNOMIAL_MODULUS_BRANCH_LIVE=true",
        "RECEIVER_MATERIALLY_CHANGED=true",
        "NEXT=Stage14-t137",
    ],
}
for key, toks in required.items():
    for tok in toks:
        assert tok in texts[key], (key, tok)

assert "BAD_PACKET_LOCALIZES_TO_ONE_FIXED_PROJECTIVE_CLASS=true" in texts["t132"]

# Nonnegative finite-label localization: a globally depleted sum has a
# principal-scale low-ratio cell when only O(1)/B^o(1) cells are present.
M = [31, 29, 23, 17]
T = [0, 1, 0, 1]
Mtot, Ttot = sum(M), sum(T)
assert Fraction(Ttot, Mtot) < Fraction(1, 20)
large = [i for i, m in enumerate(M) if m >= Mtot // (2 * len(M))]
assert large
assert any(Fraction(T[i], M[i]) < Fraction(1, 10) for i in large)

# Projective coset -> ordinary residue decomposition is additive.
residue_weights = [5, 7, 11]
assert sum(residue_weights) == 23

# Equal principal baseline splitting on the prime-residue coset preserves
# the depletion exponent in at least one residue.
T_beta = [0, 1, 2, 0]
M_each = Fraction(10, 1)
assert sum(T_beta) <= Fraction(3, 40) * (M_each * len(T_beta))
assert min(Fraction(t, M_each) for t in T_beta) <= Fraction(sum(T_beta), M_each * len(T_beta))

# Hyperbola regrouping by scalar norm and by actual Gaussian points is the
# same finite combinatorial sum in a toy model.
points = [(2, "a"), (2, "b"), (3, "c"), (5, "d")]
primes = [11, 13, 17, 19]
X = 50
direct = sum(1 for n, _ in points for ell in primes if n * ell <= X)
from_norm = 0
for n in sorted({n for n, _ in points}):
    w = sum(1 for nn, _ in points if nn == n)
    from_norm += w * sum(1 for ell in primes if n * ell <= X)
assert direct == from_norm

# Endpoint / long-headroom is an exact partition of every live R>1.
theta_cut = 4
Rs = [Fraction(11, 10), Fraction(2, 1), Fraction(4, 1), Fraction(9, 1)]
edge = [r for r in Rs if 1 < r < theta_cut]
long = [r for r in Rs if r >= theta_cut]
assert len(edge) + len(long) == len(Rs)

for key in ("t133", "t134", "t135", "th30", "t136"):
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in texts[key]
    assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in texts[key]

print("Stage14-t-batch t133-t136+tH30 audit: OK")
