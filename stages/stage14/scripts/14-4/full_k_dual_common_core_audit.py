#!/usr/bin/env python3
"""Deterministic regression audit for Stage14-4ci.

The finite search verifies the exact primitive-k-line saturation, the two
common-scale square divisibilities, and the normalized four-host equations.
It is regression evidence; the proofs are in stages/stage14/14-4ci/result.md.
"""

from collections import defaultdict
from fractions import Fraction
from importlib.util import module_from_spec, spec_from_file_location
from math import gcd
from pathlib import Path

HERE = Path(__file__).resolve()
CH_AUDIT = HERE.parent / "eight_cell_residual_lift_audit.py"
spec = spec_from_file_location("stage14_4ch_audit", CH_AUDIT)
assert spec is not None and spec.loader is not None
ch = module_from_spec(spec)
spec.loader.exec_module(ch)
s7 = ch.s7


def v2(n: int) -> int:
    e = 0
    while n and n % 2 == 0:
        n //= 2
        e += 1
    return e


def audit_pair(a: dict[str, int], b: dict[str, int]) -> None:
    cells, triple, qs, _ = ch.residual_data(a, b)
    R, S, T, J, alpha, beta, gamma, delta = cells
    C, u_res, v_res = triple
    q_k, q_xi = qs
    assert q_k == C * u_res
    assert q_xi == C * v_res

    # Primitive z direction and full k-lattice saturation.
    t = gcd(a["z"], b["z"])
    az = a["z"] // t
    bz = b["z"] // t
    assert gcd(az, bz) == 1
    assert gcd(t, a["k"]) == 1
    assert gcd(bz, a["k"]) == 1

    modulus = a["k"] ** 2
    mu = (a["z"] * pow(b["z"], -1, modulus)) % modulus
    assert (az - mu * bz) % modulus == 0

    # For Lambda={x=mu*y mod k^2}, the primitive normal n=(bz,-az)
    # has image gcd(k^2, az-mu*bz) Z.  Full divisibility gives d_k=k^2.
    d_k = gcd(modulus, az - mu * bz)
    assert d_k == modulus
    assert modulus // d_k == 1

    # Every cell-square orientation is already fixed by the primitive ratio.
    for cell in (alpha, beta, gamma, delta):
        m = cell * cell
        if m == 1:
            continue
        assert gcd(bz, m) == 1
        mu_cell = az * pow(bz, -1, m) % m
        assert (az - mu_cell * bz) % m == 0

    # Common z scale is a square divisor of q_k.
    assert q_k % (t * t) == 0
    Qk = q_k // (t * t)

    assert beta * beta * Qk == (
        alpha * alpha * b["r"] ** 4 * az * az
        + delta * delta * a["s"] ** 4 * bz * bz
    )
    assert gamma * gamma * Qk == (
        delta * delta * b["s"] ** 4 * az * az
        + alpha * alpha * a["r"] ** 4 * bz * bz
    )

    # Symmetric omega normalization.
    h = gcd(a["omega"], b["omega"])
    ao = a["omega"] // h
    bo = b["omega"] // h
    assert gcd(ao, bo) == 1
    assert gcd(h, a["xi"]) == 1
    assert q_xi % (h * h) == 0
    Qxi = q_xi // (h * h)

    assert S * S * Qxi == (
        R * R * b["x"] ** 4 * ao * ao
        + J * J * a["y"] ** 4 * bo * bo
    )
    assert T * T * Qxi == (
        J * J * b["y"] ** 4 * ao * ao
        + R * R * a["x"] ** 4 * bo * bo
    )


def audit_dyadic_ledger() -> None:
    # Feasible rational sample of the 4cg strip, including all boundary corners.
    samples = [
        (Fraction(1, 4), Fraction(1, 8)),
        (Fraction(7, 32), Fraction(5, 32)),
        (Fraction(3, 16), Fraction(3, 16)),
        (Fraction(5, 16), Fraction(1, 4)),
    ]
    for theta, phi in samples:
        assert Fraction(3, 16) <= theta <= Fraction(5, 16)
        assert Fraction(1, 8) <= phi <= Fraction(1, 4)
        assert theta >= phi
        assert theta - phi <= Fraction(1, 8)
        assert theta + phi >= Fraction(3, 8)

        c_exp = 2 * theta + 2 * phi - Fraction(3, 4)
        u_exp = 2 * theta - 2 * phi
        v_exp = Fraction(1, 4) + 2 * phi - 2 * theta
        assert c_exp >= 0
        assert u_exp >= 0
        assert v_exp >= 0
        assert u_exp + v_exp == Fraction(1, 4)
        support = c_exp + u_exp + v_exp
        assert support == 2 * (theta + phi) - Fraction(1, 2)
        assert Fraction(1, 4) <= support <= Fraction(5, 8)


def main() -> None:
    X = 420
    groups = ch.make_groups(X)
    checked = 0
    z_scale_hist: dict[int, int] = defaultdict(int)
    omega_scale_hist: dict[int, int] = defaultdict(int)

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a, b = states[i], states[j]
                if (a["a"], a["b"]) == (b["a"], b["b"]):
                    continue
                if (a["km"], a["kp"]) == (b["km"], b["kp"]):
                    continue
                audit_pair(a, b)
                z_scale_hist[gcd(a["z"], b["z"])] += 1
                omega_scale_hist[gcd(a["omega"], b["omega"])] += 1
                checked += 1

    assert checked > 0
    audit_dyadic_ledger()

    # Explicitly lock the logical X0 corollary source.
    result_4ch = (HERE.parents[2] / "14-4ch" / "result.md").read_text()
    result_x0 = (HERE.parents[2] / "14-X0" / "result.md").read_text()
    result_s722 = (HERE.parents[2] / "14-s7-22" / "result.md").read_text()
    assert "FIXED_EIGHT_CELLS_COMMON_CORE_RESIDUAL_PHYSICAL_LIFT_BO1=true" in result_4ch
    assert "JOINT_COMMON_CORE_CRT_PHYSICAL_FIBER_LEMMA_PROVED=false" in result_x0
    assert "STAGE14_S7_22=COMPLETE_RANK_THREE_DUAL_SATURATION_AND_TANGENT_RESONANCE_SPLIT" in result_s722

    print("Stage14-4ci audit: PASS")
    print(f"dual-cross finite pairs checked: {checked}")
    print("primitive z direction lies in Lambda_k: exact")
    print("k dual saturation order: k^2; defect: 1")
    print("gcd(z1,z2)^2 divides q_k: exact")
    print("gcd(omega1,omega2)^2 divides q_xi: exact")
    print("normalized four-host equations: exact")
    print("dyadic residual support exponent: 2*(theta+phi)-1/2")
    print(f"z-scale histogram: {dict(sorted(z_scale_hist.items()))}")
    print(f"omega-scale histogram: {dict(sorted(omega_scale_hist.items()))}")


if __name__ == "__main__":
    main()
