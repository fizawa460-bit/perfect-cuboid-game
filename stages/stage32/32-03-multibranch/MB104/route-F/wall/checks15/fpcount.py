#!/usr/bin/env python3
"""checks15 / fpcount.py -- upper bound for the number of slack-0 maps with field of moduli in Q(i), by counting over F_p.

Idea (P2 of ANSWER-14, CHECK-15 sec. 6):
  p = 1 mod 4, p > n, so i in F_p and the six points of B stay distinct mod p, and p does not divide n!.
  Tame specialisation: reduction mod a prime P of Q(i) above p is a bijection between the degree-n covers of P^1 over
  Qbar and over Fpbar with branch points in B and the same ramification data.  [cited, not re-proved here]
  A class with field of moduli in Q(i) is fixed by Frob_P, so
      #{classes over Q(i)}  <=  N_p := #{Frob_P-fixed classes over Fpbar}.
  Over a finite field the field of moduli is a field of definition, and the mass formula sum 1/|Aut(twist)(F_p)| = 1 gives
      #{rational functions f in F_p(x) of the datum}  =  |PGL_2(F_p)| * N_p .
  So N_p = count / (p (p^2 - 1)); integrality of N_p is a built-in check.

Counting: f = c * P0 / Q0, with P0 = A0^2 L0 (fibre over 0) and Q0 = Aoo^2 Loo (fibre over oo) as normalised binary forms
(A squarefree of degree n_y, L squarefree of degree n - 2 n_y, gcd(A, L) = 1), c in F_p^*.  For y in {i, -i, 1, -1} the
binary form c P0 - y Q0 must have exactly n_y double roots and no root of multiplicity >= 3 (counted on P^1, root at oo
included); P0, Q0 coprime.  Total ramification is then 2n - 2, so there is nothing else to check.
The datum is first rotated (octahedral rotations are defined over Z[i, 1/2]) so that n_0 + n_oo is largest.
GPU kernel (cupy RawKernel), exact integer arithmetic mod p.

Usage: python -I fpcount.py n p [datum ...]   (no datum: all representative data of hurwitz{n})
Output: one JSON line per datum to stdout and appended to fpcount.jsonl (resumable: done (n, p, datum) are skipped).
"""
import os, sys, json, itertools, time
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
F02 = os.path.normpath(os.path.join(HERE, "..", "..", "f02"))
BKEYS = ["I", "-I", "1", "-1", "0", "oo"]

KERNEL = r'''
#define MAXD 9
__device__ __forceinline__ int trim(const int *a, int d){ while (d >= 0 && a[d] == 0) d--; return d; }
__device__ int pgcd(int *a, int da, int *b, int db, const int *inv, int p){
  /* gcd of a, b (in place); returns degree of result (left in a), -1 if both zero */
  da = trim(a, da); db = trim(b, db);
  while (db >= 0){
    int il = inv[b[db]];
    while (da >= db){
      int q = (a[da] * il) % p, s = da - db;
      for (int k = 0; k <= db; k++){ a[k + s] = (a[k + s] - q * b[k]) % p; if (a[k + s] < 0) a[k + s] += p; }
      da = trim(a, da - 1);
    }
    for (int k = 0; k < MAXD; k++){ int t = a[k]; a[k] = b[k]; b[k] = t; }
    int t = da; da = db; db = t;
  }
  return da;
}
__device__ bool fibre_ok(const int *F, int n, int want, const int *inv, int p){
  int f[MAXD], g[MAXD], h[MAXD], hh[MAXD];
  for (int k = 0; k < MAXD; k++){ f[k] = (k <= n) ? F[k] : 0; g[k] = 0; h[k] = 0; hh[k] = 0; }
  int df = trim(f, n);
  if (df < 0) return false;
  int einf = n - df;
  if (einf > 2) return false;
  for (int k = 1; k <= df; k++) g[k - 1] = (k * f[k]) % p;
  for (int k = 0; k < MAXD; k++) h[k] = f[k];
  int dg = pgcd(h, df, g, df - 1, inv, p);           /* h = gcd(f, f') */
  if (dg < 0) return false;
  int dbl = dg + (einf == 2 ? 1 : 0);
  if (dbl != want) return false;
  if (dg >= 1){
    for (int k = 0; k < MAXD; k++){ hh[k] = 0; }
    for (int k = 1; k <= dg; k++) hh[k - 1] = (k * h[k]) % p;
    int d2 = pgcd(h, dg, hh, dg - 1, inv, p);         /* gcd(h, h') must be constant: no triple roots */
    if (d2 != 0) return false;
  }
  return true;
}
extern "C" __global__ void count(const int *P, const int *Q, long long nP, long long nQ, int n, int p,
                                 const int *inv, const int *yv, const int *want, unsigned long long *out){
  long long total = nP * nQ * (long long)(p - 1);
  unsigned long long local = 0;
  for (long long t = blockDim.x * (long long)blockIdx.x + threadIdx.x; t < total; t += (long long)blockDim.x * gridDim.x){
    long long c = t % (p - 1) + 1, r = t / (p - 1);
    long long iq = r % nQ, ip = r / nQ;
    const int *P0 = P + ip * (n + 1), *Q0 = Q + iq * (n + 1);
    if (P0[n] == 0 && Q0[n] == 0) continue;
    int a[MAXD], b[MAXD];
    for (int k = 0; k < MAXD; k++){ a[k] = (k <= n) ? P0[k] : 0; b[k] = (k <= n) ? Q0[k] : 0; }
    if (pgcd(a, n, b, n, inv, p) != 0) continue;
    bool ok = true;
    int F[MAXD];
    for (int j = 0; j < 4 && ok; j++){
      int y = yv[j];
      for (int k = 0; k <= n; k++){ int v = ((int)c * P0[k] - y * Q0[k]) % p; F[k] = v < 0 ? v + p : v; }
      ok = fibre_ok(F, n, want[j], inv, p);
    }
    if (ok) local++;
  }
  atomicAdd(out, local);
}
'''


def sqrt_m1(p):
    for x in range(2, p):
        if x * x % p == p - 1: return x
    raise ValueError(p)


def trim(a):
    a = list(a)
    while a and a[-1] == 0: a.pop()
    return a


def pmod_poly(a, b, p):
    a = trim(a); b = trim(b); il = pow(b[-1], p - 2, p)
    while len(a) >= len(b):
        q = a[-1] * il % p; s = len(a) - len(b)
        for k, x in enumerate(b): a[k + s] = (a[k + s] - q * x) % p
        a = trim(a)
    return a


def pgcd(a, b, p):
    a, b = trim(a), trim(b)
    while b: a, b = b, pmod_poly(a, b, p)
    return a


def deriv(a, p): return trim([(k * a[k]) % p for k in range(1, len(a))])


def mul(a, b, p):
    r = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b): r[i + j] = (r[i + j] + x * y) % p
    return r


def forms(m, p):
    """normalised binary forms of degree m (coefficient lists of length m+1; last nonzero coefficient = 1), squarefree on P^1"""
    out = []
    for top in (m, m - 1):                       # exact degree m, or degree m-1 (one simple root at oo)
        if top < 0: continue
        for low in itertools.product(range(p), repeat=top):
            t = list(low) + [1]
            if len(t) > 2 and len(pgcd(t, deriv(t, p), p)) > 1: continue
            out.append(t + [0] * (m + 1 - len(t)))
    return out


def fibre_polys(n, ny, p):
    """normalised forms A^2 L of degree n, A squarefree deg ny, L squarefree deg n-2ny, coprime on P^1"""
    As, Ls = forms(ny, p), forms(n - 2 * ny, p)
    res = []
    for A in As:
        for L in Ls:
            if A[-1] == 0 and L[-1] == 0: continue            # both vanish at oo
            if len(pgcd(A, L, p)) > 1: continue
            P = mul(mul(A, A, p), L, p)
            res.append(P[:n + 1] + [0] * (n + 1 - len(P)))
    return res


def rotations():
    """the 24 rotations of B as permutations of BKEYS (exact, over Q(i))"""
    import cmath
    pts = {"I": 1j, "-I": -1j, "1": 1, "-1": -1, "0": 0, "oo": None}
    def ap(g, z):
        a, b, c, d = g
        if z is None: return None if abs(c) < 1e-12 else a / c
        den = c * z + d
        return None if abs(den) < 1e-12 else (a * z + b) / den
    def key(z):
        for k, v in pts.items():
            if (z is None and v is None) or (z is not None and v is not None and abs(z - v) < 1e-9): return k
        return None
    gens = [(1j, 0, 0, 1), (1, 1, -1, 1)]
    seen = {tuple(BKEYS)}; frontier = [tuple(BKEYS)]
    perms = [list(range(6))]
    gperm = []
    for g in gens:
        gperm.append([BKEYS.index(key(ap(g, pts[k]))) for k in BKEYS])
    group = {tuple(range(6))}; todo = [tuple(range(6))]
    while todo:
        s = todo.pop()
        for g in gperm:
            t = tuple(g[s[i]] for i in range(6))
            if t not in group: group.add(t); todo.append(t)
    assert len(group) == 24, len(group)
    return [list(s) for s in group]


def best_rotation(datum):
    ns = [int(c) for c in datum]; best = None
    for s in rotations():
        r = [0] * 6
        for i in range(6): r[s[i]] = ns[i]
        key = (r[4] + r[5], min(r[4], r[5]))
        if best is None or key > best[0]: best = (key, r)
    return best[1]


def run(n, p, datum, cp, kern):
    ns = best_rotation(datum)
    i = sqrt_m1(p)
    yv = [i, p - i, 1, p - 1]
    want = ns[:4]
    t0 = time.time()
    P = np.array(fibre_polys(n, ns[4], p), dtype=np.int32)
    Q = np.array(fibre_polys(n, ns[5], p), dtype=np.int32)
    inv = np.array([0] + [pow(x, p - 2, p) for x in range(1, p)], dtype=np.int32)
    out = cp.zeros(1, dtype=cp.uint64)
    kern((2048,), (256,), (cp.asarray(P), cp.asarray(Q), np.int64(len(P)), np.int64(len(Q)), np.int32(n), np.int32(p),
                           cp.asarray(inv), cp.asarray(np.array(yv, dtype=np.int32)), cp.asarray(np.array(want, dtype=np.int32)), out))
    cp.cuda.Stream.null.synchronize()
    cnt = int(out[0]); G = p * (p * p - 1)
    return {"n": n, "p": p, "datum": datum, "rotated": "".join(map(str, ns)), "nP": len(P), "nQ": len(Q),
            "count": cnt, "N_p": cnt / G, "integral": cnt % G == 0, "seconds": round(time.time() - t0, 1)}


def main():
    import cupy as cp
    n, p = int(sys.argv[1]), int(sys.argv[2])
    assert p % 4 == 1 and p > n
    data = sys.argv[3:]
    if not data:
        sys.path.insert(0, F02)
        H = json.load(open(os.path.join(F02, f"hurwitz{n}.json" if n != 6 else "hurwitz6.json")))
        seen, data = set(), []
        for d in sorted(k for k in H if not k.startswith("_")):
            r = "".join(map(str, best_rotation(d)))
            if r in seen: continue
            seen.add(r); data.append(d)
    outf = os.path.join(HERE, "fpcount.jsonl")
    done = set()
    if os.path.exists(outf):
        for l in open(outf):
            if l.strip():
                r = json.loads(l); done.add((r["n"], r["p"], r["rotated"]))
    kern = cp.RawKernel(KERNEL, "count")
    for d in data:
        rot = "".join(map(str, best_rotation(d)))
        if (n, p, rot) in done: continue
        r = run(n, p, d, cp, kern)
        print(json.dumps(r), flush=True)
        with open(outf, "a") as f: f.write(json.dumps(r) + "\n")
        done.add((n, p, rot))


if __name__ == "__main__":
    main()
