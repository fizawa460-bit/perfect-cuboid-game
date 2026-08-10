#!/usr/bin/env python3
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[4]
RESULT = ROOT / "stages/stage14/14-4cc/result.md"
SUMMARY = ROOT / "stages/stage14/data/14-4/xi_saturation_k_shell_summary.json"
S714 = ROOT / "stages/stage14/14-s7-14/result.md"
T50 = ROOT / "stages/stage14/14-t50/result.md"


def sqf(n: int) -> int:
    out = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e ^= 1
        if e:
            out *= p
        p += 1 if p == 2 else 2
    if n > 1:
        out *= n
    return out


def oddpart(n: int) -> int:
    while n % 2 == 0:
        n //= 2
    return n


def tau(n: int) -> int:
    ans = 1
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            ans *= e + 1
        p += 1 if p == 2 else 2
    if n > 1:
        ans *= 2
    return ans


def main() -> None:
    text = RESULT.read_text()
    summary = json.loads(SUMMARY.read_text())
    s714 = S714.read_text()
    t50 = T50.read_text()

    required = [
        "STAGE14_4CC=CRITICAL_XI_AMBIENT_SATURATION_AND_TRANSVERSE_K_SHELL_LOCALIZATION",
        "AMBIENT_XI_SATURATION_PROVED=true",
        "PHYSICAL_XI_SATURATION_PROVED=false",
        "FOUR_CELL_GEOMETRY_ALONE_IMPLIES_XI_POWER_SPARSITY=false",
        "K_SHELL_COORDINATE_SUPPORT_EXPONENT=(1+kappa)/2",
        "SEVEN_EIGHT_CRITICAL_K_LOWER_EXPONENT=3/4",
        "OFF_DIAGONAL_XI_K_COLLISION_POWER_SAVING_PROVED=false",
        "TH14_NEEDED=true",
        "NEXT=Stage14-4cd",
    ]
    for token in required:
        assert token in text, token

    assert "XI_ONLY_MINIMAX_BARRIER=7/8" in s714
    assert "TRANSVERSE_LABEL_K=ker(Q^2-P^2)" in s714
    assert "TH14_NEEDED=true" in t50
    assert "SELECTOR_SENSITIVE_TWO_MODULUS_SECOND_MOMENT_PROVED=false" in t50

    # Critical four-cell saturation exponent bookkeeping.
    r = Fraction(1, 4)
    j = Fraction(1, 4)
    s = Fraction(1, 8)
    t = Fraction(1, 8)
    xi = r + j + s + t
    assert xi == Fraction(3, 4)
    assert r + s == Fraction(3, 8)  # a
    assert t + j == Fraction(3, 8)  # b
    assert r + t == Fraction(3, 8)  # c
    assert s + j == Fraction(3, 8)  # d

    # Canonical squarepart scale T=B^(1/16): a*x^2 and b*y^2 hit B^(1/2).
    x = Fraction(1, 16)
    assert Fraction(3, 8) + 2 * x == Fraction(1, 2)

    # k-shell support crossing and quantitative low-k gain.
    kappa = Fraction(3, 4)
    support = (1 + kappa) / 2
    assert support == Fraction(7, 8)
    delta = Fraction(1, 20)
    sub = (1 + (kappa - delta)) / 2
    assert sub == Fraction(7, 8) - delta / 2

    # Residual twist band from xi~B^(3/4), k in [B^(3/4),B].
    assert Fraction(3, 4) + Fraction(3, 4) == Fraction(3, 2)
    assert Fraction(3, 4) + 1 == Fraction(7, 4)

    # Exhaustive primitive-coordinate checks for the exact transverse labels.
    checks = 0
    odd_split_checks = 0
    by_d = {}
    for q in range(2, 81):
        for p in range(1, q):
            if gcd(p, q) != 1:
                continue
            d = q * q - p * p
            k = sqf(d)
            h2 = d // k
            h = isqrt(h2)
            assert h * h == h2

            xi0 = sqf(p * q)
            assert gcd(xi0, k) == 1

            dm = q - p
            dp = q + p
            om = oddpart(dm)
            op = oddpart(dp)
            assert gcd(om, op) == 1
            assert sqf(om) * sqf(op) == oddpart(k)
            odd_split_checks += 1

            by_d.setdefault(d, 0)
            by_d[d] += 1
            checks += 1

    # Number of positive (P,Q) representations is bounded by divisor pairs of D.
    for d, count in by_d.items():
        assert count <= tau(d)

    assert summary["current_physical_upper_bound_exponent"] == "7/8"
    assert summary["critical_xi_exponent"] == "3/4"
    assert summary["ambient_critical_xi_saturation"] == "B^(3/4-o(1))"
    assert summary["ambient_xi_saturation_proved"] is True
    assert summary["physical_xi_saturation_proved"] is False
    assert summary["k_shell_coordinate_support_exponent"] == "(1+kappa)/2"
    assert summary["critical_k_lower_exponent"] == "3/4"
    assert summary["critical_residual_twist_lower_exponent"] == "3/2"
    assert summary["critical_residual_twist_upper_exponent"] == "7/4"
    assert summary["th14_needed"] is True
    assert summary["next"] == "Stage14-4cd"

    print("STAGE14_4CC_AUDIT=PASS")
    print(f"PRIMITIVE_COORDINATE_CHECKS={checks}")
    print(f"ODD_K_SPLIT_CHECKS={odd_split_checks}")
    print("AMBIENT_CRITICAL_XI_SATURATION_EXPONENT=3/4")
    print("K_SHELL_CRITICAL_EXPONENT=3/4")
    print("CURRENT_PHYSICAL_UPPER_BOUND_EXPONENT=7/8")
    print("TH14_NEEDED=true")


if __name__ == "__main__":
    main()
