"""Seeds for the monodromy solver by moving critical values (prototype).
Start: random rational maps of degree n (2n-2 simple critical points, generic critical values).  Each critical
point gets a target branch point (profile t), and all critical values move along straight lines to B at once.
A path survives when the transpositions that meet at one branch point commute; otherwise it degenerates and is
dropped.  Returns valid slack-0 covers of the profile in the parametrisation of mono.System."""
import sys, os, time, numpy as np
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mono
from mono import System, track, analyse, analyse_loose, homB
def moebius_poly(co, T, n):
    a_, b_, c_, d_ = T[0, 0], T[0, 1], T[1, 0], T[1, 1]; out = np.zeros(n + 1, complex)
    for k in range(n + 1):
        term = np.array([1 + 0j])
        for _ in range(k): term = np.convolve(term, [b_, a_])
        for _ in range(n - k): term = np.convolve(term, [d_, c_])
        out += co[k] * term
    return out
def seeds(n, prof, fixed, L, N=400, rng=None, verbose=True):
    rng = rng or np.random.default_rng(0)
    ys = np.array([y for y in range(6) for _ in range(prof[y])]); K = len(ys)
    Sg = System(n, (1,) * 6, fixed, L)          # every critical point carries its own moving value
    Sg.ys = np.arange(K); Sg.K = K; Sg.m = 2 * (n + 1) + K - 3
    U = []; Wst = []
    while len(U) < N:
        p = rng.normal(size=n + 1) + 1j * rng.normal(size=n + 1); q = rng.normal(size=n + 1) + 1j * rng.normal(size=n + 1)
        W = np.polysub(np.polymul(np.polyder(p[::-1]), q[::-1]), np.polymul(p[::-1], np.polyder(q[::-1])))
        cr = np.roots(W)
        if len(cr) != K: continue
        rng.shuffle(cr)
        # source Moebius T with T(fixed_k) = cr_k ; g = f o T has critical points T^{-1}(cr)
        def frame(z):
            Mt = np.array([[z[0], z[1]], [1, 1]], complex); lm = np.linalg.solve(Mt, np.array([z[2], 1])); return Mt * lm
        T = frame(cr[:3]) @ np.linalg.inv(frame(fixed))
        P2, Q2 = moebius_poly(p, T, n), moebius_poly(q, T, n); x = np.concatenate([P2, Q2]); x = x / (x @ L)
        Ti = np.linalg.inv(T); cn = (Ti[0, 0] * cr + Ti[0, 1]) / (Ti[1, 0] * cr + Ti[1, 1])
        vals = np.stack([np.polyval(P2[::-1], cn), np.polyval(Q2[::-1], cn)], -1)
        U.append(np.concatenate([x, cn[3:]])); Wst.append(vals / np.linalg.norm(vals, axis=1)[:, None])
    U = np.array(U); Wst = np.array(Wst)
    Wt = homB()[ys]
    # random phases (gamma trick) keep the straight homogeneous path away from (0,0)
    g = np.exp(2j * np.pi * rng.random((N, K)))[:, :, None]
    Uend, ok, _ = track(Sg, U, Wst * g, np.broadcast_to(Wt, (N, K, 2)), h0=0.02, hmin=1e-9)
    out = []
    for u in Uend[ok]:
        p_, q_, cc = Sg.unpack(u[None])
        an = analyse(p_[0], q_[0], n, prof, cc[0], list(ys)) or analyse_loose(p_[0], q_[0], n, prof, cc[0], list(ys))
        if an is not None: out.append(u)
    if verbose: print(f'seed paths {N}: reached B {ok.sum()}, valid covers {len(out)}', flush=True)
    return out
if __name__ == '__main__':
    n = int(sys.argv[1]); prof = tuple(int(x) for x in sys.argv[2].split(',')); N = int(sys.argv[3]) if len(sys.argv) > 3 else 400
    rng = np.random.default_rng(1)
    fixed = np.array([0.31 + 0.17j, -0.52 + 0.44j, 0.13 - 0.61j]); L = rng.normal(size=2 * (n + 1)) + 1j * rng.normal(size=2 * (n + 1))
    t0 = time.time(); s = seeds(n, prof, fixed, L, N, rng); print(f'{time.time()-t0:.1f}s')

def seq_seed(n, prof, fixed, L, rng=None, starts=8, verbose=True):
    """Sequential version: critical values are sent to B one at a time; at every step all still-free critical
    points are tried in parallel and one whose path survives is kept (a small search instead of luck)."""
    rng = rng or np.random.default_rng(0)
    K = 2 * n - 2; need = {y: prof[y] for y in range(6)}
    Sg = System(n, (1,) * 6, fixed, L); Sg.ys = np.arange(K); Sg.K = K; Sg.m = 2 * (n + 1) + K - 3
    B = homB(); found = []
    for st in range(starts):
        # random start (as in seeds())
        while True:
            p = rng.normal(size=n + 1) + 1j * rng.normal(size=n + 1); q = rng.normal(size=n + 1) + 1j * rng.normal(size=n + 1)
            W = np.polysub(np.polymul(np.polyder(p[::-1]), q[::-1]), np.polymul(p[::-1], np.polyder(q[::-1])))
            cr = np.roots(W)
            if len(cr) == K: break
        def frame(z):
            Mt = np.array([[z[0], z[1]], [1, 1]], complex); lm = np.linalg.solve(Mt, np.array([z[2], 1])); return Mt * lm
        T = frame(cr[:3]) @ np.linalg.inv(frame(fixed))
        P2, Q2 = moebius_poly(p, T, n), moebius_poly(q, T, n); x = np.concatenate([P2, Q2]); x = x / (x @ L)
        Ti = np.linalg.inv(T); cn = (Ti[0, 0] * cr + Ti[0, 1]) / (Ti[1, 0] * cr + Ti[1, 1])
        Wc = np.stack([np.polyval(P2[::-1], cn), np.polyval(Q2[::-1], cn)], -1); Wc /= np.linalg.norm(Wc, axis=1)[:, None]
        u = np.concatenate([x, cn[3:]]); assign = -np.ones(K, int); left = dict(need)
        order = sorted([y for y in range(6) if left[y] > 0], key=lambda y: -left[y])
        ok_all = True
        while (assign < 0).any():
            y = next((y for y in order if left[y] > 0), None)
            free = np.nonzero(assign < 0)[0]
            if y is None: ok_all = False; break
            cand = []
            for k in free:
                Wb = Wc.copy(); Wb[k] = B[y] * np.exp(2j * np.pi * rng.random()); cand.append((k, Wb))
            Ua = np.repeat(u[None], len(cand), 0)
            Uend, ok, _ = track(Sg, Ua, np.repeat(Wc[None], len(cand), 0), np.array([c[1] for c in cand]), h0=0.05, hmin=1e-9)
            good = []
            for i in np.nonzero(ok)[0]:
                _, _, cc = Sg.unpack(Uend[i][None]); cc = cc[0]
                same = [cc[l] for l in np.nonzero(assign == y)[0]] + [cc[cand[i][0]]]
                dmin = min([abs(a - b) for a in same for b in same if a is not b] + [9])
                F, J, _ = Sg.FJ(Uend[i][None], cand[i][1][None])
                if dmin > 1e-4 and np.linalg.cond(J[0]) < 1e10: good.append(i)
            if not good: ok_all = False; break
            i = good[rng.integers(len(good))]; k = cand[i][0]
            u = Uend[i]; Wc = cand[i][1]; assign[k] = y; left[y] -= 1
        if not ok_all:
            if verbose: print(f'  start {st}: stuck', flush=True)
            continue
        # re-express in the System of the profile: critical points ordered by y
        ordk = np.argsort(assign, kind='stable')
        if not all(ordk[:3] == np.arange(3)) and verbose: pass
        _, _, cc = Sg.unpack(u[None]); cc = cc[0]
        found.append((u, assign.copy(), cc))
        if verbose: print(f'  start {st}: seed reached', flush=True)
        break
    return found
