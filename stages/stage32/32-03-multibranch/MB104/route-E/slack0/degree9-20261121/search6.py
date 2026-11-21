"""search6 (degree9-20261121) = search5 (degree8-20261120) for degree 9: same decisions (windows, thresholds,
pre-filter, one-to-one bound, verification, Omega bookkeeping, birationality stage), with
  (F) input = build7's L7 files (memory-mapped; odd points kept affinely, homogeneous pairs made on the fly), or
      build5/build6 L5 files (converted in memory) for comparisons; orbits from build7's orbG/orbA (L5: union-find);
  (G) table keys on an exact integer 2-D grid per tier (cell width CELLW6 x tier's largest S x TOL instead of a fixed
      1.5e-6 x-cell with float keys), built and sorted per (label code, x-slice) by compiled code (scan6_nb);
  (H) MIXED=1: only the mixed types of GOAL.md (E25 §0): (a, a) types (1,1)/(2,2) have j >= n - 3, (a, a+1) type (1,3)
      has j = n_small - 1; so jmin, Fb and MAXFAIL use that bound (fewer key subsets: (9,9) Fb 7, (8,9) Fb 5).
      Hits of the other types ((0,0) Hecke type, nested) can then be missed; they are closed by E03/E04 and E14 A+.
Original description of search5:

search5 = search4 (fast40-20261118, PR #1889) reorganised for degree 8 (research code, numerical).

What decides a hit is search4's: the same windows, thresholds, pre-filter, one-to-one bound, numpy/60-digit
verification, Omega bookkeeping, double fibre test and automatic 40-digit recheck (bircheck40).  What changes is
which pairs are looked at and where the data come from:

 (A) QUERIES = ONE COVER PER ORBIT OF G = Aut(B) x <conj>.  G acts on pairs (f, q∘M) diagonally (labels move with
     U, complex conjugation maps the problem to itself), so it suffices to take f from one G-orbit representative.
     The orbits are read off build5's confirmed symmetry images (union-find); an unconfirmed image is never merged,
     so at worst a query is done twice.  search4 took every cover of the 21 (75) representative profiles, i.e. every
     cover of a profile orbit once per element of its stabiliser.
 (B) KEY POINTS FROM ONE LABEL CLASS.  A hit has j >= jmin label-matched pairs, so at most nB - jmin odd points of q
     are unmatched and among any Fb = nB - jmin + 4 of them at least four are label-matched (search2/E21 §2.3 with
     Fa = nA).  search4 took q's first Fb points; here the Fb points are taken from q's largest label class (then the
     next, if that class is too small), so most table subsets have a pure label code (eeee, bbbb, aaaa) and a query
     only looks up its subsets of the same code: C(n_X, 4) instead of C(nA, 4) per code.
 (C) OWN Aut(B) CLASS -> SELF PART.  Table covers whose representative r' is an Aut(B)-image of f (r' = S∘f∘mu,
     confirmed by build5) are q = U∘f∘mu, so (f, q∘M) = (f, U∘f∘(mu M)): all of them are done in the self part
     over the 24 covers U∘f, with the same key-point rule (B) (selfscan).  search4 dropped only the table covers with
     representative index f and met the others in the main loop as exact four-point coincidences (most of its
     candidates at degree 7).
 (D) TABLE = one cover per coset of Stab(profile) (each cover of degree b exactly once, as in merge7.py), stored as
     (representative, coset); points rebuilt from the representative's odd points by an index map.  Table entries
     hold only (key, cover, subset); cross-ratio and S are recomputed in the compiled scan.  The table is built
     one label code at a time (memory).  Cell width per tier (env CELLW, default 4e-6 for tier 0) instead of 8 EPS.
 (E) a > b is allowed (for (7, 8) the degree-8 side is the query, the degree-7 side the table, Fb = 6).

usage: [JOBS=k] python3 search5.py a b dirA [dirB]   (dirs hold build5's L5_<n>_<tag>.pkl, L5hp_<n>_<tag>.npy)
env: QMAX (only the first QMAX queries, for tests), ALLQ=1 (every cover of the representative profiles as query, as
     search4; for comparisons), NOSELF=1, CODES=c1,c2 (only these label codes), OUT (result prefix)."""
import os, sys, glob, pickle, time, itertools, numpy as np
HERE = os.path.dirname(os.path.abspath(__file__)); SL = os.path.join(HERE, '..')
for d in ('numeric-upto5-20261118', 'speedup-20261118', 'fast40-20261118'): sys.path.insert(0, os.path.join(SL, d))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(SL, 'degree8-20261120'))
import mpmath as mp
mp.mp.dps = 60
from common import BLAB, AUT
import scan6_nb as scan_nb
a, b = int(sys.argv[1]), int(sys.argv[2]); DA = sys.argv[3]; DB = sys.argv[4] if len(sys.argv) > 4 else DA
SAME = (a == b) and os.path.samefile(DA, DB)
EPS = float(os.environ.get('EPS', '2.5e-6')); TOL = float(os.environ.get('TOL', '1e-9'))
MIDTOL = float(os.environ.get('MIDTOL', '1e-14'))   # margin check: see verify()
JOBS = int(os.environ.get('JOBS', '1')); QMAX = int(os.environ.get('QMAX', '0')); ALLQ = os.environ.get('ALLQ') == '1'
NOSELF = os.environ.get('NOSELF') == '1'; OUT = os.environ.get('OUT', f'res5_{a}_{b}')
CELLW = [float(x) for x in os.environ.get('CELLW', '4e-6,2e-5').split(',')]
TIERS = [float(x) for x in os.environ.get('TIERS', '0,1000,inf').split(',')]
nA, nB = 2 * a + 4, 2 * b + 4; MIXED = os.environ.get('MIXED') == '1'
jmin = (min(nA, nB) - (3 if a == b else 1)) if MIXED else max(nA, nB) - 4
Fb = nB - jmin + 4
assert 4 <= Fb <= nB
MAXFAIL = (nA - jmin) if MIXED else nA - (nA + nB - 4 + 1) // 2
BL = np.array(BLAB)
t0 = time.time()
def rss():
    try: return [l.split()[1] + 'kB' for l in open('/proc/self/status') if l.startswith(('VmRSS', 'VmHWM'))]
    except Exception: return ''

class OddView:
    """L['odd'][index] -> unit homogeneous pairs (..., 2) made from the affine Z / INF arrays"""
    def __init__(self, Z, INF): self.Z, self.INF = Z, INF
    def __getitem__(self, key):
        z = np.asarray(self.Z[key]); inf = np.asarray(self.INF[key]); nz = np.sqrt(1 + np.abs(z) ** 2)
        return np.where(inf[..., None], np.array([1, 0], complex), np.stack([z / nz, 1 / nz + 0j], -1))
class RowView:
    """rows of per-profile arrays addressed by the global cover index"""
    def __init__(self, parts, off): self.parts, self.off = parts, off
    def __getitem__(self, r):
        pi = int(np.searchsorted(self.off, r, 'right') - 1); return np.asarray(self.parts[pi][r - self.off[pi]])
def load(D, n):
    files7 = sorted(glob.glob(f'{D}/L7_{n}_*[0-9].pkl'))
    if files7: return load7(files7, n)
    files = sorted(glob.glob(f'{D}/L5_{n}_*.pkl')); assert files, (D, n)
    L = {k: [] for k in ('prof', 'z', 'inf', 'oddy', 'pq', 'crit', 'crity', 'aut', 'hp', 'pid', 'off', 'img', 'syms', 'profs')}
    off = 0
    for pi, fn in enumerate(files):
        d = pickle.load(open(fn, 'rb')); N = len(d['aut'])
        L['profs'].append(tuple(d['prof'])); L['off'].append(off)
        od = d['odd']; inf = np.abs(od[:, :, 1]) < 1e-300
        L['z'].append(np.where(inf, 0, od[:, :, 0] / np.where(inf, 1, od[:, :, 1]))); L['inf'].append(inf)
        L['oddy'].append(d['oddy'])
        L['pq'].append(d['pq']); L['crit'].append(d['crit']); L['crity'].append(d['crity']); L['aut'].append(d['aut'])
        L['pid'].append(np.full(N, pi)); L['hp'].append(np.load(fn.replace('/L5_', '/L5hp_').replace('.pkl', '.npy'), mmap_mode='r'))
        img = d['img'].astype(np.int64); L['img'].append(np.where(img >= 0, img + off, -1)); L['syms'].append(d['syms'])
        off += N
    out = {'n': n, 'profs': L['profs'], 'off': np.array(L['off'] + [off]), 'N': off}
    out['Z'] = np.concatenate(L['z']); out['INF'] = np.concatenate(L['inf'])
    out['oddy'] = np.concatenate([np.broadcast_to(o, (len(a_), len(o))) for o, a_ in zip(L['oddy'], L['aut'])]).astype(np.int64)
    out['aut'] = np.concatenate(L['aut']); out['pid'] = np.concatenate(L['pid'])
    out['pq'] = RowView(L['pq'], out['off']); out['crit'] = L['crit']; out['crity'] = L['crity']; out['hp'] = L['hp']
    out['odd'] = OddView(out['Z'], out['INF'])
    out['GA'] = classes_uf(out, L['img'], L['syms'], True); out['GB'] = classes_uf(out, L['img'], L['syms'], False)
    return out

def load7(files, n):
    L = {k: [] for k in ('z', 'inf', 'oddy', 'pq', 'crit', 'crity', 'aut', 'hp', 'pid', 'profs', 'orbG', 'orbA')}
    offs = []; off = 0; og = 0; oa = 0
    for pi, fn in enumerate(files):
        d = pickle.load(open(fn, 'rb')); N = d['N']; pre = fn[:-4]
        L['profs'].append(tuple(d['prof'])); offs.append(off)
        L['z'].append(np.load(pre + '_z.npy')); L['inf'].append(np.load(pre + '_inf.npy'))
        L['oddy'].append(d['oddy']); L['aut'].append(d['aut']); L['pid'].append(np.full(N, pi, np.int32))
        L['pq'].append(np.load(pre + '_pq.npy', mmap_mode='r')); L['crit'].append(np.load(pre + '_crit.npy', mmap_mode='r'))
        L['crity'].append(d['crity']); L['hp'].append(np.load(pre + '_hp.npy', mmap_mode='r'))
        # orbit ids -> representative = smallest global index of the orbit
        for key, dst in (('orbG', 'orbG'), ('orbA', 'orbA')):
            o = d[key]; first = np.full(o.max() + 1, -1, np.int64)
            for i in range(N - 1, -1, -1): first[o[i]] = i
            L[dst].append(first[o] + off)
        off += N
    out = {'n': n, 'profs': L['profs'], 'off': np.array(offs + [off]), 'N': off}
    out['Z'] = np.concatenate(L['z']); out['INF'] = np.concatenate(L['inf']); L['z'] = L['inf'] = None
    out['oddy'] = np.concatenate([np.broadcast_to(o, (len(a_), len(o))) for o, a_ in zip(L['oddy'], L['aut'])]).astype(np.int64)
    out['aut'] = np.concatenate(L['aut']); out['pid'] = np.concatenate(L['pid'])
    out['pq'] = RowView(L['pq'], out['off']); out['crit'] = L['crit']; out['crity'] = L['crity']; out['hp'] = L['hp']
    out['odd'] = OddView(out['Z'], out['INF'])
    out['GA'] = np.concatenate(L['orbG']); out['GB'] = np.concatenate(L['orbA'])
    return out

def classes_uf(Ld, IMG, SYMS, conj_too):
    """union-find over the confirmed symmetry images (conj_too: all of Stab in Aut(B) x <conj>, else Aut(B) only)"""
    par = np.arange(Ld['N'])
    def find(x):
        while par[x] != x: par[x] = par[par[x]]; x = par[x]
        return x
    for pi, (img, syms) in enumerate(zip(IMG, SYMS)):
        o = Ld['off'][pi]
        for k, (cj, perm) in enumerate(syms):
            if cj and not conj_too: continue
            for i in range(img.shape[0]):
                j = img[i, k]
                if j >= 0:
                    ra, rb = find(o + i), find(j)
                    if ra != rb: par[max(ra, rb)] = min(ra, rb)
    return np.array([find(x) for x in range(Ld['N'])])

LA = load(DA, a); LB = LA if SAME else load(DB, b)
print(f'(a,b)=({a},{b}) nA={nA} nB={nB} jmin={jmin} Fb={Fb}; degree {a}: {LA["N"]} covers in {len(LA["profs"])} profiles, '
      f'weighted {np.sum(1 / LA["aut"]):.2f}; degree {b}: {LB["N"]} covers, weighted {np.sum(1 / LB["aut"]):.2f}', flush=True)
GA = LA['GA']
QUERY = np.arange(LA['N']) if ALLQ else np.nonzero(GA == np.arange(LA['N']))[0]
if QMAX: QUERY = QUERY[:QMAX]
CLSB = LB['GB'] if SAME else np.full(LB['N'], -2, np.int64)
print(f'queries: {len(QUERY)} ({"all covers" if ALLQ else "one per Aut(B)x<conj> orbit"}); Aut(B) classes of the table side: '
      f'{len(np.unique(CLSB)) if SAME else "-"}', flush=True)

# ---------------- table covers: (representative, coset of Stab(profile)), index maps, key subsets
def cosets(prof):
    seen = set(); cos = []
    for ui, (M, perm) in enumerate(AUT):
        t2 = tuple(prof[[y for y in range(6) if perm[y] == z][0]] for z in range(6))
        if t2 in seen: continue
        seen.add(t2); cos.append(ui)
    return cos
def lcode(cl):
    l = sorted(cl); return ((l[0] * 3 + l[1]) * 3 + l[2]) * 3 + l[3]
def keypos(qcls, F):
    """positions (in q's list) of the F key points: largest label class first (stable order)"""
    cnt = np.bincount(qcls, minlength=3); order = sorted(range(3), key=lambda c: (-cnt[c], c))
    sel = []
    for c in order: sel += [k for k in range(len(qcls)) if qcls[k] == c]
    return sel[:F]
def posmap(oddy, perm):
    """odd list of U∘r (labels y -> perm[y]), in branch-point order: positions in r's list"""
    return np.array([k for yq in range(6) for k in range(len(oddy)) if perm[oddy[k]] == yq])
subF = np.array(list(itertools.combinations(range(Fb), 4)))
TPV = []    # (pi, ui, imap, qcls, subb (nsub,4) positions in q list, codes)
TREP = []; TTPV = []
for pi, prof in enumerate(LB['profs']):
    oy = LB['oddy'][LB['off'][pi]]
    for ui in cosets(prof):
        perm = AUT[ui][1]; im = posmap(oy, perm); qc = BL[np.array([perm[y] for y in oy])[im]]
        sel = np.array(keypos(qc, Fb)); sb = sel[subF]
        TPV.append((pi, ui, im, qc, sb, np.array([lcode(qc[s]) for s in sb])))
        r0, r1 = LB['off'][pi], LB['off'][pi + 1]
        TREP.append(np.arange(r0, r1)); TTPV.append(np.full(r1 - r0, len(TPV) - 1))
TREP = np.concatenate(TREP).astype(np.int32); TTPV = np.concatenate(TTPV).astype(np.int32)
IMAP = np.array([t[2] for t in TPV], np.int64); QCLS = np.array([t[3] for t in TPV], np.int64)
SUBB = np.array([t[4] for t in TPV], np.int64); SCODE = np.array([t[5] for t in TPV], np.int64)
wt = np.sum(1 / LB['aut'][TREP])
def _code_counts():      # table entries per label code (without materialising the (covers x subsets) array)
    nt = np.bincount(TTPV, minlength=len(TPV)); out = {}
    for t in range(len(TPV)):
        for c, k in zip(*np.unique(SCODE[t], return_counts=True)): out[int(c)] = out.get(int(c), 0) + int(k) * int(nt[t])
    return dict(sorted(out.items()))
print(f'table covers {len(TREP)} (weighted {wt:.2f}), {len(TPV)} (profile, coset) maps, {len(subF)} key subsets each; '
      f'codes: {_code_counts()}', flush=True)
CODES_ALL = sorted(set(SCODE.ravel().tolist()))
MERGEONLY = os.environ.get('MERGEONLY') == '1'      # only merge existing partial results and run the birationality stage
if MERGEONLY: CODES_ALL = []
if os.environ.get('CODES'): CODES_ALL = [c for c in CODES_ALL if c in [int(x) for x in os.environ['CODES'].split(',')]]

perm24 = np.array(list(itertools.permutations(range(4))), np.int64)
P6 = np.array([(0, 1, 2, 3), (0, 1, 3, 2), (0, 2, 1, 3), (0, 2, 3, 1), (0, 3, 1, 2), (0, 3, 2, 1)], np.int64)
subA_all = np.array(list(itertools.combinations(range(nA), 4)), np.int64)
def wedge(u, v): return u[..., 0] * v[..., 1] - u[..., 1] * v[..., 0]
def sph(num, den):
    d = np.abs(num) ** 2 + np.abs(den) ** 2
    z = 2 * num * np.conj(den) / d; Z = (np.abs(num) ** 2 - np.abs(den) ** 2) / d
    return np.stack([z.real, z.imag, Z], -1)
def cross(P):
    z1, z2, z3, z4 = P[..., 0, :], P[..., 1, :], P[..., 2, :], P[..., 3, :]
    return sph(wedge(z1, z3) * wedge(z2, z4), wedge(z1, z4) * wedge(z2, z3))
def condS(P):
    tot = 0
    for i, j in itertools.combinations(range(4), 2): tot = tot + 1 / np.abs(wedge(P[..., i, :], P[..., j, :]))
    return tot

XSPLIT = int(os.environ.get('XSPLIT', '1'))     # each label code is built in XSPLIT slices of the first sphere coordinate (memory)
CELLW6 = float(os.environ.get('CELLW6', '2'))   # grid cell of tier k = CELLW6 * TOL * (largest S of the tier), capped at 4 EPS
def build_table(code, h=0, k=1):
    """entries of one label code whose cross-ratio has x in slice h of k, per tier sorted by the integer grid key"""
    ntier = len(TIERS) - 1
    xlo, xhi = -1 + 2 * h / k, (-1 + 2 * (h + 1) / k) if h < k - 1 else 2.0
    TI = np.array(TIERS, float); cnt = np.zeros(ntier, np.int64)
    Z, INF = LB['Z'], LB['INF']
    scan_nb.count_entries(TREP, TTPV, IMAP, SUBB, SCODE, Z, INF, code, xlo, xhi, TI, cnt)
    if cnt.sum() == 0: return None
    tsmax = np.array([TIERS[i + 1] if np.isfinite(TIERS[i + 1]) else 3e7 for i in range(ntier)])
    W = np.minimum(CELLW6 * TOL * tsmax, 4 * EPS); NY = (np.floor(2.0 / W) + 2).astype(np.int64)
    start = np.concatenate([[0], np.cumsum(cnt)]).astype(np.int64); pos = np.zeros(ntier, np.int64)
    key = np.empty(start[-1], np.int64); TE = np.empty(start[-1], np.int32); SB = np.empty(start[-1], np.int8)
    scan_nb.fill_entries(TREP, TTPV, IMAP, SUBB, SCODE, Z, INF, code, xlo, xhi, TI, W, NY, start, pos, key, TE, SB)
    smax_last = 0.0
    for t in range(ntier):
        a_, b_ = start[t], start[t + 1]
        o = np.argsort(key[a_:b_], kind='stable'); key[a_:b_] = key[a_:b_][o]; TE[a_:b_] = TE[a_:b_][o]; SB[a_:b_] = SB[a_:b_][o]; o = None
    # the last tier's largest S is needed for the query window (as search5's smax_last)
    if cnt[-1]:
        idx = np.arange(start[-2], start[-1])
        smax_last = max(float(_condS_entry(int(TE[e]), int(SB[e]))) for e in idx[:: max(1, len(idx) // 20000)])
        smax_last = max(smax_last, 3e7)
    tsmax[-1] = max(tsmax[-1], smax_last)
    return dict(keys=key, te=TE, sb=SB, ntier=ntier, tstart=start[:-1].copy(), tend=start[1:].copy(), W=W, NY=NY, tsmax=tsmax, xlo=xlo, xhi=xhi)
def _condS_entry(te, sb):
    t = TTPV[te]; P = LB['odd'][int(TREP[te])][IMAP[t]][SUBB[t, sb]]; return condS(P[None])[0]

# ---------------- query side helpers
def fpts(fi):
    P = LA['odd'][fi]; return np.ascontiguousarray(P[:, 0]), np.ascontiguousarray(P[:, 1]), BL[LA['oddy'][fi]].astype(np.int64)
_SUBCODE = {}
def fsubs(fi, code):
    pi = LA['pid'][fi]
    if (pi, code) not in _SUBCODE:
        fl = BL[LA['oddy'][fi]]
        _SUBCODE[(pi, code)] = np.ascontiguousarray(subA_all[np.array([lcode(fl[s]) == code for s in subA_all])])
    return _SUBCODE[(pi, code)]
def tpts(te):
    r = TREP[te]; t = TTPV[te]; return LB['odd'][r][IMAP[t]], QCLS[t]

# ---------------- 60-digit distances (search4's hpdist_pts with flint)
from flint import acb, arb, ctx as fctx
fctx.prec = 240
def _acb(s):
    return acb(arb(s[0].decode()), arb(s[1].decode()))
def hplist(L, r, order=None):
    pi = L['pid'][r]; H = L['hp'][pi][r - L['off'][pi]]
    out = [(acb(1), acb(0)) if H[k][0] == b'inf' else (_acb(H[k]), acb(1)) for k in range(H.shape[0])]
    return out if order is None else [out[k] for k in order]
def hpdist_pts(X, Y, xs_idx, ys_idx, Dd):
    def frame(p):
        a_, b_, c_, d_ = p[0][0], p[1][0], p[0][1], p[1][1]; det = a_ * d_ - b_ * c_
        l0 = (d_ * p[2][0] - b_ * p[2][1]) / det; l1 = (-c_ * p[2][0] + a_ * p[2][1]) / det
        return ((a_ * l0, b_ * l1), (c_ * l0, d_ * l1))
    Fy = frame([Y[k] for k in ys_idx[:3]]); Fx = frame([X[k] for k in xs_idx[:3]])
    (a_, b_), (c_, d_) = Fx; det = a_ * d_ - b_ * c_; Fi = ((d_ / det, -b_ / det), (-c_ / det, a_ / det))
    M = [[Fy[i][0] * Fi[0][j] + Fy[i][1] * Fi[1][j] for j in range(2)] for i in range(2)]
    Yn = [(y, (abs(y[0]) ** 2 + abs(y[1]) ** 2).sqrt()) for y in Y]
    D = np.array(Dd, float); need = Dd < 1e-4
    for i, x in enumerate(X):
        if not need[i].any(): continue
        u0 = M[0][0] * x[0] + M[0][1] * x[1]; u1 = M[1][0] * x[0] + M[1][1] * x[1]
        nu = (abs(u0) ** 2 + abs(u1) ** 2).sqrt()
        for j in np.nonzero(need[i])[0]:
            y, ny = Yn[j]; D[i, j] = float((abs(u0 * y[1] - u1 * y[0]) / (nu * ny)).mid())
    return D
def best_triple(Dd, P, xs_idx, ys_idx):
    """search4.best_triple"""
    j = Dd.argmin(1); ok = Dd[np.arange(len(j)), j] < 1e-4
    ii = np.nonzero(ok)[0]; jj = j[ii]
    if len(set(jj.tolist())) != len(jj) or len(ii) < 3: return list(xs_idx[:3]), list(ys_idx[:3])
    order = np.argsort(Dd[ii, jj])[:10]; ii, jj = ii[order], jj[order]
    best = None
    for a_, b_, c_ in itertools.combinations(range(len(ii)), 3):
        sep = min(np.abs(wedge(P[ii[a_]], P[ii[b_]])), np.abs(wedge(P[ii[a_]], P[ii[c_]])), np.abs(wedge(P[ii[b_]], P[ii[c_]])))
        if best is None or sep > best[0]: best = (sep, (a_, b_, c_))
    t = best[1]; return [int(ii[k]) for k in t], [int(jj[k]) for k in t]
def mob3v(x, y):
    def frame(p):
        Mt = np.stack([p[:, 0], p[:, 1]], -1)
        lm = np.linalg.solve(Mt, p[:, 2][:, :, None])[:, :, 0]
        return Mt * lm[:, None, :]
    return frame(y) @ np.linalg.inv(frame(x))
def chdist(u, v): return np.abs(wedge(u, v)) / (np.linalg.norm(u, axis=-1) * np.linalg.norm(v, axis=-1))
POLES = np.array([[0, 0, -1], [0, 0, 1], [1, 0, 0]], float)
def kappa(S):
    d = np.min(np.linalg.norm(S[:, None, :] - POLES[None], axis=2), 1); return np.minimum(1.0, 10 * d)

stats = {'raw': 0, 'win': 0, 'cand_nb': 0, 'surv': 0, 'cand': 0, 'dup_skipped': 0, 'amb': 0, 'skip': 0,
         'acc_max': 0.0, 'rej_min': 1.0, 'cr_acc_max': 0.0, 'self_win': 0, 'self_surv': 0}
hist = {}; hits = []; mids = []
def verify(fi, pts, lab, subs, R, QX, YQ, qinfo, kind, qarr):
    """search4's numpy verification of the pre-filter survivors of one query f.  QX: table cover per survivor (or
    U index for the self part), YQ: matched q positions (4), qinfo(qx) -> (q points (nB,2), q class labels, hp-list fn)."""
    if not len(R): return
    X = pts[subs[R]]; Q = qarr(QX); Y = Q[np.arange(len(QX))[:, None], YQ]
    d = np.linalg.norm(cross(Y) - cross(X), axis=1)
    WIN = np.minimum(TOL * (condS(X) + condS(Y)) * np.minimum(1.0, np.maximum(kappa(cross(X)), kappa(cross(Y))) / 10 * 1.01 + 1e-12), 4 * EPS)
    ok = d <= WIN
    R, QX, YQ, X, Y, Q, d, WIN = R[ok], QX[ok], YQ[ok], X[ok], Y[ok], Q[ok], d[ok], WIN[ok]
    if not len(R): return
    stats['cand'] += len(R)
    M = mob3v(X[:, :3], Y[:, :3])
    Mf = M.reshape(len(M), 4); Mn = Mf / Mf[np.arange(len(Mf)), np.argmax(np.abs(Mf), 1)][:, None]
    kk = np.concatenate([QX[:, None].astype(float), np.round(Mn.real, 6), np.round(Mn.imag, 6)], 1)
    _, ui = np.unique(kk, axis=0, return_index=True); stats['dup_skipped'] += len(R) - len(ui)
    R, QX, YQ, M, Q, d, WIN = R[ui], QX[ui], YQ[ui], M[ui], Q[ui], d[ui], WIN[ui]
    img = np.einsum('cij,nj->cni', M, pts); img /= np.linalg.norm(img, axis=2)[:, :, None]
    D = chdist(img[:, :, None, :], Q[:, None, :, :])
    amb = ((D > 1e-11) & (D < 1e-4)).any((1, 2))
    nclose = np.minimum((D < 1e-4).any(2).sum(1), (D < 1e-4).any(1).sum(1))
    skip = nA + nB - 2 * nclose > 4
    stats['skip'] += int(skip.sum())
    kq = kappa(cross(pts[subs[R]]))
    for u in np.nonzero(~skip)[0]:
        qx = QX[u]; yq = YQ[u]; s = subs[R[u]]; Du = D[u]; qp, ql, qhp = qinfo(qx)
        if amb[u]:
            stats['amb'] += 1; xs3, ys3 = best_triple(Du, pts, s, yq)
            Du = hpdist_pts(hplist(LA, fi), qhp(), xs3, ys3, Du)
            if (Du < 1e-20).any(): stats['hp_acc_max'] = max(stats.get('hp_acc_max', 0), float(Du[Du < 1e-20].max()))
            stats['hp_rej_min'] = min(stats.get('hp_rej_min', 1), float(Du[Du >= 1e-20].min()))
            close = Du < 1e-20
        else: close = Du < 1e-11
        if all(close[s[k], yq[k]] for k in range(4)):
            stats['true_quad_cr_max'] = max(stats.get('true_quad_cr_max', 0), float(d[u]))
            stats['true_quad_win_ratio_max'] = max(stats.get('true_quad_win_ratio_max', 0), float(d[u] / WIN[u]))
        acc = Du[close]; rej = Du[~close]
        if acc.size: stats['acc_max'] = max(stats['acc_max'], float(acc.max()))
        if rej.size: stats['rej_min'] = min(stats['rej_min'], float(rej.min()))
        ii, jj = np.nonzero(close)
        assert len(set(ii)) == len(ii) and len(set(jj)) == len(jj)
        j = int((lab[ii] == ql[jj]).sum()); h = len(ii) - j; om = nA + nB - 2 * j - h
        hist[om] = hist.get(om, 0) + 1
        if om > 4:
            # margin check (E24 3 midcheck): accept every distance below MIDTOL instead of 1e-20 (60 digits) / 1e-11;
            # the one-to-one bound nA + nB - 2 min(#rows, #columns) is a lower bound of |Omega| for that acceptance.
            near = Du < MIDTOL; oml = nA + nB - 2 * min(int(near.any(1).sum()), int(near.any(0).sum()))
            rj = Du[(Du >= (1e-20 if amb[u] else 1e-11)) & near]      # rejected now, accepted under MIDTOL
            if oml <= 4 and rj.size:
                mids.append((int(fi), kind, int(qx), M[u], om, oml, float(rj.min()), bool(amb[u]), int(rj.size)))
        if om <= 4: hits.append((int(fi), kind, int(qx), M[u], om, j, h))

def run_scan(fi, code, Tb, cap=200000):
    f0, f1, fl = fpts(fi); subs = fsubs(fi, code)
    if not len(subs): return
    myc = int(CLSB[fi]) if SAME else -1; _t0 = time.time()
    while True:
        r, te, sb, p, cnt, full = scan_nb.scan6(f0, f1, fl, subs, perm24, P6, TOL, 4 * EPS, MAXFAIL,
                                               Tb['keys'], Tb['te'], Tb['sb'], Tb['ntier'], Tb['tstart'], Tb['tend'], Tb['W'], Tb['NY'], Tb['tsmax'], Tb['xlo'], Tb['xhi'],
                                               TREP, TTPV, IMAP, QCLS, SUBB, LB['Z'], LB['INF'], CLSB, myc, cap)
        if not full: break
        cap *= 4
    stats['raw'] += int(cnt[0]); stats['win'] += int(cnt[1]); stats['cand_nb'] += int(cnt[2]); stats['surv'] += len(r)
    for _k, _n in zip(('raw_cells', 'raw_slab', 'raw_t0', 'raw_t1', 'raw_t2plus'), cnt[3:8]): stats[_k] = stats.get(_k, 0) + int(_n)
    stats['t_scan'] = stats.get('t_scan', 0.0) + time.time() - _t0; _t0 = time.time()
    if not len(r): return
    u = np.unique(np.stack([r, te, sb, p], 1), axis=0); r, te, sb, p = u.T
    T = SUBB[TTPV[te].astype(np.int64), sb]; YQ = T[np.arange(len(T))[:, None], perm24[p]]
    pts = LA['odd'][fi]; lab = fl
    def qinfo(qx):
        qp, qc = tpts(qx); rr = TREP[qx]; t = TTPV[qx]
        return qp, qc, (lambda: hplist(LB, rr, IMAP[t]))
    verify(fi, pts, lab, subs, r, te, YQ, qinfo, 'T', lambda QX: LB['odd'][TREP[QX][:, None], IMAP[TTPV[QX]]])
    stats['t_verify'] = stats.get('t_verify', 0.0) + time.time() - _t0

# self part: the 24 covers U∘f
def self_part(fi, cap=200000):
    f0, f1, fl = fpts(fi); oy = LA['oddy'][fi]
    UMAP = np.array([posmap(oy, AUT[ui][1]) for ui in range(24)], np.int64)
    UCLS = np.array([BL[np.array([AUT[ui][1][y] for y in oy])[UMAP[ui]]] for ui in range(24)], np.int64)
    USUB = np.array([np.array(keypos(UCLS[ui], Fb))[subF] for ui in range(24)], np.int64)
    subs = subA_all
    while True:
        r, uu, sb, p, cnt, full = scan_nb.selfscan(f0, f1, fl, subs, perm24, P6, TOL, 4 * EPS, MAXFAIL, np.arange(24), UMAP, UCLS, USUB, cap)
        if not full: break
        cap *= 4
    stats['self_win'] += int(cnt[1]); stats['self_surv'] += len(r)
    if not len(r): return
    u = np.unique(np.stack([r, uu, sb, p], 1), axis=0); r, uu, sb, p = u.T
    T = USUB[uu, sb]; YQ = T[np.arange(len(T))[:, None], perm24[p]]
    pts = LA['odd'][fi]
    def qinfo(ui):
        return pts[UMAP[ui]], UCLS[ui], (lambda: hplist(LA, fi, UMAP[ui]))
    verify(fi, pts, fl, subs, r, uu, YQ, qinfo, 'U', lambda QX: pts[UMAP[QX]])

# ---------------- main: one label code at a time, JOBS workers forked after each table build
TT = {}
CHILD = None
BLK = int(os.environ.get('BLK', '2000'))          # queries per result block; every block is saved (resume after a restart)
NBLK = (len(QUERY) + BLK - 1) // BLK
def reset_stats():
    hits.clear(); hist.clear(); mids.clear()
    for k in list(stats):
        if k.startswith(('hp_', 'true_')): del stats[k]
        elif k == 'rej_min': stats[k] = 1.0
        elif isinstance(stats[k], float): stats[k] = 0.0
        else: stats[k] = 0
def run_blocks(tag, fn):
    """blocks of QUERY not yet saved as {OUT}_{tag}_b{k}.pkl, spread over JOBS forked workers"""
    todo = [k for k in range(NBLK) if not os.path.exists(f'{OUT}_{tag}_b{k}.pkl')]
    if not todo: return False
    kids = []
    for w in range(JOBS):
        pid = os.fork() if JOBS > 1 else 0
        if pid: kids.append(pid); continue
        for k in todo[w::JOBS]:
            reset_stats(); _t = time.time()
            for fi in QUERY[k * BLK:(k + 1) * BLK]: fn(int(fi))
            out = f'{OUT}_{tag}_b{k}.pkl'
            pickle.dump({'hits': hits, 'hist': hist, 'stats': stats, 'mids': mids, 'time': time.time() - _t}, open(out + '.tmp', 'wb'))
            os.replace(out + '.tmp', out)
        if JOBS > 1: os._exit(0)
        break
    for pid in kids: os.waitpid(pid, 0)
    reset_stats(); return True
for code, hx in [(c, h) for c in CODES_ALL for h in range(XSPLIT)]:
    tag = f'code{code}h{hx}'
    if all(os.path.exists(f'{OUT}_{tag}_b{k}.pkl') for k in range(NBLK)):
        print(f'{tag}: results exist, skipped', flush=True); continue
    _t = time.time(); Tb = build_table(code, hx, XSPLIT)
    if Tb is None: continue
    print(f'code {code} slice {hx}: {len(Tb["keys"])} entries, tiers {[(int(s), int(e)) for s, e in zip(Tb["tstart"], Tb["tend"])]}, '
          f'max S {Tb["tsmax"]}, built in {time.time() - _t:.0f}s', rss(), flush=True)
    run_blocks(tag, lambda fi: run_scan(fi, code, Tb))
    Tb = None
    print(f'code {code} slice {hx} done, {time.time() - t0:.0f}s', flush=True)
if SAME and not NOSELF and not MERGEONLY:
    if run_blocks('self', self_part): print(f'self part done, {time.time() - t0:.0f}s', flush=True)
# ---------------- merge the partial results, birationality (search4's double fibre test + automatic bircheck40)
parts = sorted(glob.glob(f'{OUT}_code*_b*.pkl')) + sorted(glob.glob(f'{OUT}_self_b*.pkl'))
H = []; HIST = {}; ST = {}; MIDS = []
for fn in parts:
    d = pickle.load(open(fn, 'rb')); H += d['hits']; MIDS.extend(d.get('mids', []))
    for k, v in d['hist'].items(): HIST[k] = HIST.get(k, 0) + v
    for k, v in d['stats'].items():
        if k in ('acc_max', 'cr_acc_max') or k.endswith('_max'): ST[k] = max(ST.get(k, 0.0), v)
        elif k.endswith('_min'): ST[k] = min(ST.get(k, 1.0), v)
        else: ST[k] = ST.get(k, 0) + v
    ST['core_s'] = ST.get('core_s', 0) + d['time']
print(f'margin check: candidates with |Omega| > 4, a rejected distance below {MIDTOL:g}, and one-to-one bound <= 4 if those counted: {len(MIDS)}', flush=True)
print('hist (distinct (f,q,M); q = table cover or U∘f)', dict(sorted(HIST.items(), key=lambda kv: (isinstance(kv[0], str), kv[0]))))
print('stats', ST, flush=True)
def coeffs(L, r, ui):
    n = L['n']; p, q = L['pq'][r][:n + 1], L['pq'][r][n + 1:]; Mu = AUT[ui][0]
    return Mu[0, 0] * p + Mu[0, 1] * q, Mu[1, 0] * p + Mu[1, 1] * q
def an_of(L, r):
    n = L['n']; pi = L['pid'][r]; k = r - L['off'][pi]; oy = L['oddy'][r]; cy = L['crity'][pi]; cr = L['crit'][pi][k]
    an = {}
    for y in range(6):
        od = [None if abs(L['odd'][r][j][1]) < 1e-300 else complex(L['odd'][r][j][0] / L['odd'][r][j][1]) for j in range(len(oy)) if oy[j] == y]
        an[y] = (od, [complex(c) for c, yy in zip(cr, cy) if yy == y])
    return an
def rep_tuple(L, r):
    n = L['n']; return (L['pq'][r][:n + 1], L['pq'][r][n + 1:], an_of(L, r))
rng = np.random.default_rng(5)
def evalc(p, q, t):
    n = len(p) - 1; t0_, t1_ = t[..., 0], t[..., 1]
    P = sum(p[m] * t0_ ** m * t1_ ** (n - m) for m in range(n + 1)); Qv = sum(q[m] * t0_ ** m * t1_ ** (n - m) for m in range(n + 1))
    return np.stack([P, Qv], -1)
import bircheck40
nonbir = 0; bir = []; flags = []; HQ = []
for fi, kind, qx, M, om, j, h in H:
    p, q = LA['pq'][fi][:a + 1], LA['pq'][fi][a + 1:]
    if kind == 'T': r, ui, Lq = int(TREP[qx]), int(TPV[TTPV[qx]][1]), LB
    else: r, ui, Lq = int(fi), int(qx), LA
    pb, qb = coeffs(Lq, r, ui); HQ.append((fi, kind, r, ui, M, om))
    isbir = True
    for trial in range(3):
        t = rng.normal(size=2) + 1j * rng.normal(size=2)
        v = evalc(p, q, t)
        rt = np.roots((v[1] * p - v[0] * q)[::-1]); fib = np.array([[z, 1] for z in rt], complex)
        g = evalc(pb, qb, (M @ fib.T).T); g0 = evalc(pb, qb, M @ t)
        if (chdist(g, g0[None, :]) < 1e-7).sum() < 2: break
    else: isbir = False
    if not isbir: nonbir += 1; continue
    res = bircheck40.check(('A', fi), rep_tuple(LA, fi), ('B' if kind == 'T' else 'A', r), rep_tuple(Lq, r), ui, M)
    flags.append((fi, kind, qx, om, res))
    print(f'  double says BIRATIONAL: f={fi} {kind}{qx} (rep {r}, U {ui}) |Omega|={om} -> 40 digits: {res["verdict"]}; '
          f'fibres (2nd smallest) {[f"{x[1]:.1e}" for x in res.get("fibres", [])]}; points matched {res.get("pts_matched")}/{res.get("npts")}', flush=True)
    if res['verdict'] == 'composite': nonbir += 1
    else: bir.append((fi, kind, qx, om, j, h, res['verdict']))
print(f'|Omega|<=4 hits: {len(H)}  non-birational: {nonbir}  (double-precision BIRATIONAL flags: {len(flags)}, '
      f'composite at 40 digits: {sum(f[4]["verdict"] == "composite" for f in flags)})  BIRATIONAL or unclear after 40 digits: {len(bir)}')
for x in bir[:20]: print('  BIR', x)
pickle.dump({'hits': H, 'hits_q': HQ, 'bir': bir, 'flags': flags, 'hist': HIST, 'stats': ST, 'queries': QUERY, 'mids': MIDS}, open(f'{OUT}.pkl', 'wb'))
print('done', f'{time.time() - t0:.0f}s', rss(), flush=True)
