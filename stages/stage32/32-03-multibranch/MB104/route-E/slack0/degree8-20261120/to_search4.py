"""Convert build5 output (L5_<n>_*.pkl + L5hp) into fast40/build_all's all_<n>.pkl format (reps, all = one image per
coset of Stab(profile), src), so that search4 can run on exactly the same covers (comparison tests only).
usage: python3 to_search4.py n dir"""
import sys, os, glob, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '../numeric-upto5-20261118'))
import mpmath as mp; mp.mp.dps = 60
from common import AUT
n = int(sys.argv[1]); D = sys.argv[2]
reps = []
for fn in sorted(glob.glob(f'{D}/L5_{n}_*.pkl')):
    d = pickle.load(open(fn, 'rb')); H = np.load(fn.replace('/L5_', '/L5hp_').replace('.pkl', '.npy'))
    prof = d['prof']; oy = d['oddy']; cy = d['crity']
    for i in range(len(d['aut'])):
        an = {}; hp = {}
        for y in range(6):
            ks = [k for k in range(len(oy)) if oy[k] == y]
            od = []; hh = []
            for k in ks:
                if H[i, k, 0] == b'inf': od.append(None); hh.append(None)
                else:
                    z = mp.mpc(mp.mpf(H[i, k, 0].decode()), mp.mpf(H[i, k, 1].decode())); hh.append(z); od.append(complex(z))
            an[y] = (od, [complex(c) for c, yy in zip(d['crit'][i], cy) if yy == y])
            if hh: hp[y] = hh
        an['hp'] = hp
        reps.append((d['pq'][i][:n + 1], d['pq'][i][n + 1:], an, int(d['aut'][i])))
allc = []; src = []
for ri, (p, q, an, aut) in enumerate(reps):
    prof = tuple(len(an[y][1]) for y in range(6)); seen = set()
    for ui, (M, perm) in enumerate(AUT):
        t2 = tuple(prof[[y for y in range(6) if perm[y] == z][0]] for z in range(6))
        if t2 in seen: continue
        seen.add(t2)
        an2 = {perm[y]: an[y] for y in range(6)}; an2['hp'] = {perm[y]: w for y, w in an['hp'].items()}
        allc.append((M[0, 0] * p + M[0, 1] * q, M[1, 0] * p + M[1, 1] * q, an2, aut)); src.append((ri, ui))
print('reps', len(reps), 'all', len(allc), 'weighted', sum(1 / c[3] for c in allc))
pickle.dump({'reps': reps, 'all': allc, 'src': src}, open(f'{D}/all_{n}.pkl', 'wb'))
