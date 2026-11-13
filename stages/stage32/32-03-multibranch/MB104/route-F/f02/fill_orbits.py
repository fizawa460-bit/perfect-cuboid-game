"""Close the degree-4 slack-0 map list under the symmetries of B.
G = the 24 Moebius maps permuting B = {0, oo, +-1, +-i} (octahedral rotations), together with complex conjugation.
Post-composition p -> g o p maps slack-0 maps to slack-0 maps (with permuted branch datum). Every image is
compared exactly (up to source Moebius, key_maps_equal) with the list, and new maps are added.
usage: python -I -O fill_orbits.py   (reads maps4.json and hurwitz4.json, rewrites maps4.json if maps were added)"""
import itertools, json, sys
import numpy as np
import mpmath as mp
import os, sys as _s; _s.path.insert(0, os.path.dirname(os.path.abspath(__file__))); import build_maps as BM

mp.mp.dps = 45
n = 4
BPTS = {"I": mp.mpc(0, 1), "-I": mp.mpc(0, -1), "1": mp.mpc(1), "-1": mp.mpc(-1), "0": mp.mpc(0), "oo": mp.inf}


def mob(M, z):
    a, b, c, d = M
    if z == mp.inf: return mp.inf if c == 0 else a / c
    den = c * z + d
    return mp.inf if abs(den) < mp.mpf(10) ** -30 else (a * z + b) / den


def close_eq(z, w):
    if z == mp.inf or w == mp.inf: return z == w
    return abs(z - w) < mp.mpf(10) ** -20


def group():
    gens = [(mp.mpc(0, 1), 0, 0, 1), (1, 1, -1, 1)]     # t -> i t, t -> (t+1)/(1-t)
    G = [(1, 0, 0, 1)]
    def mul(A, B):
        a, b, c, d = A; e, f, g, h = B
        return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
    def same(A, B):
        k = max(range(4), key=lambda t: abs(A[t]))
        if abs(B[k]) < 1e-12: return False
        s = A[k] / B[k]
        return all(abs(A[t] - s * B[t]) < 1e-12 for t in range(4))
    frontier = list(G)
    while frontier:
        new = []
        for A in frontier:
            for g in gens:
                C = tuple(mp.mpc(x) for x in mul(g, A))
                if not any(same(C, D) for D in G): G.append(C); new.append(C)
        frontier = new
    return G


def crit_points(P, Q):
    dP = [k * P[k] for k in range(1, n + 1)]; dQ = [k * Q[k] for k in range(1, n + 1)]
    W = [mp.mpc(0)] * (2 * n)
    for i, a in enumerate(dP):
        for k, b in enumerate(Q): W[i + k] += a * b
    for i, a in enumerate(P):
        for k, b in enumerate(dQ): W[i + k] -= a * b
    nrm = max(abs(t) for t in W)
    deg = max(k for k in range(2 * n) if abs(W[k]) > mp.mpf(10) ** -30 * nrm)
    rts = list(mp.polyroots(list(reversed(W[:deg + 1])), maxsteps=400, extraprec=400)) if deg > 0 else []
    return rts + [mp.inf] * (2 * n - 2 - deg)


def value(P, Q, c):
    if c == mp.inf: num, den = P[n], Q[n]
    else: num, den = mp.polyval(list(reversed(P)), c), mp.polyval(list(reversed(Q)), c)
    return mp.inf if abs(den) < mp.mpf(10) ** -25 * (abs(num) + abs(den)) else num / den


def label(v):
    for k, b in BPTS.items():
        if close_eq(v, b): return k
    return None


def record(P, Q):
    cps = crit_points(P, Q)
    vals = [label(value(P, Q, c)) for c in cps]
    if None in vals: return None
    order = sorted(range(len(cps)), key=lambda i: BM.BKEYS.index(vals[i]))
    cps = [cps[i] for i in order]; vals = [vals[i] for i in order]
    return (P, Q, cps, vals)


def datum(vals):
    return "".join(str(vals.count(k)) for k in BM.BKEYS)


maps = json.load(open("maps4.json"))
H = {k: v[0] for k, v in json.load(open("hurwitz4.json")).items()}
recs = {}
for m in maps:
    P = [BM.parse_c(c) for c in m["P"]]; Q = [BM.parse_c(c) for c in m["Q"]]
    r = record(P, Q); assert r is not None and datum(r[3]) == m["datum"], m["datum"]
    recs.setdefault(m["datum"], []).append(r)
G = group(); print("group order", len(G))
added = 0
short = [k for k in H if len(recs.get(k, [])) < H[k]]
print("short data before:", {k: (len(recs.get(k, [])), H[k]) for k in short})
def nkey(r):
    P, Q, cps, vals = r
    cd = [None if c == mp.inf else complex(c) for c in cps]
    return BM.num_key(n, [complex(x) for x in P], [complex(x) for x in Q], cd)


keys = {k: [nkey(r) for r in recs[k]] for k in short}
for k in short:          # g o p permutes the branch datum, so only maps of the short data themselves can give new ones
    for r in list(recs[k]):
        P, Q = r[0], r[1]
        for g in G:
            a, b, c, d = g
            for conj in (False, True):
                P2 = [a * p + b * q for p, q in zip(P, Q)]; Q2 = [c * p + d * q for p, q in zip(P, Q)]
                if conj: P2 = [mp.conj(x) for x in P2]; Q2 = [mp.conj(x) for x in Q2]
                r2 = record(P2, Q2)
                if r2 is None: continue
                dk = datum(r2[3])
                if dk not in short: continue
                k2 = nkey(r2)
                near = [f for f, kk in zip(recs[dk], keys[dk]) if np.max(np.abs(kk - k2)) < 1e-3]
                if any(BM.key_maps_equal(n, f, r2) for f in near): continue
                recs[dk].append(r2); keys[dk].append(k2); added += 1
                print("added a map to datum", dk, "from", k, flush=True)
print("added", added)
still = {k: (len(recs.get(k, [])), H[k]) for k in H if len(recs.get(k, [])) != H[k]}
print("data not at target after closure:", still)
if added:
    flat = [{"datum": k, "P": [mp.nstr(c, 40) for c in r[0]], "Q": [mp.nstr(c, 40) for c in r[1]]}
            for k in sorted(recs) for r in recs[k]]
    json.dump(flat, open("maps4.json", "w"))
    print("maps4.json rewritten with", len(flat), "maps")
if still: raise SystemExit(1)
