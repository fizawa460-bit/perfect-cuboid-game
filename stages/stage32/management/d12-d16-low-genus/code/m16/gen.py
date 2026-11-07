import sys, json, re
sys.path.insert(0, 'fasth0'); import script_v2 as SV
pre = open('fasth0/precompute_v2.sing').read()
NODE = {int(m.group(2)): m.group(1) for m in re.finditer(r'J = satur\(std\(S \+ ideal\(([^;]*?)\)\^1\), MX\); nm = "N(\d+)_1";', pre)}
CUR = {int(m.group(2)): m.group(1) for m in re.finditer(r'ideal G = std\(S \+ ideal\(([^;]*?)\)\);\nJ = satur\(G, MX\); nm = "C(\d+)_1";', pre)}
H = json.load(open('fasth0/d16v2f_h0.json')); SC = json.load(open('m2/scan16.json'))
TAIL = open('m16/tail.sing').read()
jobs = []; fam = []
for idx, (h, res) in SC.items():
    m, h_, D = H[idx]; D = {int(k): v for k, v in D.items()}
    for k, hh in res:
        if hh == 2 or (isinstance(hh, int) and hh > 2): fam.append((idx, k, hh)); continue
        s = SV.script(D, m); s = s[:s.index('ideal SS = std(S); "H0')]
        s += 'ideal SS = std(S); ideal NFL = simplify(reduce(Lsys, SS), 2); ideal NODES = std(S + minor(jacob(S), 4));\n'
        s += f'int HH = {h}; system("random", 2718); int ii; int kk; list FL; for (kk = 1; kk <= HH; kk++) {{ poly Ft = 0; for (ii = 1; ii <= ncols(NFL); ii++) {{ Ft = Ft + random(1,9999)*NFL[ii]; }} FL[kk] = Ft; kill Ft; }}\n'
        cids = sorted(c for c in D if c <= 92)
        s += 'ideal Dc = std(' + (('intersect(' + ','.join(f'G{c}' for c in cids) + ')') if len(cids) > 1 else (f'G{cids[0]}' if cids else 'ideal(1)')) + ');\n'
        s += 'list DL; intvec DLc;\n' + ''.join(f'DL[{i+1}] = G{c}; DLc[{i+1}] = {D[c]};\n' for i, c in enumerate(cids))
        s += 'proc ordP(poly F, ideal P) { int k = 0; int mm2; for (mm2 = 1; mm2 <= 6; mm2++) { if (size(reduce(F, satur(std(S + P^mm2), MX))) == 0) { k = mm2; } else { break; } } return(k); }\n'
        if k <= 92:
            s += f'ideal GG = satur(std(S + ideal({CUR[k]})), MX); ideal BBg = std(S + ideal(FL[1])); int c0 = (mult(BBg) - mult(satur(BBg, GG))) div mult(GG); ideal J = satur(satur(std(S + GG^(c0 + 2)), NODES), MX);\n'
        else:
            s += f'ideal NPk = std(S + ideal({NODE[k]})); int c0 = ordP(FL[1], NPk); ideal J = satur(std(S + NPk^(c0 + 2)), MX);\n'
        s += f'string TAG = "{idx}_{k}";\n' + TAIL
        n = f'm_{idx}_{k}'; open(f'm16/{n}.sing', 'w', newline='\n').write(s); jobs.append(n)
open('m16/jobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n'); json.dump(fam, open('m16/families.json', 'w'))
print('jobs', len(jobs), 'families', len(fam), fam)
