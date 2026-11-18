"""Rigorous pair search for bidegree (a, b), a <= b, using the certified cover lists cert_a.pkl, cert_b.pkl.
usage: python3 search_rig.py a b  ->  surv_a_b.pkl (all candidates whose rigorous lower bound for |Omega| is <= 4)

Arithmetic: midpoint-radius complex arithmetic in IEEE double (numpy), with rigorous rounding terms
(u = 2^-53; |fl(a-b)-(a-b)| <= 2u|.|, |fl(ab)-ab| <= sqrt5 u |a||b| < 4u|a||b|, division <= 8u|.|), and every
radius multiplied by (1 + 1e-12) to absorb the rounding of the radius computation itself.
Inputs: odd points from certify.py (320-bit midpoints, exact point within rho_odd = 1e-40 in each coordinate).

Logic (E12 Lemma 0, E10 sec. 2): |Omega| <= 4 forces j >= jmin = max(nA, nB) - 4 label-matched coincidences, so
among the first F = nA - jmin + 4 odd points of f at least four are matched; their ordered quadruple has the same
cross-ratio as the matched quadruple of q.  Every such pair of quadruples is found (window argument in
`lookup`).  For each found pair, M is the Mobius map of the first three points; for all other (x, y), M(x) = y iff
[num_x : den_x] = [num_y : den_y] (cross-ratios with the defining triple), tested as a ball containing 0.
2j + h <= sum_x w(x) with w = 2 (possible same-label partner), 1 (only other-label partner), 0, so
|Omega| >= nA + nB - sum w; the same from the q side; candidates with bound > 4 are excluded.
Table covers: base maps of all profile representatives of degree b with the 6 permutations of the label classes
(every degree-b cover is U o q, U in Aut(B), and U permutes the classes as an element of S3).
"""
import sys, pickle, itertools, time
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from rig import dec_f

U = 2.0 ** -53; G = 1 + 1e-12
def msub(a, ra, b, rb):
    m = a - b; return m, (ra + rb + 2 * U * np.abs(m)) * G
def mmul(a, ra, b, rb):
    m = a * b; aa, ab = np.abs(a), np.abs(b); return m, (aa * rb + ra * ab + ra * rb + 4 * U * aa * ab) * G
def mdiv(a, ra, b, rb):
    ab = np.abs(b); assert (ab > 2 * rb).all(), 'division by a ball containing 0'
    m = a / b; return m, ((np.abs(a) * rb + ra * ab) / (ab * (ab - rb) * (1 - 1e-12)) + 8 * U * np.abs(m)) * G

a, b = int(sys.argv[1]), int(sys.argv[2]); assert a <= b
CA = pickle.load(open(f'cert_{a}.pkl', 'rb')); CB = pickle.load(open(f'cert_{b}.pkl', 'rb'))
BLAB = [0, 0, 1, 1, 2, 2]
def covers(C):
    out = []
    for prof, r in sorted(C.items()):
        assert r['complete']
        for k, bb in enumerate(r['bases']):
            z = np.array([dec_f((re, im)) for y, re, im in bb['odd']])
            rz = bb['rho_odd'] * G + 2 * U * np.abs(z)
            ys = np.array([y for y, _, _ in bb['odd']]); lab = np.array([BLAB[y] for y in ys])
            out.append({'prof': prof, 'k': k, 'z': z, 'r': rz, 'ys': ys, 'lab': lab})
    return out
FA = covers(CA); FB = covers(CB)
nA, nB = 2 * a + 4, 2 * b + 4; jmin = max(nA, nB) - 4; F = nA - jmin + 4
assert all(len(c['z']) == nA for c in FA) and all(len(c['z']) == nB for c in FB)
print(f'(a,b)=({a},{b}) nA={nA} nB={nB} jmin={jmin} F={F} query covers {len(FA)} table covers {len(FB)} (x6 label perms)', flush=True)
DELTA = 1e-6

def cross(z, r, idx):
    """cross-ratio [num:den] and lambda of ordered quadruples idx (...,4)"""
    x = [z[..., idx[..., k]] if False else z[idx[..., k]] for k in range(4)]
    rx = [r[idx[..., k]] for k in range(4)]
    d13 = msub(x[0], rx[0], x[2], rx[2]); d24 = msub(x[1], rx[1], x[3], rx[3])
    d14 = msub(x[0], rx[0], x[3], rx[3]); d23 = msub(x[1], rx[1], x[2], rx[2])
    num = mmul(*d13, *d24); den = mmul(*d14, *d23)
    return num, den

def keys(num, den):
    """split into 'in' (|lambda| <= 1, kappa = lambda) and 'out' (kappa = 1/lambda)"""
    lam, rl = mdiv(*num, *den)
    inn = np.abs(lam) <= 1
    out = ~inn
    il, irl = mdiv(*den, *num) if out.any() else (lam, rl)
    kap = np.where(inn, lam, il); rk = np.where(inn, rl, irl)
    return lam, rl, kap, rk, inn

t0 = time.time()
# ---- table
quadsB = np.array([(s[0],) + p for s in itertools.combinations(range(nB), 4) for p in itertools.permutations(s[1:])])
T_key = []; T_kap = []; T_rk = []; T_q = []; T_quad = []; RL_IN = 0.0; RL_OUT = 0.0
for qi, c in enumerate(FB):
    num, den = cross(c['z'], c['r'], quadsB)
    lam, rl, kap, rk, inn = keys(num, den)
    code = (c['lab'][quadsB] * np.array([27, 9, 3, 1])).sum(1) * 2 + (~inn)
    T_key.append(code * 8.0 + kap.real + 4); T_kap.append(kap); T_rk.append(rk)
    RL_IN = max(RL_IN, float(rl[inn].max()) if inn.any() else 0.0); RL_OUT = max(RL_OUT, float(rl[~inn].max()) if (~inn).any() else 0.0)
    T_q.append(np.full(len(quadsB), qi, np.int32)); T_quad.append(np.arange(len(quadsB), dtype=np.int32))
T_key = np.concatenate(T_key); T_kap = np.concatenate(T_kap); T_rk = np.concatenate(T_rk)
T_q = np.concatenate(T_q); T_quad = np.concatenate(T_quad)
o = np.argsort(T_key); T_key, T_kap, T_rk, T_q, T_quad = T_key[o], T_kap[o], T_rk[o], T_q[o], T_quad[o]
RMAX = float(T_rk.max()); assert RMAX < 1e-8, RMAX
print(f'table lambda radius in/out {RL_IN:.1e}/{RL_OUT:.1e}'); print(f'table {len(T_key)} entries, max kappa radius {RMAX:.1e}, {time.time()-t0:.0f}s', flush=True)

PERMS3 = list(itertools.permutations(range(3)))           # pi; query labels are mapped by pi^{-1}
subsF = np.array(list(itertools.combinations(range(F), 4)))
perm24 = np.array(list(itertools.permutations(range(4))))
Qord = subsF[:, perm24].reshape(-1, 4)                      # all ordered quadruples from the first F points

stats = {'lookups': 0, 'cand': 0, 'excluded': 0, 'survivors': 0, 'max_query_rad': 0.0, 'lb_hist': {}}
surv = []
for fi, c in enumerate(FA):
    num, den = cross(c['z'], c['r'], Qord)
    lam, rl, _, _, _ = keys(num, den)
    stats['max_query_rad'] = max(stats['max_query_rad'], float(rl.max()))
    assert rl.max() < 0.1
    absl = np.abs(lam)
    # a true match with a table entry in 'in' has |lam*| <= 1 + RL_IN, so |lam_x| <= 1 + rl + RL_IN (searched);
    # with an entry in 'out', |lam*| >= 1 - RL_OUT, so |lam_x| >= 1 - rl - RL_OUT (searched, 1/lam computed there)
    sel_in = absl <= (1 + rl + RL_IN) * G + 1e-12; sel_out = absl >= (1 - rl - RL_OUT) * (1 - 1e-12) - 1e-12
    il, irl = mdiv(*den, *num)  # 1/lambda (only used where sel_out)
    for pi_i, pi in enumerate(PERMS3):
        inv = np.argsort(pi)                                # pi^{-1}
        labq = inv[c['lab']]                                # query label, as seen in the table's labels
        code0 = (labq[Qord] * np.array([27, 9, 3, 1])).sum(1) * 2
        for side, sel, kap, rk in ((0, sel_in, lam, rl), (1, sel_out, il, irl)):
            idx = np.nonzero(sel)[0]
            if not len(idx): continue
            key = (code0[idx] + side) * 8.0 + kap[idx].real + 4
            W = rk[idx] + RMAX + 1e-11
            lo = np.searchsorted(T_key, key - W); hi = np.searchsorted(T_key, key + W, 'right')
            stats['lookups'] += len(idx)
            for t, l, h in zip(idx, lo, hi):
                if h <= l: continue
                e = np.arange(l, h)
                ok = (np.abs(T_kap[e] - kap[t]) <= (T_rk[e] + rk[t]) * G + 4 * U * (np.abs(T_kap[e]) + np.abs(kap[t])) + 1e-300)
                # same code guaranteed? the window is far below the code spacing 8
                for ee in e[ok]:
                    stats['cand'] += 1
                    surv.append((fi, pi_i, int(t), int(T_q[ee]), int(T_quad[ee])))
    if fi % 50 == 0: print(f'  f {fi}/{len(FA)} cand {stats["cand"]} {time.time()-t0:.0f}s', flush=True)
print(f'candidate quadruple pairs: {stats["cand"]}, {time.time()-t0:.0f}s', flush=True)

# ---- verification of every candidate (vectorised per query cover)
from collections import defaultdict
byf = defaultdict(list)
for s in surv: byf[s[0]].append(s)
out = []
def chunks(lst, k=4000):
    for i in range(0, len(lst), k): yield lst[i:i + k]
for fi, lst0 in byf.items():
  for lst in chunks(lst0):
      c = FA[fi]; arr = np.array(lst)
      xq = Qord[arr[:, 2]]; Ny = len(arr)
      qs = arr[:, 3]; yq = quadsB[arr[:, 4]]
      Zy = np.stack([FB[q]['z'] for q in qs]); Ry = np.stack([FB[q]['r'] for q in qs]); Ly = np.stack([FB[q]['lab'] for q in qs])
      zx = c['z']; rx = c['r']
      X = [zx[xq[:, k]][:, None] for k in range(3)]; RX = [rx[xq[:, k]][:, None] for k in range(3)]
      Y = [Zy[np.arange(Ny), yq[:, k]][:, None] for k in range(3)]; RY = [Ry[np.arange(Ny), yq[:, k]][:, None] for k in range(3)]
      def nd(P, RP, z, rz):
          d13 = msub(P[0], RP[0], P[2], RP[2]); d2z = msub(P[1], RP[1], z, rz)
          d1z = msub(P[0], RP[0], z, rz); d23 = msub(P[1], RP[1], P[2], RP[2])
          return mmul(*d13, *d2z), mmul(*d1z, *d23)
      (nx, rnx), (dx, rdx) = nd(X, RX, zx[None, :], rx[None, :])          # (C, nA)
      (ny, rny), (dy, rdy) = nd(Y, RY, Zy, Ry)                           # (C, nB)
      A1 = mmul(nx[:, :, None], rnx[:, :, None], dy[:, None, :], rdy[:, None, :])
      A2 = mmul(ny[:, None, :], rny[:, None, :], dx[:, :, None], rdx[:, :, None])
      Dm, Dr = msub(*A1, *A2)
      poss = np.abs(Dm) <= Dr
      # triple points: exactly matched to their partner, nothing else
      for k in range(3):
          poss[np.arange(Ny), xq[:, k], :] = False; poss[np.arange(Ny), :, yq[:, k]] = False
          poss[np.arange(Ny), xq[:, k], yq[:, k]] = True
      pis = np.array([np.argsort(PERMS3[p]) for p in arr[:, 1]])          # pi^{-1}
      labx = np.take_along_axis(pis, np.broadcast_to(c['lab'][None, :], (Ny, nA)), 1)   # query labels in table terms
      same = labx[:, :, None] == Ly[:, None, :]
      wx = np.where((poss & same).any(2), 2, np.where(poss.any(2), 1, 0)).sum(1)
      wy = np.where((poss & same).any(1), 2, np.where(poss.any(1), 1, 0)).sum(1)
      lb = np.maximum(nA + nB - wx, nA + nB - wy)
      for v in lb: stats['lb_hist'][int(v)] = stats['lb_hist'].get(int(v), 0) + 1
      keep = np.nonzero(lb <= 4)[0]
      stats['excluded'] += Ny - len(keep)
      for k in keep:
          out.append({'fi': fi, 'pi': int(arr[k, 1]), 'xq': xq[k].tolist(), 'qi': int(qs[k]), 'yq': yq[k].tolist(),
                      'lb': int(lb[k]), 'poss': np.argwhere(poss[k]).tolist()})
stats['survivors'] = len(out)
print('stats', stats, f'{time.time()-t0:.0f}s', flush=True)
pickle.dump({'a': a, 'b': b, 'surv': out, 'stats': stats,
             'FA': [(c['prof'], c['k']) for c in FA], 'FB': [(c['prof'], c['k']) for c in FB]}, open(f'surv_{a}_{b}.pkl', 'wb'))
