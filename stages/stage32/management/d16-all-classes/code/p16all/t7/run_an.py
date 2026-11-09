# run the R2 analyzer (m16/an2.py, as audited) on the p16all T7 data
import sys, glob, os, re, collections
sys.path.insert(0, 'm16'); sys.argv = ['an2']
import importlib.util
spec = importlib.util.spec_from_file_location('an2', 'm16/an2.py'); A = importlib.util.module_from_spec(spec); spec.loader.exec_module(A)
C = collections.Counter()
for fn in sorted(glob.glob('p16all/t7/t7_*.out')):
    t = open(fn).read(); nm = os.path.basename(fn)[:-4]
    if 'END' not in t: C['UNFINISHED'] += 1; print(nm, 'UNFINISHED'); continue
    sg = int(re.search(r'SIGMAG\s+(-?\d+)', t).group(1))
    if sg >= 2: C['LEMMA-G'] += 1; continue
    r = A.analyze(t, pencil=True)
    st = 'FLAG' if r['flags'] else ('OK' if r['worst'] >= 2 else 'LOW')
    C[st] += 1; print(nm, st, r['worst'], r['flags'][:3])
print(dict(C))
