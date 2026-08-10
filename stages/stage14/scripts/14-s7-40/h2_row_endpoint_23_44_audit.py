#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def oddpart(n: int) -> int:
    while n % 2 == 0 and n:
        n //= 2
    return n


def check_h_square_divides_n() -> int:
    checks = 0
    for a in range(1, 13):
        for b in range(1, 13):
            for c in range(1, 45):
                for d in range(1, 45):
                    H = oddpart(gcd(c, d))
                    N = a * b * c * d
                    assert N % (H * H) == 0, (a, b, c, d, H, N)
                    checks += 1
    return checks


def check_combined_crt_spacing() -> int:
    checks = 0
    for J in range(1, 35, 2):
        for H in range(1, 24, 2):
            if gcd(J, H) != 1:
                continue
            mod = J * H * H
            for r in range(J):
                vals = [n for n in range(0, 6 * mod + 1) if n % J == r and n % (H * H) == 0]
                for x, y in zip(vals, vals[1:]):
                    assert (y - x) % mod == 0
                    assert y - x == mod
                    checks += 1
    return checks


def strip_ok(theta: F, phi: F) -> bool:
    return (
        F(3, 16) <= theta <= F(5, 16)
        and F(1, 8) <= phi <= F(1, 4)
        and F(0) <= theta - phi <= F(1, 8)
        and theta + phi >= F(3, 8)
    )


def block_at_s0(theta: F, phi: F):
    chi = 2 * theta + 2 * phi - F(3, 4)
    Es = max(2 * theta, 1 - 2 * theta)
    Ek = 3 * theta - F(1, 4)
    ERC = 2 * phi + F(1, 2) - 2 * chi
    EH0 = 3 * phi - F(1, 8)
    return chi, Es, Ek, ERC, EH0, min(Es, Ek, ERC, EH0)


def check_whole_strip() -> int:
    # 1408 is divisible by 88, so the asserted equality point lies exactly on the mesh.
    D = 1408
    best = F(-10)
    eq = []
    points = 0
    for it in range(int(F(3, 16) * D), int(F(5, 16) * D) + 1):
        theta = F(it, D)
        for ip in range(int(F(1, 8) * D), int(F(1, 4) * D) + 1):
            phi = F(ip, D)
            if not strip_ok(theta, phi):
                continue
            chi, Es, Ek, ERC, EH0, val = block_at_s0(theta, phi)
            # merged 4cx: fixed-power nonproportional high-core blocks are empty
            if chi > F(1, 4):
                continue
            points += 1
            if val > best:
                best = val
                eq = [(theta, phi, chi, Es, Ek, ERC, EH0)]
            elif val == best:
                eq.append((theta, phi, chi, Es, Ek, ERC, EH0))
    assert best == F(23, 44), (best, eq[:10])
    assert len(eq) == 1, eq
    theta, phi, chi, Es, Ek, ERC, EH0 = eq[0]
    assert theta == F(23, 88)
    assert phi == F(19, 88)
    assert chi == F(9, 44)
    assert Es == ERC == EH0 == F(23, 44)
    assert Ek == F(47, 88)
    return points


def check_endpoint_ledger() -> None:
    theta = F(23, 88)
    phi = F(19, 88)
    chi = F(9, 44)
    s = F(0)
    j = chi
    col = F(1, 4) - chi
    row = F(1, 4) - j - 2 * s
    mu = 2 * theta - 2 * phi
    nu = F(1, 4) + 2 * phi - 2 * theta
    assert col == row == F(1, 22)
    assert mu == F(1, 11)
    assert nu == F(7, 44)
    assert mu == col + row
    assert chi + mu + (2 * phi - chi) == F(23, 44)
    assert F(23, 44) - F(1, 2) == F(1, 44)


def check_predecessors() -> None:
    cx = (ROOT / 'stages/stage14/14-4cx/result.md').read_text()
    cs = (ROOT / 'stages/stage14/14-4cs/result.md').read_text()
    s39 = (ROOT / 'stages/stage14/14-s7-39/result.md').read_text()
    assert 'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44' in cx
    assert 'CAYLEY_ONLY_ANNULUS_FIXED_POWER_EMPTY=true' in cx
    assert 'FULL_LOST_CORE_DIVIDES_COLUMN_COFACTOR_PRODUCT=true' in cx
    assert 'gcd(J,H)=1' in cx
    assert 'oddpart(gcd(c,d))' in cs
    assert 'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=17/32' in s39


def check_boundary() -> None:
    out = (ROOT / 'stages/stage14/14-s7-40/result.md').read_text()
    tokens = [
        'STAGE14_S7_40=COMPLETE_CROSS_ROOT_SQUARE_ROW_MODULUS_AND_23_44_ENDPOINT_COLLAPSE',
        'MERGED_4CX_23_44_IMPORTED=true',
        'COMMON_CROSS_ROOT_SQUARE_DIVIDES_ROW_PRODUCT=true',
        'ROW_SPACING_MODULUS_EQUALS_J_TIMES_H2=true',
        'ROW_LIFT_TWO_S_SAVING_PROVED=true',
        'CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=23/44',
        'NEW_WHOLE_FAMILY_POWER_SAVING_PROVED=false',
        'OLD_23_44_SATURATION_SEGMENT_COLLAPSED=true',
        'TWENTYTHREE_44_SATURATION_POINT_UNIQUE=true',
        'TWENTYTHREE_44_SATURATION_THETA=23/88',
        'TWENTYTHREE_44_SATURATION_PHI=19/88',
        'TWENTYTHREE_44_SATURATION_CROSS_ROOT_EXPONENT=0',
        'TWENTYTHREE_44_COLUMN_SHORT_EXPONENT=1/22',
        'TWENTYTHREE_44_ROW_SHORT_EXPONENT=1/22',
        'TWENTYTHREE_44_U_RESIDUAL_CAP_EXPONENT=1/11',
        'S7_40_AUXILIARY_H_NEEDED=false',
        'NEXT=Stage14-s7-41',
    ]
    for token in tokens:
        assert token in out, token


def main() -> None:
    h_checks = check_h_square_divides_n()
    crt_checks = check_combined_crt_spacing()
    mesh_points = check_whole_strip()
    check_endpoint_ledger()
    check_predecessors()
    check_boundary()
    print('Stage14-s7-40 H-square row endpoint audit: PASS')
    print('H^2|N checks:', h_checks)
    print('combined CRT spacing checks:', crt_checks)
    print('balanced low-core mesh points:', mesh_points)
    print('current whole-family exponent: 23/44')
    print('new whole-family saving: false')
    print('unique equality: theta=23/88 phi=19/88 s=0 chi=j=9/44')
    print('endpoint short ledger: column=1/22 row=1/22 u_res=1/11')
    print('gap to sqrt: 1/44')


if __name__ == '__main__':
    main()
