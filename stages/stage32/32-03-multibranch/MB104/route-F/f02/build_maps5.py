#!/usr/bin/env python3
"""Restartable, high-precision slack-0 map builder for degrees 3, 4, 5.

Requires the existing build_maps.py in this directory and numpy + mpmath.
The random starts use a spherical (Cauchy) distribution for the five free
critical points.  The first three marked critical points are chosen over
three distinct branch values to avoid the poor chart used by build_maps.py.

Files (degree n):
  mapsn.state.jsonl  one durable line per accepted map, including critical data
  mapsn.jsonl        one grouped line per branch datum: datum,target,maps[P,Q]
  mapsn.json         flat map list in the maps4.json shape
  mapsn.progress.json restart counters

This is a numerical search, not a proof of completeness.  The Hurwitz target
counts and the independent critical-point/value checks are recorded per type.
"""
import argparse
import hashlib
import itertools
import json
import math
import os
import random
import sys
import time
from collections import defaultdict
from concurrent.futures import ProcessPoolExecutor

HERE = os.path.dirname(os.path.abspath(__file__))
# Prevent BLAS oversubscription when several independent starts run in parallel.
for _k in ("OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "MKL_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_k] = "1"
if HERE not in sys.path:
    sys.path.insert(0, HERE)
import numpy as np
import mpmath as mp
import build_maps as bm

mp.mp.dps = 60
BKEYS = list(bm.BKEYS)
BH = bm.BH


def n3_data():
    return {"".join(map(str, ns)): 4
            for ns in itertools.product(range(2), repeat=6) if sum(ns) == 4}


def load_targets(n):
    if n == 3:
        d = n3_data()
    else:
        name = f"hurwitz{n}.json"
        with open(os.path.join(HERE, name), encoding="utf-8") as f:
            H = json.load(f)
        d = {k: int(v[0]) for k, v in H.items()}
        if n == 5:
            assert len(d) == 90 and sum(d.values()) == 6090
            assert all(v[2] == {"1": v[0]} for v in H.values()), "nontrivial automorphism count detected"
    return dict(sorted(d.items()))


def chord(a, b):
    if a is None: return 1.0 / math.sqrt(1.0 + abs(b) ** 2)
    if b is None: return 1.0 / math.sqrt(1.0 + abs(a) ** 2)
    return abs(a - b) / math.sqrt((1.0 + abs(a) ** 2) * (1.0 + abs(b) ** 2))


def uniform_sphere_point(rng):
    u = min(1.0 - 1e-12, max(1e-12, rng.random()))
    r = math.sqrt(u / (1.0 - u))
    return r * complex(math.cos(2 * math.pi * rng.random()), math.sin(2 * math.pi * rng.random()))


def critical_value_order(ns, rng):
    active = [y for y, k in zip(BKEYS, ns) if k]
    first = rng.sample(active, 3)  # three distinct target values at 0, infinity, 1
    rest = []
    for y, k in zip(BKEYS, ns):
        rest.extend([y] * (k - (1 if y in first else 0)))
    rng.shuffle(rest)
    return first + rest


def sample_lambdas(rng, count, max_abs=1e3):
    out = []
    fixed = [0j, 1 + 0j, None]
    for _ in range(500):
        if len(out) == count:
            return np.asarray(out, dtype=complex)
        z = uniform_sphere_point(rng)
        if abs(z) > max_abs:
            continue
        if any(chord(z, q) < 0.025 for q in fixed):
            continue
        if any(chord(z, q) < 0.025 for q in out):
            continue
        out.append(z)
    raise RuntimeError("could not sample a separated critical-point configuration")


def damped_newton(n, vals, lam, x, ell, max_iter=80):
    z = np.concatenate([x, lam])
    for _ in range(max_iter):
        F, J = bm.system(n, vals, z[2*n+2:], z[:2*n+2], ell)
        if not np.all(np.isfinite(F)) or not np.all(np.isfinite(J)):
            return None
        norm0 = float(np.linalg.norm(F))
        if norm0 < 2e-12:
            return z
        try:
            dz = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            return None
        if not np.all(np.isfinite(dz)):
            return None
        accepted = False
        alpha = 1.0
        for _ls in range(14):
            zn = z + alpha * dz
            Fn, _ = bm.system(n, vals, zn[2*n+2:], zn[:2*n+2], ell)
            nn = float(np.linalg.norm(Fn)) if np.all(np.isfinite(Fn)) else float("inf")
            if nn < norm0 * (1.0 - 1e-4 * alpha) or nn < 2e-12:
                z = zn
                accepted = True
                break
            alpha *= 0.5
        if not accepted:
            # A damped least-squares step is a fallback for badly conditioned charts.
            try:
                dz, *_ = np.linalg.lstsq(J, -F, rcond=1e-12)
            except np.linalg.LinAlgError:
                return None
            alpha = 0.125
            for _ls in range(12):
                zn = z + alpha * dz
                Fn, _ = bm.system(n, vals, zn[2*n+2:], zn[:2*n+2], ell)
                nn = float(np.linalg.norm(Fn)) if np.all(np.isfinite(Fn)) else float("inf")
                if nn < norm0:
                    z = zn
                    accepted = True
                    break
                alpha *= 0.5
        if not accepted:
            return None
    F, _ = bm.system(n, vals, z[2*n+2:], z[:2*n+2], ell)
    return z if np.linalg.norm(F) < 1e-9 else None


def verify_map_without_root_solve(n, zz):
    """Verify degree, coprimality, and the complete simple critical divisor.

    For degree n, the homogeneous Wronskian has degree 2n-2.  In this chart
    one simple critical point is at infinity, so its affine degree is 2n-3.
    The seven (or, generally, 2n-3) finite marked points are checked as simple
    roots directly.  This avoids an expensive and ill-conditioned polyroots call.
    """
    x = zz[:2*n+2]
    P, Q = x[:n+1], x[n+1:]
    lam = zz[2*n+2:]
    cps = [mp.mpf(0), mp.inf, mp.mpf(1)] + list(lam)
    fin = [c for c in cps if c != mp.inf]
    if len(cps) != 2*n-2 or len(fin) != 2*n-3:
        return False
    for a, b in itertools.combinations(fin, 2):
        if abs(a-b) < mp.mpf("1e-10"): return False
    if any(abs(c) > mp.mpf("1e10") for c in lam): return False
    nrm = max(abs(t) for t in x)
    if nrm == 0: return False
    N = 2*n
    S = mp.matrix(N, N)
    for i in range(n):
        for k in range(n+1):
            S[i, i+k] = P[n-k]
            S[n+i, i+k] = Q[n-k]
    if abs(mp.det(S)) < mp.mpf("1e-25") * nrm**N: return False
    if abs(P[n]) < mp.mpf("1e-25")*nrm and abs(Q[n]) < mp.mpf("1e-25")*nrm: return False
    dP = [k*P[k] for k in range(1,n+1)]
    dQ = [k*Q[k] for k in range(1,n+1)]
    W = [mp.mpc(0)] * (2*n)
    for i,a in enumerate(dP):
        for k,b in enumerate(Q): W[i+k] += a*b
    for i,a in enumerate(P):
        for k,b in enumerate(dQ): W[i+k] -= a*b
    cutoff = mp.mpf("1e-30") * nrm**2
    nz = [k for k,v in enumerate(W) if abs(v) > cutoff]
    if not nz or max(nz) != 2*n-3: return False
    deg = 2*n-3
    dW = [k*W[k] for k in range(1,deg+1)]
    for c in fin:
        val = mp.polyval(list(reversed(W[:deg+1])), c)
        scale = max(mp.mpf("1e-100"), mp.fsum(abs(W[k])*abs(c)**k for k in range(deg+1)))
        if abs(val)/scale > mp.mpf("1e-30"): return False
        der = mp.polyval(list(reversed(dW)), c) if dW else mp.mpc(0)
        dscale = max(mp.mpf("1e-100"), mp.fsum(k*abs(W[k])*abs(c)**(k-1) for k in range(1,deg+1)))
        if abs(der)/dscale < mp.mpf("1e-25"): return False
    return True


def mp_critical_value_check(n, vals, zz, tol=mp.mpf("1e-30")):
    x = zz[:2*n+2]
    P, Q = x[:n+1], x[n+1:]
    cps = [mp.mpf(0), "oo", mp.mpf(1)] + list(zz[2*n+2:])
    worst = mp.mpf(0)
    for c, y in zip(cps, vals):
        yx, yz = BH[y]
        if c == "oo":
            pv, qv = P[n], Q[n]
        else:
            pv = mp.polyval(list(reversed(P)), c)
            qv = mp.polyval(list(reversed(Q)), c)
        den = abs(pv) + abs(qv)
        if den == 0:
            return False, mp.inf
        err = abs(yz * pv - yx * qv) / den
        worst = max(worst, err)
    return worst < tol, worst


def mp_constraint_check(n, vals, zz, ell, tol=mp.mpf("1e-30")):
    x = zz[:2*n+2]
    cps = [mp.mpf(0), "oo", mp.mpf(1)] + list(zz[2*n+2:])
    worst = mp.mpf(0)
    for c, y in zip(cps, vals):
        for d in (0, 1):
            row = bm.cond_rows(n, c, BH[y], d)
            terms = [mp.mpc(a) * b for a, b in zip(row, x)]
            den = max([mp.mpf(1)] + [abs(a) for a in terms])
            worst = max(worst, abs(mp.fsum(terms)) / den)
    norm = abs(mp.fsum(mp.mpc(a) * b for a, b in zip(ell, x)) - 1)
    worst = max(worst, norm)
    return worst < tol, worst


def mp_hom(c):
    return (mp.mpc(1), mp.mpc(0)) if c == mp.inf else (mp.mpc(c), mp.mpc(1))


def frame(points):
    p0, p1, p2 = [mp.matrix(mp_hom(c)) for c in points]
    C = mp.matrix([[p0[0], p1[0]], [p0[1], p1[1]]])
    coeff = mp.lu_solve(C, p2)
    return mp.matrix([[p0[0]*coeff[0], p1[0]*coeff[1]],
                      [p0[1]*coeff[0], p1[1]*coeff[1]]])


def poly_mul(a, b):
    out = [mp.mpc(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): out[i+j] += x*y
    return out


def poly_pow_linear(a, b, k):
    return [mp.binomial(k, j) * a**j * b**(k-j) for j in range(k+1)]


def compose_homogeneous(P, M, n):
    a, b, c, d = M[0,0], M[0,1], M[1,0], M[1,1]
    out = [mp.mpc(0)] * (n+1)
    for k in range(n+1):
        t = poly_mul(poly_pow_linear(a, b, k), poly_pow_linear(c, d, n-k))
        for j, v in enumerate(t): out[j] += P[k] * v
    return out


def projective_sphere_coords(X, Y):
    if abs(Y) < mp.mpf("1e-35") * max(abs(X), mp.mpf("1e-100")):
        return (mp.mpf(0), mp.mpf(0), mp.mpf(1))
    w = X / Y
    den = 1 + abs(w)**2
    return (2*mp.re(w)/den, 2*mp.im(w)/den, (abs(w)**2-1)/den)


def eval_binary(F, X, Y, n):
    return mp.fsum(F[k] * X**k * Y**(n-k) for k in range(n+1))


def signature_set(n, rec, ns):
    """High-precision source-Möbius invariant used only as a duplicate prefilter.

    A close signature never discards a map: it triggers the coefficient identity
    test in equivalent_by_source_mobius.  Thus the signature cannot create a
    false duplicate (trap C).
    """
    P, Q, cps, vals = rec
    labels = [y for y, k in zip(BKEYS, ns) if k][:3]
    pools = [[i for i, v in enumerate(vals) if v == y] for y in labels]
    sigs = []
    canonical = [mp.mpf(0), mp.inf, mp.mpf(1)]
    samples = [mp.mpc(2), mp.mpc("0.2", "1.1"), mp.mpc("-0.7", "0.3")]
    for chosen in itertools.product(*pools):
        if len(set(chosen)) != 3: continue
        M = frame(canonical) * mp.inverse(frame([cps[i] for i in chosen]))
        Minv = mp.inverse(M)
        keep = set(chosen)
        coords = {y: [] for y in BKEYS}
        for i, (c, y) in enumerate(zip(cps, vals)):
            if i in keep: continue
            h = M * mp.matrix(mp_hom(c))
            coords[y].append(projective_sphere_coords(h[0], h[1]))
        key = []
        for y in BKEYS:
            # PATCH (Claude, 2026-11-15): sort by rounded coordinates; raw mp sort broke on symmetric
            # maps (exact x-ties perturbed at 1e-100 flip the order), so equivalent maps got different keys.
            for xyz in sorted(coords[y], key=lambda t: tuple(round(float(v), 7) for v in t)): key.extend(xyz)
        for w in samples:
            h = Minv * mp.matrix([w, 1])
            pv = eval_binary(P, h[0], h[1], n)
            qv = eval_binary(Q, h[0], h[1], n)
            key.extend(projective_sphere_coords(pv, qv))
        sigs.append(tuple(key))
    return sigs


def signatures_close(A, B, tol=mp.mpf("1e-18")):
    return len(A) == len(B) and all(abs(x-y) < tol for x, y in zip(A, B))


def equivalent_by_source_mobius(n, A, B):
    """Exact-coefficient test after the unique Möbius map on an ordered critical triple."""
    PA, QA, cA, vA = A
    PB, QB, cB, vB = B
    if len(cA) != len(cB) or len(vA) != len(vB): return False
    idx = [[i for i, v in enumerate(vA) if v == vB[j]] for j in range(3)]
    if any(not t for t in idx): return False
    # The first three marked points in each chart lie over three distinct B-values.
    for ia, ib, ic in itertools.product(*idx):
        if len({ia, ib, ic}) != 3: continue
        M = frame([cA[ia], cA[ib], cA[ic]]) * mp.inverse(frame(cB[:3]))
        # Normalise map coefficients to make the residual scale-independent.
        sa = max(max(abs(t) for t in PA), max(abs(t) for t in QA))
        sb = max(max(abs(t) for t in PB), max(abs(t) for t in QB))
        pA = [t/sa for t in PA]; qA = [t/sa for t in QA]
        pB = [t/sb for t in PB]; qB = [t/sb for t in QB]
        pAm = compose_homogeneous(pA, M, n)
        qAm = compose_homogeneous(qA, M, n)
        left = poly_mul(pAm, qB)
        right = poly_mul(qAm, pB)
        scale = max([mp.mpf("1e-100")] + [abs(t) for t in left + right])
        err = max(abs(left[k] - right[k]) for k in range(len(left))) / scale
        if err < mp.mpf("1e-32"):
            return True
    return False


def trial(n, datum, attempt):
    seed_bytes = hashlib.sha256(f"routeF-F02-v2|{n}|{datum}|{attempt}".encode()).digest()
    rng = random.Random(int.from_bytes(seed_bytes[:8], "big"))
    ns = [int(c) for c in datum]
    vals = critical_value_order(ns, rng)
    lam = sample_lambdas(rng, 2*n-5)
    ell = np.asarray([complex(rng.gauss(0, 1), rng.gauss(0, 1)) for _ in range(2*n+2)], dtype=complex)
    rows = []
    for c, y in zip([0.0, "oo", 1.0] + list(lam), vals):
        for d in (0, 1): rows.append(bm.cond_rows(n, c, BH[y], d))
    A = np.asarray(rows, dtype=complex)
    try:
        _, _, vh = np.linalg.svd(A, full_matrices=False)
        x = vh[-1].conj()
        den = ell @ x
        if abs(den) < 1e-10: return None
        x = x / den
    except np.linalg.LinAlgError:
        return None
    z = damped_newton(n, vals, lam, x, ell)
    if z is None: return None
    if np.any(np.abs(z[2*n+2:]) > 1e7): return None
    try:
        zz, residual = bm.mp_refine(n, vals, z, ell)
        if residual > mp.mpf("1e-38"): return None
        if not verify_map_without_root_solve(n, zz): return None
        okv, rv = mp_critical_value_check(n, vals, zz)
        okc, rc = mp_constraint_check(n, vals, zz, ell)
        if not (okv and okc): return None
    except (ZeroDivisionError, ValueError, ArithmeticError, np.linalg.LinAlgError):
        return None
    P, Q = zz[:n+1], zz[n+1:2*n+2]
    cps = [mp.mpf(0), mp.inf, mp.mpf(1)] + list(zz[2*n+2:])
    return (P, Q, cps, vals), max(residual, rv, rc)


def trial_worker(args):
    """Top-level picklable wrapper for Windows spawn multiprocessing."""
    return trial(*args)


def cstr(z):
    if z == mp.inf: return "oo"
    return mp.nstr(z, 45)


def parse_state_map(r):
    P = [bm.parse_c(x) for x in r["P"]]
    Q = [bm.parse_c(x) for x in r["Q"]]
    cps = [mp.mpf(0) if x == "0" else (mp.inf if x == "oo" else (mp.mpf(1) if x == "1" else bm.parse_c(x)))
           for x in r["critical_points"]]
    return P, Q, cps, r["critical_values"]


def read_state(path):
    found = defaultdict(list)
    if not os.path.exists(path): return found
    with open(path, encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            r = json.loads(line)
            found[r["datum"]].append(parse_state_map(r))
    return found


def write_state_map(path, datum, target, rec, residual):
    with open(path, "a", encoding="utf-8") as f:
        f.write(json.dumps(state_row(datum, target, rec, mp.nstr(residual, 8)), ensure_ascii=False) + "\n")
        f.flush(); os.fsync(f.fileno())


def atomic_jsonl(path, rows):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + "\n")
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def state_row(datum, target, rec, residual="recovered"):
    P, Q, cps, vals = rec
    return {
        "datum": datum, "target": target,
        "P": [mp.nstr(c, 60) for c in P], "Q": [mp.nstr(c, 60) for c in Q],
        "critical_points": [cstr(c) for c in cps], "critical_values": list(vals),
        "max_verified_residual": str(residual)
    }


def rewrite_state_file(path, targets, found):
    rows = []
    for datum in sorted(found):
        if datum not in targets: continue
        for rec in found[datum]: rows.append(state_row(datum, targets[datum], rec))
    atomic_jsonl(path, rows)


def export_outputs(n, targets, found, outdir):
    rows, flat = [], []
    for datum, target in targets.items():
        maps = []
        for P, Q, cps, vals in found.get(datum, []):
            pp = [mp.nstr(c, 40) for c in P]
            qq = [mp.nstr(c, 40) for c in Q]
            maps.append({"P": pp, "Q": qq})
            flat.append({"datum": datum, "P": pp, "Q": qq})
        rows.append({"datum": datum, "target": target, "maps": maps})
    atomic_jsonl(os.path.join(outdir, f"maps{n}.jsonl"), rows)
    tmp = os.path.join(outdir, f"maps{n}.json.tmp")
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(flat, f, ensure_ascii=False, separators=(",", ":"))
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, os.path.join(outdir, f"maps{n}.json"))
    return len(flat)


def load_progress(path):
    if not os.path.exists(path): return {}
    with open(path, encoding="utf-8") as f: return json.load(f)


def save_progress(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.flush(); os.fsync(f.fileno())
    os.replace(tmp, path)


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("n", type=int, choices=(3, 4, 5))
    ap.add_argument("--only", default="", help="comma-separated branch data, e.g. 002222,011222,111122")
    ap.add_argument("--max-starts", type=int, default=60000, help="additional starts per datum in this invocation")
    ap.add_argument("--progress-every", type=int, default=100, help="batch/checkpoint size")
    ap.add_argument("--workers", type=int, default=min(6, os.cpu_count() or 1),
                    help="parallel independent Newton starts (default: up to 6)")
    ap.add_argument("--outdir", default=HERE)
    args = ap.parse_args()
    n = args.n
    targets = load_targets(n)
    if args.only:
        wanted = set(x.strip() for x in args.only.split(",") if x.strip())
        unknown = wanted - set(targets)
        if unknown: ap.error("unknown datum(s): " + ",".join(sorted(unknown)))
        targets = {k: v for k, v in targets.items() if k in wanted}
    outdir = os.path.abspath(args.outdir)
    os.makedirs(outdir, exist_ok=True)
    state_path = os.path.join(outdir, f"maps{n}.state.jsonl")
    progress_path = os.path.join(outdir, f"maps{n}.progress.json")
    found = read_state(state_path)
    # Remove duplicate records left by a crash between the map append and the progress checkpoint.
    sig_cache = defaultdict(list)
    state_deduplicated = False
    for d, recs in list(found.items()):
        ns = [int(c) for c in d]
        clean, clean_sigs = [], []
        for rec in recs:
            sig = signature_set(n, rec, ns)
            duplicate = False
            for old, oldsig in zip(clean, clean_sigs):
                if any(signatures_close(a, b) for a in sig for b in oldsig):
                    if equivalent_by_source_mobius(n, old, rec):
                        duplicate = True
                        state_deduplicated = True
                        break
            if not duplicate:
                clean.append(rec); clean_sigs.append(sig)
        found[d] = clean
        sig_cache[d] = clean_sigs
    if os.path.exists(state_path) and state_deduplicated:
        rewrite_state_file(state_path, load_targets(n), found)
    progress = load_progress(progress_path)
    progress.setdefault("attempts", {})
    progress.setdefault("started_at", time.strftime("%Y-%m-%dT%H:%M:%S"))
    progress["n"] = n
    progress["target_total"] = sum(targets.values())
    progress["datum_count"] = len(targets)
    start_all = time.time()
    full_targets = load_targets(n)
    export_outputs(n, full_targets, found, outdir)
    if args.workers < 1:
        ap.error("--workers must be >= 1")
    if args.progress_every < 1:
        ap.error("--progress-every must be >= 1")
    if args.max_starts < 0:
        ap.error("--max-starts must be >= 0")
    executor = ProcessPoolExecutor(max_workers=args.workers) if args.workers > 1 else None
    try:
        for datum, target in targets.items():
            if len(found.get(datum, [])) >= target:
                continue
            already = len(found.get(datum, []))
            attempt0 = int(progress["attempts"].get(datum, 0))
            progress["attempts"].setdefault(datum, attempt0)
            t0 = time.time(); successes = 0; completed = 0
            print(f"[{datum}] {already}/{target} maps; attempt={attempt0}; workers={args.workers}", flush=True)
            while completed < args.max_starts and len(found[datum]) < target:
                batch = min(args.progress_every, args.max_starts - completed)
                jobs = [(n, datum, attempt0 + completed + j) for j in range(batch)]
                results = executor.map(trial_worker, jobs) if executor else map(trial_worker, jobs)
                # Consume the complete batch so every dispatched deterministic start is checkpointed.
                for j, result in enumerate(results):
                    attempt = attempt0 + completed + j
                    if result is None or len(found[datum]) >= target:
                        continue
                    rec, residual = result
                    sig = signature_set(n, rec, [int(c) for c in datum])
                    duplicate = False
                    for old, oldsig in zip(found[datum], sig_cache[datum]):
                        if any(signatures_close(a, b) for a in sig for b in oldsig):
                            if equivalent_by_source_mobius(n, old, rec):
                                duplicate = True
                                break
                    if not duplicate:
                        write_state_map(state_path, datum, target, rec, residual)
                        found[datum].append(rec)
                        sig_cache[datum].append(sig)
                        successes += 1
                        total = sum(len(v) for v in found.values())
                        print(f"  accepted {len(found[datum])}/{target}; total={total}; start={attempt+1}; residual<={mp.nstr(residual,4)}", flush=True)
                        save_progress(progress_path, progress)
                completed += batch
                progress["attempts"][datum] = attempt0 + completed
                save_progress(progress_path, progress)
                export_outputs(n, full_targets, found, outdir)
                elapsed = time.time() - t0
                print(f"  progress {completed}/{args.max_starts}; found={len(found[datum])}/{target}; rate={successes/max(elapsed,1e-9):.4g} maps/s; {elapsed:.1f}s", flush=True)
            export_outputs(n, full_targets, found, outdir)
            print(f"[{datum}] end: {len(found[datum])}/{target}; added={successes}; starts={progress['attempts'][datum]}; seconds={time.time()-t0:.1f}", flush=True)
    finally:
        if executor:
            executor.shutdown(wait=True, cancel_futures=False)
    total = sum(len(found.get(k, [])) for k in targets)
    missing = {k: (v, len(found.get(k, []))) for k, v in targets.items()
               if len(found.get(k, [])) != v}
    export_outputs(n, full_targets, found, outdir)
    progress["last_run_seconds"] = round(time.time() - start_all, 2)
    progress["found_total"] = total
    progress["missing"] = missing
    save_progress(progress_path, progress)
    print(f"SUMMARY degree={n}: {total}/{sum(targets.values())} maps in selected scope; incomplete types={len(missing)}; seconds={time.time()-start_all:.1f}", flush=True)
    if missing:
        for k, (want, got) in missing.items(): print(f"  {k}: target={want}, found={got}", flush=True)
        raise SystemExit(1)


if __name__ == "__main__":
    main()
