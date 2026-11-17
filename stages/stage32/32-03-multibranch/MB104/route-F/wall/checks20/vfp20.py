#!/usr/bin/env python3
"""checks20 / vfp20.py -- GPU version of checks18/vfp18.py (F_p count of the Belyi maps pbar of V-symmetric slack-0 maps).

Same normal form and the same exact check as vfp18.py:
    c x A1^2 B1^4 - A2^2 B2^4 = c (x - 1) A3^2 B3^4   over F_p,  (a_k, b_k) = (deg A_k, deg B_k),  A_k, B_k monic.
Every dessin whose class is fixed by Frobenius gives exactly one solution, so #solutions = N_p and
#{V-symmetric maps with moduli field in Q(i)} <= N_p for p = 1 mod 4, p > n (ANSWER-18, sections 2.4 and 3).

GPU sieve (exact, no false negatives):  for each (c, A1 B1, A2 B2) with R(1) = 0, where R = c x S1 - S2, form
q = R / (c (x - 1)) (monic, degree n - 1) and test that q is the square of a monic polynomial (top half of the
coefficients determines the root, the bottom half must match).  Survivors go to the exact sympy check of vfp18.py
(shape A^2 B^4 of all three fibres, coprimality, simple points at 0, 1, oo).
Usage: python -I vfp20.py p a1,b1 a2,b2 a3,b3        (largest a + b last; results appended to vfp20.jsonl)
"""
import os, sys, json, time, itertools
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))

KERNEL = r'''
extern "C" __global__ void sieve(const short* S1, const short* S2, const int* order2, const int* start2, const int* len2,
                                 const int* v1, int k1_0, int nk1, int c, int p, int n, const int* inv,
                                 int* out, unsigned long long* nout, int cap)
{
    // one block row per k1 (blockIdx.y), threads stride over the k2 bucket with S2(1) = c * S1(1)
    int k1 = k1_0 + blockIdx.y;
    if (blockIdx.y >= nk1) return;
    int t = (int)(((long long)c * v1[k1]) % p);
    int st = start2[t], ln = len2[t];
    const short* s1 = S1 + (long long)k1 * n;          // n coefficients, low to high, degree n - 1, monic
    int ic = inv[c], inv2 = inv[2];
    int m = (n - 1) / 2;
    for (int idx = blockIdx.x * blockDim.x + threadIdx.x; idx < ln; idx += gridDim.x * blockDim.x) {
        int k2 = order2[st + idx];
        const short* s2 = S2 + (long long)k2 * n;
        int R[16], q[16], h[16];
        // R = c x S1 - S2 (degree n), coefficients 0..n
        R[0] = (p - s2[0]) % p;
        for (int k = 1; k < n; k++) R[k] = (c * s1[k - 1] - s2[k] + p * 2) % p;
        R[n] = (c * s1[n - 1]) % p;
        // q = R / (x - 1): q[n-1] = R[n], q[k-1] = R[k] + q[k]
        q[n - 1] = R[n];
        for (int k = n - 1; k >= 1; k--) q[k - 1] = (R[k] + q[k]) % p;
        // (remainder R[0] + q[0] == 0 holds by the bucket choice)
        for (int k = 0; k < n; k++) q[k] = (q[k] * ic) % p;   // monic, degree n - 1 = 2m
        // square root: h monic degree m, h[m] = 1
        h[m] = 1;
        for (int k = 1; k <= m; k++) {
            int s = q[2 * m - k];
            for (int i = 1; i < k; i++) s -= h[m - i] * h[m - k + i];
            s %= p; if (s < 0) s += p;
            h[m - k] = (s * inv2) % p;
        }
        bool ok = true;
        for (int k = m + 1; k <= 2 * m && ok; k++) {
            int s = 0;
            for (int i = k - m; i <= m; i++) s += h[m - i] * h[m - k + i];
            if ((s % p) != q[2 * m - k]) ok = false;
        }
        if (ok) {
            unsigned long long w = atomicAdd(nout, 1ULL);
            if (w < (unsigned long long)cap) { out[3 * w] = c; out[3 * w + 1] = k1; out[3 * w + 2] = k2; }
        }
    }
}
'''


def monic_all(d, p):
    """all monic polynomials of degree d, coefficients low to high, shape (p^d, d+1); row index = base-p digits of
    (coefficient of x^(d-1), ..., coefficient of x^0) as in itertools.product order of vfp18.monic_polys"""
    N = p ** d
    out = np.zeros((N, d + 1), dtype=np.int64)
    out[:, d] = 1
    idx = np.arange(N, dtype=np.int64)
    for j in range(d):                       # digit j (most significant first) is the coefficient of x^(d-1-j)
        out[:, d - 1 - j] = (idx // p ** (d - 1 - j)) % p
    return out


def conv(X, Y, p):
    """batched polynomial product, low to high: X (N, dx+1), Y (M, dy+1) -> (N*M, dx+dy+1), row = i*M + j"""
    N, dx1 = X.shape; M, dy1 = Y.shape
    Z = np.zeros((N, M, dx1 + dy1 - 1), dtype=np.int64)
    for a in range(dx1):
        Z[:, :, a:a + dy1] += X[:, a, None, None] * Y[None, :, :]
    return (Z % p).reshape(N * M, dx1 + dy1 - 1)


def square(X, p):
    """row-wise square of a batch of polynomials (low to high)"""
    N, d1 = X.shape
    Z = np.zeros((N, 2 * d1 - 1), dtype=np.int64)
    for a in range(d1):
        Z[:, a:a + d1] += X[:, a, None] * X
    return Z % p


def fibre(a, b, p):
    A = monic_all(a, p); B = monic_all(b, p)
    A2 = square(A, p); B2 = square(B, p); B4 = square(B2, p)
    S = conv(A2, B4, p)                      # row = iA * p^b + iB, matching vfp18's list L
    return A, B, S.astype(np.int16)


def main():
    import cupy as cp
    from sympy import Poly, symbols, GF
    X = symbols("x")
    p = int(sys.argv[1]); pp = [tuple(map(int, s.split(","))) for s in sys.argv[2:5]]
    n = 1 + sum(a + b for a, b in pp)
    assert p % 4 == 1 and p > n and n <= 15 and n % 2 == 1
    (a1, b1), (a2, b2), (a3, b3) = pp
    for (a, b) in pp: assert 1 + 2 * a + 4 * b == n, pp
    t0 = time.time()
    A1, B1, S1 = fibre(a1, b1, p); A2, B2, S2 = fibre(a2, b2, p)
    nB1, nB2 = len(B1), len(B2)
    v1 = (S1.astype(np.int64).sum(axis=1) % p).astype(np.int32)       # S1(1)
    v2 = (S2.astype(np.int64).sum(axis=1) % p).astype(np.int32)
    order2 = np.argsort(v2, kind="stable").astype(np.int32)
    cnt = np.bincount(v2, minlength=p).astype(np.int32)
    start2 = np.concatenate([[0], np.cumsum(cnt)[:-1]]).astype(np.int32)
    inv = np.array([0] + [pow(x, p - 2, p) for x in range(1, p)], dtype=np.int32)
    kern = cp.RawKernel(KERNEL, "sieve")
    dS1 = cp.asarray(S1.ravel()); dS2 = cp.asarray(S2.ravel())
    dord = cp.asarray(order2); dst = cp.asarray(start2); dln = cp.asarray(cnt); dv1 = cp.asarray(v1); dinv = cp.asarray(inv)
    cap = 4_000_000
    dout = cp.zeros(3 * cap, dtype=cp.int32); dn = cp.zeros(1, dtype=cp.uint64)
    L1 = len(S1); CH = 4096
    maxlen = int(cnt.max())
    gx = max(1, min(64, (maxlen + 255) // 256))
    for c in range(1, p):
        for k0 in range(0, L1, CH):
            nk = min(CH, L1 - k0)
            kern((gx, nk), (256,), (dS1, dS2, dord, dst, dln, dv1, np.int32(k0), np.int32(nk), np.int32(c), np.int32(p),
                                    np.int32(n), dinv, dout, dn, np.int32(cap)))
    cp.cuda.Stream.null.synchronize()
    nsurv = int(dn[0]); assert nsurv <= cap, nsurv
    surv = cp.asnumpy(dout[:3 * nsurv]).reshape(-1, 3)
    t1 = time.time()

    def shape_ok(f, a, b):
        da = db = 0
        for g, e in f.factor_list()[1]:
            if e == 2: da += g.degree()
            elif e == 4: db += g.degree()
            else: return False
        return da == a and db == b

    dom = GF(p)
    def P(coeffs_low): return Poly([int(x) for x in coeffs_low[::-1]], X, domain=dom)
    count = 0; sols = []
    for c, k1, k2 in surv:
        c = int(c); k1 = int(k1); k2 = int(k2)
        PA1 = P(A1[k1 // nB1]); PB1 = P(B1[k1 % nB1]); PA2 = P(A2[k2 // nB2]); PB2 = P(B2[k2 % nB2])
        N0 = Poly([1, 0], X, domain=dom) * PA1 ** 2 * PB1 ** 4; D = PA2 ** 2 * PB2 ** 4
        if not (shape_ok(PA1 ** 2 * PB1 ** 4, a1, b1) and shape_ok(D, a2, b2)): continue
        if PA1.eval(0) == 0 or PB1.eval(0) == 0: continue
        if N0.gcd(D).degree() > 0: continue
        R = c * N0 - D
        q, r = divmod(R, Poly([c, -c], X, domain=dom))
        if not r.is_zero or q.degree() != n - 1: continue
        if not shape_ok(q, a3, b3): continue
        if q.eval(1) == 0: continue
        count += 1
        sols.append([c, [int(x) for x in A1[k1 // nB1]], [int(x) for x in B1[k1 % nB1]],
                     [int(x) for x in A2[k2 // nB2]], [int(x) for x in B2[k2 % nB2]]])
    rec = {"n": n, "p": p, "passport": pp, "survivors_of_sieve": nsurv, "N_p": count,
           "gpu_seconds": round(t1 - t0, 1), "seconds": round(time.time() - t0, 1), "solutions": sols}
    print(json.dumps({k: v for k, v in rec.items() if k != "solutions"}), flush=True)
    with open(os.path.join(HERE, "vfp20.jsonl"), "a") as f: f.write(json.dumps(rec) + "\n")


if __name__ == "__main__":
    main()
