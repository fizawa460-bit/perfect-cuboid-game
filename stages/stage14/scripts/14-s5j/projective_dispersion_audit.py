#!/usr/bin/env python3
"""Deterministic consistency audit for Stage14-s5j."""

from collections import defaultdict
from itertools import combinations
from math import gcd, isqrt
import json

PRIME_LIMIT = 43
XMAX = 80
YMAX = 10
LINEAR = ("m", "n", "m-n", "m+n")


def primes_upto(n):
    out = []
    for x in range(3, n + 1, 2):
        ok = True
        for p in range(3, isqrt(x) + 1, 2):
            if x % p == 0:
                ok = False
                break
        if ok:
            out.append(x)
    return out


def primitive_pairs(xmax=XMAX, ymax=YMAX):
    out = []
    for m in range(2, xmax + 1):
        for n in range(1, min(m, ymax + 1)):
            if gcd(m, n) == 1 and (m - n) % 2 == 1:
                out.append((m, n))
    return out


def values(m, n):
    return {
        "m": m,
        "n": n,
        "m-n": m - n,
        "m+n": m + n,
        "m2+n2": m * m + n * n,
    }


def determinant(P, Q):
    m, n = P
    r, s = Q
    return m * s - r * n


def antideterminant(P, Q):
    m, n = P
    r, s = Q
    return m * s + r * n


def odd_squarefree_kernel(x):
    x = abs(x)
    while x and x % 2 == 0:
        x //= 2
    k = 1
    p = 3
    while p * p <= x:
        if x % p == 0:
            k *= p
            while x % p == 0:
                x //= p
        p += 2
    if x > 1:
        k *= x
    return k


def odd_squarefree_divisors(x):
    k = odd_squarefree_kernel(x)
    ps = []
    d = 3
    while d * d <= k:
        if k % d == 0:
            ps.append(d)
            k //= d
        d += 2
    if k > 1:
        ps.append(k)
    ds = [1]
    for p in ps:
        ds += [d * p for d in list(ds)]
    return sorted(set(ds))


def inv(a, p):
    return pow(a % p, p - 2, p)


def norm_roots(p):
    return [r for r in range(p) if (r * r + 1) % p == 0]


def projective_root_count(p, column):
    count = 0
    for m in range(p):
        for n in range(p):
            if m == 0 and n == 0:
                continue
            if column == "m":
                ok = m == 0
            elif column == "n":
                ok = n == 0
            elif column == "m-n":
                ok = (m - n) % p == 0
            elif column == "m+n":
                ok = (m + n) % p == 0
            else:
                ok = (m * m + n * n) % p == 0
            count += ok
    return count


def audit_local_roots():
    rows = []
    for p in primes_upto(PRIME_LIMIT):
        linear_counts = {c: projective_root_count(p, c) for c in LINEAR}
        assert all(v == p - 1 for v in linear_counts.values())
        nr = norm_roots(p)
        norm_count = projective_root_count(p, "m2+n2")
        expected = 2 * (p - 1) if p % 4 == 1 else 0
        assert len(nr) == (2 if p % 4 == 1 else 0)
        assert norm_count == expected
        rows.append({
            "p": p,
            "linear_vector_counts": linear_counts,
            "norm_projective_roots": nr,
            "norm_vector_count": norm_count,
        })
    return rows


def audit_linear_collisions(points):
    checks = 0
    max_ratio_num = 0
    max_ratio_den = 1
    worst = None
    for P, Q in combinations(points, 2):
        D = determinant(P, Q)
        assert D != 0
        vp = values(*P)
        vq = values(*Q)
        for ci, cj in combinations(LINEAR, 2):
            u = odd_squarefree_kernel(gcd(vp[ci], vq[ci]))
            v = odd_squarefree_kernel(gcd(vp[cj], vq[cj]))
            assert gcd(u, v) == 1
            q = u * v
            assert D % q == 0
            assert q <= abs(D)
            checks += 1
            if q * max_ratio_den > abs(D) * max_ratio_num:
                max_ratio_num = q
                max_ratio_den = abs(D)
                worst = (P, Q, ci, cj, q, D)
    return {
        "checks": checks,
        "max_q_over_abs_D": max_ratio_num / max_ratio_den,
        "worst": worst,
    }


def audit_norm_sign_collisions():
    same = 0
    opposite = 0
    for p in primes_upto(PRIME_LIMIT):
        roots = norm_roots(p)
        if not roots:
            continue
        vectors = []
        for m in range(p):
            for n in range(1, p):
                r = (m * inv(n, p)) % p
                if r in roots:
                    vectors.append(((m, n), r))
        for (P, r), (Q, s) in combinations(vectors, 2):
            if r == s:
                assert determinant(P, Q) % p == 0
                same += 1
            else:
                assert (r + s) % p == 0
                assert antideterminant(P, Q) % p == 0
                opposite += 1
    return {"same_sign_checks": same, "opposite_sign_checks": opposite}


def sparse_cell_ledger(points):
    # Use the representative genuine reciprocal edge m -- (m-n).
    cells = defaultdict(int)
    threshold = 2 * XMAX * YMAX
    for P in points:
        vs = values(*P)
        for u in odd_squarefree_divisors(vs["m"]):
            for v in odd_squarefree_divisors(vs["m-n"]):
                if u == 1 or v == 1 or gcd(u, v) != 1:
                    continue
                if u * v > threshold:
                    cells[(u, v)] += 1
    assert all(w <= 1 for w in cells.values())
    second_moment = sum(w * w for w in cells.values())
    diagonal = sum(w for w in cells.values())
    assert second_moment == diagonal
    return {
        "threshold_2XY": threshold,
        "nonempty_sparse_cells": len(cells),
        "max_sparse_cell_occupancy": max(cells.values(), default=0),
        "sparse_raw_second_moment": second_moment,
        "same_point_diagonal": diagonal,
        "offdiagonal": second_moment - diagonal,
    }


def finite_collision_ledger(points):
    threshold = 2 * XMAX * YMAX
    diag_pairs = 0
    offdiag_linear_collisions = 0
    offdiag_above_threshold = 0
    for P in points:
        ds_u = [d for d in odd_squarefree_divisors(values(*P)["m"]) if d > 1]
        ds_v = [d for d in odd_squarefree_divisors(values(*P)["m-n"]) if d > 1]
        diag_pairs += sum(gcd(u, v) == 1 for u in ds_u for v in ds_v)
    for P, Q in combinations(points, 2):
        vp = values(*P)
        vq = values(*Q)
        u = odd_squarefree_kernel(gcd(vp["m"], vq["m"]))
        v = odd_squarefree_kernel(gcd(vp["m-n"], vq["m-n"]))
        if u > 1 and v > 1 and gcd(u, v) == 1:
            offdiag_linear_collisions += 1
            if u * v > threshold:
                offdiag_above_threshold += 1
    assert offdiag_above_threshold == 0
    return {
        "same_point_divisor_pair_load": diag_pairs,
        "distinct_point_common_edge_collisions": offdiag_linear_collisions,
        "distinct_point_collisions_above_2XY": offdiag_above_threshold,
    }


def main():
    points = primitive_pairs()
    report = {
        "metadata": {
            "stage": "14-s5j",
            "classification": "EXACT_STRUCTURE_PLUS_FINITE_CONSISTENCY_AUDIT",
            "prime_limit": PRIME_LIMIT,
            "box": {"X": XMAX, "Y": YMAX},
            "primitive_opposite_parity_points": len(points),
        },
        "local_roots": audit_local_roots(),
        "linear_collision": audit_linear_collisions(points),
        "norm_sign_collision": audit_norm_sign_collisions(),
        "sparse_cell_ledger": sparse_cell_ledger(points),
        "finite_collision_ledger": finite_collision_ledger(points),
        "decision": {
            "STAGE14_S5J": "COMPLETE_PROJECTIVE_COLLISION_REDUCTION_AND_SPARSE_LINEAR_L2_BOUND",
            "LINEAR_FOUR_CRT_CLASS_UNIQUE": True,
            "LINEAR_COLLISION_DIVIDES_DETERMINANT": True,
            "SPARSE_LINEAR_REGIME_THRESHOLD": "q>2XY",
            "SPARSE_LINEAR_L2_DISPERSION": "O_epsilon(N*B^epsilon)",
            "N_SCALE_DIAGONAL_UNAVOIDABLE": True,
            "MEDIUM_RANGE_L2_DISPERSION_PROVED": False,
            "FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED": False,
            "FAMILY_LARGE_SIEVE_THEOREM_PROVED": False,
            "SQRT_B_ASYMPTOTIC_PROVED": False,
            "NEXT": "Stage14-s5k",
        },
    }
    print(json.dumps(report, indent=2))
    print("STAGE14_S5J=COMPLETE_PROJECTIVE_COLLISION_REDUCTION_AND_SPARSE_LINEAR_L2_BOUND")
    print("LINEAR_COLLISION_DIVIDES_DETERMINANT=true")
    print("SPARSE_LINEAR_L2_DISPERSION=O_epsilon(N*B^epsilon)")
    print("MEDIUM_RANGE_L2_DISPERSION_PROVED=false")
    print("FULL_STATE_SPLIT_E_SPARSE_REGIME_CLOSED=false")
    print("FAMILY_LARGE_SIEVE_THEOREM_PROVED=false")
    print("SQRT_B_ASYMPTOTIC_PROVED=false")
    print("NEXT=Stage14-s5k")


if __name__ == "__main__":
    main()
