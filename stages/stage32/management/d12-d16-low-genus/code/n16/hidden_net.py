"""32R-72 hidden points of a net (points on hidden curves of both decompositions 0 and 1, off the nodes; finite).
For each extra decomposition t >= 2 (n16/plan_ext.json): hidden points off supp(D_t) and the members of the net that
are singular there (G_q = moving part times the D_t part, nonzero at the point, so G_q singular <=> C_q singular).
Writes n16/hq_<i>_<t>.sing; each saves the hidden points ON supp(D_t) to hc_<i>_<t>.txt for the cover check."""
import json, sys
sys.path.insert(0, "fasth0")
from script_v2 import script, _g
CURVES = _g["CURVES"]
plan = json.load(open("n16/plan_ext.json")); jobs = []
def U(hid): return "intersect(" + ",".join(f"std(S + ideal({','.join(CURVES[k-1])}))" for k in hid) + ")" if len(hid) > 1 else f"std(S + ideal({','.join(CURVES[hid[0]-1])}))"
for i, p in plan.items():
    if len(p["decs"]) <= 2: continue
    h0 = p["h0"]
    for t in range(2, len(p["decs"])):
        m, D, hid = p["decs"][t]; D = {int(k): v for k, v in D.items()}
        s = script(D, m); s = s[:s.index("ideal B = std(S + Lsys);")]
        s += "ideal SS = std(S); ideal NFL = simplify(reduce(Lsys, SS), 2); \"sections\", ncols(NFL);\n"
        s += "ideal NODES = std(S + minor(jacob(S), 4));\n"
        s += f"ideal U0 = {U(p['decs'][0][2])}; ideal U1 = {U(p['decs'][1][2])};\n"
        s += 'def LL = sat(std(U0 + U1), NODES); ideal H2; if (typeof(LL) == "list") { H2 = std(LL[1]); } else { H2 = std(LL); } kill LL;\n'
        s += '"hidden set: dim", dim(H2), " degree", mult(H2);\n'
        s += 'ideal HC = std(H2 + Iall); "hidden points on supp(D_t): dim", dim(HC), " degree", mult(HC);\n'
        s += f'write(":w hc_{i}_{t}.txt", string(HC));\n'
        s += 'def LT = sat(H2, Iall); ideal HT; if (typeof(LT) == "list") { HT = std(LT[1]); } else { HT = std(LT); } kill LT;\n'
        s += '"hidden points off supp(D_t): dim", dim(HT), " degree", mult(HT);\n'
        pars = "s0,u,v" if h0 == 3 else "s0,u,v,w"
        s += f"ring RN = 10009,(a1,a2,a3,b1,b2,b3,c,{pars}),dp;\n"
        s += "ideal SN = imap(R, S); ideal FN = imap(R, NFL); ideal HN = imap(R, HT); int ii; int jj;\n"
        s += "poly G = 0; for (ii = 1; ii <= ncols(FN); ii++) { G = G + var(7 + ii) * FN[ii]; }\n"
        s += "matrix J[5][7]; for (ii = 1; ii <= 4; ii++) { for (jj = 1; jj <= 7; jj++) { J[ii, jj] = diff(SN[ii], var(jj)); } }\n"
        s += "for (jj = 1; jj <= 7; jj++) { J[5, jj] = diff(G, var(jj)); }\n"
        s += "ideal Z = std(SN + HN + ideal(G) + minor(J, 5));\n"
        s += f"ideal QI = {pars}; ideal PI = a1,a2,a3,b1,b2,b3,c;\n"
        s += 'def L1 = sat(Z, QI); ideal Z1; if (typeof(L1) == "list") { Z1 = std(L1[1]); } else { Z1 = std(L1); } kill L1;\n'
        s += 'def L2 = sat(Z1, PI); ideal Z2; if (typeof(L2) == "list") { Z2 = std(L2[1]); } else { Z2 = std(L2); } kill L2;\n'
        s += '"singular members at hidden points: dim", dim(Z2), " degree", mult(Z2);\n'
        s += 'if (dim(Z2) <= 0) { "NO-MEMBER-SINGULAR-AT-HIDDEN"; } else { "MEMBERS-SINGULAR-AT-HIDDEN"; Z2; }\nquit;\n'
        open(f"n16/hq_{i}_{t}.sing", "w", newline="\n").write(s); jobs.append(f"hq_{i}_{t}")
open("n16/hqjobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n"); print(len(jobs))
