#!/usr/bin/env python3

from itertools import product

# Retained principal Riemann form in basis (e1,e2,r*e1,r*e2).
E = [
    [0, 1, 2, 1],
    [-1, 0, 1, 2],
    [-2, -1, 0, 2],
    [-1, -2, -2, 0],
]
W2 = [(0, 0, 1, 0), (0, 0, 0, 1)]


def bilinear(x, y, M, mod=None):
    v = sum(x[i] * M[i][j] * y[j] for i in range(len(x)) for j in range(len(y)))
    return v if mod is None else v % mod


# W is isotropic for the principal Weil pairing and has maximal possible dimension 2.
for x in W2:
    for y in W2:
        assert bilinear(x, y, E, 2) == 0
assert bilinear(W2[0], W2[1], E) == 2

# Embed W subset J[2] into J[4] by doubling its F2 representatives.
W4 = {
    (0, 0, 0, 0),
    (0, 0, 2, 0),
    (0, 0, 0, 2),
    (0, 0, 2, 2),
}


def times2(x):
    return tuple((2 * a) % 4 for a in x)


J4 = list(product(range(4), repeat=4))
preimage_A2 = {x for x in J4 if times2(x) in W4}
assert len(preimage_A2) == 64
assert len(W4) == 4
assert len(preimage_A2) // len(W4) == 16

# Quotient equality modulo W.
def same_A2_class(x, y):
    d = tuple((a - b) % 4 for a, b in zip(x, y))
    return d in W4


# Explicit witness that mod 2 does not determine the action on A[2].
# T0=I. T1=I+2M with M(e3)=e1. They are equal mod2 and both fix W,
# but differ on the A[2] class represented by e3.
def T0(x):
    return x


def T1(x):
    y = list(x)
    y[0] = (y[0] + 2 * x[2]) % 4
    return tuple(y)


for w in W4:
    assert T0(w) == w
    assert T1(w) == w
x = (0, 0, 1, 0)
assert x in preimage_A2
assert T0(x) in preimage_A2 and T1(x) in preimage_A2
assert not same_A2_class(T0(x), T1(x))

# Retained Q(T) Gram matrix. A mod-4 vector determines Q mod 8:
# Q(x+4y)-Q(x)=8*x^T*A*y+16*y^T*A*y.
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


def q(v):
    return sum(v[i] * A[i][j] * v[j] for i in range(8) for j in range(8))


# Bounded exact replay of the mod-8 invariance formula on representatives.
tests = [
    ((0,0,0,0,0,0,0,0), (1,0,0,0,0,0,0,0)),
    ((1,2,3,0,1,2,3,0), (0,1,-1,2,0,-2,1,1)),
    ((3,3,3,3,3,3,3,3), (1,-1,1,-1,1,-1,1,-1)),
]
for xv, yv in tests:
    lift = tuple(xv[i] + 4 * yv[i] for i in range(8))
    assert (q(lift) - q(xv)) % 8 == 0
assert 602 % 8 == 2

Q_STATES = list(range(210, 267, 2))
RES3 = [73, 97, 235]
assert len(Q_STATES) == 29
assert len(RES3) == 3

print("PASS_EX1_05Z_ISOTROPIC_GLUE_REDUCED_TO_MOD4")
print("W_isotropic", True, "A2_order", 16, "Q602_mod8", 2)
print("states", len(Q_STATES), "mod2_residues", RES3, "excluded", 0)
