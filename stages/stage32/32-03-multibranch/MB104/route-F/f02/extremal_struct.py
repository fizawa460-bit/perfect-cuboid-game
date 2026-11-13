"""Structure of the extremal (n,n) configurations (file extremal{n}x{n}.json from analyze_extremal.py).

Each configuration (p1, q, T) with p2 = q o T is put in the first class that applies:
  1. shared left factor : n even, and p1, q have a degree-2 left factor r with the same critical values
                          (p = r o u with u the quotient by an involution in Aut(p); see analyze_extremal.py);
  2. symmetry, label-preserving : q = g o p1 o S for a Moebius S and some g in the symmetry group of B
                          (24 Moebius maps, with or without conjugation) that maps each label class {+-i},{+-1},{0,oo} to itself;
  3. symmetry, label-changing only : as 2, but every such g permutes the label classes;
  4. none.
Exact comparison via build_maps.key_maps_equal (mpmath).
usage: python -I -O extremal_struct.py n [suffix, e.g. _om14]
"""
import json, os, sys
from collections import Counter
from multiprocessing import Pool
import mpmath as mp
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import build_maps as BM
import analyze_extremal as AE
import f02_spectrum as F2
_src = open(os.path.join(HERE, "fill_orbits.py"), encoding="utf-8").read()
FO = {"__file__": os.path.join(HERE, "fill_orbits.py")}
exec(_src[:_src.index("maps = json.load")], FO)      # function definitions only
mp.mp.dps = 45
N = int(sys.argv[1]) if __name__ == "__main__" else int(os.environ.get("EXT_N", "4"))
os.environ["EXT_N"] = str(N)
FO["n"] = N                                          # fill_orbits' helpers read the global n
MAPS = None; G = None


def maps():
    global MAPS
    if MAPS is None: MAPS = F2.maps_of_degree(N)
    return MAPS


def labperm(g):
    pts = {"a": [mp.mpc(0, 1), mp.mpc(0, -1)], "b": [mp.mpc(1), mp.mpc(-1)], "e": [mp.mpc(0), mp.inf]}
    out = {}
    for k, v in pts.items():
        w = FO["mob"](g, v[0])
        for k2, v2 in pts.items():
            if any(FO["close_eq"](w, x) for x in v2): out[k] = k2
    return "".join(out[k] for k in "abe")


def lf(i):
    if N % 2: return i, set()
    P, Q = maps()[i]
    A, _, _ = AE.aut(P, Q)
    return i, {tuple((round(w.real, 8), round(w.imag, 8)) for w in x) for x in AE.left_factors(P, Q, A)}


def sym(pair):
    global G
    if G is None: G = FO["group"]()
    ia, ib = pair
    P, Q = maps()[ia]; rq = FO["record"](*maps()[ib]); hits = set()
    for g in G:
        a, b, c, d = g
        for conj in (False, True):
            P2 = [a * p + b * q for p, q in zip(P, Q)]; Q2 = [c * p + d * q for p, q in zip(P, Q)]
            if conj: P2 = [mp.conj(x) for x in P2]; Q2 = [mp.conj(x) for x in Q2]
            r2 = FO["record"](P2, Q2)
            if r2 is not None and BM.key_maps_equal(N, rq, r2): hits.add(labperm(g))
    return pair, sorted(hits)


if __name__ == "__main__":
    top = json.load(open(os.path.join(HERE, f"extremal{N}x{N}{sys.argv[2] if len(sys.argv) > 2 else ''}.json")))
    need = sorted({e["ia"] for e in top} | {e["ib"] for e in top})
    pairs = sorted({(e["ia"], e["ib"]) for e in top})
    with Pool(11) as p:
        L = dict(p.map(lf, need))
        S = dict(p.map(sym, pairs))
    cls = Counter(); perms = Counter()
    for e in top:
        pr = (e["ia"], e["ib"])
        if L[e["ia"]] & L[e["ib"]]: cls["1 shared left factor"] += 1
        elif "abe" in S[pr]: cls["2 symmetry, label-preserving"] += 1
        elif S[pr]: cls["3 symmetry, label-changing only"] += 1; perms[",".join(S[pr])] += 1
        else: cls["4 none"] += 1
    print(json.dumps(dict(n=N, extremal=len(top), distinct_pairs=len(pairs), maps_involved=len(need),
                          classes=dict(sorted(cls.items())), label_permutations_class3=dict(perms),
                          same_map=sum(1 for e in top if e["ia"] == e["ib"]))))
    jh = Counter()
    for e in top:
        pr = (e["ia"], e["ib"])
        c = ("1" if L[e["ia"]] & L[e["ib"]] else "2" if "abe" in S[pr] else "3" if S[pr] else "4")
        jh[(c, tuple(e["exact"][1:]))] += 1
    print("class x (j,h):", sorted(jh.items()))
    D = None
    try:
        D = [d["datum"] for d in json.load(open(os.path.join(HERE, f"maps{N}.json")))] if N == 4 else None
    except Exception: pass
    none_pairs = sorted({(e["ia"], e["ib"]) for e in top if not (L[e["ia"]] & L[e["ib"]]) and not S[(e["ia"], e["ib"])]})
    print("class-4 pairs (first 12):", none_pairs[:12])
