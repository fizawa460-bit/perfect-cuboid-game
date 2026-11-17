#!/usr/bin/env python3
"""checks19 / l1.py -- L1 of ANSWER-18: window census for the Lemma-M tower family (the hole of section 4.1).

Family (all slack 0 by Lemma M / lemma T0 of DRAFT-TOWER-17, re-checked by census9.Map: |O| = 2n+4, multiplicity <= 2):
  generators on the square S1 = {0, oo, 1, -1} (curve y^2 = x^3 - x):
    e5p = x((2+i)P), e5m = x((2-i)P)   (degree 5, checks14/cm14.gp)
    e9  = x([3]P)                     (degree 9, division polynomials)
  the same on S2 = {0, oo, i, -i} and S3 = {1, -1, i, -i} by conjugation with octahedral rotations;
  bottom quadratics g_{kl} = M(z^2) with critical values BV[k], BV[l] (15 pairs).
  towers: t10 = e5*o g (30), t18 = e9 o g (15), t25 = e5*(S1) o e5*(S) with S = S2, S3 (8).
p runs over these representatives (generators on S1 only); q runs over the representatives and their 24 rotations
h o q.  Conjugates h o f o h^-1 need not be listed: the source Moebius map is absorbed by T.

Search: census9.search logic (T fixed by 3 label-matched coincidences among FIRST odd points of p, chosen per q' with
the rarest labels in O(q') -- any FIRST points give completeness), chunked
so that large degrees fit in memory.  Complete for the problem window (mixed type, |Omega| <= 4) with FIRST = 6.
Besides the census9 records (T with >= |O(p)| - KEEP coincidences, mp re-check) every pair also reports the largest
numerical coincidence count over all tried T except the type-(0,0) ones (P4 of ANSWER-18: how close to the window
threshold 2 max(a, b) + 1 the family gets).  That maximum is only over the tried T (a lower bound for the true one).
Only bidegrees with |a - b| <= 1 can meet the window: m2 - m1 = |O(q')| - |O(p)| = 2(b - a), so |Omega| >= 2|b - a|,
and (1,3) needs b - a = 1.  Numerically type-(0,0) T are counted, not analysed (only a few samples get the mp check).
Resumable: one line per (bidegree, p) in l1.jsonl.  Parallel over p (process pool); the base maps are built once and
cached (pickle, outside the repository); rotated maps h o q reuse the roots of q (labels permuted), no root finding.
usage (from route-F): python -I wall/checks19/l1.py --bideg 5,10 10,10 ... [--first 6] [--keep 3]
"""
import sys, os, json, itertools, argparse, time, importlib.util
sys.dont_write_bytecode = True
from collections import defaultdict
import numpy as np
import mpmath as mp

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("census9", os.path.join(HERE, "..", "checks9", "census9.py"))
C9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(C9)
mp.mp.dps = 60
I = mp.mpc(0, 1)


# ---------- polynomial helpers (coefficient lists low -> high, mpc) ----------
def padd(a, b):
    n = max(len(a), len(b)); return [(a[i] if i < len(a) else 0) + (b[i] if i < len(b) else 0) for i in range(n)]
def pmul(a, b):
    r = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        if x == 0: continue
        for j, y in enumerate(b): r[i + j] += x * y
    return r
def pscale(a, c): return [c * x for x in a]
def ppow(a, k):
    r = [mp.mpc(1)]
    for _ in range(k): r = pmul(r, a)
    return r
def trim(a):
    a = list(a)
    while len(a) > 1 and abs(a[-1]) < mp.mpf(10) ** -45: a.pop()
    return a


def compose(f, g):
    """(P, Q) of f o g, both given as (P, Q) of the same formal degree convention"""
    P, Q = f; G1, G2 = g
    d = max(len(P), len(Q)) - 1
    def hom(C):
        out = [mp.mpc(0)]
        for k in range(d + 1):
            c = C[k] if k < len(C) else 0
            if c == 0: continue
            out = padd(out, pscale(pmul(ppow(G1, k), ppow(G2, d - k)), c))
        return out
    return trim(hom(P)), trim(hom(Q))


def target(h, f):
    a, b, c, d = h; P, Q = f
    return trim(padd(pscale(P, a), pscale(Q, b))), trim(padd(pscale(P, c), pscale(Q, d)))


def conj(h, hinv, f):
    """h o f o h^-1"""
    return target(h, compose(f, ([hinv[1], hinv[0]], [hinv[3], hinv[2]])))


# ---------- the family ----------
def generators_S1():
    x = [mp.mpc(0), mp.mpc(1)]
    e5p = ([0, -25, 0, 10 + 20 * I, 0, 3 - 4 * I], [-(3 - 4 * I), 0, -(10 + 20 * I), 0, 25])
    e5m = ([mp.conj(mp.mpc(c)) for c in e5p[0]], [mp.conj(mp.mpc(c)) for c in e5p[1]])
    e5p = ([mp.mpc(c) for c in e5p[0]], [mp.mpc(c) for c in e5p[1]])
    # x([3]P) on y^2 = x^3 - x: x - 8 (x^3 - x)(x^6 - 5x^4 - 5x^2 + 1) / psi3^2, psi3 = 3x^4 - 6x^2 - 1
    psi3 = [mp.mpc(c) for c in [-1, 0, -6, 0, 3]]
    num = padd(pmul(x, pmul(psi3, psi3)), pscale(pmul([0, -1, 0, 1], [1, 0, -5, 0, -5, 0, 1]), -8))
    e9 = (trim(num), trim(pmul(psi3, psi3)))
    return {"e5p": e5p, "e5m": e5m, "e9": e9}


R_I = (I, 0, 0, 1); R_I_inv = (-I, 0, 0, 1)                       # z -> i z      : S1 -> S2
R_C = (1, 1, -1, 1); R_C_inv = (1, -1, 1, 1)                      # z -> (1+z)/(1-z): S2 -> S3


def on_square(f, s):
    if s == 1: return f
    f2 = conj(R_I, R_I_inv, f)
    return f2 if s == 2 else conj(R_C, R_C_inv, f2)


def quadratic(k, l):
    """M(z^2) with critical values BV[k] (at 0) and BV[l] (at oo), M(1) generic"""
    c3 = mp.mpc(0.31, 0.77); b1, b2 = C9.BV[k], C9.BV[l]
    if b2 is None: A, Bc, C, D = c3 - b1, b1, 0, 1
    elif b1 is None: A, Bc, C, D = b2, (c3 - b2), 1, 0
    else: A, Bc, C, D = b2 * (c3 - b1), b1 * (b2 - c3), (c3 - b1), (b2 - c3)
    return [mp.mpc(Bc), 0, mp.mpc(A)], [mp.mpc(D), 0, mp.mpc(C)]


def family():
    G = generators_S1(); fam = {}
    fam.update({k: v for k, v in G.items()})
    for nm in ("e5p", "e5m", "e9"):
        for k, l in itertools.combinations(range(6), 2):
            fam["%s_q%d%d" % (nm, k, l)] = compose(G[nm], quadratic(k, l))
    for a in ("e5p", "e5m"):
        for s in (2, 3):
            for b in ("e5p", "e5m"):
                fam["%s_%sS%d" % (a, b, s)] = compose(G[a], on_square(G[b], s))
    return fam


RNG_T = (mp.mpc(0.83, 0.21), mp.mpc(-0.37, 0.12), mp.mpc(0.19, -0.44), mp.mpc(1.07, 0.29))   # generic source Moebius


def make_map(name, f):
    a, b, c, d = RNG_T
    P, Q = compose(f, ([b, a], [d, c]))
    return C9.Map(P, Q, name)


def rotations_mats():
    gens = [(complex(0, 1), 0, 0, 1), (1, 1, -1, 1)]
    def mul(A, B):
        a, b, c, d = A; e, f, g, h = B
        return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
    def key(M):
        a, b, c, d = M; s = max([a, b, c, d], key=abs); M = [x / s for x in M]
        return tuple((round(x.real, 9) + 0.0, round(x.imag, 9) + 0.0) for x in map(complex, M))
    G = {key((1, 0, 0, 1)): (1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        nf = []
        for g in fr:
            for s in gens:
                h = mul(s, g); k = key(h)
                if k not in G: G[k] = h; nf.append(h)
        fr = nf
    assert len(G) == 24
    return [tuple(mp.mpc(complex(x)) for x in M) for M in G.values()]


# ---------- search ----------
def search_pair(p, q, first, keep, chunk_rows, zero, sample=3):
    """census9.search for one pair, chunked; returns (records dict, best mixed numerical count).
    T that are numerically of type (0,0) (every point of O(p) and O(q') matched) are only counted in the set ZERO;
    the first SAMPLE of them per task get the full mp analysis (Theorem U check), the rest are not analysed.
    Every other T with >= |O(p)| - KEEP coincidences gets the full mp analysis (so no window record is skipped)."""
    k1 = len(p.O); recs = {}; best = 0
    byl = defaultdict(list)
    for jj, l in enumerate(q.Lnp): byl[l].append(jj)
    # any FIRST points of O(p) will do (m1 + h <= 3 leaves >= 3 label-matched common points among any 6);
    # take those whose label has the fewest candidates in O(q'), to keep the number of triples small
    pick = sorted(range(k1), key=lambda i: (len(byl[p.Lnp[i]]), i))[:min(first, k1)]
    trip = list(itertools.combinations(pick, 3))
    src = []
    for t in trip:
        for tgt in itertools.product(*[byl[p.Lnp[i]] for i in t]):
            if len(set(tgt)) == 3: src.append((t, tgt))
    x = p.Onp[None, :]; u = q.Onp[None, None, :]
    for s0 in range(0, len(src), chunk_rows):
        part = src[s0:s0 + chunk_rows]
        Z = np.array([[p.Onp[i] for i in t] for t, _ in part]); W = np.array([[q.Onp[j] for j in tg] for _, tg in part])
        z1, z2, z3 = Z[:, 0:1], Z[:, 1:2], Z[:, 2:3]; w1, w2, w3 = W[:, 0:1], W[:, 1:2], W[:, 2:3]
        cn = (x - z1) * (z2 - z3); cd = (x - z3) * (z2 - z1)
        with np.errstate(all="ignore"):
            w = (cn * w3 * (w2 - w1) - cd * w1 * (w2 - w3)) / (cn * (w2 - w1) - cd * (w2 - w3))
            dd = np.abs(w[:, :, None] - u) / np.sqrt((1 + np.abs(w[:, :, None]) ** 2) * (1 + np.abs(u) ** 2))
        dd = np.nan_to_num(dd, nan=1.0)
        cnt = (dd.min(axis=2) < C9.TOL_NUM).sum(axis=1)
        full = (cnt == k1) & (len(q.O) == k1)            # numerically type (0,0): excluded from the 'best mixed'
        mixed_cnt = np.where(full, 0, cnt)
        if len(mixed_cnt): best = max(best, int(mixed_cnt.max()))
        for idx in np.nonzero(cnt >= k1 - keep)[0]:
            t, tgt = part[idx]
            M = C9.mob_from_triples([p.O[i][0] for i in t], [q.O[j][0] for j in tgt])
            nm = M / max(abs(M[r, c]) for r in range(2) for c in range(2))
            ph = nm[0, 0] / abs(nm[0, 0]) if abs(nm[0, 0]) > 1e-3 else nm[0, 1] / abs(nm[0, 1])
            nm = nm / ph
            key = (q.name,) + tuple((round(float(nm[r, c].real), 6) + 0.0, round(float(nm[r, c].imag), 6) + 0.0)
                                    for r in range(2) for c in range(2))
            if key in recs or key in zero: continue
            if full[idx]:
                zero.add(key)
                if len(zero) > sample: continue
            recs[key] = C9.analyse(p, q, M)
    return recs, best


def rotate_map(m, h, ri):
    """h o m without root finding: the points of m over BV[k] lie over h(BV[k]) for h o m"""
    perm = []
    for k, bv in enumerate(C9.BV):
        a, b, c, d = h
        if bv is None: img = None if abs(c) < 1e-30 else a / c
        else:
            den = c * bv + d; img = None if abs(den) < 1e-30 else (a * bv + b) / den
        perm.append(min(range(6), key=lambda j: float(C9.chord(img, C9.BV[j]))))
    assert sorted(perm) == list(range(6))
    r = C9.Map.__new__(C9.Map)
    r.P, r.Q = target(h, (m.P, m.Q)); r.name = "%s_r%02d" % (m.name, ri); r.n = m.n
    r.pre = [None] * 6
    for k in range(6): r.pre[perm[k]] = m.pre[k]
    r.O = [(z, k) for k in range(6) for z, mu in r.pre[k] if mu == 1]
    r.crit = [(z, k) for k in range(6) for z, mu in r.pre[k] if mu == 2]
    r.Onp = np.array([complex(z) for z, _ in r.O]); r.Lnp = np.array([C9.LAB[k] for _, k in r.O])
    return r


_W = {}


def to_plain(m): return (m.name, m.n, m.P, m.Q, m.pre)


def from_plain(t):
    r = C9.Map.__new__(C9.Map)
    r.name, r.n, r.P, r.Q, r.pre = t
    r.O = [(z, k) for k in range(6) for z, mu in r.pre[k] if mu == 1]
    r.crit = [(z, k) for k in range(6) for z, mu in r.pre[k] if mu == 2]
    r.Onp = np.array([complex(z) for z, _ in r.O]); r.Lnp = np.array([C9.LAB[k] for _, k in r.O])
    return r


def winit(base, first, keep, chunk):
    _W["base"] = {t[0]: from_plain(t) for t in base}; _W["args"] = (first, keep, chunk); _W["q"] = {}
    _W["rot"] = rotations_mats()


def qlist(b):
    if b not in _W["q"]:
        _W["q"][b] = [rotate_map(m, h, ri) for m in _W["base"].values() if m.n == b for ri, h in enumerate(_W["rot"])]
    return _W["q"][b]


def work(task):
    (da, db), pname = task
    first, keep, chunk = _W["args"]; p = _W["base"][pname]
    t1 = time.time(); recs = {}; best = 0; bestq = None; zero = set()
    Qs = qlist(db)
    for q in Qs:
        r, bst = search_pair(p, q, first, keep, chunk, zero)
        recs.update(r)
        if bst > best: best, bestq = bst, q.name
    R = list(recs.values())
    mixed = [r for r in R if (r["m1"], r["m2"]) != (0, 0)]
    window = [r for r in mixed if r["omega"] <= 4]
    return dict(bidegree=[da, db], p=p.name, first=first, keep=keep, q_maps=len(Qs),
                records=len(R), numeric_type00=len(zero), typeU=sum(1 for r in R if r["thmU"]), typeU_all=all(r["thmU"] for r in R if r["thmU"] is not None),
                mixed=len(mixed), window=len(window),
                window_list=[dict(q=r["q"].name, m1=r["m1"], m2=r["m2"], h=r["h"], omega=r["omega"], genus=r["genus"], bdeg=r["bdeg"]) for r in window],
                mixed_types=sorted({(r["m1"], r["m2"], r["h"], r["omega"]) for r in mixed}),
                mixed_min_omega=min([r["omega"] for r in mixed], default=None),
                best_mixed_numeric_count=best, best_q=bestq, O_p=len(p.O), threshold=2 * max(da, db) + 1,
                worst=max([r["worst"] for r in R], default=0.0), gap=min([r["gap"] for r in R], default=1.0),
                seconds=round(time.time() - t1, 1))


def main():
    import pickle
    from concurrent.futures import ProcessPoolExecutor, as_completed
    ap = argparse.ArgumentParser()
    ap.add_argument("--bideg", nargs="+", required=True)
    ap.add_argument("--first", type=int, default=6)
    ap.add_argument("--keep", type=int, default=3)
    ap.add_argument("--chunk", type=int, default=4000)
    ap.add_argument("--workers", type=int, default=10)
    ap.add_argument("--cache", default=os.path.join(HERE, "..", "..", "..", "..", "..", "..", "..", "..", "route_f_work", "l1_family.pkl"))
    ap.add_argument("--out", default=os.path.join(HERE, "l1.jsonl"))
    a = ap.parse_args()
    done = set()
    if os.path.exists(a.out):
        for l in open(a.out):
            if l.strip():
                r = json.loads(l); done.add((tuple(r["bidegree"]), r["p"], r["first"], r["keep"]))
    t0 = time.time()
    if os.path.exists(a.cache):
        base = pickle.load(open(a.cache, "rb"))
    else:
        base = [to_plain(make_map(nm, f)) for nm, f in family().items()]
        os.makedirs(os.path.dirname(a.cache), exist_ok=True)
        with open(a.cache + ".tmp", "wb") as f: pickle.dump(base, f)
        os.replace(a.cache + ".tmp", a.cache)
    bydeg = defaultdict(list)
    for t in base: bydeg[t[1]].append(t[0])
    print("family:", {d: len(v) for d, v in sorted(bydeg.items())}, "ready in", round(time.time() - t0, 1), "s", flush=True)
    tasks = []
    for bd in a.bideg:
        da, db = map(int, bd.split(","))
        tasks += [((da, db), nm) for nm in bydeg[da] if ((da, db), nm, a.first, a.keep) not in done]
    with ProcessPoolExecutor(a.workers, initializer=winit, initargs=(base, a.first, a.keep, a.chunk)) as ex:
        futs = [ex.submit(work, t) for t in tasks]
        for fu in as_completed(futs):
            row = fu.result()
            print(json.dumps(row), flush=True)
            with open(a.out, "a") as f: f.write(json.dumps(row) + "\n")


if __name__ == "__main__":
    main()
