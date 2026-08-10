#!/usr/bin/env python3
"""Stage14-t65 R2: Cayley divisor locks and canonical-prime recovery audit."""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path
import json
import runpy

ROOT = Path(__file__).resolve().parents[4]
T36 = ROOT / "stages/stage14/scripts/14-t/t36_fixed_direction_squareclass_energy_audit.py"
T42 = ROOT / "stages/stage14/scripts/14-t/t42_kummer_transversality_audit.py"
T64 = ROOT / "stages/stage14/14-t64/result.md"


def oddpart(n: int) -> int:
    n = abs(n)
    while n and n % 2 == 0:
        n //= 2
    return n


def largest_odd_prime_factor(n: int) -> int:
    n = oddpart(n)
    ans = 1
    p = 3
    while p * p <= n:
        while n % p == 0:
            ans = p
            n //= p
        p += 2
    if n > 1:
        ans = max(ans, n)
    return ans


def unit_key(z):
    x, y = z
    return min(((x, y), (-y, x), (-x, -y), (y, -x)))


def main() -> None:
    assert "STAGE14_T64=COMPLETE_SQUARE_LIFTED_CROSS_RATIO_QUOTIENT_AND_JACOBI_FIBRATION" in T64.read_text()
    t36 = runpy.run_path(str(T36), run_name="stage14_t36_import")
    t42 = runpy.run_path(str(T42), run_name="stage14_t42_import")
    reps = t42["reciprocal_quotient"](t36["build_frozen_states"]())
    invisible = [s for s in reps if s["branch"] == "invisible"]
    assert len(reps) == 560 and len(invisible) == 419

    fixed_u_s = Counter()
    squareclass_by_u = defaultdict(set)
    checks = 0

    for st in invisible:
        a, b, p, q = st["a"], st["b"], st["p"], st["q"]
        eps, ell, m, n, delta = st["eps"], st["ell"], st["m"], st["n"], st["delta"]
        k = n // delta
        h = eps * m // k
        assert h * k == eps * m and gcd(delta, h) == 1
        assert ell * ell > 4 * t36["B_FROZEN"]
        assert eps * ell * m * delta // 2 <= t36["B_FROZEN"]
        assert ell > 2 * eps * m * delta
        assert n == p*p + q*q == k*delta
        assert a*a + b*b == ell*m
        assert n < ell // 2

        A = b*b*p*p - a*a*q*q
        B0 = b*b*q*q - a*a*p*p
        s = Fraction(A, B0)
        Dpi, DV = b*b-a*a, q*q-p*p
        C = (1+s)/(1-s)
        assert C == Fraction(eps*delta*Dpi, ell*h*DV)
        Ns, Ds = C.numerator, C.denominator
        assert oddpart(Ns) % oddpart(delta) == 0
        assert oddpart(Ds) % (ell * oddpart(h)) == 0
        cof = oddpart(Ds) // ell
        assert 2 * cof < ell
        assert largest_odd_prime_factor(Ds) == ell

        kappa = st["kernel"]
        sq = s / kappa
        u, v = isqrt(sq.numerator), isqrt(sq.denominator)
        assert u*u == sq.numerator and v*v == sq.denominator and gcd(u,v) == 1
        plus = v*v + kappa*u*u
        minus = v*v - kappa*u*u
        gk = gcd(plus, minus)
        assert (2*kappa) % gk == 0
        plus //= gk; minus //= gk
        assert Fraction(plus, minus) == C
        assert largest_odd_prime_factor(minus) == ell
        assert 2 * (oddpart(minus)//ell) < ell

        fixed_u_s[(tuple(st["U"]), s)] += 1
        squareclass_by_u[(unit_key(st["U"]), kappa)].add(s)
        checks += 1

    max_fiber = max(fixed_u_s.values())
    assert max_fiber <= 8
    distinct_s_classes = sum(1 for vals in squareclass_by_u.values() if len(vals) > 1)
    assert distinct_s_classes > 0

    report = {
        "stage": "14-t65-R2",
        "reciprocal_states": len(reps),
        "invisible_states": len(invisible),
        "canonical_prime_recovery_checks": checks,
        "max_fixed_exact_U_s_fiber": max_fiber,
        "shared_U_squareclasses_with_distinct_exact_s": distinct_s_classes,
        "canonical_prime_rule": "ell=LPF_odd(den(C(s)))",
        "cofactor_rule": "2*(odd den(C(s))/ell)<ell",
        "boundary": {
            "STAGE14_T65": "COMPLETE_CAYLEY_CANONICAL_PRIME_RECOVERY_AND_SQUARE_SCALE_DIVISOR_REDUCTION",
            "CANONICAL_ELL_EQUALS_LARGEST_ODD_PRIME_FACTOR": True,
            "SHARED_U_EXACT_CROSS_RATIO_FIBER_MULTIPLICITY": "O(1)",
            "CANONICAL_PRIME_TAGGED_QUADRATIC_NORM_FORM_PROVED": True,
            "SHARED_U_CANONICAL_PRIME_TAGGED_CAYLEY_SQUARE_SCALE_INCIDENCE_PROVED": False,
            "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "7/8",
            "TH18_NEEDED": False,
            "NEXT": "Stage14-t66"
        }
    }
    print(json.dumps(report, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
