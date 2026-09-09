#!/usr/bin/env python3
"""Independent H-lane check of the retained fresh-runtime 48-point dump.

This deliberately does not treat a fresh Magma index as the historical retained
exceptional index.  It verifies only the exact projective point set and its
mapping to the independently reconstructed A-lane six-family source catalog.
"""

I = 1j

RUNTIME = [
    (0,0,1,1,1,0,-1),(0,0,1,1,-1,0,-1),(0,0,1,-1,1,0,-1),(0,0,1,-1,-1,0,-1),
    (0,0,1,-1,-1,0,1),(0,0,1,-1,1,0,1),(0,0,1,1,-1,0,1),(0,0,1,1,1,0,1),
    (0,1,0,1,0,1,-1),(0,1,0,1,0,-1,-1),(0,1,0,-1,0,1,-1),(0,1,0,-1,0,-1,-1),
    (0,1,0,-1,0,-1,1),(0,1,0,-1,0,1,1),(0,1,0,1,0,-1,1),(0,1,0,1,0,1,1),
    (1,0,0,0,1,1,-1),(1,0,0,0,1,-1,-1),(1,0,0,0,-1,1,-1),(1,0,0,0,-1,-1,-1),
    (1,0,0,0,-1,-1,1),(1,0,0,0,-1,1,1),(1,0,0,0,1,-1,1),(1,0,0,0,1,1,1),
    (0,1,I,0,I,-1,0),(0,1,I,0,-I,-1,0),(0,1,-I,0,I,-1,0),(0,1,-I,0,-I,-1,0),
    (0,1,-I,0,-I,1,0),(0,1,-I,0,I,1,0),(0,1,I,0,-I,1,0),(0,1,I,0,I,1,0),
    (1,0,I,I,0,-1,0),(1,0,I,-I,0,-1,0),(1,0,-I,I,0,-1,0),(1,0,-I,-I,0,-1,0),
    (1,0,-I,-I,0,1,0),(1,0,-I,I,0,1,0),(1,0,I,-I,0,1,0),(1,0,I,I,0,1,0),
    (1,I,0,I,-1,0,0),(1,I,0,-I,-1,0,0),(1,-I,0,I,-1,0,0),(1,-I,0,-I,-1,0,0),
    (1,-I,0,-I,1,0,0),(1,-I,0,I,1,0,0),(1,I,0,-I,1,0,0),(1,I,0,I,1,0,0),
]


def source_catalog():
    out = {}
    for a in (-1, 1):
        for b in (-1, 1):
            for c in (-1, 1):
                out[(1,0,0,0,a,b,c)] = f"AXIS_X1:a={a},b={b},c={c}"
                out[(0,1,0,a,0,b,c)] = f"AXIS_X2:a={a},b={b},c={c}"
                out[(0,0,1,a,b,0,c)] = f"AXIS_X3:a={a},b={b},c={c}"
    for s in (-1, 1):
        for a in (-1, 1):
            for b in (-1, 1):
                out[(0,1,s*I,0,a*I,b,0)] = f"Y1_Z_ZERO:s={s},a={a},b={b}"
                out[(1,0,s*I,a*I,0,b,0)] = f"Y2_Z_ZERO:s={s},a={a},b={b}"
                out[(1,s*I,0,a*I,b,0,0)] = f"Y3_Z_ZERO:s={s},a={a},b={b}"
    return out


def surface_ok(v):
    a1,a2,a3,b1,b2,b3,c = v
    return (
        a1*a1 + a2*a2 - b3*b3 == 0
        and a2*a2 + a3*a3 - b1*b1 == 0
        and a1*a1 + a3*a3 - b2*b2 == 0
        and a1*a1 + a2*a2 + a3*a3 - c*c == 0
    )


CAT = source_catalog()
assert len(RUNTIME) == 48
assert len(set(RUNTIME)) == 48
assert len(CAT) == 48
assert all(surface_ok(v) for v in RUNTIME)
assert set(RUNTIME) == set(CAT)
assert all(next(x for x in v if x != 0) == 1 for v in RUNTIME)

labels = [CAT[v] for v in RUNTIME]
assert labels[0].startswith("AXIS_X3:") and labels[7].startswith("AXIS_X3:")
assert labels[8].startswith("AXIS_X2:") and labels[15].startswith("AXIS_X2:")
assert labels[16].startswith("AXIS_X1:") and labels[23].startswith("AXIS_X1:")
assert labels[24].startswith("Y1_Z_ZERO:") and labels[31].startswith("Y1_Z_ZERO:")
assert labels[32].startswith("Y2_Z_ZERO:") and labels[39].startswith("Y2_Z_ZERO:")
assert labels[40].startswith("Y3_Z_ZERO:") and labels[47].startswith("Y3_Z_ZERO:")

# The observed runtime order is not the A-lane deterministic family order.
assert labels[0] != "AXIS_X1:a=-1,b=-1,c=-1"

print("STAGE32EX5_H_RESULT_OK")
print("FRESH_RUNTIME_POINTS=48")
print("SOURCE_CANONICAL_POINTS=48")
print("COLLISIONS=0")
print("OMISSIONS=0")
print("HISTORICAL_RUNTIME_TO_RETAINED_PERMUTATION_PERSISTED=false")
