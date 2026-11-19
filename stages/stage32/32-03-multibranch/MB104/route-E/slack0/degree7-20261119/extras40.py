"""40-digit entries for covers that fail analyse in double precision (nearly colliding critical points), and their
Aut(B) images in the other profiles (one image per coset of Stab(t); different cosets give different profiles, so no
de-duplication is needed). Odd points are taken from mpmath.polyroots of the 40-digit fibre polynomials, independent
of double-precision guesses.
usage: python3 extras40.py out.pkl  extra_7_<prof>.pkl ...  [hard:<prof>:<rejhp.pkl>:<hardall.pkl>]"""
import sys, os, pickle, numpy as np
F = '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/fast40-20261118'
for d in ('../numeric-upto5-20261118', '../speedup-20261118', '.'): sys.path.insert(0, os.path.join(F, d))
_a = sys.argv; sys.argv = [_a[0], '0', '0', '1']
import hp_fast, monodromy as md
from covers import BP, AUT
sys.argv = _a
import mpmath as mp
mp.mp.dps = int(os.environ.get("XDPS","60"))
n = 7
def entry(p, q, crit, ysl, prof, aut):
    an = {y: ([], [c for c, yy in zip(crit, ysl) if yy == y]) for y in range(6)}
    for y in range(6):
        f = (BP[y][1] * p - BP[y][0] * q)
        g = f[::-1].copy()
        for c in an[y][1]:
            for _ in range(2): g, _r = np.polydiv(g, np.array([1, -c]))
        an[y] = (list(np.roots(g)) + [None] * (n - 2 * prof[y] - (len(g) - 1)), an[y][1])
    out, res, com, hpodd, critm, ys, nit = hp_fast.refine_full(p, q, an, n, iters=int(os.environ.get("IT","40")), dps=int(os.environ.get("XDPS","60")))
    assert res < 1e-25, res
    P = com[:n + 1]; Q = com[n + 1:]
    an2 = {}; hpo = {}; mind = 1.0
    worstrec = mp.mpf(0)
    for y in range(6):
        y0, y1 = mp.mpc(BP[y][0]), mp.mpc(BP[y][1])
        f = [y1 * P[m] - y0 * Q[m] for m in range(n + 1)]
        cr = [c for c, yy in zip(critm, ys) if yy == y]
        deg0 = max(m for m in range(n + 1) if abs(f[m]) > mp.mpf(10) ** -30 * max(abs(v) for v in f))
        h = list(f[:deg0 + 1])                    # low -> high
        for c in cr:
            for _ in (0, 1):                      # synthetic division by (z - c)
                hi = h[::-1]; qd = [hi[0]]
                for a in hi[1:]: qd.append(a + c * qd[-1])
                h = qd[:-1][::-1]
        rts = mp.polyroots(h[::-1], maxsteps=3000, extraprec=400) if len(h) > 1 else []
        odd = list(rts) + [None] * (n - deg0)
        assert len(odd) == n - 2 * prof[y], (y, len(odd), prof)
        # reconstruct the fibre polynomial from its roots (odd simple, critical double): checks that no root is missed
        fin = [z for z in odd if z is not None] + [c for c in cr for _ in (0, 1)]
        g = [mp.mpc(1)]
        for r in fin: g = [mp.mpc(0)] + g; g = [g[k] - r * (g[k + 1] if k + 1 < len(g) else 0) for k in range(len(g))]
        deg = len(fin); lead = f[deg]
        assert all(abs(f[m]) < mp.mpf(10) ** -30 * max(abs(v) for v in f) for m in range(deg + 1, n + 1))
        rec = max(abs(f[m] - lead * g[m]) for m in range(deg + 1)) / max(abs(v) for v in f)
        worstrec = max(worstrec, rec)
        hpo[y] = odd; an2[y] = ([None if z is None else complex(z) for z in odd], [complex(c) for c in cr])
    assert worstrec < mp.mpf(10) ** -35, worstrec
    allp = [z for y in range(6) for z in hpo[y] if z is not None] + list(critm)
    mind = min(abs(a - b) for i, a in enumerate(allp) for b in allp[:i])
    an2['hp'] = hpo
    return np.array([complex(c) for c in P]), np.array([complex(c) for c in Q]), an2, aut, float(res), float(mind), (P, Q)
def images(base, prof):
    p, q, an, aut, res, mind, (P, Q) = base
    stab = [ui for ui, (M, perm) in enumerate(AUT) if all(prof[perm[y]] == prof[y] for y in range(6))]
    cos = []; seen = set()
    for ui, (M, perm) in enumerate(AUT):
        t2 = tuple(prof[[y for y in range(6) if perm[y] == z][0]] for z in range(6))
        if t2 in seen: continue
        seen.add(t2); cos.append(ui)
    out = []
    for ui in cos:
        M, perm = AUT[ui]
        an2 = {perm[y]: an[y] for y in range(6)}; an2['hp'] = {perm[y]: v for y, v in an['hp'].items()}
        Pm = [mp.mpc(complex(M[0, 0])) * a + mp.mpc(complex(M[0, 1])) * b for a, b in zip(P, Q)]
        Qm = [mp.mpc(complex(M[1, 0])) * a + mp.mpc(complex(M[1, 1])) * b for a, b in zip(P, Q)]
        out.append((M[0, 0] * p + M[0, 1] * q, M[1, 0] * p + M[1, 1] * q, an2, aut, ui))
    assert len(cos) * len(stab) == 24
    return out
outfn = sys.argv[1]; ALL = []; REPS = []; log = []
for arg in sys.argv[2:]:
    items = []
    if arg.startswith('hard:'):
        _, profs, rejhp, hardall = arg.split(':'); prof = tuple(int(c) for c in profs)
        R = pickle.load(open(rejhp, 'rb')); H = pickle.load(open(hardall, 'rb'))
        fixed = np.array([0.31 + 0.17j, -0.52 + 0.44j, 0.13 - 0.61j]); ysl = [y for y in range(6) for _ in range(prof[y])]
        for cf, (k, au) in R['new'].items():
            u = R['fail'][k]; p, q = u[:n + 1], u[n + 1:2 * n + 2]; c = list(fixed) + list(u[2 * n + 2:])
            for M, perm in AUT:
                if not all(prof[perm[y]] == prof[y] for y in range(6)): continue
                p2 = M[0, 0] * p + M[0, 1] * q; q2 = M[1, 0] * p + M[1, 1] * q; y2 = [perm[y] for y in ysl]
                items.append((p2, q2, c, y2, 1)); conjy = {0: 0, 1: 1, 2: 2, 3: 3, 4: 5, 5: 4}
                items.append((np.conj(p2), np.conj(q2), list(np.conj(c)), [conjy[y] for y in y2], 1))
        assert len(items) == len(H), (len(items), len(H))
        auts = {}
        for v in H.values(): pass
    else:
        E = pickle.load(open(arg, 'rb')); prof = tuple(E['prof'])
        skip = {int(a.split(':')[1]) for a in os.environ.get('SKIP', '').split(',') if a and a.split(':')[0] == ''.join(map(str, prof))}
        for ki, (u, t) in enumerate(zip(E['sols'], E['tuples'])):
            if ki in skip: print('skip', prof, ki, flush=True); continue
            cf, au = md.canon(t)
            items.append((u[:n + 1], u[n + 1:2 * n + 2], list(E['fixed'][:3]) + list(u[2 * n + 2:]), list(E['ys']), au))
    for p, q, c, ysl, au in items:
        b = entry(np.asarray(p), np.asarray(q), c, ysl, prof, au)
        REPS.append(b[:4]); log.append((prof, b[4], b[5]))
        for e in images(b, prof): ALL.append(e)
    if not items: print(arg, 'no covers', flush=True); continue
    print(arg, 'covers', len(items), 'worst res', max(l[1] for l in log), 'min point distance', min(l[2] for l in log), flush=True)
print('extra reps', len(REPS), 'weighted', sum(1 / r[3] for r in REPS), ' all images', len(ALL), 'weighted', sum(1 / e[3] for e in ALL))
pickle.dump({'reps': REPS, 'all': ALL, 'log': log}, open(outfn, 'wb'))
