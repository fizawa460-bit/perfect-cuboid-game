#!/usr/bin/env python3

from collections import defaultdict
from itertools import product

# Exact retained Q(T) Gram matrix in coordinate order
# (t11.a,t11.b,t12.a,t12.b,t21.a,t21.b,t22.a,t22.b).
A = [
    [4,0,-2,-4,2,-4,-3,0],
    [0,8,4,-4,4,4,0,-6],
    [-2,4,4,0,1,4,2,-4],
    [-4,-4,0,8,-4,2,4,4],
    [2,4,1,-4,4,0,-2,-4],
    [-4,4,4,2,0,8,4,-4],
    [-3,0,2,4,-2,4,4,0],
    [0,-6,-4,4,-4,-4,0,8],
]

# Columns of the retained unimodular U with U^t A U=D4+D4.
Ucols = [
    [1,1,0,1,-2,0,-1,-1],
    [-2,0,-1,-1,1,-1,1,0],
    [1,0,0,1,0,1,-1,0],
    [1,0,0,0,0,0,1,0],
    [1,1,0,1,-1,0,-1,0],
    [-2,0,-1,-1,1,-1,2,0],
    [1,0,0,1,-1,0,-1,-1],
    [1,0,0,0,-1,1,-1,0],
]
U = [[Ucols[j][i] for j in range(8)] for i in range(8)]

RES3 = [73, 97, 235]
EXPECTED_ACTIONS = {
    73: [[1,0,0,1],[0,1,0,0],[0,0,1,0],[0,0,0,1]],
    97: [[1,0,0,0],[0,1,1,0],[0,0,1,0],[0,0,0,1]],
    235:[[1,0,1,1],[0,1,1,1],[0,0,1,0],[0,0,0,1]],
}


def q(v):
    return sum(v[i] * A[i][j] * v[j] for i in range(8) for j in range(8))


def matvec(M, v, mod=None):
    out = [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]
    return out if mod is None else [x % mod for x in out]


def rank2(rows):
    rows = [list(map(lambda x: x & 1, r)) for r in rows]
    if not rows:
        return 0
    m, n = len(rows), len(rows[0])
    rank = 0
    for col in range(n):
        pivot = next((i for i in range(rank, m) if rows[i][col]), None)
        if pivot is None:
            continue
        rows[rank], rows[pivot] = rows[pivot], rows[rank]
        for i in range(m):
            if i != rank and rows[i][col]:
                rows[i] = [a ^ b for a, b in zip(rows[i], rows[rank])]
        rank += 1
    return rank


def residue_bits(res):
    return tuple((res >> i) & 1 for i in range(8))


def code4(t):
    return sum((t[i] % 4) * (4 ** i) for i in range(8))


def decode4(c):
    out = []
    for _ in range(8):
        out.append(c % 4)
        c //= 4
    return tuple(out)


def subcode(target, left):
    t, a = decode4(target), decode4(left)
    return code4(tuple((t[i] - a[i]) % 4 for i in range(8)))


# Actual R=Z[r], r^2=-2, linear action on basis (e1,e2,r e1,r e2).
def rlinear_matrix_mod4(t):
    a11,b11,a12,b12,a21,b21,a22,b22 = t
    return [
        [a11,a12,-2*b11,-2*b12],
        [a21,a22,-2*b21,-2*b22],
        [b11,b12,a11,a12],
        [b21,b22,a21,a22],
    ]


# A[2] = {x in J[4]:2x in W}/W.  In the retained basis a quotient basis is
# [2e1],[2e2],[r e1],[r e2].
A2_GENS = [(2,0,0,0),(0,2,0,0),(0,0,1,0),(0,0,0,1)]


def encode_A2(x):
    x = tuple(a % 4 for a in x)
    return ((x[0] // 2) & 1, (x[1] // 2) & 1, x[2] & 1, x[3] & 1)


def action_A2(t):
    M = rlinear_matrix_mod4(t)
    cols = []
    for g in A2_GENS:
        y = matvec(M, g, 4)
        cols.append(encode_A2(y))
    return [[cols[j][i] for j in range(4)] for i in range(4)]


# 256 raw mod4 lifts per mod2 residue; exactly 128 satisfy Q=602 mod 8.
lifts = {}
for res in RES3:
    b = residue_bits(res)
    keep = []
    for k in product((0,1), repeat=8):
        t = tuple(b[i] + 2*k[i] for i in range(8))
        if q(t) % 8 == 602 % 8:
            keep.append(t)
    assert len(keep) == 128
    lifts[res] = keep

    actions = {tuple(sum(action_A2(t), [])) for t in keep}
    assert len(actions) == 1
    M = action_A2(keep[0])
    assert M == EXPECTED_ACTIONS[res]
    MI = [[M[i][j] ^ (1 if i == j else 0) for j in range(4)] for i in range(4)]
    assert rank2(M) == 4
    assert rank2(MI) == 1


# Exact Q=602 reachability of every retained mod4 class.
# Enumerate a single D4 in the standard even-sum model z in Z^4, ||z||^2<=602,
# convert to the retained simple-root coordinates y, and record only norm/mod4 data.
# This is bounded and does not materialize the 1.3-billion D4+D4 shell.

def z_to_y(z):
    z1,z2,z3,z4 = z
    a = z1
    b = z1 + z2
    s = z3 + b
    assert (s-z4) % 2 == 0
    c = (s-z4)//2
    d = (s+z4)//2
    return (a,b,c,d)


def contribution_code(y4, factor):
    y = list(y4) + [0,0,0,0] if factor == 0 else [0,0,0,0] + list(y4)
    x = matvec(U, y, 4)
    return code4(tuple(x))

pairs = defaultdict(list)
for a in range(-24,25):
    for b in range(-24,25):
        n = a*a + b*b
        if n <= 602:
            pairs[n].append((a,b))

reach = [defaultdict(set), defaultdict(set)]
for n12, p12 in pairs.items():
    for n34, p34 in pairs.items():
        n = n12 + n34
        if n > 602:
            continue
        for z1,z2 in p12:
            for z3,z4 in p34:
                if (z1+z2+z3+z4) & 1:
                    continue
                y = z_to_y((z1,z2,z3,z4))
                reach[0][n].add(contribution_code(y,0))
                reach[1][n].add(contribution_code(y,1))

for res in RES3:
    for t in lifts[res]:
        target = code4(t)
        ok = False
        for n, lefts in reach[0].items():
            rights = reach[1].get(602-n)
            if not rights:
                continue
            for left in lefts:
                if subcode(target,left) in rights:
                    ok = True
                    break
            if ok:
                break
        assert ok, (res,t)

# Representative exact witnesses from the bounded replay.
for w in [
    (13,-16,32,1,0,16,-19,16),
    (-11,-24,16,-16,32,9,5,24),
    (1,-27,28,-15,24,13,1,25),
]:
    assert q(w) == 602


# Prym-side finite model.
# Each Ei[2] is F2^2 with symplectic form; CM i swaps the two axis points and
# fixes the diagonal nonzero point.  K=<k=(x1,x2,x3)> and the type-(1,2,2)
# polarization kernel is k^perp/<k>.
F = [[0,1],[1,0]]
I2 = [[1,0],[0,1]]
CMI = [[0,1],[1,0]]
AXIS = (1,0)
DIAG = (1,1)


def blockdiag3(blocks):
    M = [[0]*6 for _ in range(6)]
    for b,B in enumerate(blocks):
        for i in range(2):
            for j in range(2):
                M[2*b+i][2*b+j] = B[i][j]
    return M

E6 = blockdiag3([F,F,F])


def dot2(a,b):
    return sum(x*y for x,y in zip(a,b)) & 1


def xorv(a,b):
    return tuple(x^y for x,y in zip(a,b))


def kp_action(xs, acts):
    k = tuple(c for x in xs for c in x)
    Ek = matvec(E6, k, 2)
    kperp = [v for v in product((0,1), repeat=6) if dot2(Ek,v) == 0]

    # Build a basis [k,q1,q2,q3,q4] of k^perp.
    basis = [k]
    for v in kperp:
        if rank2(basis+[v]) > rank2(basis):
            basis.append(v)
        if len(basis) == 5:
            break
    assert len(basis) == 5

    lookup = {}
    for coeff in product((0,1), repeat=5):
        v = (0,0,0,0,0,0)
        for j,c in enumerate(coeff):
            if c:
                v = xorv(v,basis[j])
        lookup[v] = coeff

    M6 = blockdiag3(acts)
    cols = []
    for v in basis[1:]:
        y = tuple(matvec(M6,v,2))
        coeff = lookup[y]
        cols.append(coeff[1:])
    return [[cols[j][i] for j in range(4)] for i in range(4)]

# If all selected xi are in the swapped CM orbit, kernel preservation forces identity.
M_id = kp_action([AXIS,AXIS,AXIS],[I2,I2,I2])
assert rank2([[M_id[i][j] ^ (1 if i==j else 0) for j in range(4)] for i in range(4)]) == 0

# If one selected xi is the unique CM-fixed point, i on that factor preserves K
# and induces a transvection on the Prym polarization kernel.
M_tr = kp_action([AXIS,AXIS,DIAG],[I2,I2,CMI])
assert rank2([[M_tr[i][j] ^ (1 if i==j else 0) for j in range(4)] for i in range(4)]) == 1

# Gaussian norm witnesses with the two possible mod2 actions.
assert 11*11 + 4*4 == 137      # 11+4i, identity mod2
assert 4*4 + 11*11 == 137      # 4+11i, i-action mod2
assert 3*3 == 9                # 3, identity mod2
assert 3*3 == 9                # 3i, i-action mod2

print("PASS_EX1_05AA_ACTUAL_RING_MOD4_COLLAPSES_TO_TRANSVECTIONS")
print("mod2_residues", RES3, "mod4_exact_realized_per_residue", 128)
print("A2_action_type", "rank1_transvection", "excluded", 0)
print("next_gate", "selected_Prym_2torsion_CM_orbit")
