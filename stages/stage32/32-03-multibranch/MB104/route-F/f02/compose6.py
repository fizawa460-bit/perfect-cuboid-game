#!/usr/bin/env python3
"""Degree-6 slack-0 maps of the form p = f o g (deg f = 3, deg g = 2), added to the build_maps6 state.

Why: monodromy tracking preserves the monodromy group, so it never moves from primitive (non-composite) maps to
imprimitive ones (Ritt).  The composite maps form their own braid orbits and random Newton starts rarely land there.
Count check (datum 112222): f in datum 001111 (4 classes), g branched at one of the 3 simple points over I and one of
the 3 over -I: 4 * 9 = 36 = 2556 - 2520 missing maps.

Construction (lemma T0 of DRAFT-TOWER-17): p = f o g is slack 0 iff g has simple critical points with values in
O(f) (the simple points of f over B).  So g(x) = (u - v x^2) / (1 - x^2) with u != v in O(f), after a random
source Moebius map of f.  Datum: n_y(p) = 2 n_y(f) + [label(u) = y] + [label(v) = y].  A rotation h of B moves the
datum to the representative; p' = h o p.  Every candidate goes through Datum.offer of build_maps6 (K duplicate filter,
mp refinement, verification, exact Moebius equivalence for close K), so nothing unverified is written.
Only degree-3 maps from MAPS3 (all 60 by rotating the 8 representatives) are used; type 2 o 3 is not built here.

Usage: python -I compose6.py MAPS6DIR MAPS3DIR [--only D1,D2]   (stop build_maps6 first: both write the state)
"""
import os, sys, json, itertools, argparse
os.environ["MAPS_N"] = "6"
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import numpy as np
import build_maps6 as B6
import build_maps5 as b5

BK = B6.BKEYS; PT = B6.PT


def rotations():
    """24 rotations as (matrix, perm) with perm[i] = index of h(B_i)"""
    def ap(g, z):
        a, b, c, d = g
        if z is None: return None if abs(c) < 1e-12 else a / c
        den = c * z + d
        return None if abs(den) < 1e-12 else (a * z + b) / den
    def lab(z):
        for k, v in PT.items():
            if (v is None and z is None) or (v is not None and z is not None and abs(z - v) < 1e-9): return k
        raise ValueError(z)
    gens = [(1j, 0, 0, 1), (1, 1, -1, 1)]
    def mulg(A, Bm):
        a, b, c, d = A; e, f, g, h = Bm
        return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
    perm = lambda g: tuple(BK.index(lab(ap(g, PT[k]))) for k in BK)
    grp = {perm((1, 0, 0, 1)): (1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        nf = []
        for g in fr:
            for s in gens:
                h = mulg(s, g); p = perm(h)
                if p not in grp: grp[p] = h; nf.append(h)
        fr = nf
    return [(np.array(m, complex).reshape(2, 2), p) for p, m in grp.items()]


ROT = rotations()


def target_apply(h, P, Q):
    """h o (P/Q): (P, Q) -> (a P + b Q, c P + d Q)"""
    return h[0, 0] * P + h[0, 1] * Q, h[1, 0] * P + h[1, 1] * Q


def hom_eval(C, X, Y):
    """sum_k C_k X^k Y^(deg-k) for polynomial arrays X, Y (ascending coefficients)"""
    deg = len(C) - 1; out = np.zeros(1, complex)
    for k, c in enumerate(C):
        t = np.array([1.0 + 0j])
        for _ in range(k): t = np.convolve(t, X)
        for _ in range(deg - k): t = np.convolve(t, Y)
        out = np.pad(out, (0, max(0, len(t) - len(out)))); t = np.pad(t, (0, len(out) - len(t)))
        out = out + c * t
    return out


def label_of(w):
    if not np.isfinite(w): return "oo"
    best = None
    for k, v in PT.items():
        d = (1 / (1 + abs(w))) if v is None else abs(w - v) / ((1 + abs(w) ** 2) ** 0.5 * (1 + abs(v) ** 2) ** 0.5)
        if best is None or d < best[0]: best = (d, k)
    return best[1] if best[0] < 1e-6 else None


def value(P, Q, x):
    pv = np.polyval(P[::-1], x); qv = np.polyval(Q[::-1], x)
    return np.inf if abs(qv) < 1e-14 * max(abs(pv), 1e-300) else pv / qv


def cubics(maps3dir, rng):
    """all degree-3 slack-0 maps (with duplicates up to Moebius), each after a random source Moebius map"""
    out = []
    for fn in os.listdir(os.path.join(maps3dir, "state")):
        if not fn.endswith(".jsonl"): continue
        for l in open(os.path.join(maps3dir, "state", fn)):
            if not l.strip(): continue
            P, Q, cps, vals = b5.parse_state_map(json.loads(l))
            P = np.array([complex(t) for t in P]); Q = np.array([complex(t) for t in Q])
            for h, perm in ROT:
                P2, Q2 = target_apply(h, P, Q)
                T = rng.normal(size=(2, 2)) + 1j * rng.normal(size=(2, 2))
                X = np.array([T[0, 1], T[0, 0]]); Y = np.array([T[1, 1], T[1, 0]])    # x -> (a x + b)/(c x + d)
                out.append((hom_eval(P2, X, Y), hom_eval(Q2, X, Y)))
    return out


def simple_points(P, Q):
    """simple points over B of the cubic P/Q (all finite after the random Moebius map)"""
    pts = []
    for y in BK:
        F = Q if y == "oo" else P - PT[y] * Q
        r = np.roots(F[::-1])
        for i, a in enumerate(r):
            if min([abs(a - b) for j, b in enumerate(r) if j != i] + [1]) > 1e-6: pts.append((a, y))
    return pts


def datum_of(ns_f, lu, lv):
    ns = [2 * k for k in ns_f]
    ns[BK.index(lu)] += 1; ns[BK.index(lv)] += 1
    return ns


def to_chart(P, Q, rng):
    """degree-6 P/Q -> builder chart (z, ell, vals) through three critical points over distinct labels"""
    n = 6
    Pn = np.pad(P, (0, n + 1 - len(P))); Qn = np.pad(Q, (0, n + 1 - len(Q)))
    W = np.zeros(2 * n, complex)
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j >= 1: W[i + j - 1] += (i - j) * Pn[i] * Qn[j]
    W = np.trim_zeros(W, "b")
    cps = list(np.roots(W[::-1]))
    if len(cps) < 2 * n - 2: cps.append(None)                    # critical point at oo
    if len(cps) != 2 * n - 2: return None
    vals = [label_of(value(Pn, Qn, c)) if c is not None else label_of(Pn[n] / Qn[n] if abs(Qn[n]) > 1e-14 else np.inf) for c in cps]
    if any(v is None for v in vals): return None
    best = None
    for i0, i1, i2 in itertools.permutations(range(len(cps)), 3):
        if len({vals[i0], vals[i1], vals[i2]}) < 3: continue
        c0, c1, c2 = cps[i0], cps[i1], cps[i2]
        A = np.stack([B6.hom(c1), B6.hom(c0)], axis=1)
        try: co = np.linalg.solve(A, B6.hom(c2))
        except np.linalg.LinAlgError: continue
        T = A * co[None, :]; Ti = np.linalg.inv(T)
        rest = [i for i in range(len(cps)) if i not in (i0, i1, i2)]
        lam = []
        for i in rest:
            h = Ti @ B6.hom(cps[i])
            lam.append(h[0] / h[1] if abs(h[1]) > 1e-13 * abs(h[0]) else 1e13)
        mc = B6.min_chord(np.array([lam]))[0]
        if best is None or mc > best[0]: best = (mc, T, (i0, i1, i2), rest, lam)
    if best is None or best[0] < B6.KEEP: return None
    mc, T, tri, rest, lam = best
    order = sorted(range(len(rest)), key=lambda j: BK.index(vals[rest[j]]))
    nv = [vals[i] for i in tri] + [vals[rest[j]] for j in order]
    lam = np.array([lam[j] for j in order])
    x = np.concatenate([B6.poly_compose(Pn, T), B6.poly_compose(Qn, T)])
    e = rng.normal(size=B6.NC) + 1j * rng.normal(size=B6.NC)
    x = x / (e @ x)
    zz = np.concatenate([x, lam])[None, :]
    yx, yz = B6.yvecs(nv)
    for _ in range(8):
        F, J = B6.system_batch(yx, yz, zz[:, B6.NC:], zz[:, :B6.NC], e[None, :])
        st = B6.safe_solve(J, -F)
        if not np.isfinite(st).all(): return None
        zz = zz + st
    F, _ = B6.system_batch(yx, yz, zz[:, B6.NC:], zz[:, :B6.NC], e[None, :])
    if np.linalg.norm(F) > 1e-10: return None
    return zz[0], e, nv


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("maps6"); ap.add_argument("maps3"); ap.add_argument("--only", default="")
    a = ap.parse_args()
    H = json.load(open(os.path.join(HERE, "hurwitz6.json")))
    reps = {d: t for d, t, _ in B6.rep_data(H)}
    if a.only: reps = {d: t for d, t in reps.items() if d in set(a.only.split(","))}
    rng = np.random.default_rng(20261116)
    C = cubics(a.maps3, rng)
    D = {}
    stats = {}
    for P, Q in C:
        pts = simple_points(P, Q)
        if len(pts) != 10: continue
        # datum of f from its critical values
        W = np.zeros(6, complex)
        for i in range(4):
            for j in range(4):
                if i + j >= 1: W[i + j - 1] += (i - j) * P[i] * Q[j]
        cv = [label_of(value(P, Q, c)) for c in np.roots(np.trim_zeros(W, "b")[::-1])]
        if None in cv or len(cv) != 4: continue
        nsf = [cv.count(y) for y in BK]
        for (u, lu), (v, lv) in itertools.combinations(pts, 2):
            ns = datum_of(nsf, lu, lv)
            for h, perm in ROT:
                img = [0] * 6
                for i in range(6): img[perm[i]] = ns[i]
                key = "".join(map(str, img))
                if key in reps: break
            else:
                continue
            if key not in D:
                D[key] = B6.Datum(key, reps[key], a.maps6); D[key].prog.setdefault("found_by_compose", 0)
                stats[key] = [len(D[key].recs), 0, 0]
            Dk = D[key]
            if len(Dk.recs) >= Dk.target: continue
            X = np.array([u, 0, -v]); Y = np.array([1.0 + 0j, 0, -1.0])          # g = (u - v x^2) / (1 - x^2)
            Pp, Qp = hom_eval(P, X, Y), hom_eval(Q, X, Y)
            Pp, Qp = target_apply(h, Pp, Qp)
            r = to_chart(Pp, Qp, rng)
            stats[key][1] += 1
            if r is None: continue
            z, e, nv = r
            if Dk.offer(z, e, "compose", nv): stats[key][2] += 1
    import time
    for k, Dk in D.items():
        Dk.save(time.time(), "compose")
        print(k, "before", stats[k][0], "tried", stats[k][1], "added", stats[k][2], "now", len(Dk.recs), "/", Dk.target, flush=True)


if __name__ == "__main__":
    main()
