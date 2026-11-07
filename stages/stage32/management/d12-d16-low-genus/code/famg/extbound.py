import json, re, sys
sys.argv = ['x']; g = {}
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
Cm, K, Gq = g['Cm'], g['K'], g['Gq']
import numpy as np
Gn = np.array([[int(Gq[i,j].p) for j in range(64)] for i in range(64)], dtype=np.int64)
ext = json.load(open('famg/ext.json')); R = json.load(open('famg/milp2.json'))
SKIP = {'28246_0_0', '28246_2_0', '28255_0_1', '28255_1_0', '28255_2_0', '27988_0_0', '27988_1_0'}
for tag in R:
    if tag in SKIP: continue
    fix = {int(k): c for k, c in R[tag]['fix'].items()}
    gfix = sum(1 for k in fix if k <= 92 and int(K @ Gn @ Cm[k-1]) == 4)
    m = R[tag]['alt']['m']; D2 = {int(k): c for k, c in R[tag]['alt']['D2'].items()}
    y = m*K - sum(c*Cm[k-1] for k, c in D2.items()); gy = (int(y @ Gn @ y) + int(y @ Gn @ K)) // 2 + 1
    allowed = gy + gfix - 2
    A = {}
    for rep, kind, fac, ln in ext.get(tag, []):
        d = max(1, max([int(e) for e in re.findall(r'\^(\d+)', fac)] + [1]))
        T = A.setdefault(rep, {}).setdefault(fac, {'crit': None, 'node': 0, 'deg': d})
        if kind == 'crit': T['crit'] = ln
        elif kind.startswith('node'): T['node'] += ln // d
        else: print('  !!', tag, kind, fac)
    tot = []
    for rep in ('1', '2'):
        best = 1
        for fac, T in A.get(rep, {}).items():
            val = (T['crit'] if T['crit'] is not None else 1) + T['node']
            best = max(best, val)
        tot.append(best)
    print(tag, 'g(Y)', gy, 'g(Fix)', gfix, 'allowed drop', allowed, '| ext max rep1', tot[0], 'rep2', tot[1], '=>', 'OK' if sum(tot) <= allowed else 'CHECK')
