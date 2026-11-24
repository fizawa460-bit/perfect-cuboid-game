"""Directed monodromy solver: predict where a move sends a cover, and track only covers whose image is unknown.

Every cover carries its monodromy tuple (monodromy.py).  A half-twist of two branch points (braid.py) acts on
tuples by an explicit Hurwitz formula, so before any tracking we know which cover class the move will reach.
We track a cover along a move only when that class is still missing; each successful track then gives a new
cover, and its images under Stab(prof) in Aut(B) x <conj> are added as in mono.py.  Predictions are checked
against the tracked result (the measured tuple always decides; a wrong prediction only wastes one track).

Images under the 48 symmetries are named by autact.py's learned rules (no numerical root following), so covers
with almost-coincident critical points (where double-precision monodromy fails) are not lost.  A random share
(--verify) of the images is still numbered numerically and compared.  Covers whose class comes only from a
prediction are flagged in the output ('confirmed' False) so they can be checked at 40 digits.

usage: python3 mono_dir.py n t1,..,t6 --rules aut_rules_7_222222.pkl [--seed S] [--ckpt file] [--maxtime sec]

mono_par.py (degree9-20261121): fastmono mono_dir.py with the numba tracker (degree8-20261120/track_nb.py) and the
expensive per-chunk work (tracking, numerical numbering, analyse) spread over PAR worker processes (env PAR,
default 4).  Work goes out in waves of PAR chunks; after each wave the results are accepted and imaged in the main
process, and the next wave drops targets that are known by then (as the serial loop does chunk by chunk).
Env NOENDGAME=1 stops before the endgame (the ill-conditioned last few per cent; finished later in a second pass
from the checkpoint).  Same outputs as mono_dir.py."""
import sys, os, time, pickle, argparse
import numpy as np
import multiprocessing as mp
HERE = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'fastmono-20261119')
D8 = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'degree8-20261120')
sys.path.insert(0, D8); sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
import mono
from mono import System, track, homB, analyse, analyse_loose
import closure, monodromy as md
import fasttuples as ft
import seed as _seed
import braid
from braid import comp
from fractions import Fraction
from math import factorial
from hurwitz_char import C
from mono_rep import group_order
import autact
import hp_track
import track_nb
track_nb.install()
_G = {}
# ---- memory-light containers (2,2,3,3,3,3 at 2.5M covers took 11 GB with plain lists of tuples and arrays) ----
def tkey(c):
    """canonical tuple -> compact bytes key (entries < 256)"""
    return c if isinstance(c, bytes) else bytes([x for g in c for x in g])
class KeyDict(dict):
    """dict keyed by canonical monodromy tuples, stored as bytes"""
    def __contains__(self, c): return dict.__contains__(self, tkey(c))
    def __getitem__(self, c): return dict.__getitem__(self, tkey(c))
    def __setitem__(self, c, v): dict.__setitem__(self, tkey(c), v)
    def get(self, c, d=None): return dict.get(self, tkey(c), d)
class PackedTT:
    """list of monodromy tuples (6 permutations of n points), packed as int8 rows; items come back as tuples"""
    def __init__(self, n): self.n = n; self.blocks = []; self.cur = None; self.m = 0; self.B = 1 << 16
    def append(self, t):
        if self.m % self.B == 0: self.cur = np.zeros((self.B, 6, self.n), np.int8); self.blocks.append(self.cur)
        self.cur[self.m % self.B] = t; self.m += 1
    def __len__(self): return self.m
    def _row(self, i):
        if i < 0: i += self.m
        if not 0 <= i < self.m: raise IndexError(i)
        return self.blocks[i // self.B][i % self.B]
    def __getitem__(self, i):
        if isinstance(i, slice): return [self[j] for j in range(*i.indices(self.m))]
        return tuple(map(tuple, self._row(i).tolist()))
    def __iter__(self):
        for j in range(self.m): yield self[j]
    def array(self, start=0): return np.concatenate(self.blocks)[start:self.m] if self.blocks else np.zeros((0, 6, self.n), np.int8)
    def __reduce__(self): return (list, (list(self),))      # pickled as a plain list (export's full_ file)
class Rows:
    """growing 2-D complex array of solution vectors, in blocks; rows come back as 1-D views"""
    def __init__(self): self.blocks = []; self.cur = None; self.m = 0; self.B = 1 << 15
    def append(self, u):
        if self.m % self.B == 0: self.cur = np.zeros((self.B, len(u)), complex); self.blocks.append(self.cur)
        self.cur[self.m % self.B] = u; self.m += 1
    def __len__(self): return self.m
    def __getitem__(self, i):
        if isinstance(i, slice): return self.array()[i]
        if i < 0: i += self.m
        if not 0 <= i < self.m: raise IndexError(i)
        return self.blocks[i // self.B][i % self.B]
    def __iter__(self):
        for j in range(self.m): yield self[j]
    def array(self): return np.concatenate(self.blocks)[:self.m] if self.blocks else np.zeros((0, 0), complex)
def tt_rows(TT):
    """monodromy tuples of a checkpoint, whether stored as a list of tuples or as an int8 array"""
    if isinstance(TT, np.ndarray):
        for r in TT: yield tuple(map(tuple, r.tolist()))
    else: yield from TT

def _hpwork(job):
    """worker: one 40/80-digit track (ill-conditioned covers, where double precision cannot take the first step)"""
    u, k, dd, dps = job
    try: uh = hp_track.track_path(_G['S'], u, _G['move_path'](k, dd), dps=dps)
    except Exception: return None
    return None if uh is None else hp_track.to_np(uh)

def _work(job):
    """worker: track one chunk along move k, careful retry of failures, then number and analyse the endpoints"""
    k, U0 = job
    U1, ok = _G['run_move'](U0, k)
    if (~ok).any():
        U2, ok2 = _G['run_move'](U0[~ok], k, careful=True)
        ii = np.nonzero(~ok)[0]; U1[ii[ok2]] = U2[ok2]; ok[ii[ok2]] = True
    Us = list(U1[ok]); tn = _G['number'](Us) if Us else []
    okan = [_G['an_of'](u) is not None for u in Us]
    return U1, ok, tn, okan

# (a, b, side, w1, w2): after the half-twist, t[a] = e1 t[b] e1^-1 and t[b] = e2 t[a] e2^-1 with e = product of
# the listed generators (old tuple), every other entry unchanged.  Found by probe.py / probe2.py on 2,2,2,2,2,2
# (100% agreement on 40-60 covers each) for the base point monodromy.W0 = -0.663-0.421i.
MOVES = [(4, 3, +1, (4,), ()), (4, 3, -1, (), (3,)),
         (5, 2, +1, (5,), ()), (5, 2, -1, (), (2,)),
         (2, 4, +1, (2, 0), (0,)), (2, 4, -1, (0,), (4, 0))]

# pure braids: point a runs once around b (braid.path_loop); t[a] -> e1 t[a] e1^-1, t[b] -> e2 t[b] e2^-1, others
# unchanged.  Found by probe3.py on 2,2,2,2,2,2 (40/40 each).  Needed where the stabiliser is trivial.
LOOPS = [(0, 2, +1, (0, 2), (0,)), (0, 2, -1, (2,), (2, 0)), (0, 4, +1, (4,), (4, 0)), (0, 4, -1, (0, 4), (0,))]

def ev(t, w):
    n = len(t[0]); g = tuple(range(n))
    for i in w: g = comp(g, t[i])
    return g
def conj(t, w, x):
    e = ev(t, w); ei = [0] * len(e)
    for i, v in enumerate(e): ei[v] = i
    return comp(e, comp(x, tuple(ei)))
def predict(t, mv):
    a, b, _, w1, w2 = mv; s = list(t)
    s[a] = conj(t, w1, t[b]); s[b] = conj(t, w2, t[a]); return tuple(s)

TM = 12   # loop sampling for fasttuples (60 = monodromy.py's original)

_kept = []
def make_to_u(S, n):
    """mono.py's to_u, made robust for covers with almost-coincident critical points: the three critical points
    sent to S.fixed may be any members of their branch-point groups (all choices are tried), Newton is skipped
    when the exact Moebius transform already solves the system, and the best iterate is kept."""
    B0 = homB()
    import itertools
    def frame(pp):
        Mt = np.array([[pp[0], pp[1]], [1, 1]], complex); lm = np.linalg.solve(Mt, np.array([pp[2], 1])); return Mt * lm
    def resid(u):
        F, J, _ = S.FJ(u[None], B0[None]); return np.linalg.norm(F) / (1 + np.abs(u).max()), F[0], J[0]
    def one(x2, groups):
        cs = np.array([z for g in groups for z in g], complex)
        try:
            T = frame(cs[:3]) @ np.linalg.inv(frame(S.fixed))
            P2, Q2 = _seed.moebius_poly(x2[:n + 1], T, n), _seed.moebius_poly(x2[n + 1:], T, n)
            xx = np.concatenate([P2, Q2]); xx = xx / (xx @ S.L)
            Ti = np.linalg.inv(T); cnew = (Ti[0, 0] * cs + Ti[0, 1]) / (Ti[1, 0] * cs + Ti[1, 1])
        except (np.linalg.LinAlgError, ZeroDivisionError, FloatingPointError): return None, np.inf
        u = np.concatenate([xx, cnew[3:]])
        if not np.isfinite(u).all(): return None, np.inf
        best, bu = np.inf, None
        for _ in range(6):
            r, F, J = resid(u)
            if r < best: best, bu = r, u
            if r < 1e-12: break
            try: u = u - np.linalg.solve(J, F)
            except np.linalg.LinAlgError: break
            if not np.isfinite(u).all(): break
        return bu, best
    def to_u(x2, an2, tol=1e-9):
        if any(z is None for y in range(6) for z in an2[y][1]): return None
        first = {}
        for y in S.ys:
            if y not in first: first[y] = list(an2[y][1])
        ys_order = list(dict.fromkeys(S.ys))
        # orderings of the critical points inside each group (S.ys lists a group's critical points together)
        opts = [list(itertools.permutations(first[y])) for y in ys_order[:2]] + [[tuple(first[y])] for y in ys_order[2:]]
        best, bu = np.inf, None
        for choice in itertools.product(*opts):
            u, r = one(x2, choice)
            if r < 1e-9 * 0.01: return u
            if r < best: best, bu = r, u
        if os.environ.get('TOU_DEBUG') and best >= 1e-9: print('  to_u: best residual', best, flush=True)
        if os.environ.get('TOU_KEEP') and bu is not None: _kept.append((best, bu))
        return bu if best < tol else None
    return to_u

def _an_chunk(args):
    """worker: which covers of a chunk pass analyse in double precision (export's test)"""
    n, prof, fixed, L, U = args
    S = System(n, prof, fixed, L); out = []
    for u in U:
        p, q, cc = S.unpack(u[None])
        out.append((analyse(p[0], q[0], n, prof, cc[0], list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cc[0], list(S.ys))) is not None)
    return out

def export_lean(d, n, prof):
    """the only output build6/build7 read: full_<tag>.pkl with sols (array), tuples (int8 array (N, 6, n)), confirmed,
    in_cov_file = all.  No cov_/rej_/extra_ copies (export() kept three copies of 3M covers plus a list of 3M tuples:
    13 GB, killed on 2,3,2,3,3,3).  EXPORT_FULL=1 in mono_par's environment restores export_par."""
    S = System(n, prof, d['fixed'], d['L']); tag = f'{n}_{"".join(map(str, prof))}'
    sols = d['sols'].array() if isinstance(d['sols'], Rows) else np.asarray(d['sols'])
    TT = d['TT'].array() if isinstance(d['TT'], PackedTT) else np.array(d['TT'], np.int8)
    N = len(sols)
    pickle.dump({'sols': sols, 'ys': S.ys, 'L': d['L'], 'fixed': d['fixed'], 'tuples': TT, 'confirmed': list(d['CONF']),
                 'in_cov_file': np.arange(N)}, open(f'full_{tag}.pkl.tmp', 'wb'), protocol=4)
    os.replace(f'full_{tag}.pkl.tmp', f'full_{tag}.pkl')
    pickle.dump({'sols': np.zeros((0, sols.shape[1]), complex), 'ys': S.ys, 'REJ': d['REJ'], 'L': d['L'], 'fixed': d['fixed']},
                open(f'rej_{tag}.pkl', 'wb'))
    return N, N

def export_par(d, n, prof, pool):
    """fastmono export.export with the analyse loop spread over the worker pool (hours at 10^6 covers otherwise)"""
    import export as _ex
    sols = d['sols'].array() if isinstance(d['sols'], Rows) else np.array(d['sols']); d = dict(d, sols=sols)
    if os.environ.get('EXPORT_ANALYSE', '0') == '1':
        ch = [(n, prof, d['fixed'], d['L'], sols[k:k + 2000]) for k in range(0, len(sols), 2000)]
        oks = [o for r in (pool.map(_an_chunk, ch, chunksize=1) if pool is not None else map(_an_chunk, ch)) for o in r]
    else:
        # default: no analyse here.  build6 only reads full_ and tries refine_cov (which runs analyse itself) on every
        # cover listed in in_cov_file, falling back to refine_extra; so listing all covers loses nothing.  The cov_ file
        # then holds every cover and extra_ is empty (they are only used by the old build_all path).
        oks = [True] * len(sols)
    keepset = {i for i, o in enumerate(oks) if o}
    _orig = _ex.analyse; _cnt = [0]
    def fake(p, q, n_, prof_, cc, ys):          # export() calls analyse once per cover in order: answer from oks
        i = _cnt[0]; _cnt[0] += 1; return True if i in keepset else None
    _ex.analyse = fake; _ex.analyse_loose = lambda *a_, **k_: None
    try: return _ex.export(d, n, prof)
    finally: _ex.analyse = _orig

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('n', type=int); ap.add_argument('prof')
    ap.add_argument('--rules', required=True); ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--ckpt', default=''); ap.add_argument('--maxtime', type=float, default=1e18)
    ap.add_argument('--batch', type=int, default=300); ap.add_argument('--seedtries', type=int, default=40)
    ap.add_argument('--verify', type=float, default=0.03)
    ap.add_argument('--seedfile', default='', help='pickle list of (P, Q, crit points, branch index per crit point), e.g. composite covers')
    ap.add_argument('--loops', type=int, default=6, help='random loops to try when predictions run dry')
    a = ap.parse_args()
    n = a.n; prof = tuple(int(x) for x in a.prof.split(',')); rng = np.random.default_rng(a.seed)
    # half-twist where the two points carry the same profile entry and no fixed critical point, else full twist
    ys0 = [y for y in range(6) for _ in range(prof[y])]
    def half_ok(a_, b_):
        return prof[a_] == prof[b_] and all(ys0[k] not in (a_, b_) for k in range(3))
    MV = [(mv, half_ok(mv[0], mv[1])) for mv in MOVES] + [(lp, 'loop') for lp in LOOPS]
    NM = len(MV)
    def pred(t, k):
        mv, half = MV[k]
        if half == 'loop':
            a_, b_, _, w1, w2 = mv; s_ = list(t); s_[a_] = conj(t, w1, t[a_]); s_[b_] = conj(t, w2, t[b_]); return tuple(s_)
        t1 = predict(t, mv); return t1 if half else predict(t1, mv)
    def move_path(k, d=0.15):
        mv, half = MV[k]
        if half == 'loop': return braid.path_loop(mv[0], mv[1], r=0.3 + (d - 0.15), sense=mv[2])
        return (braid.path if half is True else braid.path_full)(mv[0], mv[1], mv[2], d=d)
    def run_move(U, k, careful=False, d=0.15):
        # careful retries: with the compiled tracker, also accept Newton steps that only reach ~1e-6 relative
        # (ill-conditioned covers; about 9% of the large degree-8 profiles fail the 1e-10 test in double precision).
        # Safe: the endpoint is numbered by its own monodromy and stored under that number, not under the prediction.
        tnb = sys.modules.get('track_nb') if careful else None
        if tnb is not None: old = tnb.NTOL[0]; tnb.NTOL[0] = float(os.environ.get('CAREFUL_NTOL', '1e-6'))
        try:
            mv, half = MV[k]; U1, ok = braid.run_path(S, U, move_path(k, d), careful=careful)
        finally:
            if tnb is not None: tnb.NTOL[0] = old
        return (braid.relabel(S, U1, mv[0], mv[1]) if half is True else U1), ok
    def endgame():
        """retry every move predicted to reach a missing class along isotopic paths (other arc offsets), carefully"""
        if os.environ.get('HPENDGAME'): return hp_endgame()
        got = []
        for dd in (0.06, 0.3, 0.45, 0.1, 0.22):
            jobs = {}
            for i in range(len(sols)):
                for k in range(NM):
                    pt = pred(TT[i], k)
                    if not md.check(pt, prof): continue
                    c = md.canon(pt)[0]
                    if c not in TUP and c not in jobs: jobs[c] = (k, i, pt)
            if not jobs: break
            for k in range(NM):
                lst = [(i, pt, c) for c, (kk, i, pt) in jobs.items() if kk == k]
                if not lst: continue
                U0 = np.array([sols[i] for i, _, _ in lst]); U1, ok = run_move(U0, k, careful=True, d=dd)
                stat['tracks'] += len(lst); stat['fail'] += int((~ok).sum())
                good = [(pt, c) for (i, pt, c), o in zip(lst, ok) if o]
                if good:
                    nw, _ = accept_tracked(list(U1[ok]), good); got += nw + add_images(nw)
            report(f'  endgame d={dd}: {len(jobs)} missing targets tried')
        # still missing: 40-digit tracking, every (cover, move) that predicts the class, two arc offsets
        allj = {}
        for i in range(len(sols)):
            for k in range(NM):
                pt = pred(TT[i], k)
                if not md.check(pt, prof): continue
                c = md.canon(pt)[0]
                if c not in TUP: allj.setdefault(c, []).append((k, i, pt))
        for c, lst in allj.items():
            # 40 digits first; then 80 (some degree-8 covers stall at 40 digits just above the 1e-24 step tolerance)
            for dps, dd, nsrc in ((40, 0.15, 8), (40, 0.3, 8), (80, 0.15, 3), (80, 0.3, 3)):
                if c in TUP: break
                for k, i, pt in lst[:nsrc]:
                    if c in TUP: break
                    mv, half = MV[k]; Ws = move_path(k, dd)
                    uh = hp_track.track_path(S, sols[i], Ws, dps=dps); stat['hp_tracks'] += 1
                    if uh is None: continue
                    un = hp_track.to_np(uh)[None]
                    if half is True: un = braid.relabel(S, un, mv[0], mv[1])
                    nw, _ = accept_tracked([un[0]], [(pt, c)]); got += nw + add_images(nw)
                    if not nw and c not in TUP:
                        # reached, but not usable in double (e.g. critical points ~1e-9 apart): finish at 80 digits and
                        # keep it under its predicted class (unconfirmed); build5 starts from the 80-digit point
                        if half is True:
                            perm = braid.relabel(S, np.arange(len(un[0]))[None].astype(complex), mv[0], mv[1])[0].real.round().astype(int)
                            uh = [uh[int(m)] for m in perm]
                        hp_track.setup(80); H = hp_track.HP(S); W0 = [tuple(hp_track.to_acb(r)) for r in B0]
                        for _ in range(12):
                            F_, J_, _ = H.FJ(uh, W0); dx = hp_track.solve(J_, F_); uh = [(x_ - d_).mid() for x_, d_ in zip(uh, dx)]
                        F_, _, _ = H.FJ(uh, W0); res = max(abs(complex(f.real.mid()) + 1j * float(f.imag.mid())) for f in F_)
                        ud = hp_track.to_np(uh); cc = np.concatenate([fixed, ud[2 * n + 2:]])
                        dmin = min(abs(cc[x] - cc[w]) for x in range(len(cc)) for w in range(x))
                        report(f'  80-digit finish of a reached target: residual {res:.1e}, smallest critical-point distance {dmin:.1e}')
                        if res < 1e-60 and dmin > 1e-30:
                            j = add(ud, pt, False, rep=True)
                            if j is not None:
                                got += [j] + add_images([j])
                                rf = f'regen_{tag}.pkl'; old_ = pickle.load(open(rf, 'rb')) if os.path.exists(rf) else {}
                                old_[j] = [(z.real.mid().str(90, radius=False), z.imag.mid().str(90, radius=False)) for z in uh]
                                pickle.dump(old_, open(rf, 'wb'))
        report(f'  endgame 40-digit: {len(allj)} missing targets')
        return got
    # symmetry rules are geometric (base point + loops), learned on any profile; look them up by (conj, perm)
    R = pickle.load(open(a.rules, 'rb'))
    rkey = {(cj, pi): w for (cj, M, pi), (pi2, w) in zip(autact.sym_list(tuple(R['prof'])), R['rules'])}
    SYMS = autact.sym_list(prof); RULES = [(pi, rkey[(cj, pi)]) for cj, M, pi in SYMS]
    assert all(r[1] is not None for r in RULES)
    print('moves', [(mv[:3], {True: 'half', False: 'full'}.get(h, h)) for mv, h in MV], '; symmetries', len(SYMS), flush=True)
    tag = f'{n}_{"".join(map(str, prof))}'; ckpt = a.ckpt or f'ckpt_dir_{tag}.pkl'
    target = float(Fraction(C(n, prof), factorial(n)))
    fixed = np.array([0.31 + 0.17j, -0.52 + 0.44j, 0.13 - 0.61j])
    import covers; covers.rng = rng
    L = rng.normal(size=2 * (n + 1)) + 1j * rng.normal(size=2 * (n + 1))
    S = System(n, prof, fixed, L); B0 = homB(); t0 = time.time()
    sols = Rows(); TT = PackedTT(n); TUP = KeyDict(); REJ = []; ISREP = []; CONF = []; NOIMG = []
    W = [0.0]
    stat = dict(tracks=0, fail=0, pred_ok=0, pred_bad=0, img=0, img_fail=0, ver_ok=0, ver_bad=0, ver_skip=0,
                unconf=0, seeds=0, hp_tracks=0)
    def an_of(u):
        p, q, cc = S.unpack(u[None])
        return analyse(p[0], q[0], n, prof, cc[0], list(S.ys)) or analyse_loose(p[0], q[0], n, prof, cc[0], list(S.ys))
    def an_simple(u):
        _, _, cc = S.unpack(u[None]); return {y: ([], [cc[0][k] for k in range(S.K) if S.ys[k] == y]) for y in range(6)}
    def add(u, t, conf, rep=False):
        cf, au = md.canon(t)
        if cf is None or cf in TUP: return None
        TUP[cf] = len(sols); W[0] += 1 / au; sols.append(u); TT.append(t); ISREP.append(rep); CONF.append(conf)
        if not conf: stat['unconf'] += 1
        return len(sols) - 1
    def number(Us):
        """numerical tuples, one by one where the batch fails; None where root following fails"""
        p, q, _ = S.unpack(np.array(Us))
        try: return ft.tuples(p, q, TM)
        except (RuntimeError, AssertionError):
            out = []
            for k in range(len(Us)):
                try: out.append(ft.tuples(p[k:k + 1], q[k:k + 1], TM)[0])
                except (RuntimeError, AssertionError): out.append(None)
            return out
    to_u = make_to_u(S, n)
    def add_images(new):
        """images of new covers under all symmetries; classes from the learned rules"""
        got = []; ver = []
        for i in new:
            u = sols[i]; t = TT[i]; x = np.concatenate(S.unpack(u[None])[:2], 1)[0]; an = an_simple(u)
            for (cj, M, pi), rule in zip(SYMS, RULES):
                t2 = autact.apply(t, rule); cf = md.canon(t2)[0]
                if cf in TUP: continue
                x2, an2 = autact.image_cover(x, an, n, cj, M, pi); u2 = to_u(x2, an2)
                if u2 is None: stat['img_fail'] += 1; NOIMG.append((i, len(got))); continue
                j = add(u2, t2, CONF[i])
                if j is not None:
                    got.append(j); stat['img'] += 1
                    if rng.random() < a.verify: ver.append(j)
        if ver:
            for j, tn in zip(ver, number([sols[j] for j in ver])):
                if tn is None or not md.check(tn, prof): stat['ver_skip'] += 1   # double precision cannot number it
                elif md.canon(tn)[0] == md.canon(TT[j])[0]: stat['ver_ok'] += 1
                else: stat['ver_bad'] += 1
        return got
    def accept_tracked(Us, preds, tn=None, okans=None):
        """tracked endpoints: numbered numerically; if that fails, the predicted class is used (unconfirmed)"""
        out = []; cls = []
        if tn is None: tn = number(Us)
        if okans is None: okans = [None] * len(Us)
        for u, t, (pt, pc), oa in zip(Us, tn, preds, okans):
            okan = (an_of(u) is not None) if oa is None else oa
            if t is not None and okan and md.check(t, prof):
                c = md.canon(t)[0]; cls.append(c)
                if c == pc: stat['pred_ok'] += 1
                else: stat['pred_bad'] += 1
                j = add(u, t, True, rep=True)
            else:
                F, _, _ = S.FJ(u[None], B0[None]); _, _, cc = S.unpack(u[None]); cs = cc[0]
                dmin = min(abs(cs[i] - cs[k]) for i in range(S.K) for k in range(i))
                if np.linalg.norm(F) < 1e-9 * (1 + np.abs(u).max()) and dmin > 1e-9:
                    j = add(u, pt, False, rep=True); cls.append(pc)
                else: REJ.append(u.copy()); j = None; cls.append(None)
            if j is not None: out.append(j)
        return out, cls
    def random_loop():
        def rnd_W():
            Wr = B0.copy(); fin = [0, 2, 3, 4, 5]
            Wr[fin, 0] = B0[fin, 0] + 2.0 * (rng.normal(size=5) + 1j * rng.normal(size=5)); return Wr
        B1, B2 = rnd_W(), rnd_W()
        idx = [i for i in range(len(sols)) if ISREP[i] and CONF[i]] or list(range(len(sols)))
        U0 = np.array([sols[i] for i in idx]); U = U0.copy(); ok = np.ones(len(U), bool)
        for Wa, Wb in ((B0, B1), (B1, B2), (B2, B0)):
            U, o, _ = track(S, U, Wa, Wb); ok &= o
        stat['tracks'] += len(U); got = []
        tn = number(list(U[ok]))
        for u, t in zip(U[ok], tn):
            if t is not None and md.check(t, prof) and an_of(u) is not None:
                j = add(u, t, True, rep=True)
                if j is not None: got.append(j)
        return got + add_images(got)
    CKPT_EVERY = float(os.environ.get('CKPT_EVERY', '240')); _last_save = [time.time()]
    def save():
        tmp = ckpt + '.tmp'
        pickle.dump({'sols': sols.array(), 'TT': TT.array(), 'ISREP': ISREP, 'CONF': CONF, 'REJ': REJ, 'L': L,
                     'fixed': fixed, 'ys': S.ys, 'rng': rng.bit_generator.state, 'stat': stat}, open(tmp, 'wb'))
        os.replace(tmp, ckpt)
    def new_seed():
        raw = []
        while not raw: raw = _seed.seq_seed(n, prof, fixed, L, rng, starts=20, verbose=False)
        u_, assign, cc_ = raw[0]; xg = u_[:2 * n + 2]; stat['seeds'] += 1
        an0 = analyse(xg[:n + 1], xg[n + 1:], n, prof, cc_, list(assign)) or analyse_loose(xg[:n + 1], xg[n + 1:], n, prof, cc_, list(assign))
        sd = to_u(xg, an0) if an0 is not None else None
        if sd is None or an_of(sd) is None: return []
        t = number([sd])[0]
        if t is None or not md.check(t, prof): return []
        j = add(sd, t, True, rep=True)
        return [] if j is None else [j] + add_images([j])
    if os.path.exists(ckpt):
        d = pickle.load(open(ckpt, 'rb')); L = d['L']; S = System(n, prof, fixed, L); to_u = make_to_u(S, n)
        rng.bit_generator.state = d['rng']; stat.update(d['stat']); REJ[:] = d['REJ']
        for u, t, r, c in zip(d['sols'], tt_rows(d['TT']), d['ISREP'], d['CONF']): add(u, t, c, r)
        del d
        stat['unconf'] = sum(not c for c in CONF)
        print(f'resumed {len(sols)} covers', flush=True)
    else:
        new_seed()
    def seed_from_file(fn):
        """start covers given explicitly (composites g o h lie in braid orbits that random seeds almost never reach)"""
        got = []; bad = 0; hpstarts = {}; why = {'analyse': 0, 'to_u': 0, 'an_of': 0, 'number': 0, 'check': 0}
        for si, (P_, Q_, cc_, as_) in enumerate(pickle.load(open(fn, 'rb'))):
            xg = np.concatenate([P_, Q_])
            an0 = analyse(P_, Q_, n, prof, np.asarray(cc_), list(as_)) or analyse_loose(P_, Q_, n, prof, np.asarray(cc_), list(as_))
            forced = False
            if an0 is None and os.environ.get('SEEDNOAN'):
                # composite seeds made in double often miss analyse's thresholds (a critical point off by 1e-7,
                # an odd point numerically double); to_u only needs the critical points: go to 80 digits directly
                an0 = {y: ([], [cc_[k] for k in range(len(as_)) if as_[k] == y]) for y in range(6)}; forced = True
            if an0 is None: why['analyse'] += 1; why.setdefault('idx_analyse', []).append(si); bad += 1; continue
            sd = None if forced else to_u(xg, an0); hpu = None
            if sd is None:
                # ill-conditioned in double (Newton stalls near 1e-8; seen for composites): finish at 80 digits,
                # keep the 80-digit point for build5 (regen file) and its double rounding for tracking/numbering
                sd0 = to_u(xg, an0, tol=1e-5)
                if sd0 is not None:
                    hp_track.setup(80); H = hp_track.HP(S); W0 = [tuple(hp_track.to_acb(r)) for r in B0]; uh = hp_track.to_acb(sd0)
                    for _ in range(12):
                        F_, J_, _ = H.FJ(uh, W0); dx = hp_track.solve(J_, F_); uh = [(x_ - d_).mid() for x_, d_ in zip(uh, dx)]
                    F_, _, _ = H.FJ(uh, W0)
                    if max(abs(complex(f.real.mid()) + 1j * float(f.imag.mid())) for f in F_) < 1e-60:
                        sd = hp_track.to_np(uh); hpu = [(z.real.mid().str(90, radius=False), z.imag.mid().str(90, radius=False)) for z in uh]
            if sd is None: why['to_u'] += 1; why.setdefault('idx_to_u', []).append(si); bad += 1; continue
            if hpu is None and an_of(sd) is None and not os.environ.get('SEEDNOANOF'): why['an_of'] += 1; why.setdefault('idx_an_of', []).append(si); bad += 1; continue
            t = number([sd])[0]
            if t is None and os.environ.get('SEEDNOAN'):
                # cannot be numbered in double: step off it along a move at 40 digits; a neighbour that can be numbered
                # starts the exploration of this braid orbit (the loop then predicts the seed's class back)
                for k in range(NM):
                    try: uh = hp_track.track_path(S, sd, move_path(k), dps=40)
                    except Exception: uh = None
                    if uh is None: continue
                    mv, half = MV[k]; un = hp_track.to_np(uh)[None]
                    if half is True: un = braid.relabel(S, un, mv[0], mv[1])
                    t2 = number([un[0]])[0]
                    if t2 is not None and md.check(t2, prof) and an_of(un[0]) is not None:
                        j = add(un[0], t2, True, rep=True)
                        why['neighbour'] = why.get('neighbour', 0) + 1
                        if j is not None: got.append(j); why['neighbour_new'] = why.get('neighbour_new', 0) + 1
                        break
                else: why['number'] += 1; why.setdefault('idx_number', []).append(si); bad += 1
                continue
            if t is None: why['number'] += 1; why.setdefault('idx_number', []).append(si); bad += 1; continue
            if not md.check(t, prof): why['check'] += 1; why.setdefault('idx_check', []).append(si); bad += 1; continue
            j = add(sd, t, True, rep=True)
            if j is not None:
                got.append(j)
                if hpu is not None: hpstarts[j] = hpu
        print('seed file: not usable because', why, '; finished at 80 digits:', sorted(hpstarts), flush=True)
        if hpstarts:            # build5 uses these as 80-digit starts (regen file, merged with an existing one)
            rf = f'regen_{tag}.pkl'; old_ = pickle.load(open(rf, 'rb')) if os.path.exists(rf) else {}
            old_.update(hpstarts); pickle.dump(old_, open(rf, 'wb'))
        return got + add_images(got), bad
    def report(msg):
        st = ' '.join(f'{k} {v}' for k, v in stat.items())
        print(f'{msg}: covers {len(sols)} weighted {W[0]:.4f}/{target} {st} rej {len(REJ)} t={time.time()-t0:.1f}s', flush=True)
    if os.environ.get('REGEN'):
        # rebuild given covers at 80 digits (for build5: covers whose double-precision position is too poor for Newton,
        # e.g. near-degenerate ones that slide to a map with a common root of P and Q): track to the cover's class
        # from other covers along predicted moves at 80 digits, Newton at 80 digits, keep the result as strings.
        import flint
        want = [int(x) for x in os.environ['REGEN'].split(',')]; outd = {}
        for i in want:
            c = md.canon(TT[i])[0]; srcs = []
            # candidate sources: the covers one move away from i (each move has its inverse in MV), found by lookup;
            # the old scan over all covers took hours at 3 million covers.  Each candidate is checked forward as before.
            cand = set()
            for k2 in range(NM):
                pt = pred(TT[i], k2)
                if not md.check(pt, prof): continue
                j = TUP.get(md.canon(pt)[0])
                if j is not None and j != i: cand.add(j)
            for j in sorted(cand):
                for k in range(NM):
                    pt = pred(TT[j], k)
                    if md.check(pt, prof) and md.canon(pt)[0] == c: srcs.append((j, k))
                if len(srcs) >= 6: break
            got = None
            for j, k in srcs:
                for dd in (0.15, 0.3):
                    mv, half = MV[k]; uh = hp_track.track_path(S, sols[j], move_path(k, dd), dps=80)
                    if uh is None: continue
                    if half is True:      # relabel at 80 digits: same permutation as braid.relabel applies to the double vector
                        ud = hp_track.to_np(uh); perm = braid.relabel(S, np.arange(len(ud))[None].astype(complex), mv[0], mv[1])[0].real.round().astype(int)
                        uh = [uh[int(m)] for m in perm]
                    H = hp_track.HP(S); W0 = [tuple(hp_track.to_acb(r)) for r in B0]
                    for _ in range(30):
                        F_, J_, _ = H.FJ(uh, W0); dx = hp_track.solve(J_, F_); uh = [(x_ - d_).mid() for x_, d_ in zip(uh, dx)]
                    F_, _, _ = H.FJ(uh, W0); res = max(abs(complex(f.real.mid()) + 1j * float(f.imag.mid())) for f in F_)
                    ud = hp_track.to_np(uh); cc = np.concatenate([fixed, ud[2 * n + 2:]])
                    dmin = min(abs(cc[x] - cc[w]) for x in range(len(cc)) for w in range(x))
                    tn = number([ud])[0]; cn = md.canon(tn)[0] if tn is not None else None
                    print(f'regen {i}: source {j} move {k} d={dd}: residual {res:.1e}, smallest crit distance {dmin:.1e}, '
                          f'class {"same" if cn == c else ("numbering failed" if cn is None else "OTHER")}', flush=True)
                    if res < 1e-60 and dmin > 1e-12 and cn in (c, None):
                        got = [(z.real.mid().str(90, radius=False), z.imag.mid().str(90, radius=False)) for z in uh]; break
                if got: break
            outd[i] = got
        rf = os.environ.get('REGEN_OUT', f'regen_{tag}.pkl'); old_ = pickle.load(open(rf, 'rb')) if os.path.exists(rf) else {}
        old_.update({i: v for i, v in outd.items() if v is not None})      # keep the 80-digit starts already there
        pickle.dump(old_, open(rf + '.tmp', 'wb')); os.replace(rf + '.tmp', rf)
        print('regen done', {i: v is not None for i, v in outd.items()}, flush=True); sys.exit(0)
    if a.seedfile:
        gotf, badf = seed_from_file(a.seedfile); report(f'seed file {a.seedfile}: {len(gotf)} new, {badf} not usable')
        if os.environ.get('SEEDONLY'):
            if _kept:       # Newton at high precision from the best double point of each seed that to_u could not finish
                import flint
                for best, u0 in _kept:
                    H = hp_track.HP(S); W0 = [tuple(hp_track.to_acb(r)) for r in B0]
                    for dps in (40, 80, 160):
                        hp_track.setup(dps); uh = hp_track.to_acb(u0); rs = []
                        for it in range(25):
                            F_, J_, _ = H.FJ(uh, W0); rs.append(max(abs(complex(f.real.mid()) + 1j * float(f.imag.mid())) for f in F_))
                            dx = hp_track.solve(J_, F_); uh = [(x_ - d_).mid() for x_, d_ in zip(uh, dx)]
                        print('  kept seed (double residual %.1e): dps %d residuals' % (best, dps), ' '.join('%.0e' % r for r in rs[::3]), flush=True)
            sys.exit(0)
    _G.update(run_move=run_move, number=number, an_of=an_of, S=S, move_path=move_path)
    if os.environ.get('PROBE'):                 # diagnose failing tracks to missing classes, then exit
        NP_ = int(os.environ['PROBE']); idx = rng.permutation(len(sols))
        miss = []
        for i in idx:
            if not ISREP[i]: continue
            for k in range(NM):
                pt = pred(TT[i], k)
                if md.check(pt, prof) and md.canon(pt)[0] not in TUP: miss.append((i, k, pt))
        print(f'probe: {len(miss)} missing-target moves from {len(idx)} sampled covers', flush=True)
        import collections; print('probe missing edges by move', collections.Counter(k for _, k, _ in miss), 'distinct targets', len(set(md.canon(pt)[0] for _, _, pt in miss)), 'distinct sources', len(set(i for i, _, _ in miss)), flush=True)
        sel = rng.permutation(len(miss))[:400]
        pickle.dump({'n': n, 'prof': prof, 'fixed': fixed, 'L': L, 'ys': S.ys, 'MV': MV,
                     'edges': [(sols[miss[j][0]].copy(), miss[j][1], miss[j][2], TT[miss[j][0]]) for j in sel]}, open(f'probe_edges_{tag}.pkl', 'wb'))
        if os.environ.get('PROBE_DUMPONLY'): sys.exit(0)
        miss = [miss[j] for j in rng.permutation(len(miss))[:NP_]]; res = []
        for i, k, pt in miss:
            u = sols[i]; _, _, cc = S.unpack(u[None]); cs = np.concatenate([fixed, cc[0]])
            dmin = min(abs(cs[x] - cs[w]) for x in range(len(cs)) for w in range(x))
            r = dict(k=k, umax=float(np.abs(u).max()), dmin=float(dmin), ccmax=float(np.abs(cc[0]).max()))
            for nm, kw in (('plain', {}), ('careful', dict(careful=True)), ('careful_d03', dict(careful=True, d=0.3))):
                U1, ok = run_move(u[None].copy(), k, **kw); r[nm] = bool(ok[0])
                if ok[0]:
                    t1 = number([U1[0]])[0]; r[nm + '_hit'] = t1 is not None and md.canon(t1)[0] == md.canon(pt)[0]
                    if nm == 'plain': break
            res.append(r); print('probe', r, flush=True)
        import collections
        print('probe by move', {k: (sum(1 for r in res if r['k'] == k), sum(1 for r in res if r['k'] == k and (r['plain'] or r.get('careful')))) for k in range(NM)}, flush=True)
        pickle.dump(res, open(f'probe_{tag}.pkl', 'wb')); sys.exit(0)
    PAR = int(os.environ.get('PAR', '4')); PIPE = os.environ.get('PIPE', '1') == '1'
    import gc; gc.collect(); gc.freeze()      # resumed runs: keep the forked workers from copying the heap
    POOL = mp.get_context('fork').Pool(PAR) if PAR > 1 else None
    OWN = os.environ.get('OWN', '')            # 'r/K': track only targets whose symmetry orbit hashes to r mod K (split one profile over K machines)
    _own = {}
    if OWN:
        import hashlib; own_r, own_K = map(int, OWN.split('/')); print(f'split mode: share {own_r} of {own_K}', flush=True)
    def owns(c):
        if not OWN: return True
        o = _own.get(c)
        if o is None:
            key = min([c] + [md.canon(autact.apply(c, rule))[0] for rule in RULES])
            o = int(hashlib.md5(repr(key).encode()).hexdigest()[:8], 16) % own_K == own_r; _own[c] = o
        return o
    def finish80(i, k, dd, pt):
        """target reached at 40 digits but not usable in double (rejected by accept_tracked): track again at 80 digits,
        Newton at 80 digits and keep it under its predicted class (unconfirmed), with the 80-digit point as build's
        regen start (the old endgame's last step, which hp_endgame had left out)"""
        mv, half = MV[k]; uh = hp_track.track_path(S, sols[i], move_path(k, dd), dps=80); stat['hp_tracks'] += 1
        if uh is None: return []
        un = hp_track.to_np(uh)[None]
        if half is True:
            perm = braid.relabel(S, np.arange(len(un[0]))[None].astype(complex), mv[0], mv[1])[0].real.round().astype(int)
            uh = [uh[int(m)] for m in perm]
        hp_track.setup(80); H = hp_track.HP(S); W0 = [tuple(hp_track.to_acb(r)) for r in B0]
        for _ in range(12):
            F_, J_, _ = H.FJ(uh, W0); dx = hp_track.solve(J_, F_); uh = [(x_ - d_).mid() for x_, d_ in zip(uh, dx)]
        F_, _, _ = H.FJ(uh, W0); res = max(abs(complex(f.real.mid()) + 1j * float(f.imag.mid())) for f in F_)
        ud = hp_track.to_np(uh); cc = np.concatenate([fixed, ud[2 * n + 2:]])
        dmin = min(abs(cc[x] - cc[w]) for x in range(len(cc)) for w in range(x))
        report(f'  80-digit finish of a reached target: residual {res:.1e}, smallest critical-point distance {dmin:.1e}')
        if not (res < 1e-60 and dmin > 1e-30): return []
        j = add(ud, pt, False, rep=True)
        if j is None: return []
        rf = f'regen_{tag}.pkl'; old_ = pickle.load(open(rf, 'rb')) if os.path.exists(rf) else {}
        old_[j] = [(z.real.mid().str(90, radius=False), z.imag.mid().str(90, radius=False)) for z in uh]
        pickle.dump(old_, open(rf, 'wb'))
        return [j] + add_images([j])
    def hp_endgame():
        """HPENDGAME=1: every missing class straight at 40 digits on the worker pool (the double-precision endgame
        cannot start from the ill-conditioned covers next to the missing ones: condition 1e10-1e13 at s = 0,
        critical points 1e-3..1e-5 apart; 40 digits takes ~5 s a track).  Waves of 4*PAR targets, so a class
        reached as an image of an earlier hit is not tracked again."""
        allj = {}
        for i in range(len(sols)):
            for k in range(NM):
                pt = pred(TT[i], k)
                if not md.check(pt, prof): continue
                c = md.canon(pt)[0]
                if c not in TUP and owns(c): allj.setdefault(tkey(c), []).append((k, i, pt))
        report(f'  hp endgame: {len(allj)} missing classes, {sum(len(v) for v in allj.values())} edges')
        got = []; nfail = 0
        confs = ((40, 0.15, 0), (40, 0.3, 0), (40, 0.15, 1), (40, 0.3, 1), (80, 0.15, 0), (40, 0.15, 2), (80, 0.3, 1))
        if os.environ.get('HPCONF'):    # e.g. HPCONF='80,0.05,0;80,0.05,1;80,0.08,0' for the last few classes (smaller detours)
            confs = tuple((int(a_), float(b_), int(c_)) for a_, b_, c_ in (x.split(',') for x in os.environ['HPCONF'].split(';')))
        for dps, dd, src in confs:
            todo = [(c, lst[src]) for c, lst in allj.items() if len(lst) > src and c not in TUP]
            if not todo: continue
            W_ = 4 * max(PAR, 1)
            for w0 in range(0, len(todo), W_):
                wave = [(c, e_) for c, e_ in todo[w0:w0 + W_] if c not in TUP]
                if not wave: continue
                jobs_ = [(sols[i].copy(), k, dd, dps) for c, (k, i, pt) in wave]
                outs = POOL.map(_hpwork, jobs_, chunksize=1) if POOL is not None else [_hpwork(j) for j in jobs_]
                for (c, (k, i, pt)), un in zip(wave, outs):
                    stat['hp_tracks'] += 1
                    if c in TUP: continue
                    if un is None: nfail += 1; continue
                    mv, half = MV[k]; un = un[None]
                    if half is True: un = braid.relabel(S, un, mv[0], mv[1])
                    nw, _ = accept_tracked([un[0]], [(pt, md.canon(pt)[0])]); got += nw + add_images(nw)
                    if not nw and c not in TUP: got += finish80(i, k, dd, pt)
                    if not nw: nfail += 1
                if time.time() - _last_save[0] > CKPT_EVERY: save(); _last_save[0] = time.time()
                if time.time() - t0 > a.maxtime: break
            report(f'  hp endgame dps {dps} d {dd} source {src}: {len(todo)} tried, {len(got)} new so far, {nfail} failed')
            if time.time() - t0 > a.maxtime: break
        save(); return got
    if os.environ.get('HPENDGAME'):
        got = hp_endgame(); report(f'hp endgame -> {len(got)} new')
    expanded = 0; pending = set(); tried = set(); use_images = False; seedfail = 0; rnd = 0; rescanned = False; reimaged = False; loops_left = a.loops; endgamed = False
    while W[0] < target - 1e-9 and time.time() - t0 < a.maxtime:
        rnd += 1
        jobs = {k: [] for k in range(NM)}
        for i in range(expanded, len(sols)):
            if not ISREP[i] and not use_images: continue
            for k in range(NM):
                if (k, i) in tried: continue
                pt = pred(TT[i], k); c = md.canon(pt)[0]
                if c not in TUP and c not in pending and owns(c): pending.add(c); jobs[k].append((i, pt, c))
        expanded = len(sols)
        if sum(len(v) for v in jobs.values()) == 0:
            if not rescanned:                  # predictions from every cover (images too), failed ones dropped
                expanded = 0; pending.clear(); use_images = True; rescanned = True
                report(f'round {rnd} rescan with images'); continue
            if loops_left > 0:                 # random triangle loops on the tracked covers (mono.py style)
                loops_left -= 1; got = random_loop(); report(f'round {rnd} random loop -> {len(got)} new')
                if got: rescanned = False; use_images = False; expanded = 0; pending.clear()
                continue
            if not endgamed and os.environ.get('NOENDGAME'):
                report(f'round {rnd} stop before endgame (NOENDGAME)'); break
            if not endgamed:
                endgamed = True; got = endgame(); report(f'round {rnd} endgame -> {len(got)} new')
                if got: rescanned = False; use_images = False; expanded = 0; pending.clear(); endgamed = False
                continue
            if not reimaged:
                reimaged = True; gotimg = add_images(list(range(len(sols))))
                report(f'round {rnd} re-image pass -> {len(gotimg)} new')
                if gotimg: rescanned = False; use_images = False; expanded = 0; pending.clear()
                continue
            nw = new_seed(); report(f'round {rnd} new seed -> {len(nw)} new')
            if nw: rescanned = False; use_images = False; seedfail = 0; reimaged = False
            else:
                seedfail += 1
                if seedfail >= a.seedtries: break
            continue
        allch = [(k, lst[s0:s0 + a.batch]) for k, lst in jobs.items() for s0 in range(0, len(lst), a.batch)]
        def handle(wave, res):
            for (k, chunk), (U1, ok, tn_, oa_) in zip(wave, res):
                stat['tracks'] += len(chunk); stat['fail'] += int((~ok).sum())
                for (i, pt, c), o in zip(chunk, ok):
                    if not o: pending.discard(c)
                good = [(pt, c) for (i, pt, c), o in zip(chunk, ok) if o]
                if not good: continue
                nw, cls = accept_tracked(list(U1[ok]), good, tn_, oa_)
                for (pt, c), cf in zip(good, cls):
                    if cf != c: pending.discard(c)
                add_images(nw)
        inflight = None      # PIPE=1: the next wave is tracked while the main process accepts and images the last one
        for w0 in range(0, len(allch), PAR):
            wave = []
            for k, raw in allch[w0:w0 + PAR]:
                chunk = [(i, pt, c) for i, pt, c in raw if c not in TUP]
                if not chunk: continue
                for i, _, _ in chunk: tried.add((k, i))
                wave.append((k, chunk))
            if not wave: continue
            jobsw = [(k, np.array([sols[i] for i, _, _ in chunk])) for k, chunk in wave]
            if POOL is not None and PIPE:
                r = POOL.map_async(_work, jobsw, chunksize=1)
                if inflight is not None: handle(inflight[0], inflight[1].get())
                inflight = (wave, r)
            else:
                handle(wave, POOL.map(_work, jobsw, chunksize=1) if POOL is not None else [_work(j) for j in jobsw])
            if time.time() - _last_save[0] > CKPT_EVERY:      # also inside long rounds (the container may restart)
                save(); _last_save[0] = time.time()
            if time.time() - t0 > a.maxtime: break
        if inflight is not None: handle(inflight[0], inflight[1].get())
        report(f'round {rnd}')
        save()
    report('done'); save()
    if os.environ.get('DELTA_OUT'):            # split mode: write only the covers found beyond the shared base, no export
        nb = int(os.environ.get('NBASE', '0'))
        pickle.dump({'sols': sols.array()[nb:], 'TT': TT.array(nb), 'ISREP': ISREP[nb:], 'CONF': CONF[nb:], 'REJ': REJ,
                     'nbase': nb, 'stat': stat}, open(os.environ['DELTA_OUT'] + '.tmp', 'wb'))
        os.replace(os.environ['DELTA_OUT'] + '.tmp', os.environ['DELTA_OUT'])
        print(f'wrote delta {len(sols) - nb} covers -> {os.environ["DELTA_OUT"]}', flush=True); return
    if os.environ.get('NOENDGAME') and not os.environ.get('EXPORT_PHASE1'): print('phase 1: no export (phase 2 writes it)', flush=True); return
    ex_ = (lambda d_: export_par(d_, n, prof, POOL)) if os.environ.get('EXPORT_FULL') == '1' else (lambda d_: export_lean(d_, n, prof))
    k, N = ex_({'sols': sols, 'TT': TT, 'CONF': CONF, 'REJ': REJ, 'L': L, 'fixed': fixed})
    print(f'wrote cov_{tag}.pkl ({k} covers passing analyse) and full_{tag}.pkl ({N})', flush=True)

if __name__ == '__main__': main()
