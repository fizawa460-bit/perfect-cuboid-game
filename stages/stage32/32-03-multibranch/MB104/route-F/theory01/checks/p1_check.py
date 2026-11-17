"""Prediction P1 of ROUTE-F-THEORY-01 (part T): for the birational (4,4) configurations at omega = 14
(f02/extremal4x4_om14.json), does T transfer a symmetry?

G(p) = { Moebius sigma : p o sigma = g o p for some g in the 24 Moebius symmetries of B }.
A configuration (p1, q, T) with p2 = q o T (T maps the O-points of p1 to those of q) is of type (T) when
T o s1 = s2 o T (projectively) for some nontrivial s1 in G(p1) and s2 in G(q).
Each configuration is also given its F02-SHAPE class (1 shared left factor / 2,3 symmetry / 4 none), recomputed
with extremal_struct.py.

Resumable: the per-map groups and the per-pair classes are cached in p1_cache.json next to this script
(git-ignored); delete them to recompute.
usage: python -I -O p1_check.py      (about 10-20 minutes on 11 workers)
"""
import itertools, json, os, sys
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02"))
sys.path.insert(0, F02)
os.environ["EXT_N"] = "4"
import mpmath as mp
import extremal_struct as ES
import analyze_extremal as AE
mp.mp.dps = 45
TOL = mp.mpf(10) ** -15
G = None


def grp():
    global G
    if G is None: G = ES.FO["group"]()
    return G


def gaut(i):
    """G(p) for map i: list of (sigma, index of g)"""
    P, Q = ES.maps()[i]
    cps = AE.crit(P, Q); vals = [AE.peval(P, Q, c) for c in cps]
    out = []
    for gi, g in enumerate(grp()):
        gv = [AE.mob(g, v) for v in vals]
        for tri in itertools.permutations(range(len(cps)), 3):
            if not all(AE.same_pt(vals[t], gv[k], TOL) for k, t in enumerate(tri)): continue
            S = AE.mob3([cps[0], cps[1], cps[2]], [cps[t] for t in tri])
            if all(AE.same_pt(AE.peval(P, Q, AE.mob(S, z)), AE.mob(g, AE.peval(P, Q, z)), TOL) for z in AE.TESTS):
                if not any(proj_eq(S, T) for T, _ in out): out.append((S, gi))
    return i, out


def proj_eq(A, B):
    sc = max(max(abs(x) for x in A), max(abs(x) for x in B))
    return all(abs(A[k] * B[m] - A[m] * B[k]) < TOL * sc * sc for k in range(4) for m in range(4))


def mul(A, B):
    a, b, c, d = A; e, f, g, h = B
    return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)


def order(S):
    M = S
    for k in range(1, 49):
        if proj_eq(M, (1, 0, 0, 1)): return k
        M = mul(M, S)
    return None


def ser(S): return [[mp.nstr(mp.re(mp.mpc(x)), 40), mp.nstr(mp.im(mp.mpc(x)), 40)] for x in S]


def deser(S): return tuple(mp.mpc(mp.mpf(a), mp.mpf(b)) for a, b in S)


def job(k):             # one pool for everything: ("m", i) -> G(p) and left factors; ("p", (ia, ib)) -> symmetry
    kind, x = k[0], k[1:]
    if kind == "m":
        x = x[0]
        _, ga = gaut(x); _, lf = ES.lf(x)
        return k, dict(g=[(ser(S), gi) for S, gi in ga], lf=sorted(map(list, lf)))
    return k, ES.sym(tuple(x))[1]


def run_jobs(keys):
    path = os.path.join(HERE, "p1_cache.json")
    have = {}
    if os.path.exists(path):
        have = {tuple(json.loads(k)): v for k, v in json.load(open(path)).items()}
    def save(): json.dump({json.dumps(k): v for k, v in have.items()}, open(path, "w"))
    todo = [k for k in keys if k not in have]
    if todo:
        with Pool(11) as p:
            for n, (k, v) in enumerate(p.imap_unordered(job, todo, chunksize=2)):
                have[tuple(k)] = v
                if n % 50 == 49: save()
        save()
    return have


def opts(rec):          # O-points (affine, mp.inf allowed) of map i, in the order used by f02
    return [mp.inf if abs(x[1]) < mp.mpf(10) ** -40 else x[0] / x[1] for x, _ in rec]


if __name__ == "__main__":
    top = json.load(open(os.path.join(F02, "extremal4x4_om14.json")))
    need = sorted({e["ia"] for e in top} | {e["ib"] for e in top})
    pairs = sorted({(e["ia"], e["ib"]) for e in top})
    H = run_jobs([("m", i) for i in need] + [("p",) + tuple(pr) for pr in pairs])
    GA = {i: [(deser(S), gi) for S, gi in H[("m", i)]["g"]] for i in need}
    LF = {i: {tuple(map(tuple, x)) for x in H[("m", i)]["lf"]} for i in need}
    SY = {tuple(pr): H[("p",) + tuple(pr)] for pr in pairs}
    import recheck_amb as RA
    RA._rinit(4, 4)
    A, Bq = RA._R["A_mp"], RA._R["B_mp"]
    res = Counter(); detail = Counter(); rows = []
    for e in top:
        ia, ib = e["ia"], e["ib"]
        cls = "1" if LF[ia] & LF[ib] else "2" if "abe" in SY[(ia, ib)] else "3" if SY[(ia, ib)] else "4"
        X1, Xq = opts(A[ia]), opts(Bq[ib])
        co = e["co"]
        T = AE.mob3([X1[c[0]] for c in co[:3]], [Xq[c[1]] for c in co[:3]])
        assert all(AE.same_pt(AE.mob(T, X1[c[0]]), Xq[c[1]], mp.mpf(10) ** -20) for c in co), "T does not fit"
        hits = []
        for s1, g1 in GA[ia]:
            o1 = order(s1)
            if o1 == 1: continue
            for s2, g2 in GA[ib]:
                if proj_eq(mul(T, s1), mul(s2, T)):
                    coinc = {c[0] for c in co}
                    inv = {i for i in coinc if any(AE.same_pt(AE.mob(s1, X1[i]), X1[k], mp.mpf(10) ** -20) for k in coinc)} == coinc
                    hits.append((o1, inv))
        typ = "T" if hits else "-"
        res[(cls, tuple(e["exact"][1:]), typ)] += 1
        if hits: detail[(cls, tuple(e["exact"][1:]), max(h[0] for h in hits), any(h[1] for h in hits))] += 1
        rows.append(dict(ia=ia, ib=ib, jh=e["exact"][1:], cls=cls, T=typ, orders=sorted({h[0] for h in hits}),
                         gsize=(len(GA[ia]), len(GA[ib]))))
    json.dump(rows, open(os.path.join(HERE, "p1_rows.json"), "w"))
    print("configurations:", len(top), " |G(p)| of maps involved:", dict(Counter(len(GA[i]) for i in need)))
    print("class x (j,h) x transfer:")
    for k, v in sorted(res.items()): print("  ", k, v)
    print("transfer detail (class, (j,h), max order, coincidence set invariant):")
    for k, v in sorted(detail.items()): print("  ", k, v)
    print("class-4 without transfer, |G| pairs:",
          dict(Counter(r["gsize"] for r in rows if r["cls"] == "4" and r["T"] == "-")))
