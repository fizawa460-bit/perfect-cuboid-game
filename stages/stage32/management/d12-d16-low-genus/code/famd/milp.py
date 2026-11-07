import json, re, glob, os, sys
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
sys.argv=['x']; g={}
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
Cm, K = g['Cm'], g['K']
sys.path.insert(0, 'fasth0'); import fasth0v2 as F
H = json.load(open('fasth0/d16v2f_h0.json'))
nmap = {int(a): int(b) for a, b in (x.split(':') for x in open('famd/nodemap.txt').read().split())}
def names(D): return [f"C{k}_{c}" if k <= 92 else f"N{k}_{c}" for k, c in sorted(D.items()) if c > 0]
res = {}
for f in sorted(glob.glob('famd/x_*.out')):
    n = os.path.basename(f)[2:-4]; idx = n.split('_')[0]; t = open(f).read()
    m, h, D = H[idx]; D = {int(k): v for k, v in D.items()}
    fix = {}
    for a, b in re.findall(r'^FIXC\s+(\d+)\s+(\d+)', t, re.M): fix[int(a)] = fix.get(int(a), 0) + int(b)
    for a, b in re.findall(r'^FIXE\s+(\d+)\s+(\d+)', t, re.M): fix[nmap[int(a)]] = fix.get(nmap[int(a)], 0) + int(b)
    Dy = dict(D)
    for k, v in fix.items(): Dy[k] = Dy.get(k, 0) + v
    vec = np.zeros(64, dtype=np.int64)
    for k, v in Dy.items(): vec += v * Cm[k - 1]
    out = None
    for mp in (m, m + 1, m + 2):
        target = vec + (mp - m) * K
        avoid = set(k for k in fix if k <= 92)
        prefer_avoid = set(k for k in Dy if k <= 92)
        cost = np.array([100.0 if (k + 1) in prefer_avoid else 1.0 for k in range(140)])
        ub = np.array([0 if (k + 1) in avoid else (4 if k < 92 else 3) for k in range(140)], dtype=float)
        r = milp(c=cost, constraints=[LinearConstraint(Cm.T.astype(float), target.astype(float), target.astype(float))],
                 integrality=np.ones(140), bounds=Bounds(0, ub))
        if r.success:
            c = np.round(r.x).astype(int); D2 = {k + 1: int(c[k]) for k in range(140) if c[k] > 0}
            hh = F.h0(mp, names(D2)); h0y = None
            out = dict(m=mp, D2=D2, h0=hh, h0_orig=h0y, shared=sorted(set(D2) & prefer_avoid))
            break
    res[n] = dict(fix=fix, alt=out)
    print(n, 'fix', fix, '->', None if out is None else (out['m'], 'h0', out['h0'], 'orig h0', out['h0_orig'], 'shared curves', out['shared']))
json.dump(res, open('famd/milp.json', 'w'))
