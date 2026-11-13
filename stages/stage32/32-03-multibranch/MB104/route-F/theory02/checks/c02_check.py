"""Claude's check of ROUTE-F-THEORY-02 on the repository map data (mpmath), predictions P5 and P6.

P5 (degree 4): for the 6,144 type-(H) configurations of CHECK-01 (rows of theory01 p1_rows.json that are class 4,
   no transfer, no shared left factor after g):
   (i)  the critical values of p1 form an "edge-type" 4-set B' (not a square);
   (ii) q o S = h o p1 with h = g o k, g a symmetry of B and k an involution swapping the points of B' in pairs;
   also: pairs per map (is 192 = 48 maps x 4 partners?).
   (THEORY-02's item (iii), S iota S^-1 in Aut(q), holds automatically when q o S = h o p1, so it is not tested.)
P6 (degree 3): for every degree-3 map whose critical values form an edge-type B', and every involution k of B'
   that is not a symmetry of B: is k o p = p o sigma for a Moebius sigma?
usage: python -I -O c02_check.py > c02_check.out
"""
import itertools, json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
T01 = os.path.normpath(os.path.join(HERE, "..", "..", "theory01", "checks"))
sys.path.insert(0, T01)
import p1_check as P1
AE = P1.AE; mp = P1.mp; ES = P1.ES; BM = ES.BM
G = ES.FO["group"]()
TOL = mp.mpf(10) ** -15
SQUARES = [{"0", "oo", "1", "-1"}, {"0", "oo", "I", "-I"}, {"1", "-1", "I", "-I"}]
BP = dict(zip(AE.BNAME, AE.BPTS))


def lab(v):
    for k, b in BP.items():
        if AE.same_pt(v, b, TOL): return k
    return None


def critvals(P, Q):
    return {lab(AE.peval(P, Q, c)) for c in AE.crit(P, Q)}


def is_sym(h):
    return all(any(AE.same_pt(AE.mob(h, b), c, TOL) for c in AE.BPTS) for b in AE.BPTS)


def involutions(Bp):
    """the 3 Moebius involutions swapping the 4 points of Bp in pairs"""
    a, b, c, d = [BP[x] for x in sorted(Bp)]
    return [AE.mob3([a, b, c], [b, a, d]), AE.mob3([a, b, c], [c, d, a]), AE.mob3([a, b, c], [d, c, b])]


def find_h(ia, ib):
    P, Q = ES.maps()[ia]; Pq, Qq = ES.maps()[ib]
    c1 = AE.crit(P, Q); cq = AE.crit(Pq, Qq)
    v1 = [AE.peval(P, Q, z) for z in c1]; vq = [AE.peval(Pq, Qq, z) for z in cq]
    out = []
    for tri in itertools.permutations(range(6), 3):
        S = AE.mob3(c1[:3], [cq[t] for t in tri])
        if not all(any(AE.same_pt(AE.mob(S, z), w, TOL) for w in cq) for z in c1): continue
        img = [next(k for k, w in enumerate(cq) if AE.same_pt(AE.mob(S, z), w, TOL)) for z in c1]
        idx = []
        for k in range(6):
            if not any(AE.same_pt(v1[k], v1[m]) for m in idx): idx.append(k)
        h = AE.mob3([v1[k] for k in idx[:3]], [vq[img[k]] for k in idx[:3]])
        if all(AE.same_pt(AE.peval(Pq, Qq, AE.mob(S, z)), AE.mob(h, AE.peval(P, Q, z)), TOL) for z in AE.TESTS):
            out.append(h)
    return out


def ginv(g):
    a, b, c, d = g
    return (d, -b, -c, a)


if __name__ == "__main__":
    lsrc = open(os.path.join(T01, "l_check.py"), encoding="utf-8").read().split("res = Counter()")[0]
    ls = {"__file__": os.path.join(T01, "l_check.py")}; exec(lsrc, ls)
    rows = json.load(open(os.path.join(T01, "p1_rows.json")))
    H = [x for x in rows if x["cls"] == "4" and x["T"] == "-" and not ls["shared"](x["ia"], x["ib"])]
    pairs = Counter((x["ia"], x["ib"]) for x in H)
    maps = sorted({a for a, _ in pairs} | {b for _, b in pairs})
    print("P5: configurations", len(H), " pairs", len(pairs), " maps", len(maps))
    print("  partners per map (as p1):", dict(Counter(Counter(a for a, _ in pairs).values())),
          " T per pair:", dict(Counter(pairs.values())))
    cv = {i: critvals(*ES.maps()[i]) for i in maps}
    print("  (i) critical-value sets: sizes", dict(Counter(len(v) for v in cv.values())),
          " squares", sum(1 for v in cv.values() if v in SQUARES))
    ok = Counter()
    for (ia, ib), n in pairs.items():
        hs = find_h(ia, ib)
        ks = involutions(cv[ia])
        def decomp(h):
            for g in G:
                k = P1.mul(ginv(g), h)
                if any(P1.proj_eq(k, kk) for kk in ks): return True
            return False
        ok[(len(hs) > 0, all(not is_sym(h) for h in hs), all(decomp(h) for h in hs))] += n
    print("  (ii) (h found, no h is a symmetry, every h = g o k):", dict(ok))

    # P6, degree 3
    import recheck_amb as RA
    RA._rinit(3, 3)
    FO3 = {"__file__": ES.FO["__file__"]}
    src = open(ES.FO["__file__"], encoding="utf-8").read(); exec(src[:src.index("maps = json.load")], FO3); FO3["n"] = 3
    res = Counter()
    for P, Q in RA._R["A_maps"]:
        P = [mp.mpc(x) for x in P]; Q = [mp.mpc(x) for x in Q]
        v = critvals(P, Q)
        if v in SQUARES: res["square (skipped)"] += 1; continue
        rp = FO3["record"](P, Q)
        for k in involutions(v):
            if is_sym(k): continue
            a, b, c, d = k
            P2 = [a * p + b * q for p, q in zip(P, Q)]; Q2 = [c * p + d * q for p, q in zip(P, Q)]
            r2 = FO3["record"](P2, Q2)
            res["k o p = p o sigma" if r2 is not None and BM.key_maps_equal(3, rp, r2) else "FAIL"] += 1
    print("P6 (degree 3, edge-type maps x non-symmetry involutions k of B'):", dict(res))
