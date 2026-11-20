"""Compiled (numba) version of speedup-20261118/mono.track: the same predictor-corrector (RK4 predictor of
du/ds = -J^-1 F_W.dW, three Newton corrections, the same acceptance test and step-size rule), run cover by cover
instead of as a numpy batch.  The batch version spends almost all its time in numpy call overhead (m = 4n-3 = 29
unknowns at n = 8) and lets the stiffest cover of a batch set the number of loop passes for all.
install():  replaces mono.track (and the names imported from it) by this version.
One difference: numpy's batched solve raises for the whole batch if one matrix is singular (all predictor
velocities set to 0); here only that cover is affected."""
import numpy as np
from numba import njit

@njit(cache=True)
def _solve(A, b):
    """complex LU with partial pivoting; returns (x, ok)"""
    m = A.shape[0]; A = A.copy(); x = b.copy()
    for k in range(m):
        p = k; amax = abs(A[k, k])
        for i in range(k + 1, m):
            if abs(A[i, k]) > amax: amax = abs(A[i, k]); p = i
        if amax == 0.0: return x, False
        if p != k:
            for j in range(m):
                t = A[k, j]; A[k, j] = A[p, j]; A[p, j] = t
            t = x[k]; x[k] = x[p]; x[p] = t
        piv = A[k, k]
        for i in range(k + 1, m):
            f = A[i, k] / piv
            if f != 0:
                for j in range(k + 1, m): A[i, j] -= f * A[k, j]
                x[i] -= f * x[k]
    for k in range(m - 1, -1, -1):
        s = x[k]
        for j in range(k + 1, m): s -= A[k, j] * x[j]
        x[k] = s / A[k, k]
    return x, True

@njit(cache=True)
def _FJ(u, W0, W1, n, ys, fixed, L, dW0, dW1, want_fd):
    K = len(ys); m = 2 * (n + 1) + K - 3
    c = np.empty(K, np.complex128); c[:3] = fixed; c[3:] = u[2 * n + 2:]
    F = np.empty(m, np.complex128); J = np.zeros((m, m), np.complex128); Fd = np.zeros(m, np.complex128)
    for k in range(K):
        y0 = W0[ys[k]]; y1 = W1[ys[k]]; ck = c[k]
        Pv = 0j; Qv = 0j; Pd = 0j; Qd = 0j; Pdd = 0j; Qdd = 0j
        pw = np.empty(n + 1, np.complex128); pw[0] = 1.0
        for j in range(1, n + 1): pw[j] = pw[j - 1] * ck
        for j in range(n + 1):
            pj = u[j]; qj = u[n + 1 + j]
            Pv += pj * pw[j]; Qv += qj * pw[j]
            J[k, j] = y1 * pw[j]; J[k, n + 1 + j] = -y0 * pw[j]
            if j >= 1:
                dj = j * pw[j - 1]
                Pd += pj * dj; Qd += qj * dj
                J[K + k, j] = y1 * dj; J[K + k, n + 1 + j] = -y0 * dj
            if j >= 2:
                ddj = j * (j - 1) * pw[j - 2]
                Pdd += pj * ddj; Qdd += qj * ddj
        F[k] = y1 * Pv - y0 * Qv; F[K + k] = y1 * Pd - y0 * Qd
        if k >= 3:
            J[k, 2 * n + 2 + k - 3] = y1 * Pd - y0 * Qd
            J[K + k, 2 * n + 2 + k - 3] = y1 * Pdd - y0 * Qdd
        if want_fd:
            d0 = dW0[ys[k]]; d1 = dW1[ys[k]]
            Fd[k] = d1 * Pv - d0 * Qv; Fd[K + k] = d1 * Pd - d0 * Qd
    s = 0j
    for j in range(2 * n + 2):
        s += u[j] * L[j]; J[2 * K, j] = L[j]
    F[2 * K] = s - 1
    return F, J, Fd

@njit(cache=True)
def _vel(uu, ss, Wa0, Wa1, Wb0, Wb1, n, ys, fixed, L):
    W0 = Wa0 + ss * (Wb0 - Wa0); W1 = Wa1 + ss * (Wb1 - Wa1)
    _, J, Fd = _FJ(uu, W0, W1, n, ys, fixed, L, Wb0 - Wa0, Wb1 - Wa1, True)
    x, ok = _solve(J, Fd)
    return -x, ok

@njit(cache=True)
def _sc(v):
    mx = 0.0
    for z in v:
        if abs(z) > mx: mx = abs(z)
    return 1 + mx

@njit(cache=True)
def track_one(u0, Wa0, Wa1, Wb0, Wb1, n, ys, fixed, L, h0, hmin, dmax, maxsteps):
    u = u0.copy(); s = 0.0; h = h0; steps = 0
    while True:
        if s >= 1 - 1e-14: return u, True, steps
        steps += 1
        if steps > maxsteps: return u, False, steps
        ha = min(h, 1 - s)
        k1, o1 = _vel(u, s, Wa0, Wa1, Wb0, Wb1, n, ys, fixed, L)
        k2, o2 = _vel(u + ha / 2 * k1, s + ha / 2, Wa0, Wa1, Wb0, Wb1, n, ys, fixed, L)
        k3, o3 = _vel(u + ha / 2 * k2, s + ha / 2, Wa0, Wa1, Wb0, Wb1, n, ys, fixed, L)
        k4, o4 = _vel(u + ha * k3, s + ha, Wa0, Wa1, Wb0, Wb1, n, ys, fixed, L)
        if not (o1 and o2 and o3 and o4):
            k1[:] = 0; k2[:] = 0; k3[:] = 0; k4[:] = 0
        up = u + ha / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        s1 = s + ha; W0 = Wa0 + s1 * (Wb0 - Wa0); W1 = Wa1 + s1 * (Wb1 - Wa1)
        good = True
        for z in up:
            if not (np.isfinite(z.real) and np.isfinite(z.imag)): good = False
        d_first = 0.0; nd = 0.0
        for it in range(3):
            F, J, _ = _FJ(up, W0, W1, n, ys, fixed, L, W0, W1, False)
            dx, ok = _solve(J, F)
            if ok:
                nrm = 0.0
                for z in dx: nrm += z.real * z.real + z.imag * z.imag
                nd = np.sqrt(nrm) / _sc(up)
            else:
                nd = np.nan
            if it == 0: d_first = nd
            if it == 2: good = good and (nd < 1e-10 + 0.1 * d_first)
            if ok: up = up - dx
            else: up = up * np.nan
        good = good and np.isfinite(nd) and (d_first < dmax)
        if good:
            u = up; s = s1; h = min(h * 1.8, 0.25)
        else:
            h *= 0.5
            if h < hmin: return u, False, steps

import os
MAXSTEPS = int(os.environ.get('TRACK_MAXSTEPS', '400'))   # per path segment; mono.track has no cap (a careful retry could spend seconds)
def track(S, u, Wa, Wb, h0=0.05, hmin=1e-7, dmax=1e-4):
    """drop-in for mono.track (same signature/return: u_end, ok mask, number of steps)"""
    u = np.asarray(u, np.complex128); N = len(u)
    Wa = np.asarray(Wa, np.complex128); Wb = np.asarray(Wb, np.complex128)
    out = u.copy(); ok = np.zeros(N, bool); st = 0
    ys = np.asarray(S.ys, np.int64); fixed = np.asarray(S.fixed, np.complex128); L = np.asarray(S.L, np.complex128)
    for i in range(N):
        wa = Wa[i] if Wa.ndim == 3 else Wa; wb = Wb[i] if Wb.ndim == 3 else Wb
        ui, oi, si = track_one(u[i], wa[:, 0].copy(), wa[:, 1].copy(), wb[:, 0].copy(), wb[:, 1].copy(), S.n, ys, fixed, L, h0, hmin, dmax, MAXSTEPS)
        out[i] = ui; ok[i] = oi; st = max(st, si)
    out[~ok] = u[~ok] if False else out[~ok]
    return out, ok, st

def install():
    import sys
    for name in ('mono', 'braid', 'mono_dir', 'mono_rep', 'hp_track', 'seed'):
        mod = sys.modules.get(name)
        if mod is not None and hasattr(mod, 'track'): mod.track = track
