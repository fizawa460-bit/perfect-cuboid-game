#!/usr/bin/env python3
from fractions import Fraction as F
from math import gcd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]


def crt2(a, m, b, n):
    assert gcd(m, n) == 1
    inv = pow(m, -1, n)
    t = ((b - a) * inv) % n
    return (a + m * t) % (m * n)


def check_row_column_algebra():
    # Four pairwise-coprime prime-power cells.  This is a structural toy
    # regression for the exact row/column bookkeeping, not a physical sample.
    cells = (5, 13, 17, 29)
    for i in range(4):
        for j in range(i):
            assert gcd(cells[i], cells[j]) == 1
    jmm, jmp, jpm, jpp = cells
    J = jmm * jmp * jpm * jpp
    JCm = jmm * jmp
    JCp = jpm * jpp
    JLm = jmm * jpm
    JLp = jmp * jpp
    assert JCm * JCp == J and gcd(JCm, JCp) == 1
    assert JLm * JLp == J and gcd(JLm, JLp) == 1

    hm, hp = 3, 7
    Lm, Lp = JLm * hm, JLp * hp
    Az_num = Lp + Lm
    Bz_num = Lp - Lm
    assert Az_num % 2 == 0 and Bz_num % 2 == 0
    Az, Bz = Az_num // 2, Bz_num // 2
    assert Az - Bz == Lm
    assert Az + Bz == Lp
    assert abs(Lm * Lp) // J == hm * hp

    # Row CRT: N=M on C- and N=-M on C+.
    M = 1234567
    n0 = crt2(M % JCm, JCm, (-M) % JCp, JCp)
    assert (n0 - M) % JCm == 0
    assert (n0 + M) % JCp == 0
    for hN in (-3, -1, 0, 2, 5):
        N = n0 + J * hN
        assert (N - M) % JCm == 0
        assert (N + M) % JCp == 0


def strip_ok(theta, phi):
    return (
        F(3,16) <= theta <= F(5,16)
        and F(1,8) <= phi <= F(1,4)
        and F(0) <= theta - phi <= F(1,8)
        and theta + phi >= F(3,8)
    )


def bounds(theta, phi, rho):
    chi = 2*theta + 2*phi - F(3,4)
    Es = max(2*theta, 1-2*theta)
    Ek = 3*theta - F(1,4)
    Ex = 3*phi - F(1,8) - rho
    Erc = 2*phi + F(1,2) - 2*chi + 6*rho
    return chi, Es, Ek, Ex, Erc, min(Es, Ek, Ex, Erc)


def check_symbolic_ledger():
    # Weighted minimum removes rho exactly.
    theta, phi, rho = F(7,24), F(1,4), F(1,24)
    chi, Es, Ek, Ex, Erc, E = bounds(theta, phi, rho)
    assert chi == F(1,3)
    assert Es == F(7,12)
    assert Ek == F(5,8)
    assert Ex == F(7,12)
    assert Erc == F(7,12)
    assert E == F(7,12)
    j = chi - 3*rho
    assert j == F(5,24)
    assert F(1,4) - j == F(1,24)
    assert F(19,32) - F(7,12) == F(1,96)
    assert F(9,16) < F(7,12)

    # Identity behind (6.3).
    weighted = (6*Ex + Erc) / 7
    closed = (16*phi - 4*theta + F(5,4)) / 7
    assert weighted == closed == F(7,12)


def check_fraction_grid():
    # Exact rational regression over the whole balanced strip.  rho is sampled
    # at 1/1536, which contains the equality value 1/24 exactly.
    target = F(7,12)
    max_seen = F(-1)
    equality = set()
    for it in range(144, 241):
        theta = F(it, 768)
        for ip in range(96, 193):
            phi = F(ip, 768)
            if not strip_ok(theta, phi):
                continue
            chi = 2*theta + 2*phi - F(3,4)
            # Nonproportional J|L-L+ condition from 4cu.
            r0 = max(F(0), (chi - F(1,4))/3)
            # residual norm permits only polynomially bounded rho; 1/4 is
            # more than enough for this regression.
            local = F(-1)
            local_rhos = []
            for ir in range(0, 385):
                rho = F(ir, 1536)
                if rho < r0:
                    continue
                _, Es, Ek, Ex, Erc, E = bounds(theta, phi, rho)
                if E > local:
                    local = E
                    local_rhos = [rho]
                elif E == local:
                    local_rhos.append(rho)
            if local > max_seen:
                max_seen = local
                equality = {(theta, phi, r) for r in local_rhos}
            elif local == max_seen:
                equality |= {(theta, phi, r) for r in local_rhos}
    assert max_seen == target, (max_seen, equality)
    assert equality == {(F(7,24), F(1,4), F(1,24))}, equality


def check_predecessor_locks():
    cu = (ROOT / "stages/stage14/14-4cu/result.md").read_text()
    s33 = (ROOT / "stages/stage14/14-s7-33/result.md").read_text()
    s27 = (ROOT / "stages/stage14/14-s7-27/result.md").read_text()
    required_cu = [
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=19/32",
        "JOINT_CORE_DIVIDES_ENDPOINT_LINEAR_PRODUCT=true",
        "THREE_GAUSSIAN_ROOT_ORIENTATION_ENTROPY_RANK=2",
        "PROPORTIONAL_BRANCH_UPPER_BOUND_EXPONENT=9/16",
    ]
    for token in required_cu:
        assert token in cu, token
    required_s33 = [
        "COMMON_CORE_ORIENTATION_DOUBLE_CHARGE_FORBIDDEN=true",
        "STRONG_CANONICAL_ST_SPLIT_UNIVERSALLY_VALID=false",
        "COMMON_CORE_CANCELLED_GAUSSIAN_TRANSFER_IDENTITY_PROVED=true",
    ]
    for token in required_s33:
        assert token in s33, token
    assert "oddpart(c_x^- c_x^+) = oddpart(u_res)" in s27
    assert "oddpart(c_k^- c_k^+) = oddpart(v_res)" in s27


def check_current_boundary():
    result = (ROOT / "stages/stage14/14-4cv/result.md").read_text()
    tokens = [
        "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12",
        "IMPROVEMENT_OVER_PREVIOUS_19_32=1/96",
        "SEVEN_TWELFTHS_SATURATION_THETA=7/24",
        "SEVEN_TWELFTHS_SATURATION_PHI=1/4",
        "SEVEN_TWELFTHS_SATURATION_JOINT_CORE_EXPONENT=5/24",
        "STRONG_CANONICAL_ST_SPLIT_USED=false",
        "COMMON_CORE_ORIENTATION_DOUBLE_CHARGED=false",
        "MAINLINE_H_NEEDED=false",
        "NEXT=Stage14-4cw",
    ]
    for token in tokens:
        assert token in result, token


def main():
    check_row_column_algebra()
    check_symbolic_ledger()
    check_fraction_grid()
    check_predecessor_locks()
    check_current_boundary()
    print("Stage14-4cv audit: OK")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/12")
    print("UNIQUE_GRID_SATURATION=theta=7/24,phi=1/4,rho=1/24")


if __name__ == "__main__":
    main()
