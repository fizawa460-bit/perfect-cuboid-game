#!/usr/bin/env python3
"""Stage14-t18 local-image and packet-Fourier audit (standard library only)."""

import itertools
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
OUT = ROOT / "stages/stage14/data/14-t18/local_image_fourier_audit.json"


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


def A(t, x):
    return (x - 1) ** 2 - 4 * t * t * x


def B(t, x):
    return x * x + (4 * t**4 - 2) * x + 1


def least_nonsquare(p):
    for a in range(2, p):
        if pow(a, (p - 1) // 2, p) == p - 1:
            return a
    raise AssertionError("odd prime must have a nonsquare unit")


def squareclass_representatives(p):
    if p == 2:
        return [1, 3, 5, 7, 2, 6, 10, 14]
    u = least_nonsquare(p)
    return [1, u, p, p * u]


def local_class_witness_exponent(t, p, representative):
    """Find x in the chosen squareclass, p-adically close enough to 0."""
    for k in range(30):
        x = Fraction(representative * p ** (2 * k), 1)
        if local_square(A(t, x), p) and local_square(B(t, x), p):
            return k
    raise AssertionError("failed to enter the square neighborhood of x=0")


def prime_factors(n):
    n = abs(n)
    out = set()
    p = 2
    while p * p <= n:
        if n % p == 0:
            out.add(p)
            while n % p == 0:
                n //= p
        p = 3 if p == 2 else p + 2
    if n > 1:
        out.add(n)
    return out


def support_fraction(q):
    return prime_factors(q.numerator) | prime_factors(q.denominator)


def dot(a, b):
    return sum(x * y for x, y in zip(a, b)) % 2


def main():
    # The eight branch points give the tame quadratic branch-character space
    # {e in F_2^8 : sum(e_i)=0}, of dimension seven.  The Stage14 cover
    # r^2=x has odd valuation at every branch point, hence monodromy 11111111.
    branch_count = 8
    branch_character_dimension = branch_count - 1
    monodromy = [1] * branch_count
    assert sum(monodromy) % 2 == 0
    assert branch_character_dimension == 7

    # Physical samples F=(S,X,H), t=X/S.
    triples = [(4, 3, 5), (12, 5, 13), (24, 7, 25), (21, 20, 29)]
    local_places = [2, 3, 5, 7, 11]
    local_sample_table = {}
    moving_support_table = {}

    for S, X, H in triples:
        t = Fraction(X, S)
        assert S * S + X * X == H * H
        assert t > 0 and t != 1

        by_place = {}
        for p in local_places:
            reps = squareclass_representatives(p)
            exponents = [local_class_witness_exponent(t, p, d) for d in reps]
            by_place[str(p)] = {
                "squareclass_count": len(reps),
                "max_witness_k": max(exponents),
            }

        # The real squareclass group has two signs.  Both occur for sufficiently
        # small x because A_t(0)=B_t(0)=1.
        real_ks = []
        for sign in (1, -1):
            for k in range(1, 12):
                x = Fraction(sign, 10**k)
                if A(t, x) > 0 and B(t, x) > 0:
                    real_ks.append(k)
                    break
            else:
                raise AssertionError("failed real local witness")
        by_place["infinity"] = {
            "squareclass_count": 2,
            "max_decimal_witness_k": max(real_ks),
        }
        local_sample_table[f"{X}/{S}"] = by_place

        # Canonical moving base support: this is exactly the prime support of
        # t(t^2-1)(t^2+1), rewritten in primitive Pythagorean data.
        rational_bad_support = support_fraction(t * (t * t - 1) * (t * t + 1))
        pythagorean_support = prime_factors(S * X * H * (S - X) * (S + X))
        assert rational_bad_support == pythagorean_support
        moving_support_table[f"{X}/{S}"] = sorted(rational_bad_support)

    # Finite Fourier packet audit.  Signatures live in F_2^r.  The zero
    # signature is the local-square survivor class for the selected characters.
    r = 4
    counts = [10, 1, 4, 2, 3, 0, 5, 1, 2, 4, 1, 3, 0, 2, 1, 4]
    assert len(counts) == 2**r
    M = sum(counts)
    Q = sum(n * n for n in counts)

    fourier = {}
    for e in itertools.product((0, 1), repeat=r):
        total = 0
        for index, multiplicity in enumerate(counts):
            signature = tuple((index >> j) & 1 for j in range(r))
            total += multiplicity * (-1 if dot(e, signature) else 1)
        fourier[e] = total

    trivial = (0,) * r
    assert fourier[trivial] == M
    energy_nontrivial = sum(value * value for e, value in fourier.items() if e != trivial)
    assert energy_nontrivial == (2**r) * Q - M * M

    # Exact projector for the zero signature.
    n_zero = counts[0]
    assert sum(fourier.values()) == (2**r) * n_zero

    # Cauchy-Schwarz packet inequality, checked without floating point:
    # n_0 <= M/2^r + sqrt((1-2^-r)(Q-M^2/2^r)).
    mean = Fraction(M, 2**r)
    collision_excess = Fraction(Q, 1) - Fraction(M * M, 2**r)
    correction_squared = Fraction(2**r - 1, 2**r) * collision_excess
    excess_zero = max(Fraction(0), Fraction(n_zero, 1) - mean)
    assert excess_zero * excess_zero <= correction_squared

    report = {
        "stage": "14-t18",
        "branch_character": {
            "branch_count": branch_count,
            "quadratic_branch_character_space_dimension": branch_character_dimension,
            "stage14_x_cover_monodromy_vector": monodromy,
            "selected_cover_ramifies_at_every_branch_point": True,
            "full_semiabelian_2_descent_image_computed": False,
            "selected_stage14_branch_character_computed": True,
        },
        "selected_local_image": {
            "statement": "for every place v and physical t, delta_{t,v}: C0,t(Q_v) -> Q_v^*/Q_v^{*2} is surjective",
            "reason": "A_t(0)=B_t(0)=1; every local squareclass has representatives arbitrarily close to x=0, where both A_t(x) and B_t(x) are squares",
            "local_support_reduction_available": False,
            "sample_verification": local_sample_table,
        },
        "moving_place_packet": {
            "base_support_formula": "{infinity,2} union Supp(S*X*H*(S-X)*(S+X)) for t=X/S, plus point numerator/denominator support as needed",
            "bad_parameter_identity": "Supp(t(t^2-1)(t^2+1)) = Supp(S*X*H*(S-X)*(S+X))",
            "sample_base_support": moving_support_table,
            "fixed_universal_prime_thinning_claimed": False,
        },
        "packet_fourier": {
            "rank": r,
            "synthetic_signature_counts": counts,
            "M": M,
            "Q_collision": Q,
            "nontrivial_fourier_energy": energy_nontrivial,
            "parseval_identity": "E_nontrivial = 2^r Q - M^2",
            "zero_signature_count": n_zero,
            "collision_excess": str(collision_excess),
            "upper_bound": "N_square <= M/2^r + sqrt((1-2^-r)*(Q-M^2/2^r))",
            "physical_height_window_retained": True,
        },
        "decision": {
            "STAGE14_T18": "COMPLETE_SELECTED_BRANCH_LOCAL_IMAGE_AND_PACKET_FOURIER_BOUND",
            "BRANCH_CHARACTER_SPACE_DIMENSION": branch_character_dimension,
            "STAGE14_X_BRANCH_MONODROMY_ALL_ONES": True,
            "SELECTED_LOCAL_X_SQUARECLASS_IMAGE_FULL_AT_EVERY_PLACE": True,
            "LOCAL_OBSTRUCTION_SAVING_AVAILABLE": False,
            "MOVING_ARITHMETIC_PLACE_PACKET_DEFINED": True,
            "PACKET_FOURIER_PROJECTOR_EXACT": True,
            "PACKET_PARSEVAL_COLLISION_IDENTITY": True,
            "PACKET_SECOND_MOMENT_UPPER_BOUND": True,
            "GLOBAL_CHARACTER_CANCELLATION_PROVED": False,
            "T_O_SQRT_B_PROVED": False,
            "PERFECT_CUBOID_NONEXISTENCE_PROVED": False,
            "NEXT": "Stage14-t19 instantiate moving packets on the exact physical point ledger and attack squareclass-signature collision excess / family second moment",
        },
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report["decision"], indent=2))


if __name__ == "__main__":
    main()
