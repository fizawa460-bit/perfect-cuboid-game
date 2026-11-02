"""Equality-face classification (route E, item 2).
For each prime p of K=Q(sqrt2) with N(p)+1 <= 42 and each twist sigma in Delta/Gamma: the Hecke curve
Z_sigma = {(Gamma z, sigma Gamma a z)}, its stabilizer S in the box group G ~ (Z/2)^3, and the genus of Z_sigma/S,
computed from permutation actions of Delta = <x, y> (x^2 = y^3 = (xy)^8 = 1)."""
import json, itertools, sys
from fractions import Fraction as Fr
from qalg import *
from deltagrp import X, Y, XINV, build, mul, normalize, U
REPS, KEYS, PX, PY = build(); NG = len(REPS)
BC = {}   # structure constants: e_s * e_t = sum c e_u  (exact, integral in Z[sqrt2])
for s in range(4):
    for t in range(4): BC[(s, t)] = coords(qm(BASIS[s], BASIS[t]))
for v in BC.values():
    for c in v:
        if not (c[0].denominator == 1 and c[1].denominator == 1): raise SystemExit('FAIL: non-integral structure constant')
# ---------- residue field O_K / p ----------
class Fq:
    def __init__(self, p, s=None):   # split: sqrt2 -> s (mod p); inert: F_p[t]/(t^2-2)
        self.p, self.s = p, s; self.q = p if s is not None else p * p
    def red(self, c):                # c = (a, b) rationals with denominators prime to p
        p = self.p
        def r(x): return (x.numerator * pow(x.denominator, -1, p)) % p
        a, b = r(c[0]), r(c[1])
        return ((a + b * self.s) % p, 0) if self.s is not None else (a, b)
    def add(self, x, y): return ((x[0] + y[0]) % self.p, (x[1] + y[1]) % self.p)
    def mul(self, x, y):
        p = self.p
        if self.s is not None: return (x[0] * y[0] % p, 0)
        return ((x[0]*y[0] + 2*x[1]*y[1]) % p, (x[0]*y[1] + x[1]*y[0]) % p)
    def inv(self, x):
        p = self.p
        if self.s is not None: return (pow(x[0], -1, p), 0)
        n = (x[0]*x[0] - 2*x[1]*x[1]) % p; ni = pow(n, -1, p); return (x[0]*ni % p, (-x[1])*ni % p)
    def zero(self, x): return x[0] % self.p == 0 and x[1] % self.p == 0
def qred(F, q): return [F.red(c) for c in coords(q)]
def rmul(F, v, g):   # v * g for v, g coordinate vectors mod p
    out = [(0, 0)] * 4
    for s in range(4):
        if F.zero(v[s]): continue
        for t in range(4):
            if F.zero(g[t]): continue
            c = F.mul(v[s], g[t])
            for u in range(4): out[u] = F.add(out[u], F.mul(c, F.red(BC[(s, t)][u])))
    return out
BCR = {}
def ideal_key(F, vecs):   # RREF of span(vecs) in F^4
    rows = [list(v) for v in vecs]; R = []; col = 0
    for c in range(4):
        piv = next((r for r in rows if not F.zero(r[c])), None)
        if piv is None: continue
        iv = F.inv(piv[c]); piv = [F.mul(iv, t) for t in piv]
        rows = [r for r in rows if r is not piv]
        new = []
        for r in rows:
            if not F.zero(r[c]):
                f = r[c]; r = [F.add(r[t], F.mul((-f[0] % F.p, -f[1] % F.p), piv[t])) for t in range(4)]
            if any(not F.zero(t) for t in r): new.append(r)
        R = [[F.add(rr[t], F.mul((-rr[c][0] % F.p, -rr[c][1] % F.p), piv[t])) if not F.zero(rr[c]) else rr[t] for t in range(4)] for rr in R]
        R.append(piv); rows = new
    return tuple(tuple(r) for r in sorted(R))
def left_ideal(F, u):  # Qbar * u
    return ideal_key(F, [rmul(F, qred(F, BASIS[s]), u) for s in range(4)])
def ideal_times(F, Ik, g):  # I * g
    return ideal_key(F, [rmul(F, list(r), g) for r in Ik])
# ---------- find a with nrd(a) generating p ----------
def find_a(pi):
    rng = range(-2, 3)
    target = kn(pi)
    for c in itertools.product([(a, b) for a in rng for b in rng], repeat=4):
        q = qa(*[qs((Fr(c[t][0]), Fr(c[t][1])), BASIS[t]) for t in range(4)])
        n = nrd(q)
        if kn(n) == target and n[0] > 0:
            # same ideal as pi: n / pi must be a unit
            r = km(n, kinv(pi))
            if abs(kn(r)) == 1 and r[0].denominator == 1 and r[1].denominator == 1: return q
    return None
# ---------- 2-adic reduction, phi = conjugation by a on Delta/Gamma ----------
def red2(c):
    def r(x):
        if x.denominator % 2 == 0: raise ValueError("not 2-integral")
        return (x.numerator * pow(x.denominator, -1, 2)) % 2
    return (r(c[0]), r(c[1]))
def key2(q):   # Gamma-coset key for any 2-integral element of nrd 1 (even) or u*(2-unit square) (odd)
    n = nrd(q)
    if n == ONE: return ("e",) + tuple(red2(t) for t in coords(q))
    return ("o",) + tuple(red2(t) for t in coords(normalize(qm(XINV, q))))
def phi_table(a):
    ainv = qinv(a); tab = []
    for i, r in enumerate(REPS):
        w = qm(qm(a, r), ainv)            # nrd preserved (1 or u)
        k = key2(w); tab.append(KEYS[k])
    return tab
# ---------- group utilities on Delta/Gamma (left regular action) ----------
def compose(p, q): return [p[q[t]] for t in range(len(q))]   # p after q

# simpler: left multiplication by rep i is determined by i = image of coset 0; build all left perms by BFS on group
from collections import deque
gens = [PX, PY]; seen = {tuple(range(NG)): 0}; perms = [list(range(NG))]; dq = deque([0])
while dq:
    i = dq.popleft()
    for g in gens:
        h = compose(g, perms[i]); t = tuple(h)
        if t not in seen: seen[t] = len(perms); perms.append(h); dq.append(seen[t])
if len(perms) != NG: raise SystemExit('FAIL: group size')
IDX = {p[0]: k for k, p in enumerate(perms)}          # group element <-> image of coset 0
GP = [perms[IDX[c]] for c in range(NG)]               # GP[c] = left mult by the element whose coset is c
def gmul(c1, c2): return GP[c1][c2]
def ginv(c): return next(d for d in range(NG) if gmul(c, d) == 0)
def gorder(c):
    k, d = 1, c
    while d != 0: d = gmul(d, c); k += 1
    return k
# ---------- box group G, free part G0, fixed points ----------
EX = PX[0]; EY = PY[0]; EXY = gmul(EX, EY)
def cyc(e):
    out = [0]; d = e
    while d != 0: out.append(d); d = gmul(d, e)
    return out
CONE = {"x": cyc(EX), "y": cyc(EY), "xy": cyc(EXY)}
def fixed_points(h):
    tot = 0
    for nm, sub in CONE.items():
        cos = set()
        for c in range(NG):
            k = frozenset(gmul(c, s) for s in sub)
            if k in cos: continue
            cos.add(k)
            if frozenset(gmul(h, t) for t in k) == k: tot += 1
    return tot
INV = [ginv(c) for c in range(NG)]
def conj(h, c): return gmul(gmul(c, h), INV[c])
def conj_class(h): return frozenset(conj(h, c) for c in range(NG))
invols = [c for c in range(1, NG) if gmul(c, c) == 0]
classes = sorted({conj_class(c) for c in invols}, key=len)
G = None
for k in range(1, len(classes) + 1):
    for combo in itertools.combinations(classes, k):
        S_ = set().union(*combo) | {0}
        if len(S_) == 8 and all(gmul(a, b) in S_ for a in S_ for b in S_):
            G = sorted(S_); break
    if G: break
FP = {g: fixed_points(g) for g in G}
FREE = [g for g in G if g != 0 and FP[g] == 0]
G0 = None
for a, b in itertools.combinations(FREE, 2):
    c = gmul(a, b)
    if c in FREE: G0 = sorted({0, a, b, c}); break
if __name__ == "__main__":
    print("involution classes sizes", [len(c) for c in classes])
    print("G", G, "fixed points", [FP[g] for g in G])
    print("G0", G0, " G normal:", all(conj(g, c) in G for g in G for c in range(NG)))
    print("fixed points of x, y, xy:", fixed_points(EX), fixed_points(EY), fixed_points(EXY))
# ---------- extra fail-closed checks (E04 audit round 1) ----------
def check_G_unique():
    """G must be the unique normal subgroup of order 8 consisting of the identity and involutions, and G0 the unique
    subgroup of order 4 of G all of whose nontrivial elements act freely on C8."""
    cands = []
    for k in range(1, len(classes) + 1):
        for combo in itertools.combinations(classes, k):
            S_ = set().union(*combo) | {0}
            if len(S_) == 8 and all(gmul(a, b) in S_ for a in S_ for b in S_): cands.append(sorted(S_))
    free_subgroups = []
    for a, b in itertools.combinations(FREE, 2):
        c = gmul(a, b)
        if c in FREE:
            H = sorted({0, a, b, c})
            if H not in free_subgroups: free_subgroups.append(H)
    return len(cands) == 1 and cands[0] == G, len(free_subgroups) == 1 and free_subgroups[0] == G0, len(cands), len(free_subgroups)
def gamma_elements(count=8):
    """nontrivial elements of Gamma = PQ1_B(2): Schreier generators rep(g*c)^-1 * g * rep(c)"""
    from deltagrp import inv, key
    idk = key(Q1); out = []
    for c in range(NG):
        for g, P in ((X, PX), (Y, PY)):
            gm = mul(inv(REPS[P[c]]), mul(g, REPS[c]))
            if key(gm) != idk: raise SystemExit("FAIL: Schreier generator not in Gamma")
            if any(t != Z0 for t in coords(gm)[1:]): out.append(gm)
            if len(out) >= count: return out
    return out
def check_phi_lift_independent(a, gam):
    """phi(h) computed from rep*gamma must equal phi(h) computed from rep, for every coset and every sample gamma"""
    ainv = qinv(a); base = phi_table(a)
    for i, r in enumerate(REPS):
        for gm in gam:
            w = qm(qm(a, mul(r, gm)), ainv)
            if KEYS[key2(w)] != base[i]: return False
    return True
