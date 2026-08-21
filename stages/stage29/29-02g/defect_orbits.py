#!/usr/bin/env python3
"""Exact F2 check for the Stage29-02g torsion-defect orbit split."""

from itertools import product


def mm(a, b):
    return tuple(
        tuple(sum(a[i][k] * b[k][j] for k in range(2)) % 2 for j in range(2))
        for i in range(2)
    )


def det(a):
    return (a[0][0] * a[1][1] - a[0][1] * a[1][0]) % 2


def inv(a):
    # det=1 over F2
    return ((a[1][1] % 2, (-a[0][1]) % 2), ((-a[1][0]) % 2, a[0][0] % 2))


def conj(g, a):
    return mm(mm(g, a), inv(g))


mats = [
    ((a, b), (c, d))
    for a, b, c, d in product((0, 1), repeat=4)
    if (a + d) % 2 == 0
]
group = [
    ((a, b), (c, d))
    for a, b, c, d in product((0, 1), repeat=4)
    if det(((a, b), (c, d))) == 1
]

assert len(mats) == 8
assert len(group) == 6

seen = set()
orbits = []
for a in mats:
    if a in seen:
        continue
    orbit = {conj(g, a) for g in group}
    seen |= orbit
    orbits.append(orbit)

orbits.sort(key=lambda o: (len(o), sorted(o)))
sizes = sorted(len(o) for o in orbits)
assert sizes == [1, 1, 3, 3]

classes = []
for orbit in orbits:
    rep = sorted(orbit)[0]
    if rep == ((0, 0), (0, 0)):
        label = "zero"
    elif rep == ((1, 0), (0, 1)):
        label = "identity"
    elif det(rep) == 0:
        label = "nonzero_det0"
    else:
        label = "det1_nonidentity"
    classes.append((len(orbit), label, rep))

print("trace_zero_matrices=8")
print("SL2_F2_order=6")
for size, label, rep in classes:
    print(f"orbit size={size} type={label} representative={rep}")
print("orbit_sizes=1,1,3,3")
print("PASS")
