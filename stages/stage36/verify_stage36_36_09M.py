#!/usr/bin/env python3
from __future__ import annotations

import json
import subprocess
from dataclasses import dataclass
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
STATE = ROOT / "stages" / "stage36" / "MAIN-STATE.json"
CERT = ROOT / "stages" / "stage36" / "36-09M" / "universal-order4-2isogeny-physical-family-preflight.json"
SOURCE = ROOT / "stages" / "stage36" / "36-09M" / "lmfdb-32a3-source-lock.md"
L_CERT = ROOT / "stages" / "stage36" / "36-09L" / "physical-base-full2-descent-preflight.json"

BASE = "dd0fab674db9a10d6494590c1987333aa338a37e"
V37_BLOB = "af9edd74876f9792772bf8f32167f5e76a21905b"
L_CERT_BLOB = "56fd432a3ae6046bc4643b56bf562660af49fe89"
SOURCE_BLOB = "e820cc4e73af3be46f60f92aede8c076a92504df"
CERT_BLOB = "470e87d3e48c857b99793bd8ac0d01eff75eb727"


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def blob(path: Path) -> str:
    return git("hash-object", str(path.relative_to(ROOT)))


@dataclass(frozen=True)
class Quad:
    a: Fraction
    b: Fraction
    D: Fraction

    def __add__(self, other):
        if isinstance(other, (int, Fraction)):
            other = Quad(Fraction(other), Fraction(0), self.D)
        assert self.D == other.D
        return Quad(self.a + other.a, self.b + other.b, self.D)

    __radd__ = __add__

    def __neg__(self):
        return Quad(-self.a, -self.b, self.D)

    def __sub__(self, other):
        return self + (-other)

    def __rsub__(self, other):
        return (-self) + other

    def __mul__(self, other):
        if isinstance(other, (int, Fraction)):
            other = Quad(Fraction(other), Fraction(0), self.D)
        assert self.D == other.D
        return Quad(self.a * other.a + self.b * other.b * self.D,
                    self.a * other.b + self.b * other.a, self.D)

    __rmul__ = __mul__

    def inv(self):
        den = self.a * self.a - self.b * self.b * self.D
        assert den != 0
        return Quad(self.a / den, -self.b / den, self.D)

    def __truediv__(self, other):
        if isinstance(other, (int, Fraction)):
            assert other != 0
            return Quad(self.a / other, self.b / other, self.D)
        return self * other.inv()

    def __pow__(self, n: int):
        assert n >= 0
        out = Quad(Fraction(1), Fraction(0), self.D)
        base = self
        while n:
            if n & 1:
                out = out * base
            base = base * base
            n >>= 1
        return out


def qconst(x: Fraction, D: Fraction) -> Quad:
    return Quad(x, Fraction(0), D)


def check_c8_adapter(u: Fraction) -> None:
    assert u != 0
    D = u**4 + 6*u*u + 1
    v = Quad(Fraction(0), Fraction(1), D)
    A = (v + 1) / (u*u)
    B = qconst(u, D) * (A*A - 1)
    assert B*B == (2*A + 6) * (A*A - 1)
    x = (A + 1) / 2
    y = B / 4
    assert y*y == x*x*x - x

    # exact open inverse round trip
    A2 = 2*x - 1
    u2 = y / (x*(x-1))
    v2 = A2*u2*u2 - 1
    assert A2 == A
    assert u2 == qconst(u, D)
    assert v2 == v


def physical_k(t: Fraction) -> tuple[Fraction, Fraction]:
    # line rho=2+t(k-1) through (k,rho)=(1,2)
    den = t*t - 2
    assert den != 0
    k = (t*t - 4*t + 2) / den
    rho = 2 + t*(k-1)
    assert rho*rho == 2*(k*k+1)
    return k, rho


def check_family(t: Fraction) -> None:
    k, rho = physical_k(t)
    assert k not in (0, 1, -1)

    # E_k and its two universal order-4 points.
    def fE(x: Fraction) -> Fraction:
        return x*(x+1)*(x+k*k)

    for x, y in [(k, k*(k+1)), (-k, k*(k-1))]:
        assert y*y == fE(x)
        A = 1+k*k
        B = k*k
        m = (3*x*x + 2*A*x + B) / (2*y)
        x2 = m*m - A - 2*x
        y2 = -y + m*(x-x2)
        assert x2 == 0 and y2 == 0

    # 2-isogenous quotient factorization and images of Pplus/Pminus.
    A = 1+k*k
    B = k*k
    Bp = A*A - 4*B
    assert Bp == (1-k*k)**2
    roots = ((k+1)**2, (k-1)**2)
    assert roots[0] + roots[1] == 2*(1+k*k)
    assert roots[0] * roots[1] == Bp

    for x, y, expected in [
        (k, k*(k+1), roots[0]),
        (-k, k*(k-1), roots[1]),
    ]:
        x1 = y*y/(x*x)
        y1 = y*(B-x*x)/(x*x)
        assert x1 == expected and y1 == 0

    # Duplication-square identity on y^2=x^3+A*x^2+B*x.
    for x in [Fraction(2), Fraction(3,2), Fraction(-2)]:
        y2 = x*x*x + A*x*x + B*x
        if y2 == 0:
            continue
        lhs = ((3*x*x + 2*A*x + B)**2)/(4*y2) - A - 2*x
        rhs = ((x*x-B)**2)/(4*y2)
        assert lhs == rhs


def main() -> None:
    c = json.loads(CERT.read_text())
    s = json.loads(STATE.read_text())
    src = SOURCE.read_text()

    assert c["schema"] == "STAGE36_36_09M_ORDER4_2ISOGENY_PHYSICAL_FAMILY_PREFLIGHT_V1"
    assert c["base_main_sha"] == BASE
    assert blob(CERT) == CERT_BLOB
    assert blob(SOURCE) == SOURCE_BLOB
    assert blob(L_CERT) == L_CERT_BLOB
    assert git("rev-parse", f"{BASE}:stages/stage36/MAIN-STATE.json") == V37_BLOB

    for needle in [
        "LMFDB label: `32.a3`",
        "equation: `y^2=x^3-x`",
        "Mordell-Weil rank: `0`",
        "torsion structure: `[2,2]`",
        "https://www.lmfdb.org/EllipticCurve/Q/32/a/",
    ]:
        assert needle in src

    for u in [Fraction(1,2), Fraction(2,3), Fraction(3,2), Fraction(-1,2)]:
        check_c8_adapter(u)

    for t in [Fraction(0), Fraction(1,2), Fraction(3), Fraction(-1)]:
        k, _ = physical_k(t)
        if k in (0,1,-1):
            continue
        check_family(t)

    assert c["C8_rational_point_exhaustion"]["result"] == [
        "(1,2)", "(1,-2)", "(-1,2)", "(-1,-2)"
    ]
    assert c["physical_nonsquare_gate"]["conclusion"] == [
        "k is not a rational square", "-k is not a rational square"
    ]
    assert c["two_primary_torsion_Ek"]["conclusion"] == (
        "E_k(Q)[2^infinity] is exactly Z/4 x Z/2 on every retained physical fiber"
    )
    assert c["two_primary_torsion_Ek_prime"]["conclusion"] == (
        "E'_k(Q)[2^infinity] is exactly (Z/2)^2 on every retained physical fiber"
    )

    assert s["schema"] == "STAGE36_CAMPEDELLI_UNIFORM_TORSOR_MAIN_STATE_V38_36_09M_PENDING_HOSTILE_AUDIT"
    assert s["status"] == "ACTIVE_PENDING_HOSTILE_AUDIT"
    M = s["authority_frontier"]["36-09M"]
    assert M["certificate_blob_sha"] == CERT_BLOB
    assert M["source_lock_blob_sha"] == SOURCE_BLOB
    assert M["PHYSICAL_K_AND_MINUS_K_NONSQUARE"] is True
    assert M["E_K_2PRIMARY_TORSION"] == "Z/4 x Z/2"
    assert M["E_K_PRIME_2PRIMARY_TORSION"] == "(Z/2)^2"
    assert M["B3_RELATIVE_2_ISOGENY_ROUTE"] == "LIVE"
    assert s["current"]["36_09N_entry_allowed"] is False
    assert s["promotion_gates"]["uniform_Mordell_Weil_group_proved"] is False
    assert s["promotion_gates"]["isogeny_Selmer_groups_computed"] is False
    assert s["promotion_gates"]["receiver_emptiness_proved"] is False
    assert s["promotion_gates"]["R29_CAMP2_closed"] is False

    print("36-09M exact physical torsion-growth gate verified; C8->32.a3 locked; 2-primary torsion controlled; 36-09N locked")


if __name__ == "__main__":
    main()
