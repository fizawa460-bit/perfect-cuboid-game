import sys, glob, re, os, collections
sys.path.insert(0, 'm16'); sys.argv = ['x']
import an2, importlib
src = open('m16/web.py').read(); web = {}
exec(src.split('C = collections.Counter(); out = []')[0], web)
C = collections.Counter(); changed = []
files = []
for d in ('m16/m_*.out', 'm16/w_*.out', 'm16u/*.out', 'm2c/*.out', 'famc/*.out', 'famd/*.out', 'famg/s1_*.out', 'gph/g_*.out'):
    files += sorted(glob.glob(d))
for fn in files:
    t = open(fn).read()
    if 'COMP ' not in t or 'END' not in t: continue
    if os.path.basename(fn).startswith('g_'):
        nm = os.path.basename(fn)[2:-4]; hp = f'gph2/h_{nm}.out'
        if os.path.exists(hp): t = t + open(hp).read()
    m = re.search(r'SIGMAG\s+(-?\d+)', t)
    if m and int(m.group(1)) >= 2: C['lemmaG'] += 1; continue
    hm = re.search(r'^HH\s+(\d+)', t, re.M); hh = int(hm.group(1)) if hm else 3
    multi = False
    if hh >= 4 or os.path.basename(fn).startswith('w_'):
        try:
            t2, nc = web['run'](fn)
        except Exception:
            t2 = 'PARSEFAIL'
        if t2 is None: C['web-nnout'] += 1; continue
        if t2 == 'PARSEFAIL': C['web-parsefail'] += 1; print('PARSEFAIL', fn)
        else: t = t2; multi = True
    res = []
    for flag in (False, True):
        an2.COLLIDE = flag
        try: r = an2.analyze(t, pencil=(hh == 2), multi=multi)
        except Exception as e: r = {'worst': 'ERR ' + str(e)[:40], 'flags': []}
        res.append(r['worst'])
    C['analyzed'] += 1
    if res[0] != res[1]: changed.append((fn, res))
    if isinstance(res[1], int) and res[1] < 2: C['LOW-after'] += 1; print('LOW', fn, res)
print(dict(C)); print('changed', len(changed))
for c in changed[:40]: print(c)
