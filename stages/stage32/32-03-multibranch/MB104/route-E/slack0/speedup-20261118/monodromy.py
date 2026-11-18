"""Numerical monodromy of covers f = P/Q (degree n) over B = {0, inf, 1, -1, i, -i}: returns for every cover the
tuple (g_0, g_inf, g_1, g_-1, g_i, g_-i) of permutations of the fibre over a base point, up to conjugation via
the canonical form of braid_orbits.c.  Roots of P - wQ are followed along fixed loops with batched eigenvalue
solves; a step is refined until the nearest-root matching is unambiguous.  Exact identity of covers: two covers
are equal iff their canonical tuples agree."""
import numpy as np
FIN = [(0, 0j), (2, 1 + 0j), (3, -1 + 0j), (4, 1j), (5, -1j)]          # (index in B, value) for finite points
R = 0.12
def _segdist(a, b, z):
    t = np.clip(((z - a) * np.conj(b - a)).real / abs(b - a) ** 2, 0, 1); return abs(a + t * (b - a) - z)
def choose_base(seed=3):
    rng = np.random.default_rng(seed)
    while True:
        w0 = complex(rng.uniform(-0.8, 0.8), rng.uniform(-0.8, 0.8))
        if min(abs(w0 - v) for _, v in FIN) < 0.3: continue
        ok = True
        for _, v in FIN:
            e = v + R * (w0 - v) / abs(w0 - v)
            for _, u in FIN:
                if u != v and _segdist(w0, e, u) < 2 * R: ok = False
        if ok: return w0
W0 = choose_base()
def loop_path(v, m=60):
    e = v + R * (w0n := (W0 - v) / abs(W0 - v))
    seg = W0 + (e - W0) * np.linspace(0, 1, m)
    ang = np.angle(w0n) + np.linspace(0, 2 * np.pi, 4 * m)
    circ = v + R * np.exp(1j * ang)
    return np.concatenate([seg, circ[1:], seg[::-1][1:]])
def roots(p, q, w):
    """p,q (N,n+1) low->high; w (N,) -> roots (N,n) of P - wQ via companion eigenvalues"""
    c = p - w[:, None] * q; n = c.shape[1] - 1
    Cm = np.zeros((len(c), n, n), complex); Cm[:, 1:, :-1] = np.eye(n - 1)
    Cm[:, :, -1] = -c[:, :n] / c[:, n:n + 1]
    return np.linalg.eigvals(Cm)
def _step(p, q, z, wa, wb, depth=0):
    """move roots z (N,n) from wa to wb; subdivide only the covers whose matching is ambiguous"""
    N, n = z.shape
    zn = roots(p, q, np.full(N, wb))
    D = np.abs(z[:, :, None] - zn[:, None, :]); j = D.argmin(2); dmin = D.min(2)
    sep = np.abs(zn[:, :, None] - zn[:, None, :]); sep[:, np.arange(n), np.arange(n)] = np.inf
    js = np.sort(j, 1); perm_ok = (js == np.arange(n)).all(1)
    amb = (dmin > 0.3 * np.take_along_axis(sep.min(2), j, 1)).any(1)
    bad = ~perm_ok | amb
    out = zn[np.arange(N)[:, None], j]
    if bad.any():
        if depth > 14: raise RuntimeError('root following failed')
        wm = (wa + wb) / 2; i = np.nonzero(bad)[0]
        zm = _step(p[i], q[i], z[i], wa, wm, depth + 1)
        out[i] = _step(p[i], q[i], zm, wm, wb, depth + 1)
    return out
def follow(p, q, path):
    N, n = p.shape[0], p.shape[1] - 1
    z0 = roots(p, q, np.full(N, path[0])); z = z0.copy()
    for k in range(1, len(path)): z = _step(p, q, z, path[k - 1], path[k])
    D = np.abs(z[:, :, None] - z0[:, None, :]); sig = D.argmin(2)
    assert all(len(set(r)) == n for r in sig)
    return sig, z0
def tuples(p, q):
    """p,q (N,n+1). returns list of tuples (6 permutations, in B order) per cover"""
    N, n = p.shape[0], p.shape[1] - 1
    g = {}
    for y, v in FIN:
        g[y], _ = follow(p, q, loop_path(v))
    # loops ordered by angle around W0 (counter-clockwise); product of all, then g_inf closes it
    order = sorted([y for y, _ in FIN], key=lambda y: np.angle(dict(FIN)[y] - W0))
    out = []
    for i in range(N):
        perms = {y: list(g[y][i]) for y, _ in FIN}
        # composite: first loop order[0], then order[1], ... ; sigma_{ab}(x) = sigma_b(sigma_a(x))
        P = list(range(n))
        for y in order: P = [perms[y][P[x]] for x in range(n)]
        inv = [0] * n
        for x in range(n): inv[P[x]] = x
        perms[1] = inv
        out.append(tuple(tuple(perms[y]) for y in range(6)))
    return out
def canon(t):
    n = len(t[0]); best = None; naut = 0
    for s in range(n):
        lab = [-1] * n; lab[s] = 0; ordr = [s]; h = 0
        while h < len(ordr):
            x = ordr[h]; h += 1
            for g in t:
                z = g[x]
                if lab[z] < 0: lab[z] = len(ordr); ordr.append(z)
        if len(ordr) < n: return None, 0
        c = tuple(tuple(lab[g[ordr[k]]] for k in range(n)) for g in t)
        if best is None or c < best: best, naut = c, 1
        elif c == best: naut += 1
    return best, naut
def check(t, prof):
    """valid slack-0 tuple of this profile?"""
    n = len(t[0])
    for y, g in enumerate(t):
        if any(g[g[x]] != x for x in range(n)): return False
        if sum(1 for x in range(n) if g[x] != x) // 2 != prof[y]: return False
    return True
