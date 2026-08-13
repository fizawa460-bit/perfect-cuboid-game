from pathlib import Path
from fractions import Fraction

ROOT = Path(__file__).resolve().parents[3]

paths = {
    "t131": ROOT / "stages/stage14/14-t131/result.md",
    "bsx31": ROOT / "stages/stage14/14-Work-bsX31/result.md",
    "t132": ROOT / "stages/stage14/14-t132/result.md",
}
for name, path in paths.items():
    assert path.exists(), (name, path)
texts = {name: path.read_text() for name, path in paths.items()}

assert "FIXED_U_ALL_LIVE_BRANCHES_SCALAR_NORM_OUTER_COORDINATE=true" in texts["t131"]
assert "COMMON_ONE_DIMENSIONAL_OUTER_RECIPROCAL_SELECTOR_LANGUAGE_PROVED=true" in texts["bsx31"]
assert "COMMON_PHYSICAL_WEIGHT_ADAPTER_PROVED=false" in texts["bsx31"]

for token in [
    "COFACTOR_PROJECTIVE_CLASS_NONNEGATIVE_DECOMPOSITION_EXACT=true",
    "FIXED_COFACTOR_CLASS_HAS_FIXED_INVERSE_PRIME_CLASS=true",
    "BAD_PACKET_LOCALIZES_TO_ONE_FIXED_PROJECTIVE_CLASS=true",
    "LOCALIZED_CLASS_PRINCIPAL_MASS=BoMinus1_TIMES_TOTAL",
    "LOCALIZED_CLASS_RETAINS_FIXED_POSITIVE_DEPLETION_POWER=true",
    "MOVING_SELECTED_CLASS_AS_MINIMAL_RECEIVER_SUPERSEDED=true",
    "REAL_NONREAL_COFACTOR_BRANCH_SPLIT_AS_MINIMAL_RECEIVER_SUPERSEDED=true",
    "FIXED_PROJECTIVE_CLASS_RECIPROCAL_PRIME_DEPLETION_RECEIVER_PROVED=true",
    "RECEIVER_MATERIALLY_CHANGED=true",
    "T_ROUTE_H_NEEDED=false",
    "NEXT=Stage14-t133",
]:
    assert token in texts["t132"], token

# Exact finite-group class decomposition in a toy model.
g = 5
# W_c(n) for three scalar norms and five projective classes.
W = [
    [2, 0, 1, 0, 1],
    [0, 1, 0, 2, 0],
    [1, 1, 0, 0, 1],
]
# total prime counts in the corresponding reciprocal intervals
P = [25, 15, 10]
# class occupancy K_n(q); every row partitions P_n
K = [
    [5, 4, 6, 5, 5],
    [3, 2, 4, 3, 3],
    [2, 2, 1, 3, 2],
]
assert all(sum(row) == p for row, p in zip(K, P))
# fixed a-class shift represented by q_c=(-c-a) mod g in additive notation
aclass = 2
T_c = []
M_c = []
for c in range(g):
    q = (-c - aclass) % g
    T_c.append(sum(W[n][c] * K[n][q] for n in range(len(W))))
    M_c.append(sum(Fraction(W[n][c] * P[n], g) for n in range(len(W))))
T = sum(T_c)
M = sum(M_c)
assert T == sum(
    W[n][c] * K[n][(-c-aclass) % g]
    for n in range(len(W)) for c in range(g)
)
assert M == sum(Fraction(sum(W[n]) * P[n], g) for n in range(len(W)))

# Localization lemma: if T <= eps M, low-ratio classes carry almost all M,
# and because there are g classes one low-ratio class has >= (1-sqrt(eps))M/g.
# Use a synthetic depleted family to test the inequality exactly.
Bpow_delta = Fraction(1, 100)   # B^{-delta}
Bpow_half = Fraction(1, 10)     # B^{-delta/2}
Ms = [Fraction(40), Fraction(25), Fraction(20), Fraction(10), Fraction(5)]
Ts = [Fraction(1, 10), Fraction(1, 20), Fraction(1, 20), Fraction(1, 100), Fraction(1, 100)]
Mtot = sum(Ms)
Ttot = sum(Ts)
assert Ttot <= Bpow_delta * Mtot
high = [i for i in range(g) if Ts[i] > Bpow_half * Ms[i]]
low = [i for i in range(g) if i not in high]
assert sum(Ms[i] for i in high) <= Bpow_half * Mtot
assert sum(Ms[i] for i in low) >= (1-Bpow_half) * Mtot
assert max(Ms[i] for i in low) >= (1-Bpow_half) * Mtot / g
assert any(Ts[i] <= Bpow_half * Ms[i] for i in low)

assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=1/2" in texts["t132"]
assert "STRICT_SUBSQRT_POWER_SAVING_PROVED=false" in texts["t132"]

print("Stage14-t-batch t132 audit: OK")
