"""Exact-label Moebius alignment test (numba): is there a Moebius map mu with mu(X) = Y as labelled point sets?
Used by build5.py to confirm numerically every symmetry image that the monodromy rules name (no merge rests on the
rules alone)."""
import numpy as np
from numba import njit

@njit(cache=True)
def _frame(a0, a1, b0, b1, c0, c1):
    det = a0 * b1 - b0 * a1
    l0 = (b1 * c0 - b0 * c1) / det; l1 = (-a1 * c0 + a0 * c1) / det
    return a0 * l0, b0 * l1, a1 * l0, b1 * l1

@njit(cache=True)
def align(X0, X1, LX, Y0, Y1, LY, anchors, tol):
    """X, Y: unit homogeneous points (K,), labels LX, LY.  anchors: 3 indices of X.  Tries every label-consistent
    assignment of the anchors to distinct Y points; returns the largest matching distance of the best assignment
    (every X point to its nearest same-label Y point, which must be one-to-one), or 1.0 if none fits."""
    K = len(X0); best = 1.0
    i0, i1, i2 = anchors[0], anchors[1], anchors[2]
    a00, a01, a10, a11 = _frame(X0[i0], X1[i0], X0[i1], X1[i1], X0[i2], X1[i2])
    det = a00 * a11 - a01 * a10
    if abs(det) == 0: return 1.0
    v00 = a11 / det; v01 = -a01 / det; v10 = -a10 / det; v11 = a00 / det
    used = np.zeros(K, np.bool_)
    for j0 in range(K):
        if LY[j0] != LX[i0]: continue
        for j1 in range(K):
            if j1 == j0 or LY[j1] != LX[i1]: continue
            for j2 in range(K):
                if j2 == j0 or j2 == j1 or LY[j2] != LX[i2]: continue
                b00, b01, b10, b11 = _frame(Y0[j0], Y1[j0], Y0[j1], Y1[j1], Y0[j2], Y1[j2])
                M00 = b00 * v00 + b01 * v10; M01 = b00 * v01 + b01 * v11
                M10 = b10 * v00 + b11 * v10; M11 = b10 * v01 + b11 * v11
                worst = 0.0; ok = True
                for k in range(K): used[k] = False
                for i in range(K):
                    u0 = M00 * X0[i] + M01 * X1[i]; u1 = M10 * X0[i] + M11 * X1[i]
                    nu = np.sqrt(abs(u0) ** 2 + abs(u1) ** 2)
                    if nu == 0: ok = False; break
                    dmin = 2.0; kmin = -1
                    for k in range(K):
                        if LY[k] != LX[i]: continue
                        d = abs(u0 * Y1[k] - u1 * Y0[k]) / nu
                        if d < dmin: dmin = d; kmin = k
                    if dmin > tol or used[kmin]: ok = False; break
                    used[kmin] = True
                    if dmin > worst: worst = dmin
                if ok and worst < best: best = worst
    return best
