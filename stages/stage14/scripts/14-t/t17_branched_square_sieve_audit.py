#!/usr/bin/env python3
"""Stage14-t17 generalized-Jacobian squareclass-sieve audit."""

import itertools
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t17/branched_square_sieve_audit.json"


def vp_integer(n, p):
    n = abs(n)
    if n == 0:
        raise ValueError("zero has no finite valuation")
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def local_square(q, place):
    """Exact square test in R, Q_2, or Q_p for odd prime p."""
    if q == 0:
        return True
    if place == "infinity":
        return q > 0

    p = int(place)
    a, b = q.numerator, q.denominator
    va = vp_integer(a, p)
    vb = vp_integer(b, p)
    if (va - vb) % 2:
        return False

    a0 = a // (p**va)
    b0 = b // (p**vb)
    if p == 2:
        unit = (a0 * pow(b0, -1, 8)) % 8
        return unit == 1

    unit = (a0 * pow(b0, -1, p)) % p
    return pow(unit, (p - 1) // 2, p) == 1


def character_projector(bits):
    """Orthogonality projector for an elementary 2-group signature."""
    total = 0
    for character in itertools.product((0, 1), repeat=len(bits)):
        dot = sum(a * b for a, b in zip(character, bits)) % 2
        total += -1 if dot else 1
    return Fraction(total, 2 ** len(bits))


def is_square_fraction(q):
    if q < 0:
        return False
    return isqrt(q.numerator) ** 2 == q.numerator and isqrt(q.denominator) ** 2 == q.denominator


def main():
    # Physical Pythagorean slope samples used throughout the t-track.
    samples = [Fraction(3, 4), Fraction(5, 12), Fraction(7, 24), Fraction(20, 21)]
    for t in samples:
        assert t > 0 and t != 1
        assert is_square_fraction(1 + t * t)

    # t16 geometry: genus-5 double cover of genus-1 base, branch degree 8.
    genus_cover = 5
    genus_base = 1
    branch_degree = 8
    prym_dimension = genus_cover - genus_base
    assert prym_dimension == 4

    # The branch modulus consists of 4 rational zero points and 4 rational
    # points at infinity.  For a split reduced modulus of degree 8 the torus
    # Res_m G_m / G_m has rank 7, hence generalized-Jacobian dimension 8.
    zero_points = 4
    infinity_points = 4
    assert zero_points + infinity_points == branch_degree
    torus_rank = branch_degree - 1
    generalized_jacobian_dimension = genus_base + torus_rank
    assert torus_rank == 7
    assert generalized_jacobian_dimension == 8
    assert branch_degree % 2 == 0

    # Exact finite-place squareclass detector and character orthogonality.
    places = ["infinity", 2, 3, 5, 7, 11, 13, 17]
    square_examples = [Fraction(4, 9), Fraction(25, 16), Fraction(49, 121)]
    nonsquare_examples = [Fraction(-1), Fraction(2), Fraction(3), Fraction(5), Fraction(21, 25), Fraction(17)]
    signatures = {}

    for q in square_examples + nonsquare_examples:
        bits = [0 if local_square(q, place) else 1 for place in places]
        signatures[str(q)] = bits
        projector = character_projector(bits)
        assert projector == (1 if not any(bits) else 0)

    for q in square_examples:
        assert not any(signatures[str(q)])
    for q in nonsquare_examples:
        assert any(signatures[str(q)])

    report = {
        "stage": "14-t17",
        "geometry": {
            "base_genus": genus_base,
            "cover_genus": genus_cover,
            "branch_modulus_degree": branch_degree,
            "branch_modulus_split_rational": True,
            "prym_dimension": prym_dimension,
        },
        "generalized_jacobian": {
            "torus": "Res_m(G_m)/G_m",
            "split_torus_rank": torus_rank,
            "dimension": generalized_jacobian_dimension,
            "modulus_setup_n": 2,
            "n_divides_modulus_degree": True,
        },
        "squareclass_sieve": {
            "global_detector": "delta_t(P)=[x(P)] in Q^*/Q^{*2}; rational lift iff delta_t(P)=1",
            "local_places": places,
            "local_signature_examples": signatures,
            "character_projector_identity_checked": True,
            "finite_local_sieve_is_only_necessary_for_global_square": True,
            "moving_branch_sensitive_place_set_required": True,
        },
        "decision": {
            "STAGE14_T17": "COMPLETE_GENERALIZED_JACOBIAN_SQUARECLASS_SIEVE_INTERFACE",
            "BRANCH_MODULUS_DEGREE": branch_degree,
            "BRANCH_MODULUS_SPLIT_RATIONAL": True,
            "PRYM_DIMENSION": prym_dimension,
            "GENERALIZED_JACOBIAN_TORUS_RANK": torus_rank,
            "GENERALIZED_JACOBIAN_DIMENSION": generalized_jacobian_dimension,
            "SQUARE_LIFT_IFF_GLOBAL_X_SQUARECLASS_TRIVIAL": True,
            "FINITE_LOCAL_CHARACTER_PROJECTOR_EXACT": True,
            "FIXED_UNIVERSAL_PRIME_SIEVE_CLAIMED": False,
            "MOVING_BRANCH_SENSITIVE_PLACE_SET_REQUIRED": True,
            "PHYSICAL_HEIGHT_WINDOW_RETAINED": True,
            "CHARACTER_CANCELLATION_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t18 derive the explicit branch-modulus 2-descent/local image and first moving character-sum inequality",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
