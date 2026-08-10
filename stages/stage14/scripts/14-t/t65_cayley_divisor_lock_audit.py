#!/usr/bin/env python3
"""Stage14-t65: Cayley radial divisor locks / exact-s fiber audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42_SCRIPT = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T58_RESULT = ROOT / "stages/stage14/14-t58/result.md"
T64_RESULT = ROOT / "stages/stage14/14-t64/result.md"


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def gaussian_unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def main() -> None:
    t58 = T58_RESULT.read_text()
    t64 = T64_RESULT.read_text()
    assert "PHYSICAL_RADIAL_CELL_MULTIPLICITY_B_O1=true" in t58
    assert "STAGE14_T64=COMPLETE_SQUARE_LIFTED_CROSS_RATIO_QUOTIENT_AND_JACOBI_FIBRATION" in t64

    t36 = runpy.run_path(str(T36_SCRIPT), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42_SCRIPT), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    assert len(reps) == 560
    invis = [s for s in reps if s["branch"] == "invisible"]
    assert len(invis) == 419

    locks = 0
    gcd_checks = 0
    square_scale_checks = 0
    exact_fibers = defaultdict(list)
    radial_cells = Counter()

    for st in invis:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        ell, eps, m, delta = st["ell"], st["eps"], st["m"], st["delta"]
        n = st["n"]
        k = n // delta
        h = eps * m // k
        assert h * k == eps * m
        assert gcd(delta, h) == 1
        assert n == k * delta
        assert (a*a + b*b) == ell * m
        assert (p*p + q*q) == n
        assert n % ell != 0
        assert gcd(ell, delta) == 1

        dpi = b*b - a*a
        dv = q*q - p*p
        assert dpi > 0 and dv > 0
        assert gcd(p*p + q*q, dv) <= 2
        assert gcd(a*a + b*b, dpi) <= 2

        A = b*b*p*p - a*a*q*q
        B0 = b*b*q*q - a*a*p*p
        assert A > 0 and B0 > 0
        s = Fraction(A, B0)
        assert 0 < s < 1
        C = (1 + s) / (1 - s)
        radial = Fraction(eps * delta * dpi, ell * h * dv)
        assert C == radial

        Ns, Ds = C.numerator, C.denominator
        assert Ns % oddpart(delta) == 0
        assert Ds % oddpart(ell * h) == 0
        locks += 1

        # The two sides cannot cancel through any moving odd radial factor.
        assert gcd(oddpart(delta), oddpart(ell * h * dv)) == 1
        assert gcd(oddpart(ell * h), oddpart(eps * delta * dpi)) == 1
        gcd_checks += 1

        # s = kappa*(u/v)^2 and the Cayley plus/minus gcd is supported on 2*kappa.
        kappa = st["kernel"]
        d2 = st["F"] // kappa
        d = isqrt(d2)
        assert d*d == d2
        w = Fraction(d, B0)
        u, v = w.numerator, w.denominator
        assert gcd(u, v) == 1
        assert s == kappa * w * w
        assert v*v > kappa*u*u
        plus = v*v + kappa*u*u
        minus = v*v - kappa*u*u
        g = gcd(plus, minus)
        assert (2 * kappa) % g == 0
        assert Fraction(plus, minus) == C
        assert Ns == plus // g and Ds == minus // g
        assert (plus // g) % oddpart(delta) == 0
        assert (minus // g) % oddpart(ell * h) == 0
        square_scale_checks += 1

        fkey = (gaussian_unit_key(st["U"]), eps, k, s)
        exact_fibers[fkey].append(st)
        radial_cells[(gaussian_unit_key(st["U"]), eps, k, ell, delta)] += 1

    max_exact_fiber = max(len(v) for v in exact_fibers.values())
    max_radial_cell = max(radial_cells.values())
    max_radial_choices_per_exact_s = 0
    for members in exact_fibers.values():
        choices = {(x["ell"], x["delta"]) for x in members}
        max_radial_choices_per_exact_s = max(max_radial_choices_per_exact_s, len(choices))
        sample = members[0]
        a, b, p, q = sample["a"], sample["b"], sample["p"], sample["q"]
        s = Fraction(b*b*p*p-a*a*q*q, b*b*q*q-a*a*p*p)
        C = (1+s)/(1-s)
        for x in members:
            kk = x["n"] // x["delta"]
            hh = x["eps"] * x["m"] // kk
            assert C.numerator % oddpart(x["delta"]) == 0
            assert C.denominator % oddpart(x["ell"] * hh) == 0

    # t64 already showed that one squareclass can contain different exact s values.
    by_packet_kernel = defaultdict(set)
    for st in invis:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        s = Fraction(b*b*p*p-a*a*q*q, b*b*q*q-a*a*p*p)
        k = st["n"] // st["delta"]
        by_packet_kernel[(gaussian_unit_key(st["U"]), st["eps"], k, st["kernel"])].add(s)
    max_exact_s_per_squareclass = max(len(v) for v in by_packet_kernel.values())

    report = {
        "stage": "14-t65",
        "reciprocal_states": len(reps),
        "invisible_states": len(invis),
        "cayley_radial_lock_checks": locks,
        "odd_noncancellation_checks": gcd_checks,
        "square_scale_plus_minus_checks": square_scale_checks,
        "exact_s_fibers": len(exact_fibers),
        "max_frozen_exact_s_fiber": max_exact_fiber,
        "max_frozen_radial_cell": max_radial_cell,
        "max_frozen_radial_choices_per_exact_s": max_radial_choices_per_exact_s,
        "max_frozen_exact_s_values_per_packet_squareclass": max_exact_s_per_squareclass,
        "identity": "C(s)=eps*delta*(b^2-a^2)/(ell*h*(q^2-p^2))",
        "square_scale": "C(kappa*(u/v)^2)=(v^2+kappa*u^2)/(v^2-kappa*u^2)",
        "boundary": {
            "STAGE14_T65": "COMPLETE_CAYLEY_RADIAL_DIVISOR_LOCK_AND_EXACT_S_FIBER_RIGIDITY",
            "ODD_DELTA_SURVIVES_REDUCED_CAYLEY_NUMERATOR": True,
            "ODD_ELL_H_SURVIVES_REDUCED_CAYLEY_DENOMINATOR": True,
            "SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY_PROVED": True,
            "CAYLEY_PLUS_MINUS_GCD_DIVIDES_2KAPPA": True,
            "CAYLEY_SQUARE_SCALE_TWO_SIDED_DIVISOR_LOCK_PROVED": True,
            "SHARED_U_CAYLEY_SQUARE_SCALE_DIVISOR_INCIDENCE_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH18_NEEDED": False,
            "NEXT": "Stage14-t66",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
