#!/usr/bin/env python3

# Lightweight arithmetic replay for EX1-05X.
# It verifies the deck-intersection pullback scaling, Rosati cross traces,
# H-character Fourier split, and statewise genus/character dimensions.

D1 = 105
D2 = 81
BASELINE = 2 * D1 * D2
assert BASELINE == 17010

# Order: e,u,v,uv on S0.
a_s0 = [3874, 3892, 4020, 4020]
a_zxz = [4 * x for x in a_s0]
assert a_zxz == [15496, 15568, 16080, 16080]

sigma = [BASELINE - x for x in a_zxz]
assert sigma == [1514, 1442, 930, 930]

# Character signs in the same order. Labeling of the three nontrivial
# characters is intentionally arbitrary; only the multiset is retained.
chars = [
    [1, 1, 1, 1],
    [1, 1, -1, -1],
    [1, -1, 1, -1],
    [1, -1, -1, 1],
]
traces = [sum(c * s for c, s in zip(chi, sigma)) // 4 for chi in chars]
assert traces == [1204, 274, 18, 18]
assert sum(traces) == sigma[0] == 1514
assert sorted(traces[1:]) == [18, 18, 274]

# Each nontrivial H-character canonical piece of the genus-5 etale V4 cover
# has holomorphic dimension one, hence gives an elliptic Prym factor. On H1,
# Rosati trace of alpha^dagger alpha is twice deg(alpha).
prym_degrees = [x // 2 for x in traces[1:]]
assert prym_degrees == [137, 9, 9]
assert all(2 * d == t for d, t in zip(prym_degrees, traces[1:]))

rows = []
for r in range(29):
    Q = 210 + 2 * r
    gD = 106 + r
    gDt = 4 * (gD - 1) + 1
    inv_holo = gD
    nontriv_holo = gD - 1
    assert gDt == 421 + 4 * r
    assert inv_holo + 3 * nontriv_holo == gDt
    rows.append((Q, r, gD, gDt, inv_holo, nontriv_holo))

assert rows[0] == (210, 0, 106, 421, 106, 105)
assert rows[-1] == (266, 28, 134, 533, 134, 133)
assert len(rows) == 29

print("PASS_EX1_05X_CHARACTER_PRYM_FOURIER_SPLIT")
print("cross_rosati", sigma)
print("character_traces", traces, "prym_degrees", prym_degrees)
print("states", len(rows), "gDtilde_range", (rows[0][3], rows[-1][3]))
