"""Delta(2,3,8) = <x, y>, x = -1 + alpha + beta (nrd u = 2+sqrt2), y = alpha (nrd 1), as quaternions with nrd in {1, u}.
Gamma = PQ1_B(2).  Coset key of delta*Gamma: even element q (nrd 1): coords of q mod 2;
odd element q (nrd u): ('o', coords of x^-1 q mod 2).  Builds the permutation action on Delta/Gamma (192 cosets)."""
from qalg import *
U = (Fr(2), Fr(1)); UINV = kinv(U); U2 = km(U, U)
X = qa(qs(kc(-1), Q1), alpha, beta); Y = alpha; XINV = qs(UINV, conj(X))      # nrd X^-1 = 1/u
def normalize(q):
    n = nrd(q)
    if n == ONE or n == U: return q
    if n == U2: return qs(UINV, q)
    if n == UINV: return qs(U, q)
    raise ValueError("unexpected norm %s" % (n,))
def mul(a, b): return normalize(qm(a, b))
def inv(a): return normalize(qinv(a))
def mod2key(q):
    c = coords(q)
    for t in c:
        if t[0].denominator != 1 or t[1].denominator != 1: raise ValueError("non-integral")
    return tuple((int(t[0]) % 2, int(t[1]) % 2) for t in c)
def key(q):
    if nrd(q) == ONE: return ("e",) + mod2key(q)
    return ("o",) + mod2key(normalize(qm(XINV, q)))
def build():
    reps = [Q1]; keys = {key(Q1): 0}; px = {}; py = {}; frontier = [0]
    while frontier:
        nf = []
        for i in frontier:
            for P, g in ((px, X), (py, Y)):
                h = mul(g, reps[i]); k = key(h)
                if k not in keys: keys[k] = len(reps); reps.append(h); nf.append(keys[k])
                P[i] = keys[k]
        frontier = nf
    n = len(reps)
    return reps, keys, [px[i] for i in range(n)], [py[i] for i in range(n)]
def order(p):
    e = list(range(len(p))); q = p[:]; k = 1
    while q != e: q = [p[t] for t in q]; k += 1
    return k
if __name__ == "__main__":
    import json
    reps, keys, px, py = build()
    pxy = [px[py[t]] for t in range(len(px))]
    print("cosets", len(reps), " orders x, y, xy:", order(px), order(py), order(pxy))
    json.dump({"x": px, "y": py}, open("delta_mod_gamma.json", "w"))
