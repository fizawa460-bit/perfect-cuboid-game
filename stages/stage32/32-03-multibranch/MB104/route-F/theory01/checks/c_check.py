"""For the 6,144 (4,4) omega = 14 configurations left by g2_check.py: does T map the critical points of p1 onto the
critical points of q?  (T sends the coincident O-points of p1 to those of q; p2 = q o T.)  If so, record how the
critical values correspond: is there a Moebius h with q(T z) = h(p1(z)) at the critical points?
usage: python -I -O c_check.py > c_check.out
"""
import json, os, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import p1_check as P1
AE = P1.AE; mp = P1.mp; ES = P1.ES
lsrc = open(os.path.join(HERE, "l_check.py"), encoding="utf-8").read().split("res = Counter()")[0]
ls = {"__file__": os.path.join(HERE, "l_check.py")}; exec(lsrc, ls)
top = json.load(open(os.path.join(P1.F02, "extremal4x4_om14.json")))
rows = json.load(open(os.path.join(HERE, "p1_rows.json")))
keep = [i for i, x in enumerate(rows) if x["cls"] == "4" and x["T"] == "-" and not ls["shared"](x["ia"], x["ib"])]
if __name__ == "__main__":
    import recheck_amb as RA
    RA._rinit(4, 4)
    A, Bq = RA._R["A_mp"], RA._R["B_mp"]
    res = Counter(); hits = Counter()
    for k in keep:
        e = top[k]; ia, ib = e["ia"], e["ib"]
        X1, Xq = P1.opts(A[ia]), P1.opts(Bq[ib])
        T = AE.mob3([X1[c[0]] for c in e["co"][:3]], [Xq[c[1]] for c in e["co"][:3]])
        c1 = AE.crit(*ES.maps()[ia]); cq = AE.crit(*ES.maps()[ib])
        m = sum(any(AE.same_pt(AE.mob(T, z), w, mp.mpf(10) ** -15) for w in cq) for z in c1)
        res[m] += 1
        coinc_vals = Counter((c[2], c[3]) for c in e["co"])
        hits[(m, tuple(sorted(coinc_vals.items())))] += 1
    print("configurations:", len(keep))
    print("number of critical points of p1 sent by T to critical points of q:", dict(sorted(res.items())))
    print("(that number, labels of coincident O-points):", dict(hits))
    # are the critical-point sets of p1 and q Moebius-equivalent at all?
    import itertools
    def equiv(ia, ib):
        c1 = AE.crit(*ES.maps()[ia]); cq = AE.crit(*ES.maps()[ib])
        for tri in itertools.permutations(range(6), 3):
            S = AE.mob3(c1[:3], [cq[t] for t in tri])
            if all(any(AE.same_pt(AE.mob(S, z), w, mp.mpf(10) ** -15) for w in cq) for z in c1): return True
        return False
    prs = Counter((top[k]["ia"], top[k]["ib"]) for k in keep)
    eq = Counter(); 
    for pr, n in prs.items(): eq[equiv(*pr)] += n
    print("pairs:", len(prs), " configurations whose critical sets are Moebius-equivalent:", dict(eq))
    print("p1 == q as list entries:", sum(n for pr, n in prs.items() if pr[0] == pr[1]))
    # is q o S = h o p1 for Moebius S, h (h not necessarily a symmetry of B)?  h is fixed by three critical values.
    def posteq(ia, ib):
        P, Q = ES.maps()[ia]; Pq, Qq = ES.maps()[ib]
        c1 = AE.crit(P, Q); cq = AE.crit(Pq, Qq)
        v1 = [AE.peval(P, Q, z) for z in c1]; vq = [AE.peval(Pq, Qq, z) for z in cq]
        out = []
        for tri in itertools.permutations(range(6), 3):
            S = AE.mob3(c1[:3], [cq[t] for t in tri])
            if not all(any(AE.same_pt(AE.mob(S, z), w, mp.mpf(10) ** -15) for w in cq) for z in c1): continue
            img = [next(k for k, w in enumerate(cq) if AE.same_pt(AE.mob(S, z), w, mp.mpf(10) ** -15)) for z in c1]
            vals = [vq[k] for k in img]
            idx = []
            for k in range(6):
                if not any(AE.same_pt(v1[k], v1[m]) for m in idx): idx.append(k)
            idx = idx[:3]
            h = AE.mob3([v1[k] for k in idx], [vals[k] for k in idx])
            if all(AE.same_pt(AE.peval(Pq, Qq, AE.mob(S, z)), AE.mob(h, AE.peval(P, Q, z)), mp.mpf(10) ** -15) for z in AE.TESTS):
                hb = [AE.mob(h, b) for b in AE.BPTS]
                out.append(sum(any(AE.same_pt(x, b) for b in AE.BPTS) for x in hb))
        return out
    pe = Counter()
    for pr, n in prs.items():
        o = posteq(*pr); pe[(bool(o), max(o) if o else None)] += n
    print("q o S = h o p1 for some Moebius h (found, max |h(B) cap B|):", dict(pe))
