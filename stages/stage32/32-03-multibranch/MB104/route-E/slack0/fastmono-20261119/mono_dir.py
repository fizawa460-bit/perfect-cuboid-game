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

usage: python3 mono_dir.py n t1,..,t6 --rules aut_rules_7_222222.pkl [--seed S] [--ckpt file] [--maxtime sec]"""
import sys, os, time, pickle, argparse
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE); sys.path.insert(0, os.path.join(HERE, '../speedup-20261118'))
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
    sols = []; TT = []; TUP = {}; REJ = []; ISREP = []; CONF = []; NOIMG = []
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
    def accept_tracked(Us, preds):
        """tracked endpoints: numbered numerically; if that fails, the predicted class is used (unconfirmed)"""
        out = []; cls = []
        tn = number(Us)
        for u, t, (pt, pc) in zip(Us, tn, preds):
            okan = an_of(u) is not None
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
        pickle.dump({'sols': np.array(sols), 'TT': TT, 'ISREP': ISREP, 'CONF': CONF, 'REJ': REJ, 'L': L,
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
        for u, t, r, c in zip(d['sols'], d['TT'], d['ISREP'], d['CONF']): add(u, t, c, r)
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
            if an0 is None: why['analyse'] += 1; why.setdefault('idx_analyse', []).append(si); bad += 1; continue
            sd = to_u(xg, an0); hpu = None
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
            if hpu is None and an_of(sd) is None: why['an_of'] += 1; why.setdefault('idx_an_of', []).append(si); bad += 1; continue
            t = number([sd])[0]
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
            for j in range(len(sols)):
                if j == i: continue
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
        pickle.dump(outd, open(os.environ.get('REGEN_OUT', f'regen_{tag}.pkl'), 'wb'))
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
    expanded = 0; pending = set(); tried = set(); use_images = False; seedfail = 0; rnd = 0; rescanned = False; reimaged = False; loops_left = a.loops; endgamed = False
    while W[0] < target - 1e-9 and time.time() - t0 < a.maxtime:
        rnd += 1
        jobs = {k: [] for k in range(NM)}
        for i in range(expanded, len(sols)):
            if not ISREP[i] and not use_images: continue
            for k in range(NM):
                if (k, i) in tried: continue
                pt = pred(TT[i], k); c = md.canon(pt)[0]
                if c not in TUP and c not in pending: pending.add(c); jobs[k].append((i, pt, c))
        expanded = len(sols)
        if sum(len(v) for v in jobs.values()) == 0:
            if not rescanned:                  # predictions from every cover (images too), failed ones dropped
                expanded = 0; pending.clear(); use_images = True; rescanned = True
                report(f'round {rnd} rescan with images'); continue
            if loops_left > 0:                 # random triangle loops on the tracked covers (mono.py style)
                loops_left -= 1; got = random_loop(); report(f'round {rnd} random loop -> {len(got)} new')
                if got: rescanned = False; use_images = False; expanded = 0; pending.clear()
                continue
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
        for k, lst in jobs.items():
            for s0 in range(0, len(lst), a.batch):
                chunk = [(i, pt, c) for i, pt, c in lst[s0:s0 + a.batch] if c not in TUP]
                if not chunk: continue
                for i, _, _ in chunk: tried.add((k, i))
                U0 = np.array([sols[i] for i, _, _ in chunk])
                U1, ok = run_move(U0, k)
                if (~ok).any():
                    U2, ok2 = run_move(U0[~ok], k, careful=True)
                    ii = np.nonzero(~ok)[0]; U1[ii[ok2]] = U2[ok2]; ok[ii[ok2]] = True
                stat['tracks'] += len(chunk); stat['fail'] += int((~ok).sum())
                for (i, pt, c), o in zip(chunk, ok):
                    if not o: pending.discard(c)
                good = [(pt, c) for (i, pt, c), o in zip(chunk, ok) if o]
                if not good: continue
                nw, cls = accept_tracked(list(U1[ok]), good)
                for (pt, c), cf in zip(good, cls):
                    if cf != c: pending.discard(c)
                add_images(nw)
                if time.time() - _last_save[0] > CKPT_EVERY:      # also inside long rounds (the container may restart)
                    save(); _last_save[0] = time.time()
        report(f'round {rnd}')
        save()
    report('done'); save()
    from export import export
    k, N = export({'sols': sols, 'TT': TT, 'CONF': CONF, 'REJ': REJ, 'L': L, 'fixed': fixed}, n, prof)
    print(f'wrote cov_{tag}.pkl ({k} covers passing analyse) and full_{tag}.pkl ({N})', flush=True)

if __name__ == '__main__': main()
