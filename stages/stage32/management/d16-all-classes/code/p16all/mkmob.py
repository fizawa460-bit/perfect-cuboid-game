"""32R-71: Moebius maps between the pencil maps of the decompositions of each d=18 pencil.
For dec t vs dec 0: find constants (a,b,c,d) with F0t*(c*G0 + d*G1) - F1t*(a*G0 + b*G1) = 0 mod I(S)
(G = dec-0 pencil), i.e. F0t/F1t = (a w + b)/(c w + d) on S, w = G0/G1.  Exact (reduce mod std(S), constant syzygies).
usage (from stoll/): python p16all/mkmob.py -> p16all/m_<i>.sing, p16all/jobs.txt"""
import json, os
NL = "\n"
st = json.load(open("p16all/plan.json"))
jobs = []
for i, s in st.items():
    s["nD"] = len(s["decs"])
    if s["nD"] < 2: continue
    body = 'system("--ticks-per-sec", 1000); int TT0 = rtimer;' + NL
    body += "ring RK = 10009,(a1,a2,a3,b1,b2,b3,c),dp;" + NL
    body += "ideal SK = std(ideal(a1^2+a2^2-b3^2, a2^2+a3^2-b1^2, a1^2+a3^2-b2^2, a1^2+a2^2+a3^2-c^2));" + NL
    for t in range(s["nD"]):
        src = open(f"p16all/c_{i}_{t}.sing").read(); k = src.index('system("random", 2718);')
        pre = src[:k] + src[k:].split(NL, 1)[0] + NL
        body += pre + f"setring RK; poly P{t}0 = imap(R, F0); poly P{t}1 = imap(R, F1);" + NL
    body += "setring RK; int tt; int kk; int jj; module KK; ideal NN; int ok;" + NL
    for t in range(1, s["nD"]):
        body += (f"NN = reduce(P{t}0*P00, SK), reduce(P{t}0*P01, SK), reduce(P{t}1*P00, SK), reduce(P{t}1*P01, SK);" + NL
                 + "KK = syz(NN); ok = 0;" + NL
                 + "for (kk = 1; kk <= ncols(KK); kk++) { if (deg(KK[kk]) == 0) { ok++; "
                 + f'"MOB {t}", leadcoef(KK[kk][1]), leadcoef(KK[kk][2]), leadcoef(KK[kk][3]), leadcoef(KK[kk][4]); }} }}' + NL
                 + f'"MOBCOUNT {t}", ok;' + NL)
    body += '"time ms", rtimer - TT0;' + NL + "quit;" + NL
    open(f"p16all/m_{i}.sing", "w", newline=NL).write(body); jobs.append(i)
open("p16all/mobjobs.txt", "w", newline=NL).write(NL.join(jobs) + NL)
print(len(jobs))
