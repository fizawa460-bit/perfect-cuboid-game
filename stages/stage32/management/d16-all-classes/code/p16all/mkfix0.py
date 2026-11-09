"""R2 fix0/mk.py (T2') for the 21 new d16 pencils with a component fixed in |x|_p (p16all/fixed.json): exact h0 over
Q(zeta_8) of D and of D + Gamma.  usage (from stoll/): python p16all/mkfix0.py"""
import json, re, sys
pre = open('fasth0/precompute_v2.sing').read()
NPline = re.search(r'^ideal NP = .*$', pre, re.M).group(0)
NODE = {}
for m in re.finditer(r'J = satur\(std\(S \+ ideal\(([^;]*?)\)\^1\), MX\); nm = "N(\d+)_1";', pre): NODE[int(m.group(2))] = m.group(1)
CUR = {}
for m in re.finditer(r'ideal G = std\(S \+ ideal\(([^;]*?)\)\);\nJ = satur\(G, MX\); nm = "C(\d+)_1";', pre): CUR[int(m.group(2))] = m.group(1)
assert len(NODE) == 48 and len(CUR) == 92, (len(NODE), len(CUR))
L = [l.split(chr(9)) for l in open('//wsl.localhost/Ubuntu/root/j16all_new_h0pos.txt').read().split(chr(10))[:-1]]
FXL = json.load(open('p16all/fixed.json'))
H = {}; F = {}; R = []
for i, k in FXL:
    j = L[int(i)][2].split(); H[str(i)] = (int(j[0]), int(j[1]), {a: int(b) for a, b in (q.split(':') for q in j[2].split(','))}); F[str(i)] = [k]; R.append(str(i))
def comp(k, c):
    if k > 92: return f'satur(std(S + ideal({NODE[k]})^{c}), MX)'
    if c == 1: return f'satur(std(S + ideal({CUR[k]})), MX)'
    return f'satur(satur(std(S + std(S + ideal({CUR[k]}))^{c}), NP), MX)'
names = []
for idx in R:
    m, h, D = H[idx]; D = {int(k): v for k, v in D.items()}; fx = F[idx]
    s = 'LIB "elim.lib";\nring R = (0,z),(a1,a2,a3,b1,b2,b3,c),dp; minpoly = z^4+1;\n'
    s += 'ideal S = a1^2+a2^2-b3^2, a2^2+a3^2-b1^2, a1^2+a3^2-b2^2, a1^2+a2^2+a3^2-c^2;\nideal MX = maxideal(1);\n'
    s += 'proc satur(ideal I, ideal Q) { def T = sat(I, Q); ideal R2; if (typeof(T) == "list") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }\n'
    s += NPline + '\n'
    s += f'int mm = {m};\n'
    s += 'proc dimdeg(ideal J, int mm) { int q; int r; int t = 0; ideal Ls; for (q = 1; q <= ncols(J); q++) { if (J[q] != 0) { if (deg(J[q]) <= mm) { if (deg(J[q]) == mm) { t++; Ls[t] = J[q]; } else { ideal U = maxideal(mm - deg(J[q])); for (r = 1; r <= ncols(U); r++) { t++; Ls[t] = U[r] * J[q]; } kill U; } } } } if (size(Ls) == 0) { return(0); } matrix M = coeffs(Ls, maxideal(mm)); return(rank(M)); }\n'
    s += 'int dS = dimdeg(std(S), mm);\n'
    s += 'list CL;\n'
    keys = sorted(D)
    for i, k in enumerate(keys): s += f'CL[{i+1}] = {comp(k, D[k])};\n'
    s += 'proc h0of(list L, int mm, int dS) { ideal I = L[1]; int i; for (i = 2; i <= size(L); i++) { I = intersect(I, L[i]); } I = std(I); return(dimdeg(I, mm) - dS); }\n'
    s += f'int h0D = h0of(CL, mm, dS); "H0-CHAR0 D", h0D, " (char p {h})";\n'
    for k in fx:
        c1 = D.get(k, 0) + 1
        if k in D:
            i = keys.index(k) + 1
            s += f'list CL2 = CL; CL2[{i}] = {comp(k, c1)};\n'
        else:
            s += f'list CL2 = CL; CL2[size(CL2) + 1] = {comp(k, c1)};\n'
        s += f'int hh = h0of(CL2, mm, dS); "H0-CHAR0 D+{k}", hh, " fixed-in-char0", hh == h0D; kill CL2; kill hh;\n'
    s += 'quit;\n'
    n = f'f_{idx}'; open(f'p16all/fix0/{n}.sing', 'w', newline='\n').write(s); names.append(n)
open('p16all/fix0/jobs.txt', 'w', newline='\n').write('\n'.join(names) + '\n'); print(len(names))
