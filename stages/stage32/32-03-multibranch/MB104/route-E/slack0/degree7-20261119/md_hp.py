"""High-precision fallback for monodromy.tuples: roots of P - wQ by mpmath (dps 40) for covers whose roots nearly
collide (double-precision companion eigenvalues cannot separate them)."""
import sys, numpy as np, mpmath as mp
sys.path.insert(0, '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/speedup-20261118')
import monodromy as md
mp.mp.dps = 40
def _roots(pc, qc, w, guess=None):
    c = [pc[k] - w * qc[k] for k in range(len(pc))][::-1]
    while abs(c[0]) == 0: c = c[1:]
    r = mp.polyroots(c, maxsteps=200, extraprec=120)
    return list(r)
def _match(z, zn):
    n = len(z)
    D = [[abs(a - b) / mp.sqrt((1 + abs(a) ** 2) * (1 + abs(b) ** 2)) for b in zn] for a in z]
    j = [min(range(n), key=lambda k: D[i][k]) for i in range(n)]
    if len(set(j)) < n: return None
    for i in range(n):
        others = [D[i][k] for k in range(n) if k != j[i]]
        if D[i][j[i]] > 0.3 * min(others): return None
    return [zn[j[i]] for i in range(n)]
def _step(pc, qc, z, wa, wb, depth=0):
    zn = _roots(pc, qc, wb); m = _match(z, zn)
    if m is not None: return m
    if depth > 40: raise RuntimeError('hp root following failed')
    wm = (wa + wb) / 2
    return _step(pc, qc, _step(pc, qc, z, wa, wm, depth + 1), wm, wb, depth + 1)
def follow1(pc, qc, path):
    path = [mp.mpc(complex(w)) for w in path]
    z0 = _roots(pc, qc, path[0]); z = list(z0)
    for k in range(1, len(path)): z = _step(pc, qc, z, path[k - 1], path[k])
    n = len(z0)
    sig = [min(range(n), key=lambda k: abs(z[i] - z0[k]) / mp.sqrt((1 + abs(z[i]) ** 2) * (1 + abs(z0[k]) ** 2))) for i in range(n)]
    assert len(set(sig)) == n
    return sig
def tuple1(p, q):
    pc = [mp.mpc(complex(v)) for v in p]; qc = [mp.mpc(complex(v)) for v in q]; n = len(p) - 1
    g = {y: follow1(pc, qc, md.loop_path(v, m=30)) for y, v in md.FIN}
    order = sorted([y for y, _ in md.FIN], key=lambda y: np.angle(dict(md.FIN)[y] - md.W0))
    P = list(range(n))
    for y in order: P = [g[y][P[x]] for x in range(n)]
    inv = [0] * n
    for x in range(n): inv[P[x]] = x
    g[1] = inv
    return tuple(tuple(g[y]) for y in range(6))
