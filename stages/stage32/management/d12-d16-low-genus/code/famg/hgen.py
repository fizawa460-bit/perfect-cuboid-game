"""Hidden points of the 2-Gamma pencils: P in (curves of D_t + Fix) cap (curves of D2), off the nodes.
For each P, the members Y_s (rep 2, F0 - u F1 in I(D2)) singular at P: F in sat(prod gpow(D2 curve through P) * m_P^2)."""
import json, re
xs = open('famd/x_28246_121.sing').read()
KL = dict(re.findall(r'KL\[(\d+)\] = (satur\(std\(S \+ ideal\([^;]*\)\), MX\));', xs)); KL = {int(k): v for k, v in KL.items()}
R = json.load(open('famg/milp2.json')); jobs = []
for tag, v in R.items():
    D = {int(k): c for k, c in v['D'].items()}; fix = {int(k): c for k, c in v['fix'].items()}
    D2 = {int(k): c for k, c in v['alt']['D2'].items()}
    A = sorted(set(k for k in list(D) + list(fix) if k <= 92)); B = sorted(k for k in D2 if k <= 92)
    r = open(f'famg/r_{tag}.sing').read(); head = r[:r.index('ideal BL = ')]
    s = head + 'ideal NODES = std(S + minor(jacob(S), 4));\n'
    s += 'proc gpow(ideal G, int c) { if (c == 0) { return(ideal(1)); } return(satur(satur(std(S + G^c), NODES), MX)); }\nlist KL;\n'
    for k in sorted(set(A) | set(B)): s += f'KL[{k}] = {KL[k]};\n'
    for a in A:
        for b in B:
            s += f'ideal W = satur(std(KL[{a}] + KL[{b}]), NODES); list PW; if (dim(W) > 0) {{ PW = minAssGTZ(W); }} int iw;\n'
            s += 'for (iw = 1; iw <= size(PW); iw++) { ideal P = std(PW[iw]); ideal Jp = ideal(1);\n'
            for b2 in B: s += f'  if (size(reduce(KL[{b2}], P)) == 0) {{ Jp = Jp * gpow(KL[{b2}], {D2[b2]}); }}\n'
            s += ('  ideal JJ = satur(satur(std(S + Jp * P^2), NODES), MX); poly r0 = reduce(F0, JJ); poly r1 = reduce(F1, JJ);\n'
                  '  string rsv; if (r0 == 0 && r1 == 0) { rsv = "ALL"; } else { if (r1 == 0) { rsv = "u=inf"; } else { if (r0 == 0) { rsv = "u=0"; } else { number kq = leadcoef(r0)/leadcoef(r1); if (r0 - kq*r1 == 0) { rsv = "u=" + string(kq); } else { rsv = "NONE"; } kill kq; } } }\n'
                  f'  "HIDPT {a} {b}", iw, " pdeg", mult(P), " singular member:", rsv; kill P; kill Jp; kill JJ; kill r0; kill r1; kill rsv; }}\n'
                  'kill W; kill PW; kill iw;\n')
    s += 'quit;\n'
    open(f'famg/h_{tag}.sing', 'w', newline='\n').write(s); jobs.append(f'h_{tag}')
open('famg/hjobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n'); print(len(jobs))
