"""Composite covers f = g o h of degree 8 (g of degree 4 with six simple branch points at B, h of degree 2).

usage: python3 make_comp.py outdir ckpt_dir_4_<g profile>.pkl [...]   (mono_dir runs of degree 4)

f's critical points are h^-1(crit g) (two over every point of B) and the two branch points of h, so h must be
branched at two non-critical points c1, c2 of g^-1(B): f then has profile 2,2,2,2,2,2 + e(g(c1)) + e(g(c2)).
g may have two critical points over one point of B (fibre 2+2, no non-critical point there).  (The other
decomposition 2 o 4 puts four critical points over two values; it is not built here.)  Writes seeds_8_<tag>.pkl per
profile: lists of (P, Q, crit points, branch index) for mono_dir --seedfile.  Duplicates are harmless (mono_dir
names every cover by its monodromy tuple and keeps one per class).
"""
import sys, os, pickle, itertools
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); FM = os.path.join(HERE, '..', 'fastmono-20261119')
sys.path.insert(0, FM); sys.path.insert(0, os.path.join(FM, '../speedup-20261118'))
sys.argv, _argv = sys.argv[:1] + ['4', '1,1,1,1,1,1'], sys.argv
from mono import homB
sys.argv = _argv
B = homB()


def pv(c, z): return np.polyval(c[::-1], z)


def compose(P, Q, num, den, m=4):
    """coefficients (low->high) of sum_k P_k num^k den^(m-k) and the same for Q"""
    out = []
    for C in (P, Q):
        acc = np.zeros(1, complex)
        for k in range(m + 1):
            t = np.array([C[k]], complex)
            for _ in range(k): t = np.polymul(t, num[::-1])
            for _ in range(m - k): t = np.polymul(t, den[::-1])
            acc = np.polyadd(acc, t)
        out.append(acc[::-1])
    L = max(len(o) for o in out)
    return [np.concatenate([o, np.zeros(L - len(o))]) for o in out]


def crit_assign(P, Q, cr):
    ys = []
    for z in cr:
        v = np.array([pv(P, z), pv(Q, z)]); v /= np.linalg.norm(v)
        d = [abs(v[0] * b[1] - v[1] * b[0]) / np.linalg.norm(b) for b in B]
        ys.append(int(np.argmin(d))); assert min(d) < 1e-6, min(d)
    return cr, ys


def main():
    outdir = sys.argv[1]; seeds = {}
    sols = [u for fn in sys.argv[2:] for u in pickle.load(open(fn, 'rb'))['sols']]
    for u in sols:
        P, Q = u[:5], u[5:10]
        Wg = np.polysub(np.polymul(np.polyder(P[::-1]), Q[::-1]), np.polymul(P[::-1], np.polyder(Q[::-1])))
        gcr = np.roots(Wg); assert len(gcr) == 6
        fib = {}
        for y, b in enumerate(B):
            c = b[1] * P - b[0] * Q                      # g = b  <=>  b1 P - b0 Q = 0
            r = np.roots(c[::-1])
            fib[y] = [z for z in r if np.abs(gcr - z).min() > 1e-4]     # drop double roots (critical points of g)
        for y1, y2 in itertools.combinations_with_replacement(range(6), 2):
            for c1 in fib[y1]:
                for c2 in fib[y2]:
                    if abs(c1 - c2) < 1e-9: continue
                    # h(z) = (c1 (z+1)^2 - c2 (z-1)^2) / (4z): branched at z = 1 (value c1) and z = -1 (value c2)
                    num = c1 * np.array([1, 2, 1]) - c2 * np.array([1, -2, 1]); den = np.array([0, 4, 0], complex)
                    Pf, Qf = compose(P, Q, num, den)
                    s = np.abs(np.concatenate([Pf, Qf])).max(); Pf, Qf = Pf / s, Qf / s
                    cr = [1.0 + 0j, -1.0 + 0j]
                    for gam in gcr:                       # h(z) = gamma: num - 4 gamma z = 0
                        cr += list(np.roots((num - gam * den)[::-1]))
                    cr, ys = crit_assign(Pf, Qf, np.array(cr))
                    prof = tuple(ys.count(y) for y in range(6))
                    order = np.argsort(ys, kind='stable')
                    seeds.setdefault(prof, []).append((Pf, Qf, cr[order], [ys[k] for k in order]))
    for prof, lst in sorted(seeds.items()):
        tag = ''.join(map(str, prof)); pickle.dump(lst, open(os.path.join(outdir, f'seeds_8_{tag}.pkl'), 'wb'))
        print(tag, len(lst))


if __name__ == '__main__': main()
