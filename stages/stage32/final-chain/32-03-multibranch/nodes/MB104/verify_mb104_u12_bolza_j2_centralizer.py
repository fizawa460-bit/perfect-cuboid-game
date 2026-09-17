#!/usr/bin/env python3
"""Exact F2 replay for the Bolza six-Weierstrass S4 action on J[2].

This is a finite group-theory verifier only.  It proves the orbit and centralizer
claims used by MB104-U12-BOLZA-J2-HECKE-SHADOW-20260917.md; it does not prove
that an arbitrary commensurator correspondence is a standard Hecke operator.
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
    # permutation on the six edges of a tetrahedron
    edge_perm = []
    for a, b in EDGES:
        image = tuple(sorted((p[a], p[b])))
        edge_perm.append(EDGES.index(image))
    P = [[0] * 6 for _ in range(6)]
    for source, target in enumerate(edge_perm):
        P[target][source] = 1
    return P


def even6_to_q4(v):
    # E={even vectors in F2^6}; quotient by all-ones.
    # Write v=sum_{i=0}^4 c_i(e_i+e_5), so c_i=v_i.
    c = list(v[:5])
    # canonical quotient representative sets c_4=0 by adding c_4*(1,1,1,1,1)
    return tuple(c[i] ^ c[4] for i in range(4))


def q4_basis_lift(j):
    v = [0] * 6
    v[j] = 1
    v[5] = 1
    return v


def action4(p):
    P = vertex_perm_matrix(p)
    cols = []
    for j in range(4):
        v = q4_basis_lift(j)
        vp = [sum(P[i][k] * v[k] for k in range(6)) & 1 for i in range(6)]
        cols.append(even6_to_q4(vp))
    return tuple(tuple(cols[j][i] for j in range(4)) for i in range(4))


def rank4(A):
    M = [list(row) for row in A]
    r = 0
    for c in range(4):
        pivot = next((i for i in range(r, 4) if M[i][c]), None)
        if pivot is None:
            continue
        M[r], M[pivot] = M[pivot], M[r]
        for i in range(4):
            if i != r and M[i][c]:
                M[i] = [x ^ y for x, y in zip(M[i], M[r])]
        r += 1
    return r


def main():
    s4 = [action4(p) for p in permutations(range(4))]
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

    # The key U12 finite lemma: an S4-equivariant F2 endomorphism killing
    # any vector in the 12-orbit must be the zero endomorphism.
    for delta in orbit12:
        killers = [A for A in centralizer if mat_vec(A, delta) == (0, 0, 0, 0)]
        assert killers == [Z4]

    print("PASS STAGE32_MB104_U12_BOLZA_J2_CENTRALIZER_V1")
    print("nonzero J[2] orbits under S4: 3 + 12")
    print("End_{S4}(J[2]) has 4 elements with ranks 0,2,4,4")
    print("unique rank-2 nilpotent has kernel equal to the 3-orbit")
    print("killing any 12-orbit vector forces the zero endomorphism")


if __name__ == "__main__":
    main()
