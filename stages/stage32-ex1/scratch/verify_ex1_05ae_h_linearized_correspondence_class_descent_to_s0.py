#!/usr/bin/env python3

# Exact finite replay for EX1-05AE.
# This verifier checks the numerical consequences of the assembled 05AD
# H-equivariant endomorphism and the degree-4 diagonal-H quotient scaling.
# It intentionally does NOT claim primitive integral descent in NS(S0).

from itertools import product

D1 = 105
D2 = 81
G_C = 5
H_ORDER = 4
TWO_D1_D2 = 2 * D1 * D2

# Character traces from 05AD / 05X in order 1, chi_u, chi_v, chi_uv.
CHAR = [1204, 18, 274, 18]

# Hadamard character table for H=(Z/2)^2, deck order 1,u,v,uv.
HAD = [
    [1, 1, 1, 1],
    [1, 1,-1,-1],
    [1,-1, 1,-1],
    [1,-1,-1, 1],
]

DECK = [sum(HAD[i][j] * CHAR[j] for j in range(4)) for i in range(4)]
assert DECK == [1514, 1442, 930, 930]

# Upstairs correspondence class alpha_F on X(8)xX(8).
alpha2 = TWO_D1_D2 - DECK[0]
K_alpha = (2 * G_C - 2) * (D1 + D2)
pa_alpha = 1 + (alpha2 + K_alpha) // 2

assert TWO_D1_D2 == 17010
assert alpha2 == 15496
assert K_alpha == 1488
assert pa_alpha == 8493

# If alpha_F descends primitively through the degree-4 etale quotient,
# intersection and adjunction data scale by 4 exactly.
assert alpha2 % H_ORDER == 0
assert K_alpha % H_ORDER == 0
beta2 = alpha2 // H_ORDER
K_beta = K_alpha // H_ORDER
pa_beta = 1 + (beta2 + K_beta) // 2
assert beta2 == 3874
assert K_beta == 372
assert pa_beta == 2124

# Residual deck intersection package.
downstairs_cross = []
for tr in DECK:
    numerator = TWO_D1_D2 - tr
    assert numerator % H_ORDER == 0
    downstairs_cross.append(numerator // H_ORDER)
assert downstairs_cross == [3874, 3892, 4020, 4020]

# Normalization-defect scaling for all r=0..28.
for r in range(29):
    g0 = 106 + r
    delta0 = 2018 - r
    g_up = H_ORDER * (g0 - 1) + 1
    delta_up = pa_alpha - g_up
    assert g_up == 421 + 4 * r
    assert delta_up == 8072 - 4 * r
    assert delta_up == H_ORDER * delta0

# Transfer identity at the level of an H-invariant additive class is formal:
# p^* p_* alpha = sum_h h^* alpha = 4 alpha.
# Replay it on a generic coordinate vector to make clear that this only proves
# 4*alpha is in the pullback image, not alpha itself.
alpha = (D1, D2, 7, -3, 11)
translates = [alpha for _ in range(H_ORDER)]
transfer = tuple(sum(v[i] for v in translates) for i in range(len(alpha)))
assert transfer == tuple(H_ORDER * x for x in alpha)

# Denominator possibilities not excluded by transfer alone.
possible_saturation_orders = [1, 2, 4]
assert all(H_ORDER % d == 0 for d in possible_saturation_orders)

Q_STATES = list(range(210, 267, 2))
RES3 = [73, 97, 235]
assert len(Q_STATES) == 29
assert len(RES3) == 3

print("PASS_EX1_05AE_RATIONAL_DESCENT_NUMERICS_EXACT_INTEGRAL_SATURATION_OPEN")
print("upstairs", {"square": alpha2, "Kdot": K_alpha, "pa": pa_alpha})
print("downstairs_numeric", {"square": beta2, "Kdot": K_beta, "pa": pa_beta})
print("deck_intersections", downstairs_cross)
print("saturation_orders_still_possible", possible_saturation_orders)
print("Q_states", len(Q_STATES), "residues", RES3, "excluded", 0)
