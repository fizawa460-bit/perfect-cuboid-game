"""For the extremal (4,4) configurations without a shared degree-2 left factor: is q = g o p1 o S for a Moebius S
and some g in the label-preserving symmetry group of B (z -> +-z, +-1/z, each with or without complex conjugation;
order 8)? Exact comparison via build_maps.key_maps_equal. usage: python -I -O extremal_symcheck.py"""
import json, os, sys
from collections import Counter
from multiprocessing import Pool
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_maps as BM
import extremal_crosstab as XT
_src = open(os.path.join(HERE, "fill_orbits.py"), encoding="utf-8").read()
FO = {"__file__": os.path.join(HERE, "fill_orbits.py")}; exec(_src[:_src.index("maps = json.load")], FO)      # function definitions only (no top-level run)
mp.mp.dps = 45
D = json.load(open(os.path.join(HERE, "maps4.json")))
V = [(1, 0, 0, 1), (-1, 0, 0, 1), (0, 1, 1, 0), (0, -1, 1, 0)]      # z, -z, 1/z, -1/z
def PQ(i): return [BM.parse_c(c) for c in D[i]["P"]], [BM.parse_c(c) for c in D[i]["Q"]]
def check(pair):
    ia, ib = pair
    P, Q = PQ(ia); rq = FO["record"](*PQ(ib))
    hits = []
    for gi, (a, b, c, d) in enumerate(V):
        for conj in (False, True):
            P2 = [a * p + b * q for p, q in zip(P, Q)]; Q2 = [c * p + d * q for p, q in zip(P, Q)]
            if conj: P2 = [mp.conj(x) for x in P2]; Q2 = [mp.conj(x) for x in Q2]
            r2 = FO["record"](P2, Q2)
            if r2 is not None and BM.key_maps_equal(4, rq, r2): hits.append((["z", "-z", "1/z", "-1/z"][gi], conj))
    return pair, hits
if __name__ == "__main__":
    top = json.load(open(os.path.join(HERE, "extremal4x4.json")))
    need = sorted({e["ia"] for e in top} | {e["ib"] for e in top})
    with Pool(11) as p:
        inf = {i: set(lf) for i, n, lf in p.map(XT.info, need)}
        rest = [e for e in top if not (inf[e["ia"]] & inf[e["ib"]])]
        pairs = sorted({(e["ia"], e["ib"]) for e in rest})
        res = dict(p.map(check, pairs))
    w = Counter((e["ia"], e["ib"]) for e in rest)
    c = Counter(); none = 0
    for pr, hits in res.items():
        if hits: c[tuple(sorted(set(h for h in hits)))] += w[pr]
        else: none += w[pr]
    print("configurations without shared left factor:", len(rest), " distinct pairs:", len(pairs))
    for k, v in c.most_common(): print(v, k)
    print("not explained by a label-preserving symmetry:", none)
    un = Counter((e["ia"] == e["ib"], D[e["ia"]]["datum"], D[e["ib"]]["datum"]) for e in rest if not res[(e["ia"], e["ib"])])
    print("unexplained by (same map, datum p1, datum q):", sorted(un.items()))
    sm = Counter((D[e["ia"]]["datum"], bool(res[(e["ia"], e["ib"])])) for e in rest if e["ia"] == e["ib"])
    print("same-map configurations by datum, explained:", sorted(sm.items()))
