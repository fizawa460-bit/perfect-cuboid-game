"""32R-75 representation 2 for the 2-Gamma pencils: y = x - Fix, D2 = decomposition of mp*K - y avoiding the
curves of D_t and Fix (MILP, as famd/milp.py); writes famg/r_<tag>.sing (critical scheme of |y| in D2)."""
import json, re, glob, os, sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.argv = ['x']; g = {}
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
Cm, K = g['Cm'], g['K']
sys.path.insert(0, 'fasth0'); import fasth0v2 as F, script_v2 as SV
nmap = {int(a): int(b) for a, b in (x.split(':') for x in open('famd/nodemap.txt').read().split())}
def names(D): return [f"C{k}_{c}" if k <= 92 else f"N{k}_{c}" for k, c in sorted(D.items()) if c > 0]
rt = open('famd/r_28246_121.sing').read(); rt = rt[rt.index('ideal SS = std(S); ideal NFL'):]
meta = json.load(open('famg/meta.json')); res = {}; jobs = []
for tag, v in meta.items():
    hd = open(f"n16/d_{v['job']}.sing").read(); hd = hd[:hd.index('ideal Iall')]
    D = {}
    for mm_ in re.finditer(r'ideal G(\d+)(p*) = ', hd): k = int(mm_.group(1)); D[k] = max(D.get(k, 0), 1 + len(mm_.group(2)))
    for mm_ in re.finditer(r'ideal N(\d+) = satur\(std\(S \+ ideal\([^;]*\)\^(\d+)\)', hd): D[int(mm_.group(1))] = int(mm_.group(2))
    m = int(re.search(r'int mm = (\d+);', open(f"n16/d_{v['job']}.sing").read()).group(1))
    t = open(f'famg/x_{tag}.out').read(); fix = {}
    for a, b in re.findall(r'^FIXC\s+(\d+)\s+(\d+)', t, re.M): fix[int(a)] = fix.get(int(a), 0) + int(b)
    for a, b in re.findall(r'^FIXE\s+(\d+)\s+(\d+)', t, re.M): fix[nmap[int(a)]] = fix.get(nmap[int(a)], 0) + int(b)
    Dy = dict(D)
    for k, c in fix.items(): Dy[k] = Dy.get(k, 0) + c
    vec = np.zeros(64, dtype=np.int64)
    for k, c in Dy.items(): vec += c * Cm[k - 1]
    out = None
    for mp in (m, m + 1, m + 2):
        target = vec + (mp - m) * K
        avoid = set(k for k in Dy if k <= 92)
        ub = np.array([0 if (k + 1) in avoid else (4 if k < 92 else 3) for k in range(140)], dtype=float)
        r = milp(c=np.ones(140), constraints=[LinearConstraint(Cm.T.astype(float), target.astype(float), target.astype(float))],
                 integrality=np.ones(140), bounds=Bounds(0, ub))
        if r.success:
            c = np.round(r.x).astype(int); D2 = {k + 1: int(c[k]) for k in range(140) if c[k] > 0}
            hh = F.h0(mp, names(D2)); out = dict(m=mp, D2=D2, h0=hh); break
    res[tag] = dict(D=D, fix=fix, alt=out)
    print(tag, 'm', m, 'fix', fix, '->', None if out is None else (out['m'], 'h0', out['h0'], 'D2', out['D2']))
    if out and out['h0'] == 2:
        s = SV.script(out['D2'], out['m']); s = s[:s.index('ideal SS = std(S); "H0')]
        open(f'famg/r_{tag}.sing', 'w', newline='\n').write(s + rt); jobs.append(f'r_{tag}')
json.dump(res, open('famg/milp2.json', 'w'), indent=1)
open('famg/rjobs.txt', 'w', newline='\n').write('\n'.join(jobs) + '\n')
