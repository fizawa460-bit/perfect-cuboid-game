#!/usr/bin/env python3
"""Stage32EX5-D exact canonicalization hostile check.

Scratch-only verifier for BC2-01B. It reconstructs the 48 singular nodes in
Q(i), checks singularity/uniqueness, defines a projective canonical key in the
fixed Stoll coordinate order, and attacks the tempting but invalid stronger
notion of invariance under the geometric automorphism generators.
"""

from fractions import Fraction
from itertools import product
from random import Random


def G(re=0, im=0):
    return (Fraction(re), Fraction(im))


ZERO = G()
ONE = G(1)
I = G(0, 1)


def add(x, y):
    return (x[0] + y[0], x[1] + y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (
        x[0] * y[0] - x[1] * y[1],
        x[0] * y[1] + x[1] * y[0],
    )


def inv(x):
    den = x[0] * x[0] + x[1] * x[1]
    assert den != 0
    return (x[0] / den, -x[1] / den)


def div(x, y):
    return mul(x, inv(y))


def smul(n, x):
    return (Fraction(n) * x[0], Fraction(n) * x[1])


def iszero(x):
    return x == ZERO


def q(n):
    return G(n)


def qi(n):
    return G(0, n)


def canonicalize_projective(point):
    """Normalize in fixed named order [a1,a2,a3,b1,b2,b3,c]."""
    for pivot in point:
        if not iszero(pivot):
            return tuple(div(x, pivot) for x in point)
    raise ValueError("zero vector has no projective class")


def scale(point, lam):
    return tuple(mul(lam, x) for x in point)


def conjugate(point):
    return tuple((x[0], -x[1]) for x in point)


def build_nodes():
    out = []
    # [1,0,0,0,a,b,c]
    for a, b, c in product((-1, 1), repeat=3):
        out.append((q(1), q(0), q(0), q(0), q(a), q(b), q(c)))
    # [0,1,0,a,0,b,c]
    for a, b, c in product((-1, 1), repeat=3):
        out.append((q(0), q(1), q(0), q(a), q(0), q(b), q(c)))
    # [0,0,1,a,b,0,c]
    for a, b, c in product((-1, 1), repeat=3):
        out.append((q(0), q(0), q(1), q(a), q(b), q(0), q(c)))
    # [0,1,s*i,0,a*i,b,0]
    for s, a, b in product((-1, 1), repeat=3):
        out.append((q(0), q(1), qi(s), q(0), qi(a), q(b), q(0)))
    # [1,0,s*i,a*i,0,b,0]
    for s, a, b in product((-1, 1), repeat=3):
        out.append((q(1), q(0), qi(s), qi(a), q(0), q(b), q(0)))
    # [1,s*i,0,a*i,b,0,0]
    for s, a, b in product((-1, 1), repeat=3):
        out.append((q(1), qi(s), q(0), qi(a), q(b), q(0), q(0)))
    return out


def surface_values(p):
    a1, a2, a3, b1, b2, b3, c = p
    return [
        sub(add(mul(a1, a1), mul(a2, a2)), mul(b3, b3)),
        sub(add(mul(a2, a2), mul(a3, a3)), mul(b1, b1)),
        sub(add(mul(a1, a1), mul(a3, a3)), mul(b2, b2)),
        sub(add(add(mul(a1, a1), mul(a2, a2)), mul(a3, a3)), mul(c, c)),
    ]


def jacobian(p):
    a1, a2, a3, b1, b2, b3, c = p
    z = ZERO
    return [
        [smul(2, a1), smul(2, a2), z, z, z, smul(-2, b3), z],
        [z, smul(2, a2), smul(2, a3), smul(-2, b1), z, z, z],
        [smul(2, a1), z, smul(2, a3), z, smul(-2, b2), z, z],
        [smul(2, a1), smul(2, a2), smul(2, a3), z, z, z, smul(-2, c)],
    ]


def matrix_rank(mat):
    a = [row[:] for row in mat]
    rows = len(a)
    cols = len(a[0])
    rank = 0
    for col in range(cols):
        pivot = next(
            (r for r in range(rank, rows) if not iszero(a[r][col])),
            None,
        )
        if pivot is None:
            continue
        a[rank], a[pivot] = a[pivot], a[rank]
        pivot_inv = inv(a[rank][col])
        a[rank] = [mul(x, pivot_inv) for x in a[rank]]
        for r in range(rows):
            if r != rank and not iszero(a[r][col]):
                factor = a[r][col]
                a[r] = [
                    sub(a[r][j], mul(factor, a[rank][j]))
                    for j in range(cols)
                ]
        rank += 1
        if rank == rows:
            break
    return rank


def swap12(p):
    a1, a2, a3, b1, b2, b3, c = p
    return (a2, a1, a3, b2, b1, b3, c)


def swap13(p):
    a1, a2, a3, b1, b2, b3, c = p
    return (a3, a2, a1, b3, b2, b1, c)


def duality(p):
    a1, a2, a3, b1, b2, b3, c = p
    return (
        mul(I, c),
        a2,
        a3,
        b1,
        mul(I, b3),
        neg(mul(I, b2)),
        neg(mul(I, a1)),
    )


def flip(k):
    def action(p):
        out = list(p)
        out[k] = neg(out[k])
        return tuple(out)

    return action


def orbit(start, generator_maps):
    seen = {start}
    stack = [start]
    while stack:
        current = stack.pop()
        for g in generator_maps:
            nxt = g[current]
            if nxt not in seen:
                seen.add(nxt)
                stack.append(nxt)
    return seen


def main():
    nodes = build_nodes()
    assert len(nodes) == 48

    # Each displayed point lies on the surface and has Jacobian rank 3.
    assert all(all(iszero(v) for v in surface_values(p)) for p in nodes)
    assert {matrix_rank(jacobian(p)) for p in nodes} == {3}

    keys = [canonicalize_projective(p) for p in nodes]
    keyset = set(keys)
    assert len(keyset) == 48

    # Zero-coordinate edge cases: the first nonzero pivot occurs only in a1/a2/a3.
    pivot_counts = [0] * 7
    for p in nodes:
        pivot = next(j for j, x in enumerate(p) if not iszero(x))
        pivot_counts[pivot] += 1
    assert pivot_counts == [24, 16, 8, 0, 0, 0, 0]

    # Exact global-projective-scale invariance on adversarial representatives.
    scalars = [G(-1), I, G(2), G(1, 1), G(3, -2)]
    for lam in scalars:
        assert {canonicalize_projective(scale(p, lam)) for p in nodes} == keyset

    # Enumeration-order invariance: sorted/set canonical identities do not change.
    shuffled = nodes[:]
    Random(3205).shuffle(shuffled)
    assert {canonicalize_projective(p) for p in shuffled} == keyset
    assert {canonicalize_projective(p) for p in reversed(nodes)} == keyset

    # Stoll's nine substitution generators preserve the 48-node set bijectively.
    generators = [swap12, swap13, duality] + [flip(k) for k in range(6)]
    generator_maps = []
    for action in generators:
        images = [canonicalize_projective(action(p)) for p in keys]
        assert len(set(images)) == 48
        assert set(images) == keyset
        generator_maps.append(
            {p: canonicalize_projective(action(p)) for p in keyset}
        )

    # Hostile check: quotienting by the full geometric action destroys node identity.
    full_orbit = orbit(next(iter(keyset)), generator_maps)
    assert len(full_orbit) == 48

    # Independent sign changes are not projective equivalences.
    moved = []
    for action in generators[3:]:
        moved.append(
            sum(canonicalize_projective(action(p)) != p for p in keyset)
        )
    assert moved == [24, 24, 24, 32, 32, 32]

    # Complex conjugation is also a permutation/equivariance, not pointwise identity.
    conjugated = {canonicalize_projective(conjugate(p)) for p in keyset}
    assert conjugated == keyset
    assert any(canonicalize_projective(conjugate(p)) != p for p in keyset)

    print("PASS stage32ex5-d canonicalization hostile check")
    print("nodes=48 unique_keys=48 jacobian_rank=3")
    print("pivot_counts=[24,16,8,0,0,0,0]")
    print("stoll_generator_orbit_size=48")
    print("full_geometric_orbit_invariance=REJECTED_COLLAPSES_48_TO_1")
    print("maximal_required_invariance=projective_scale+enumeration_order")
    print("geometric_action_semantics=EQUIVARIANT_NOT_INVARIANT")


if __name__ == "__main__":
    main()
