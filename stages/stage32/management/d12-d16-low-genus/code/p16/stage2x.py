"""32R-69m stage 2 (replaces the union-of-conjugates jobs of stage2.py): for every heavy fibre factor f (per fibre
>= h, see stage2.py) one member F0 - w F1 with w a root of f: over F_p for deg f = 1, over F_p(w), minpoly f, for
deg f >= 2 (all conjugate members have the same genus).  Fast genus tail on that degree-16 member.
usage (from stoll/, after stage2.py): python p16/stage2x.py -> p16/sx_<i>_<t>_<j>.sing, p16/sxjobs.txt"""
import json, re
NL = chr(10)
plan = json.load(open("p16/plan.json")); st = json.load(open("p16/stage2.json"))
FAST = open("gfast/tail_fast.sing").read()
jobs = []
for i, s in st.items():
    for t, d in enumerate(s["decs"]):
        if not isinstance(d, dict): continue
        src = open(f"p16/c_{i}_{t}.sing").read(); k = src.index('system("random", 2718);')
        pre = src[:k] + src[k:].split(NL, 1)[0] + NL
        D = plan[i]["decs"][t][1]
        cids = sorted(int(x) for x in D if int(x) <= 92)
        dc = ("intersect(" + ",".join(f"G{x}" for x in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
        for j, (deg, L, fac) in enumerate(d["heavy"]):
            body = pre + f"ideal Dc = std({dc});" + NL
            if deg == 1:
                body += f"ring RQ = 10009,(u),dp; poly qq = {fac}; matrix CQ = coeffs(qq, u); setring R;" + NL
                body += "poly NN = number(imap(RQ, CQ)[2, 1]) * F0 + number(imap(RQ, CQ)[1, 1]) * F1;" + NL
            else:
                body += f"poly NN = F0 - ww * F1;" + NL
            body += 'ideal B = std(S + ideal(NN)); def LL = sat(B, Dc); ideal Bp; if (typeof(LL) == "list") { Bp = std(LL[1]); } else { Bp = std(LL); } kill LL;' + NL
            body += f'"heavy member: factor degree {deg}, per fibre {L}; residual dim", dim(Bp), " degree", mult(Bp), " expected 16";' + NL
            body += 'if (mult(Bp) < 16) { "MEMBER-REDUCIBLE (contains a D-curve)"; quit; }' + NL
            body += 'if (dim(Bp) != 2) { "MEMBER-NOT-CURVE"; quit; }' + NL + FAST
            if deg >= 2:
                mp = fac.replace("u", "ww")
                body = re.sub(r"ring (\w+) = 10009,(\([^)]*\)),dp;", lambda mm: f"ring {mm.group(1)} = (10009,ww),{mm.group(2)},dp; minpoly = {mp};", body)
            nm = f"sx_{i}_{t}_{j}"; open(f"p16/{nm}.sing", "w", newline=NL).write(body); jobs.append((deg, nm))
jobs.sort()
open(__import__("os").environ.get("SXOUT", "p16/sxjobs.txt"), "w", newline=NL).write(NL.join(n for _, n in jobs) + NL)
from collections import Counter
print(len(jobs), sorted(Counter(dg for dg, _ in jobs).items()))
