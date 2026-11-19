"""Certify the complete list of slack-0 covers of degree n for every profile representative.
usage: python3 certify.py n datadir  ->  cert_n.pkl

For each profile t (one per Aut(B)-orbit):
  * every numerical cover is renormalized to the system of rig.Sys (three crit points at PHI); this "base" map is
    refined at 320 bits and certified by the Krawczyk test (unique exact solution in a box of radius 1e-50);
    genuineness: homogeneous resultant of (P, Q) excludes 0, crit balls pairwise disjoint (then by Riemann-Hurwitz
    the map is a cover of profile t with simple critical points exactly at these points);
  * all ordered choices of the three PHI-crit points (in the fixed fibres of the profile) are transported from the
    base box by ball arithmetic; each transported enclosure contains an exact normalized map;
  * the enclosures are clustered by overlap of their (P, Q) parts; #clusters is a lower bound for the number of
    distinct exact normalized maps found; it must equal m(t) * H(t) (m = number of ordered choices, H = exact
    Hurwitz number), which is the total number of normalized maps.  Then every cover of profile t is isomorphic
    to one of the base maps.
  * odd points of every base map: 1-D Krawczyk on F_y with ball coefficients, pairwise disjoint and disjoint from
    the crit balls, n - 2 t(y) of them, deg F_y = n certified (leading coefficient excludes 0).
"""
import sys, pickle, glob, itertools, time
from fractions import Fraction
from math import factorial, perm
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from rig import *
from hurwitz_exact import hurwitz

n = int(sys.argv[1]); datadir = sys.argv[2]
H = hurwitz(n)
RHO0 = 1e-50; RHO_U = 1e-16; RHO_ODD_U = 1e-20


def slots_for(prof):
    best = None
    for k in itertools.product(range(4), repeat=6):
        if sum(k) != 3 or any(k[y] > prof[y] for y in range(6)): continue
        m = 1
        for y in range(6): m *= perm(prof[y], k[y])
        key = (m, [-x for x in k])
        if best is None or key < best[0]: best = (key, k, m)
    k = best[1]
    return [y for y in range(6) for _ in range(k[y])], best[2]


def num_crits(p, q):
    """numeric crit points (double) and their fibres; p, q coefficient arrays low->high"""
    P = np.poly1d(p[::-1]); Q = np.poly1d(q[::-1])
    W = (P.deriv() * Q - P * Q.deriv()).coeffs
    W = np.trim_zeros(np.where(np.abs(W) < 1e-12 * np.abs(W).max(), 0, W), 'f')
    cr = np.roots(W)
    assert len(cr) == 2 * n - 2, ('crit at infinity', len(cr))
    out = []
    for c in cr:
        for _ in range(5): c = c - np.polyval(W, c) / np.polyval(np.polyder(W), c)
        v = (P(c), Q(c))
        y = min(range(6), key=lambda y: abs(v[0] * BH[y][1] - v[1] * BH[y][0]) / (abs(v[0]) + abs(v[1])))
        out.append((c, y))
    return out


def subst_num(co, T):
    a, b, c, d = np.asarray(T).flatten(); out = np.zeros(n + 1, complex)
    for k in range(n + 1):
        t = np.array([1 + 0j])
        for _ in range(k): t = np.convolve(t, [b, a])
        for _ in range(n - k): t = np.convolve(t, [d, c])
        out += co[k] * t
    return out


def mob3_num(x, y):
    def fr(p0, p1, p2):
        l0 = (p2 - p1) / (p0 - p1); l1 = 1 - l0; return np.array([[p0 * l0, p1 * l1], [l0, l1]])
    return fr(*y) @ np.linalg.inv(fr(*x))


def choices(crits, slots):
    """ordered choices of 3 distinct crit indices with fibres = slots"""
    out = []
    for c in itertools.permutations(range(len(crits)), 3):
        if all(crits[c[i]][1] == slots[i] for i in range(3)): out.append(c)
    return out


def certify_profile(prof, covers):
    slots, m = slots_for(prof)
    rest = [y for y in range(6) for _ in range(prof[y] - slots.count(y))]
    ys = slots + rest
    S = Sys(n, ys)
    Lc = np.array(Lvec(n))
    bases = []; encl = []
    for ci, x in enumerate(covers):
        p, q = x[:n + 1], x[n + 1:]
        cr = num_crits(p, q)
        if sorted(y for _, y in cr) != sorted(ys): raise RuntimeError(('fibres', prof, ci))
        ch = choices(cr, slots)
        assert len(ch) == m
        # base: choice 0
        c3 = ch[0]
        T = mob3_num(np.array(PHIc), np.array([cr[i][0] for i in c3]))
        P2, Q2 = subst_num(p, T), subst_num(q, T)
        xx = np.concatenate([P2, Q2]); xx = xx / (xx @ Lc)
        Ti = np.linalg.inv(T)
        others = [k for k in range(len(cr)) if k not in c3]
        free = []
        for y in rest:
            k = next(k for k in others if cr[k][1] == y and k not in [f for f, _ in free]); free.append((k, y))
        cn = [(Ti[0, 0] * cr[k][0] + Ti[0, 1]) / (Ti[1, 0] * cr[k][0] + Ti[1, 1]) for k, _ in free]
        u0 = [A(z) for z in list(xx) + cn]
        u, st = S.newton(u0)
        ok, worst = S.krawczyk(u, RHO0)
        if not ok: raise RuntimeError(('krawczyk', prof, ci, worst, st))
        rho_u = RHO_U
        while not S.krawczyk(u, rho_u)[0]:
            rho_u /= 1e3
            if rho_u < 1e-45: raise RuntimeError(('krawczyk uniqueness', prof, ci))
        Z = box(u, RHO0)
        pz, qz, cz = S.unpack(Z)
        res = sylvester_res(pz, qz, n)
        if res.contains(0): raise RuntimeError(('resultant', prof, ci))
        for i in range(len(cz)):
            for j in range(i):
                if cz[i].overlaps(cz[j]): raise RuntimeError(('crit overlap', prof, ci))
        # odd points
        odd = []; tight = []
        for y in range(6):
            Fy = [Y1[y] * pz[j] - Y0[y] * qz[j] for j in range(n + 1)]
            if Fy[n].contains(0): raise RuntimeError(('leading', prof, ci, y))
            Fm = np.array([cpx(c) for c in Fy])
            cy = [cz[k] for k in range(len(ys)) if ys[k] == y]
            g = Fm[::-1].copy()
            for c in cy:
                for _ in range(2): g, r = np.polydiv(g, np.array([1, -cpx(c)]))
            rts = np.roots(g) if len(g) > 1 else []
            if len(rts) != n - 2 * prof[y]: raise RuntimeError(('odd count', prof, ci, y))
            Fmid = [c.mid() for c in Fy]
            pts = []
            for r0 in rts:
                z = newton1(Fmid, A(complex(r0)))
                ok1, tt = krawczyk1(Fy, z, RHO_ODD_U)
                if not ok1: raise RuntimeError(('odd krawczyk', prof, ci, y))
                bz = ball(z, RHO_ODD_U)
                for w in pts + cy:
                    if bz.overlaps(w): raise RuntimeError(('odd overlap', prof, ci, y))
                ok2, tt2 = krawczyk1(Fy, z, 1e-44)
                if ok2: tt = min(tt, tt2)
                pts.append(bz); tight.append(tt)
            odd += [(y, z) for z in pts]
        bases.append({'u': [enc(x) for x in u], 'odd': [(y,) + enc(z) for y, z in odd],
                      'rho': RHO0, 'rho_u': rho_u, 'rho_odd_u': RHO_ODD_U, 'rho_odd': max(tight), 'res_lo': float(res.abs_lower()), 'kraw': worst})
        # transported enclosures for all choices (exact renormalizations of the exact base map)
        cl = cz  # crit balls; index in ys order
        for c3b in itertools.permutations(range(len(ys)), 3):
            if not all(ys[c3b[i]] == slots[i] for i in range(3)): continue
            Tb = mob3(PHI, [cl[i] for i in c3b])
            P3 = mob_subst(pz, n, Tb); Q3 = mob_subst(qz, n, Tb)
            lx = acb(0)
            for j in range(n + 1): lx = lx + S.L[j] * P3[j] + S.L[n + 1 + j] * Q3[j]
            if lx.contains(0): raise RuntimeError(('Lx', prof, ci))
            e = [z / lx for z in P3 + Q3]
            encl.append((ci, e))
    # clustering of (P,Q) enclosures
    N = len(encl)
    mid = np.array([[cpx(z) for z in e] for _, e in encl])
    rad = np.array([[radup(z) for z in e] for _, e in encl])
    parent = list(range(N))
    def fd(i):
        while parent[i] != i: parent[i] = parent[parent[i]]; i = parent[i]
        return i
    mind = np.inf
    for i in range(N):
        dr = np.abs(mid[i + 1:].real - mid[i].real); di = np.abs(mid[i + 1:].imag - mid[i].imag)
        sep = np.maximum(dr, di) - rad[i + 1:] - rad[i]       # > 0 in some coordinate => disjoint
        disj = (sep > 0).any(1)
        for j in np.nonzero(~disj)[0]: parent[fd(i + 1 + j)] = fd(i)
        if (disj).any(): mind = min(mind, float(np.max(np.where(disj[:, None], sep, -1), 1)[disj].min()))
    ncl = len(set(fd(i) for i in range(N)))
    target = m * H[prof]
    return {'prof': prof, 'ys': ys, 'slots': slots, 'm': m, 'H': H[prof], 'n_encl': N, 'clusters': ncl,
            'target': target, 'complete': ncl == target, 'bases': bases, 'min_sep': mind,
            'max_rad': float(rad.max()), 'kraw_worst': max(b['kraw'] for b in bases)}


if __name__ == '__main__':
    out = {}
    t0 = time.time()
    for fn in sorted(glob.glob(f'{datadir}/cov_{n}_*.pkl')):
        d = pickle.load(open(fn, 'rb'))
        covers = [np.asarray(x) for x, aut in d['covers']]
        r = certify_profile(tuple(d['prof']), covers)
        out[r['prof']] = r
        print(r['prof'], 'covers', len(covers), 'm', r['m'], 'enclosures', r['n_encl'], 'clusters', r['clusters'],
              'target m*H', r['target'], 'COMPLETE' if r['complete'] else 'INCOMPLETE',
              f"min_sep {r['min_sep']:.2e} max_rad {r['max_rad']:.1e} kraw {r['kraw_worst']:.1e}  {time.time()-t0:.0f}s", flush=True)
    pickle.dump(out, open(f'cert_{n}.pkl', 'wb'))
    print('all complete:', all(r['complete'] for r in out.values()))
