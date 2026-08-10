#!/usr/bin/env python3
"""Stage14-t66: opposite-sign quadratic root-line audit."""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T65 = ROOT / "stages/stage14/14-t65/result.md"


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def factor(n: int) -> dict[int, int]:
    n = abs(n)
    out: dict[int, int] = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def largest_odd_prime_factor(n: int) -> int:
    fs = [p for p in factor(oddpart(n)) if p % 2]
    return max(fs, default=1)


def legendre(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def main() -> None:
    t65 = T65.read_text()
    assert "STAGE14_T65=COMPLETE_CAYLEY_CANONICAL_PRIME_RECOVERY_AND_SQUARE_SCALE_DIVISOR_REDUCTION" in t65
    assert "CANONICAL_ELL_EQUALS_LARGEST_ODD_PRIME_FACTOR=true" in t65

    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [st for st in reps if st["branch"] == "invisible"]
    assert len(reps) == 560
    assert len(invisible) == 419

    gcd_exact_checks = 0
    radial_kappa_coprime_checks = 0
    root_prime_power_checks = 0
    splitting_checks = 0
    ell_tag_checks = 0
    max_crt_root_lines = 1
    root_line_hist = Counter()

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta
        h = eps * m // k
        assert h * k == eps * m
        assert gcd(delta, h) == 1
        assert ell > 2 * eps * m * delta

        A = b * b * p * p - a * a * q * q
        B0 = b * b * q * q - a * a * p * p
        s = Fraction(A, B0)
        kappa = st["kernel"]
        sq = s / kappa
        u = isqrt(sq.numerator)
        v = isqrt(sq.denominator)
        assert u * u == sq.numerator
        assert v * v == sq.denominator
        assert gcd(u, v) == 1
        assert v * v > kappa * u * u

        raw_plus = v * v + kappa * u * u
        raw_minus = v * v - kappa * u * u
        G = gcd(raw_plus, raw_minus)
        d = gcd(kappa, v)
        assert G in (d, 2 * d)
        assert oddpart(G) == oddpart(d)
        eta = G // d
        assert eta in (1, 2)
        kappa0 = kappa // d
        v0 = v // d
        assert raw_plus // G == (d * v0 * v0 + kappa0 * u * u) // eta
        assert raw_minus // G == (d * v0 * v0 - kappa0 * u * u) // eta
        Pplus = raw_plus // G
        Pminus = raw_minus // G
        assert gcd(Pplus, Pminus) == 1
        assert Fraction(Pplus, Pminus) == (1 + s) / (1 - s)
        gcd_exact_checks += 1

        Qplus = oddpart(delta)
        Qminus = ell * oddpart(h)
        assert gcd(Qplus, Qminus) == 1
        assert gcd(Qplus * Qminus, kappa) == 1
        assert gcd(u, Qplus * Qminus) == 1
        assert Pplus % Qplus == 0
        assert Pminus % Qminus == 0
        radial_kappa_coprime_checks += 1

        assert largest_odd_prime_factor(Pminus) == ell
        fminus = factor(oddpart(Pminus))
        assert fminus.get(ell, 0) == 1
        assert 2 * (oddpart(Pminus) // ell) < ell
        ell_tag_checks += 1

        distinct_primes = set()
        for side, modulus in ((+1, Qminus), (-1, Qplus)):
            for r, e in factor(modulus).items():
                if r == 2:
                    continue
                distinct_primes.add(r)
                assert r % 4 == 1
                assert kappa % r != 0
                assert u % r != 0
                pe = r ** e
                z = (v * pow(u, -1, pe)) % pe
                assert (z * z - side * kappa) % pe == 0
                assert legendre(kappa, r) == 1
                if side == -1:
                    assert legendre(-kappa, r) == 1
                splitting_checks += 1
                root_prime_power_checks += 1

        lines = 1 << len(distinct_primes)
        max_crt_root_lines = max(max_crt_root_lines, lines)
        root_line_hist[lines] += 1

    report = {
        "stage": "14-t66",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "gcd_exact_checks": gcd_exact_checks,
        "radial_kappa_coprime_checks": radial_kappa_coprime_checks,
        "root_prime_power_checks": root_prime_power_checks,
        "splitting_checks": splitting_checks,
        "canonical_ell_tag_checks": ell_tag_checks,
        "max_frozen_crt_root_lines": max_crt_root_lines,
        "crt_root_line_histogram": dict(sorted(root_line_hist.items())),
        "root_system": "z^2=-kappa mod odd(delta), z^2=+kappa mod ell*odd(h)",
        "boundary": {
            "STAGE14_T66": "COMPLETE_PRIMEWISE_CAYLEY_ALLOCATION_AND_OPPOSITE_SIGN_ROOT_LINE_REDUCTION",
            "CAYLEY_GCD_ODD_PART_EQUALS_GCD_KAPPA_V": True,
            "ODD_PHYSICAL_RADIAL_MODULUS_COPRIME_TO_KAPPA": True,
            "OPPOSITE_SIGN_QUADRATIC_ROOT_CONGRUENCES_PROVED": True,
            "CRT_ROOT_LINE_MULTIPLICITY": "Bo1",
            "PLUS_AND_MINUS_HAVE_SAME_LEGENDRE_SPLITTING_CONDITION": True,
            "CANONICAL_LARGEST_PRIME_TAG_RETAINED": True,
            "SHARED_U_CANONICAL_PRIME_TAGGED_OPPOSITE_SIGN_QUADRATIC_ROOT_LINE_ENERGY_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH18_NEEDED": True,
            "TH18_REQUESTED_OBJECT": "CanonicalPrimeTaggedOppositeSignQuadraticRootLargeSieve",
            "NEXT": "Stage14-t67",
        },
    }
    print(json.dumps(report, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
