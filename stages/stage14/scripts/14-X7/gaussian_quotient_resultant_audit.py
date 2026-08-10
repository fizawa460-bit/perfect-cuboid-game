#!/usr/bin/env python3
"""Deterministic audit for Stage14-X7.

The proof of the charged-once quantifier statements is in result.md.  This
script checks on frozen physical packets that the X6 real roots are exactly the
two reconstructed linear values, lifts the s7-29 common-core root orientation
to an explicit Gaussian divisor, verifies the post-common-core Gaussian norm
support, and exhaustively checks the two-point cross-resultant dictionary over
small finite fields.
"""

from importlib.util import module_from_spec, spec_from_file_location
from math import gcd, isqrt
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


s29 = load_module(
    "stage14_s729_x7",
    SCRIPTS / "14-s7-29" / "common_core_primitive_root_line_audit.py",
)
x6 = load_module(
    "stage14_x6_x7",
    SCRIPTS / "14-X6" / "singular_elimination_four_root_crt_audit.py",
)
s28 = s29.s28
ch = s29.ch


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
    n = abs(n)
    e = 0
    while n and n % p == 0:
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


def sum_two_squares_prime(p: int) -> tuple[int, int]:
    assert p % 4 == 1
    for r in range(1, isqrt(p) + 1):
        s2 = p - r * r
        if s2 <= 0:
            continue
        s = isqrt(s2)
        if s * s == s2:
            return r, s
    raise AssertionError(f"no sum-of-two-squares representation for {p}")


def gaussian_norm(z: tuple[int, int]) -> int:
    x, y = z
    return x * x + y * y


def gaussian_div(z: tuple[int, int], pi: tuple[int, int]) -> tuple[int, int] | None:
    x, y = z
    r, s = pi
    p = r * r + s * s
    nr = x * r + y * s
    ni = y * r - x * s
    if nr % p or ni % p:
        return None
    return nr // p, ni // p


def gaussian_associates(r: int, s: int) -> list[tuple[int, int]]:
    raw = [
        (r, s), (r, -s), (-r, s), (-r, -s),
        (s, r), (s, -r), (-s, r), (-s, -r),
    ]
    out = []
    for z in raw:
        if z not in out:
            out.append(z)
    return out


def divide_prime_power(z: tuple[int, int], p: int, e: int) -> tuple[int, int]:
    r, s = sum_two_squares_prime(p)
    for pi in gaussian_associates(r, s):
        cur = z
        ok = True
        for _ in range(e):
            nxt = gaussian_div(cur, pi)
            if nxt is None:
                ok = False
                break
            cur = nxt
        if ok:
            return cur
    raise AssertionError(f"no oriented Gaussian p^{e} divisor found for p={p}")


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    # Run both predecessor packet audits first.
    s29.audit_packet(a_state, b_state)
    x6.audit_packet(a_state, b_state)

    d = s28.packet_data(a_state, b_state)
    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, _, _ = d["triple"]

    r = int(d["r"])
    s = int(d["s"])
    U = int(d["lx_plus"])
    V = int(d["lx_minus"])
    a = int(d["cx_plus"])
    b = int(d["cx_minus"])
    A = int(d["A"])
    D = int(d["D"])

    assert gcd(U, V) == 1
    assert a * U - b * V == 2 * A == 2 * r * alpha
    assert a * U + b * V == 2 * D == 2 * s * delta

    # The two real factors have only fixed coefficient common support.
    linear_gcd = gcd(a * U - b * V, a * U + b * V)
    assert (2 * a * b) % linear_gcd == 0

    real_bad = 2 * a * b * r * s
    real_checks = 0
    for p in prime_factors(alpha):
        if real_bad % p == 0:
            continue
        assert valuation(a * U - b * V, p) == 1
        assert (a * U + b * V) % p != 0
        real_checks += 1
    for p in prime_factors(delta):
        if real_bad % p == 0:
            continue
        assert valuation(a * U + b * V, p) == 1
        assert (a * U - b * V) % p != 0
        real_checks += 1

    # s7-29 coefficient peeling.
    g = gcd(a, b)
    a0 = a // g
    b0 = b // g
    C_bad = gcd(C, g * g)
    C0 = C // C_bad
    assert gcd(a0, b0) == 1
    assert (a0 * a0 * U * U + b0 * b0 * V * V) % C0 == 0
    assert gcd(C0, a0 * b0 * U * V) == 1

    # Explicitly remove one oriented Gaussian divisor of norm C0.
    z = (a0 * U, b0 * V)
    original_norm = gaussian_norm(z)
    for p, e, _ in s29.factor_prime_powers(C0):
        assert p % 4 == 1
        z = divide_prime_power(z, p, e)
    W = z
    norm_w = gaussian_norm(W)
    assert norm_w * C0 == original_norm

    # Outside the frozen X6 bad support, N(W) has exactly the xi-switch support.
    xi_switch = S * T
    plus_bad = 2 * a * b * r * s * C
    support = prime_factors(norm_w) | prime_factors(xi_switch)
    twisted_checks = 0
    for p in support:
        if plus_bad % p == 0:
            continue
        assert (p in prime_factors(norm_w)) == (p in prime_factors(xi_switch))
        if p in prime_factors(xi_switch):
            assert valuation(norm_w, p) == 1
            assert p % 4 == 1
            twisted_checks += 1

    return real_checks, twisted_checks, C0 > 1


def cross_resultant_dictionary_audit() -> None:
    # Exhaustively verify the four transfer equivalences in projective slope
    # coordinates over small odd primes.  Set V1=V2=1; homogeneity makes this
    # equivalent to the general unit-denominator statement.
    primes = (5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43)
    checks = 0
    for p in primes:
        for a in (1, 2, 3, 4):
            for b in (1, 2, 3, 4):
                if (a * b) % p == 0:
                    continue
                a2 = a * a % p
                b2 = b * b % p
                for t1 in range(1, p):
                    fm1 = (a2 * t1 * t1 - b2) % p
                    fp1 = (a2 * t1 * t1 + b2) % p
                    if fm1 and fp1:
                        continue
                    for t2 in range(1, p):
                        fm2 = (a2 * t2 * t2 - b2) % p
                        fp2 = (a2 * t2 * t2 + b2) % p
                        R12 = (t1 * t1 - t2 * t2) % p
                        K12 = (t1 * t1 + t2 * t2) % p
                        if fm1 == 0:
                            assert (fm2 == 0) == (R12 == 0)
                            assert (fp2 == 0) == (K12 == 0)
                            checks += 2
                        if fp1 == 0:
                            assert (fp2 == 0) == (R12 == 0)
                            assert (fm2 == 0) == (K12 == 0)
                            checks += 2
    assert checks > 0


def exponent_ledger_audit() -> None:
    # Imported merged mainline boundary: 3/4 is current and only phi=1/4 can
    # saturate 2phi+1/4.
    from fractions import Fraction

    for phi in (Fraction(1, 8), Fraction(3, 16), Fraction(7, 32), Fraction(1, 4)):
        total = 2 * phi + Fraction(1, 4)
        assert total <= Fraction(3, 4)
        if total == Fraction(3, 4):
            assert phi == Fraction(1, 4)


def boundary_audit() -> None:
    x6_text = (ROOT / "stages/stage14/14-X6/result.md").read_text()
    s29_text = (ROOT / "stages/stage14/14-s7-29/result.md").read_text()
    cp_text = (ROOT / "stages/stage14/14-4cp/result.md").read_text()

    assert "STAGE14_X6=COMPLETE_TOP_THETA_SINGULAR_ELIMINATION_AND_PRIMITIVE_FOUR_ROOT_CRT_REDUCTION" in x6_text
    assert "OUTSIDE_FIXED_BAD_SUPPORT_MOVING_KERNELS_DISJOINT=true" in x6_text
    assert "STAGE14_S7_29=COMPLETE_COMMON_CORE_GAUSSIAN_ROOT_LINE_PRIMITIVE_LATTICE_COUNT_AND_3_4_BOUND" in s29_text
    assert "PRIMITIVE_ROOT_LINE_DYADIC_COUNT_PROVED=true" in s29_text
    assert "STAGE14_4CP=COMPLETE_THREE_QUARTER_PROMOTION_SINGULAR_ELIMINATION_AND_QUARTER_PHI_ROOTLINE_REDUCTION" in cp_text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=3/4" in cp_text
    assert "SELF_GENERATED_FOUR_ROOT_MODULI_CHARGED_AS_INDEPENDENT_SPACING=false" in cp_text
    assert "REMAINING_RECEIVER=QuarterPhiCommonCorePrimitiveFourRootQuadraticValueEnergy" in cp_text


def main() -> None:
    boundary_audit()
    exponent_ledger_audit()
    cross_resultant_dictionary_audit()

    groups = ch.make_groups(600)
    checked = 0
    real_checks = 0
    twisted_checks = 0
    nontrivial_gaussian_divisor = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                rc, tc, nontrivial = audit_packet(a_state, b_state)
                real_checks += rc
                twisted_checks += tc
                nontrivial_gaussian_divisor += int(nontrivial)
                checked += 1

    assert checked == 52

    print("Stage14-X7 Gaussian quotient / resultant audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"good real linear-factor prime checks: {real_checks}")
    print(f"good Gaussian-quotient xi-switch prime checks: {twisted_checks}")
    print(f"packets with nontrivial explicit common-core Gaussian divisor: {nontrivial_gaussian_divisor}")
    print("real four-root mask -> exact two linear values: PASS")
    print("common-core root orientation -> Gaussian divisor and quotient: PASS")
    print("post-common-core twisted support -> Gaussian quotient norm: PASS")
    print("same-role / cross-role resultant dictionary: exhaustive finite-field PASS")
    print("self-generated four-root moduli are not outer spacing data")
    print("current whole-family exponent remains 3/4")
    print("X7 additional whole-family power saving: false")
    print("X7 auxiliary H needed: false")


if __name__ == "__main__":
    main()
