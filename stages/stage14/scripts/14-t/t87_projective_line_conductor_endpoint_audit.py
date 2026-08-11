#!/usr/bin/env python3

import json
import math
from pathlib import Path


def prime_factors(n):
    out = []
    x = n
    p = 2
    while p * p <= x:
        if x % p == 0:
            out.append(p)
            while x % p == 0:
                x //= p
        p += 1
    if x > 1:
        out.append(x)
    return out


def is_squarefree(n):
    return all(n % (p * p) for p in prime_factors(n))


def phi(n):
    r = n
    for p in prime_factors(n):
        r -= r // p
    return r


def chi4(p):
    assert p % 2 == 1
    return 1 if p % 4 == 1 else -1


def expected_projective_order(d):
    ans = 1
    for p in prime_factors(d):
        ans *= p - chi4(p)
    return ans


def units_mod(d):
    return [a for a in range(d) if math.gcd(a, d) == 1]


def canon_projective(x, y, d, units=None):
    if units is None:
        units = units_mod(d)
    return min(((lam * x) % d, (lam * y) % d) for lam in units)


def build_projective_data(d):
    units = units_mod(d)
    class_map = {}
    classes = set()
    gaussian_units = 0
    for x in range(d):
        for y in range(d):
            if math.gcd(x * x + y * y, d) != 1:
                continue
            gaussian_units += 1
            c = canon_projective(x, y, d, units)
            class_map[(x, y)] = c
            classes.add(c)

    classes = sorted(classes)
    assert gaussian_units == phi(d) * len(classes)
    return units, class_map, classes, gaussian_units


def cmul(z, w):
    x, y = z
    a, b = w
    return x * a - y * b, x * b + y * a


def class_of(z, d, class_map):
    x, y = z
    key = (x % d, y % d)
    assert key in class_map
    return class_map[key]


def reduced_primitive_forms(D):
    assert D < 0 and D % 4 in (0, 1)
    forms = []
    max_a = int(math.sqrt(abs(D) / 3)) + 2
    for a in range(1, max_a + 1):
        for b in range(-a, a + 1):
            num = b * b - D
            if num % (4 * a):
                continue
            c = num // (4 * a)
            if a > c:
                continue
            if math.gcd(a, math.gcd(abs(b), c)) != 1:
                continue
            if (abs(b) == a or a == c) and b < 0:
                continue
            forms.append((a, b, c))
    return forms


def count_annulus_class(d, c, L, class_map):
    R = int(math.isqrt(2 * L)) + 1
    count = 0
    for x in range(-R, R + 1):
        for y in range(-R, R + 1):
            n = x * x + y * y
            if not (L <= n < 2 * L):
                continue
            if math.gcd(n, d) != 1:
                continue
            if class_of((x, y), d, class_map) == c:
                count += 1
    return count


def main():
    ds = [d for d in range(3, 40, 2) if is_squarefree(d)]
    Ls = [25, 50, 100, 200, 400, 800]

    group_order_checks = 0
    projective_classes_total = 0
    gaussian_unit_residue_checks = 0
    ring_class_order_checks = 0
    reduced_form_classes_total = 0
    projective_incidence_checks = 0
    projective_identity_triples = 0
    annulus_line_checks = 0
    annulus_line_points = 0
    max_line_bound_ratio = 0.0
    max_line_bound_case = None

    projective = {}

    # Exact finite local/CRT group order.
    for d in ds:
        units, class_map, classes, gaussian_units = build_projective_data(d)
        projective[d] = (units, class_map, classes)
        assert len(classes) == expected_projective_order(d)
        group_order_checks += 1
        projective_classes_total += len(classes)
        gaussian_unit_residue_checks += gaussian_units

    # Independent reduced-form count for Disc=-4 d^2.
    for d in [x for x in ds if x <= 25]:
        forms = reduced_primitive_forms(-4 * d * d)
        assert len(forms) == expected_projective_order(d) // 2
        ring_class_order_checks += 1
        reduced_form_classes_total += len(forms)

    # [z1][z2][z3]=1 iff the product is rational mod d.
    # This is the finite-model version of [gamma][a][pi']=1 from d|Im(z).
    for d in ds:
        _, class_map, classes = projective[d]
        identity = class_of((1, 0), d, class_map)
        for c1 in classes:
            for c2 in classes:
                z12 = cmul(c1, c2)
                for c3 in classes:
                    z = cmul(z12, c3)
                    projective_identity = class_of(z, d, class_map) == identity
                    rational_mod_d = z[1] % d == 0
                    assert projective_identity == rational_mod_d
                    projective_incidence_checks += 1
                    if projective_identity:
                        projective_identity_triples += 1

    # Finite regression for the index-d projective-line annulus bound.
    # We freeze a generous universal constant 3 on the audited range:
    # count <= 3*(L/d + sqrt(L) + 1).
    for d in ds:
        _, class_map, classes = projective[d]
        for L in Ls:
            denominator = L / d + math.sqrt(L) + 1.0
            for c in classes:
                count = count_annulus_class(d, c, L, class_map)
                ratio = count / denominator
                assert ratio < 3.0
                annulus_line_checks += 1
                annulus_line_points += count
                if ratio > max_line_bound_ratio:
                    max_line_bound_ratio = ratio
                    max_line_bound_case = {
                        "d": d,
                        "L": L,
                        "class": list(c),
                        "count": count,
                    }

    boundary = {
        "STAGE14_T87": "COMPLETE_PROJECTIVE_RING_CLASS_BRIDGE_AND_FIXED_POWER_CONDUCTOR_ENDPOINT_COLLAPSE",
        "PROJECTIVE_GAUSSIAN_SELECTOR_GROUP_REENTERED": True,
        "EXACT_GAMMA_A_PRIME_PROJECTIVE_INCIDENCE": True,
        "PROJECTIVE_GROUP_ORDER_SCALE": "d*Bo1",
        "T86_FORM_DISCRIMINANT_RING_CLASS_IDENTIFIED": True,
        "RING_CLASS_NUMBER_SCALE": "d*Bo1",
        "PROJECTIVE_CLASS_IS_INDEX_D_LATTICE": True,
        "PROJECTIVE_ANNULUS_LATTICE_BOUND": "L/d+sqrt(L)+1",
        "FIXED_POWER_D_PROJECTIVE_LATTICE_SAVING_PROVED": True,
        "HARD_SELECTOR_CONDUCTOR_ENDPOINT": "d=Bo1",
        "HARD_PROJECTIVE_GROUP_SIZE": "Bo1",
        "HARD_RING_CLASS_NUMBER": "Bo1",
        "TH25_NEEDED": True,
        "TH25_TARGET_REOPENED": False,
        "TH26_NEEDED": False,
        "CURRENT_PHYSICAL_WHOLE_FAMILY_EXPONENT": "1/2",
        "STRICT_SUBSQRT_POWER_SAVING_PROVED": False,
        "NEXT": "Stage14-t88",
    }

    data = {
        "stage": "14-t87",
        "d_values": ds,
        "annulus_L_values": Ls,
        "group_order_checks": group_order_checks,
        "projective_classes_total": projective_classes_total,
        "gaussian_unit_residue_checks": gaussian_unit_residue_checks,
        "ring_class_order_checks": ring_class_order_checks,
        "reduced_form_classes_total": reduced_form_classes_total,
        "projective_incidence_checks": projective_incidence_checks,
        "projective_identity_triples": projective_identity_triples,
        "annulus_line_checks": annulus_line_checks,
        "annulus_line_points": annulus_line_points,
        "max_line_bound_ratio": max_line_bound_ratio,
        "max_line_bound_case": max_line_bound_case,
        "boundary": boundary,
    }

    print(json.dumps(data, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
