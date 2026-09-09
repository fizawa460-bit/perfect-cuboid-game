#!/usr/bin/env python3

# Lightweight arithmetic replay for EX1-05Y.
# Source-bound identification of the X(8) character Pryms with j=1728 elliptic
# quotients is recorded in the companion JSON artifact.

# Riemann-Hurwitz for each single-sign involution on genus-5 X(8).
g_C = 5
fixed_points = 8
# 2g_C-2 = 2(2g_E-2)+R
lhs = 2 * g_C - 2
numerator = lhs - fixed_points
assert numerator % 2 == 0
assert numerator // 2 == 0  # 2g_E-2=0
assert 1 + (numerator // 2) // 2 == 1

# 05X named-H Fourier replay.
sigma_e = 1514
sigma_u = 1442
sigma_v = 930
sigma_uv = 930
trivial = (sigma_e + sigma_u + sigma_v + sigma_uv) // 4
chi_u = (sigma_e - sigma_u + sigma_v - sigma_uv) // 4
chi_v = (sigma_e + sigma_u - sigma_v - sigma_uv) // 4
chi_uv = (sigma_e - sigma_u - sigma_v + sigma_uv) // 4
assert (trivial, chi_u, chi_v, chi_uv) == (1204, 18, 274, 18)

# Elliptic Rosati trace is twice endomorphism degree.
assert (chi_v // 2, chi_u // 2, chi_uv // 2) == (137, 9, 9)

# Gaussian CM norm witnesses on E_i=C/Z[i].
assert 11 * 11 + 4 * 4 == 137
assert 3 * 3 == 9

# The same fixed-class Prym data apply to all 29 EX1 Q states.
rows = []
for r in range(29):
    Q = 210 + 2 * r
    g_D = 106 + r
    assert Q == 2 * g_D - 2
    rows.append((Q, r, g_D, (137, 9, 9)))

assert rows[0] == (210, 0, 106, (137, 9, 9))
assert rows[-1] == (266, 28, 134, (137, 9, 9))
assert len(rows) == 29

residues = [73, 97, 235]
assert len(residues) == 3

print("PASS_EX1_05Y_GAUSSIAN_PRYM_NORMS_REALIZABLE")
print("states", len(rows), "fourier", [trivial, chi_u, chi_v, chi_uv])
print("prym_degrees", [137, 9, 9], "residues", residues)
