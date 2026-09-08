#!/usr/bin/env python3

# Lightweight arithmetic replay for EX1-05R.
# The deformation-theoretic theorem source-lock is recorded in the JSON artifact;
# this verifier replays only the exact numerical consequences used by the leaf.

P_A = 8090
L2 = 15806
KDOTL = 372
H0_L = 7718
Q_SURFACE = 4
DIM_LINEAR = H0_L - 1
DIM_CURVES = H0_L - 1 + Q_SURFACE

assert DIM_LINEAR == 7717
assert DIM_CURVES == 7721
assert 1 + (L2 + KDOTL)//2 == P_A

rows = []
for r in range(29):
    Q = 210 + 2*r
    g = 106 + r
    delta = P_A - g
    deg_adj_tangent = (2*g - 2) - KDOTL
    assert delta == 7984 - r
    assert deg_adj_tangent == -162 + 2*r
    assert deg_adj_tangent < 0
    # A line bundle of strictly negative degree on a smooth projective curve
    # has no nonzero global sections. Dedieu-Sernesi then bounds the reduced
    # equigeneric tangent cone by zero.
    h0_adj_tangent = 0
    assert h0_adj_tangent == 0
    fixed_excess = delta - DIM_LINEAR
    full_excess = delta - DIM_CURVES
    assert fixed_excess == 267 - r
    assert full_excess == 263 - r
    rows.append((Q, r, g, delta, deg_adj_tangent, fixed_excess, full_excess))

assert rows[0] == (210, 0, 106, 7984, -162, 267, 263)
assert rows[-1] == (266, 28, 134, 7956, -106, 239, 235)
assert min(x[4] for x in rows) == -162
assert max(x[4] for x in rows) == -106
assert min(x[5] for x in rows) == 239
assert max(x[5] for x in rows) == 267
assert min(x[6] for x in rows) == 235
assert max(x[6] for x in rows) == 263

print("PASS_EX1_05R_EQUIDEFECT_ISOLATION")
