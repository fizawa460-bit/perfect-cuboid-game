import sys, os, pickle, numpy as np
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '../speedup-20261118'))
import mono, monodromy as md, braid
from mono import System
d = pickle.load(open(sys.argv[1], 'rb')); n = 7; prof = (2,) * 6
S = System(n, prof, d['fixed'], d['L']); U = d['sols'][:int(sys.argv[2])]
p, q, _ = S.unpack(U); T0 = md.tuples(p, q)
for a, b in ((2, 4), (4, 3), (3, 5), (5, 2)):
    for side in (1, -1):
        U1, ok = braid.run(S, U, a, b, side)
        p, q, _ = S.unpack(U1[ok]); T1 = md.tuples(p, q); T0k = [t for t, o in zip(T0, ok) if o]
        F, J, _ = S.FJ(U1[ok], np.broadcast_to(mono.homB(), (ok.sum(), 6, 2)))
        res = np.abs(F).max()
        cnt = {f: sum(md.canon(braid.predict(t0, a, b, f))[0] == md.canon(t1)[0] for t0, t1 in zip(T0k, T1)) for f in 'ABS'}
        print(a, b, side, 'ok', ok.sum(), 'resid %.1e' % res, cnt, flush=True)
