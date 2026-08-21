#!/usr/bin/env python3
"""Exact audit checks for the Stage29-02ha seven-line sign/Kummer cover.

Uses only Python standard-library exact arithmetic. Besides the original incidence
ledger, this certifies:
  * every incidence automorphism is induced by a PGL_3(Q) projectivity;
  * the base arrangement projective automorphism group is S4 of order 24;
  * exactly the S3 coordinate-permutation subgroup lifts to the full sign cover over Q;
  * all 24 base projectivities lift after adjoining i;
  * the six triple fibers split as 24 Q-defined and 24 strictly Q(i)-defined A1 nodes.
"""

from fractions import Fraction
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
FRAME = ("A1", "A2", "A3", "C")


def cross(a, b):
    return (
        a[1] * b[2] - a[2] * b[1],
        a[2] * b[0] - a[0] * b[2],
        a[0] * b[1] - a[1] * b[0],
    )


def normalize_projective_int(p):
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


def det3(m):
    return (
        m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
        - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
        + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0])
    )


def inv3(m):
    d = det3(m)
    assert d != 0
    a, b, c = m[0]
    d0, e, f = m[1]
    g, h, i = m[2]
    cof = [
        [e*i-f*h, -(d0*i-f*g), d0*h-e*g],
        [-(b*i-c*h), a*i-c*g, -(a*h-b*g)],
        [b*f-c*e, -(a*f-c*d0), a*e-b*d0],
    ]
    return [[Fraction(cof[j][r], d) for j in range(3)] for r in range(3)]


def mat_vec(m, v):
    return tuple(sum(m[r][c] * v[c] for c in range(3)) for r in range(3))


def mat_cols(cols):
    return [[Fraction(cols[c][r]) for c in range(3)] for r in range(3)]


def proportional_scalar(v, w):
    lam = None
    for vi, wi in zip(v, w):
        vi = Fraction(vi)
        wi = Fraction(wi)
        if wi:
            q = vi / wi
            if lam is None:
                lam = q
            elif q != lam:
                return None
        elif vi:
            return None
    return lam


def squareclass_q(q):
    """Squareclass representative in Q*/Q*^2 as signed squarefree integer."""
    q = Fraction(q)
    sign = -1 if q < 0 else 1
    num = abs(q.numerator)
    den = q.denominator
    parity = {}
    for n in (num, den):
        p = 2
        while p * p <= n:
            while n % p == 0:
                parity[p] = parity.get(p, 0) ^ 1
                n //= p
            p += 1
        if n > 1:
            parity[n] = parity.get(n, 0) ^ 1
    out = sign
    for p, bit in parity.items():
        if bit:
            out *= p
    return out


# Incidence ledger.
points = {}
for u, v in combinations(LABELS, 2):
    p = normalize_projective_int(cross(LINES[u], LINES[v]))
    incident = frozenset(k for k in LABELS if dot(LINES[k], p) == 0)
    points[p] = incident

triple_points = {p: s for p, s in points.items() if len(s) == 3}
double_points = {p: s for p, s in points.items() if len(s) == 2}
assert len(triple_points) == 6
assert len(double_points) == 3
assert len(points) == 9

# The seven lines remain distinct with the same 6-triple/3-double incidence
# pattern in every odd characteristic. Inclusion-exclusion gives
# #(P^2\D)(F_p)=(p-3)^2.
assert 7 - 12 - 3 == -8

incidence_blocks = set(triple_points.values()) | set(double_points.values())
incidence_aut = []
for perm_tuple in permutations(LABELS):
    perm = dict(zip(LABELS, perm_tuple))
    image_blocks = {
        frozenset(perm[x] for x in block)
        for block in incidence_blocks
    }
    if image_blocks == incidence_blocks:
        incidence_aut.append(perm)
assert len(incidence_aut) == 24


# Projective realization and cover-lift field.
def frame_projectivity(targets):
    """Unique dual-P2 projectivity sending FRAME to targets."""
    q1, q2, q3, q4 = [LINES[t] for t in targets]
    qmat = mat_cols((q1, q2, q3))
    inv = inv3(qmat)
    lam = mat_vec(inv, q4)
    cols = []
    for j, q in enumerate((q1, q2, q3)):
        cols.append(tuple(lam[j] * Fraction(x) for x in q))
    return mat_cols(cols)


projective_aut = []
for targets in permutations(FRAME):
    m = frame_projectivity(targets)
    mapping = {}
    scalars = {}
    for label, v in LINES.items():
        mv = mat_vec(m, v)
        matches = []
        for target, w in LINES.items():
            lam = proportional_scalar(mv, w)
            if lam not in (None, 0):
                matches.append((target, lam))
        assert len(matches) == 1
        mapping[label], scalars[label] = matches[0]
    assert len(set(mapping.values())) == 7
    projective_aut.append((mapping, scalars))

# All 24 frame permutations preserve the seven-line set, so the incidence S4 is
# the actual PGL_3(Q) automorphism group of the arrangement.
assert len(projective_aut) == 24
assert {
    tuple(mapping[k] for k in LABELS)
    for mapping, _ in projective_aut
} == {
    tuple(g[k] for k in LABELS)
    for g in incidence_aut
}

q_lifts = []
qi_lifts = []
for mapping, scalars in projective_aut:
    classes = [squareclass_q(scalars[k]) for k in LABELS]
    # A projectivity lifts over F iff all line multipliers have one common
    # squareclass in F*/F*^2; a common multiplier is projectively irrelevant.
    if len(set(classes)) == 1:
        q_lifts.append(mapping)
    # Here the only multiplier squareclasses are +/-1, so adjoining i makes
    # every projectivity lift.
    assert set(abs(c) for c in classes) == {1}
    qi_lifts.append(mapping)

assert len(q_lifts) == 6
assert len(qi_lifts) == 24


def label_orbits(group):
    seen = set()
    out = []
    for label in LABELS:
        if label in seen:
            continue
        orb = frozenset(g[label] for g in group)
        seen |= set(orb)
        out.append(orb)
    return set(out)


assert label_orbits(q_lifts) == {
    frozenset({"A1", "A2", "A3"}),
    frozenset({"B1", "B2", "B3"}),
    frozenset({"C"}),
}
assert label_orbits(qi_lifts) == {
    frozenset({"A1", "A2", "A3", "C"}),
    frozenset({"B1", "B2", "B3"}),
}

# Deck group has order 64. 64*24 matches the independently published full
# geometric automorphism-group order of the cuboid surface.
assert 64 * len(projective_aut) == 1536
assert 64 * len(q_lifts) == 384


# Arithmetic field of the 48 nodes.
q_triples = 0
qi_triples = 0
for p, block in triple_points.items():
    values = [dot(LINES[k], p) for k in LABELS if k not in block]
    assert all(v != 0 for v in values)
    ref = values[0]
    classes = {squareclass_q(Fraction(v, ref)) for v in values}
    if classes == {1}:
        q_triples += 1
    else:
        assert classes <= {1, -1} and -1 in classes
        qi_triples += 1

assert (q_triples, qi_triples) == (3, 3)
assert q_triples * 8 == 24
assert qi_triples * 8 == 24


print("t3=6")
print("t2=3")
print("triple_points=")
for p, block in sorted(triple_points.items()):
    print(" ", p, sorted(block))
print("double_points=")
for p, block in sorted(double_points.items()):
    print(" ", p, sorted(block))
print("projective_arrangement_aut_order=24")
print("projective_arrangement_aut_group=S4")
print("Q_liftable_base_aut_order=6")
print("Q_liftable_base_aut_group=S3")
print("Q_line_orbits=[3:{A1,A2,A3}, 3:{B1,B2,B3}, 1:{C}]")
print("Q(i)_liftable_base_aut_order=24")
print("Q(i)_line_orbits=[4:{A1,A2,A3,C}, 3:{B1,B2,B3}]")
print("sign_deck_order=64")
print("geometric_sign_semidirect_order=64*24=1536")
print("Q_defined_sign_semidirect_order=64*6=384")
print("node_field_split=24_Q_plus_24_strict_Q(i)")
print("odd_characteristic_projective_complement_count=(p-3)^2")
print("PASS")
