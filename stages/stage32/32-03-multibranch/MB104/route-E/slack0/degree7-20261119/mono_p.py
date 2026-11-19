"""Batched monodromy solver for slack-0 covers (prototype).
All known covers of one profile are tracked together (numpy, one stacked linear solve per step) while the
five finite branch points move along a random triangle loop B -> B1 -> B2 -> B.  New covers are kept.
usage: python3 mono.py n t1,..,t6 [maxloops] [seed]"""
import sys, time, pickle
import numpy as np
_argv = sys.argv; sys.argv = [_argv[0], '0', '0', '1']
import os; sys.path.insert(0, '/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/speedup-20261118'); sys.path.insert(0, os.path.join('/home/user/perfect-cuboid-game/stages/stage32/32-03-multibranch/MB104/route-E/slack0/speedup-20261118', '../numeric-upto5-20261118'))
from covers import newton_batch, analyse, invariant, fingerprint, BP
import closure, covers as _cov, monodromy as md
sys.path.insert(0, '/home/user/work7'); import md_hp
# analyse() with the heuristic thresholds relaxed: an odd point is a simple root as soon as it is not a critical
# point (all 2n-2 critical points are known), so the |f'| test only has to exclude numerical garbage.
_src = open(os.path.join(os.path.dirname(_cov.__file__), 'covers.py')).read()
_code = _src[_src.index('def analyse'):_src.index('def hom(z)')].replace('def analyse', 'def analyse_loose')
_code = _code.replace("<1e-6*np.abs(df).max()*max(1,abs(z))**(n-1)", "<1e-10*np.abs(df).max()*max(1,abs(z))**(n-1)")
pass  # point-separation test kept at 1e-6 (relaxing it admits near-degenerate spurious solutions)
_ns = dict(_cov.__dict__); exec(_code, _ns); analyse_loose = _ns['analyse_loose']
sys.argv = _argv
from fractions import Fraction
from math import factorial
from hurwitz_char import C

def safe_tuples(p, q):
    if len(p) > 128:
        out = []
        for i in range(0, len(p), 128): out += safe_tuples(p[i:i + 128], q[i:i + 128])
        return out
    try: return md.tuples(p, q)
    except (RuntimeError, AssertionError, np.linalg.LinAlgError):
        if len(p) == 1: return [None]
        h = len(p) // 2; return safe_tuples(p[:h], q[:h]) + safe_tuples(p[h:], q[h:])
class System:
    def __init__(s, n, prof, fixed, L):
        s.n = n; s.prof = prof
        s.ys = np.array([y for y in range(6) for _ in range(prof[y])]); s.K = len(s.ys)
        s.fixed = fixed; s.L = L; s.m = 2 * (n + 1) + s.K - 3
        s.mm = np.arange(n + 1)
    def unpack(s, u):
        N = len(u); c = np.empty((N, s.K), complex); c[:, :3] = s.fixed; c[:, 3:] = u[:, 2 * s.n + 2:]
        return u[:, :s.n + 1], u[:, s.n + 1:2 * s.n + 2], c
    def FJ(s, u, W, dW=None):
        """W: (N,6,2) homogeneous branch points. returns F (N,m), J (N,m,m), Fdot (N,m) = dF/dW . dW"""
        n, K, m = s.n, s.K, s.m; p, q, c = s.unpack(u); N = len(u)
        y0 = W[:, s.ys, 0]; y1 = W[:, s.ys, 1]                      # N,K
        mm = s.mm
        V = c[:, :, None] ** mm
        D = np.zeros_like(V); D[:, :, 1:] = mm[1:] * c[:, :, None] ** (mm[1:] - 1)
        D2 = np.zeros_like(V); D2[:, :, 2:] = mm[2:] * (mm[2:] - 1) * c[:, :, None] ** (mm[2:] - 2)
        Pv = np.einsum('nkm,nm->nk', V, p); Qv = np.einsum('nkm,nm->nk', V, q)
        Pd = np.einsum('nkm,nm->nk', D, p); Qd = np.einsum('nkm,nm->nk', D, q)
        Pdd = np.einsum('nkm,nm->nk', D2, p); Qdd = np.einsum('nkm,nm->nk', D2, q)
        F = np.concatenate([y1 * Pv - y0 * Qv, y1 * Pd - y0 * Qd, (u[:, :2 * n + 2] @ s.L - 1)[:, None]], 1)
        J = np.zeros((N, m, m), complex)
        J[:, :K, :n + 1] = y1[:, :, None] * V; J[:, :K, n + 1:2 * n + 2] = -y0[:, :, None] * V
        J[:, K:2 * K, :n + 1] = y1[:, :, None] * D; J[:, K:2 * K, n + 1:2 * n + 2] = -y0[:, :, None] * D
        J[:, 2 * K, :2 * n + 2] = s.L
        k = np.arange(3, K)
        J[:, k, 2 * n + 2 + k - 3] = (y1 * Pd - y0 * Qd)[:, 3:]
        J[:, K + k, 2 * n + 2 + k - 3] = (y1 * Pdd - y0 * Qdd)[:, 3:]
        Fd = None
        if dW is not None:
            d0 = dW[:, s.ys, 0]; d1 = dW[:, s.ys, 1]
            Fd = np.concatenate([d1 * Pv - d0 * Qv, d1 * Pd - d0 * Qd, np.zeros((N, 1))], 1)
        return F, J, Fd

def track(S, u, Wa, Wb, h0=0.05, hmin=1e-7, dmax=1e-4):
    """track u (N,m) from Wa to Wb (each (6,2)); returns u_end, ok mask, number of steps"""
    N = len(u); u = u.copy(); s = np.zeros(N); h = np.full(N, h0); ok = np.ones(N, bool); done = np.zeros(N, bool)
    Wa = np.broadcast_to(Wa, (N,) + Wa.shape[-2:]); Wb = np.broadcast_to(Wb, (N,) + Wb.shape[-2:])
    WA0, WB0 = Wa, Wb; steps = 0
    sc = lambda v: 1 + np.abs(v).max(1)
    while True:
        A = np.nonzero(~done & ok)[0]
        if len(A) == 0: break
        steps += 1
        ua = u[A]; sa = s[A]; ha = np.minimum(h[A], 1 - sa)
        Wa, Wb = WA0[A], WB0[A]; dW = Wb - Wa
        # RK4 predictor of du/ds = -J^{-1} F_W.dW
        def vel(uu, ss):
            WW = Wa + ss[:, None, None] * (Wb - Wa)
            _, J, Fd = S.FJ(uu, WW, dW)
            return -np.linalg.solve(J, Fd[:, :, None])[:, :, 0]
        try:
            k1 = vel(ua, sa); k2 = vel(ua + ha[:, None] / 2 * k1, sa + ha / 2)
            k3 = vel(ua + ha[:, None] / 2 * k2, sa + ha / 2); k4 = vel(ua + ha[:, None] * k3, sa + ha)
        except np.linalg.LinAlgError:
            k1 = k2 = k3 = k4 = np.zeros_like(ua)
        up = ua + ha[:, None] / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        s1 = sa + ha; W1 = Wa + s1[:, None, None] * (Wb - Wa)
        # Newton corrector, 3 steps; accept if contracting and first correction small
        d_first = None; good = np.isfinite(up).all(1)
        for it in range(3):
            F, J, _ = S.FJ(up, W1)
            try: dx = np.linalg.solve(J, F[:, :, None])[:, :, 0]
            except np.linalg.LinAlgError: dx = np.full_like(up, np.nan)
            nd = np.linalg.norm(dx, axis=1) / sc(up)
            if it == 0: d_first = nd
            if it == 2: good &= nd < 1e-10 + 0.1 * d_first
            up = up - dx
        good &= np.isfinite(nd) & (d_first < dmax)
        g = A[good]; b = A[~good]
        u[g] = up[good]; s[g] = s1[good]; h[g] = np.minimum(h[g] * 1.8, 0.25)
        h[b] *= 0.5; ok[b[h[b] < hmin]] = False
        done[g[s[g] >= 1 - 1e-14]] = True
    global _LAST_S
    _LAST_S = s.copy()
    return u, ok, steps

def homB():
    return np.array([[z0, z1] for z0, z1 in BP], complex)

def main():
    n = int(sys.argv[1]); prof = tuple(int(x) for x in sys.argv[2].split(','))
    maxloops = int(sys.argv[3]) if len(sys.argv) > 3 else 200
    rng = np.random.default_rng(int(sys.argv[4]) if len(sys.argv) > 4 else 1)
    target = float(Fraction(C(n, prof), factorial(n)))
    fixed = np.array([0.31 + 0.17j, -0.52 + 0.44j, 0.13 - 0.61j])
    if os.environ.get('FIXSEED'):
        _r = np.random.default_rng(int(os.environ['FIXSEED'])); fixed = 0.7 * (_r.normal(size=3) + 1j * _r.normal(size=3))
    import covers; covers.rng = rng
    L = rng.normal(size=2 * (n + 1)) + 1j * rng.normal(size=2 * (n + 1))
    S = System(n, prof, fixed, L)
    t0 = time.time()
    # seed: critical values of a random map sent to B one at a time (seed.py)
    import seed as _seed
    raw = []
    while not raw: raw = _seed.seq_seed(n, prof, fixed, L, rng, starts=20, verbose=False)
    seed = None
    print(f'seed found {time.time()-t0:.1f}s; target weighted {target}', flush=True)
    B0 = homB()
    sols = [seed]; INV = []; W = 0.0; REJ = []; LOOSE = []; ISLOOSE = []
    TUP = set(); TINV = {}; MIS = []; RESC = []; HARDSOLS = []; HARD = bool(os.environ.get('HARD')); DIAG = bool(os.environ.get('DIAG'))
    def valid(u):
        p, q, cc = S.unpack(u[None])
        an = analyse(p[0], q[0], n, prof, cc[0], list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cc[0], list(S.ys))
        if an is None: REJ.append(u.copy())
        return an is not None
    def accept_batch(Us):
        """exact dedupe: a cover is identified by its monodromy tuple up to conjugation (monodromy.py)"""
        nonlocal W
        Uall = list(Us); vv = [valid(u) for u in Uall]
        Us = [u for u, v in zip(Uall, vv) if v]
        if HARD:
            for u in [u for u, v in zip(Uall, vv) if not v]:
                try: t = md_hp.tuple1(u[:n + 1], u[n + 1:2 * n + 2])
                except Exception: continue
                if not md.check(t, prof): continue
                cf, au = md.canon(t)
                if cf is None or cf in TUP: continue
                TUP.add(cf); W += 1 / au; HARDSOLS.append((u.copy(), au)); print(f'  HARD cover accepted (aut {au}), total hard {len(HARDSOLS)}', flush=True)
        if not Us: return []
        Us = np.array(Us); p, q, _ = S.unpack(Us)
        new = []
        for u, t in zip(Us, safe_tuples(p, q)):
            if t is None or not md.check(t, prof): REJ.append(u.copy()); continue
            cf, au = md.canon(t)
            if DIAG and cf is not None:
                pp, qq, cc = S.unpack(u[None])
                an_ = analyse(pp[0], qq[0], n, prof, cc[0], list(S.ys)) or analyse_loose(pp[0], qq[0], n, prof, cc[0], list(S.ys))
                v_ = invariant(an_)
                if cf in TINV:
                    if np.abs(TINV[cf] - v_).max() > 1e-4 * (1 + np.abs(v_).max()): MIS.append(u.copy())
                else: TINV[cf] = v_
            if cf is None or cf in TUP: continue
            TUP.add(cf); W += 1 / au; new.append(u)
        return new
    def to_u(x2, an2):
        # re-express an image cover in our parametrisation: Mobius in the source sending three crits to 'fixed'
        crit = [z for y in range(6) for z in an2[y][1]]; ysl = [y for y in range(6) for z in an2[y][1]]
        if any(z is None for z in crit): return None
        crit = np.array(crit, complex); ysl = np.array(ysl)
        # crits of each y in S.ys order; choose the first crits of S.ys[0..2] groups
        idx = []; used = set()
        for y in S.ys:
            cand = [k for k in range(len(crit)) if ysl[k] == y and k not in used]; used.add(cand[0]); idx.append(cand[0])
        cs = crit[idx]
        # Mobius T with T(fixed_k) = cs_k ; new cover x(z) = old(T(z))
        def frame(p):
            Mt = np.array([[p[0], p[1]], [1, 1]], complex); lm = np.linalg.solve(Mt, np.array([p[2], 1]))
            return Mt * lm
        T = frame(cs[:3]) @ np.linalg.inv(frame(S.fixed))
        nn = S.n; p, q = x2[:nn + 1], x2[nn + 1:]
        # substitute z -> (a z + b)/(c z + d), homogenise with (c z + d)^n
        a_, b_, c_, d_ = T[0, 0], T[0, 1], T[1, 0], T[1, 1]
        def subst(co):
            out = np.zeros(nn + 1, complex)
            for k in range(nn + 1):
                term = np.array([1 + 0j])
                for _ in range(k): term = np.convolve(term, [b_, a_])
                for _ in range(nn - k): term = np.convolve(term, [d_, c_])
                out += co[k] * term
            return out
        P2, Q2 = subst(p), subst(q); xx = np.concatenate([P2, Q2]); xx = xx / (xx @ S.L)
        Ti = np.linalg.inv(T); cnew = (Ti[0, 0] * cs + Ti[0, 1]) / (Ti[1, 0] * cs + Ti[1, 1])
        u = np.concatenate([xx, cnew[3:]])
        # polish by Newton at B0
        for _ in range(5):
            F, J, _ = S.FJ(u[None], B0[None]); u = u - np.linalg.solve(J[0], F[0])
        F, _, _ = S.FJ(u[None], B0[None])
        return u if np.linalg.norm(F) < 1e-9 * (1 + np.abs(u).max()) else None
    def add_images(Us):
        cand = []
        for u in Us:
            p, q, cc = S.unpack(u[None]); an = analyse(p[0], q[0], n, prof, cc[0], list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cc[0], list(S.ys))
            for x2, an2 in closure.images(np.concatenate([p[0], q[0]]), an, n, prof):
                u2 = to_u(x2, an2)
                if u2 is not None: cand.append(u2)
        new = accept_batch(cand); sols.extend(new); return len(new)
    u_, assign, cc_ = raw[0]
    xg = u_[:2 * n + 2]
    an0 = analyse(xg[:n + 1], xg[n + 1:], n, prof, cc_, list(assign)) or analyse_loose(xg[:n + 1], xg[n + 1:], n, prof, cc_, list(assign))
    seed = to_u(xg, an0); assert seed is not None, 'seed conversion failed'
    sols = [seed]
    CK = f'ckpt_{n}_{"".join(map(str,prof))}.pkl'
    if os.path.exists(CK):
        d = pickle.load(open(CK, 'rb')); sols = list(d['sols']); TUP |= set(d['TUP']); W = d['W']; HARDSOLS.extend(d.get('hard', []))
        f_old = d.get('fixed', np.array([0.31 + 0.17j, -0.52 + 0.44j, 0.13 - 0.61j]))
        if np.abs(f_old - fixed).max() > 1e-12:
            So = System(n, prof, f_old, d.get('L', L)); conv = []
            for u in sols:
                p_, q_, c_ = So.unpack(np.asarray(u)[None])
                an_ = analyse(p_[0], q_[0], n, prof, c_[0], list(So.ys)) or analyse_loose(p_[0], q_[0], n, prof, c_[0], list(So.ys))
                u2 = to_u(np.concatenate([p_[0], q_[0]]), an_) if an_ is not None else None
                if u2 is not None: conv.append(u2)
            print(f'converted {len(conv)}/{len(sols)} covers to the new normalisation', flush=True); sols = conv
        print(f'resumed {len(sols)} covers weighted {W}', flush=True)
        if DIAG:
            T0 = set(TUP); TUP.clear(); W0_ = W; W = 0.0; accept_batch(list(sols)); print(f'DIAG relabelled: {len(TUP)} tuples (stored {len(T0)}), same set {TUP == T0}, mislabels {len(MIS)}', flush=True); TUP |= T0; W = W0_
    else:
        accept_batch([seed]); add_images([seed])
    STALL = int(os.environ.get('STALL', '4')); stall = 0
    tracks = 0; fails = 0
    SCALE = float(sys.argv[5]) if len(sys.argv) > 5 else 2.0
    for loop in range(maxloops):
        # random triangle: perturb finite branch points (index 1 = infinity stays)
        def rnd():
            Wr = B0.copy(); fin = [0, 2, 3, 4, 5]
            Wr[fin, 0] = B0[fin, 0] + SCALE * (rng.normal(size=5) + 1j * rng.normal(size=5)); return Wr
        B1, B2 = rnd(), rnd()
        U = np.array(sols); okall = np.ones(len(U), bool)
        U0 = U.copy()
        for Wa, Wb in ((B0, B1), (B1, B2), (B2, B0)):
            U, ok, st = track(S, U, Wa, Wb); okall &= ok
        if (~okall).any():   # retrack failures carefully (small steps, looser Newton window, smaller hmin)
            Uf = U0[~okall]; okf = np.ones(len(Uf), bool)
            FL = np.full(len(Uf), -1); FS = np.zeros(len(Uf))
            for leg, (Wa, Wb) in enumerate(((B0, B1), (B1, B2), (B2, B0))):
                Uf, ok, st = track(S, Uf, Wa, Wb, h0=0.002, hmin=1e-12, dmax=1e-2)
                nf = okf & ~ok; FL[nf] = leg; FS[nf] = _LAST_S[nf]; okf &= ok
            if DIAG:
                print('  DIAG failures by leg', [int((FL == l).sum()) for l in range(3)], ' last leg s>0.99:', int(((FL == 2) & (FS > 0.99)).sum()), ' s quantiles', np.round(np.quantile(FS[FL >= 0], [0.1, 0.5, 0.9]), 3) if (FL >= 0).any() else None, flush=True)
                RESC.extend([(Uf[i].copy(), FL[i], FS[i]) for i in np.nonzero(FL == 2)[0]]); pickle.dump(RESC, open('resc_' + CK, 'wb'))
            U[~okall] = Uf; idx = np.nonzero(~okall)[0]; okall[idx[okf]] = True
            print(f'  retracked {len(Uf)}, recovered {okf.sum()}', flush=True)
        tracks += len(U); fails += (~okall).sum()
        nw = accept_batch(list(U[okall])); sols.extend(nw); new = len(nw) + add_images(nw)
        if DIAG: print(f'  DIAG mislabels so far {len(MIS)}', flush=True); pickle.dump(MIS, open('mis_' + CK, 'wb'))
        if REJ: print(f'  analyse rejected {len(REJ)} tracked endpoints so far', flush=True)
        print(f'loop {loop}: tracked {len(U)} (failed {(~okall).sum()}), new {new}, covers {len(sols)} weighted {W:.4f}/{target} t={time.time()-t0:.1f}s', flush=True)
        pickle.dump({'sols': np.array(sols), 'TUP': list(TUP), 'W': W, 'fixed': fixed, 'L': L, 'hard': HARDSOLS}, open(CK + '.tmp', 'wb')); os.replace(CK + '.tmp', CK)
        if W >= target - 1e-9: break
        stall = stall + 1 if new == 0 else 0
        if stall >= STALL: print(f'stalled {stall} loops', flush=True); break
    print(f'rejected endpoints: {len(REJ)}')
    print(f'done: covers {len(sols)} weighted {W} target {target}; tracks {tracks}, failed {fails}, time {time.time()-t0:.1f}s')
    covs = []
    for u in sols:
        p, q, cc = S.unpack(u[None]); an = analyse(p[0], q[0], n, prof, cc[0], list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cc[0], list(S.ys))
        covs.append((np.concatenate([p[0], q[0]]), fingerprint(an)[1]))
    # same format as run_covers.py, so allcovers.py can read it
    pickle.dump({'sols': np.array(sols), 'ys': S.ys, 'REJ': REJ, 'L': L, 'fixed': fixed}, open(f'rej_{n}_{"".join(map(str,prof))}.pkl', 'wb'))
    pickle.dump({'n': n, 'prof': prof, 'covers': covs}, open(f'cov_{n}_{"".join(map(str,prof))}.pkl', 'wb'))

if __name__ == '__main__': main()
