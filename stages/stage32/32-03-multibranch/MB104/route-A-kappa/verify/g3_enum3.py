#!/usr/bin/env python3
"""Enumeration of short vectors in W via fpylll-LLL transform + custom FP.
Run with the venv python (has fpylll + numpy).
Usage: venv/bin/python g3_enum3.py B8 6
Saves g3_enum_{tag}_{bound}.json (K-coords, exact -v^2 in [1,bound]) and
g3_red_{tag}.json (the reducing transform U and reduced Gram, for reuse).
"""
import json
import math
import sys
import time

import numpy as np
from fpylll import IntegerMatrix, GSO, LLL

sys.setrecursionlimit(100000)


def reduce_form(Q):
    """LLL-reduce the positive-definite integer form Q (numpy int64).
    Returns (U, Gred): U unimodular int64, Gred = U^T Q U exact (object array)."""
    n = Q.shape[0]
    L0 = np.linalg.cholesky(Q.astype(float))
    s = 30
    A0 = np.round(L0 * (2.0 ** s)).astype(np.int64)
    A = IntegerMatrix.from_matrix(A0.tolist())
    U = IntegerMatrix.identity(n)
    M = GSO.Mat(A, U=U)
    M.update_gso()
    red = LLL.Reduction(M)
    red()
    Ared = np.array([[int(A[i, j]) for j in range(n)] for i in range(n)], dtype=np.int64)
    Um = np.array([[int(U[i, j]) for j in range(n)] for i in range(n)], dtype=np.int64)
    assert np.array_equal(Um @ A0, Ared), "U tracking convention mismatch"
    assert round(abs(float(np.linalg.det(Um.astype(float))))) == 1
    Utrue = Um
    Qo = Q.astype(object)
    Uo = Utrue.astype(object)
    Gred = Uo @ Qo @ Uo.T
    return Utrue, Gred


def fp_enumerate(Gred, bound_float):
    """All z in Z^n with z^T Gred z <= bound_float (Gred exact int object array).
    Float Cholesky FP; caller exact-filters. Returns (list of tuples, node count)."""
    n = Gred.shape[0]
    Gf = np.array([[float(v) for v in row] for row in Gred.tolist()], dtype=float)
    L = np.linalg.cholesky(Gf)
    S = [[float(L[j, i]) for j in range(n)] for i in range(n)]  # S[i][j], upper: Q=|Sz|^2, S[i][j]=L[j][i]
    # Actually numpy cholesky: Gf = L @ L.T, Q(z) = |L^T z|^2, (L^T)[i][j] = L[j][i].
    results = []
    z = [0] * n
    partial = [0.0] * n
    nodes = [0]

    def rec(i, rem):
        nodes[0] += 1
        if i < 0:
            results.append(tuple(z))
            return
        sii = S[i][i]
        ci = partial[i]
        r = math.sqrt(rem) if rem > 0 else 0.0
        lo = math.ceil((-r - ci) / sii - 1e-9)
        hi = math.floor((r - ci) / sii + 1e-9)
        Si = S[i]
        for zi in range(lo, hi + 1):
            z[i] = zi
            if zi != 0:
                for j in range(i):
                    partial[j] += S[j][i] * zi
            rec(i - 1, rem - (sii * zi + ci) ** 2)
            if zi != 0:
                for j in range(i):
                    partial[j] -= S[j][i] * zi
        z[i] = 0

    rec(n - 1, bound_float)
    return results, nodes[0]


def main():
    tag = sys.argv[1]
    bound = int(sys.argv[2])
    d = json.load(open(f"/home/hatch/workspace/kappa-trace/g3_data_{tag}.json"))
    Q = np.array([[int(v) for v in row] for row in d["Qpos"]], dtype=np.int64)
    n = Q.shape[0]
    t0 = time.time()
    try:
        red = json.load(open(f"/home/hatch/workspace/kappa-trace/g3_red_{tag}.json"))
        U = np.array(red["U"], dtype=np.int64)
        Qo = Q.astype(object)
        Gred = U.astype(object) @ Qo @ U.astype(object).T
        print(f"{tag}: loaded saved reduction", flush=True)
    except FileNotFoundError:
        U, Gred = reduce_form(Q)
        with open(f"/home/hatch/workspace/kappa-trace/g3_red_{tag}.json", "w") as f:
            json.dump({"U": [[int(v) for v in row] for row in U.tolist()]}, f)
        print(f"{tag}: LLL done in {time.time()-t0:.1f}s", flush=True)
    # GSO profile of reduced form (float)
    Gf = np.array([[float(v) for v in row] for row in Gred.tolist()])
    Lc = np.linalg.cholesky(Gf)
    diag = [float(Lc[i, i]) ** 2 for i in range(n)]
    print(f"{tag}: reduced GSO diag B_i: min={min(diag):.3f} max={max(diag):.3f} "
          f"first5={[round(x,2) for x in diag[:5]]} last5={[round(x,2) for x in diag[-5:]]}", flush=True)
    t1 = time.time()
    red_vecs, nodes = fp_enumerate(Gred, bound + 0.5)
    print(f"{tag}: FP nodes={nodes} returned={len(red_vecs)} in {time.time()-t1:.1f}s", flush=True)
    Qo = Q.astype(object)
    Uo = U.astype(object)
    out = []
    for yr in red_vecs:
        y = np.array(yr, dtype=object)
        z = Uo.T @ y
        n2 = int(z @ Qo @ z)
        if 1 <= n2 <= bound:
            out.append([int(v) for v in z])
    print(f"{tag}: exact -v^2 in [1,{bound}]: {len(out)}", flush=True)
    with open(f"/home/hatch/workspace/kappa-trace/g3_enum_{tag}_{bound}.json", "w") as f:
        json.dump(out, f)


if __name__ == "__main__":
    main()
