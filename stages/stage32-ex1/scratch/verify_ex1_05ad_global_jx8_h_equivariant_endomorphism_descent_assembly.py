#!/usr/bin/env python3

from itertools import permutations, product

# Exact finite replay for EX1-05AD.
# This verifies the three exact Q602 base witnesses, their descent-compatible
# A[2] actions, an explicit symplectic gluing model to the Prym kernel, Gaussian
# component choices for every possible abstract-factor/named-character adapter,
# and the retained H-Fourier deck trace package. It does not construct a curve.

GRAM = [
    [4,0,-2,-4,2,-4,-3,0],
    [0,8,4,-4,4,4,0,-6],
    [-2,4,4,0,1,4,2,-4],
    [-4,-4,0,8,-4,2,4,4],
    [2,4,1,-4,4,0,-2,-4],
    [-4,4,4,2,0,8,4,-4],
    [-3,0,2,4,-2,4,4,0],
    [0,-6,-4,4,-4,-4,0,8],
]

WITNESSES = {
    73:  (13,-16,32,1,0,16,-19,16),
    97:  (-11,-24,16,-16,32,9,5,24),
    235: (1,-27,28,-15,24,13,1,25),
}

EXPECTED_A2 = {
    73:  [[1,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    97:  [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
    235: [[1,0,1,1],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
}

CENTERS_A = {
    73:  (1,0,0,0),
    97:  (0,1,0,0),
    235: (1,1,0,0),
}

# 05AC abstract factor order L1,L2,L3.
SELECTED_FACTOR = {73:0, 97:1, 235:2}

JA = [
    [0,0,0,1],
    [0,0,1,0],
    [0,1,0,1],
    [1,0,1,0],
]

I2 = [[1,0],[0,1]]
CMI = [[0,1],[1,0]]
I4 = [[1 if i == j else 0 for j in range(4)] for i in range(4)]


def q(v):
    return sum(v[i] * GRAM[i][j] * v[j] for i in range(8) for j in range(8))


def residue(v):
    return sum(((v[i] & 1) << i) for i in range(8))


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


def bilinear(x, J, y):
    return sum(x[i] * J[i][j] * y[j] for i in range(len(x)) for j in range(len(y))) & 1


def preserves_form(M, J):
    return matmul(transpose(M), matmul(J, M)) == J


def addv(a, b):
    return tuple(x ^ y for x, y in zip(a, b))


def rlinear_matrix_mod4(t):
    a11,b11,a12,b12,a21,b21,a22,b22 = t
    return [
        [a11,a12,-2*b11,-2*b12],
        [a21,a22,-2*b21,-2*b22],
        [b11,b12,a11,a12],
        [b21,b22,a21,a22],
    ]


A2_GENS = [(2,0,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,1)]
W2 = [(0,0,1,0),(0,0,0,1)]


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


# Base exact witnesses: Q=602, exact residue, W fixed, A[2] transvection.
for res, t in WITNESSES.items():
    assert q(t) == 602
    assert residue(t) == res
    M4 = rlinear_matrix_mod4(t)
    M2 = [[x & 1 for x in row] for row in M4]
    for w in W2:
        assert tuple(matvec(M2, w)) == w
    MA = action_A2(t)
    assert MA == EXPECTED_A2[res]
    assert preserves_form(MA, JA)
    center = CENTERS_A[res]
    for x in product((0,1), repeat=4):
        rhs = tuple(x[i] ^ (bilinear(x, JA, center) * center[i]) for i in range(4))
        assert tuple(matvec(MA, x)) == rhs

# Prym finite kernel model: P=(E1xE2xE3)/<k>, xi=(1,1) CM-fixed.
F = [[0,1],[1,0]]
E6 = [[0]*6 for _ in range(6)]
for block in range(3):
    for i in range(2):
        for j in range(2):
            E6[2*block+i][2*block+j] = F[i][j]

xfix = (1,1)
k = xfix + xfix + xfix


def symp6(a, b):
    return bilinear(a, E6, b)


kperp = [v for v in product((0,1), repeat=6) if symp6(k, v) == 0]
assert len(kperp) == 32
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
    for c, b in zip(coeff, basis):
        if c:
            v = addv(v, b)
    lookup[v] = coeff
assert len(lookup) == 32


def qclass(v):
    return tuple(lookup[tuple(v)][1:])


JP = [[symp6(basis[i+1], basis[j+1]) for j in range(4)] for i in range(4)]
assert rank2(JP) == 4

centersP = []
for factor in range(3):
    v = [0]*6
    v[2*factor:2*factor+2] = xfix
    centersP.append(qclass(tuple(v)))
assert len(set(centersP)) == 3
assert addv(addv(centersP[0], centersP[1]), centersP[2]) == (0,0,0,0)


def blockdiag3(blocks):
    M = [[0]*6 for _ in range(6)]
    for b, B in enumerate(blocks):
        for i in range(2):
            for j in range(2):
                M[2*b+i][2*b+j] = B[i][j]
    return M


def quotient_action(M6):
    cols = []
    for qv in basis[1:]:
        y = tuple(matvec(M6, qv))
        assert y in lookup
        cols.append(qclass(y))
    return [[cols[j][i] for j in range(4)] for i in range(4)]


MP_FACTOR = {}
for factor in range(3):
    blocks = [I2,I2,I2]
    blocks[factor] = CMI
    MP = quotient_action(blockdiag3(blocks))
    MP_FACTOR[factor] = MP
    assert preserves_form(MP, JP)
    c = centersP[factor]
    for y in product((0,1), repeat=4):
        rhs = tuple(y[i] ^ (bilinear(y, JP, c) * c[i]) for i in range(4))
        assert tuple(matvec(MP, y)) == rhs

# Construct one symplectic psi with 73->factor0, 97->factor1, 235->factor2.
# Any actual symplectic psi with these center images conjugates the same
# transvections, because a symplectic transvection is determined by its center.
vecP = list(product((0,1), repeat=4))
psi = None
for v3 in vecP:
    for v4 in vecP:
        cols = [centersP[0], centersP[1], v3, v4]
        M = [[cols[j][i] for j in range(4)] for i in range(4)]
        if rank2(transpose(M)) != 4:
            continue
        if matmul(transpose(M), matmul(JP, M)) == JA:
            psi = M
            break
    if psi is not None:
        break
assert psi is not None
assert tuple(matvec(psi, CENTERS_A[73])) == centersP[0]
assert tuple(matvec(psi, CENTERS_A[97])) == centersP[1]
assert tuple(matvec(psi, CENTERS_A[235])) == centersP[2]

for res in (73,97,235):
    MA = EXPECTED_A2[res]
    MP = MP_FACTOR[SELECTED_FACTOR[res]]
    assert matmul(MP, psi) == matmul(psi, MA)

# Gaussian choices. Named character order is chi_u, chi_v, chi_uv, with norms
# 9,137,9. 05AC deliberately leaves the abstract L1/L2/L3 -> named-character
# adapter unspecified, so replay all 6 adapters. Every adapter works.
NAMED_NORMS = [9,137,9]

def gaussian_pair(norm, action_type):
    if norm == 137 and action_type == "identity":
        return (11,4)
    if norm == 137 and action_type == "i":
        return (4,11)
    if norm == 9 and action_type == "identity":
        return (3,0)
    if norm == 9 and action_type == "i":
        return (0,3)
    raise AssertionError((norm, action_type))

for adapter in permutations(range(3)):
    # adapter[abstract_factor] = named_character_index
    assert sorted(adapter) == [0,1,2]
    for res in (73,97,235):
        selected = SELECTED_FACTOR[res]
        alphas = []
        for abstract_factor in range(3):
            named = adapter[abstract_factor]
            norm = NAMED_NORMS[named]
            typ = "i" if abstract_factor == selected else "identity"
            a,b = gaussian_pair(norm, typ)
            assert a*a + b*b == norm
            alphas.append((a,b))
            # Both I and i fix xfix, hence every component fixes the chosen xi.
            M2 = [[(a*I2[i][j] + b*CMI[i][j]) & 1 for j in range(2)] for i in range(2)]
            assert tuple(matvec(M2, xfix)) == xfix
        # Mod-2 product action is exactly the selected-factor transvection.
        blocks = []
        for a,b in alphas:
            blocks.append([[(a*I2[i][j] + b*CMI[i][j]) & 1 for j in range(2)] for i in range(2)])
        MP = quotient_action(blockdiag3(blocks))
        assert MP == MP_FACTOR[selected]
        assert matmul(MP, psi) == matmul(psi, EXPECTED_A2[res])

# Rosati character package and inverse H-Fourier transform.
base_trace = 2 * 602
named_degrees = [9,137,9]  # chi_u, chi_v, chi_uv
char_traces = [base_trace] + [2*d for d in named_degrees]
assert char_traces == [1204,18,274,18]

r0, ru, rv, ruv = char_traces
deck = [
    r0 + ru + rv + ruv,
    r0 - ru + rv - ruv,
    r0 + ru - rv - ruv,
    r0 - ru - rv + ruv,
]
assert deck == [1514,1442,930,930]

Q_STATES = list(range(210,267,2))
assert len(Q_STATES) == 29

print("PASS_EX1_05AD_GLOBAL_JX8_ASSEMBLY_ALL_RESIDUES")
print("Q602_witnesses", {r:list(v) for r,v in WITNESSES.items()})
print("character_traces", char_traces, "deck_traces", deck)
print("abstract_to_named_adapters_checked", 6)
print("Q_states", len(Q_STATES), "residues", [73,97,235], "excluded", 0)
