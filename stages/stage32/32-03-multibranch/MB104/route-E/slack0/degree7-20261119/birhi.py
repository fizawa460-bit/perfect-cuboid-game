"""Recheck of the 'unclear' (7,7) flags at higher precision: bircheck40 with dps 100, 60 refinement iterations,
thresholds 1e-25 -> 1e-60 (coincidence) and 1e-12 (separation) unchanged."""
import sys, os, pickle, numpy as np
F = '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fast40-20261118'
for d in ('../numeric-upto5-20261118', '../speedup-20261118', '.'): sys.path.insert(0, os.path.join(F, d))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import mpmath as mp; mp.mp.dps = 100
src = open(F + '/bircheck40.py').read().replace('workdps(40)', 'workdps(100)').replace('iters=15)', 'iters=60, dps=100)').replace('1e-25', '1e-60').replace('extraprec=120', 'extraprec=300')
ns = {'__name__': 'birhi'}; exec(compile(src, 'birhi', 'exec'), ns)
sys.argv = _a
A = pickle.load(open('all_7.pkl', 'rb'))
R = pickle.load(open(sys.argv[1], 'rb'))
for fi, qi, M, om, j, h in [x for x in R['hits'] if (x[0], x[1]) in {(b[0], b[1]) for b in R['bir']}]:
    r_, u_ = A['src'][qi]
    an = A['reps'][fi][2]; pts = [z for y in range(6) for t in (0, 1) for z in an[y][t] if z is not None]
    print('f', fi, 'profile', tuple(len(an[y][1]) for y in range(6)), 'min point distance %.1e' % min(abs(a - b) for i, a in enumerate(pts) for b in pts[:i]))
    res = ns['check'](('A', fi), A['reps'][fi], ('B', r_), A['reps'][r_], u_, M)
    print(fi, qi, r_, u_, res['verdict'], ['%.1e / %.1e' % (f[1], f[2] if len(f) > 2 else 0) for f in res['fibres']], 'pts', res['pts_matched'], '/', res['npts'], 'res', res['res'], flush=True)
