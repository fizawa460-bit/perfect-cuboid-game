#!/usr/bin/env python3
"""Deterministic audit for Stage14-4co.

Checks the lambda=4 singular Mobius lift, the two gcd-square identities,
residual squareclass locks, and a synthetic infinite primitive family showing
that the rational singular branch is not divisor-many by algebra alone.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd, isqrt
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


cn = load_module(
    "stage14_4cn_4co",
    SCRIPTS / "14-4" / "reciprocal_edwards_reduction_audit.py",
)
ch = cn.ch


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def squarefree_kernel(n: int) -> int:
    n = abs(n)
    assert n >= 1
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out *= n
    return out


def is_square(n: int) -> bool:
    if n < 0:
        return False
    r = isqrt(n)
    return r * r == n


def singular_data(a_state: dict[str, int], b_state: dict[str, int]):
    triple, singular, lam = cn.audit_pair(a_state, b_state)
    cells, _, _, _ = ch.residual_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = cells
    _, u_res, v_res = triple

    r = a_state["r"] * b_state["r"]
    s = a_state["s"] * b_state["s"]
    X = a_state["x"] * b_state["x"]
    Y = a_state["y"] * b_state["y"]
    A = alpha * r
    D = delta * s
    P = R * X
    Q = J * Y

    X_ag = R * J
    K_ag = alpha * delta
    lx_m = gcd(oddpart(X_ag), D - A)
    lx_p = gcd(oddpart(X_ag), D + A)
    lk_m = gcd(oddpart(K_ag), Q - P)
    lk_p = gcd(oddpart(K_ag), Q + P)

    cx_m = (D - A) // lx_m
    cx_p = (D + A) // lx_p
    ck_m = (Q - P) // lk_m
    ck_p = (Q + P) // lk_p
    eps_x = X_ag // oddpart(X_ag)
    eps_k = K_ag // oddpart(K_ag)

    if singular:
        # Notation of result.md: a=cx+, b=cx-, c=ck+, d=ck-.
        aa, bb, cc, dd = cx_p, cx_m, ck_p, ck_m
        uu, vv, nn, mm = lx_p, lx_m, lk_p, lk_m

        Gk = gcd(dd * (aa * uu + bb * vv), cc * (aa * uu - bb * vv))
        Gx = gcd(bb * (cc * nn + dd * mm), aa * (cc * nn - dd * mm))

        assert nn == dd * (aa * uu + bb * vv) // Gk
        assert mm == cc * (aa * uu - bb * vv) // Gk
        assert uu == bb * (cc * nn + dd * mm) // Gx
        assert vv == aa * (cc * nn - dd * mm) // Gx

        rhs_k = 4 * r * s * eps_k * cc * dd
        rhs_x = 4 * X * Y * eps_x * aa * bb
        assert Gk * Gk == rhs_k
        assert Gx * Gx == rhs_x
        assert is_square(rhs_k) and is_square(rhs_x)

        assert squarefree_kernel(oddpart(v_res)) == squarefree_kernel(oddpart(r * s))
        assert squarefree_kernel(oddpart(u_res)) == squarefree_kernel(oddpart(X * Y))

    return singular, lam


def synthetic_family_audit() -> int:
    # a=b=c=1, d=4, r=s=X=Y=eps_x=eps_k=1 gives lambda=4.
    count = 0
    for t in range(1, 100, 2):
        u, v = 4 * t + 1, 1
        m, n = t, 4 * t + 2
        assert gcd(u, v) == 1
        assert gcd(m, n) == 1

        assert u * u - v * v == 4 * m * n
        assert n * n - (4 * m) * (4 * m) == 4 * u * v

        D = (u + v) // 2
        A = (u - v) // 2
        Q = (n + 4 * m) // 2
        P = (n - 4 * m) // 2
        assert D > A > 0 and Q > P > 0
        assert D * (Q - P) == A * (Q + P)

        Gk = gcd((u + v) * 4, u - v)
        Gx = gcd(n + 4 * m, n - 4 * m)
        assert Gk == 4
        assert Gx == 2
        count += 1
    return count


def exponent_ledger_audit() -> None:
    for phi in (Fraction(3, 16), Fraction(13, 64), Fraction(7, 32), Fraction(15, 64), Fraction(1, 4)):
        gu = Fraction(5, 8) - 2 * phi
        gv = 2 * phi - Fraction(3, 8)
        assert gu >= 0 and gv >= 0
        assert gu + gv == Fraction(1, 4)
        assert gu / 2 + gv / 2 == Fraction(1, 8)


def boundary_audit() -> None:
    root = HERE.parents[4]
    cn_text = (root / "stages/stage14/14-4cn/result.md").read_text()
    s28_text = (root / "stages/stage14/14-s7-28/result.md").read_text()
    x5_text = (root / "stages/stage14/14-X5/result.md").read_text()
    assert "STAGE14_4CN=COMPLETE_PRIMITIVE_RATIO_INJECTIVITY_AND_RECIPROCAL_EDWARDS_SINGULAR_SMOOTH_SPLIT" in cn_text
    assert "STAGE14_S7_28=" in s28_text
    assert "STAGE14_X5=COMPLETE_RECIPROCAL_BIQUADRATIC_SINGULAR_LOCUS_AND_POSITIVE_COMPONENT_REDUCTION" in x5_text


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()
    synthetic_count = synthetic_family_audit()

    groups = ch.make_groups(600)
    checked = 0
    singular_hits = 0
    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                singular, _ = singular_data(a_state, b_state)
                checked += 1
                singular_hits += int(singular)

    assert checked > 0
    print("Stage14-4co singular Cayley squareclass audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite physical lambda=4 hits: {singular_hits}")
    print("singular gcd-square identities: exact on every finite singular hit")
    print("odd v_res squareclass = odd r*s squareclass: exact")
    print("odd u_res squareclass = odd X*Y squareclass: exact")
    print("fixed-root residual-pair exponent: 1/8 vs raw 1/4")
    print(f"synthetic primitive singular family members checked: {synthetic_count}")
    print("singular rational fiber B^o(1): NOT PROVED")
    print("whole-family exponent remains 7/8")


if __name__ == "__main__":
    main()
