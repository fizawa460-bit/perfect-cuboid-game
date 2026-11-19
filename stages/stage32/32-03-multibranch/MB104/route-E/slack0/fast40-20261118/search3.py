"""Pair search for slack (0,0), = speedup-20261118/search2.py (j-invariant keys, split subsets, same tolerances and
the same Omega bookkeeping) with two changes:

 (1) SELF PAIRS SEPARATELY.  A table cover q = U∘r whose representative r IS the query cover f has the same odd points
     as f (only the labels are permuted by U).  For such pairs search2 meets every quadruple of f twice over (M = id
     and the Klein-four reorderings), which is where almost all candidates of E22 (6,6) came from (3·10^8).  Here the
     main loop drops every table entry of f's own Aut(B)-orbit, and the self pairs are done exactly once per f:
     all Möbius maps M sending an ordered 4-subset of f's first F1 odd points to a 4-subset of f's first F2 odd points
     with the same cross-ratio (F1 + F2 >= 2 nA - jmin + 4, so every M with >= jmin matched points is met), the point
     matching D is computed once per M,
     and Omega is evaluated for every table cover U∘f of the orbit by relabelling.  M = id is included (q∘id = U∘f is
     a composite by construction).
 (1') KEY.  search2 keys an unordered 4-subset by its j-invariant on the Riemann sphere.  j has a pole of order 2 at
     the cross-ratio 0, 1, ∞, so every quadruple with a cross-ratio below ~0.05 lands within the 10^-5 window of the
     pole: at (5,5) > 99 % of all key matches were such pole matches (e.g. 868,197 of 870,225 for one f).  Here the
     table keys a 4-subset by its cross-ratio (in its own order, on the sphere) and the query side looks up the 6
     cross-ratios of each of its 4-subsets (one ordering per coset of the Klein four-group, which fixes the
     cross-ratio).  This is the same quantity and the same window as the cross-ratio test that search2 applies to
     every candidate anyway (|cross(Y) - cross(X)| <= 4 EPS), so no candidate that search2 accepts is lost.
 (1'') RELATIVE WINDOW NEAR THE POLES.  Covers with nearly colliding odd points have many quadruples whose cross-ratio
     is within 1e-5 of 0, 1 or ∞; any two such quadruples (of any two covers) fall in the same absolute window, which
     made > 90 % of the remaining key matches at degree 7.  The key test is therefore |Δ| <= 4 EPS · min(1, 10 κ),
     κ = chordal distance of the cross-ratio to the nearest of 0, 1, ∞.  For a true matched quadruple the error of
     the cross-ratio is relative: |Δλ|/|λ| <~ Σ ε/|z_i - z_j| (ε ~ 1e-16 from the 40-digit points rounded to double,
     separations >= 1e-6 by the analyse test), i.e. <~ 1e-9, far inside the window; the measured largest ratio is
     printed as 'true_quad_rel_max'.  The final cross-ratio test on every candidate is unchanged (absolute 4 EPS).
 (2) every pair that the double-precision fibre test calls BIRATIONAL is rechecked at 40 digits automatically
     (bircheck40.py = the E22 §3 procedure); the final count uses the 40-digit verdict.

usage: python3 search3.py a b EPS [Fa|-] [shard nshards] [dirA] [dirB]      (input all_n.pkl from build_all.py)
       env NOSELF=1 skips part (1b) (only for timing); env ONLYSELF=1 runs only the self part."""
import os, sys
here = os.path.dirname(os.path.abspath(__file__))
for d in ('../numeric-upto5-20261118', '.'): sys.path.insert(0, os.path.join(here, d))
import pickle, time, itertools, numpy as np
from common import *
a, b = int(sys.argv[1]), int(sys.argv[2]); assert a <= b
EPS = float(sys.argv[3]) if len(sys.argv) > 3 else 1e-9
FA = int(sys.argv[4]) if len(sys.argv) > 4 and sys.argv[4] != '-' else None
SH = int(sys.argv[5]) if len(sys.argv) > 5 else 0; NSH = int(sys.argv[6]) if len(sys.argv) > 6 else 1
DA = sys.argv[7] if len(sys.argv) > 7 else '.'; DB = sys.argv[8] if len(sys.argv) > 8 else DA
import mpmath as mp
mp.mp.dps = 40   # BEFORE unpickling: mpmath rounds unpickled mpf/mpc to the current precision.  search.py (E21) and
                 # speedup-20261118/search2.py load the pickles at the default 15 digits, so their "40-digit" points
                 # were really double precision (true matches then sit at ~1e-17 > the 1e-20 acceptance threshold).
A = pickle.load(open(f'{DA}/all_{a}.pkl', 'rb')); Bd = pickle.load(open(f'{DB}/all_{b}.pkl', 'rb'))
SRC = np.array(Bd['src'], np.int64)                     # (Ncov, 2): representative, Aut(B) index
SAME = (a == b)                                          # self pairs exist only for a == b
ONLYSELF = os.environ.get('ONLYSELF') == '1'
def oddlist(an):
    pts = []; lab = []; ys = []
    for y in range(6):
        for z in an[y][0]:
            w = np.array((1, 0) if z is None else (z, 1), complex); w /= np.linalg.norm(w)
            pts.append(w); lab.append(BLAB[y]); ys.append(y)
    return np.array(pts), np.array(lab), np.array(ys)
def wedge(u, v): return u[..., 0] * v[..., 1] - u[..., 1] * v[..., 0]
def sph(num, den):
    d = np.abs(num) ** 2 + np.abs(den) ** 2
    z = 2 * num * np.conj(den) / d; Z = (np.abs(num) ** 2 - np.abs(den) ** 2) / d
    return np.stack([z.real, z.imag, Z], -1)
def cross(P):
    z1, z2, z3, z4 = P[..., 0, :], P[..., 1, :], P[..., 2, :], P[..., 3, :]
    return sph(wedge(z1, z3) * wedge(z2, z4), wedge(z1, z4) * wedge(z2, z3))
nA, nB = 2 * a + 4, 2 * b + 4; jmin = max(nA, nB) - 4
need = nA + nB - jmin + 4
if FA is None: FA = nA
Fa = FA; Fb = need - Fa; assert 4 <= Fa <= nA and 4 <= Fb <= nB, (Fa, Fb)
print(f'(a,b)=({a},{b}) nA={nA} nB={nB} jmin={jmin} Fa={Fa} Fb={Fb} query covers={len(A["reps"])} table covers={len(Bd["all"])}', flush=True)
t0 = time.time()
def jkey(P):
    z1, z2, z3, z4 = P[..., 0, :], P[..., 1, :], P[..., 2, :], P[..., 3, :]
    num = wedge(z1, z3) * wedge(z2, z4); den = wedge(z1, z4) * wedge(z2, z3)
    Aj = (num ** 2 - num * den + den ** 2) ** 3; Bj = (num * den * (num - den)) ** 2
    s = np.sqrt(np.abs(Aj) ** 2 + np.abs(Bj) ** 2); return sph(Aj / s, Bj / s)
def lcode(L):
    Ls = np.sort(L, -1); return (Ls * np.array([27, 9, 3, 1])).sum(-1)
W8 = 8 * EPS; NX = int(np.ceil(2 / W8)) + 3
def gkey(lc, cell, y): return (lc * NX + cell) * 4 + y + 1
Q = [oddlist(c[2]) for c in Bd['all']]
QP = np.array([x[0] for x in Q]); QL = np.array([x[1] for x in Q])
subB = np.array(list(itertools.combinations(range(Fb), 4)))
if not ONLYSELF:
    # 2-d grid key: (label code, cell of the first sphere coordinate of width 8 EPS, second coordinate); a query looks in
    # the (at most two) cells that its window [x - 4EPS, x + 4EPS] meets.  (search2 used the first coordinate only: a
    # slab of width 8 EPS around a great circle, whose content grows with the table.)
    S_ = cross(QP[:, subB]); K_ = gkey(lcode(QL[:, subB]), np.floor((S_[..., 0] + 1) / W8), S_[..., 1])
    keys = K_.ravel(); TSall = S_.reshape(-1, 3)
    qid = np.repeat(np.arange(len(Q), dtype=np.int32), len(subB)); qq = np.tile(np.arange(len(subB), dtype=np.int32), len(Q))
    o = np.argsort(keys, kind='stable'); keys = keys[o]; qid = qid[o]; qq = qq[o]; TS = TSall[o]; del S_, K_, TSall, o
    print(f'table {len(keys)} entries, {time.time() - t0:.0f}s', flush=True)
import mpmath as mp
mp.mp.dps = 40
from flint import acb, arb, fmpz, ctx as fctx
fctx.prec = 200                                   # the 40-digit points are exact inputs; 200 bits leaves no rounding at 1e-40
def _mpf2arb(x):
    sg, man, ex, bc = x._mpf_
    if not man: return arb(0)
    v = arb(fmpz(int(man))) * arb(2) ** int(ex)             # exact
    return -v if sg else v
def _mp2acb(z): return acb(_mpf2arb(z.real), _mpf2arb(z.imag))
def hplist(an):
    """40-digit odd points as homogeneous pairs of flint acb (search2 used mpmath here; same values, ~50x faster)."""
    out = []
    for y in range(6):
        for z in an['hp'].get(y, []):
            out.append((acb(1), acb(0)) if z is None else (_mp2acb(z), acb(1)))
    return out
def hpdist_pts(X, Y, xs_idx, ys_idx):
    """40-digit chordal distances between M(X_i) and Y_j, M the Möbius map with M X[xs_idx[k]] ~ Y[ys_idx[k]], k<3."""
    def frame(p):    # columns p0*l0, p1*l1 with l0 p0 + l1 p1 = p2
        a, b, c, d = p[0][0], p[1][0], p[0][1], p[1][1]; det = a * d - b * c
        l0 = (d * p[2][0] - b * p[2][1]) / det; l1 = (-c * p[2][0] + a * p[2][1]) / det
        return ((a * l0, b * l1), (c * l0, d * l1))
    Fy = frame([Y[k] for k in ys_idx[:3]]); Fx = frame([X[k] for k in xs_idx[:3]])
    (a, b), (c, d) = Fx; det = a * d - b * c; Fi = ((d / det, -b / det), (-c / det, a / det))
    M = [[Fy[i][0] * Fi[0][j] + Fy[i][1] * Fi[1][j] for j in range(2)] for i in range(2)]
    Yn = [(y, (abs(y[0]) ** 2 + abs(y[1]) ** 2).sqrt()) for y in Y]
    D = np.zeros((len(X), len(Y)))
    for i, x in enumerate(X):
        u0 = M[0][0] * x[0] + M[0][1] * x[1]; u1 = M[1][0] * x[0] + M[1][1] * x[1]
        nu = (abs(u0) ** 2 + abs(u1) ** 2).sqrt()
        for j, (y, ny) in enumerate(Yn):
            D[i, j] = float((abs(u0 * y[1] - u1 * y[0]) / (nu * ny)).mid())
    return D
HA = {}; HB = {}
def best_triple(Dd, P, xs_idx, ys_idx):
    """Three point pairs for the 40-digit Möbius map: the double-precision nearest-neighbour pairs (D < 1e-4, one-to-one)
    whose f points are best separated.  The pairs of the key quadruple can be a near-miss pairing when the cover has
    nearly symmetric points, and the dedupe of (q, M) may keep exactly that quadruple (seen at (6,6): an exact
    composite was missed).  Falls back to the quadruple when fewer than 3 clean pairs exist."""
    j = Dd.argmin(1); ok = Dd[np.arange(len(j)), j] < 1e-4
    ii = np.nonzero(ok)[0]; jj = j[ii]
    if len(set(jj.tolist())) != len(jj) or len(ii) < 3: return list(xs_idx[:3]), list(ys_idx[:3])
    order = np.argsort(Dd[ii, jj])[:10]; ii, jj = ii[order], jj[order]
    best = None
    for a_, b_, c_ in itertools.combinations(range(len(ii)), 3):
        sep = min(np.abs(wedge(P[ii[a_]], P[ii[b_]])), np.abs(wedge(P[ii[a_]], P[ii[c_]])), np.abs(wedge(P[ii[b_]], P[ii[c_]])))
        if best is None or sep > best[0]: best = (sep, (a_, b_, c_))
    t = best[1]; return [int(ii[k]) for k in t], [int(jj[k]) for k in t]
def hpdist(fi, qi, s, pr, yq):
    if fi not in HA: HA[fi] = hplist(A['reps'][fi][2])
    if qi not in HB: HB[qi] = hplist(Bd['all'][qi][2])
    return hpdist_pts(HA[fi], HB[qi], [s[pr[k]] for k in range(4)], list(yq))
perm24 = np.array(list(itertools.permutations(range(4))))
POLES = np.array([[0, 0, -1], [0, 0, 1], [1, 0, 0]], float)     # cross-ratio 0, ∞, 1 on the sphere
def kappa(S):
    """relative window factor min(1, 10 * distance of the cross-ratio to the nearest of 0, 1, ∞); see (1'')."""
    d = np.min(np.linalg.norm(S[:, None, :] - POLES[None], axis=2), 1)
    return np.minimum(1.0, 10 * d)
# S4 acts on the cross-ratio through S4/V4 = S3; these 6 orderings (all fixing the first point) give the 6 values
P6 = np.array([(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1)])
stats = {'cand': 0, 'acc_max': 0.0, 'rej_min': 1.0, 'cr_acc_max': 0.0, 'dup_skipped': 0, 'amb_skipped': 0, 'amb': 0,
         'own_orbit_entries_dropped': 0, 'self_M': 0, 'self_pairs': 0}
hist = {}; hits = []
subA = np.array(list(itertools.combinations(range(Fa), 4)))
def mob3v(x, y):
    def frame(p):
        Mt = np.stack([p[:, 0], p[:, 1]], -1)
        lm = np.linalg.solve(Mt, p[:, 2][:, :, None])[:, :, 0]
        return Mt * lm[:, None, :]
    return frame(y) @ np.linalg.inv(frame(x))
def chdist(u, v): return np.abs(wedge(u, v)) / (np.linalg.norm(u, axis=-1) * np.linalg.norm(v, axis=-1))
def record(fi, qi, M, Du, close, lab, ql, s, yq, d):
    acc = Du[close]; rej = Du[~close]
    if acc.size: stats['acc_max'] = max(stats['acc_max'], float(acc.max()))
    if rej.size: stats['rej_min'] = min(stats['rej_min'], float(rej.min()))
    if d is not None: stats['cr_acc_max'] = max(stats['cr_acc_max'], float(d))
    ii, jj = np.nonzero(close)
    assert len(set(ii)) == len(ii) and len(set(jj)) == len(jj)
    j = int((lab[ii] == ql[jj]).sum()); h = len(ii) - j; om = nA + nB - 2 * j - h
    hist[om] = hist.get(om, 0) + 1
    if om <= 4: hits.append((fi, qi, M, om, j, h))
# orbit lists for the self part: table covers whose representative is fi
orbit = {}
if SAME:
    for qi, (r, u) in enumerate(SRC): orbit.setdefault(int(r), []).append(qi)
# split subsets for the self part (unlabelled): a matching with >= jmin pairs has >= 4 pairs with the source among
# f's first F1 points and the target among f's first F2 points as soon as F1 + F2 >= 2 nA - jmin + 4.
F2 = min(nA, (2 * nA - jmin + 4 + 1) // 2); F1 = min(nA, 2 * nA - jmin + 4 - F2)
allsub = np.array(list(itertools.combinations(range(F2), 4)))
allord = np.array(list(itertools.combinations(range(F1), 4)))[:, perm24].reshape(-1, 4)
for fi, (p, q, an, aut) in enumerate(A['reps']):
    if fi % NSH != SH: continue
    pts, lab, ys = oddlist(an)
    # ---------------- (1a) main part: all table covers outside f's own orbit
    if not ONLYSELF:
        SA = cross(pts[subA][:, P6]).reshape(-1, 3); lcA = np.repeat(lcode(lab[subA]), 6)
        KAP = kappa(SA)
        c1 = np.floor((SA[:, 0] - 4 * EPS + 1) / W8); c2 = np.floor((SA[:, 0] + 4 * EPS + 1) / W8)
        k1 = gkey(lcA, c1, SA[:, 1]); k2 = gkey(lcA, c2, SA[:, 1])
        lo1 = np.searchsorted(keys, k1 - EPS * 4); hi1 = np.searchsorted(keys, k1 + EPS * 4, 'right')
        lo2 = np.searchsorted(keys, k2 - EPS * 4); hi2 = np.searchsorted(keys, k2 + EPS * 4, 'right')
        hi2 = np.where(c2 == c1, lo2, hi2)
        lo = np.concatenate([lo1, lo2]); hi = np.concatenate([hi1, hi2]); SA2 = np.concatenate([SA, SA]); KAP2 = np.concatenate([KAP, KAP])
        cnt = hi - lo
        if cnt.sum():
            R_ = np.repeat(np.arange(len(lo)), cnt); E_ = np.repeat(lo, cnt) + (np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt))
            ok = np.linalg.norm(TS[E_] - SA2[R_], axis=1) <= EPS * 4 * KAP2[R_]; R_ = (R_[ok] % len(SA)) // 6; E_ = E_[ok]
            if len(R_):
                u_ = np.unique(R_.astype(np.int64) * len(keys) + E_); R_ = u_ // len(keys); E_ = u_ % len(keys)
            if SAME:
                own = SRC[qid[E_], 0] == fi; stats['own_orbit_entries_dropped'] += int(own.sum()); R_ = R_[~own]; E_ = E_[~own]
            if len(R_):
                QI = qid[E_]; T_ = subB[qq[E_]]
                YQ = T_[:, perm24]
                labok = (QL[QI[:, None, None], YQ] == lab[subA[R_]][:, None, :]).all(-1)
                c_, p_ = np.nonzero(labok)
                R2 = R_[c_]; QI2 = QI[c_]; YQ2 = YQ[c_, p_]
                X = pts[subA[R2]]; Y = QP[QI2[:, None], YQ2]
                d = np.linalg.norm(cross(Y) - cross(X), axis=1); ok = d <= EPS * 4
                R2, QI2, YQ2, X, Y, d = R2[ok], QI2[ok], YQ2[ok], X[ok], Y[ok], d[ok]
                if len(R2):
                    stats['cand'] += len(R2)
                    M = mob3v(X[:, :3], Y[:, :3])
                    Mf = M.reshape(len(M), 4); Mn = Mf / Mf[np.arange(len(Mf)), np.argmax(np.abs(Mf), 1)][:, None]
                    kk = np.concatenate([QI2[:, None].astype(float), np.round(Mn.real, 6), np.round(Mn.imag, 6)], 1)
                    _, ui = np.unique(kk, axis=0, return_index=True); stats['dup_skipped'] += len(R2) - len(ui)
                    R2, QI2, YQ2, M, d = R2[ui], QI2[ui], YQ2[ui], M[ui], d[ui]
                    img = np.einsum('cij,nj->cni', M, pts); img /= np.linalg.norm(img, axis=2)[:, :, None]
                    D = chdist(img[:, :, None, :], QP[QI2][:, None, :, :])
                    amb = ((D > 1e-11) & (D < 1e-4)).any((1, 2))
                    nclose = (D < 1e-4).any(2).sum(1)
                    skip = amb & (nA + nB - 2 * nclose > 4)
                    stats['amb_skipped'] += int(skip.sum()); hist['>4(skipped)'] = hist.get('>4(skipped)', 0) + int(skip.sum())
                    kq = kappa(cross(pts[subA[R2]])[:, :])
                    for u in np.nonzero(~skip)[0]:
                        qi = int(QI2[u]); yq = YQ2[u]; s = subA[R2[u]]; Du = D[u]
                        if amb[u]:
                            stats['amb'] += 1; xs3, ys3 = best_triple(Du, pts, s, yq)
                            if fi not in HA: HA[fi] = hplist(A['reps'][fi][2])
                            if qi not in HB: HB[qi] = hplist(Bd['all'][qi][2])
                            Du = hpdist_pts(HA[fi], HB[qi], xs3, ys3)
                            if (Du < 1e-20).any(): stats['hp_acc_max'] = max(stats.get('hp_acc_max', 0), float(Du[Du < 1e-20].max()))
                            stats['hp_rej_min'] = min(stats.get('hp_rej_min', 1), float(Du[Du >= 1e-20].min()))
                            close = Du < 1e-20
                        else: close = Du < 1e-11
                        if all(close[s[k], yq[k]] for k in range(4)):
                            stats['true_quad_cr_max'] = max(stats.get('true_quad_cr_max', 0), float(d[u]))
                            stats['true_quad_rel_max'] = max(stats.get('true_quad_rel_max', 0), float(d[u] / kq[u]))
                        record(fi, qi, M[u], Du, close, lab, QL[qi], s, yq, d[u])
    # ---------------- (1b) self part: q = U∘f for the table covers of f's own orbit
    if SAME and os.environ.get('NOSELF') != '1' and fi in orbit:
        Sa = cross(pts[allsub]); So = cross(pts[allord])
        # canonical key: first coordinate of the cross-ratio point; window as in the main part
        o = np.argsort(Sa[:, 0]); ks = Sa[o, 0]
        lo = np.searchsorted(ks, So[:, 0] - EPS * 4); hi = np.searchsorted(ks, So[:, 0] + EPS * 4, 'right'); cnt = hi - lo
        R_ = np.repeat(np.arange(len(So)), cnt); E_ = o[np.repeat(lo, cnt) + (np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt))]
        ok = np.linalg.norm(Sa[E_] - So[R_], axis=1) <= EPS * 4; R_ = R_[ok]; E_ = E_[ok]
        X = pts[allord[R_]]; Y = pts[allsub[E_]]                  # ordered f-quadruple -> sorted f-quadruple
        M = mob3v(X[:, :3], Y[:, :3])
        Mf = M.reshape(len(M), 4); Mn = Mf / Mf[np.arange(len(Mf)), np.argmax(np.abs(Mf), 1)][:, None]
        kk = np.concatenate([np.round(Mn.real, 6), np.round(Mn.imag, 6)], 1)
        _, ui = np.unique(kk, axis=0, return_index=True)
        M = M[ui]; R_ = R_[ui]; E_ = E_[ui]; stats['self_M'] += len(M)
        img = np.einsum('cij,nj->cni', M, pts); img /= np.linalg.norm(img, axis=2)[:, :, None]
        D = chdist(img[:, :, None, :], pts[None, None, :, :])     # (U, nA, nA): f point i -> f point k
        amb = ((D > 1e-11) & (D < 1e-4)).any((1, 2))
        nclose = (D < 1e-4).any(2).sum(1)
        keep = np.nonzero(nA + nB - 2 * nclose <= 4)[0]           # a necessary condition for Omega <= 4 for every U
        for u in keep:
            Du = D[u]
            if amb[u]:
                stats['amb'] += 1
                if fi not in HA: HA[fi] = hplist(an)
                xs3, ys3 = best_triple(Du, pts, list(allord[R_[u]]), list(allsub[E_[u]]))
                Du = hpdist_pts(HA[fi], HA[fi], xs3, ys3); close = Du < 1e-20
            else: close = Du < 1e-11
            # relabel for every cover of the orbit: q = U∘f, q's odd point list is f's points regrouped by perm
            for qi in orbit[fi]:
                stats['self_pairs'] += 1
                perm = AUT[SRC[qi, 1]][1]
                # index map: f point index i (over y) -> position of the same point in q's list (over perm[y])
                offs_q = {}; pos = 0
                inv = {perm[y]: y for y in range(6)}
                for yq in range(6): offs_q[yq] = pos; pos += int((ys == inv[yq]).sum())
                pi = np.empty(nA, int); cntr = {}
                for i in range(nA):
                    yq = perm[ys[i]]; pi[i] = offs_q[yq] + cntr.get(yq, 0); cntr[yq] = cntr.get(yq, 0) + 1
                Dq = np.empty_like(Du); Dq[:, pi] = Du; cq = np.zeros_like(close); cq[:, pi] = close
                assert np.allclose(QP[qi][pi], pts) or np.allclose(np.abs(wedge(QP[qi][pi], pts)), 0, atol=1e-9)
                record(fi, qi, M[u], Dq, cq, lab, QL[qi], None, None, None)
print('hist (distinct (f,q,M))', hist)
print('stats', stats, f'{time.time() - t0:.0f}s', flush=True)
# ---- birationality test (double, as search2) + automatic 40-digit recheck of every BIRATIONAL flag
rng = np.random.default_rng(5)
def evalc(p, q, t):
    n = len(p) - 1; t0_, t1_ = t[..., 0], t[..., 1]
    P = sum(p[m] * t0_ ** m * t1_ ** (n - m) for m in range(n + 1)); Qv = sum(q[m] * t0_ ** m * t1_ ** (n - m) for m in range(n + 1))
    return np.stack([P, Qv], -1)
nonbir = 0; bir = []; flags = []
import bircheck40
for fi, qi, M, om, j, h in hits:
    p, q, _, _ = A['reps'][fi]; pb, qb, _, _ = Bd['all'][qi]
    isbir = True
    for trial in range(3):
        t = rng.normal(size=2) + 1j * rng.normal(size=2)
        v = evalc(p, q, t)
        r = np.roots((v[1] * p - v[0] * q)[::-1]); fib = np.array([[z, 1] for z in r], complex)
        g = evalc(pb, qb, (M @ fib.T).T); g0 = evalc(pb, qb, M @ t)
        if (chdist(g, g0[None, :]) < 1e-7).sum() < 2: break
    else: isbir = False
    if not isbir: nonbir += 1; continue
    r_, u_ = map(int, SRC[qi])
    res = bircheck40.check(('A', fi), A['reps'][fi], ('B', r_), Bd['reps'][r_], u_, M)
    flags.append((fi, qi, om, res))
    print(f'  double says BIRATIONAL: f={fi} q={qi} (rep {r_}, U {u_}) |Omega|={om} -> 40 digits: {res["verdict"]}; '
          f'fibres (2nd smallest) {[f"{x[1]:.1e}" for x in res.get("fibres", [])]}; points matched {res.get("pts_matched")}/{res.get("npts")}', flush=True)
    if res['verdict'] == 'composite': nonbir += 1
    else: bir.append((fi, qi, om, j, h, res['verdict']))
print(f'|Omega|<=4 hits: {len(hits)}  non-birational: {nonbir}  (double-precision BIRATIONAL flags: {len(flags)}, '
      f'composite at 40 digits: {sum(f[3]["verdict"] == "composite" for f in flags)})  BIRATIONAL or unclear after 40 digits: {len(bir)}')
for x in bir[:20]: print('  BIR', x)
print(f'done {time.time() - t0:.0f}s')
pickle.dump({'hits': hits, 'bir': bir, 'flags': flags, 'hist': hist, 'stats': stats}, open(f'res3_{a}_{b}_{SH}of{NSH}.pkl', 'wb'))
