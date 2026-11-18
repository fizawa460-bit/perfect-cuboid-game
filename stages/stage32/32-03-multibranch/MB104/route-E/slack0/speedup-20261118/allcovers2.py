"""allcovers.py with the relaxed analyse() fallback of mono.py (covers with nearly colliding points). usage: python3 allcovers2.py n"""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here); sys.path.insert(0, os.path.join(here, '../numeric-upto5-20261118'))
ns = sys.argv[1:]; sys.argv = [sys.argv[0], '0', '0', '1']
import mono, allcovers, pickle
_strict = allcovers.analyse
allcovers.analyse = lambda *a, **k: _strict(*a, **k) or mono.analyse_loose(*a, **k)
for n in map(int, ns):
    reps, allc = allcovers.full(n)
    print(n, 'reps', len(reps), 'all', len(allc), 'weighted', sum(1 / c[3] for c in allc))
    pickle.dump({'reps': reps, 'all': allc}, open(f'all_{n}.pkl', 'wb'))
