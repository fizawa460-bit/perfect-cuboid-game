#!/usr/bin/env python3

# Lightweight arithmetic replay for EX1-05T.
# The deformation/virtual-class source locks live in the JSON artifact.

DIM_LINEAR = 7717
P_A = 8090

rows = []
for r in range(29):
    Q = 210 + 2*r
    g = 106 + r
    delta = P_A - g
    deg_M = -162 + 2*r
    chi_M = deg_M + 1 - g
    h0_M = 0
    h1_M = -chi_M
    expected = DIM_LINEAR - delta
    excess = delta - DIM_LINEAR

    assert delta == 7984 - r
    assert deg_M < 0
    assert chi_M == r - 267
    assert h1_M == 267 - r
    assert expected == r - 267
    assert excess == 267 - r
    assert h1_M == excess == -expected
    rows.append((Q, r, g, delta, deg_M, h1_M, expected, excess))

assert rows[0] == (210, 0, 106, 7984, -162, 267, -267, 267)
assert rows[-1] == (266, 28, 134, 7956, -106, 239, -239, 239)
assert min(x[5] for x in rows) == 239
assert max(x[5] for x in rows) == 267

# Same-target diagonal counterexample replay from 05N:
# N_Delta ~= T_C2 has deg -2 on genus-2 C2.
diag_deg_N = -2
diag_genus = 2
diag_chi = diag_deg_N + 1 - diag_genus
assert diag_chi == -3
assert diag_deg_N < 0
# Hence h0=0 and h1=3, yet the diagonal exists.
diag_h0 = 0
diag_h1 = -diag_chi
assert diag_h1 == 3

print("PASS_EX1_05T_OBSTRUCTION_SATURATION")
