#!/usr/bin/env python3
"""Independent exact Q[x] verification of the eight rational divisors."""
import json
from pathlib import Path

from sympy import Poly, QQ, Rational, symbols

HERE = Path(__file__).resolve().parent
X = symbols("X")
R = 961


def poly(v):
    return Poly.from_list([Rational(c) for c in reversed(v)], X, domain=QQ)


def line(*polys):
    out = []
    for p in polys:
        v = [int(c.p) * pow(int(c.q), -1, R) % R for c in reversed(p.all_coeffs())]
        while v and not v[-1]:
            v.pop()
        out.extend((len(v), *v))
    return " ".join(map(str, out))


def main():
    C = json.loads((HERE / "curve_C29.json").read_text())
    f, a, b = [poly(C[k]) for k in ("F_ascending", "A_star_ascending", "B_star_ascending")]
    assert f.degree() == 105 and f.LC() == 1
    divs = [("H", b, (-a).rem(b)),
            ("D+", poly([-1, 1]), poly([2**35])),
            ("D-", poly([1, 1]), poly([2**35]))]
    for d in json.loads((HERE / "mw_divisors.json").read_text()):
        if d["name"] != "D15b":
            divs.append((d["name"], poly(d["u"]), poly(d["v"])))
    assert len(divs) == 8
    print(line(f))
    for name, u, v in divs:
        assert u.LC() == 1 and v.degree() < u.degree() <= 52
        assert (f-v*v).rem(u).is_zero
        assert u.gcd(u.diff()).degree() == u.gcd(v).degree() == 0
        print(name, line(u, v))


if __name__ == "__main__":
    main()
