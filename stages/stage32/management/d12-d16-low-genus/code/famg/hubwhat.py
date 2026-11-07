import sys, re, os, collections
sys.path.insert(0, 'm16'); sys.argv = ['x']
import an2
src = open('m16/web.py').read(); web = {}
exec(src.split('C = collections.Counter(); out = []')[0], web)
lows = [l.split()[1].replace(chr(92), '/') for l in open('famg/recheck_hub3.out') if l.startswith('LOW')]
C = collections.Counter()
for fn in lows:
    t = open(fn).read()
    if os.path.basename(fn).startswith('g_'):
        nm = os.path.basename(fn)[2:-4]; hp = f'gph2/h_{nm}.out'
        if os.path.exists(hp): t = t + open(hp).read()
    hm = re.search(r'^HH\s+(\d+)', t, re.M); hh = int(hm.group(1)) if hm else 3
    multi = False
    if hh >= 4 or os.path.basename(fn).startswith('w_'):
        t, nc = web['run'](fn); multi = True
    out = []
    for a in ((), (2,), (3,), (2, 3)):
        an2.ASSUME1 = a; out.append(an2.analyze(t, pencil=(hh == 2), multi=multi)['worst'])
    an2.ASSUME1 = ()
    C[tuple(out)] += 1; print(fn, out)
print(C)
