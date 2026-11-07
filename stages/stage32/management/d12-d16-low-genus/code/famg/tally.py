import glob, re, json, sys, os, numpy as np
sys.argv=['x']; g={}
exec(open("baselocus.py", encoding="utf-8").read().split('if __name__ == "__main__":')[0], g)
Cm, K, Gq = g['Cm'], g['K'], g['Gq']
Gn = np.array([[int(Gq[i,j].p) for j in range(64)] for i in range(64)], dtype=np.int64)
R = json.load(open('famg/milp2.json'))
gfix = {t: sum(1 for k in v['fix'] if int(k) <= 92 and int(K @ Gn @ Cm[int(k)-1]) == 4) for t, v in R.items()}
cnt = {}; low = []; bad = []
for f in sorted(glob.glob('famg/s[12]_*.out')):
    n = os.path.basename(f)[:-4]; rep = n[1]; tag = '_'.join(n.split('_')[1:4])
    t = open(f).read(); m = re.search(r'SIGMAG (\d+)', t)
    if not m: bad.append((n, t[-300:].replace('\n', ' | '))); continue
    sg = int(m.group(1)) + (gfix[tag] if rep == '2' else 0)
    key = 'ok' if sg >= 2 else 'low'; cnt[key] = cnt.get(key, 0) + 1
    if sg < 2: low.append((n, sg))
print(cnt, 'no result', len(bad)); print('LOW', low)
for b in bad[:30]: print('BAD', b)
