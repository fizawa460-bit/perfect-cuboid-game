"""checks13 / cone13.py -- STRATEGY-13b candidate 3, prediction: for a cone point x of tau_p, count the cone points
adjacent to x (tiling distance l_min = 1.5286 <= 1.6).  Prediction: more than half of the cone points have >= 3.
Same maps as bands13 (degree 5: the 7 orbit-representative types, 612 maps; degree 4: all 680), same tau.
usage: python3 -I .../wall/checks13/cone13.py [--workers 4]
"""
import sys, os, io, contextlib, json, argparse
sys.dont_write_bytecode = True
from collections import Counter, defaultdict
from concurrent.futures import ProcessPoolExecutor
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS"): os.environ[_k] = "1"
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import bands13 as B13


def job(args):
    deg, ids = args
    G = B13._G.setdefault("G", B13.defs())
    if ("M", deg) not in B13._G: B13._G[("M", deg)] = dict(B13.items(deg)[0])
    M = B13._G[("M", deg)]; out = []
    for i in ids:
        with contextlib.redirect_stdout(io.StringIO()):
            PP, QQ = G["with_generic_source"](M[i].P, M[i].Q, M[i].n)
            m, verts, arcs, good = G["tau"](PP, QQ)
        cone = {k for k, v in enumerate(verts) if v[2] == 1}
        nb = defaultdict(set)
        for u, v in arcs: nb[u].add(v); nb[v].add(u)
        out.append((i, bool(good), [len(nb[c] & cone) for c in sorted(cone)]))
    return out


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--workers", type=int, default=4); a = ap.parse_args()
    res = {}
    for deg in (4, 5):
        ids = [i for i, _ in B13.items(deg)[0]]
        chunks = [(deg, ids[k:k + 16]) for k in range(0, len(ids), 16)]
        rows = []
        with ProcessPoolExecutor(max_workers=a.workers) as ex:
            for r in ex.map(job, chunks): rows += r
        allc = Counter(c for _, _, cs in rows for c in cs)
        tot = sum(allc.values()); ge3 = sum(v for k, v in allc.items() if k >= 3)
        res[deg] = dict(maps=len(rows), good=sum(g for _, g, _ in rows), cone_points=tot,
                        cone_neighbours=dict(sorted(allc.items())), share_ge3=round(ge3 / tot, 4))
        print(deg, json.dumps(res[deg]), flush=True)
    ok = all(r["share_ge3"] > 0.5 for r in res.values())
    print("prediction (share >= 3 neighbours > 1/2):", "HOLDS" if ok else "FAILS")


if __name__ == "__main__":
    main()
