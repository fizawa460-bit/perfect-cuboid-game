#!/usr/bin/env python3
"""Degree-6 slack-0 maps, orbit representatives under the 24 rotations of B (route F, P2 of ANSWER-14).

Same equations and the same mp verification as build_maps5.py.  Speed-ups:
  * batched Newton: many random starts solved at once with numpy (stacked 21x21 solves);
    starts whose critical points coalesce (the dominant degenerate attractor) are dropped early;
    each random batch uses a random chart (0, oo, 1 over a random label triple): maps with clustered
    critical points are badly conditioned in a fixed chart (found on degree 5, type 111212);
  * monodromy: one branch value w is moved around a random circle through its B-point and back;
    all known maps of the datum are tracked together (predictor-corrector, batched).  The end points
    are again slack-0 maps of the same datum (often new ones).  Random starts are used only to seed
    and when the monodromy stalls (the Hurwitz space may have several components);
  * float duplicate filter: a Moebius- and within-label-invariant feature vector K (sum over all
    normalising triples); only maps with a new K are refined and verified in mpmath;
  * one process per representative branch datum (27 data up to the 24 rotations of B).
Every accepted map: mp Newton refinement (dps 60, residual < 1e-38), Wronskian = the 2n-3 finite critical
points, all simple, exact degree, P,Q coprime, values as prescribed.  Distinctness: K differs; any pair with K
closer than CLOSE gets the exact coefficient identity test after a source Moebius map.  The count per datum
must reach the Burnside class count of hurwitz6.json.  Tracking errors (path jumping) cannot create false
maps: every end point is verified like a random-start solution.

Resumable: OUTDIR/state/<datum>.jsonl (one line per accepted map, fsync), <datum>.progress.json.
Usage: python -I build_maps6.py OUTDIR [--workers 11] [--batch 1024] [--only D1,D2] [--max-seconds S]
       python -I build_maps6.py OUTDIR --list
"""
import os, sys
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_k] = "1"
import argparse, hashlib, itertools, json, math, random, time
HERE = os.path.dirname(os.path.abspath(__file__))
if HERE not in sys.path: sys.path.insert(0, HERE)
import numpy as np
import mpmath as mp
import build_maps as bm
import build_maps5 as b5

n = int(os.environ.get("MAPS_N", "6"))   # 6; 5 only as a regression test against maps5
NC = 2 * n + 2          # coefficient unknowns
M = 2 * n - 5           # free critical points
NE = 2 * (2 * n - 2) + 1
BKEYS = bm.BKEYS        # ["I", "-I", "1", "-1", "0", "oo"]
PT = {"I": 1j, "-I": -1j, "1": 1 + 0j, "-1": -1 + 0j, "0": 0j, "oo": None}
CLOSE = 1e-4
DUP = 1e-7
KILL = 1e-5             # critical points closer than this (chordal) -> degenerate attractor, drop
KEEP = 1e-4
RECHART = 0.05          # before each monodromy loop, maps with smaller chordal gap move to their best chart
RNG_CENTERS = [0.3 + 0.2j, -0.7 + 1.1j, 1.9 - 0.4j]
SAMPLES = [2.0 + 0j, 0.2 + 1.1j, -0.7 + 0.3j]
KDIM = 6 * 3 * 2 + 9


# ---------- rotations of B and representative data ----------
def rotation_perms():
    def ap(g, z):
        a, b, c, d = g
        if z is None: return None if abs(c) < 1e-12 else a / c
        den = c * z + d
        return None if abs(den) < 1e-12 else (a * z + b) / den
    def lab(z):
        for k, v in PT.items():
            if (v is None and z is None) or (v is not None and z is not None and abs(z - v) < 1e-9): return k
        raise ValueError(z)
    gens = [(1j, 0, 0, 1), (1, 1, -1, 1)]
    def mulg(A, Bm):
        a, b, c, d = A; e, f, g, h = Bm
        return (a * e + b * g, a * f + b * h, c * e + d * g, c * f + d * h)
    perm = lambda g: tuple(BKEYS.index(lab(ap(g, PT[k]))) for k in BKEYS)
    grp = {perm((1, 0, 0, 1)): (1, 0, 0, 1)}; fr = [(1, 0, 0, 1)]
    while fr:
        nf = []
        for g in fr:
            for s in gens:
                h = mulg(s, g); p = perm(h)
                if p not in grp: grp[p] = h; nf.append(h)
        fr = nf
    assert len(grp) == 24
    return list(grp)


def rep_data(H):
    perms = rotation_perms()
    seen, reps = set(), []
    for d in sorted(k for k in H if not k.startswith("_")):
        if d in seen: continue
        orb = set()
        for p in perms:
            img = [0] * 6
            for i in range(6): img[p[i]] = d[i]
            orb.add("".join(img))
        seen |= orb
        if H[d][0] > 0: reps.append((d, H[d][0], len(orb)))
    return reps


# ---------- equations (batched) ----------
def canonical_vals(ns):
    """fixed chart per datum: critical points 0, oo, 1 over the first three active labels (distinct values)"""
    act = [y for y, k in zip(BKEYS, ns) if k]
    first = act[:3]
    rest = []
    for y, k in zip(BKEYS, ns): rest += [y] * (k - (1 if y in first else 0))
    return first + rest


def chart_vals(ns, rng):
    """random chart: critical points 0, oo, 1 over a random ordered triple of distinct active labels"""
    act = [y for y, k in zip(BKEYS, ns) if k]
    first = rng.sample(act, 3)
    rest = []
    for y, k in zip(BKEYS, ns): rest += [y] * (k - (1 if y in first else 0))
    return first + rest


def yvecs(vals, ystar=None, w=None):
    yx = np.array([complex(bm.BH[y][0]) for y in vals]); yz = np.array([complex(bm.BH[y][1]) for y in vals])
    if ystar is not None:
        m = np.array([y == ystar for y in vals]); yx[m] = w; yz[m] = 1.0
    return yx, yz


def fixed_v():
    k = np.arange(n + 1); V = []
    for c in ("0", "oo", "1"):
        for d in (0, 1):
            v = np.zeros(n + 1, complex)
            if c == "0": v[d] = 1.0
            elif c == "oo": v[n - d] = 1.0
            else: v[:] = 1.0 if d == 0 else k
            V.append(v)
    return np.array(V)                                             # (6, n+1)


FV = fixed_v()


def powers(lam):
    k = np.arange(n + 1)
    pw = lam[:, :, None] ** k
    d1 = np.zeros_like(pw); d1[:, :, 1:] = k[1:] * pw[:, :, :-1]
    d2 = np.zeros_like(pw); d2[:, :, 2:] = (k[2:] * (k[2:] - 1)) * pw[:, :, :-2]
    return pw, d1, d2


def system_batch(yx, yz, lam, x, ell):
    """yx, yz (10,) values of the critical points (0, oo, 1, lam...); lam (B,M); x, ell (B,NC)"""
    Bn = lam.shape[0]
    pw, d1, d2 = powers(lam)
    F = np.empty((Bn, NE), complex); J = np.zeros((Bn, NE, NE), complex)
    FR = np.concatenate([np.repeat(yz[:3], 2)[:, None] * FV, -np.repeat(yx[:3], 2)[:, None] * FV], axis=1)  # (6,NC)
    F[:, :6] = x @ FR.T; J[:, :6, :NC] = FR
    zf = yz[None, 3:, None]; xf = yx[None, 3:, None]
    R0 = np.concatenate([zf * pw, -xf * pw], axis=2)
    R1 = np.concatenate([zf * d1, -xf * d1], axis=2)
    D1 = np.concatenate([zf * d2, -xf * d2], axis=2)
    idx = np.arange(M); r0 = 6 + 2 * idx; r1 = r0 + 1
    F[:, r0] = np.einsum("bmk,bk->bm", R0, x); F[:, r1] = np.einsum("bmk,bk->bm", R1, x)
    J[:, r0, :NC] = R0; J[:, r1, :NC] = R1
    J[:, r0, NC + idx] = np.einsum("bmk,bk->bm", R1, x)
    J[:, r1, NC + idx] = np.einsum("bmk,bk->bm", D1, x)
    F[:, -1] = np.einsum("bk,bk->b", ell, x) - 1; J[:, -1, :NC] = ell
    return F, J


def dF_dw(mask, lam, x):
    """derivative of F with respect to the moving value w (yx = w, yz = 1 on the masked critical points)"""
    Bn = lam.shape[0]; out = np.zeros((Bn, NE), complex)
    Q = x[:, n + 1:]
    for r in range(6):
        if mask[r // 2]: out[:, r] = -(Q @ FV[r])
    pw, d1, _ = powers(lam)
    for j in range(M):
        if mask[3 + j]:
            out[:, 6 + 2 * j] = -np.einsum("bk,bk->b", pw[:, j], Q)
            out[:, 7 + 2 * j] = -np.einsum("bk,bk->b", d1[:, j], Q)
    return out


def min_chord(lam):
    pts = np.concatenate([np.zeros((lam.shape[0], 1)), np.ones((lam.shape[0], 1)), lam], axis=1)
    s = np.sqrt(1 + np.abs(pts) ** 2)
    with np.errstate(invalid="ignore", over="ignore"):
        d = np.abs(pts[:, :, None] - pts[:, None, :]) / (s[:, :, None] * s[:, None, :])
    i = np.arange(pts.shape[1]); d[:, i, i] = np.inf
    out = np.minimum(d.min(axis=(1, 2)), (1 / s).min(axis=1))
    out[~np.isfinite(out)] = 0
    return out


def safe_solve(J, F):
    try:
        return np.linalg.solve(J, F[..., None])[..., 0]
    except np.linalg.LinAlgError:
        out = np.full(F.shape, np.nan, complex)
        for i in range(J.shape[0]):
            try: out[i] = np.linalg.solve(J[i], F[i])
            except np.linalg.LinAlgError: pass
        return out


def sphere_sample(rng, Bn):
    u = np.clip(rng.random((Bn, M)), 1e-12, 1 - 1e-12)
    r = np.sqrt(u / (1 - u)); t = 2 * np.pi * rng.random((Bn, M))
    return r * np.exp(1j * t)


def newton_batch(vals, rng, Bn, iters=60):
    yx, yz = yvecs(vals)
    lam = sphere_sample(rng, Bn)
    ell = rng.normal(size=(Bn, NC)) + 1j * rng.normal(size=(Bn, NC))
    _, J0 = system_batch(yx, yz, lam, np.zeros((Bn, NC), complex), ell)
    _, _, vh = np.linalg.svd(J0[:, :-1, :NC])
    x = vh[:, -1, :].conj()
    den = np.einsum("bk,bk->b", ell, x); den[np.abs(den) < 1e-12] = np.nan
    z = np.concatenate([x / den[:, None], lam], axis=1)
    alive = np.all(np.isfinite(z), axis=1)
    z[~alive] = 0
    F, J = system_batch(yx, yz, z[:, NC:], z[:, :NC], ell)
    nr = np.linalg.norm(F, axis=1)
    for _ in range(iters):
        act = alive & (nr > 1e-13)
        if not act.any(): break
        ia = np.where(act)[0]
        dz = safe_solve(J[ia], -F[ia])
        ok = np.all(np.isfinite(dz), axis=1)
        dz[~ok] = 0
        alpha = np.ones(len(ia)); best = z[ia].copy(); bestn = nr[ia].copy(); moved = np.zeros(len(ia), bool)
        for _ls in range(8):
            trial = z[ia] + alpha[:, None] * dz
            Ft, _ = system_batch(yx, yz, trial[:, NC:], trial[:, :NC], ell[ia])
            nt = np.linalg.norm(Ft, axis=1)
            good = ok & ~moved & np.isfinite(nt) & (nt < nr[ia] * (1 - 1e-4 * alpha))
            best[good] = trial[good]; bestn[good] = nt[good]; moved |= good
            if moved[ok].all(): break
            alpha = np.where(moved, alpha, alpha * 0.5)
        z[ia] = best; nr[ia] = bestn
        alive[ia[~moved & (bestn > 1e-13)]] = False
        alive &= min_chord(z[:, NC:]) > KILL
        F, J = system_batch(yx, yz, z[:, NC:], z[:, :NC], ell)
        nr = np.linalg.norm(F, axis=1)
    conv = alive & (nr < 1e-10) & (min_chord(z[:, NC:]) > KEEP)
    return z[conv], ell[conv]


def random_circle(ystar, rng):
    """circle through PT[ystar], avoiding the other finite B points by >= 0.2; returns w(t) samples"""
    y0 = PT[ystar]
    others = [v for k, v in PT.items() if v is not None and k != ystar]
    for _ in range(1000):
        r = math.exp(rng.uniform(math.log(0.35), math.log(3.0)))
        phi = rng.uniform(0, 2 * math.pi)
        c = y0 + r * complex(math.cos(phi), math.sin(phi))
        if all(abs(abs(o - c) - r) > 0.2 for o in others):
            inside = sum(1 for o in others if abs(o - c) < r)
            if inside == 0: continue
            steps = max(150, int(2 * math.pi * r / 0.015))
            sgn = 1 if rng.random() < 0.5 else -1
            th0 = phi + math.pi
            ts = th0 + sgn * np.linspace(0, 2 * math.pi, steps + 1)
            w = c + r * np.exp(1j * ts)
            w[-1] = y0
            return w, inside
    raise RuntimeError("no circle")


def track(Z, ELL, vals, ystar, wpath):
    yx0, yz0 = yvecs(vals)
    mask = np.array([y == ystar for y in vals])
    z = Z.copy(); ok = np.ones(len(z), bool)
    for a, b in zip(wpath[:-1], wpath[1:]):
        yx, yz = yvecs(vals, ystar, a)
        F, J = system_batch(yx, yz, z[:, NC:], z[:, :NC], ELL)
        g = dF_dw(mask, z[:, NC:], z[:, :NC])
        dz = safe_solve(J, -g)                        # dz/dw
        z = z + dz * (b - a)
        yx, yz = yvecs(vals, ystar, b)
        for _ in range(3):
            F, J = system_batch(yx, yz, z[:, NC:], z[:, :NC], ELL)
            st = safe_solve(J, -F)
            st[~np.isfinite(st).all(axis=1)] = np.nan
            z = z + st
        bad = ~np.isfinite(z).all(axis=1)
        ok &= ~bad; z[bad] = Z[bad]
        ok &= min_chord(z[:, NC:]) > KILL
    yx, yz = yvecs(vals)
    for _ in range(4):
        F, J = system_batch(yx, yz, z[:, NC:], z[:, :NC], ELL)
        st = safe_solve(J, -F); st[~np.isfinite(st).all(axis=1)] = 0; z = z + st
    F, _ = system_batch(yx, yz, z[:, NC:], z[:, :NC], ELL)
    ok &= np.linalg.norm(F, axis=1) < 1e-10
    ok &= min_chord(z[:, NC:]) > KEEP
    return z[ok], ELL[ok]


def poly_compose(C, T):
    """coefficients (ascending) of sum_k C_k (a x + b)^k (c x + d)^(n-k), T = [[a, b], [c, d]]"""
    a, b, c, d = T[0, 0], T[0, 1], T[1, 0], T[1, 1]
    out = np.zeros(n + 1, complex)
    for k in range(n + 1):
        t = np.array([1.0 + 0j])
        for _ in range(k): t = np.convolve(t, [b, a])
        for _ in range(n - k): t = np.convolve(t, [d, c])
        out += C[k] * t
    return out


def rechart(z, ell, vals, rng):
    """move a map to the chart (0, oo, 1 = three critical points over distinct labels) with the largest
    smallest chordal distance among the critical points; returns (z, ell, vals) or None"""
    cps = [0j, None, 1 + 0j] + list(z[NC:])
    best = None
    for i0, i1, i2 in itertools.permutations(range(len(cps)), 3):
        if len({vals[i0], vals[i1], vals[i2]}) < 3: continue
        c0, c1, c2 = cps[i0], cps[i1], cps[i2]
        A = np.stack([hom(c1), hom(c0)], axis=1)
        try: co = np.linalg.solve(A, hom(c2))
        except np.linalg.LinAlgError: continue
        T = A * co[None, :]
        Ti = np.linalg.inv(T)
        rest = [i for i in range(len(cps)) if i not in (i0, i1, i2)]
        lam = []
        for i in rest:
            h = Ti @ hom(cps[i])
            lam.append(h[0] / h[1] if abs(h[1]) > 1e-13 * abs(h[0]) else 1e13)
        mc = min_chord(np.array([lam]))[0]
        if best is None or mc > best[0]: best = (mc, T, (i0, i1, i2), rest, lam)
    if best is None: return None
    mc, T, tri, rest, lam = best
    order = sorted(range(len(rest)), key=lambda j: BKEYS.index(vals[rest[j]]))
    nv = [vals[i] for i in tri] + [vals[rest[j]] for j in order]
    lam = np.array([lam[j] for j in order])
    x = np.concatenate([poly_compose(z[:n + 1], T), poly_compose(z[n + 1:NC], T)])
    e = rng.normal(size=NC) + 1j * rng.normal(size=NC)
    x = x / (e @ x)
    zz = np.concatenate([x, lam])[None, :]
    yx, yz = yvecs(nv)
    for _ in range(5):
        F, J = system_batch(yx, yz, zz[:, NC:], zz[:, :NC], e[None, :])
        st = safe_solve(J, -F)
        if not np.isfinite(st).all(): return None
        zz = zz + st
    F, _ = system_batch(yx, yz, zz[:, NC:], zz[:, :NC], e[None, :])
    if np.linalg.norm(F) > 1e-10: return None
    return zz[0], e, tuple(nv)


# ---------- float checks and the invariant K ----------
def wronskian(P, Q):
    W = np.zeros(2 * n, complex)
    for i in range(n + 1):
        for j in range(n + 1):
            if i + j >= 1: W[i + j - 1] += (i - j) * P[i] * Q[j]
    return W


def float_ok(z):
    P, Q, lam = z[:n + 1], z[n + 1:NC], z[NC:]
    fin = np.concatenate([[0, 1], lam])
    W = wronskian(P, Q); s = np.max(np.abs(W))
    if s == 0 or abs(W[2 * n - 3]) < 1e-9 * s or np.max(np.abs(W[2 * n - 2:])) > 1e-9 * s: return False
    sc = np.max(np.abs(np.concatenate([P, Q])))
    for c in fin:
        pv = np.polyval(P[::-1], c); qv = np.polyval(Q[::-1], c)
        if abs(pv) + abs(qv) < 1e-8 * sc * (1 + abs(c)) ** n: return False
        dW = np.polyval((np.arange(1, 2 * n - 2) * W[1:2 * n - 2])[::-1], c)
        dsc = np.sum(np.arange(1, 2 * n - 2) * np.abs(W[1:2 * n - 2]) * abs(c) ** np.arange(0, 2 * n - 3))
        if abs(dW) < 1e-8 * dsc: return False
    if abs(P[n]) < 1e-9 * sc and abs(Q[n]) < 1e-9 * sc: return False
    return True


def hom(c):
    return np.array([1, 0], complex) if c is None else np.array([c, 1], complex)


def frame_f(a, b, c):
    A = np.stack([hom(a), hom(b)], axis=1)
    co = np.linalg.solve(A, hom(c))
    return A * co[None, :]


def to_sph(h):
    X, Y = h
    if abs(Y) < 1e-14 * max(abs(X), 1e-300): return np.array([0.0, 0.0, 1.0])
    w = X / Y; d = 1 + abs(w) ** 2
    return np.array([2 * w.real / d, 2 * w.imag / d, (abs(w) ** 2 - 1) / d])


def kfeature(P, Q, cps, vals, ns):
    """Moebius- and within-label-invariant feature vector (sum over all normalising triples)."""
    act = [y for y, k in zip(BKEYS, ns) if k][:3]
    pools = [[i for i, v in enumerate(vals) if v == y] for y in act]
    L = {y: j for j, y in enumerate(BKEYS)}
    tot = np.zeros(KDIM)
    for tri in itertools.product(*pools):
        Fm = frame_f(*[cps[i] for i in tri])
        Fi = np.linalg.inv(Fm)
        f = np.zeros(KDIM)
        for i, (c, y) in enumerate(zip(cps, vals)):
            if i in tri: continue
            h = Fi @ hom(c)
            w = 1e14 if abs(h[1]) < 1e-14 * abs(h[0]) else h[0] / h[1]
            for j, a in enumerate(RNG_CENTERS):
                g = 1.0 / (1.0 + abs(w - a) ** 2)
                f[(L[y] * 3 + j) * 2] += g
                f[(L[y] * 3 + j) * 2 + 1] += g * g
        for j, s in enumerate(SAMPLES):
            X, Y = Fm @ np.array([s, 1])
            pv = sum(P[k] * X ** k * Y ** (n - k) for k in range(n + 1))
            qv = sum(Q[k] * X ** k * Y ** (n - k) for k in range(n + 1))
            f[36 + 3 * j:39 + 3 * j] = to_sph((pv, qv))
        tot += f + 0.37 * f * f
    return tot


# ---------- per-datum worker ----------
class Datum:
    def __init__(self, datum, target, outdir):
        self.datum, self.target = datum, target
        self.ns = [int(c) for c in datum]
        self.vals = canonical_vals(self.ns)
        self.sp = os.path.join(outdir, "state", f"{datum}.jsonl")
        self.pp = os.path.join(outdir, "state", f"{datum}.progress.json")
        self.log = open(os.path.join(outdir, "logs", f"{datum}.log"), "a", encoding="utf-8")
        self.recs, self.keys, self.Z, self.E, self.V = [], [], [], [], []
        if os.path.exists(self.sp):
            for line in open(self.sp, encoding="utf-8"):
                if not line.strip(): continue
                r = json.loads(line)
                self.recs.append(b5.parse_state_map(r)); self.keys.append(np.array(r["K"]))
                self.Z.append(np.array([complex(a, b) for a, b in r["zf"]])); self.E.append(np.array([complex(a, b) for a, b in r["ell"]]))
                self.V.append(tuple(r["critical_values"]))
        self.prog = json.load(open(self.pp)) if os.path.exists(self.pp) else {
            "batches": 0, "loops": 0, "converged": 0, "tracked_ok": 0, "float_ok": 0, "dups": 0,
            "close_pairs": 0, "rejected_mp": 0, "found_by_random": 0, "found_by_monodromy": 0, "seconds": 0.0}

    def offer(self, z, ell, source, vals):
        vals = list(vals)
        if len(self.recs) >= self.target or not float_ok(z): return False
        self.prog["float_ok"] += 1
        cps = [0j, None, 1 + 0j] + list(z[NC:])
        K = kfeature(z[:n + 1], z[n + 1:NC], cps, vals, self.ns)
        if self.keys:
            A = np.array(self.keys)
            dists = np.max(np.abs(A - K[None, :]) / (1 + np.abs(A)), axis=1)
            if dists.min() < DUP: self.prog["dups"] += 1; return False
        else:
            dists = np.zeros(0)
        try:
            zz, res = bm.mp_refine(n, vals, z, ell)
            if res > mp.mpf("1e-38") or not b5.verify_map_without_root_solve(n, zz): self.prog["rejected_mp"] += 1; return False
            okv, rv = b5.mp_critical_value_check(n, vals, zz)
            okc, rc = b5.mp_constraint_check(n, vals, zz, ell)
            if not (okv and okc): self.prog["rejected_mp"] += 1; return False
        except (ZeroDivisionError, ValueError, ArithmeticError, np.linalg.LinAlgError):
            self.prog["rejected_mp"] += 1; return False
        rec = (zz[:n + 1], zz[n + 1:NC], [mp.mpf(0), mp.inf, mp.mpf(1)] + list(zz[NC:]), vals)
        for j in np.where(dists < CLOSE)[0]:
            self.prog["close_pairs"] += 1
            if b5.equivalent_by_source_mobius(n, self.recs[j], rec) or b5.equivalent_by_source_mobius(n, rec, self.recs[j]):
                self.prog["dups"] += 1; return False
        zf = np.array([complex(t) for t in zz])
        row = b5.state_row(self.datum, self.target, rec, mp.nstr(max(res, rv, rc), 8))
        row["K"] = [float(t) for t in K]
        row["zf"] = [[t.real, t.imag] for t in zf]; row["ell"] = [[t.real, t.imag] for t in ell]
        row["source"] = source
        with open(self.sp, "a", encoding="utf-8") as f:
            f.write(json.dumps(row) + "\n"); f.flush(); os.fsync(f.fileno())
        self.recs.append(rec); self.keys.append(K); self.Z.append(zf); self.E.append(np.array(ell)); self.V.append(tuple(vals))
        self.prog["found_by_" + source] += 1
        return True

    def save(self, t0, what):
        self.prog["seconds"] += time.time() - t0
        self.prog["found"] = len(self.recs); self.prog["target"] = self.target
        tmp = self.pp + ".tmp"; json.dump(self.prog, open(tmp, "w")); os.replace(tmp, self.pp)
        self.log.write(f"{what} found {len(self.recs)}/{self.target} batches {self.prog['batches']} loops {self.prog['loops']} "
                       f"dups {self.prog['dups']} {self.prog['seconds']:.0f}s\n"); self.log.flush()

    def random_batch(self, Bn):
        t0 = time.time(); b = self.prog["batches"]
        seed = int.from_bytes(hashlib.sha256(f"routeF-maps6|{self.datum}|batch|{b}".encode()).digest()[:8], "big")
        vals = chart_vals(self.ns, random.Random(seed))
        Z, E = newton_batch(vals, np.random.default_rng(seed), Bn)
        self.prog["converged"] += len(Z)
        new = sum(self.offer(z, e, "random", vals) for z, e in zip(Z, E))
        self.prog["batches"] = b + 1
        self.save(t0, f"batch {b+1} new {new}")
        return new

    def loop(self):
        t0 = time.time(); L = self.prog["loops"]
        rng = random.Random(int.from_bytes(hashlib.sha256(f"routeF-maps6|{self.datum}|loop|{L}".encode()).digest()[:8], "big"))
        movable = [y for y, k in zip(BKEYS, self.ns) if k and y != "oo"]
        ystar = rng.choice(movable)
        w, inside = random_circle(ystar, rng)
        # in-memory re-charting of badly conditioned maps (the state file keeps the verified record)
        rr = np.random.default_rng(L)
        for i in range(len(self.Z)):
            if min_chord(self.Z[i][None, NC:])[0] < RECHART:
                r = rechart(self.Z[i], self.E[i], list(self.V[i]), rr)
                if r is not None:
                    self.Z[i], self.E[i], self.V[i] = r
                    self.prog["recharted"] = self.prog.get("recharted", 0) + 1
        groups = {}
        for i, v in enumerate(self.V): groups.setdefault(v, []).append(i)
        new = 0; Z1n = 0
        for v, idx in groups.items():
            Z1, E1 = track(np.array([self.Z[i] for i in idx]), np.array([self.E[i] for i in idx]), list(v), ystar, w)
            Z1n += len(Z1)
            new += sum(self.offer(z, e, "monodromy", v) for z, e in zip(Z1, E1))
        self.prog["tracked_ok"] += Z1n; Z1 = range(Z1n)
        self.prog["loops"] = L + 1
        self.save(t0, f"loop {L+1} y*={ystar} inside={inside} steps={len(w)-1} tracked {len(Z1)}/{len(self.Z)} new {new}")
        return new


def run_datum(args):
    datum, target, outdir, Bn, max_seconds = args
    D = Datum(datum, target, outdir)
    t0 = time.time(); stall = 0
    while len(D.recs) < target and time.time() - t0 < max_seconds:
        if not D.recs:
            D.random_batch(Bn); continue
        new = D.loop()
        stall = 0 if new else stall + 1
        if stall >= 6:
            for _ in range(4): D.random_batch(Bn)
            stall = 3
    D.log.close()
    return datum, len(D.recs), target, D.prog["batches"], D.prog["loops"], round(D.prog["seconds"], 1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("outdir"); ap.add_argument("--workers", type=int, default=11)
    ap.add_argument("--batch", type=int, default=1024); ap.add_argument("--max-seconds", type=float, default=36000)
    ap.add_argument("--only", default=""); ap.add_argument("--list", action="store_true")
    a = ap.parse_args()
    H = json.load(open(os.path.join(HERE, f"hurwitz{n}.json")))
    reps = rep_data(H)
    if a.list:
        for d, t, o in reps: print(d, t, o)
        print("reps", len(reps), "rep maps", sum(t for _, t, _ in reps), "all maps", sum(t * o for _, t, o in reps))
        return
    if a.only: reps = [r for r in reps if r[0] in set(a.only.split(","))]
    os.makedirs(os.path.join(a.outdir, "state"), exist_ok=True); os.makedirs(os.path.join(a.outdir, "logs"), exist_ok=True)
    reps.sort(key=lambda r: -r[1])
    jobs = [(d, t, a.outdir, a.batch, a.max_seconds) for d, t, _ in reps]
    from concurrent.futures import ProcessPoolExecutor, as_completed
    t0 = time.time(); done = []
    with ProcessPoolExecutor(max_workers=a.workers) as ex:
        futs = [ex.submit(run_datum, j) for j in jobs]
        for f in as_completed(futs):
            r = f.result(); done.append(r)
            print(f"[{r[0]}] {r[1]}/{r[2]} batches={r[3]} loops={r[4]} seconds={r[5]}  ({len(done)}/{len(jobs)}, {time.time()-t0:.0f}s)", flush=True)
    miss = [r for r in done if r[1] != r[2]]
    print("SUMMARY reps", len(done), "maps", sum(r[1] for r in done), "/", sum(r[2] for r in done), "incomplete", len(miss), flush=True)
    for r in miss: print("  missing", r, flush=True)


if __name__ == "__main__":
    main()
