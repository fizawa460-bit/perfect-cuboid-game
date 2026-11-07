"""32R-69i node analysis for pencils (h0 = 2) with nodes k where m_k = x.E_k >= 2.
Blow-up chart at the node (two random charts), moving part of the pencil restricted to E_k (closure Ym of the
strict transforms minus the fixed D-curve points), special t-values = branch values of Ym -> A1_t (a member meeting
E_k with multiplicity >= 2 at a point, the only way a member can be singular on E_k) and t-values where the moving
part meets a fixed point.  Uses decomposition 0 and the same random pencil basis as c_<i>_0.sing.
usage (from stoll/): python p16/node_jobs.py -> p16/n_<i>_<k>_<chart>.sing, p16/njobs.txt"""
import json, sys
import numpy as np
sys.path.insert(0, "fasth0")
from script_v2 import _g
POINTS, NOL, Pn = _g["POINTS"], _g["node_of_label"], np.array(_g["L"].D["Pn"], dtype=object)
plan = json.load(open("p16/plan.json")); prof = json.load(open("fasth0/d16_pencil_profile.json"))
jobs = []
for i, p in plan.items():
    if prof[i]["mmax"] < 2: continue
    src = open(f"p16/c_{i}_0.sing").read()
    pre = src[:src.index('system("random", 2718);')] + src[src.index('system("random", 2718);'):].split("\n", 1)[0] + "\n"
    m, D, hid = p["decs"][0]
    cids = sorted(int(k) for k in D if int(k) <= 92)
    dc = ("intersect(" + ",".join(f"G{k}" for k in cids) + ")") if len(cids) > 1 else (f"G{cids[0]}" if cids else "ideal(1)")
    for k in prof[i]["m2"]:
        for ch, seed in ((1, 1111), (2, 2222)):
            s = pre + f"ideal Dc = std({dc});\n"
            s += f"ideal PK = std(ideal({POINTS[NOL[k]]}));\n"
            s += "int j0 = 0; int ii; ideal QPK; for (ii = 1; ii <= 7; ii++) { QPK = std(PK + ideal(var(ii) - 1)); if (QPK[1] != 1) { j0 = ii; break; } }\n"
            s += "ideal CS = reduce(maxideal(1), QPK);\n"
            s += f'"node {k} chart {ch}: j0", j0;\n'
            s += "ring RB = 10009,(s,v2,v3,v4,v5,v6,tt),dp;\n"
            s += f"system(\"random\", {seed}); matrix AA[6][6]; int r1; int r2; for (r1 = 1; r1 <= 6; r1++) {{ for (r2 = 1; r2 <= 6; r2++) {{ AA[r1, r2] = random(1, 9999); }} }}\n"
            s += "ideal WW = s, s*v2, s*v3, s*v4, s*v5, s*v6; ideal CSB = imap(R, CS); ideal IMG; int rr = 0;\n"
            s += "for (ii = 1; ii <= 7; ii++) { if (ii == j0) { IMG[ii] = 1; } else { rr++; IMG[ii] = CSB[ii]; for (r2 = 1; r2 <= 6; r2++) { IMG[ii] = IMG[ii] + AA[rr, r2] * WW[r2]; } } }\n"
            s += "map PHI = R, IMG;\n"
            s += "proc satB(ideal I, ideal Q) { def T = sat(I, Q); ideal R2; if (typeof(T) == \"list\") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }\n"
            s += "ideal IS = satB(std(PHI(S)), ideal(s)); ideal EE = std(IS + ideal(s)); \"E x A1: dim\", dim(EE), \" (expect 2)\";\n"
            s += "poly GG = PHI(F0) - tt * PHI(F1); ideal JY = satB(std(IS + ideal(GG)), ideal(s)); ideal YY = std(JY + ideal(s));\n"
            s += "ideal DF = std(satB(std(IS + PHI(Dc)), ideal(s)) + ideal(s));\n"
            s += "ideal YM = YY; if (dim(DF) >= 0) { YM = satB(YY, DF); }\n"
            s += '"moving part on E: dim", dim(YM), " (expect 1)"; if (dim(YM) != 1) { "NODE-OPEN: moving part not a curve over t"; quit; }\n'
            s += "ideal YF = std(YM + DF); \"moving part meets fixed points: dim\", dim(YF); if (dim(YF) >= 1) { \"NODE-OPEN: base point on E\"; quit; }\n"
            s += "matrix JJ[ncols(YM)][6]; for (r1 = 1; r1 <= ncols(YM); r1++) { for (r2 = 1; r2 <= 6; r2++) { JJ[r1, r2] = diff(YM[r1], var(r2)); } }\n"
            s += "ideal RRM = std(YM + minor(JJ, 6)); \"ramification scheme: dim\", dim(RRM); if (dim(RRM) >= 1) { \"NODE-OPEN: ramification not finite\"; quit; }\n"
            s += 'ideal FB = std(YM + ideal(tt - 1234)); "generic fibre length on E", vdim(FB), " reduced", vdim(std(radical(FB)));\n'
            s += 'ideal SP = intersect(RRM, YF); ideal ET = eliminate(SP, s*v2*v3*v4*v5*v6); "special t:", ET;\n'
            s += "if (size(ET) == 0) { \"NODE-NONE\"; quit; }\n"
            s += "list FT = factorize(ET[1]); int kk; for (kk = 2; kk <= size(FT[1]); kk++) { \"  special factor:\", FT[1][kk]; }\nquit;\n"
            nm = f"n_{i}_{k}_{ch}"; open(f"p16/{nm}.sing", "w", newline="\n").write(s); jobs.append(nm)
open("p16/njobs.txt", "w", newline="\n").write("\n".join(jobs) + "\n"); print(len(jobs))
