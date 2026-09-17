#!/usr/bin/env python3
"""Exact F2 replay for the Bolza six-Weierstrass S4 action on J[2].

This finite group-theory verifier proves the orbit/centralizer claims used by
MB104 U12.  It also proves that the S4 orbit of one ordered adjacent
Weierstrass pair forces theta-differences spanning all of J[2].
It does not by itself prove adelic Hecke level semantics.
"""

from itertools import combinations, permutations, product

EDGES = list(combinations(range(4), 2))


def mat_vec(A, v):
    return tuple(sum(A[i][j] * v[j] for j in range(4)) & 1 for i in range(4))


def mat_mul(A, B):
    return tuple(tuple(sum(A[i][k] * B[k][j] for k in range(4)) & 1 for j in range(4)) for i in range(4))


def mat_add(A, B):
    return tuple(tuple(A[i][j] ^ B[i][j] for j in range(4)) for i in range(4))


I4 = tuple(tuple(1 if i == j else 0 for j in range(4)) for i in range(4))
Z4 = tuple(tuple(0 for _ in range(4)) for _ in range(4))


def vertex_perm_matrix(p):
    edge_perm = []
    for a, b in EDGES:
        image = tuple(sorted((p[a], p[b])))
        edge_perm.append(EDGES.index(image))
    P = [[0] * 6 for _ in range(6)]
    for source, target in enumerate(edge_perm):
        P[target][source] = 1
    return P


def even6_to_q4(v):
    # J[2] = {even vectors in F2^6}/<all-ones>.
    # Write v=sum_{i=0}^4 c_i(e_i+e_5), c_i=v_i, then use complement
    # to set c_4=0 and obtain four quotient coordinates.
    assert sum(v) % 2 == 0
    c = list(v[:5])
    return tuple(c[i] ^ c[4] for i in range(4))


def q4_basis_lift(j):
    v = [0] * 6
    v[j] = 1
    v[5] = 1
    return v


def pair_class(i, j):
    v = [0] * 6
    v[i] = 1
    v[j] = 1
    return even6_to_q4(v)


def action4(p):
    P = vertex_perm_matrix(p)
    cols = []
    for j in range(4):
        v = q4_basis_lift(j)
        vp = [sum(P[i][k] * v[k] for k in range(6)) & 1 for i in range(6)]
        cols.append(even6_to_q4(vp))
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def rank_vectors(vs):
    M = [list(v) for v in vs]
    r = 0
    for c in range(4):
        pivot = next((i for i in range(r, len(M)) if M[i][c]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        for i in range(len(M)):
            if i != r and M[i][c]:
                M[i] = [x ^ y for x, y in zip(M[i], M[r])]
        r += 1
    return r


def rank4(A):
    return rank_vectors(A)


def edge_image(p, i):
    a, b = EDGES[i]
    return EDGES.index(tuple(sorted((p[a], p[b]))))


def adjacent(i, j):
    return i != j and len(set(EDGES[i]) & set(EDGES[j])) == 1


def main():
    perms = list(permutations(range(4)))
    s4 = [action4(p) for p in perms]
    assert len(set(s4)) == 24

    nonzero = [v for v in product((0, 1), repeat=4) if any(v)]
    unseen = set(nonzero)
    orbits = []
    while unseen:
        v = next(iter(unseen))
        orb = {mat_vec(A, v) for A in s4}
        orbits.append(orb)
        unseen -= orb
    assert sorted(map(len, orbits)) == [3, 12]
    orbit3 = next(o for o in orbits if len(o) == 3)
    orbit12 = next(o for o in orbits if len(o) == 12)

    centralizer = []
    for bits in range(1 << 16):
        A = tuple(tuple((bits >> (4 * i + j)) & 1 for j in range(4)) for i in range(4))
        if all(mat_mul(A, G) == mat_mul(G, A) for G in s4):
            centralizer.append(A)
    assert len(centralizer) == 4
    ranks = sorted(rank4(A) for A in centralizer)
    assert ranks == [0, 2, 4, 4]

    N = next(A for A in centralizer if rank4(A) == 2)
    kerN = {v for v in nonzero if mat_vec(N, v) == (0, 0, 0, 0)}
    assert kerN == orbit3
    assert mat_mul(N, N) == Z4
    assert mat_add(I4, N) in centralizer

    for delta in orbit12:
        killers = [A for A in centralizer if mat_vec(A, delta) == (0, 0, 0, 0)]
        assert killers == [Z4]

    # The six Weierstrass points are tetrahedron edges.  Ordered adjacent edge
    # pairs form one orbit of size 24.  This models transporting one U12 spin
    # equality by the full S4 level-symmetry action.
    ordered_adjacent = {(i, j) for i in range(6) for j in range(6) if adjacent(i, j)}
    assert len(ordered_adjacent) == 24
    seed = next(iter(ordered_adjacent))
    seed_orbit = {
        (edge_image(p, seed[0]), edge_image(p, seed[1]))
        for p in perms
    }
    assert seed_orbit == ordered_adjacent

    # For a fixed first edge a, spin equalities for all adjacent b imply that
    # p1^* kills theta_b-theta_c for pairs b,c adjacent to a.  Each anchor
    # gives rank 3; taking the full S4 orbit (all anchors) spans all J[2].
    generated = []
    anchor_ranks = []
    for a in range(6):
        neigh = [b for b in range(6) if adjacent(a, b)]
        assert len(neigh) == 4
        local = [pair_class(b, c) for b, c in combinations(neigh, 2)]
        anchor_ranks.append(rank_vectors(local))
        generated.extend(local)
    assert anchor_ranks == [3] * 6
    assert rank_vectors(generated) == 4
    assert set(generated) == set(nonzero)

    print("PASS STAGE32_MB104_U12_BOLZA_J2_CENTRALIZER_V2")
    print("nonzero J[2] orbits under S4: 3 + 12")
    print("End_{S4}(J[2]) has 4 elements with ranks 0,2,4,4")
    print("unique rank-2 nilpotent has kernel equal to the 3-orbit")
    print("killing any 12-orbit vector forces the zero endomorphism")
    print("ordered adjacent Weierstrass pairs form one S4 orbit of size 24")
    print("spin differences: rank 3 per anchor, rank 4 globally; all 15 nonzero J[2] classes occur")


if __name__ == "__main__":
    main()
