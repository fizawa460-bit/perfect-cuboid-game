#!/usr/bin/env python3
"""Deterministic audit for Stage14-X6.

Checks the exact singular/common-core coupling implication and the primitive
plus/minus quadratic-value four-root structure on the frozen physical family.
Finite enumeration is diagnostic only; the asymptotic singular elimination is
proved in result.md by squarefree valuation parity plus the top-theta ledger.
"""

from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
SCRIPTS = HERE.parents[1]
ROOT = HERE.parents[4]


def load_module(name: str, path: Path):
    spec = spec_from_file_location(name, path)
    assert spec is not None and spec.loader is not None
    module = module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


s28 = load_module(
    "stage14_s728_x6",
    SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py",
)
ch = s28.ch


def v2(n: int) -> int:
    assert n > 0
    e = 0
    while n % 2 == 0:
        n //= 2
        e += 1
    return e


def oddpart(n: int) -> int:
    assert n > 0
    return n >> v2(n)


def valuation(n: int, p: int) -> int:
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def prime_factors(n: int) -> set[int]:
    n = abs(n)
    out: set[int] = set()
    p = 2
    while p * p <= n:
        if n % p:
            p = 3 if p == 2 else p + 2
            continue
        out.add(p)
        while n % p == 0:
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.add(n)
    return out


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    d = s28.packet_data(a_state, b_state)
    s28.audit_reconstruction(d)

    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, _, _ = d["triple"]
    hk_plus, _, hx_plus, _ = d["hs"]

    r = int(d["r"])
    s = int(d["s"])
    A = int(d["A"])
    D = int(d["D"])
    P = int(d["P"])
    Q = int(d["Q"])
    epsk = int(d["epsilon_k"])

    u = int(d["lx_plus"])
    v = int(d["lx_minus"])
    aa = int(d["cx_plus"])
    bb = int(d["cx_minus"])

    assert gcd(u, v) == 1
    assert D + A == aa * u
    assert D - A == bb * v

    K_switch = beta * gamma
    Xi_switch = S * T
    G = a_state["g"] * b_state["g"]
    assert G in (1, 2, 4)

    # Imported common-core plus coupling.
    assert G * K_switch * hk_plus == 2 * Xi_switch * hx_plus

    # The X5/s7-28 singular condition and its two square-kernel identities are
    # equivalent on positive physical packets once the plus coupling is used.
    K_ratio = 16 * r * s * int(d["X"]) * int(d["Y"]) * int(d["epsilon_x"]) * epsk
    singular = K_ratio == 4 * aa * bb * int(d["ck_plus"]) * int(d["ck_minus"])
    relation = D * (Q - P) == A * (Q + P)
    assert singular == relation

    plus_square_identity = G * K_switch * (D + A) ** 2 == 4 * Xi_switch * Q * Q
    minus_square_identity = G * K_switch * (D - A) ** 2 == 4 * Xi_switch * P * P
    assert plus_square_identity == singular
    assert minus_square_identity == singular

    if singular:
        assert oddpart(K_switch) == 1
        assert oddpart(Xi_switch) == 1

    # Primitive quadratic values.
    F_minus = aa * aa * u * u - bb * bb * v * v
    F_plus = aa * aa * u * u + bb * bb * v * v
    Nk = oddpart(alpha * delta)

    assert F_minus == 4 * r * s * epsk * Nk
    assert F_plus == 2 * hk_plus
    assert oddpart(F_plus) == C * oddpart(Xi_switch)

    # Fixed common support theorem.
    common = gcd(F_minus, F_plus)
    assert (2 * aa * aa * bb * bb) % common == 0

    bad = 2 * aa * bb * r * s * C
    good_minus = set()
    good_plus = set()

    # Real root classes for good k-agreement primes.
    for p in prime_factors(Nk):
        if bad % p == 0:
            continue
        assert p % 2 == 1
        assert F_minus % p == 0
        assert valuation(F_minus, p) == 1
        assert (aa * bb * u * v) % p != 0
        t = (u * pow(v, -1, p)) % p
        q = (bb * pow(aa, -1, p)) % p
        assert t == q or t == (-q) % p
        good_minus.add(p)

    # Quadratic-twist root classes for good xi-switch primes.
    for p in prime_factors(Xi_switch):
        if bad % p == 0:
            continue
        assert p % 2 == 1
        assert F_plus % p == 0
        assert (aa * bb * u * v) % p != 0
        assert p % 4 == 1
        t = (u * pow(v, -1, p)) % p
        q = (bb * pow(aa, -1, p)) % p
        assert (t * t + q * q) % p == 0
        good_plus.add(p)

    assert good_minus.isdisjoint(good_plus)
    return singular, len(good_minus), len(good_plus)


def exponent_ledger_audit() -> None:
    theta = Fraction(5, 16)
    k_switch_exp = 1 - 2 * theta
    assert k_switch_exp == Fraction(3, 8)

    for phi in (Fraction(3, 16), Fraction(7, 32), Fraction(1, 4)):
        xi_switch_exp = Fraction(3, 4) - 2 * phi
        assert xi_switch_exp >= Fraction(1, 4)
        assert xi_switch_exp <= Fraction(3, 8)


def boundary_audit() -> None:
    x5 = (ROOT / "stages/stage14/14-X5/result.md").read_text()
    s28_text = (ROOT / "stages/stage14/14-s7-28/result.md").read_text()
    cg = (ROOT / "stages/stage14/14-4cg/result.md").read_text()
    cn = (ROOT / "stages/stage14/14-4cn/result.md").read_text()

    assert "STAGE14_X5=COMPLETE_RECIPROCAL_BIQUADRATIC_SINGULAR_LOCUS_AND_POSITIVE_COMPONENT_REDUCTION" in x5
    assert "PHYSICAL_SINGULAR_HOST_IDENTITY=D*(Q-P)=A*(Q+P)" in x5
    assert "STAGE14_S7_28=COMPLETE_RATIO_SINGULAR_CLASSIFICATION_AND_PRIMITIVE_MODULUS_PAIR_RECONSTRUCTION" in s28_text
    assert "GENERIC_GENUS_ONE_RECEIVER_MINIMAL=false" in s28_text
    assert "REMAINING_RECEIVER=TopThetaPrimitiveAgreementQuadraticValueDivisibilityIncidence" in s28_text
    assert "g_1 g_2 K_switch H_k^+" in cg
    assert "CAYLEY_SINGULAR_CROSS_ROLE_RELATION=D*(Q-P)=A*(Q+P)" in cn


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()

    groups = ch.make_groups(600)
    checked = 0
    singular_hits = 0
    good_minus_checks = 0
    good_plus_checks = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                singular, gm, gp = audit_packet(a_state, b_state)
                singular_hits += int(singular)
                good_minus_checks += gm
                good_plus_checks += gp
                checked += 1

    assert checked == 52

    print("Stage14-X6 singular elimination / four-root CRT audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"finite singular lambda=4 hits: {singular_hits}")
    print(f"good real-root prime checks: {good_minus_checks}")
    print(f"good twisted-root prime checks: {good_plus_checks}")
    print("singular square-kernel identities: exact")
    print("top-theta singular branch elimination: algebraic theorem in result.md")
    print("gcd(F_minus,F_plus) | 2*a^2*b^2: exact")
    print("good k-agreement roots: +/-b/a")
    print("good xi-switch roots: +/-i*b/a, p=1 mod 4")
    print("whole-family exponent remains 7/8")


if __name__ == "__main__":
    main()
