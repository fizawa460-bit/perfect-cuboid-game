"""Route F, F-02: construct all slack-0 maps of degree n (n = 3 as a check, n = 4) numerically.

Slack 0 (E11 Lemma 1): 2n-2 simple critical points, all over B, every local degree 1 or 2.
For each branch datum (n_y = number of critical points over y, n_y <= floor(n/2)), unknowns are the coefficients
of p = P/Q (2n+2, normalised by a random linear functional) and the critical points beyond the first three, which
are fixed to 0, oo, 1. Equations: p(c) = y_c and p'(c) = 0, linear in (P, Q). The square system is solved by
Newton (numpy) from random starts, refined in mpmath, verified (degree, distinct simple critical points over the
prescribed values), and deduplicated up to source Moebius maps. The count per datum is compared with
the permutation count of hurwitz4.py (n = 4) or with 15 x 4 = 60 (n = 3).

usage: python -I -O build_maps.py 4 > maps4.json   (writes maps as coefficient strings with 40 digits)
"""
import itertools, json, sys, random
import numpy as np
import mpmath as mp

mp.mp.dps = 45
BKEYS = ["I", "-I", "1", "-1", "0", "oo"]
BH = {"I": (1j, 1), "-I": (-1j, 1), "1": (1, 1), "-1": (-1, 1), "0": (0, 1), "oo": (1, 0)}


def cond_rows(n, c, y, deriv_order):
    """rows (P0..Pn, Q0..Qn) for the k-th derivative (k = 0, 1) of yz*P - yx*Q at the point c (affine or 'oo')."""
    yx, yz = y
    if isinstance(c, str):                 # c = oo: use the reversed coefficients (coefficient of x^(n-k))
        v = [0] * (n + 1); v[n - deriv_order] = 1
    else:
        if deriv_order == 0: v = [c**k for k in range(n + 1)]
        else: v = [k * c**(k - 1) if k else 0 for k in range(n + 1)]
    return [yz * x for x in v] + [-yx * x for x in v]


def drow(n, c, y, deriv_order):
    """d/dc of cond_rows (c affine)"""
    yx, yz = y
    if deriv_order == 0: v = [k * c**(k - 1) if k else 0 for k in range(n + 1)]
    else: v = [k * (k - 1) * c**(k - 2) if k > 1 else 0 for k in range(n + 1)]
    return [yz * x for x in v] + [-yx * x for x in v]


def system(n, vals, lam, x, ell):
    cps = [0.0, "oo", 1.0] + list(lam)
    F = []; J = np.zeros((4 * n - 3, 2 * n + 2 + len(lam)), dtype=complex); r = 0
    for i, (c, y) in enumerate(zip(cps, vals)):
        for d in (0, 1):
            row = np.array(cond_rows(n, c, BH[y], d), dtype=complex)
            F.append(row @ x); J[r, :2 * n + 2] = row
            if i >= 3: J[r, 2 * n + 2 + i - 3] = np.array(drow(n, c, BH[y], d), dtype=complex) @ x
            r += 1
    F.append(ell @ x - 1); J[r, :2 * n + 2] = ell
    return np.array(F), J


def newton(n, vals, lam, x, ell, it=60):
    z = np.concatenate([x, lam])
    for _ in range(it):
        F, J = system(n, vals, z[2 * n + 2:], z[:2 * n + 2], ell)
        if not np.all(np.isfinite(F)): return None
        try: dz = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError: return None
        z = z + dz
        if np.linalg.norm(dz) < 1e-13 * (1 + np.linalg.norm(z)): break
    F, _ = system(n, vals, z[2 * n + 2:], z[:2 * n + 2], ell)
    if np.linalg.norm(F) > 1e-9: return None
    return z


def mp_refine(n, vals, z, ell):
    """Newton in mpmath on the same system"""
    m = len(z); zz = [mp.mpc(complex(t)) for t in z]
    L = [mp.mpc(complex(t)) for t in ell]
    def FJ(zz):
        lam = zz[2 * n + 2:]; x = zz[:2 * n + 2]
        cps = [mp.mpf(0), "oo", mp.mpf(1)] + list(lam)
        F = []; J = mp.matrix(m, m); r = 0
        for i, (c, y) in enumerate(zip(cps, vals)):
            yv = (mp.mpc(BH[y][0]), mp.mpc(BH[y][1]))
            for d in (0, 1):
                row = cond_rows(n, c, yv, d)
                F.append(mp.fsum(a * b for a, b in zip(row, x)))
                for k in range(2 * n + 2): J[r, k] = row[k]
                if i >= 3: J[r, 2 * n + 2 + i - 3] = mp.fsum(a * b for a, b in zip(drow(n, c, yv, d), x))
                r += 1
        F.append(mp.fsum(a * b for a, b in zip(L, x)) - 1)
        for k in range(2 * n + 2): J[r, k] = L[k]
        return F, J
    for _ in range(12):
        F, J = FJ(zz)
        dz = mp.lu_solve(J, mp.matrix([-f for f in F]))
        zz = [a + dz[k] for k, a in enumerate(zz)]
        if mp.norm(dz) < mp.mpf(10) ** -38: break
    F, _ = FJ(zz)
    return zz, mp.norm(mp.matrix(F))


def peval_mp(P, Q, t):
    return mp.polyval(list(reversed(P)), t), mp.polyval(list(reversed(Q)), t)


def verify(n, vals, zz):
    """genuine degree n, the 2n-2 critical points distinct and simple, values as prescribed"""
    x = zz[:2 * n + 2]; P, Q = x[:n + 1], x[n + 1:]
    lam = zz[2 * n + 2:]
    cps = [mp.mpf(0), mp.inf, mp.mpf(1)] + list(lam)
    # distinct critical points (on the sphere)
    fin = [c for c in cps if c != mp.inf]
    for a, b in itertools.combinations(fin, 2):
        if abs(a - b) < mp.mpf(10) ** -10: return False
    if any(abs(c) > mp.mpf(10) ** 10 for c in lam): return False
    # resultant of P, Q nonzero (genuine degree n, no common root) via Sylvester matrix
    N = 2 * n; S = mp.matrix(N, N)
    for i in range(n):
        for k in range(n + 1): S[i, i + k] = P[n - k]; S[n + i, i + k] = Q[n - k]
    nrm = max(abs(t) for t in x)
    if abs(mp.det(S)) < mp.mpf(10) ** -25 * nrm ** N: return False
    if abs(P[n]) < mp.mpf(10) ** -25 * nrm and abs(Q[n]) < mp.mpf(10) ** -25 * nrm: return False
    # Wronskian P'Q - PQ' has degree <= 2n-2 with roots exactly the finite critical points (oo is critical)
    dP = [k * P[k] for k in range(1, n + 1)]; dQ = [k * Q[k] for k in range(1, n + 1)]
    W = [mp.mpc(0)] * (2 * n)
    for i, a in enumerate(dP):
        for k, b in enumerate(Q): W[i + k] += a * b
    for i, a in enumerate(P):
        for k, b in enumerate(dQ): W[i + k] -= a * b
    deg = max(k for k in range(2 * n) if abs(W[k]) > mp.mpf(10) ** -30 * nrm**2)
    if deg != 2 * n - 3: return False                     # exactly one critical point at oo, simple
    rts = mp.polyroots(list(reversed(W[:deg + 1])), maxsteps=400, extraprec=400)
    for c in fin:
        if min(abs(c - r) for r in rts) > mp.mpf(10) ** -15: return False
    return True


def key_maps_equal(n, A, B):
    """p_B = p_A o M for some Moebius M?  A, B = (P, Q, cps, vals); try M sending 3 critical points of B to
    critical points of A with equal values, then compare at random points."""
    PA, QA, cA, vA = A; PB, QB, cB, vB = B
    if sorted(vA) != sorted(vB): return False
    def hom(c): return (mp.mpc(1), mp.mpc(0)) if c == mp.inf else (c, mp.mpc(1))
    src = [hom(c) for c in cB[:3]]
    tests = [mp.mpc(0.31, 0.77), mp.mpc(-1.13, 0.29), mp.mpc(0.6, -1.4)]
    for tri in itertools.permutations(range(len(cA)), 3):
        if any(vA[t] != vB[s] for t, s in zip(tri, range(3))): continue
        dst = [hom(cA[t]) for t in tri]
        def frame(p):
            M = mp.matrix([[p[0][0], p[1][0]], [p[0][1], p[1][1]]])
            co = mp.lu_solve(M, mp.matrix([p[2][0], p[2][1]]))
            return mp.matrix([[p[0][0] * co[0], p[1][0] * co[1]], [p[0][1] * co[0], p[1][1] * co[1]]])
        M = frame(dst) * mp.inverse(frame(src))
        ok = True
        for t in tests:
            u = M * mp.matrix([t, 1])
            a1, a2 = peval_mp(PA, QA, u[0] / u[1]) if abs(u[1]) > mp.mpf(10) ** -20 else (PA[n], QA[n])
            b1, b2 = peval_mp(PB, QB, t)
            if abs(a1 * b2 - a2 * b1) > mp.mpf(10) ** -20 * (abs(a1) + abs(a2)) * (abs(b1) + abs(b2)): ok = False; break
        if ok: return True
    return False


def num_key(n, P, Q, cps):
    """numeric invariant of p mod source Moebius: min over ordered triples of critical points (sent to 0, 1, oo)
    of (positions of the other critical points, value of p at the normalised point 2), as a complex vector."""
    def hom(c): return np.array([1, 0], dtype=complex) if c is None else np.array([c, 1], dtype=complex)
    pts = [hom(c) for c in cps]
    best = None
    for i, j, k in itertools.permutations(range(len(pts)), 3):
        M = np.stack([pts[i], pts[k]], axis=-1)            # 0 -> pts[i], oo -> pts[k]
        co = np.linalg.solve(M, pts[j]); M = M * co[None, :]  # 1 -> pts[j]
        Mi = np.linalg.inv(M)
        rest = []
        for m in range(len(pts)):
            if m in (i, j, k): continue
            v = Mi @ pts[m]; rest.append(v[0] / v[1] if abs(v[1]) > 1e-12 * abs(v[0]) else 1e12)
        v = M @ np.array([2, 1], dtype=complex)
        px = sum(P[e] * v[0]**e * v[1]**(n - e) for e in range(n + 1)); qx = sum(Q[e] * v[0]**e * v[1]**(n - e) for e in range(n + 1))
        val = px / qx if abs(qx) > 1e-12 * abs(px) else 1e12
        vec = np.array(sorted(rest, key=lambda z: (round(z.real, 7), round(z.imag, 7))) + [val])
        cand = tuple(np.round(np.concatenate([vec.real, vec.imag]), 7))
        if best is None or cand < best: best = cand
    return np.array(best)


def build(n, ns, target, rng, max_starts=60000):
    vals = []
    for y, k in zip(BKEYS, ns): vals += [y] * k
    found = []; keys = []; starts = 0
    nlam = 2 * n - 5
    while len(found) < target and starts < max_starts:
        starts += 1
        sc = rng.choice((0.5, 1.5, 4.0)); lam = np.array([complex(rng.gauss(0, sc), rng.gauss(0, sc)) for _ in range(nlam)])
        ell = np.array([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2 * n + 2)])
        F, J = system(n, vals, lam, np.zeros(2 * n + 2, dtype=complex), ell)
        A = J[:-1, :2 * n + 2]
        x = np.linalg.svd(A)[2][-1].conj(); x = x / (ell @ x)
        z = newton(n, vals, lam, x, ell)
        if z is None: continue
        lamz = z[2 * n + 2:]
        if np.any(np.abs(lamz) > 1e8): continue
        cps_d = [0.0, None, 1.0] + list(lamz)
        fin = [c for c in cps_d if c is not None]
        if min(abs(p - q) for p, q in itertools.combinations(fin, 2)) < 1e-7: continue
        try:
            k = num_key(n, z[:n + 1], z[n + 1:2 * n + 2], cps_d)
        except np.linalg.LinAlgError:
            continue
        if any(np.max(np.abs(k - kk)) < 1e-5 for kk in keys): continue
        try:
            zz, res = mp_refine(n, vals, z, ell)
            if res > mp.mpf(10) ** -30 or not verify(n, vals, zz): continue
        except (ZeroDivisionError, ValueError):
            continue
        x = zz[:2 * n + 2]
        rec = (x[:n + 1], x[n + 1:], [mp.mpf(0), mp.inf, mp.mpf(1)] + list(zz[2 * n + 2:]), vals)
        if any(key_maps_equal(n, f, rec) for f in found): keys.append(k); continue
        found.append(rec); keys.append(k)
    return found, starts


def work(args):
    n, ns_s, target = args
    import zlib
    rng = random.Random(zlib.crc32(f"20261112b-{n}-{ns_s}".encode()))
    found, starts = build(n, [int(ch) for ch in ns_s], target, rng)
    return ns_s, target, starts, [{"datum": ns_s, "P": [mp.nstr(c, 40) for c in P], "Q": [mp.nstr(c, 40) for c in Q]}
                                  for P, Q, cps, vals in found]


if __name__ == "__main__":
    import multiprocessing as mpc, os
    n = int(sys.argv[1]); outp = f"maps{n}.jsonl"
    if n == 4:
        H = json.loads(open("hurwitz4.json").read())
        data = {k: v[0] for k, v in H.items()}
    elif n == 3:
        data = {"".join(map(str, ns)): 4 for ns in itertools.product(range(2), repeat=6) if sum(ns) == 4}
    done = {}
    if os.path.exists(outp):
        for line in open(outp):
            r = json.loads(line); done[r["datum"]] = r
    todo = [(n, k, v) for k, v in sorted(data.items()) if k not in done or len(done[k]["maps"]) != v]
    print(f"{len(data)} data, {len(todo)} to do", file=sys.stderr, flush=True)
    with mpc.Pool(int(sys.argv[2]) if len(sys.argv) > 2 else 6) as pool:
        for ns_s, target, starts, maps in pool.imap_unordered(work, todo):
            print(f"datum {ns_s}: target {target}, found {len(maps)}, starts {starts}", file=sys.stderr, flush=True)
            done[ns_s] = {"datum": ns_s, "target": target, "starts": starts, "maps": maps}
            with open(outp, "w") as f:
                for k in sorted(done): f.write(json.dumps(done[k]) + chr(10))
    bad = [k for k, v in data.items() if len(done[k]["maps"]) != v]
    flat = [m for k in sorted(done) for m in done[k]["maps"]]
    json.dump(flat, open(f"maps{n}.json", "w"))
    print(f"total maps {len(flat)}, data short of target: {bad}", file=sys.stderr)
    if bad: raise SystemExit(1)


def parse_c(s):
    """parse mp.nstr output of a complex number, e.g. '(-0.12 + 3.4e-5j)' or '0.5' or '2.0j', at full precision"""
    import re
    s = s.strip().strip("()").replace(" ", "")
    if not s.endswith("j"): return mp.mpc(mp.mpf(s))
    m = re.match(r"^([+-]?[0-9.]+(?:e[+-]?[0-9]+)?)([+-][0-9.]+(?:e[+-]?[0-9]+)?)j$", s)
    if m: return mp.mpc(mp.mpf(m.group(1)), mp.mpf(m.group(2)))
    return mp.mpc(0, mp.mpf(s[:-1]))
