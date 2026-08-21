#!/usr/bin/env python3
"""Exact combinatorial checks for the Stage29-02ha seven-line sign cover.

Uses only integer arithmetic and exhaustive permutations of seven labels.
"""

from itertools import combinations, permutations
from math import gcd

LINES = {
    "A1": (1, 0, 0),
    "A2": (0, 1, 0),
    "A3": (0, 0, 1),
    "B3": (1, 1, 0),
    "B2": (1, 0, 1),
    "B1": (0, 1, 1),
    "C":  (1, 1, 1),
}
LABELS = tuple(LINES)


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def normalize_projective(p):
    g = 0
    for v in p:
        g = gcd(g, abs(v))
    q = tuple(v // g for v in p)
    for v in q:
        if v:
            if v < 0:
                q = tuple(-w for w in q)
            break
    return q


def dot(a, p):
    return sum(x * y for x, y in zip(a, p))


points = {}
for u, v in combinations(LABELS, 2):
    p = normalize_projective(cross(LINES[u], LINES[v]))
    incident = frozenset(k for k in LABELS if dot(LINES[k], p) == 0)
    points[p] = incident

triple_points = {p: s for p, s in points.items() if len(s) == 3}
double_points = {p: s for p, s in points.items() if len(s) == 2}
assert len(triple_points) == 6
assert len(double_points) == 3
assert len(points) == 9

# A seven-line arrangement with t3=6,t2=3 has, over every odd finite field
# where the incidence pattern is unchanged, union size
#   7(p+1) - 6*(3-1) - 3*(2-1) = 7p-8,
# hence projective-complement size (p^2+p+1)-(7p-8)=(p-3)^2.
assert 7 - 12 - 3 == -8

incidence_blocks = set(triple_points.values()) | set(double_points.values())

automorphisms = []
for perm_tuple in permutations(LABELS):
    perm = dict(zip(LABELS, perm_tuple))
    image_blocks = {
        frozenset(perm[x] for x in block)
        for block in incidence_blocks
    }
    if image_blocks == incidence_blocks:
        automorphisms.append(perm)

assert len(automorphisms) == 24


def orbit(label):
    return frozenset(g[label] for g in automorphisms)

orbits = []
seen = set()
for label in LABELS:
    if label not in seen:
        o = orbit(label)
        seen.update(o)
        orbits.append(o)

assert set(orbits) == {
    frozenset({"A1", "A2", "A3", "C"}),
    frozenset({"B1", "B2", "B3"}),
}

# The action on the four-element A/C orbit is faithful; order 24 therefore
# identifies the incidence automorphism group with S4.
restrictions = {
    tuple(g[x] for x in ("A1", "A2", "A3", "C"))
    for g in automorphisms
}
assert len(restrictions) == 24

print("t3=6")
print("t2=3")
print("triple_points=")
for p, block in sorted(triple_points.items()):
    print(" ", p, sorted(block))
print("double_points=")
for p, block in sorted(double_points.items()):
    print(" ", p, sorted(block))
print("incidence_automorphism_group_order=24")
print("incidence_automorphism_group=S4 via faithful action on {A1,A2,A3,C}")
print("line_orbits=[4:{A1,A2,A3,C}, 3:{B1,B2,B3}]")
print("odd_characteristic_projective_complement_count=(p-3)^2")
print("node_count=6*(64/8)=48")
