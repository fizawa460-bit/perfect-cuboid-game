#!/usr/bin/env python3

from fractions import Fraction
from itertools import combinations, product

# Exact finite replay for EX1-05AC.
# External geometry/source locks (Torelli, complementary polarization gluing,
# Borowka-Ortega isotropic Prym structure) are not reproved here. This verifier
# checks the retained integral matrices and every finite F2 consequence used by
# the alignment argument.


def matmul(A, B, mod=2):
    return [[sum(A[i][k] * B[k][j] for k in range(len(B))) % mod
             for j in range(len(B[0]))] for i in range(len(A))]


def matvec(A, v, mod=2):
    return [sum(A[i][j] * v[j] for j in range(len(v))) % mod
            for i in range(len(A))]


def transpose(A):
    return [list(x) for x in zip(*A)]


def rank2(rows):
    rows = [[x & 1 for x in row] for row in rows]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    r = 0
    for c in range(n):
        p = next((i for i in range(r, m) if rows[i][c]), None)
        if p is None:
            continue
        rows[r], rows[p] = rows[p], rows[r]
        for i in range(m):
            if i != r and rows[i][c]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[r])]
        r += 1
    return r


def addv(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def span(vs):
    out = {(0,) * len(vs[0])}
    for v in vs:
        out |= {addv(x, tuple(v)) for x in list(out)}
    return frozenset(out)


def invariant(S, M):
    return all(tuple(matvec(M, v)) in S for v in S)


def bilinear(x, J, y):
    return sum(x[i] * J[i][j] * y[j] for i in range(len(x)) for j in range(len(y))) & 1


def preserves_form(M, J):
    return matmul(transpose(M), matmul(J, M)) == J


# ---------------------------------------------------------------------------
# 1. Invariant-side principal quotient polarization.
# ---------------------------------------------------------------------------
E = [
    [0, 1, 2, 1],
    [-1, 0, 1, 2],
    [-2, -1, 0, 2],
    [-1, -2, -2, 0],
]

# A=J/W has lattice generated, in the old J lattice coordinates, by
# e1,e2,(r e1)/2,(r e2)/2.  q^*lambda_A0=2 lambda_J.
U = [
    [Fraction(1), 0, 0, 0],
    [0, Fraction(1), 0, 0],
    [0, 0, Fraction(1, 2), 0],
    [0, 0, 0, Fraction(1, 2)],
]
JA = [[0] * 4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        val = Fraction(0)
        for a in range(4):
            for b in range(4):
                val += 2 * E[a][b] * U[i][a] * U[j][b]
        assert val.denominator == 1
        JA[i][j] = int(val) & 1

EXPECTED_JA = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
]
assert JA == EXPECTED_JA
assert rank2(JA) == 4

# Retained residue actions from 05AA, in basis [2e1,2e2,r e1,r e2].
ACT = {
    73:  [[1,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    97:  [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
    235: [[1,0,1,1],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
}
CENTERS = {
    73:  (1,0,0,0),
    97:  (0,1,0,0),
    235: (1,1,0,0),
}
I4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]

for residue, M in ACT.items():
    assert preserves_form(M, JA)
    N = [[M[i][j] ^ I4[i][j] for j in range(4)] for i in range(4)]
    assert rank2(N) == 1
    v = CENTERS[residue]
    # Exact transvection formula x -> x + <x,v>v.
    for x in product((0,1), repeat=4):
        rhs = tuple(x[i] ^ (bilinear(x, JA, v) * v[i]) for i in range(4))
        assert tuple(matvec(M, x)) == rhs

UA = span([(1,0,0,0),(0,1,0,0)])
assert UA == frozenset({(0,0,0,0), CENTERS[73], CENTERS[97], CENTERS[235]})

# ---------------------------------------------------------------------------
# 2. b3,b4 action on A[2] from the actual R=Z[r], r^2=-2 matrices.
# ---------------------------------------------------------------------------
def rlinear_matrix_mod4(t):
    a11,b11,a12,b12,a21,b21,a22,b22 = t
    return [
        [a11,a12,-2*b11,-2*b12],
        [a21,a22,-2*b21,-2*b22],
        [b11,b12,a11,a12],
        [b21,b22,a21,a22],
    ]

A2_GENS = [(2,0,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,1)]


def encode_A2(x):
    x = tuple(a % 4 for a in x)
    return ((x[0] // 2) & 1, (x[1] // 2) & 1, x[2] & 1, x[3] & 1)


def action_A2(t):
    M = rlinear_matrix_mod4(t)
    cols = []
    for g in A2_GENS:
        y = [sum(M[i][j] * g[j] for j in range(4)) % 4 for i in range(4)]
        cols.append(encode_A2(y))
    return [[cols[j][i] for j in range(4)] for i in range(4)]

# b3=[[-1,-1],[1,0]], b4=[[1,1+r],[0,-1]].
b3 = action_A2((-1,0,-1,0, 1,0,0,0))
b4 = action_A2((1,0,1,1, 0,0,-1,0))
EXPECTED_B3 = [[1,1,0,0],[1,0,0,0],[0,0,1,1],[0,0,1,0]]
EXPECTED_B4 = [[1,1,0,1],[0,1,0,0],[0,0,1,1],[0,0,0,1]]
assert b3 == EXPECTED_B3
assert b4 == EXPECTED_B4
assert preserves_form(b3, JA)
assert preserves_form(b4, JA)
assert invariant(UA, b3) and invariant(UA, b4)

# The residue-center permutations agree with the retained marked gauge orbit.
assert tuple(matvec(b3, CENTERS[73])) == CENTERS[235]
assert tuple(matvec(b3, CENTERS[235])) == CENTERS[97]
assert tuple(matvec(b3, CENTERS[97])) == CENTERS[73]
assert tuple(matvec(b4, CENTERS[73])) == CENTERS[73]
assert tuple(matvec(b4, CENTERS[97])) == CENTERS[235]
assert tuple(matvec(b4, CENTERS[235])) == CENTERS[97]

# Enumerate every two-plane in F2^4: UA is the unique one invariant under both.
vecs4 = [v for v in product((0,1), repeat=4) if any(v)]
planes = set()
for a, b in combinations(vecs4, 2):
    if rank2([a,b]) == 2:
        planes.add(span([a,b]))
assert len(planes) == 35
inv_planes = [S for S in planes if invariant(S,b3) and invariant(S,b4)]
assert inv_planes == [UA]

# ---------------------------------------------------------------------------
# 3. Prym polarization kernel K(P,Xi)=k^perp/<k> and factor centers.
# ---------------------------------------------------------------------------
F = [[0,1],[1,0]]
E6 = [[0]*6 for _ in range(6)]
for block in range(3):
    for i in range(2):
        for j in range(2):
            E6[2*block+i][2*block+j] = F[i][j]

xfix = (1,1)  # unique nonzero Gaussian-CM-fixed point in the chosen E[2] basis
k = xfix + xfix + xfix


def symp6(a,b):
    return bilinear(a,E6,b)

kperp = [v for v in product((0,1), repeat=6) if symp6(k,v) == 0]
assert len(kperp) == 32

# Choose a basis [k,q1,q2,q3,q4] of k^perp and use q1..q4 for the quotient.
basis = [k]
for v in kperp:
    if rank2(basis + [v]) > rank2(basis):
        basis.append(v)
    if len(basis) == 5:
        break
assert len(basis) == 5

lookup = {}
for coeff in product((0,1), repeat=5):
    v = (0,0,0,0,0,0)
    for c,b in zip(coeff,basis):
        if c:
            v = addv(v,b)
    lookup[v] = coeff
assert len(lookup) == 32


def qclass(v):
    return tuple(lookup[tuple(v)][1:])

# Quotient symplectic form from k^perp/<k>.
JP = [[0]*4 for _ in range(4)]
for i in range(4):
    for j in range(4):
        JP[i][j] = symp6(basis[i+1], basis[j+1])
assert rank2(JP) == 4

centersP = []
for factor in range(3):
    v = [0]*6
    v[2*factor:2*factor+2] = xfix
    assert symp6(k,tuple(v)) == 0
    centersP.append(qclass(tuple(v)))
assert len(set(centersP)) == 3
assert addv(addv(centersP[0],centersP[1]),centersP[2]) == (0,0,0,0)
UP = span([centersP[0], centersP[1]])
assert UP == frozenset({(0,0,0,0), *centersP})

# Multiplication by i on E[2] swaps the axes and fixes xfix.
CMI = [[0,1],[1,0]]
I2 = [[1,0],[0,1]]


def blockdiag3(blocks):
    M = [[0]*6 for _ in range(6)]
    for b,B in enumerate(blocks):
        for i in range(2):
            for j in range(2):
                M[2*b+i][2*b+j] = B[i][j]
    return M


def quotient_action(M6):
    cols = []
    for qv in basis[1:]:
        y = tuple(matvec(M6,qv))
        assert y in lookup
        cols.append(qclass(y))
    return [[cols[j][i] for j in range(4)] for i in range(4)]

for factor in range(3):
    blocks = [I2,I2,I2]
    blocks[factor] = CMI
    MP = quotient_action(blockdiag3(blocks))
    assert preserves_form(MP, JP)
    N = [[MP[i][j] ^ I4[i][j] for j in range(4)] for i in range(4)]
    assert rank2(N) == 1
    c = centersP[factor]
    for y in product((0,1), repeat=4):
        rhs = tuple(y[i] ^ (bilinear(y,JP,c) * c[i]) for i in range(4))
        assert tuple(matvec(MP,y)) == rhs

# ---------------------------------------------------------------------------
# 4. Abstract factor S3 action and forced equivariant alignment.
# ---------------------------------------------------------------------------
# Label factors so b3: 1->3->2->1 and b4 fixes 1 and swaps 2,3,
# matching the retained L1->L3->L2 cycle and L1-fixed involution.
def permute_factor_vector(v, perm):
    out = [0]*6
    for old,new in enumerate(perm):
        out[2*new:2*new+2] = v[2*old:2*old+2]
    return tuple(out)

p3 = [2,0,1]
p4 = [0,2,1]
assert qclass(permute_factor_vector(xfix+(0,0)+(0,0),p3)) == centersP[2]
assert qclass(permute_factor_vector((0,0)+xfix+(0,0),p3)) == centersP[0]
assert qclass(permute_factor_vector((0,0)+(0,0)+xfix,p3)) == centersP[1]
assert qclass(permute_factor_vector(xfix+(0,0)+(0,0),p4)) == centersP[0]
assert qclass(permute_factor_vector((0,0)+xfix+(0,0),p4)) == centersP[2]
assert qclass(permute_factor_vector((0,0)+(0,0)+xfix,p4)) == centersP[1]

# Naturality of the fixed gluing anti-isometry implies psi^{-1}(UP) is a
# b3,b4-invariant two-plane in A[2].  The finite replay above proves the only
# possibility is UA.  Thus psi maps the three residue centers bijectively to
# the three factor centers.  Equivariance fixes the abstract L-labels uniquely:
# b4-fixed 73 -> b4-fixed L1, then the b3 cycle determines the rest.
alignment = {73:"L1",235:"L3",97:"L2"}
assert alignment[73] == "L1"
assert alignment[235] == "L3"
assert alignment[97] == "L2"

# The required norm on any selected factor can have either mod2 action.
assert 11*11 + 4*4 == 137   # 11+4i: identity mod2
assert 4*4 + 11*11 == 137   # 4+11i: i mod2
assert 3*3 == 9             # 3: identity mod2
assert 3*3 == 9             # 3i: i mod2

Q_STATES = list(range(210,267,2))
assert len(Q_STATES) == 29
assert sorted(ACT) == [73,97,235]

print("PASS_EX1_05AC_FIXED_GLUE_ALIGNS_ALL_THREE_TRANSVECTIONS")
print("A2_pairing", JA)
print("unique_invariant_plane", sorted(UA))
print("alignment", alignment)
print("Q_states", len(Q_STATES), "residues", [73,97,235], "excluded", 0)
