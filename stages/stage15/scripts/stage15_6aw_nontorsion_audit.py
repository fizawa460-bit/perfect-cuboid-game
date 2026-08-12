from __future__ import annotations

from fractions import Fraction


def duplication_x(x: Fraction, d: int) -> Fraction:
    return (x * x + d * d) ** 2 / (4 * x * (x * x - d * d))


def division3_polynomial(x: Fraction, d: int) -> Fraction:
    return 3 * x**4 - 6 * d * d * x * x - d**4


def stage15_x_ratio(f: int, g: int) -> Fraction:
    if f <= 0 or g <= 0:
        raise ValueError("positive coordinates required")
    return Fraction(f * f + g * g, 2 * f * g)


def torsion_unit_branch(f: int, g: int, k: int, Z: int, kappa: int, T: int) -> bool:
    return f == g == 1 and k == 2 and Z == 1 and kappa == T == 1


def audit() -> dict[str, object]:
    # The equations obtained by setting x(2P)=+-d reduce to these squares.
    # Their rational roots would require sqrt(2).
    plus_coeffs = [1, -4, 2, 4, 1]   # (u^2-2u-1)^2
    minus_coeffs = [1, 4, 2, -4, 1]  # (u^2+2u-1)^2
    return {
        "half_plus_d_polynomial": plus_coeffs,
        "half_minus_d_polynomial": minus_coeffs,
        "division3_discriminant": 48,
        "unit_ratio": [stage15_x_ratio(1, 1).numerator, stage15_x_ratio(1, 1).denominator],
        "witness_ratio_gt_one": stage15_x_ratio(117, 1) > 1,
        "torsion_unit_branch": torsion_unit_branch(1, 1, 2, 1, 1, 1),
    }


if __name__ == "__main__":
    print(audit())
