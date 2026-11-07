# inventory of hubs in the directions where the corrected (MINMH) bound is < 2
import sys, re, os, collections
sys.path.insert(0, 'm16'); sys.argv = ['x']
import an2
src = open('m16/web.py').read(); web = {}
exec(src.split('C = collections.Counter(); out = []')[0], web)
lows = [l.split()[1].replace(chr(92), '/') for l in open('famg/recheck_hub3.out') if l.startswith('LOW')]
summ = collections.Counter()
for fn in lows:
    t = open(fn).read()
    if os.path.basename(fn).startswith('g_'):
        nm = os.path.basename(fn)[2:-4]; hp = f'gph2/h_{nm}.out'
        if os.path.exists(hp): t = t + open(hp).read()
    hm = re.search(r'^HH\s+(\d+)', t, re.M); hh = int(hm.group(1)) if hm else 3
    multi = False
    if hh >= 4 or os.path.basename(fn).startswith('w_'):
        t, nc = web['run'](fn); multi = True
    an2.HUBRH = 'MINMH'; an2.HUBLOG.clear()
    r = an2.analyze(t, pencil=(hh == 2), multi=multi)
    an2.HUBRH = False; r0 = an2.analyze(t, pencil=(hh == 2), multi=multi)
    an2.HUBRH = 'MINMH'
    bad = [d for d, v in r['perdir'].items() if v < 2]
    hubs = sorted({(lam, v, m, g, h, tuple(sorted(map(str, nb)))) for (lam, v, m, g, h, nb) in an2.HUBLOG if lam in bad and h >= 2 and g == 0})
    print(fn, 'new', r['perdir'], '\n   old', r0['perdir'])
    for hb in hubs: print('   HUB', hb)
    for hb in hubs: summ[(hb[2], hb[4])] += 1
print(summ)
