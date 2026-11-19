"""Accuracy audit of the stored 60-digit points: refine every representative again at 100 digits and report, per
cover, the largest distance between a stored odd point and the nearest 100-digit odd point of the same fibre.
usage: python3 ptacc.py all_7.pkl shard nshard out.pkl"""
import sys, os, pickle, numpy as np
F = '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fast40-20261118'
for d in ('../numeric-upto5-20261118', '../speedup-20261118', '.'): sys.path.insert(0, os.path.join(F, d))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import mpmath as mp; mp.mp.dps = 60
import hp_fast
sys.argv = _a
A = pickle.load(open(sys.argv[1], 'rb')); sh, nsh = int(sys.argv[2]), int(sys.argv[3])
out = []
LO, HI = int(os.environ.get('LO', 0)), int(os.environ.get('HI', 10**9))
for i, (p, q, an, aut) in enumerate(A['reps']):
    if i % nsh != sh or not (LO <= i < HI): continue
    n = len(p) - 1
    try:
        o, res, co, hpo, crit, ys, nit = hp_fast.refine_full(p, q, {y: an[y] for y in range(6)}, n, iters=40, dps=100)
    except Exception as e:
        out.append((i, None, repr(e))); continue
    S = [(y, mp.mpc(z)) for y in range(6) for z in an['hp'][y] if z is not None]
    N = {y: [z for z in hpo[y] if z is not None] for y in range(6)}
    Nn = [(y, min(N[y], key=lambda w: abs(w - z))) for y, z in S]      # nearest new point (the shift is ~1e-15)
    import itertools
    idx = range(len(S))
    tri = max(itertools.combinations(idx, 3), key=lambda t: min(abs(S[a][1] - S[b][1]) for a, b in itertools.combinations(t, 2)))
    def frame(zs):
        Mt = mp.matrix([[zs[0], zs[1]], [1, 1]]); lm = mp.lu_solve(Mt, mp.matrix([zs[2], 1]))
        return mp.matrix([[zs[0] * lm[0], zs[1] * lm[1]], [lm[0], lm[1]]])
    T = frame([Nn[k][1] for k in tri]) * mp.inverse(frame([S[k][1] for k in tri]))
    worst = 0.0
    for (y, z) in S:
        w = (T[0, 0] * z + T[0, 1]) / (T[1, 0] * z + T[1, 1])
        d = min(abs(w - v) / (mp.sqrt(1 + abs(w) ** 2) * mp.sqrt(1 + abs(v) ** 2)) for v in N[y])
        worst = max(worst, float(d))
    out.append((i, float(res), worst))
    if len(out) % 2000 == 0: print(sh, len(out), flush=True)
pickle.dump(out, open(sys.argv[4], 'wb'))
ws = sorted(out, key=lambda x: -(x[2] if isinstance(x[2], float) else 1))[:10]
print('worst', ws, 'fails', sum(1 for x in out if x[1] is None))
