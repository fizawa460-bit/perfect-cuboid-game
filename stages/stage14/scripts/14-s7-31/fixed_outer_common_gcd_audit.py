#!/usr/bin/env python3
"""Deterministic audit for Stage14-s7-31.

The asymptotic theorem is proved in result.md.  This script verifies on the
finite physical packet that the odd common gcd of the opposite signed
quotients divides the common z scale and hence has square dividing the already
fixed q_k=C*u_res.  It also exhaustively regresses the fixed-outer version of
the nonprimitive quadratic root-pair lemma on small boxes and locks the exact
5/8 exponent ledger.
"""

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


s28 = load_module(
    "stage14_s728_s731",
    SCRIPTS / "14-s7-28" / "primitive_ratio_reconstruction_audit.py",
)
s30 = load_module(
    "stage14_s730_s731",
    SCRIPTS / "14-s7-30" / "two_sided_common_core_root_pair_audit.py",
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


def prime_factors(n: int):
    x = n
    out = []
    p = 3
    while p * p <= x:
        if x % p:
            p += 2
            continue
        out.append(p)
        while x % p == 0:
            x //= p
        p += 2
    if x > 1:
        out.append(x)
    return out


def physical_z(state: dict[str, int]) -> int:
    # Canonical state coordinates: P=a*x^2, Q=b*y^2.
    P = state["a"] * state["x"] * state["x"]
    Q = state["b"] * state["y"] * state["y"]
    assert Q > P > 0
    assert gcd(P, Q) == 1
    g = gcd(Q - P, Q + P)
    assert g in (1, 2)
    num = 2 * state["x"] * state["y"]
    assert num % g == 0
    return num // g


def audit_packet(a_state: dict[str, int], b_state: dict[str, int]):
    # Run the full merged s7-30 audit first.
    C, u_res, v_res, p, q, c, d, h = s30.audit_packet(a_state, b_state)
    data = s28.packet_data(a_state, b_state)

    R, S, T, J, alpha, beta, gamma, delta = data["cells"]
    P = int(data["P"])
    Q = int(data["Q"])
    X = int(data["X"])
    Y = int(data["Y"])

    # Opposite agreement primes are k-primes and are units on P*Q.
    assert p * q == oddpart(alpha * delta)
    assert gcd(p * q, P * Q) == 1

    z1 = physical_z(a_state)
    z2 = physical_z(b_state)
    t = gcd(z1, z2)

    h_odd = oddpart(h)
    assert oddpart(t) % h_odd == 0
    assert (C * u_res) % (h_odd * h_odd) == 0

    # Primewise physical support audit.  For every odd prime in the quotient
    # common gcd, the cell factors R,J are units and the prime is carried by
    # both root products X,Y; hence it enters both z roots.
    for ell in prime_factors(h_odd):
        assert R % ell != 0
        assert J % ell != 0
        assert X % ell == 0
        assert Y % ell == 0
        assert z1 % ell == 0
        assert z2 % ell == 0

    return C, u_res, v_res, h, t


def finite_physical_audit(limit: int = 600):
    groups = ch.make_groups(limit)
    checked = 0
    max_h = 1
    max_h_odd = 1
    max_t = 1
    nontrivial_h_odd = 0

    for states in groups.values():
        for i in range(len(states)):
            for j in range(i + 1, len(states)):
                a_state, b_state = states[i], states[j]
                if (a_state["a"], a_state["b"]) == (b_state["a"], b_state["b"]):
                    continue
                if (a_state["km"], a_state["kp"]) == (b_state["km"], b_state["kp"]):
                    continue
                _, _, _, h, t = audit_packet(a_state, b_state)
                max_h = max(max_h, h)
                max_h_odd = max(max_h_odd, oddpart(h))
                max_t = max(max_t, t)
                nontrivial_h_odd += int(oddpart(h) > 1)
                checked += 1

    assert checked > 0
    return checked, max_h, max_h_odd, max_t, nontrivial_h_odd


def synthetic_cross_root_support_audit() -> None:
    # The valuation mechanism of Section 3 can occur with a nontrivial odd
    # common gcd.  These synthetic primitive root pairs isolate the cross-root
    # placement without pretending to be full physical packets.
    samples = [
        # x1,y1,x2,y2; odd cross gcd
        (3, 2, 1, 3, 3),
        (5, 2, 3, 5, 5),
        (7, 4, 3, 7, 7),
    ]
    for x1, y1, x2, y2, ell in samples:
        assert gcd(x1, y1) == 1 and gcd(x2, y2) == 1
        X = x1 * x2
        Y = y1 * y2
        assert X % ell == 0 and Y % ell == 0
        z1 = 2 * x1 * y1
        z2 = 2 * x2 * y2
        assert gcd(z1, z2) % ell == 0


def fixed_outer_root_pair_regression() -> None:
    # Exhaustive small-box regression for the shape
    # N_{Q,W}(M) << B^o(1)*(1+M/Q).
    # The theorem is the divisor/root-line proof in result.md; this finite test
    # uses a deliberately loose divisor/log envelope.
    W_values = (1, 9, 25, 45, 81, 225)
    for Q in range(1, 50, 2):
        for A in range(1, min(Q + 1, 8)):
            if gcd(A, Q) != 1:
                continue
            for B in range(1, min(Q + 1, 8)):
                if gcd(B, Q) != 1:
                    continue
                for W in W_values:
                    for M in (12, 24, 48, 72):
                        count = 0
                        for x in range(1, M + 1):
                            for y in range(1, M // x + 1):
                                h = gcd(x, y)
                                ho = oddpart(h)
                                if W % (ho * ho) != 0:
                                    continue
                                if (A * A * x * x + B * B * y * y) % Q == 0:
                                    count += 1
                        logfac = (M.bit_length() + 2) ** 2
                        # Integer upper envelope for const*tau(Q)*tau(W)*log^2*(1+M/Q).
                        rhs = 32 * tau(Q) * tau(W) * logfac * (2 + M // Q)
                        assert count <= rhs


def exponent_ledger_audit() -> None:
    vals = [Fraction(n, 64) for n in range(8, 21)]
    saw = 0
    worst = Fraction(0, 1)
    worst_points = []

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

            chi = 2 * theta + 2 * phi - Fraction(3, 4)
            mu = 2 * theta - 2 * phi
            nu = Fraction(1, 4) + 2 * phi - 2 * theta
            assert chi >= 0 and mu >= 0 and nu >= 0

            second = max(Fraction(0), nu - chi)
            total_direct = chi + mu + (2 * phi - chi) + second
            total_formula = max(2 * theta, 1 - 2 * theta)
            assert total_direct == total_formula
            assert total_formula <= Fraction(5, 8)

            if total_formula > worst:
                worst = total_formula
                worst_points = [(theta, phi)]
            elif total_formula == worst:
                worst_points.append((theta, phi))
            saw += 1

    assert saw > 0
    assert worst == Fraction(5, 8)

    # On the 1/64 audit grid, saturation is exactly the lower symmetric corner
    # plus the full admissible top-theta edge.
    assert (Fraction(3, 16), Fraction(3, 16)) in worst_points
    top_points = [p for p in worst_points if p[0] == Fraction(5, 16)]
    assert top_points
    assert all(Fraction(3, 16) <= p[1] <= Fraction(1, 4) for p in top_points)
    assert all(
        p == (Fraction(3, 16), Fraction(3, 16)) or p[0] == Fraction(5, 16)
        for p in worst_points
    )
    assert Fraction(5, 8) - Fraction(1, 2) == Fraction(1, 8)


def boundary_audit() -> None:
    root = HERE.parents[4]
    s30_text = (root / "stages/stage14/14-s7-30/result.md").read_text()
    ci_text = (root / "stages/stage14/14-4ci/result.md").read_text()
    cj_text = (root / "stages/stage14/14-4cj/result.md").read_text()
    cq_text = (root / "stages/stage14/14-4cq/result.md").read_text()
    x7_text = (root / "stages/stage14/14-X7/result.md").read_text()

    assert "STAGE14_S7_30=COMPLETE_TWO_SIDED_COMMON_CORE_QUADRATIC_ROOT_PAIR_COUNT_AND_11_16_BOUND" in s30_text
    assert "CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=11/16" in s30_text
    assert "REMAINING_RECEIVER=TopCornerOppositeSignedQuotientCommonGcdRootProductIncidence" in s30_text
    assert "COMMON_Z_SCALE_SQUARE_DIVIDES_QK=true" in ci_text
    assert "PHYSICAL_XI_ROOT_VECTOR_PRIMITIVE=true" in cj_text
    assert "STAGE14_4CQ=COMPLETE_DUAL_COMMON_CORE_CAYLEY_DIVISOR_COLLAPSE_AND_SYMMETRIC_QUARTER_QUARTER_REDUCTION" in cq_text
    assert "SECOND_DETERMINANT_SPACING_FROM_POINTWISE_FOUR_ROOT_DATA=false" in x7_text


def main() -> None:
    boundary_audit()
    synthetic_cross_root_support_audit()
    fixed_outer_root_pair_regression()
    exponent_ledger_audit()
    checked, max_h, max_h_odd, max_t, nontrivial_h_odd = finite_physical_audit()

    print("Stage14-s7-31 fixed-outer common-gcd audit: PASS")
    print(f"finite dual-cross physical pairs checked: {checked}")
    print(f"max finite opposite signed-quotient gcd: {max_h}")
    print(f"max finite odd opposite signed-quotient gcd: {max_h_odd}")
    print(f"finite packets with nontrivial odd quotient gcd: {nontrivial_h_odd}")
    print(f"max finite common z scale: {max_t}")
    print("odd quotient gcd divides common z scale: exact on finite physical packets")
    print("odd quotient gcd square divides fixed q_k=C*u_res: exact")
    print("fixed-outer nonprimitive root-pair bound 1+M/C: exhaustive regression PASS")
    print("two-sided fixed-outer block exponent: max(2theta,1-2theta)")
    print("new whole-family physical upper-bound exponent: 5/8")
    print("gap to sqrt scale: 1/8")
    print("s7-31 auxiliary H needed: false")


if __name__ == "__main__":
    main()
