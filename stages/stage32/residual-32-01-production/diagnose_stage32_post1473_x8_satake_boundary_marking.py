#!/usr/bin/env python3
"""Exact lightweight checker for the Stage32 X(8) Satake-boundary marking.

No floating point arithmetic and no external packages are used.
Gaussian integers are pairs (real, imag), and every expression below is
linear in one free theta variable t.
"""

I = (0, 1)
ONE = (1, 0)
ZERO = (0, 0)


def gadd(x, y):
    return (x[0] + y[0], x[1] + y[1])


def gneg(x):
    return (-x[0], -x[1])


def gmul(x, y):
    return (x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0])


def padd(x, y):
    return (gadd(x[0], y[0]), gadd(x[1], y[1]))


def pneg(x):
    return (gneg(x[0]), gneg(x[1]))


def pscale_g(a, x):
    return (gmul(a, x[0]), gmul(a, x[1]))


def pzero(x):
    return x == (ZERO, ZERO)


def const(a):
    return (a, ZERO)


T = (ZERO, ONE)


def coords(Az, Bz, Aw, Bw):
    def mul(x, y):
        c0 = gmul(x[0], y[0])
        c1 = gadd(gmul(x[0], y[1]), gmul(x[1], y[0]))
        assert gmul(x[1], y[1]) == ZERO
        return (c0, c1)

    W1 = padd(mul(Bz, Aw), mul(Az, Bw))
    W2 = pscale_g(I, padd(mul(Bz, Aw), pneg(mul(Az, Bw))))
    W3 = padd(mul(Az, Aw), pneg(mul(Bz, Bw)))
    C = padd(mul(Az, Aw), mul(Bz, Bw))
    return W1, W2, W3, C


def matching_signs(block, factor, branch):
    # Generic free coordinate is t on the unfixed X(8) factor.
    if factor == "z":
        Aw, Bw = const(ONE), T
        if block == "Z1":
            Az, Bz = const(ONE), const((branch, 0))
        elif block == "Z2":
            Az, Bz = const(ONE), const((0, branch))
        else:
            # Z3=theta10(z)theta10(w); theta10(z)=0 means Az=0 or Bz=0.
            Az, Bz = (const(ONE), const(ZERO)) if branch == 1 else (const(ZERO), const(ONE))
    else:
        Az, Bz = const(ONE), T
        if block == "Z1":
            Aw, Bw = const(ONE), const((branch, 0))
        elif block == "Z2":
            Aw, Bw = const(ONE), const((0, branch))
        else:
            Aw, Bw = (const(ONE), const(ZERO)) if branch == 1 else (const(ZERO), const(ONE))

    W1, W2, W3, C = coords(Az, Bz, Aw, Bw)
    ans = []
    for e1 in (1, -1):
        for e2 in (1, -1):
            if block == "Z1":
                q1 = padd(pscale_g(I, W2), pscale_g((e1, 0), W3))
                q2 = padd(W1, pscale_g((e2, 0), C))
            elif block == "Z2":
                q1 = padd(pscale_g(I, W3), pscale_g((e1, 0), W1))
                q2 = padd(W2, pscale_g((e2, 0), C))
            else:
                q1 = padd(pscale_g(I, W1), pscale_g((e1, 0), W2))
                q2 = padd(W3, pscale_g((e2, 0), C))
            if pzero(q1) and pzero(q2):
                ans.append((e1, e2))
    assert len(ans) == 1
    return ans[0]


def main():
    for block in ("Z1", "Z2", "Z3"):
        z = {matching_signs(block, "z", s) for s in (1, -1)}
        w = {matching_signs(block, "w", s) for s in (1, -1)}
        assert z == {(1, -1), (-1, 1)}, (block, z)
        assert w == {(1, 1), (-1, -1)}, (block, w)

    # Magma sequence constructors iterate the first range innermost.
    per_block = [(1, 1), (-1, 1), (1, -1), (-1, -1)]
    z_local = [i + 1 for i, p in enumerate(per_block) if p[1] == -p[0]]
    w_local = [i + 1 for i, p in enumerate(per_block) if p[1] == p[0]]
    assert z_local == [2, 3]
    assert w_local == [1, 4]

    starts = [33, 37, 41]
    z_labels = [s + i - 1 for s in starts for i in z_local]
    w_labels = [s + i - 1 for s in starts for i in w_local]
    assert z_labels == [34, 35, 38, 39, 42, 43]
    assert w_labels == [33, 36, 37, 40, 41, 44]
    assert sorted(z_labels + w_labels) == list(range(33, 45))

    print("PASS")
    print("first_factor_z_fixed:", z_labels)
    print("second_factor_w_fixed:", w_labels)


if __name__ == "__main__":
    main()
