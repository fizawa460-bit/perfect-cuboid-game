import re, sys, glob, os
sys.path.insert(0, 'fasth0')
src = open('fix0/mk.py').read().split("H = json.load")[0]
exec(src)  # NPline, NODE, CUR, comp() need H? comp only uses NODE/CUR
def comp(k, c):
    if k > 92: return f'satur(std(S + ideal({NODE[k]})^{c}), MX)'
    if c == 1: return f'satur(std(S + ideal({CUR[k]})), MX)'
    return f'satur(satur(std(S + std(S + ideal({CUR[k]}))^{c}), NP), MX)'
import json as _j
_H = {'c1': _j.load(open('fasth0/d16v2_h0.json')), 'c14v': _j.load(open('fasth0/d14v2_h0.json')), 'c14f': _j.load(open('fasth0/d14fullf_h0.json'))}
def parse(path):
    b = os.path.basename(path)[:-5]; pre, idx = b.rsplit('_', 1)
    m, h, D = _H[pre][idx]; assert h == 1, (b, h)
    return m, {int(k): v for k, v in D.items()}
def parse_old(path):
    s = open(path).read(); m = int(re.search(r"int mm = (\d+);", s).group(1))
    parts = re.search(r"ideal Iall = (?:intersect\()?([^;)]*)\)?; Iall", s).group(1).split(",")
    D = {}
    for p_ in parts:
        p_ = p_.strip()
        if p_.startswith("G"):
            k = int(re.match(r"G(\d+)", p_).group(1))
            c = int(re.search(rf"sat\(std\(S \+ G{k}\^(\d+)\)", s).group(1)) if p_.endswith("p") else 1
        else:
            k = int(p_[1:]); c = int(re.search(rf"ideal N{k} = std\(S \+ ideal\([^;]*\)\^(\d+)\);", s).group(1))
        D[k] = c
    return m, D
HEAD = ('LIB "elim.lib";\nring R = (0,z),(a1,a2,a3,b1,b2,b3,c),dp; minpoly = z^4+1;\n'
 'ideal S = a1^2+a2^2-b3^2, a2^2+a3^2-b1^2, a1^2+a3^2-b2^2, a1^2+a2^2+a3^2-c^2;\nideal MX = maxideal(1);\n'
 'proc satur(ideal I, ideal Q) { def T = sat(I, Q); ideal R2; if (typeof(T) == "list") { R2 = T[1]; } else { R2 = T; } return(std(R2)); }\n'
 + NPline + '\n'
 'proc dimdeg(ideal J, int mm) { int q; int r; int t = 0; ideal Ls; for (q = 1; q <= ncols(J); q++) { if (J[q] != 0) { if (deg(J[q]) <= mm) { if (deg(J[q]) == mm) { t++; Ls[t] = J[q]; } else { ideal U = maxideal(mm - deg(J[q])); for (r = 1; r <= ncols(U); r++) { t++; Ls[t] = U[r] * J[q]; } kill U; } } } } if (size(Ls) == 0) { return(0); } matrix M = coeffs(Ls, maxideal(mm)); return(rank(M)); }\n'
 'proc h0of(list L, int mm, int dS) { ideal I = L[1]; int i; for (i = 2; i <= size(L); i++) { I = intersect(I, L[i]); } I = std(I); return(dimdeg(I, mm) - dS); }\n')
def script(m, D, tests):
    s = HEAD + f'int mm = {m}; int dS = dimdeg(std(S), mm);\nlist CL;\n'
    keys = sorted(D)
    for i, k in enumerate(keys): s += f'CL[{i+1}] = {comp(k, D[k])};\n'
    s += 'int h0D = h0of(CL, mm, dS); "H0-CHAR0 D", h0D;\n'
    for name, add in tests:
        s += 'list CL2 = CL;\n'
        for k in add:
            if k in D: s += f'CL2[{keys.index(k)+1}] = {comp(k, D[k]+1)};\n'
            else: s += f'CL2[size(CL2) + 1] = {comp(k, 1)};\n'
        s += f'int hh = h0of(CL2, mm, dS); "TEST {name}", hh; kill CL2; kill hh;\n'
    return s + 'quit;\n'
jobs = []
def emit(n, sing, tests):
    m, D = parse(sing); open(f'pic0/{n}.sing', 'w', newline='\n').write(script(m, D, tests)); jobs.append(n)
# 386 + 8: cgk KCOMP lists
for f in sorted(glob.glob('cgk/k_c1_*.out')) + sorted(glob.glob('cgk/k_c14*.out')):
    b = os.path.basename(f)[2:-4]; ks = sorted({int(x) for x in re.findall(r'KCOMP degree \d+\s+known (\d+)', open(f).read())})
    sing = ('cg1/' if b.startswith('c1_') else 'cg14/') + b + '.sing'
    emit('p_' + b, sing, [('ALL ' + ' '.join(map(str, ks)), ks)])
# ALLKNOWN from cgq / cgq14: CONTAINS lists
for f in sorted(glob.glob('cgq/q_*.out')) + sorted(glob.glob('cgq14/q_*.out')):
    t = open(f).read()
    if 'ALLKNOWN' not in t: continue
    b = os.path.basename(f)[2:-4]; ks = sorted({int(x) for x in re.findall(r'CONTAINS (\d+)', t)})
    sing = ('cg1/' if b.startswith('c1_') else 'cg14/') + b + '.sing'
    emit('p_' + b, sing, [('ALL ' + ' '.join(map(str, ks)), ks)])
# residual not a curve: try every single +1 over the 140 curves/nodes
for f in sorted(glob.glob('cgq/q_*.out')):
    if 'residual not a curve' not in open(f).read(): continue
    b = os.path.basename(f)[2:-4]
    emit('p_' + b, 'cg1/' + b + '.sing', [(f'ONE {k}', [k]) for k in range(1, 141)])
open('pic0/jobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n'); print(len(jobs))
