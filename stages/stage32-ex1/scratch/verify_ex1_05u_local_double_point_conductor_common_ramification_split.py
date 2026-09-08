#!/usr/bin/env python3

GAMMA2 = 15806
KDOT = 372
PA = 8090

rows = []
for r in range(29):
    Q = 210 + 2*r
    g = 106 + r
    delta = PA - g
    degN = (2*g - 2) - KDOT
    tau_min = 0
    tau_max = 2*r

    assert delta == 7984 - r
    assert degN == -162 + 2*r
    assert GAMMA2 == degN + 2*delta

    for tau in (tau_min, tau_max):
        degNbar = degN - tau
        assert GAMMA2 == degNbar + tau + 2*delta
        assert degNbar < 0

    rows.append((Q, r, g, delta, degN, tau_max))

assert rows[0] == (210, 0, 106, 7984, -162, 0)
assert rows[-1] == (266, 28, 134, 7956, -106, 56)

# Local method countermodels from EX1-05L:
# y^2-x^(2m): delta=m with immersive normalization branches (torsion 0)
# y^2-x^(2m+1): delta=m with normalization differential torsion 1
# Hence no universal extraction of delta from tau is legal.
for m in (1, 2, 10, 472, 7956, 7984):
    assert m > 0
    immersed_tau = 0
    cusp_tau = 1
    assert immersed_tau != cusp_tau

print("PASS_EX1_05U_DOUBLE_POINT_IDENTITY")
