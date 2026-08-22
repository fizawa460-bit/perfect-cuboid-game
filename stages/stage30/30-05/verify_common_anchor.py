#!/usr/bin/env python3
"""Stage30-05 exact common Q(i) modular/cuboid anchor checker.

This is deliberately finite/exact.  It checks the chosen X(4) gauge on the
Testa--Stoll common quotient model, its induced action on the seven cuboid
squareclasses, and the resulting map from PSL2(Z/4) to arrangement
permutations.  No Galois-cocycle or defect-elimination claim is made here.
"""
from fractions import Fraction
from itertools import product
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
ACTION = ROOT / "stages/stage30/30-02C/action-tables.json"

class QI:
    __slots__ = ("a", "b")
    def __init__(self, a=0, b=0):
        self.a, self.b = Fraction(a), Fraction(b)
    def __add__(self, other):
        other = qi(other)
        return QI(self.a + other.a, self.b + other.b)
    __radd__ = __add__
    def __neg__(self): return QI(-self.a, -self.b)
    def __sub__(self, other): return self + (-qi(other))
    def __rsub__(self, other): return qi(other) - self
    def __mul__(self, other):
        other = qi(other)
        return QI(self.a*other.a-other.b*self.b,
                  self.a*other.b+self.b*other.a)
    __rmul__ = __mul__
    def __truediv__(self, other):
        other = qi(other)
        d = other.a*other.a + other.b*other.b
        assert d
        return QI((self.a*other.a+self.b*other.b)/d,
                  (self.b*other.a-self.a*other.b)/d)
    def __eq__(self, other):
        other = qi(other)
        return self.a == other.a and self.b == other.b
    def zero(self): return self.a == 0 and self.b == 0
    def text(self):
        if self.b == 0: return str(self.a)
        return f"{self.a}+({self.b})i"

def qi(x): return x if isinstance(x, QI) else QI(x)
I_QI = QI(0, 1)

def p_add(p, q):
    out = dict(p)
    for m, c in q.items():
        out[m] = out.get(m, QI()) + c
        if out[m].zero(): del out[m]
    return out

def p_scale(p, c):
    c = qi(c)
    return {m: v*c for m, v in p.items() if not (v*c).zero()}

def lin_mul(a, b):
    out = {}
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            m = tuple(sorted((i, j)))
            out[m] = out.get(m, QI()) + ai*bj
    return {m:c for m,c in out.items() if not c.zero()}

def segre_reduce(p):
    # On Q = X(4)xX(4), XY=TZ.
    out = dict(p)
    c = out.pop((0,1), QI())
    if not c.zero():
        out[(2,3)] = out.get((2,3), QI()) + c
    return {m:c for m,c in out.items() if not c.zero()}

def subst_quad(p, linear_images):
    out = {}
    for (i,j), c in p.items():
        out = p_add(out, p_scale(lin_mul(linear_images[i], linear_images[j]), c))
    return segre_reduce(out)

def proportional(p, q):
    lam = None
    for m in set(p) | set(q):
        a, b = p.get(m,QI()), q.get(m,QI())
        if b.zero():
            if not a.zero(): return None
        else:
            r = a/b
            if lam is None: lam = r
            elif r != lam: return None
    return lam

def e(i):
    return [QI(1 if j == i else 0) for j in range(4)]

def lsum(*terms):
    out = [QI() for _ in range(4)]
    for c, v in terms:
        for j in range(4): out[j] = out[j] + qi(c)*v[j]
    return out

Xv, Yv, Tv, Zv = e(0), e(1), e(2), e(3)
sq = lambda v: lin_mul(v,v)
FORMS = {
    "A1": segre_reduce(sq(lsum((1,Xv),(-1,Yv)))),
    "C":  segre_reduce(sq(lsum((1,Xv),(1,Yv)))),
    "A2": segre_reduce(sq(lsum((1,Tv),(1,Zv)))),
    "A3": segre_reduce(p_scale(sq(lsum((1,Tv),(-1,Zv))), -1)),
    "B1": segre_reduce(p_scale(lin_mul(Xv,Yv), 4)),
    "B2": segre_reduce(p_add(p_add(sq(Xv),sq(Yv)),
                              p_scale(p_add(sq(Tv),sq(Zv)),-1))),
    "B3": segre_reduce(p_add(p_add(sq(Xv),sq(Yv)),
                              p_add(sq(Tv),sq(Zv)))),
}

half = QI(Fraction(1,2))
# Chosen X(4) gauge:
# S: [x:y] -> [-x+y:x+y] (the common scalar sqrt(2) is irrelevant here)
# T: [x:y] -> [i*x:y].
S_COORD = [
    lsum((half,Xv),(-half,Tv),(-half,Zv),(half,Yv)),
    lsum((half,Xv),(half,Tv),(half,Zv),(half,Yv)),
    lsum((-half,Xv),(-half,Tv),(half,Zv),(half,Yv)),
    lsum((-half,Xv),(half,Tv),(-half,Zv),(half,Yv)),
]
T_COORD = [lsum((-1,Xv)), Yv, lsum((I_QI,Tv)), lsum((I_QI,Zv))]

EXPECTED_S = {"A1":"A2","A2":"A1","A3":"A3","B1":"B2","B2":"B1","B3":"B3","C":"C"}
EXPECTED_T = {"A1":"C","C":"A1","A2":"A2","A3":"A3","B1":"B1","B2":"B3","B3":"B2"}

def induced_squareclass_perm(linear_images):
    out, scalars = {}, {}
    for name, p in FORMS.items():
        pp = subst_quad(p, linear_images)
        hits = []
        for target, q in FORMS.items():
            lam = proportional(pp, q)
            if lam is not None: hits.append((target, lam))
        assert len(hits) == 1
        target, lam = hits[0]
        # Every multiplier in this gauge is +/-1; both are squares over Q(i).
        assert lam in (QI(1), QI(-1))
        out[name], scalars[name] = target, lam.text()
    assert len(set(out.values())) == 7
    return out, scalars

S_BRANCH, S_SCALARS = induced_squareclass_perm(S_COORD)
T_BRANCH, T_SCALARS = induced_squareclass_perm(T_COORD)
assert S_BRANCH == EXPECTED_S
assert T_BRANCH == EXPECTED_T

# Exact PSL2(Z/4) construction with Task-A canonicalization.
def mm(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(2)) % 4
                       for j in range(2)) for i in range(2))
def neg(A): return tuple(tuple((-x)%4 for x in row) for row in A)
def canon(A): return min(A, neg(A), key=lambda z: sum(z,()))
SL = [((a,b),(c,d)) for a,b,c,d in product(range(4), repeat=4)
      if (a*d-b*c)%4 == 1]
G = sorted({canon(M) for M in SL}, key=lambda z:sum(z,()))
assert len(SL) == 48 and len(G) == 24
idx = {g:i for i,g in enumerate(G)}
mul = [[idx[canon(mm(a,b))] for b in G] for a in G]
ID = idx[canon(((1,0),(0,1)))]
S_MOD = idx[canon(((0,3),(1,0)))]
T_MOD = idx[canon(((1,1),(0,1)))]

LABELS = ("A1","A2","A3","B1","B2","B3","C")
def pcompose(p,q): return {x:p[q[x]] for x in LABELS}
PID = {x:x for x in LABELS}
def pkey(p): return tuple(p[x] for x in LABELS)

# Extend S_mod->S_BRANCH and T_mod->T_BRANCH to all 24 elements.
rho = {ID: PID}
queue = [ID]
for g in queue:
    pg = rho[g]
    for h, ph in ((S_MOD,S_BRANCH),(T_MOD,T_BRANCH)):
        hg = mul[h][g]
        phg = pcompose(ph, pg)
        if hg not in rho:
            rho[hg] = phg
            queue.append(hg)
        else:
            assert pkey(rho[hg]) == pkey(phg)
assert len(rho) == 24

kernel = sorted(i for i,p in rho.items() if pkey(p) == pkey(PID))
image = {pkey(p) for p in rho.values()}
assert len(kernel) == 4 and len(image) == 6
V = sorted(idx[g] for g in G
           if tuple(tuple(x%2 for x in row) for row in g) == ((1,0),(0,1)))
assert kernel == V == [4,6,12,14]

data = json.loads(ACTION.read_text())
arr_by_perm = {
    tuple(row["images"][x] for x in LABELS): row["id"]
    for row in data["arrangement"]["elements"]
}
image_ids = sorted(arr_by_perm[k] for k in image)
assert image_ids == ["a00","a05","a06","a11","a19","a21"]
assert data["modular"]["V_mod"] == ["g04","g06","g12","g14"]
assert data["arrangement"]["q_liftable_subgroup"] == ["a00","a02","a06","a08","a12","a14"]
# This chosen Q(i) gauge gives a conjugate S3, not the Q-liftable coordinate S3.
assert set(image_ids) != set(data["arrangement"]["q_liftable_subgroup"])

def p_pow(p,n):
    z=PID
    for _ in range(n): z=pcompose(p,z)
    return z
assert pkey(p_pow(T_BRANCH,2)) == pkey(PID)
assert mul[T_MOD][T_MOD] != ID
assert mul[mul[T_MOD][T_MOD]][mul[T_MOD][T_MOD]] == ID
assert mul[T_MOD][T_MOD] in kernel

print("COMMON_TESTA_STOLL_QI_MODEL=PASS")
print("S_BRANCH_ACTION=a06")
print("T_BRANCH_ACTION=a21")
print("MODULAR_PSL2_Z4_ORDER=24")
print("MODULAR_TO_BRANCH_IMAGE_ORDER=6")
print("MODULAR_TO_BRANCH_KERNEL_ORDER=4")
print("MODULAR_TO_BRANCH_KERNEL_IDS=g04,g06,g12,g14")
print("MODULAR_TO_BRANCH_KERNEL_EQUALS_V_MOD=true")
print("MODULAR_TO_BRANCH_IMAGE_IDS=" + ",".join(image_ids))
print("IMAGE_EQUALS_Q_LIFTABLE_S3=false")
print("STAGE30_04_24_ISOMORPHISMS_ARE_GEOMETRIC_ADAPTERS=false")
print("Q_GALOIS_COCYCLE_VERIFIED=false")
print("R29_KUM5_DISCHARGED=false")
print("PERFECT_CUBOID_EXISTENCE_CLAIM=false")
print("PERFECT_CUBOID_NONEXISTENCE_CLAIM=false")
print("PASS")
