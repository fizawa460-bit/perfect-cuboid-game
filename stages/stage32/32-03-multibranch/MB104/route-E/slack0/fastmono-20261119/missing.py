import sys, os, pickle, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono, monodromy as md, autact, mono_dir
from mono import System, homB
from collections import defaultdict
d = pickle.load(open(sys.argv[1], 'rb')); R = pickle.load(open(sys.argv[2], 'rb'))['rules']
n = 7; prof = (2,) * 6; S = System(n, prof, d['fixed'], d['L']); syms = autact.sym_list(prof)
TT = d['TT']; known = set(md.canon(t)[0] for t in TT)
via = defaultdict(list)
for i, t in enumerate(TT):
    for k, mv in enumerate(mono_dir.MOVES):
        c = md.canon(mono_dir.predict(t, mv))[0]
        if c not in known: via[c].append(('mv', k, i))
    for k, rule in enumerate(R):
        c = md.canon(autact.apply(t, rule))[0]
        if c not in known: via[c].append(('sym', k, i))
w = sum(1 / md.canon(md_t)[1] for md_t in [None] if False)
print('missing classes reachable', len(via))
to_u = mono_dir.make_to_u(S, n); B0 = homB()
for c, lst in list(via.items())[:40]:
    nm = sum(1 for x in lst if x[0] == 'mv'); ns = len(lst) - nm
    # try one image with relaxed check
    info = ''
    for kind, k, i in lst:
        if kind != 'sym': continue
        u = d['sols'][i]; x = np.concatenate(S.unpack(u[None])[:2], 1)[0]; _, _, cc = S.unpack(u[None])
        an = {y: ([], [cc[0][j] for j in range(S.K) if S.ys[j] == y]) for y in range(6)}
        cj, M, pi = syms[k]; x2, an2 = autact.image_cover(x, an, n, cj, M, pi)
        cs = cc[0]; dmin = min(abs(cs[a] - cs[b]) for a in range(12) for b in range(a))
        info = f'src crit dmin {dmin:.1e} conf {d["CONF"][i]}'; break
    print(f'via moves {nm} syms {ns} {info}')

print('--- image polish diagnostics')
import seed as _seed
def to_u_dbg(x2, an2, iters):
    crit = [z for y in range(6) for z in an2[y][1]]; ysl = [y for y in range(6) for z in an2[y][1]]
    crit = np.array(crit, complex); ysl = np.array(ysl); idx = []; used = set()
    for y in S.ys:
        cand = [k for k in range(len(crit)) if ysl[k] == y and k not in used]; used.add(cand[0]); idx.append(cand[0])
    cs = crit[idx]
    def frame(pp):
        Mt = np.array([[pp[0], pp[1]], [1, 1]], complex); lm = np.linalg.solve(Mt, np.array([pp[2], 1])); return Mt * lm
    T = frame(cs[:3]) @ np.linalg.inv(frame(S.fixed))
    P2, Q2 = _seed.moebius_poly(x2[:n + 1], T, n), _seed.moebius_poly(x2[n + 1:], T, n)
    xx = np.concatenate([P2, Q2]); xx = xx / (xx @ S.L)
    Ti = np.linalg.inv(T); cnew = (Ti[0, 0] * cs + Ti[0, 1]) / (Ti[1, 0] * cs + Ti[1, 1])
    u = np.concatenate([xx, cnew[3:]]); res = []
    for _ in range(iters):
        F, J, _ = S.FJ(u[None], B0[None]); res.append(np.linalg.norm(F) / (1 + np.abs(u).max()))
        u = u - np.linalg.solve(J[0], F[0])
    F, J, _ = S.FJ(u[None], B0[None]); res.append(np.linalg.norm(F) / (1 + np.abs(u).max()))
    return u, res, np.linalg.cond(J[0]), np.abs(u).max()
for c, lst in list(via.items())[:31:5]:
    for kind, k, i in lst:
        if kind != 'sym': continue
        u = d['sols'][i]; x = np.concatenate(S.unpack(u[None])[:2], 1)[0]; _, _, cc = S.unpack(u[None])
        an = {y: ([], [cc[0][j] for j in range(S.K) if S.ys[j] == y]) for y in range(6)}
        cj, M, pi = syms[k]; x2, an2 = autact.image_cover(x, an, n, cj, M, pi)
        u2, res, cond, mx = to_u_dbg(x2, an2, 12)
        print('res', ['%.0e' % r for r in res[::2]], 'cond %.1e' % cond, 'max|u| %.1e' % mx); break
