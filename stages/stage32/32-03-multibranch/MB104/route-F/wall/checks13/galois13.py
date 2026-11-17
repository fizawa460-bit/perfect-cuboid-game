#!/usr/bin/env python3
"""galois13: is the moduli field of a slack-0 map contained in Q(i)?  (STRATEGY-13b candidate 2, table G-Q1)

For each map p (critical values in B = {0, oo, +-1, +-i}, simple critical points):
  1. refine to 100 digits (degree 3, 4: from P, Q via Wronskian roots + a source Moebius sending three
     finite critical points to 0, oo, 1, then refine5.refine; degree 5: the stored 100-digit state);
  2. compute two Moebius-invariant, label-sensitive invariants
        I_w = sum over ordered 4-tuples (a, b, c, d) of distinct critical points of
              w(a) w(b)^2 w(c)^3 w(d)^5 * cr(a, b, c, d),   cr = (a-c)(b-d)/((a-d)(b-c)),
     with two weight tables w (by the label = critical value);
     Gal(Qbar/Q(i)) fixes B pointwise, so sigma(I(p)) = I(sigma p);
  3. find the smallest d <= DMAX with an integer relation  sum_k (r_k + s_k i) I^k = 0  (PSLQ on
     Re + sqrt(2)*Im, then checked in C to 1e-80).  d = 1 for both invariants  =>  sigma p = p for all
     sigma fixing Q(i) (if I is injective on the type, checked), i.e. moduli field inside Q(i).
     "none" means no relation of degree <= DMAX with coefficients < 10^MAXC was found (not a proof).
Resumable: one JSON line per map in OUT; finished maps are skipped on restart.
Usage: python -I galois13.py DEGREE OUT.jsonl [--dmax 2] [--maxc 40]
"""
import argparse, itertools, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02"))
sys.path.insert(0, F02)
import mpmath as mp
import build_maps as bm
import build_maps5 as b5
import refine5
DPS = 320
mp.mp.dps = DPS
W1 = {"I": 2, "-I": 3, "1": 5, "-1": 7, "0": 11, "oo": 13}
W2 = {"I": 3, "-I": 7, "1": 2, "-1": 13, "0": 5, "oo": 11}
BV = {"I": mp.mpc(0, 1), "-I": mp.mpc(0, -1), "1": mp.mpc(1), "-1": mp.mpc(-1), "0": mp.mpc(0)}


def peval(C, z): return mp.polyval(list(reversed(C)), z)


def label(P, Q, c):
    q = peval(Q, c)
    if abs(q) < mp.mpf(10) ** -15 * (1 + abs(peval(P, c))): return "oo"
    v = peval(P, c) / q
    k = min(BV, key=lambda k: abs(v - BV[k]))
    assert abs(v - BV[k]) < mp.mpf(10) ** -20, mp.nstr(v, 10)
    return k


def from_PQ(n, P, Q):
    """state record (P, Q, cps=[0,oo,1,...], vals) from coefficient lists at moderate precision"""
    mp.mp.dps = 60
    P = [mp.mpc(x) for x in P]; Q = [mp.mpc(x) for x in Q]
    # generic source Moebius z -> z/(s z + 1) first, so that no critical point sits at infinity
    sg = mp.mpf("0.3719")
    P = subst(n, P, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1)); Q = subst(n, Q, mp.mpc(1), mp.mpc(0), mp.mpc(sg), mp.mpc(1))
    W = [mp.mpc(0)] * (2 * n)       # P'Q - PQ'
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j - 1 >= 0: W[i + j - 1] += (i - j) * P[i] * Q[j]
    while abs(W[-1]) < mp.mpf(10) ** -30: W.pop()
    roots = mp.polyroots(list(reversed(W)), maxsteps=400, extraprec=400)
    assert len(roots) >= 3
    c0, c1, c2 = roots[:3]
    A = (c2 - c1) / (c2 - c0)
    al, be, ga, de = c1, -A * c0, mp.mpc(1), -A       # z = (al w + be)/(ga w + de)
    Pn, Qn = subst(n, P, al, be, ga, de), subst(n, Q, al, be, ga, de)
    cps_w = [mp.mpf(0), mp.inf, mp.mpf(1)]
    lab = lambda c: label(P, Q, c)
    vals = [lab(c0), lab(c1), lab(c2)]
    rest = [r for r in roots[3:]]
    if len(W) - 1 < 2 * n - 2: rest_inf = True
    else: rest_inf = False
    assert not rest_inf, "critical point at infinity: not handled"
    for r in rest:
        cps_w.append(A * (r - c0) / (r - c1)); vals.append(lab(r))
    mp.mp.dps = DPS
    return [mp.mpc(x) for x in Pn], [mp.mpc(x) for x in Qn], cps_w, vals


def subst(n, C, al, be, ga, de):
    """coefficients of (ga w + de)^n C((al w + be)/(ga w + de))"""
    out = [mp.mpc(0)] * (n + 1)
    for k, ck in enumerate(C):
        num = [mp.mpc(1)]
        for _ in range(k): num = mul(num, [be, al])
        for _ in range(n - k): num = mul(num, [de, ga])
        for t, x in enumerate(num): out[t] += ck * x
    return out


def mul(a, b):
    out = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i + j] += x * y
    return out


def cr(a, b, c, d):
    def f(x, y): return None if (x == mp.inf or y == mp.inf) else x - y
    num = [f(a, c), f(b, d)]; den = [f(a, d), f(b, c)]
    v = mp.mpc(1)
    for t in num:
        if t is not None: v *= t
    for t in den:
        if t is not None: v /= t
    return v


ORDER = {"I": 0, "-I": 1, "1": 2, "-1": 3, "0": 4, "oo": 5}


def invariant_cr(cps, vals, shift):
    """sum over label-respecting orderings of the points of cr(pt[shift..shift+3])"""
    groups = {}
    for c, v in zip(cps, vals): groups.setdefault(ORDER[v], []).append(c)
    keys = sorted(groups)
    s = mp.mpc(0)
    for perms in itertools.product(*(itertools.permutations(groups[k]) for k in keys)):
        pts = [c for g in perms for c in g]
        q = pts[shift:shift + 4] if shift + 4 <= len(pts) else [pts[0], pts[2], pts[1], pts[3]]
        s += cr(*q)
    return s


def invariant(cps, vals, W):
    s = mp.mpc(0); m = len(cps)
    for t in itertools.permutations(range(m), 4):
        a, b, c, d = t
        s += W[vals[a]] * W[vals[b]] ** 2 * W[vals[c]] ** 3 * W[vals[d]] ** 5 * cr(*(cps[k] for k in t))
    return s


def relation(I, dmax, maxc):
    w = mp.sqrt(2)
    for d in range(1, dmax + 1):
        u = []
        for k in range(d + 1):
            u += [I ** k, mp.mpc(0, 1) * I ** k]
        vec = [x.real + w * x.imag for x in u]
        mc = maxc or max(8, (DPS - 40) // (2 * (d + 1)) - 4)
        rel = mp.pslq(vec, maxcoeff=10 ** mc, maxsteps=400000)
        if rel is None: continue
        chk = abs(mp.fsum(c * x for c, x in zip(rel, u)))
        scale = max(abs(x) for x in u)
        if chk < mp.mpf(10) ** -(DPS - 40) * scale and any(rel[2 * k] or rel[2 * k + 1] for k in range(1, d + 1)):
            return d, rel
    return None, None


def load(deg):
    if deg == 5:
        with open(os.path.join(F02, "maps5reps.state.jsonl"), encoding="utf-8") as f:
            return [("rep", json.loads(l)) for l in f if l.strip()]
    with open(os.path.join(F02, f"maps{deg}.json"), encoding="utf-8") as f:
        return [("pq", r) for r in json.load(f)]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("deg", type=int); ap.add_argument("out")
    ap.add_argument("--dmax", type=int, default=2); ap.add_argument("--maxc", type=int, default=40)
    ap.add_argument("--limit", type=int, default=0)
    a = ap.parse_args(); n = a.deg
    rows = load(n)
    if a.limit: rows = rows[:a.limit]
    done = set()
    if os.path.exists(a.out):
        with open(a.out, encoding="utf-8") as f:
            for l in f:
                if l.strip(): done.add(json.loads(l)["idx"])
    with open(a.out, "a", encoding="utf-8") as fo:
        for idx, (kind, r) in enumerate(rows):
            if idx in done: continue
            if kind == "rep": rec = b5.parse_state_map(r)
            else: rec = from_PQ(n, [bm.parse_c(x) for x in r["P"]], [bm.parse_c(x) for x in r["Q"]])
            new, res, step, cond = refine5.refine(n, rec)
            new, res, step, cond = refine5.refine(n, new)
            assert res < mp.mpf(10) ** -(DPS - 30), (idx, mp.nstr(res, 5))
            P, Q, cps, vals = new
            out = {"idx": idx, "datum": r["datum"], "res": mp.nstr(res, 3)}
            for name, sh in (("I1", 0), ("I2", 1)):
                I = invariant_cr(cps, vals, sh)
                d, rel = relation(I, a.dmax, None)
                out[name] = mp.nstr(I, 30); out[name + "_deg"] = d
                out[name + "_rel"] = [int(x) for x in rel] if rel else None
            fo.write(json.dumps(out) + "\n"); fo.flush()
            print(idx, r["datum"], out["I1_deg"], out["I2_deg"], flush=True)


if __name__ == "__main__":
    main()
