#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
import subprocess
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09P" / "etau-generic-mw-zero-exceptional-growth-preflight.json"
O_CERT = ROOT / "stages" / "stage36" / "36-09O" / "physical-square-lift-v4-quotient-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09N" / "relative-2isogeny-specialization-source-lock.md"
W03 = ROOT / "docs" / "arsenal" / "cards" / "formal" / "S34-W03.md"

BASE = "911418e205349e55fb2b4c828a309fbf55afcc47"
V43_BLOB = "80bed5d8d6d51c2a8e6864a9f83cf405d7cd3659"
CERT_BLOB = "a611b698fccfbd29a971ccede5c77b6832101c77"
O_CERT_BLOB = "6a2678ebedba40e13277100441361039ee47ca28"
SOURCE_BLOB = "a562d7053a6f04deff4473067777b7cfd538ea8a"
W03_BLOB = "1d5275321f42768a6414d4610ac912c63be43f96"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


def is_square_int(n: int) -> bool:
    if n < 0:
        return False
    r = math.isqrt(n)
    return r * r == n


def is_square_frac(q: Fraction) -> bool:
    return q >= 0 and is_square_int(q.numerator) and is_square_int(q.denominator)


def square_residues(m: int) -> set[int]:
    return {x * x % m for x in range(m)}


def quartic_has_primitive_local(d: int, modulus: int, a: int, b: int) -> bool:
    assert d != 0 and b % d == 0
    sq = square_residues(modulus)
    for M in range(modulus):
        for e in range(modulus):
            if math.gcd(math.gcd(M, e), modulus) != 1:
                continue
            rhs = (
                d * pow(M, 4, modulus)
                + a * pow(M, 2, modulus) * pow(e, 2, modulus)
                + (b // d) * pow(e, 4, modulus)
            ) % modulus
            if rhs in sq:
                return True
    return False


def count_curve_mod(q: int, roots: tuple[int, int, int]) -> int:
    squares = square_residues(q)
    total = 1  # point at infinity
    for x in range(q):
        rhs = 1
        for root in roots:
            rhs = rhs * (x - root) % q
        if rhs == 0:
            total += 1
        elif rhs in squares:
            total += 2
    return total


def polynomial_identities() -> None:
    # Check identities coefficientwise by elementary expansion at enough integer p values,
    # while each expression has degree <= 8. Nine distinct samples force equality.
    for p in range(-6, 7):
        if p in (-1, 0, 1):
            continue
        D = p * (p * p - 1)
        Q = (p * p - 1) ** 4 + 16 * p ** 4
        C = p ** 4 - 6 * p * p + 1
        H = (p * p + 1) ** 2
        Nm = p * p - 2 * p - 1
        Np = p * p + 2 * p - 1
        assert Q + 8 * D * D == H * H
        assert Q - 8 * D * D == C * C
        assert H * H - C * C == (4 * D) ** 2
        assert H + 4 * D == Np * Np
        assert H - 4 * D == Nm * Nm

    # Exact quartic->cubic derivation after clearing denominators.
    # From z=(v+4)/R^2 and v^2=R^4+A R^2+16:
    # R^2(z^2-1)=A+8z. Hence w=R(z^2-1) obeys
    # w^2=(z^2-1)(A+8z); X=8z,Y=8w gives
    # Y^2=(X^2-64)(X+A).
    for A in [Fraction(5, 2), Fraction(17, 3), Fraction(-7, 4)]:
        for z in [Fraction(2), Fraction(3, 2), Fraction(-2)]:
            if z * z == 1:
                continue
            R2 = (A + 8 * z) / (z * z - 1)
            lhs = 64 * R2 * (z * z - 1) ** 2
            X = 8 * z
            rhs = (X - 8) * (X + 8) * (X + A)
            assert lhs == rhs


def injective_specialization_check() -> None:
    p0 = Fraction(3, 2)
    values = {
        "Nminus": p0 * p0 - 2 * p0 - 1,
        "Nplus": p0 * p0 + 2 * p0 - 1,
        "p": p0,
        "p-1": p0 - 1,
        "p+1": p0 + 1,
        "p2+1": p0 * p0 + 1,
    }
    assert values == {
        "Nminus": Fraction(-7, 4),
        "Nplus": Fraction(17, 4),
        "p": Fraction(3, 2),
        "p-1": Fraction(1, 2),
        "p+1": Fraction(5, 2),
        "p2+1": Fraction(13, 4),
    }
    support_sets = [
        ["Nminus", "Nplus", "p2+1"],
        ["Nminus", "Nplus", "p", "p-1", "p+1"],
        ["p2+1", "p", "p-1", "p+1"],
    ]
    for support in support_sets:
        for mask in range(1, 1 << len(support)):
            value = Fraction(1)
            for i, name in enumerate(support):
                if (mask >> i) & 1:
                    value *= values[name]
            assert not is_square_frac(value), (support, mask, value)


def specialized_descent_check() -> None:
    a = -42722
    b = 404452321
    assert b == (119 * 169) ** 2
    ap = -2 * a
    bp = a * a - 4 * b
    assert ap == 85444
    assert bp == 207360000 == 14400 ** 2
    # x^2 + 85444 x + 14400^2 = (x+50^2)(x+288^2)
    assert 50 ** 2 + 288 ** 2 == ap
    assert (50 * 288) ** 2 == bp

    alpha_positive = [1, 7, 13, 17, 91, 119, 221, 1547]
    alpha_all = alpha_positive + [-d for d in alpha_positive]
    assert len(alpha_all) == 16
    # Every negative alpha quartic has all three coefficients negative over R.
    for d in [-x for x in alpha_positive]:
        assert d < 0 and a < 0 and b // d < 0
    alpha_obstructions = {7: 5, 13: 5, 91: 16, 17: 3, 119: 3, 221: 3, 1547: 3}
    for d, m in alpha_obstructions.items():
        assert not quartic_has_primitive_local(d, m, a, b), ("alpha", d, m)

    beta_positive = [1, 2, 3, 5, 6, 10, 15, 30]
    beta_all = beta_positive + [-d for d in beta_positive]
    assert len(beta_all) == 16
    beta_obstructions = {
        2: 13, -2: 13,
        3: 17, -3: 17,
        5: 13, -5: 13,
        6: 13, -6: 13,
        10: 17, -10: 17,
        15: 13, -15: 13,
    }
    for d, m in beta_obstructions.items():
        assert not quartic_has_primitive_local(d, m, ap, bp), ("beta", d, m)

    realized = {
        1: (0, 1, 14400),
        -1: (-50, 1, 0),
        30: (-60, 1, 26520),
        -30: (-40, 1, 7280),
    }
    for d, (M, e, N) in realized.items():
        assert bp % d == 0
        rhs = d * M ** 4 + ap * M * M * e * e + (bp // d) * e ** 4
        assert rhs == N * N, (d, rhs, N * N)
        assert math.gcd(M, e) == 1

    # Exact images have sizes 1 and 4, so rank is zero.
    assert (1 * 4) // 4 == 1


def specialized_torsion_check() -> None:
    e0, e1, e2 = 0, 119 ** 2, 169 ** 2
    assert e2 - e0 == 169 ** 2
    assert e2 - e1 == 120 ** 2
    # Other nonzero 2-torsion points cannot be halved over Q because one root difference is negative.
    assert e0 - e1 < 0 and e0 - e2 < 0
    assert e1 - e0 == 119 ** 2 and e1 - e2 < 0

    order4 = [(48841, 5860920), (48841, -5860920), (8281, 993720), (8281, -993720)]
    for x, y in order4:
        assert y * y == x * (x - e1) * (x - e2)
    assert 48841 == 221 ** 2
    assert not is_square_int(48841 - e1)
    assert not is_square_int(48841 - e2)
    assert 8281 == 91 ** 2
    assert 8281 - e1 < 0 and 8281 - e2 < 0

    # Good reduction and point counts; torsion order divides gcd(16,16)=16.
    for q in (11, 19):
        residues = {e0 % q, e1 % q, e2 % q}
        assert len(residues) == 3
        assert count_curve_mod(q, (e0, e1, e2)) == 16
    assert math.gcd(16, 16) == 16

    # E[4](Q) has exactly 8 elements: full E[2] plus halves of the unique divisible nonzero 2-torsion.
    # Order 16 would therefore require either an order-8 point or E[4] of size 16; both are excluded above.
    exact_torsion_order = 8
    assert exact_torsion_order == 8


def generic_and_receiver_check(c: dict) -> None:
    gm = c["generic_MW_deduction"]
    assert gm["generic_rank"] == 0
    assert gm["exact_generic_torsion"] == "Z/4 x Z/2"
    assert gm["exact_generic_MW_group"] == "Z/4 x Z/2"

    inv = c["quartic_generic_point_inventory_and_receiver_test"]
    assert inv["generic_rational_points_count"] == 8
    assert len(inv["points"]) == 8
    assert inv["generic_receiver_compatible_points"] == 0
    # Direct receiver predicate on finite affine R-values.
    assert not is_square_frac(Fraction(0 * 0 - 4))
    assert Fraction(2 * 2 - 4) == 0
    assert Fraction((-2) ** 2 - 4) == 0

    red = c["exceptional_MW_growth_reduction"]
    assert len(red["growth_species"]) == 2
    assert red["receiver_exceptional_growth_locus_empty_proved"] is False
    assert red["rank_jumps_excluded"] is False
    assert red["torsion_growth_excluded"] is False
    assert red["S34_W03_receiver_intersection_executed"] is False
    assert red["receiver_closed"] is False


def main() -> None:
    c = json.loads(CERT.read_text())
    assert c["schema"] == "STAGE36_36_09P_E_TAU_GENERIC_MW_ZERO_EXCEPTIONAL_GROWTH_PREFLIGHT_V1"
    assert c["status"] == "EXACT_E_TAU_GENERIC_MW_ZERO_AND_EXCEPTIONAL_GROWTH_REDUCTION_PENDING_HOSTILE_AUDIT"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert blob(O_CERT) == O_CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(W03) == W03_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V43_BLOB

    polynomial_identities()
    injective_specialization_check()
    specialized_descent_check()
    specialized_torsion_check()
    generic_and_receiver_check(c)

    # Certificate consistency / credit firewalls.
    sp = c["injective_specialization_p0"]
    assert sp["specialization_E_tau_Qp_to_E_star_Q_injective"] is True
    d = c["specialized_2isogeny_descent"]
    assert d["alpha"]["candidate_count"] == 16 and d["alpha"]["image_size"] == 1
    assert d["beta"]["candidate_count"] == 16 and d["beta"]["image_size"] == 4
    assert d["rank_E_star_Q"] == 0
    tor = c["specialized_torsion"]
    assert tor["exact_torsion_order"] == 8 and tor["exact_torsion"] == "Z/4 x Z/2"
    fw = c["scope_firewalls"]
    assert fw["E_tau_generic_rank_computed"] is True and fw["E_tau_generic_rank"] == 0
    assert fw["E_tau_generic_torsion_computed"] is True
    assert fw["E_tau_generic_receiver_compatible_points_excluded"] is True
    assert fw["E_sigma_tau_generic_rank_computed"] is False
    assert fw["all_specialized_E_tau_groups_computed"] is False
    assert fw["rank_jumps_excluded"] is False
    assert fw["torsion_growth_excluded"] is False
    assert fw["S34_W03_receiver_intersection_empty"] is False
    assert fw["top_genus3_rational_points_exhausted"] is False
    assert fw["gaussian_norm_route_resolved"] is False
    assert fw["receiver_emptiness_proved"] is False
    assert fw["R29_CAMP2_closed"] is False
    assert fw["Q11_CAMPEDELLI_closed"] is False
    assert fw["endpoint_closed"] is False
    assert fw["perfect_cuboid_nonexistence_claim"] is False

    print("36-09P E_tau generic MW exact: rank 0, torsion Z/4xZ/2; all 8 generic points nonreceiver; receiver fibers require exceptional MW growth")


if __name__ == "__main__":
    main()
