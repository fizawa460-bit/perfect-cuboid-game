#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-32.

The asymptotic proof is in result.md.  This script checks the exact one-host
Gaussian identities and reconstruction formulas on the finite physical packet,
regresses the short-root uniqueness mechanism, and verifies the three-way
minimax ledger that leaves only (theta,phi)=(5/16,1/4) at exponent 5/8.
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


s28 = load_module(
    "stage14_s728_s732",
    SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py",
)
s31 = load_module(
    "stage14_s731_s732",
    SCRIPTS / "14-s7-31" / "fixed_outer_common_gcd_audit.py",
)
g4cf = load_module(
    "stage14_4cf_s732",
    SCRIPTS / "14-4" / "gaussian_square_divisor_descent_audit.py",
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
    return n >> v2(n)


def gnorm(z: tuple[int, int]) -> int:
    return z[0] * z[0] + z[1] * z[1]


def gaussian_descent_allow_one(A: int, B: int, cell: int):
    c = oddpart(cell)
    z = (A, B)
    if c == 1:
        return (1, 0), z
    return g4cf.gaussian_square_divisor(A, B, c)


def state_pq(state: dict[str, int]) -> tuple[int, int, int]:
    P = state["a"] * state["x"] * state["x"]
    Q = state["b"] * state["y"] * state["y"]
    assert Q > P > 0
    assert gcd(P, Q) == 1
    g = gcd(Q - P, Q + P)
    assert g in (1, 2)
    return P, Q, g


def reconstruct_from_k_cells(
    alpha: int,
    beta: int,
    gamma: int,
    delta: int,
    a_state: dict[str, int],
    b_state: dict[str, int],
):
    out = []
    for idx, state in enumerate((a_state, b_state)):
        P0, Q0, g = state_pq(state)
        r = state["r"]
        s = state["s"]
        if idx == 0:
            km = alpha * beta
            kp = gamma * delta
        else:
            km = alpha * gamma
            kp = beta * delta
        u = km * r * r
        v = kp * s * s
        assert g * (v - u) % 2 == 0
        assert g * (v + u) % 2 == 0
        P = g * (v - u) // 2
        Q = g * (v + u) // 2
        assert (P, Q) == (P0, Q0)
        out.append((P, Q))
    return out


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    # Full predecessor check first.
    s31.audit_packet(a_state, b_state)
    d = s28.packet_data(a_state, b_state)

    R, S, T, J, alpha, beta, gamma, delta = d["cells"]
    C, u_res, v_res = d["triple"]
    qk = C * u_res
    qxi = C * v_res

    P1, Q1, g1 = state_pq(a_state)
    P2, Q2, g2 = state_pq(b_state)

    z1 = s31.physical_z(a_state)
    z2 = s31.physical_z(b_state)
    omega1 = g1 * a_state["r"] * a_state["s"]
    omega2 = g2 * b_state["r"] * b_state["s"]

    # Exact four positive Gaussian host identities.
    Zb = (
        alpha * b_state["r"] ** 2 * z1,
        delta * a_state["s"] ** 2 * z2,
    )
    Zg = (
        delta * b_state["s"] ** 2 * z1,
        alpha * a_state["r"] ** 2 * z2,
    )
    ZS = (
        R * b_state["x"] ** 2 * omega1,
        J * a_state["y"] ** 2 * omega2,
    )
    ZT = (
        J * b_state["y"] ** 2 * omega1,
        R * a_state["x"] ** 2 * omega2,
    )

    assert gnorm(Zb) == beta * beta * qk
    assert gnorm(Zg) == gamma * gamma * qk
    assert gnorm(ZS) == S * S * qxi
    assert gnorm(ZT) == T * T * qxi

    # One-host Gaussian descents, including the possible squarefree factor 2.
    lam_b, Wb = gaussian_descent_allow_one(Zb[0], Zb[1], beta)
    lam_S, WS = gaussian_descent_allow_one(ZS[0], ZS[1], S)
    assert gnorm(lam_b) == oddpart(beta)
    assert gnorm(lam_S) == oddpart(S)
    assert gnorm(Wb) == qk * (beta // oddpart(beta)) ** 2
    assert gnorm(WS) == qxi * (S // oddpart(S)) ** 2

    # k-host reconstruction: once alpha,delta,z1,z2 are read from the fixed
    # coordinates, the equal residual norm makes gamma unique.
    gamma_sq_num = gnorm(Zg)
    assert gamma_sq_num % qk == 0
    gamma_sq = gamma_sq_num // qk
    assert isqrt(gamma_sq) ** 2 == gamma_sq
    assert isqrt(gamma_sq) == gamma
    reconstruct_from_k_cells(alpha, beta, gamma, delta, a_state, b_state)

    # xi-host reconstruction: after the agreement orientations select x1,y2,
    # equality of the k labels is linear in T^2.
    lhs_coeff = omega2 * omega2 * J * J * a_state["y"] ** 4 + \
        omega1 * omega1 * R * R * b_state["x"] ** 4
    rhs_core = omega1 * omega1 * J * J * b_state["y"] ** 4 + \
        omega2 * omega2 * R * R * a_state["x"] ** 4
    numerator = S * S * rhs_core
    assert numerator % lhs_coeff == 0
    T_sq = numerator // lhs_coeff
    assert isqrt(T_sq) ** 2 == T_sq
    assert isqrt(T_sq) == T

    # Direct physical values from the reconstructed xi cells/roots.
    assert R * S * a_state["x"] ** 2 == P1
    assert T * J * a_state["y"] ** 2 == Q1
    assert R * T * b_state["x"] ** 2 == P2
    assert S * J * b_state["y"] ** 2 == Q2

    return qk, qxi, beta, S


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    max_qk = max_qxi = 1
    max_beta = max_S = 1

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                qk, qxi, beta, S = audit_packet(a_state, b_state)
                max_qk = max(max_qk, qk)
                max_qxi = max(max_qxi, qxi)
                max_beta = max(max_beta, beta)
                max_S = max(max_S, S)
                checked += 1

    assert checked > 0
    return checked, max_qk, max_qxi, max_beta, max_S


def short_root_uniqueness_regression() -> None:
    # If the root interval length is strictly smaller than the modulus, one
    # residue class contains at most one positive root.  This is the exact
    # mechanism used after fixing an agreement-cell orientation.
    for modulus in range(5, 80):
        for bound in range(1, modulus):
            for residue in range(modulus):
                hits = [x for x in range(1, bound + 1) if x % modulus == residue]
                assert len(hits) <= 1


def exponent_ledger_audit() -> None:
    vals = [Fraction(n, 64) for n in range(8, 21)]
    worst = Fraction(-1, 1)
    worst_points = []
    saw = 0

    for theta in vals:
        if not (Fraction(3, 16) <= theta <= Fraction(5, 16)):
            continue
        for phi in vals:
            if not (Fraction(1, 8) <= phi <= Fraction(1, 4)):
                continue
            if theta < phi:
                continue
            if theta - phi > Fraction(1, 8):
                continue
            if theta + phi < Fraction(3, 8):
                continue

            e_s = max(2 * theta, 1 - 2 * theta)
            e_k = 3 * theta - Fraction(1, 4)
            e_xi = 3 * phi - Fraction(1, 8)
            e = min(e_s, e_k, e_xi)

            assert e <= Fraction(5, 8)
            if theta <= Fraction(1, 4):
                assert e_k <= Fraction(1, 2)
                assert e <= Fraction(1, 2)
            if phi < Fraction(1, 4):
                assert e_xi < Fraction(5, 8)

            if e > worst:
                worst = e
                worst_points = [(theta, phi)]
            elif e == worst:
                worst_points.append((theta, phi))
            saw += 1

    assert saw > 0
    assert worst == Fraction(5, 8)
    assert worst_points == [(Fraction(5, 16), Fraction(1, 4))]

    # Exact top-corner scales.
    theta = Fraction(5, 16)
    phi = Fraction(1, 4)
    assert 4 * theta - Fraction(3, 4) == Fraction(1, 2)
    assert 4 * phi - Fraction(1, 2) == Fraction(1, 2)
    assert Fraction(3, 8) - phi == Fraction(1, 8)
    assert 3 * phi - Fraction(1, 8) == Fraction(5, 8)


def boundary_audit() -> None:
    root = HERE.parents[4]
    s31_text = (root / "stages/stage14/14-s7-31/result.md").read_text()
    cf_text = (root / "stages/stage14/14-4cf/result.md").read_text()
    cg_text = (root / "stages/stage14/14-4cg/result.md").read_text()
    cj_text = (root / "stages/stage14/14-4cj/result.md").read_text()
    cr_text = (root / "stages/stage14/14-4cr/result.md").read_text()
    x8_text = (root / "stages/stage14/14-X8/result.md").read_text()
    t70_text = (root / "stages/stage14/14-t70/result.md").read_text()

    assert "STAGE14_S7_31=COMPLETE_FIXED_OUTER_COMMON_GCD_SQUARE_DIVISIBILITY_AND_5_8_BOUND" in s31_text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=5/8" in s31_text
    assert "COMPLETE_BALANCED_EIGHT_CELL_GAUSSIAN_SQUARE_DIVISOR_DESCENT" in cf_text
    assert "K_HOST_RESIDUAL_NORMS_EQUAL=true" in cg_text
    assert "XI_HOST_RESIDUAL_NORMS_EQUAL=true" in cg_text
    assert "XI_PHYSICAL_SHORT_SPAN_RANK=1" in cj_text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=2/3" in cr_text
    assert "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT=2/3" in x8_text
    assert "COMMON_SUPPORT_ROOT_LINE_MULTIPLICITY=Bo1" in t70_text


def main() -> None:
    boundary_audit()
    short_root_uniqueness_regression()
    exponent_ledger_audit()
    checked, max_qk, max_qxi, max_beta, max_S = finite_physical_audit()

    print("Stage14-s7-32 one-host Gaussian boundary audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"max finite q_k: {max_qk}")
    print(f"max finite q_xi: {max_qxi}")
    print(f"max finite beta switched cell: {max_beta}")
    print(f"max finite S switched cell: {max_S}")
    print("one k-switched Gaussian host physical reconstruction: exact")
    print("one xi-switched Gaussian host + agreement orientation reconstruction: exact")
    print("k one-host block exponent: 3theta-1/4")
    print("xi one-host block exponent: 3phi-1/8")
    print("combined 5/8 saturation: unique at theta=5/16, phi=1/4")
    print("whole-family physical upper-bound exponent remains: 5/8")
    print("s7-32 auxiliary H needed: false")


if __name__ == "__main__":
    main()
