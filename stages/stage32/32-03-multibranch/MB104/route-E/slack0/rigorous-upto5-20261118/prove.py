"""Exact non-birationality of every survivor of search_rig.py.
usage: python3 prove.py a b  ->  proof_a_b.pkl, prints a summary; exits non-zero if any survivor is unproved.

Lemma (isolation).  Let f be a certified base map: unique exact solution of its normalized system in the box
Z_f (radius rho_u).  Let h be an exact rational map with the same branch data (crit points over the same points
of B with the same multiplicities).  Renormalize h by the exact Mobius A_h sending PHI to three of its crit
points.  If the ball enclosure of h o A_h lies in Z_f, then h o A_h = f.

V-type (q o M = U o f).  M is the exact Mobius map of the defining triple x_i -> y_i of the survivor, U in Aut(B)
with U(f(x_i)) = q(y_i).  h = U^{-1} o q o M satisfies h(x_i) = f(x_i).  By the lemma f = h o A_h, so
f(A_h^{-1} x_i) = f(x_i); A_h^{-1} x_i lies in the uniqueness rectangle of the odd point x_i, hence equals x_i;
three fixed points give A_h = id, i.e. q o M = U o f: the pair (f, q o M) is not birational.
Other survivors of the same group (same f, q, labels, numerically the same M): M0 maps every odd point x of f to
an odd point of q over U(f(x)); if the ball of M0(x'_i) lies in the uniqueness rectangle of y'_i for the triple
of that survivor, then M0(x'_i) = y'_i, so its M equals M0.

S-type (shared involution).  sigma = exact Mobius (x_a, x_a', x_c) -> (x_a', x_a, x_c') (odd points of f in equal
fibres; it swaps two points, so it is an involution).  Lemma with h = f o sigma and three isolated points gives
f o sigma = f.  tau = M sigma M^{-1}, fixed points w_1, w_2.  Lemma for q with h = q o tau: beta = tau o A_h is in
Aut(q).  q(A_h^{-1} w_k) = q(w_k) and isolation of the generic fibre at w_k (1-D Krawczyk) give A_h w_k = w_k, so
beta fixes w_1, w_2; beta has order k <= n (Aut(q) acts freely on a generic fibre), so its multiplier mu is a
k-th root of unity; |mu + 1| < 0.5 < 2 sin(pi/2n) forces mu = -1, i.e. beta = tau.  Hence q o M o sigma = q o M
and f o sigma = f with sigma != id: (f, q o M) is not birational.
"""
import sys, pickle, itertools, time
from fractions import Fraction as Fr
import numpy as np
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from rig import *

a, b = int(sys.argv[1]), int(sys.argv[2])
CA = pickle.load(open(f'cert_{a}.pkl', 'rb')); CB = pickle.load(open(f'cert_{b}.pkl', 'rb'))
SV = pickle.load(open(f'surv_{a}_{b}.pkl', 'rb'))
PERMS3 = list(itertools.permutations(range(3)))

# ---------- exact Aut(B): Gaussian rationals as pairs of Fractions
class Gq:
    def __init__(s, re, im=0): s.re = Fr(re); s.im = Fr(im)
    def __add__(s, o): return Gq(s.re + o.re, s.im + o.im)
    def __sub__(s, o): return Gq(s.re - o.re, s.im - o.im)
    def __mul__(s, o): return Gq(s.re * o.re - s.im * o.im, s.re * o.im + s.im * o.re)
    def inv(s):
        d = s.re * s.re + s.im * s.im; return Gq(s.re / d, -s.im / d)
    def iszero(s): return s.re == 0 and s.im == 0
    def acb(s): return acb(arb(s.re.numerator) / s.re.denominator, arb(s.im.numerator) / s.im.denominator)
BHq = [(Gq(0), Gq(1)), (Gq(1), Gq(0)), (Gq(1), Gq(1)), (Gq(-1), Gq(1)), (Gq(0, 1), Gq(1)), (Gq(0, -1), Gq(1))]
def heq(u, v): return (u[0] * v[1] - u[1] * v[0]).iszero()
def autB():
    out = []
    for tr in itertools.permutations(range(6), 3):
        A_, B_, C_ = BHq[tr[0]], BHq[tr[1]], BHq[tr[2]]
        # M = [B*l, A*m] (columns), M(inf)=B, M(0)=A, M(1)= l B + m A = C
        det = B_[0] * A_[1] - A_[0] * B_[1]
        l = (C_[0] * A_[1] - A_[0] * C_[1]) * det.inv(); m = (B_[0] * C_[1] - C_[0] * B_[1]) * det.inv()
        M = (B_[0] * l, A_[0] * m, B_[1] * l, A_[1] * m)
        perm = []
        for z in BHq:
            w = (M[0] * z[0] + M[1] * z[1], M[2] * z[0] + M[3] * z[1])
            k = [i for i in range(6) if heq(w, BHq[i])]
            if len(k) != 1: break
            perm.append(k[0])
        else: out.append((M, tuple(perm)))
    return out
AUTq = autB(); assert len(AUTq) == 24 and len(set(p for _, p in AUTq)) == 24
for M, p in AUTq: assert sorted(BLAB[p[y]] for y in range(6)) == sorted(BLAB) and all(BLAB[p[y]] == BLAB[p[y ^ 1]] for y in range(6))

# ---------- certified data
class Cov:
    def __init__(s, n, C, key):
        prof, k = key; r = C[prof]; bb = r['bases'][k]
        s.n = n; s.prof = prof; s.ys = r['ys']; s.S = Sys(n, s.ys)
        s.u = [dec(t) for t in bb['u']]; s.rho_u = bb['rho_u']; s.rho = bb['rho']
        s.Z = box(s.u, s.rho); s.ZU = box(s.u, s.rho_u)
        s.p, s.q, s.c = s.S.unpack(s.Z)
        s.oddy = [t[0] for t in bb['odd']]
        s.odd = [ball(dec((t[1], t[2])), bb['rho_odd']) for t in bb['odd']]       # tight enclosures
        s.oddU = [ball(dec((t[1], t[2])), bb['rho_odd_u']) for t in bb['odd']]    # uniqueness rectangles
        s.oddc = [cpx(z) for z in s.odd]
        s.pc = np.array([cpx(z) for z in s.p]); s.qc = np.array([cpx(z) for z in s.q])
    def val(s, t):  # numeric value f(t)
        return np.polyval(s.pc[::-1], t) / np.polyval(s.qc[::-1], t)
FA = [Cov(a, CA, k) for k in SV['FA']]; FB = [Cov(b, CB, k) for k in SV['FB']]

def renorm_into(cov, Ph, Qh, hcrit):
    """hcrit: list of (ball, B index) of h.  Renormalize h to cov's normal form; True if enclosure in cov.ZU.
    Returns (ok, A_h)."""
    n = cov.n; ys = cov.ys
    used = set(); chosen = []
    for j in range(3):
        cand = [k for k in range(len(hcrit)) if hcrit[k][1] == ys[j] and k not in used]
        if not cand: return False, None
        k = min(cand, key=lambda k: abs(cpx(hcrit[k][0]) - PHIc[j])); used.add(k); chosen.append(k)
    Ah = mob3(PHI, [hcrit[k][0] for k in chosen])
    P3 = mob_subst(Ph, n, Ah); Q3 = mob_subst(Qh, n, Ah)
    lx = acb(0)
    for j in range(n + 1): lx = lx + cov.S.L[j] * P3[j] + cov.S.L[n + 1 + j] * Q3[j]
    if lx.contains(0): return False, None
    e = [z / lx for z in P3 + Q3]
    Ai = mob_inv(Ah)
    for kk in range(3, len(ys)):
        cand = [k for k in range(len(hcrit)) if hcrit[k][1] == ys[kk] and k not in used]
        if not cand: return False, None
        ims = [(k, mob_apply(Ai, hcrit[k][0])) for k in cand]
        k, z = min(ims, key=lambda t: abs(cpx(t[1]) - cpx(cov.u[2 * n + 2 + kk - 3])))
        used.add(k); e.append(z)
    if len(used) != len(hcrit): return False, None
    ok = all(cov.ZU[i].contains(e[i]) for i in range(len(e)))
    return ok, Ah

def comp_left(T, P, Q):
    a_, b_, c_, d_ = T
    return [a_ * x + b_ * y for x, y in zip(P, Q)], [c_ * x + d_ * y for x, y in zip(P, Q)]

def odd_index_near(cov, z, yidx):
    """index k of the odd point of cov over B index yidx whose uniqueness rectangle contains the ball z (or None)"""
    for k, w in enumerate(cov.oddU):
        if cov.oddy[k] == yidx and w.contains(z): return k
    return None

def prove_V(f, q, xq, yq, U):
    Mq, perm = U
    Uinv = mob_inv(tuple(x.acb() for x in Mq))
    xs = [f.odd[k] for k in xq[:3]]; ysb = [q.odd[k] for k in yq[:3]]
    for i in range(3):
        if perm[f.oddy[xq[i]]] != q.oddy[yq[i]]: return False, 'U does not match the triple'
    M = mob3(xs, ysb)
    P1 = mob_subst(q.p, q.n, M); Q1 = mob_subst(q.q, q.n, M)
    Ph, Qh = comp_left(Uinv, P1, Q1)
    pinv = [perm.index(y) for y in range(6)]
    Mi = mob_inv(M)
    hcrit = [(mob_apply(Mi, q.c[k]), pinv[q.ys[k]]) for k in range(len(q.ys))]
    if sorted(y for _, y in hcrit) != sorted(f.ys): return False, 'profile mismatch'
    ok, Ah = renorm_into(f, Ph, Qh, hcrit)
    if not ok: return False, 'not in box'
    Ai = mob_inv(Ah)
    for k in xq[:3]:
        if not f.oddU[k].contains(mob_apply(Ai, f.odd[k])): return False, 'A_h not id'
    return True, M

def transfer_V(f, q, M0, perm, xq, yq):
    for i in range(3):
        if perm[f.oddy[xq[i]]] != q.oddy[yq[i]]: return False
        if not q.oddU[yq[i]].contains(mob_apply(M0, f.odd[xq[i]])): return False
    return True

def find_sigma(f):
    """numerically: involutions sigma in Aut(f), given by (x_a, x_a', x_c) -> (x_a', x_a, x_c')"""
    out = []; z = np.array(f.oddc); ys = f.oddy; nO = len(z)
    t0 = np.array([0.37 + 0.21j, -0.83 + 0.4j, 1.7 - 0.9j])
    def mob3n(x, y):
        def fr(p0, p1, p2):
            l0 = (p2 - p1) / (p0 - p1); l1 = 1 - l0; return np.array([[p0 * l0, p1 * l1], [l0, l1]])
        return fr(*y) @ np.linalg.inv(fr(*x))
    xa = 0
    for xb in range(nO):
        if xb == xa or ys[xb] != ys[xa]: continue
        xc = next(k for k in range(nO) if k not in (xa, xb))
        for xd in range(nO):
            if ys[xd] != ys[xc] or xd in (xa, xb): continue
            S_ = mob3n(z[[xa, xb, xc]], z[[xb, xa, xd]])
            tt = (S_[0, 0] * t0 + S_[0, 1]) / (S_[1, 0] * t0 + S_[1, 1])
            if np.abs(f.val(tt) - f.val(t0)).max() < 1e-8 * (1 + np.abs(f.val(t0)).max()):
                out.append((xa, xb, xc, xd))
    return out

def prove_sigma_aut(f, sg):
    xa, xb, xc, xd = sg
    sig = mob3([f.odd[xa], f.odd[xb], f.odd[xc]], [f.odd[xb], f.odd[xa], f.odd[xd]])
    Ph = mob_subst(f.p, f.n, sig); Qh = mob_subst(f.q, f.n, sig)
    si = mob_inv(sig)
    hcrit = [(mob_apply(si, f.c[k]), f.ys[k]) for k in range(len(f.ys))]
    ok, Ah = renorm_into(f, Ph, Qh, hcrit)
    if not ok: return None
    Ai = mob_inv(Ah)
    for k in (xa, xb, xc):
        if not f.oddU[k].contains(mob_apply(Ai, f.odd[k])): return None
    return sig

def fixed_points(T):
    a_, b_, c_, d_ = T
    # c z^2 + (d - a) z - b = 0
    disc = (d_ - a_) ** 2 + 4 * b_ * c_
    s = disc.sqrt()
    return [((a_ - d_) + s) / (2 * c_), ((a_ - d_) - s) / (2 * c_)]

def prove_S(f, q, xq, yq, sig, n):
    xs = [f.odd[k] for k in xq[:3]]; ysb = [q.odd[k] for k in yq[:3]]
    M = mob3(xs, ysb); Mi = mob_inv(M)
    tau = mob_mul(M, mob_mul(sig, Mi))
    if tau[2].contains(0): return False, 'tau fixes infinity (not handled)'
    ws = fixed_points(tau)
    Ph = mob_subst(q.p, q.n, tau); Qh = mob_subst(q.q, q.n, tau)
    ti = mob_inv(tau)
    hcrit = [(mob_apply(ti, q.c[k]), q.ys[k]) for k in range(len(q.ys))]
    ok, Ah = renorm_into(q, Ph, Qh, hcrit)
    if not ok: return False, 'not in box'
    Ai = mob_inv(Ah)
    for w in ws:
        v = peval(q.p, w) / peval(q.q, w)
        G_ = [x - v * y for x, y in zip(q.p, q.q)]
        wm = w.mid()
        ok1, _ = krawczyk1(G_, wm, 1e-20)
        R = ball(wm, 1e-20)
        if not (ok1 and R.contains(w) and R.contains(mob_apply(Ai, w))): return False, 'fixed point isolation'
    beta = mob_mul(tau, Ah)
    a_, b_, c_, d_ = beta
    mu = (a_ * d_ - b_ * c_) / (c_ * ws[0] + d_) ** 2
    if not (abs(mu + 1).upper() < 0.5): return False, 'multiplier'
    if 2 * np.sin(np.pi / (2 * n)) <= 0.5: return False, 'n too large for the multiplier bound'
    return True, M

# ---------- main
t0 = time.time()
groups = {}
def numM(fi, qi, s):
    x = np.array([FA[fi].oddc[k] for k in s['xq'][:3]]); y = np.array([FB[qi].oddc[k] for k in s['yq'][:3]])
    def fr(p0, p1, p2):
        l0 = (p2 - p1) / (p0 - p1); l1 = 1 - l0; return np.array([[p0 * l0, p1 * l1], [l0, l1]])
    M = fr(*y) @ np.linalg.inv(fr(*x)); return M / M.flat[np.argmax(np.abs(M))]
for s in SV['surv']:
    M = numM(s['fi'], s['qi'], s)
    groups.setdefault((s['fi'], s['qi'], s['pi']) + tuple(np.round(M.flatten(), 5)), []).append(s)
print(f'survivors {len(SV["surv"])}, groups {len(groups)}', flush=True)
res = {'V': 0, 'V_transfer': 0, 'S': 0, 'fail': []}
sigcache = {}
AUTn = [(np.array([[x.re + 1j * x.im for x in M[:2]], [x.re + 1j * x.im for x in M[2:]]], complex), p) for M, p in AUTq]
for gi, (key, mem) in enumerate(groups.items()):
    fi, qi, pi_i = key[:3]; f = FA[fi]; q = FB[qi]
    s0 = mem[0]
    Mn = numM(fi, qi, s0)
    # numeric V-type test
    tt = np.array([0.37 + 0.21j, -0.83 + 0.4j, 1.7 - 0.9j])
    gv = q.val((Mn[0, 0] * tt + Mn[0, 1]) / (Mn[1, 0] * tt + Mn[1, 1])); fv = f.val(tt)
    Ucand = []
    for (Mq, perm), (Mnum, _) in zip(AUTq, AUTn):
        Uf = (Mnum[0, 0] * fv + Mnum[0, 1]) / (Mnum[1, 0] * fv + Mnum[1, 1])
        if np.abs(Uf - gv).max() < 1e-6 * (1 + np.abs(gv).max()): Ucand.append((Mq, perm))
    done = False
    if Ucand:
        U = Ucand[0]
        ok, M0 = prove_V(f, q, s0['xq'], s0['yq'], U)
        if ok:
            res['V'] += 1; rest_fail = []
            for s in mem[1:]:
                if transfer_V(f, q, M0, U[1], s['xq'], s['yq']): res['V_transfer'] += 1
                else:
                    ok2, _ = prove_V(f, q, s['xq'], s['yq'], U)
                    if ok2: res['V'] += 1
                    else: rest_fail.append(s)
            if rest_fail: res['fail'].append((key, 'V members', len(rest_fail)))
            done = True
        else:
            print('  V proof failed', key[:3], M0, flush=True)
    if not done:
        if fi not in sigcache:
            sigs = []
            for sg in find_sigma(f):
                sig = prove_sigma_aut(f, sg)
                if sig is not None: sigs.append((sg, sig))
            sigcache[fi] = sigs
        nfail = 0
        for s in mem:
            proved = False
            for sg, sig in sigcache[fi]:
                ok, why = prove_S(f, q, s['xq'], s['yq'], sig, b)
                if ok: proved = True; break
            if proved: res['S'] += 1
            else: nfail += 1
        if nfail: res['fail'].append((key, 'S', nfail, len(sigcache[fi])))
    if gi % 200 == 0: print(f'  group {gi}/{len(groups)} V {res["V"]} transfer {res["V_transfer"]} S {res["S"]} fail {len(res["fail"])} {time.time()-t0:.0f}s', flush=True)
print('RESULT', {k: (v if k != 'fail' else len(v)) for k, v in res.items()}, f'{time.time()-t0:.0f}s')
for x in res['fail'][:20]: print('  FAIL', x)
pickle.dump(res, open(f'proof_{a}_{b}.pkl', 'wb'))
sys.exit(1 if res['fail'] else 0)
