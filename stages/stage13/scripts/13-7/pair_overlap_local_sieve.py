#!/usr/bin/env python3
"""Stage13-7jf: local finite-field sieve for a second integral face.

For an oriented raw incidence

    x^2+y^2=P^2,   P^2+z^2=d^2,

a second face containing x and z can be integral only if x^2+z^2 is a
quadratic residue modulo every odd prime.

The theorem-level proof in 7jf uses only the robust local statement

    rho_p = 1/2 + O(p^-1/2)

for the fixed-congruence raw local density.  This follows by a one-variable
Weil bound after normalizing P != 0; the P=0/singular valuation strata have
lower p-adic mass.  Hence rho_p<3/4 for every sufficiently large prime.

For inert primes p=3 mod 4 there is also a stronger exact F_p identity:

  normalized P=1 total       = p^2-1,
  normalized accepted        = (p+1)^2/2,
  primitive affine total     = (p-1)(p^2+1),
  primitive affine accepted  = (p-1)(p^2+2p+5)/2,

so the affine mod-p acceptance ratio is

  (p^2+2p+5)/(2(p^2+1)) < 2/3  for p>=11.

The exact finite-field formula is a diagnostic strengthening.  The global
argument needs only the weaker uniform <3/4 bound from the Weil estimate and
fixed-prime p-adic lifting.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

OUT = Path("stages/stage13/data/13-7/pair_overlap_local_sieve_report.json")


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for q in range(2, math.isqrt(n) + 1):
        if n % q == 0:
            return False
    return True


def chi(a: int, p: int) -> int:
    a %= p
    if a == 0:
        return 0
    return 1 if pow(a, (p - 1) // 2, p) == 1 else -1


def is_qr_or_zero(a: int, p: int) -> bool:
    return chi(a, p) >= 0


def normalized_counts(p: int) -> tuple[int, int, int]:
    """Count the P=1 conic product in O(p^2) accepted-point operations."""
    circle = [
        (x, y)
        for x in range(p)
        for y in range(p)
        if (x * x + y * y - 1) % p == 0
    ]
    hyperbola = [
        (z, d)
        for z in range(p)
        for d in range(p)
        if (d * d - z * z - 1) % p == 0
    ]
    total = len(circle) * len(hyperbola)
    accepted = 0
    char_sum = 0
    for x, _y in circle:
        for z, _d in hyperbola:
            a = (x * x + z * z) % p
            char_sum += chi(a, p)
            accepted += is_qr_or_zero(a, p)
    return total, accepted, char_sum


def affine_from_normalized(p: int, nt: int, na: int) -> tuple[int, int]:
    """Reconstruct primitive affine counts from P!=0 scaling plus P=0.

    For p=3 mod4, P=0 in x^2+y^2=P^2 forces x=y=0.  Then d^2=z^2;
    after deleting the primitive-forbidden origin there are 2p-2 residues,
    and every one passes x^2+z^2=z^2.
    """
    p_nonzero_total = (p - 1) * nt
    p_nonzero_accepted = (p - 1) * na
    p_zero_primitive = 2 * p - 2
    return (
        p_nonzero_total + p_zero_primitive,
        p_nonzero_accepted + p_zero_primitive,
    )


def build_report() -> dict:
    rows = []
    failures = 0
    for p in range(3, 80):
        if not is_prime(p) or p % 4 != 3:
            continue
        nt, na, cs = normalized_counts(p)
        at, aa = affine_from_normalized(p, nt, na)
        expected_nt = p * p - 1
        expected_na = (p + 1) * (p + 1) // 2
        expected_cs = 2 * (p - 1)
        expected_at = (p - 1) * (p * p + 1)
        expected_aa = (p - 1) * (p * p + 2 * p + 5) // 2
        ok = (
            nt == expected_nt
            and na == expected_na
            and cs == expected_cs
            and at == expected_at
            and aa == expected_aa
        )
        failures += int(not ok)
        rho = aa / at
        rows.append({
            "p": p,
            "circle_points": p + 1,
            "hyperbola_points": p - 1,
            "normalized_total": nt,
            "normalized_accepted": na,
            "normalized_character_sum": cs,
            "primitive_affine_total": at,
            "primitive_affine_accepted": aa,
            "primitive_affine_acceptance": rho,
            "exact_formula_acceptance": (p * p + 2 * p + 5) / (2 * (p * p + 1)),
            "below_two_thirds": rho < 2 / 3,
            "pass": bool(ok),
        })

    return {
        "metadata": {
            "stage": "13-7jf",
            "scope": "finite-field local validator; the global proof uses the fixed-prime Weil/Hensel bound rho_p=1/2+O(p^-1/2)",
        },
        "local_sieve_condition": {
            "raw_equations": "x^2+y^2=P^2, P^2+z^2=d^2",
            "extra_face_test": "x^2+z^2 is a square over Z => quadratic residue or zero modulo every odd p",
            "theorem_level_density": "rho_p=1/2+O(p^-1/2) on the primitive p-adic raw-incidence locus",
            "proof_route": "normalize P!=0, expand the residue indicator, apply the one-variable Weil bound to the resulting fixed-degree quadratic-character sums; P=0/singular valuation strata have lower local mass",
            "consequence": "rho_p<3/4 for all sufficiently large p; this is all the global finite-set squeeze needs",
        },
        "inert_prime_exact_identity": {
            "condition": "p=3 mod 4",
            "normalized_total": "p^2-1",
            "normalized_accepted": "(p+1)^2/2",
            "normalized_character_sum": "2(p-1)",
            "primitive_affine_total": "(p-1)(p^2+1)",
            "primitive_affine_accepted": "(p-1)(p^2+2p+5)/2",
            "primitive_affine_acceptance": "(p^2+2p+5)/(2(p^2+1))",
            "two_thirds_check": "2/3-rho=(p^2-6p-11)/(6(p^2+1)), positive for inert primes p>=11",
        },
        "finite_checks": {
            "inert_primes_below_80": len(rows),
            "failures": failures,
            "rows": rows,
        },
        "status": "PASS" if failures == 0 else "FAIL",
    }


def main() -> None:
    report = build_report()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + "\n")
    print(json.dumps({
        "status": report["status"],
        "checked_primes": report["finite_checks"]["inert_primes_below_80"],
        "failures": report["finite_checks"]["failures"],
    }, indent=2))


if __name__ == "__main__":
    main()
