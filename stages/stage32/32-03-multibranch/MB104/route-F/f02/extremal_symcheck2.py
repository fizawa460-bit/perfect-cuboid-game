"""Second pass for extremal_symcheck.py: the configurations not explained by the label-preserving group are tested
against the full symmetry group of B (24 Moebius maps, with or without conjugation).
For a hit it reports the permutation of the label classes {a, b, e} that g induces.
usage: python -I -O extremal_symcheck2.py"""
import json, os, sys
from collections import Counter
from multiprocessing import Pool
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import extremal_symcheck as S1
import extremal_crosstab as XT
FO, BM, D, PQ = S1.FO, S1.BM, S1.D, S1.PQ
G = None
def labperm(g):
    pts = {"a": [mp.mpc(0, 1), mp.mpc(0, -1)], "b": [mp.mpc(1), mp.mpc(-1)], "e": [mp.mpc(0), mp.inf]}
    out = {}
    for k, v in pts.items():
        w = FO["mob"](g, v[0])
        for k2, v2 in pts.items():
            if any(FO["close_eq"](w, x) for x in v2): out[k] = k2
    return "".join(out[k] for k in "abe")
def check(pair):
    global G
    if G is None: G = FO["group"]()
    ia, ib = pair
    P, Q = PQ(ia); rq = FO["record"](*PQ(ib)); hits = set()
    for g in G:
        a, b, c, d = g
        for conj in (False, True):
            P2 = [a * p + b * q for p, q in zip(P, Q)]; Q2 = [c * p + d * q for p, q in zip(P, Q)]
            if conj: P2 = [mp.conj(x) for x in P2]; Q2 = [mp.conj(x) for x in Q2]
            r2 = FO["record"](P2, Q2)
            if r2 is not None and BM.key_maps_equal(4, rq, r2): hits.add((labperm(g), conj))
    return pair, sorted(hits)
if __name__ == "__main__":
    top = json.load(open(os.path.join(HERE, "extremal4x4.json")))
    need = sorted({e["ia"] for e in top} | {e["ib"] for e in top})
    with Pool(11) as p:
        inf = {i: set(lf) for i, n, lf in p.map(XT.info, need)}
        rest = [e for e in top if not (inf[e["ia"]] & inf[e["ib"]])]
        pairs = sorted({(e["ia"], e["ib"]) for e in rest})
        res = dict(p.map(check, pairs))
    w = Counter((e["ia"], e["ib"]) for e in rest)
    kinds = Counter()
    for pr, hits in res.items():
        perms = sorted({h[0] for h in hits})
        kinds["none" if not hits else ("label-preserving" if "abe" in perms else "only label-changing: " + ",".join(perms))] += w[pr]
    print(sorted(kinds.items(), key=lambda x: -x[1]))
