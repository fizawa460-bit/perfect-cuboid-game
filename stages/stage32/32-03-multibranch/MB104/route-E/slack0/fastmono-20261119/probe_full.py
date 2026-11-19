"""check: full twist = half-twist formula applied twice (on covers of a stored checkpoint)"""
import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, braid, fasttuples as ft, mono_dir
from mono import System
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = tuple(int(x) for x in sys.argv[2].split(','))
S = System(n, prof, d['fixed'], d['L']); U = d['sols'][:int(sys.argv[3])]
T0 = d.get('TT')[:len(U)]
for mv in mono_dir.MOVES:
    U1, ok = braid.run_full(S, U, mv[0], mv[1], mv[2])
    good = 0; tot = 0
    for u, o, t in zip(U1, ok, T0):
        if not o: continue
        try: t1 = ft.tuples(*S.unpack(u[None])[:2], 12)[0]
        except Exception: continue
        tot += 1; good += md.canon(t1)[0] == md.canon(mono_dir.predict(mono_dir.predict(t, mv), mv))[0]
    print(mv[:3], f'{good}/{tot}', flush=True)
