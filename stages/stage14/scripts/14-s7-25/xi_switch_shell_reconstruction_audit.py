#!/usr/bin/env python3
"""Deterministic regression/falsifier for Stage14-s7-25.

The asymptotic theorem is the divisor reconstruction in 14-s7-25/result.md.
This script checks the exact two-shell identities on finite physical packets,
validates the elementary shell-count mechanisms, and freezes the dyadic
exponent ledger.  Finite enumeration is diagnostic, not the proof.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


ch = load_module(
    "stage14_4ch_s725",
    SCRIPTS / "14-4" / "eight_cell_residual_lift_audit.py",
)


def tau(n: int) -> int:
    assert n >= 1
    x = n
    out = 1
    p = 2
    while p * p <= x:
        if x % p:
            p = 3 if p == 2 else p + 2
            continue
        e = 0
        while x % p == 0:
            x //= p
            e += 1
        out *= e + 1
        p = 3 if p == 2 else p + 2
    if x > 1:
        out *= 2
    return out


def v2(n: int) -> int:
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def oddpart(n: int) -> int:
    return n >> v2(n)


def shell_proxy(U: int, V: int, M: int, N: int, hk_plus: int, hx_minus: int, W: int) -> int:
    # Deliberately loose finite proxy for the divisor reconstruction.
    # Constants absorb signs/parity/2-adic decorations.
    return (
        256
        * tau(hk_plus * hk_plus)
        * tau(hx_minus * hx_minus)
        * tau(U)
        * tau(V)
        * tau(M)
        * tau(N)
        * tau(W) ** 3
    )


def audit_physical_pair(a: dict[str, int], b: dict[str, int]):
    cells, triple, qs, hs = ch.residual_data(a, b)
    ch.audit_pair(a, b)

    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u, v = triple
    qk, qxi = qs
    hk_plus, hk_minus, hx_plus, hx_minus = hs

    U = S * T
    V = R * J
    M = beta * gamma
    N = alpha * delta
    rho = a["r"] * b["r"] * a["s"] * b["s"]
    W = a["x"] * a["y"] * b["x"] * b["y"]

    assert a["xi"] == b["xi"] == U * V
    assert a["k"] == b["k"] == M * N
    assert qk == C * u
    assert qxi == C * v

    # Exact common-core odd-part normalization.
    assert oddpart(hk_plus) == C * oddpart(U)
    assert oddpart(hx_plus) == C * oddpart(M)
    assert hk_plus == (2 ** v2(hk_plus)) * C * oddpart(U)
    assert hx_plus == (2 ** v2(hx_plus)) * C * oddpart(M)

    # First Pythagorean shell.
    assert hk_plus * hk_plus == hk_minus * hk_minus + (2 * rho * N) ** 2
    assert U * V * C * u == hk_plus * hk_minus
    assert hk_minus * (2 ** v2(hk_plus)) == (2 ** v2(U)) * V * u

    # Second difference-of-squares shell and its dyadic cancellation.
    assert hx_plus * hx_plus - (2 * V * W) ** 2 == hx_minus * hx_minus
    assert M * N * C * v == hx_plus * hx_minus
    assert hx_minus * (2 ** v2(hx_plus)) == (2 ** v2(M)) * N * v

    # The recovered products split back to the eight cells and four roots.
    assert S * T == U
    assert R * J == V
    assert beta * gamma == M
    assert alpha * delta == N
    assert a["x"] * a["y"] * b["x"] * b["y"] == W

    proxy = shell_proxy(U, V, M, N, hk_plus, hx_minus, W)
    return (triple, U), (a["P"], a["Q"], b["P"], b["Q"]), proxy


def finite_physical_audit(limit: int = 500) -> tuple[int, int, int]:
    groups = ch.make_groups(limit)
    fixed_key_rows: dict[object, list[tuple[int, int, int, int]]] = defaultdict(list)
    fixed_key_proxies: dict[object, list[int]] = defaultdict(list)
    checked = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                # Keep the same dual-cross physical coefficient space as s7-21/X1.
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                key, physical, proxy = audit_physical_pair(a, b)
                fixed_key_rows[key].append(physical)
                fixed_key_proxies[key].append(proxy)
                checked += 1

    assert checked > 0
    max_fiber = max(len(rows) for rows in fixed_key_rows.values())
    max_proxy = max(max(values) for values in fixed_key_proxies.values())

    for key, rows in fixed_key_rows.items():
        assert len(rows) <= max(fixed_key_proxies[key])

    return checked, max_fiber, max_proxy


def elementary_shell_count_audit() -> None:
    # Any integer points on A^2+B^2=H^2 are certainly bounded by 4*tau(H^2).
    for H in range(1, 81):
        count = 0
        for A in range(H + 1):
            B2 = H * H - A * A
            B = int(B2 ** 0.5)
            while (B + 1) * (B + 1) <= B2:
                B += 1
            while B * B > B2:
                B -= 1
            if B * B == B2:
                count += 1
        assert count <= 4 * tau(H * H)

    # H^2-Z^2=L^2 is parameterized by factor pairs of L^2.
    for L in range(1, 81):
        n = L * L
        solutions = set()
        for d in range(1, n + 1):
            if n % d:
                continue
            e = n // d
            if d > e or (d + e) % 2 or (e - d) % 2:
                continue
            H = (d + e) // 2
            Z = (e - d) // 2
            assert H * H - Z * Z == n
            solutions.add((H, Z))
        assert len(solutions) <= tau(n)


def exponent_ledger_audit() -> None:
    current = Fraction(7, 8)
    theta_max = Fraction(5, 16)
    theta_min = Fraction(3, 16)
    phi_min = Fraction(1, 8)
    phi_max = Fraction(1, 4)

    blocks = []
    for ti in range(3, 6):
        theta = Fraction(ti, 16)
        for pi in range(2, 5):
            phi = Fraction(pi, 16)
            if not (theta_min <= theta <= theta_max and phi_min <= phi <= phi_max):
                continue
            if theta < phi:
                continue
            if theta - phi > Fraction(1, 8):
                continue
            if theta + phi < Fraction(3, 8):
                continue

            residual = 2 * (theta + phi) - Fraction(1, 2)
            U_support = Fraction(3, 4) - 2 * phi
            packet = residual + U_support
            assert packet == 2 * theta + Fraction(1, 4)
            assert current - packet == 2 * (theta_max - theta)
            blocks.append((theta, phi, packet))

    assert blocks
    assert max(packet for _, _, packet in blocks) == current
    max_blocks = [(theta, phi) for theta, phi, packet in blocks if packet == current]
    assert all(theta == theta_max for theta, _ in max_blocks)
    assert [phi for _, phi in max_blocks] == [Fraction(3, 16), Fraction(1, 4)]

    assert 2 * theta_max + Fraction(1, 4) == current
    assert theta_max - Fraction(1, 8) == Fraction(3, 16)


def main() -> None:
    elementary_shell_count_audit()
    exponent_ledger_audit()
    checked, max_fiber, max_proxy = finite_physical_audit()

    print("Stage14-s7-25 xi-switch shell reconstruction audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"max finite fixed-(C,u,v,U) physical fiber: {max_fiber}")
    print(f"max finite loose divisor proxy: {max_proxy}")
    print("first shell: (Hk+)^2=(Hk-)^2+(2*rho*N)^2 exact")
    print("second shell: (Hxi+)^2-(2*V*W)^2=(Hxi-)^2 exact")
    print("fixed (C,u,v,U) packet fiber theorem: B^o(1) by divisor reconstruction")
    print("dyadic packet exponent: 2*theta+1/4")
    print("remaining 7/8 barrier: theta=5/16, phi in [3/16,1/4]")
    print("new whole-family power saving: not proved")


if __name__ == "__main__":
    main()
