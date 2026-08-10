#!/usr/bin/env python3
"""Deterministic audit for Stage14-X12 lost-core fourth-root coupling."""

from __future__ import annotations

from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
X11 = ROOT / "stages/stage14/14-X11/result.md"
S737 = ROOT / "stages/stage14/14-s7-37/result.md"
S735 = ROOT / "stages/stage14/14-s7-35/result.md"
CU = ROOT / "stages/stage14/14-4cu/result.md"
X12 = ROOT / "stages/stage14/14-X12/result.md"

ENTERING = F(19, 34)
TARGET = F(71, 128)
PROP = F(7, 16)


def need(text: str, token: str, source: str) -> None:
    assert token in text, f"missing {token!r} in {source}"


def factor(n: int) -> dict[int, int]:
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1 if p == 2 else 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def divisors(n: int) -> list[int]:
    ds = [1]
    for p, e in factor(n).items():
        old = list(ds)
        mul = 1
        for _ in range(e):
            mul *= p
            ds.extend(d * mul for d in old)
    return sorted(set(ds))


def root4(n: int) -> int:
    r = 1
    for p, e in factor(n).items():
        r *= p ** ((e + 3) // 4)
    return r


def predecessor_audit() -> None:
    x11 = X11.read_text()
    s737 = S737.read_text()
    s735 = S735.read_text()
    cu = CU.read_text()

    need(x11, "STAGE14_X11=COMPLETE_PROPORTIONAL_FOUR_ROOT_GCD_DECOMPOSITION_AND_19_34_PROMOTION", "X11")
    need(x11, "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=19/34", "X11")
    need(s737, "STAGE14_S7_37=COMPLETE_PROPORTIONAL_SAMESIDE_RESIDUAL_TRANSFER_AND_19_34_REFINEMENT", "s7-37")
    need(s737, "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16", "s7-37")
    need(s735, "XI_EXTRA_GCD_DIVIDES_ENDPOINT_OMEGA_PRODUCT=true", "s7-35")
    need(s735, "rho=2eta_star", "s7-35")
    need(cu, "J_star=gcd(C_Cayley,C_res)", "4cu")
    need(cu, "J_star | L_-*L_+", "4cu")
    need(cu, "No switched-cell prime is discarded", "4cu")


def lost_core_integer_audit() -> int:
    """Check D0|Hs^4 Ho^2 => R4(D0)|Hs*Ho with endpoint overlap removed."""
    checks = 0
    for hs in (1, 3, 5, 7, 9, 11, 15, 25):
        for ho in (1, 3, 5, 7, 9, 11, 13):
            if gcd(hs, ho) != 1:
                continue
            for omega in (1, 3, 5, 9, 15, 21, 25):
                ambient = omega * hs**4 * ho**2
                for d in divisors(ambient):
                    d0 = d // gcd(d, omega)
                    assert (hs**4 * ho**2) % d0 == 0
                    q = root4(d0)
                    assert (hs * ho) % q == 0
                    assert q**4 >= d0
                    checks += 1
    assert checks > 1000
    return checks


def column_transfer_audit() -> int:
    """If q divides both columns and the column moduli are coprime, q divides h_-h_+."""
    checks = 0
    for jm in range(1, 18):
        for jp in range(1, 18):
            if gcd(jm, jp) != 1:
                continue
            for hm in range(1, 18):
                lm = jm * hm
                for hp in range(1, 18):
                    lp = jp * hp
                    common = gcd(lm, lp)
                    for q in divisors(common):
                        assert (hm * hp) % q == 0
                        checks += 1
    assert checks > 10000
    return checks


def admissible(theta: F, phi: F) -> bool:
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and 0 <= theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def e_s(theta: F) -> F:
    return max(2 * theta, 1 - 2 * theta)


def e_k(theta: F) -> F:
    return 3 * theta - F(1, 4)


def e_new(theta: F, phi: F) -> F:
    return F(3, 2) * phi - F(6, 5) * theta + F(41, 80)


def exponent_audit() -> tuple[int, list[tuple[F, F]]]:
    assert ENTERING - TARGET == F(9, 2176)
    assert TARGET - F(1, 2) == F(7, 128)
    assert PROP < F(1, 2) < TARGET

    # denominator 1024 contains theta=71/256 and phi=1/4 exactly.
    mesh: list[tuple[F, F, F]] = []
    for ti in range(int(F(3, 16) * 1024), int(F(5, 16) * 1024) + 1):
        theta = F(ti, 1024)
        for pi in range(int(F(1, 8) * 1024), int(F(1, 4) * 1024) + 1):
            phi = F(pi, 1024)
            if not admissible(theta, phi):
                continue
            val = min(e_s(theta), e_k(theta), e_new(theta, phi))
            assert val <= TARGET
            mesh.append((val, theta, phi))

    worst = max(v for v, _, _ in mesh)
    sat = [(t, p) for v, t, p in mesh if v == TARGET]
    assert worst == TARGET
    assert sat == [(F(71, 256), F(1, 4))]

    theta = F(71, 256)
    phi = F(1, 4)
    chi = 2 * theta + 2 * phi - F(3, 4)
    eta_star = F(3, 128)
    eta_other = F(0)
    rho = 2 * eta_star
    j = chi - 4 * eta_star - 2 * eta_other
    lost = chi - j
    raw_col = F(1, 4) - j
    forced = lost / 4
    eff_col = raw_col - forced
    row = F(1, 4) - j

    assert chi == F(39, 128)
    assert rho == F(3, 64)
    assert j == F(27, 128)
    assert lost == F(3, 32)
    assert raw_col == F(5, 128)
    assert forced == F(3, 128)
    assert eff_col == F(1, 64)
    assert row == F(5, 128)
    assert 2 * phi + eff_col + row == TARGET

    eh = 3 * phi - F(1, 8) - 3 * eta_star - 3 * eta_other
    erc = 2 * phi + F(1, 2) - 2 * chi + 7 * eta_star + F(7, 2) * eta_other
    assert eh == erc == TARGET
    assert e_s(theta) == TARGET
    assert e_new(theta, phi) == TARGET

    return len(mesh), sat


def weighted_cancellation_audit() -> int:
    checks = 0
    for ti in range(0, 25):
        eta_star = F(ti, 256)
        for oi in range(0, ti + 1):
            eta_other = F(oi, 256)
            for theta in (F(1, 4), F(71, 256), F(19, 68), F(5, 16)):
                for phi in (F(3, 16), F(1, 4)):
                    chi = 2 * theta + 2 * phi - F(3, 4)
                    eh = 3 * phi - F(1, 8) - 3 * eta_star - 3 * eta_other
                    erc = 2 * phi + F(1, 2) - 2 * chi + 7 * eta_star + F(7, 2) * eta_other
                    avg = (7 * eh + 3 * erc) / 10
                    expected = F(3, 2) * phi - F(6, 5) * theta + F(41, 80) - F(21, 20) * eta_other
                    assert avg == expected
                    checks += 1
    return checks


def boundary_audit() -> None:
    text = X12.read_text()
    tokens = [
        "STAGE14_X12=COMPLETE_LOST_CORE_FOURTH_ROOT_COLUMN_COFACTOR_COUPLING_AND_71_128_PROMOTION",
        "LOST_CORE_QUOTIENT_D_EQUALS_C_OVER_J=true",
        "LOST_CORE_QUOTIENT_DIVIDES_ENDPOINT_SMALL_HSTAR4_HOTHER2=true",
        "LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_H=true",
        "LOST_CORE_FOURTH_ROOT_DIVISOR_DIVIDES_COLUMN_COFACTOR_PRODUCT=true",
        "REFINED_ROW_COLUMN_COMPLETE_COUNT=2phi+1/2-chi/4-7j/4",
        "NONPROPORTIONAL_WEIGHTED_COMPLETE_COUNT_COMBINATION=7:3",
        "NONPROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=71/128",
        "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=7/16",
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=71/128",
        "IMPROVEMENT_OVER_MERGED_19_34=9/2176",
        "CURRENT_GAP_TO_SQRT=7/128",
        "SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_SATURATION_THETA=71/256",
        "SEVENTY_ONE_ONE_HUNDRED_TWENTY_EIGHTHS_EFFECTIVE_COLUMN_QUOTIENT_EXPONENT=1/64",
        "SWITCHED_CELL_PRIMES_MAY_REMAIN_IN_J=true",
        "JOINT_CORE_CROSS_ROOT_PRODUCT_SHORTCUT_USED=false",
        "X12_AUXILIARY_H_NEEDED=false",
        "NEXT_RECOMMENDED=Stage14-X13",
    ]
    for token in tokens:
        need(text, token, "X12")


def main() -> None:
    predecessor_audit()
    lost_checks = lost_core_integer_audit()
    column_checks = column_transfer_audit()
    mesh_points, sat = exponent_audit()
    weight_checks = weighted_cancellation_audit()
    boundary_audit()

    print("Stage14-X12 lost-core fourth-root audit: PASS")
    print(f"lost-core fourth-root integer checks: {lost_checks}")
    print(f"column-transfer divisibility checks: {column_checks}")
    print(f"balanced rational mesh points checked: {mesh_points}")
    print(f"weighted cancellation checks: {weight_checks}")
    print(f"saturation points: {sat}")
    print("entering exponent: 19/34")
    print("current whole-family exponent: 71/128")
    print("improvement over 19/34: 9/2176")
    print("gap to sqrt scale: 7/128")
    print("equality: theta=71/256 phi=1/4 chi=39/128 j=27/128")
    print("column: raw=5/128 forced=3/128 effective=1/64; row CRT=5/128")
    print("invalid J*H shortcut used: false")
    print("X12 auxiliary H needed: false")


if __name__ == "__main__":
    main()
