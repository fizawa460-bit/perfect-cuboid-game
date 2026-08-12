from __future__ import annotations

from fractions import Fraction


def descent_coordinates(k: int, kappa: int, Z: int, T: int, f: int, g: int) -> dict[str, Fraction | int]:
    s = k * kappa
    lam = 1 if s % 2 else 2
    d = 2 * s if s % 2 else s // 2
    U = Fraction(k * Z, lam * T)
    Vm = Fraction(f - g, lam * T)
    Vp = Fraction(f + g, lam * T)
    X = U * U
    if X - d != k * Vm * Vm:
        raise AssertionError("X-d descent identity fails")
    if X + d != k * Vp * Vp:
        raise AssertionError("X+d descent identity fails")
    return {"lambda": lam, "d": d, "U": U, "V_minus": Vm, "V_plus": Vp, "X": X}


def witness() -> dict[str, object]:
    out = descent_coordinates(k=10, kappa=13, Z=37, T=3, f=117, g=1)
    return {
        "lambda": out["lambda"],
        "d": out["d"],
        "U": [out["U"].numerator, out["U"].denominator],
        "V_minus": [out["V_minus"].numerator, out["V_minus"].denominator],
        "V_plus": [out["V_plus"].numerator, out["V_plus"].denominator],
        "X": [out["X"].numerator, out["X"].denominator],
    }


if __name__ == "__main__":
    print(witness())
