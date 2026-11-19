"""search4 = search3 with the changes (4)-(9) below (same |Omega|<=4 hits as search3 on every test: (7,7) on 3 and 6
degree-7 profiles, 8,536 and 27,278 hits, set-identical; see SEARCH4-20261119.md).  Everything not listed is search3.

 (4) KEY POINTS FROM THE 40-DIGIT VALUES: the odd points used for keys and double-precision checks are the stored
     40-digit points rounded to double (env HPKEY=0: an[y][0] as in search3).
 (5) WINDOW FROM AN ERROR ESTIMATE instead of the fixed 4 EPS = 1e-5: for a query quadruple X and a table quadruple Y
     the cross-ratio test is |cr(X) - cr(Y)| <= min(TOL (S_X + S_Y) min(1, kappa/10 * 1.01), 4 EPS), S = sum over the 6
     pairs of 1/chordal distance, kappa = search3's pole factor; TOL = 1e-9.  For a matched quadruple (points equal to
     ~1e-16, accepted up to 1e-11) the cross-ratio error is ~ (point error) * S * (distance to the nearest pole); the
     largest measured ratio (difference / window) over all true quadruples is printed as true_quad_win_ratio_max
     (1.6e-5 on the tests, i.e. a margin of ~10^5).  The table is split into tiers by S (env TIERS) so that a lookup
     uses the largest window of its tier.  The window never exceeds search3's.
 (6) COMPILED PRE-FILTER (verify_nb.prefilter, numba): label test over the 24 orderings, cross-ratio test, Möbius
     map and the count of query points with a table point within 1e-4, with early exit after MAXFAIL unmatched points;
     only candidates with nA + nB - 2 nclose <= 4 continue (search3 drops or records all others with |Omega| > 4).
 (7) ONE-TO-ONE BOUND: a hit's matching is one-to-one, so nclose is replaced by min(nclose, number of table points
     that have a query image within 1e-4).  This drops the candidates where M squeezes many query points next to
     one table point (most of search3's 40-digit 'amb' work at larger tables).  Same basis as search3's own skip
     rule (a true match has double distance < 1e-4).
 (8) SELF PART: same window (5) and a compiled pre-filter (verify_nb.self_filter) before the Möbius dedupe; the index
     maps of the orbit covers are computed once per q instead of once per (M, q).
 (9) MEMORY: one copy of all_n.pkl when a == b; the table is built in chunks; the 'all' list is dropped after the
     table is built and a table cover is rebuilt on demand from its representative and Aut(B) index (checked against
     the stored entry on 200 random covers at start-up); JOBS=k forks k workers after the table is built
     (copy-on-write, the table is in memory once), worker w doing shard SH*k + w of NSH*k.
 env OLDWIN=1 restores search3's windows and disables (6) (for comparison); NB=0 disables (6)-(8)'s compiled parts.

----- search3 header -----
Pair search for slack (0,0), = speedup-20261118/search2.py (j-invariant keys, split subsets, same tolerances and
the same Omega bookkeeping) with these changes (same |Omega|<=4 hits on every test, plus hits search2 missed):

 (1) SELF PAIRS SEPARATELY.  A table cover q = U∘r whose representative r IS the query cover f has the same odd points
     as f (only the labels are permuted by U).  For such pairs search2 meets every quadruple of f twice over (M = id
     and the Klein-four reorderings), which is where almost all candidates of E22 (6,6) came from (3·10^8).  Here the
     main loop drops every table entry whose representative index is f (pairs with a different representative that
     happens to be in the same Aut(B)-orbit, e.g. through the profile stabiliser, stay in the main loop), and the
     self pairs are done exactly once per f:
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
 (1''') 2-D GRID KEY: (label code, cell of width 8 EPS in the first sphere coordinate, second coordinate), so a lookup
     meets a small square instead of a slab around a great circle.
 (1'''') 40-DIGIT DISTANCES: computed with flint at 200 bits from the exact stored points, only for entries whose double
     distance is < 1e-4, and with the Möbius map rebuilt from the three best separated nearest-neighbour pairs.
 (3) PRECISION BUG FIXED: mp.dps is raised BEFORE the pickles are loaded (mpmath rounds unpickled numbers to the
     current precision; search.py of E21 and search2.py of PR #1881 load at 15 digits, so their "40-digit" check
     used double-precision points; at (5,5) this lost 7 composite hits).
 (2) every pair that the double-precision fibre test calls BIRATIONAL is rechecked at 40 digits automatically
     (bircheck40.py = the E22 §3 procedure); the final count uses the 40-digit verdict.

usage: [JOBS=k] python3 search4.py a b EPS [Fa|-] [shard nshards] [dirA] [dirB]      (input all_n.pkl from build_all.py)
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
mp.mp.dps = 60   # BEFORE unpickling (60 >= the digits of any stored list, see build_all DPS): mpmath rounds unpickled mpf/mpc to the current precision.  search.py (E21) and
                 # speedup-20261118/search2.py load the pickles at the default 15 digits, so their "40-digit" points
                 # were really double precision (true matches then sit at ~1e-17 > the 1e-20 acceptance threshold).
Bd = pickle.load(open(f'{DB}/all_{b}.pkl', 'rb'))
A = Bd if (a == b and os.path.samefile(f'{DA}/all_{a}.pkl', f'{DB}/all_{b}.pkl')) else pickle.load(open(f'{DA}/all_{a}.pkl', 'rb'))   # one copy in memory
NB_ALL = len(Bd['all'])
SRC = np.array(Bd['src'], np.int64)                     # (Ncov, 2): representative, Aut(B) index
SAME = (a == b)                                          # self pairs exist only for a == b
ONLYSELF = os.environ.get('ONLYSELF') == '1'
HPKEY = os.environ.get('HPKEY', '1') == '1'        # odd points for keys/verification = the 40-digit points rounded to double
DIAG = os.environ.get('DIAG') == '1'; DIAGL = []
NB = os.environ.get('NB', '1') == '1' and os.environ.get('OLDWIN') != '1'   # compiled pre-filter (verify_nb.py)
if NB: import verify_nb
ONE2ONE = os.environ.get('ONE2ONE', '1') == '1'
FASTSKIP = os.environ.get('FASTSKIP', '1') == '1'   # skip all candidates with Omega lower bound > 4 (not only ambiguous ones)
TOL = float(os.environ.get('TOL', '1e-9'))           # window of a quadruple pair = TOL * (S_query + S_table), see (5)
OLDWIN = os.environ.get('OLDWIN') == '1'             # 1 = search3 windows (for comparison)
def condS(P):
    """S = sum over the 6 pairs of a quadruple of 1/chordal distance (unit homogeneous vectors)."""
    tot = 0
    for i, j in itertools.combinations(range(4), 2): tot = tot + 1 / np.abs(wedge(P[..., i, :], P[..., j, :]))
    return tot
def rss():
    try: return [l for l in open('/proc/self/status') if l.startswith(('VmRSS', 'VmHWM'))]
    except Exception: return ''
def oddlist(an):
    pts = []; lab = []; ys = []
    for y in range(6):
        src_ = an['hp'].get(y, []) if HPKEY else an[y][0]
        assert len(src_) == len(an[y][0])
        for z in src_:
            w = np.array((1, 0) if z is None else (complex(z), 1), complex); w /= np.linalg.norm(w)
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
print('mem after load', rss(), flush=True)
QP = np.empty((NB_ALL, nB, 2), complex); QL = np.empty((NB_ALL, nB), np.int64)
for i_, c_ in enumerate(Bd['all']): QP[i_], QL[i_] = oddlist(c_[2])[:2]
# the table covers are rebuilt on demand from their representative (build_all: q = U∘r, an relabelled by perm), so the
# 'all' list (the largest object: 40-digit points of every table cover) is dropped
_AUT = AUT                 # from common (as used by the self part)
def table_cover(qi):
    r, u = map(int, SRC[qi]); p, q, an, aut = Bd['reps'][r]; Mu, perm = _AUT[u]
    an2 = {perm[y]: an[y] for y in range(6)}; an2['hp'] = {perm[y]: v for y, v in an['hp'].items()}
    return (Mu[0, 0] * p + Mu[0, 1] * q, Mu[1, 0] * p + Mu[1, 1] * q, an2, aut)
_chk = np.random.default_rng(0).choice(NB_ALL, min(200, NB_ALL), replace=False)
for qi in _chk:      # the rebuilt cover is the stored one
    c1, c2 = Bd['all'][qi], table_cover(qi)
    assert np.allclose(c1[0], c2[0]) and np.allclose(c1[1], c2[1]) and c1[3] == c2[3]
    assert all(c1[2][y] == c2[2][y] for y in range(6)) and all(list(c1[2]['hp'].get(y, [])) == list(c2[2]['hp'].get(y, [])) for y in range(6))
del Bd['all']; import gc; gc.collect()
print('mem after QP', rss(), flush=True)
subB = np.array(list(itertools.combinations(range(Fb), 4)))
if not ONLYSELF:
    # 2-d grid key: (label code, cell of the first sphere coordinate of width 8 EPS, second coordinate); a query looks in
    # the (at most two) cells that its window [x - 4EPS, x + 4EPS] meets.  (search2 used the first coordinate only: a
    # slab of width 8 EPS around a great circle, whose content grows with the table.)
    nsB = len(subB); keys = np.empty(NB_ALL * nsB); TSall = np.empty((NB_ALL * nsB, 3)); STall = np.empty(NB_ALL * nsB)
    for c0 in range(0, NB_ALL, 20000):      # in chunks (QP[:, subB] of the whole table would need ~9 kB per cover)
        c1_ = min(NB_ALL, c0 + 20000); PP = QP[c0:c1_][:, subB]
        S_ = cross(PP); K_ = gkey(lcode(QL[c0:c1_][:, subB]), np.floor((S_[..., 0] + 1) / W8), S_[..., 1])
        keys[c0 * nsB:c1_ * nsB] = K_.ravel(); TSall[c0 * nsB:c1_ * nsB] = S_.reshape(-1, 3); STall[c0 * nsB:c1_ * nsB] = condS(PP).ravel()
    S_ = K_ = PP = None
    qid = np.repeat(np.arange(NB_ALL, dtype=np.int32), nsB); qq = np.tile(np.arange(nsB, dtype=np.int32), NB_ALL)
    # tiers by the table condition number S_t: a lookup in tier k uses the window TOL*(S_q + max S_t of the tier)
    TIERS = [float(x) for x in os.environ.get('TIERS', '0,1000,inf').split(',')]; tier = np.searchsorted(TIERS, STall, 'right') - 1
    o = np.lexsort((keys, tier)); keys = keys[o]; qid = qid[o]; qq = qq[o]; TS = TSall[o]; ST = STall[o]; tier = tier[o]
    TB = [(int(np.searchsorted(tier, k)), int(np.searchsorted(tier, k, 'right')), float(ST[tier == k].max()) if (tier == k).any() else 0.0) for k in range(len(TIERS) - 1)]
    del S_, K_, TSall, STall, o, tier
    print('tiers (start, end, max S_t):', TB, flush=True)
    print(f'table {len(keys)} entries, {time.time() - t0:.0f}s', rss(), flush=True)
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
def hpdist_pts(X, Y, xs_idx, ys_idx, Dd=None):
    """40-digit chordal distances between M(X_i) and Y_j, M the Möbius map with M X[xs_idx[k]] ~ Y[ys_idx[k]], k<3."""
    def frame(p):    # columns p0*l0, p1*l1 with l0 p0 + l1 p1 = p2
        a, b, c, d = p[0][0], p[1][0], p[0][1], p[1][1]; det = a * d - b * c
        l0 = (d * p[2][0] - b * p[2][1]) / det; l1 = (-c * p[2][0] + a * p[2][1]) / det
        return ((a * l0, b * l1), (c * l0, d * l1))
    Fy = frame([Y[k] for k in ys_idx[:3]]); Fx = frame([X[k] for k in xs_idx[:3]])
    (a, b), (c, d) = Fx; det = a * d - b * c; Fi = ((d / det, -b / det), (-c / det, a / det))
    M = [[Fy[i][0] * Fi[0][j] + Fy[i][1] * Fi[1][j] for j in range(2)] for i in range(2)]
    Yn = [(y, (abs(y[0]) ** 2 + abs(y[1]) ** 2).sqrt()) for y in Y]   # (cheap)
    # entries whose double-precision distance is >= 1e-4 cannot be < 1e-20 at 40 digits: keep the double value there
    D = np.array(Dd, float) if Dd is not None else np.zeros((len(X), len(Y)))
    need = (Dd < 1e-4) if Dd is not None else np.ones((len(X), len(Y)), bool)
    for i, x in enumerate(X):
        if not need[i].any(): continue
        u0 = M[0][0] * x[0] + M[0][1] * x[1]; u1 = M[1][0] * x[0] + M[1][1] * x[1]
        nu = (abs(u0) ** 2 + abs(u1) ** 2).sqrt()
        for j in np.nonzero(need[i])[0]:
            y, ny = Yn[j]
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
    if qi not in HB: HB[qi] = hplist(table_cover(qi)[2])
    return hpdist_pts(HA[fi], HB[qi], [s[pr[k]] for k in range(4)], list(yq))
perm24 = np.array(list(itertools.permutations(range(4))))
MAXFAIL = nA - (nA + nB - 4 + 1) // 2           # nA + nB - 2 nclose <= 4  <=>  nA - nclose <= MAXFAIL
QP0 = np.ascontiguousarray(QP[:, :, 0]); QP1 = np.ascontiguousarray(QP[:, :, 1]); QL = np.ascontiguousarray(QL.astype(np.int64))
POLES = np.array([[0, 0, -1], [0, 0, 1], [1, 0, 0]], float)     # cross-ratio 0, ∞, 1 on the sphere
def kappa(S):
    """relative window factor min(1, 10 * distance of the cross-ratio to the nearest of 0, 1, ∞); see (1'')."""
    d = np.min(np.linalg.norm(S[:, None, :] - POLES[None], axis=2), 1)
    return np.minimum(1.0, 10 * d)
# S4 acts on the cross-ratio through S4/V4 = S3; these 6 orderings (all fixing the first point) give the 6 values
P6 = np.array([(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1)])
stats = {'cand': 0, 'acc_max': 0.0, 'rej_min': 1.0, 'cr_acc_max': 0.0, 'dup_skipped': 0, 'amb_skipped': 0, 'amb': 0,
         'own_orbit_entries_dropped': 0, 'self_M': 0, 'self_pairs': 0}
hist = {}; hits = []; TT = {}
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
# JOBS=k: the table is built once and k worker processes are forked (copy-on-write, so the table is in memory once);
# worker w does shard SH*k + w of NSH*k and writes its own res4_a_b_{SH*k+w}of{NSH*k}.pkl
JOBS = int(os.environ.get('JOBS', '1')); CHILDREN = []; PARENT = os.getpid()
if JOBS > 1:
    w_ = 0
    for w in range(1, JOBS):
        pid = os.fork()
        if pid == 0: w_ = w; CHILDREN = []; break
        CHILDREN.append(pid)
    SH, NSH = SH * JOBS + w_, NSH * JOBS
for fi, (p, q, an, aut) in enumerate(A['reps']):
    if fi % NSH != SH: continue
    pts, lab, ys = oddlist(an)
    # ---------------- (1a) main part: all table covers outside f's own orbit
    if not ONLYSELF:
        _t = time.perf_counter()
        SA = cross(pts[subA][:, P6]).reshape(-1, 3); lcA = np.repeat(lcode(lab[subA]), 6)
        KAP = kappa(SA)
        SQ = np.repeat(condS(pts[subA]), 6); KQ = np.minimum(1.0, KAP / 10 * 1.01 + 1e-12)   # chordal distance of the cross-ratio to 0,1,inf (capped at 1)
        if OLDWIN:
            c1 = np.floor((SA[:, 0] - 4 * EPS + 1) / W8); c2 = np.floor((SA[:, 0] + 4 * EPS + 1) / W8)
            k1 = gkey(lcA, c1, SA[:, 1]); k2 = gkey(lcA, c2, SA[:, 1])
            parts = []
            for (t0_, t1_, smax) in TB:
                if t1_ == t0_: continue
                kk_ = keys[t0_:t1_]
                lo1 = np.searchsorted(kk_, k1 - EPS * 4) + t0_; hi1 = np.searchsorted(kk_, k1 + EPS * 4, 'right') + t0_
                lo2 = np.searchsorted(kk_, k2 - EPS * 4) + t0_; hi2 = np.searchsorted(kk_, k2 + EPS * 4, 'right') + t0_
                hi2 = np.where(c2 == c1, lo2, hi2)
                parts.append((np.concatenate([lo1, lo2]), np.concatenate([hi1, hi2])))
            WQ = None
        else:
            parts = []
            for (t0_, t1_, smax) in TB:
                if t1_ == t0_: continue
                w = np.minimum(TOL * (SQ + smax) * KQ, 4 * EPS)  # >= the window of every entry of this tier (capped at search3's window)
                c1 = np.floor((SA[:, 0] - w + 1) / W8); c2 = np.floor((SA[:, 0] + w + 1) / W8)
                k1 = gkey(lcA, c1, SA[:, 1]); k2 = gkey(lcA, c2, SA[:, 1])
                kk_ = keys[t0_:t1_]
                lo1 = np.searchsorted(kk_, k1 - w) + t0_; hi1 = np.searchsorted(kk_, k1 + w, 'right') + t0_
                two = np.nonzero(c2 != c1)[0]                  # the window meets a second cell (rare)
                lo2 = lo1.copy(); hi2 = lo1.copy()
                if len(two):
                    lo2[two] = np.searchsorted(kk_, k2[two] - w[two]) + t0_; hi2[two] = np.searchsorted(kk_, k2[two] + w[two], 'right') + t0_
                assert (c2 - c1 <= 1).all()
                parts.append((np.concatenate([lo1, lo2]), np.concatenate([hi1, hi2])))
        lo = np.concatenate([p_[0] for p_ in parts]); hi = np.concatenate([p_[1] for p_ in parts])
        nrep = len(lo) // len(SA); SA2 = np.tile(SA, (nrep, 1)); KAP2 = np.tile(KAP, nrep); SQ2 = np.tile(SQ, nrep); KQ2 = np.tile(KQ, nrep) if not OLDWIN else None
        TT['lookup'] = TT.get('lookup',0) + time.perf_counter() - _t; _t = time.perf_counter()
        cnt = hi - lo
        stats['lookups'] = stats.get('lookups', 0) + int(cnt.sum())
        if cnt.sum():
            R_ = np.repeat(np.arange(len(lo)), cnt); E_ = np.repeat(lo, cnt) + (np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt))
            dd_ = np.linalg.norm(TS[E_] - SA2[R_], axis=1)
            ok = (dd_ <= EPS * 4 * KAP2[R_]) if OLDWIN else (dd_ <= np.minimum(TOL * (SQ2[R_] + ST[E_]) * KQ2[R_], 4 * EPS))
            R_ = (R_[ok] % len(SA)) // 6; E_ = E_[ok]
            if len(R_):
                u_ = np.unique(R_.astype(np.int64) * len(keys) + E_); R_ = u_ // len(keys); E_ = u_ % len(keys)
            if SAME:
                own = SRC[qid[E_], 0] == fi; stats['own_orbit_entries_dropped'] += int(own.sum()); R_ = R_[~own]; E_ = E_[~own]
            if len(R_):
                QI = qid[E_]; T_ = subB[qq[E_]]
                TT['expand'] = TT.get('expand',0) + time.perf_counter() - _t; _t = time.perf_counter()
                if NB:
                    c_, p_, nc_ = verify_nb.prefilter(pts[:, 0].copy(), pts[:, 1].copy(), lab, subA, R_.astype(np.int64), QI.astype(np.int64), T_,
                                                      QP0, QP1, QL, perm24, TOL, 4 * EPS, nB, MAXFAIL)
                    stats['cand_nb'] = stats.get('cand_nb', 0) + int(nc_)
                    R2 = R_[c_]; QI2 = QI[c_]; YQ2 = T_[c_[:, None], perm24[p_]]
                else:
                    YQ = T_[:, perm24]
                    labok = (QL[QI[:, None, None], YQ] == lab[subA[R_]][:, None, :]).all(-1)
                    c_, p_ = np.nonzero(labok)
                    R2 = R_[c_]; QI2 = QI[c_]; YQ2 = YQ[c_, p_]
                X = pts[subA[R2]]; Y = QP[QI2[:, None], YQ2]
                d = np.linalg.norm(cross(Y) - cross(X), axis=1)
                WIN = EPS * 4 * np.ones(len(d)) if OLDWIN else np.minimum(TOL * (condS(X) + condS(Y)) * np.minimum(1.0, np.maximum(kappa(cross(X)), kappa(cross(Y))) / 10 * 1.01 + 1e-12), 4 * EPS)
                ok = d <= WIN
                R2, QI2, YQ2, X, Y, d, WIN = R2[ok], QI2[ok], YQ2[ok], X[ok], Y[ok], d[ok], WIN[ok]
                TT['filter'] = TT.get('filter',0) + time.perf_counter() - _t; _t = time.perf_counter()
                if len(R2):
                    stats['cand'] += len(R2)
                    M = mob3v(X[:, :3], Y[:, :3])
                    Mf = M.reshape(len(M), 4); Mn = Mf / Mf[np.arange(len(Mf)), np.argmax(np.abs(Mf), 1)][:, None]
                    kk = np.concatenate([QI2[:, None].astype(float), np.round(Mn.real, 6), np.round(Mn.imag, 6)], 1)
                    _, ui = np.unique(kk, axis=0, return_index=True); stats['dup_skipped'] += len(R2) - len(ui)
                    R2, QI2, YQ2, M, d, WIN = R2[ui], QI2[ui], YQ2[ui], M[ui], d[ui], WIN[ui]
                    img = np.einsum('cij,nj->cni', M, pts); img /= np.linalg.norm(img, axis=2)[:, :, None]
                    D = chdist(img[:, :, None, :], QP[QI2][:, None, :, :])
                    amb = ((D > 1e-11) & (D < 1e-4)).any((1, 2))
                    nclose = (D < 1e-4).any(2).sum(1)
                    if ONE2ONE:     # the matching of a hit is one-to-one: at most (number of table points with a close image) pairs
                        ncol = (D < 1e-4).any(1).sum(1); stats['one2one_dropped'] = stats.get('one2one_dropped', 0) + int(((nA + nB - 2 * nclose <= 4) & (nA + nB - 2 * ncol > 4)).sum())
                        nclose = np.minimum(nclose, ncol)
                    skip = (nA + nB - 2 * nclose > 4) if FASTSKIP else amb & (nA + nB - 2 * nclose > 4)
                    TT['verify'] = TT.get('verify',0) + time.perf_counter() - _t; _t = time.perf_counter()
                    if DIAG:
                        for u in np.nonzero(skip)[0][:200]:
                            DIAGL.append((fi, int(QI2[u]), float(d[u]), int(nclose[u]), int(((D[u] < 1e-11)).any(1).sum()), float(np.sort(D[u].min(1))[4]), cross(pts[subA[R2[u]]][None])[0].copy(), tuple(subA[R2[u]]), tuple(lab[subA[R2[u]]])))
                    stats['amb_skipped'] += int(skip.sum()); hist['>4(skipped)'] = hist.get('>4(skipped)', 0) + int(skip.sum())
                    kq = kappa(cross(pts[subA[R2]])[:, :])
                    for u in np.nonzero(~skip)[0]:
                        qi = int(QI2[u]); yq = YQ2[u]; s = subA[R2[u]]; Du = D[u]
                        if amb[u]:
                            stats['amb'] += 1; xs3, ys3 = best_triple(Du, pts, s, yq)
                            if fi not in HA: HA[fi] = hplist(A['reps'][fi][2])
                            if qi not in HB: HB[qi] = hplist(table_cover(qi)[2])
                            Du = hpdist_pts(HA[fi], HB[qi], xs3, ys3, Du)
                            if (Du < 1e-20).any(): stats['hp_acc_max'] = max(stats.get('hp_acc_max', 0), float(Du[Du < 1e-20].max()))
                            stats['hp_rej_min'] = min(stats.get('hp_rej_min', 1), float(Du[Du >= 1e-20].min()))
                            close = Du < 1e-20
                        else: close = Du < 1e-11
                        if all(close[s[k], yq[k]] for k in range(4)):
                            stats['true_quad_cr_max'] = max(stats.get('true_quad_cr_max', 0), float(d[u]))
                            stats['true_quad_rel_max'] = max(stats.get('true_quad_rel_max', 0), float(d[u] / kq[u]))
                            stats['true_quad_win_ratio_max'] = max(stats.get('true_quad_win_ratio_max', 0), float(d[u] / WIN[u]))
                        record(fi, qi, M[u], Du, close, lab, QL[qi], s, yq, d[u])
        TT['loop'] = TT.get('loop',0) + time.perf_counter() - _t; _t = time.perf_counter()
    # ---------------- (1b) self part: q = U∘f for the table covers of f's own orbit
    _t2 = time.perf_counter()
    if SAME and os.environ.get('NOSELF') != '1' and fi in orbit:
        Sa = cross(pts[allsub]); So = cross(pts[allord])
        # canonical key: first coordinate of the cross-ratio point; window as in the main part
        o = np.argsort(Sa[:, 0]); ks = Sa[o, 0]
        lo = np.searchsorted(ks, So[:, 0] - EPS * 4); hi = np.searchsorted(ks, So[:, 0] + EPS * 4, 'right'); cnt = hi - lo
        R_ = np.repeat(np.arange(len(So)), cnt); E_ = o[np.repeat(lo, cnt) + (np.arange(cnt.sum()) - np.repeat(np.cumsum(cnt) - cnt, cnt))]
        ok = np.linalg.norm(Sa[E_] - So[R_], axis=1) <= EPS * 4; R_ = R_[ok]; E_ = E_[ok]
        stats['self_raw'] = stats.get('self_raw', 0) + len(R_); TT['self_a'] = TT.get('self_a', 0) + time.perf_counter() - _t2
        if not OLDWIN:      # the window of (5), as in the main part
            if 'SSa' not in dir() or SSa_f != fi: SSa = condS(pts[allsub]); KSa = kappa(Sa); SSa_f = fi
            SSo = condS(pts[allord[R_]]); KSo = kappa(So[R_])
            wl = np.minimum(TOL * (SSo + SSa[E_]) * np.minimum(1.0, np.maximum(KSo, KSa[E_]) / 10 * 1.01 + 1e-12), 4 * EPS)
            ok = np.linalg.norm(Sa[E_] - So[R_], axis=1) <= wl; R_ = R_[ok]; E_ = E_[ok]
        if NB:
            keepm = verify_nb.self_filter(pts[:, 0].copy(), pts[:, 1].copy(), allord[R_], allsub[E_], MAXFAIL)
            stats['self_M_nb_dropped'] = stats.get('self_M_nb_dropped', 0) + int((~keepm).sum()); R_ = R_[keepm]; E_ = E_[keepm]
        TT['self_b'] = TT.get('self_b', 0) + time.perf_counter() - _t2
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
        if ONE2ONE: nclose = np.minimum(nclose, (D < 1e-4).any(1).sum(1))
        keep = np.nonzero(nA + nB - 2 * nclose <= 4)[0]           # a necessary condition for Omega <= 4 for every U
        TT['self_pre'] = TT.get('self_pre', 0) + time.perf_counter() - _t2
        # index maps (search3 computed them inside the loop over M; they depend only on q): f point index i (over y)
        # -> position of the same point in q's list (over perm[y]); q = U∘f, q's odd point list is f's points regrouped
        PI = {}
        for qi in orbit[fi]:
            perm = AUT[SRC[qi, 1]][1]
            offs_q = {}; pos = 0
            inv = {perm[y]: y for y in range(6)}
            for yq in range(6): offs_q[yq] = pos; pos += int((ys == inv[yq]).sum())
            pi = np.empty(nA, int); cntr = {}
            for i in range(nA):
                yq = perm[ys[i]]; pi[i] = offs_q[yq] + cntr.get(yq, 0); cntr[yq] = cntr.get(yq, 0) + 1
            assert np.allclose(QP[qi][pi], pts) or np.allclose(np.abs(wedge(QP[qi][pi], pts)), 0, atol=1e-9)
            PI[qi] = pi
        for u in keep:
            Du = D[u]
            if amb[u]:
                stats['amb'] += 1
                if fi not in HA: HA[fi] = hplist(an)
                xs3, ys3 = best_triple(Du, pts, list(allord[R_[u]]), list(allsub[E_[u]]))
                Du = hpdist_pts(HA[fi], HA[fi], xs3, ys3, Du); close = Du < 1e-20
            else: close = Du < 1e-11
            # relabel for every cover of the orbit: q = U∘f, q's odd point list is f's points regrouped by perm
            for qi in orbit[fi]:
                stats['self_pairs'] += 1
                pi = PI[qi]
                Dq = np.empty_like(Du); Dq[:, pi] = Du; cq = np.zeros_like(close); cq[:, pi] = close
                record(fi, qi, M[u], Dq, cq, lab, QL[qi], None, None, None)
    TT['self'] = TT.get('self',0) + time.perf_counter() - _t2
print('timing', {k: round(v, 1) for k, v in TT.items()})
print('hist (distinct (f,q,M))', hist)
if DIAG: pickle.dump(DIAGL, open('diag.pkl', 'wb')); print('diag', len(DIAGL))
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
    p, q, _, _ = A['reps'][fi]; pb, qb, _, _ = table_cover(qi)
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
pickle.dump({'hits': hits, 'bir': bir, 'flags': flags, 'hist': hist, 'stats': stats}, open(f'res4_{a}_{b}_{SH}of{NSH}.pkl' if not OLDWIN else f'res4old_{a}_{b}_{SH}of{NSH}.pkl', 'wb'))
for pid in CHILDREN: os.waitpid(pid, 0)
if JOBS > 1 and not CHILDREN and os.getpid() != PARENT: os._exit(0)
