"""Composite covers f = g o h of degree 9 (g and h of degree 3), as seeds for mono_par/mono_dir --seedfile.

usage: python3 make_comp9.py outdir ckpt_dir_3_<g profile>.pkl [...]   (mono_par runs of degree 3, all 15 profiles)

g: a slack-0 cover of degree 3 (four simple critical points over B).  f = g o h is slack 0 exactly when h has its
four critical points w_i over four distinct NON-critical points c_i of g^-1(B) (then f has index 2 at w_i and is
unramified over B elsewhere except at h^-1(crit g), where it has index 2 too).  Profile of f:
t_y(f) = 3 t_y(g) + #{i : g(c_i) = y}.  Like the 4 o 2 composites of degree 8 (degree8-20261120/make_comp.py) these
lie in their own braid orbits, so tracking and random seeds do not reach them.

h for given c_1..c_4: normalise w_1, w_2, w_3 = 0, 1, -1; then (A - c_i B)(w_i) = (A - c_i B)'(w_i) = 0 is a linear
system M(w_4) (A, B) = 0 in the eight coefficients, so w_4 is a root of det M(w_4) (polynomial, found by
interpolation) and (A, B) spans the kernel.  Degenerate roots (w_4 in {0, 1, -1}, a common root of A and B, wrong
critical values) are dropped.  Writes seeds_9_<tag>.pkl per profile (lists of (P, Q, crit points, branch index));
duplicates are harmless (mono_dir names every cover by its monodromy tuple)."""
import sys, os, pickle, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); D8 = os.path.join(HERE, '..', 'degree8-20261120')
sys.path.insert(0, D8)
import make_comp as MC          # compose(), crit_assign(), B (homogeneous points of B)
B = MC.B

def pv(c, z): return np.polyval(c[::-1], z)

def rows(w, c):
    """two rows of M for critical point w with value c: coefficients of A (low->high) then of B"""
    v = np.array([w ** k for k in range(4)], complex); dv = np.array([k * w ** (k - 1) if k else 0 for k in range(4)], complex)
    return np.array([np.concatenate([v, -c * v]), np.concatenate([dv, -c * dv])])

def solve_h(cs):
    W3 = [0.0, 1.0, -1.0]
    R0 = np.concatenate([rows(W3[i], cs[i]) for i in range(3)])
    def M(w4): return np.concatenate([R0, rows(w4, cs[3])])
    zs = 3.0 * np.exp(2j * np.pi * np.arange(16) / 16)
    dets = np.array([np.linalg.det(M(z)) for z in zs])
    coef = np.fft.fft(dets) / 16          # det(M(3 e^{it})) = sum_k a_k 3^k e^{ikt}, degree <= 6
    a = np.array([coef[k] / 3 ** k for k in range(7)])
    out = []
    for w4 in np.roots(a[::-1]):
        for _ in range(3):                # polish det M(w4) = 0 by Newton on the smallest singular value direction
            h = 1e-7; d0 = np.linalg.det(M(w4)); d1 = np.linalg.det(M(w4 + h))
            if d1 == d0: break
            w4 = w4 - d0 * h / (d1 - d0)
        if min(abs(w4 - x) for x in W3) < 1e-6 or not np.isfinite(w4): continue
        u, s, vh = np.linalg.svd(M(w4)); x = vh[-1].conj()
        A_, B_ = x[:4], x[4:]
        if s[-1] > 1e-8 * s[0]: continue
        # degree 3 exactly, no common root
        rA = np.roots(A_[::-1]) if abs(A_).max() > 0 else []
        if len(rA) and min(abs(pv(B_, r)) for r in rA) < 1e-8 * np.abs(B_).max(): continue
        if abs(A_[3]) < 1e-12 and abs(B_[3]) < 1e-12: continue
        ws = W3 + [w4]
        ok = all(abs(pv(A_, w) - c * pv(B_, w)) < 1e-8 * (abs(pv(B_, w)) + 1) for w, c in zip(ws, cs))
        if ok: out.append((A_, B_, np.array(ws, complex)))
    return out

def main():
    outdir = sys.argv[1]; seeds = {}; rng = np.random.default_rng(int(os.environ.get('SEED', '1')))
    gs = []
    for fn in sys.argv[2:]:
        d = pickle.load(open(fn, 'rb')); gs += list(d['sols'])
    nh = 0; nbad = [0]
    for u in gs:
        P, Q = u[:4], u[4:8]
        # random Moebius change of g's source (same cover; keeps critical and odd points finite)
        a0, b0, c0, d0 = np.array([1, 0, 0, 1]) + 0.3 * (rng.normal(size=4) + 1j * rng.normal(size=4))
        P, Q = MC.compose(P, Q, np.array([b0, a0]), np.array([d0, c0]), m=3)
        Wg = np.polysub(np.polymul(np.polyder(P[::-1]), Q[::-1]), np.polymul(P[::-1], np.polyder(Q[::-1])))
        Wg = np.trim_zeros(np.where(np.abs(Wg) < 1e-11 * np.abs(Wg).max(), 0, Wg), 'f')
        gcr = np.roots(Wg)
        if len(gcr) != 4: print('skip g: critical points', len(gcr)); continue
        gval = []
        for z in gcr:
            v = np.array([pv(P, z), pv(Q, z)]); v /= np.linalg.norm(v)
            gval.append(int(np.argmin([abs(v[0] * b[1] - v[1] * b[0]) / np.linalg.norm(b) for b in B])))
        odd = []                                 # (point, label y) of the simple points of g^-1(B), finite only
        for y, b in enumerate(B):
            r = np.roots((b[1] * P - b[0] * Q)[::-1])
            odd += [(z, y) for z in r if np.abs(gcr - z).min() > 1e-4]
        for four in itertools.combinations(range(len(odd)), 4):
            cs = [odd[k][0] for k in four]; ys4 = [odd[k][1] for k in four]
            for A_, B_, ws in solve_h(cs):
                nh += 1
                Pf, Qf = MC.compose(P, Q, A_, B_, m=3)
                s = np.abs(np.concatenate([Pf, Qf])).max(); Pf, Qf = Pf / s, Qf / s
                cr = list(ws)
                for gam in gcr: cr += list(np.roots((A_ - gam * B_)[::-1]))
                try: cr, ys = MC.crit_assign(Pf, Qf, np.array(cr))
                except AssertionError: nbad[0] += 1; continue
                a_, b_, c_, d_ = np.array([1, 0, 0, 1]) + 0.3 * (rng.normal(size=4) + 1j * rng.normal(size=4))
                Pf, Qf = MC.compose(Pf, Qf, np.array([b_, a_]), np.array([d_, c_]), m=9)
                s = np.abs(np.concatenate([Pf, Qf])).max(); Pf, Qf = Pf / s, Qf / s
                cr = (d_ * cr - b_) / (-c_ * cr + a_)
                prof = tuple(ys.count(y) for y in range(6))
                if sum(prof) != 16 or len(cr) != 16: continue
                order = np.argsort(ys, kind='stable')
                seeds.setdefault(prof, []).append((Pf, Qf, cr[order], [ys[k] for k in order]))
    print('g covers', len(gs), 'h maps', nh, 'dropped (critical value test)', nbad[0])
    for prof, lst in sorted(seeds.items()):
        tag = ''.join(map(str, prof)); pickle.dump(lst, open(os.path.join(outdir, f'seeds_9_{tag}.pkl'), 'wb'))
        print(tag, len(lst))

if __name__ == '__main__': main()
