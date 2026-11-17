"""Cross-tabulate the extremal (4,4) configurations (extremal4x4.json) by Aut sizes, shared left factor,
q == p1 and branch data. usage: python -I -O extremal_crosstab.py"""
import json, os, sys
from collections import Counter
from multiprocessing import Pool
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import analyze_extremal as AE
import build_maps as BM
D = json.load(open(os.path.join(HERE, "maps4.json")))
def info(i):
    P = [BM.parse_c(c) for c in D[i]["P"]]; Q = [BM.parse_c(c) for c in D[i]["Q"]]
    A, _, _ = AE.aut(P, Q)
    return i, len(A), [tuple((round(w.real, 8), round(w.imag, 8)) for w in x) for x in AE.left_factors(P, Q, A)]
if __name__ == "__main__":
    top = json.load(open(os.path.join(HERE, "extremal4x4.json")))
    need = sorted({e["ia"] for e in top} | {e["ib"] for e in top})
    with Pool(11) as p: inf = {i: (n, set(lf)) for i, n, lf in p.map(info, need)}
    c = Counter()
    for e in top:
        a1, l1 = inf[e["ia"]]; a2, l2 = inf[e["ib"]]
        c[(tuple(sorted((a1, a2))), bool(l1 & l2), e["ia"] == e["ib"],
           tuple(sorted((D[e["ia"]]["datum"], D[e["ib"]]["datum"]))) if not (l1 & l2) else "-")] += 1
    for k, v in sorted(c.items(), key=lambda x: (-x[1])): print(v, k)
    print("maps involved:", len(need), " aut of involved:", Counter(inf[i][0] for i in need))
