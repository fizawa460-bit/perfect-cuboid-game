#!/usr/bin/env python3
"""Exact finite Artin conditions for the two row376 Kummer characters."""

import json
from functools import reduce
from math import isqrt, prod
from operator import or_
from pathlib import Path

from flint import nmod_poly

HERE = Path(__file__).resolve().parent
LIMIT = 5003
OLD_ABC = {3, 5, 7, 11, 13, 19, 31, 41, 43, 47, 53, 59, 67, 71, 79,
           103, 107, 137, 139, 167, 227}
CASES = ("both", "sum", "equal_case", "one_zero_case")


def elliptic_add(P, Q, a2, a4, p):
    if P is None:
        return Q
    if Q is None:
        return P
    x, y = P
    u, v = Q
    if x == u:
        if (y + v) % p == 0:
            return None
        assert y == v
        slope = (3*x*x + 2*a2*x + a4) * pow(2*y, -1, p) % p
    else:
        slope = (v-y) * pow(u-x, -1, p) % p
    xx = (slope*slope - a2 - x - u) % p
    return xx, (slope*(x-xx)-y) % p


def elliptic_multiply(n, point, a2, a4, p):
    result = None
    for bit in bin(n)[2:]:
        result = elliptic_add(result, result, a2, a4, p)
        if bit == "1":
            result = elliptic_add(result, point, a2, a4, p)
    return result


def check_reduction(point, A, C, a2, a4, p):
    if point is None:
        return
    x, y = point
    assert y*y % p == (x*x*x + a2*x*x + a4*x) % p
    if (A*A + C*C) % p == 0:
        assert (x, y) != (A*A % p, 0)


def original_filter(A, B, C, p, roots):
    D = A*C % p
    if D*B % p == 0:
        return "abc"
    a2, a4 = B*B % p, -D*D % p
    inv_B = pow(B, -1, p)
    R = (D*D*inv_B*inv_B % p, -pow(D*inv_B, 3, p) % p)
    check_reduction(R, A, C, a2, a4, p)
    multiple = elliptic_multiply(30, R, a2, a4, p)
    check_reduction(multiple, A, C, a2, a4, p)
    reduced = elliptic_add(multiple, (0, 0), a2, a4, p)
    check_reduction(reduced, A, C, a2, a4, p)
    if reduced is None:
        if p % 4 != 1 or A not in roots or C not in roots:
            return "reject_pole_s243"
        unit = 8*a2*pow(D, -1, p) % p
        if not any(pow(unit*i % p, (p-1)//4, p) == 1 for i in roots[p-1]):
            return "reject_pole_s269"
        return "pole"
    r2 = -reduced[0] % p
    s2 = (a2-r2) % p
    l2 = (A*A+r2) % p
    q2 = (C*C-r2) % p
    if not all(x in roots for x in (r2, s2, l2, q2)):
        return "reject_affine_squares"
    inverse_D = pow(D, -1, p)
    for pq in roots[l2*q2 % p]:
        for rs in roots[r2*s2 % p]:
            t = (pq+rs)*inverse_D % p
            if t and t in roots and all(x % p in roots for x in
                                        (C+A*t, C-A*t, C*t+A, C*t-A)):
                return "affine"
    return "reject_affine_s243"


def possible_slopes(p, coefficients, polynomials, roots, counters):
    square_s = {s for s in range(p) if all(int(f(s)) in roots for f in polynomials)}
    old = []
    new = []
    for u, v in [(1, 0)] + [(j, 1) for j in range(p)]:
        A, B, C = 2*u*v % p, (u*u-v*v) % p, (u*u+v*v) % p
        D = A*C % p
        s = D*pow(B, -2, p) % p if B else None
        if B:
            passes = s in square_s
        else:
            passes = all(co[-1]*pow(D, len(co)-1, p) % p in roots for co in coefficients)
        if not passes:
            continue
        slope = (u, v, A, B, C, s)
        old.append(slope)
        status = original_filter(A, B, C, p, roots)
        counters[status] = counters.get(status, 0)+1
        if not status.startswith("reject"):
            new.append(slope)
    assert any(u == 1 and v == 0 for u, v, *rest in new)
    assert any(u == 0 and v == 1 for u, v, *rest in new)
    return old, new


def quadratic_artin(s, factors, roots):
    # At a vanishing linear factor the square global norm supplies the last bit.
    bits = 0
    branch = None
    for i, factor in enumerate(factors):
        value = int(factor(s))
        if value == 0:
            assert branch is None and factor.degree() == 1
            branch = i
        elif value not in roots:
            bits |= 1 << i
    if bits.bit_count() % 2:
        assert branch is not None
        bits |= 1 << branch
    return bits


def union(values):
    return reduce(or_, values, 0)


def artin_cases(pairs):
    return {
        "both": union(a | b for a, b in pairs),
        "sum": union(a ^ b for a, b in pairs),
        "equal_case": union(a for a, b in pairs if a == b),
        "one_zero_case": union(a | b for a, b in pairs if a == 0 or b == 0),
    }


def rank(rows):
    pivots = {}
    for row in rows:
        while row:
            i = row.bit_length()-1
            if i not in pivots:
                pivots[i] = row
                break
            row ^= pivots[i]
    return len(pivots)


def main():
    source = json.loads((HERE/"curve_factors.json").read_text(encoding="utf-8"))
    assert source["factor_order"] == ["F29(s)", "F29(-s)", "E29(s)", "F31(s)", "F31(-s)", "E31(s)"]
    coefficients = source["ascending_coefficients"]
    assert [len(c)-1 for c in coefficients] == [105, 105, 210, 120, 120, 240]
    counts = dict.fromkeys(CASES, 2)  # Both dyadic places, already split by row376.
    whole_p = dict.fromkeys(CASES, 0)
    forced_abc, forced_a, six_only_abc, skipped = [], [], [], []
    entries = []
    counters = {}
    for p in range(3, LIMIT+1, 2):
        if any(p % d == 0 for d in range(2, isqrt(p)+1)):
            continue
        roots = {}
        for j in range(p):
            roots.setdefault(j*j % p, []).append(j)
        polynomials = [nmod_poly(c, p) for c in coefficients]
        old, new = possible_slopes(p, coefficients, polynomials, roots, counters)
        if all(A*B*C % p == 0 for _, _, A, B, C, _ in old):
            six_only_abc.append(p)
        if all(A*B*C % p == 0 for _, _, A, B, C, _ in new):
            forced_abc.append(p)
        if all(A == 0 for _, _, A, _, _, _ in new):
            forced_a.append(p)
        unit, decomposition = polynomials[0].factor()
        assert unit == 1
        if any(e != 1 for _, e in decomposition):
            skipped.append(p)
            continue
        factors = sorted((g for g, _ in decomposition), key=lambda g: (g.degree(), list(map(int,g))))
        check = nmod_poly([1],p)
        for g in factors:
            check *= g
        assert check == polynomials[0]
        pairs = sorted({(0,0) if B == 0 else
                        (quadratic_artin(s, factors, roots), quadratic_artin(-s % p, factors, roots))
                        for _, _, _, B, _, s in new})
        assert (0,0) in pairs
        assert sorted((b,a) for a,b in pairs) == pairs
        support = artin_cases(pairs)
        for case in CASES:
            counts[case] += len(factors)-support[case].bit_count()
            whole_p[case] += (support[case] == 0)
        entries.append({
            "p":p, "six_squares_slopes":len(old), "retained_slopes":len(new),
            "factors_ascending":[list(map(int,g)) for g in factors],
            "pairs":pairs, "possible_nonsplit_masks":support,
            "pair_span_rank":rank(a | (b << len(factors)) for a,b in pairs),
        })
    assert skipped == [199] and len(entries) == 668
    assert OLD_ABC <= set(forced_abc)
    assert len(forced_abc) == 56 and len(forced_a) == 41
    assert counts == {"both":399, "sum":652, "equal_case":3034, "one_zero_case":2732}
    assert whole_p == {"both":68, "sum":74, "equal_case":502, "one_zero_case":403}
    table = {row["p"]:row for row in entries}
    assert table[17]["pairs"] == [(0,0),(0,17),(17,0)]
    assert table[29]["pairs"] == [(0,0),(3,3)]
    assert table[109]["pairs"] == [(0,0),(27,57),(48,48),(57,27)]
    mod_a = 8*prod(forced_a)
    assert len(str(mod_a)) == 95
    summary = {
        "odd_prime_limit":LIMIT, "artin_rational_primes":len(entries),
        "excluded_from_artin_due_to_nonsquarefree_reduction":skipped,
        "source_reduction_filter_status_counts":counters,
        "forced_rational_primes_ABC":forced_abc,
        "forced_rational_primes_A":forced_a,
        "new_forced_ABC_from_S243_S269_within_same_cutoff":sorted(set(forced_abc)-set(six_only_abc)),
        "A_modulus":str(mod_a),
        "split_prime_ideals_including_2":counts,
        "odd_rational_primes_all_places_split":whole_p,
        "inert_rational_primes_automatically_principal":sum(len(r["factors_ascending"]) == 1 for r in entries),
        "additional_odd_partial_split_ideals_for_both":sum(
            len(r["factors_ascending"])-r["possible_nonsplit_masks"]["both"].bit_count()
            for r in entries if r["possible_nonsplit_masks"]["both"]),
    }
    print(json.dumps({"summary":summary,"prime_tables":entries},separators=(",",":")))


if __name__ == "__main__":
    main()
