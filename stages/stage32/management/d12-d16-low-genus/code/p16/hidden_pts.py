"""32R-69j: pencils whose hidden set H (finite, off the 48 nodes) is non-empty.  A point q of H lies on D-curves,
so F0(q) = F1(q) = 0 says nothing; instead the moving parts R_u = sat(S + (F0 - u F1), D-curves) (u a variable)
are intersected with H: if q is not a base point of the moving part, exactly the members u with q in R_u pass
through q -> special factors for stage 2 (fast genus on those members).  A moving base point in H is reported."""
import json, re, sys
sys.path.insert(0, "fasth0")
from script_v2 import _g
CURVES = _g["CURVES"]
NL = chr(10)
plan = json.load(open("p16/plan.json")); jobs = []
for i, p in plan.items():
    t = open(f"p16/h_{i}.out").read()
    md = re.search(r"dim (-?\d+)", t)
    if "no hidden" in t or int(md.group(1)) <= 0: continue
    src = open(f"p16/c_{i}_0.sing").read()
    pre = src[:src.index('system("random", 2718);')] + src[src.index('system("random", 2718);'):].split(NL, 1)[0] + NL
    L = [pre + "ideal NODES = std(S + minor(jacob(S), 4));"]; parts = []
    for tt, (m, D, hid) in enumerate(p["decs"]):
        if len(hid) > 1:
            L.append(f"ideal U{tt} = intersect(" + ",".join(f"std(S + ideal({','.join(CURVES[k-1])}))" for k in hid) + ");")
        else:
            L.append(f"ideal U{tt} = std(S + ideal({','.join(CURVES[hid[0]-1])}));")
        parts.append(f"U{tt}")
    L.append("ideal HH = std(" + " + ".join(parts) + ");")
    L.append('def LL = sat(HH, NODES); ideal H2; if (typeof(LL) == "list") { H2 = std(LL[1]); } else { H2 = std(LL); }')
    L.append('H2 = std(radical(H2)); "hidden points: degree", mult(H2);')
    m0, D0, _ = p["decs"][0]
    cids = sorted(int(k) for k in D0 if int(k) <= 92)
    dc = ("intersect(" + ",".join(f"G{k}" for k in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
    L.append(f"ideal Dc = std({dc});")
    L.append("ring RU = 10009,(a1,a2,a3,b1,b2,b3,c,u),dp; ideal SU = imap(R, S); poly FU0 = imap(R, F0); poly FU1 = imap(R, F1); ideal DcU = imap(R, Dc); ideal H2U = imap(R, H2);")
    L.append('def LU = sat(std(SU + ideal(FU0 - u * FU1)), DcU); ideal RF; if (typeof(LU) == "list") { RF = std(LU[1]); } else { RF = std(LU); }')
    L.append('ideal RHall = std(RF + H2U); ideal RH = std(RHall + ideal(a1 + 3*a2 + 5*a3 + 7*b1 + 11*b2 + 13*b3 + 17*c - 1)); ideal RH0 = std(RHall + ideal(a1 + 3*a2 + 5*a3 + 7*b1 + 11*b2 + 13*b3 + 17*c, a2 + 2*a3 + 4*b1 + 8*b2 + 16*b3 + 32*c - 1)); "hidden points on chart hyperplane: dim", dim(RH0); if (dim(RH0) >= 0) { "HIDDEN-CHART"; }');
    L.append(' "members through hidden points (chart): dim", dim(RH), " (0 = finitely many)"; if (dim(RH) >= 1) { "HIDDEN-MOVING-BASEPOINT"; quit; }')
    L.append('ideal EU = eliminate(RH, a1*a2*a3*b1*b2*b3*c); "hidden fibre values:", EU;')
    L.append('if (size(EU) > 0) { list FA = factorize(EU[1]); int kk; for (kk = 2; kk <= size(FA[1]); kk++) { "  special factor:", FA[1][kk]; } }')
    L.append("quit;")
    open(f"p16/hp_{i}.sing", "w", newline=NL).write(NL.join(L) + NL); jobs.append(f"hp_{i}")
open("p16/hpjobs.txt", "w", newline=NL).write(NL.join(jobs) + NL); print(len(jobs))
