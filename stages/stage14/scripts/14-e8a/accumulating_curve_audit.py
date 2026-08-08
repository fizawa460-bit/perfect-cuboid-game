#!/usr/bin/env python3
from __future__ import annotations

import itertools
import json
import math
from collections import defaultdict
from fractions import Fraction
from pathlib import Path

E7 = Path('stages/stage14/data/14-e7/secondary_crossover_audit.json')
OUT = Path('stages/stage14/data/14-e8a/accumulating_curve_audit.json')
SCAN_BOUND = 8


def is_square(n: int) -> bool:
    r = math.isqrt(n)
    return r * r == n


def cube_root(n: int) -> int | None:
    r = round(n ** (1 / 3))
    for z in range(max(0, r - 2), r + 3):
        if z ** 3 == n:
            return z
    return None


def pythagorean_neighbors(hyp_limit: int):
    nbr = defaultdict(set)
    m = 2
    while m * m + 1 <= hyp_limit:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            a, b, h = m * m - n * n, 2 * m * n, m * m + n * n
            if h > hyp_limit:
                continue
            for k in range(1, hyp_limit // h + 1):
                A, C = k * a, k * b
                nbr[A].add(C)
                nbr[C].add(A)
        m += 1
    return nbr


def enumerate_primitive_euler_bricks(B: int) -> dict[tuple[int, int, int], int]:
    nbr = pythagorean_neighbors(B)
    B2 = B * B
    bricks: dict[tuple[int, int, int], int] = {}
    for e, others in nbr.items():
        vals = sorted(others)
        for i, x in enumerate(vals):
            ex = e * e + x * x
            if ex >= B2:
                continue
            y_max = math.isqrt(B2 - ex)
            for y in vals[i + 1:]:
                if y > y_max:
                    break
                if math.gcd(math.gcd(e, x), y) != 1:
                    continue
                if is_square(x * x + y * y):
                    br = tuple(sorted((e, x, y)))
                    bricks[br] = sum(z * z for z in br)
    return bricks


def primitive_pythagorean_triples(max_hyp: int):
    out = []
    m = 2
    while m * m + 1 <= max_hyp:
        for n in range(1, m):
            if math.gcd(m, n) != 1 or (m - n) % 2 == 0:
                continue
            u, v, w = m * m - n * n, 2 * m * n, m * m + n * n
            if w <= max_hyp:
                out.append((u, v, w))
        m += 1
    return out


def saunderson(u: int, v: int, w: int):
    A = abs(u * (3 * v * v - u * u))
    B = abs(v * (3 * u * u - v * v))
    C = abs(4 * u * v * w)
    g = math.gcd(math.gcd(A, B), C)
    return tuple(sorted((A // g, B // g, C // g))), g


def derived_saunderson(u: int, v: int, w: int):
    P = 3 * v * v - u * u
    Q = 3 * u * u - v * v
    A = abs(P * Q)
    B = abs(4 * u * w * P)
    C = abs(4 * v * w * Q)
    g = math.gcd(math.gcd(A, B), C)
    return tuple(sorted((A // g, B // g, C // g))), g


def h_coeffs(a: int, b: int, c: int, d: int) -> list[int]:
    # For s=(a*r+b)/(c*r+d), clear the fourth-power denominator in
    # G=r^2(1-s^2)^2+s^2(1-r^2)^2.  These are the coefficients r^0..r^6.
    return [
        b * b * d * d,
        2 * b * d * (a * d + b * c),
        a * a * d * d + 4 * a * b * c * d + b ** 4 + b * b * c * c - 4 * b * b * d * d + d ** 4,
        2 * (a * a * c * d + 2 * a * b ** 3 + a * b * c * c - 4 * a * b * d * d - 4 * b * b * c * d + 2 * c * d ** 3),
        6 * a * a * b * b + a * a * c * c - 4 * a * a * d * d - 16 * a * b * c * d - 4 * b * b * c * c + b * b * d * d + 6 * c * c * d * d,
        2 * (2 * a ** 3 * b - 4 * a * a * c * d - 4 * a * b * c * c + a * b * d * d + b * b * c * d + 2 * c ** 3 * d),
        a ** 4 - 4 * a * a * c * c + a * a * d * d + 4 * a * b * c * d + b * b * c * c + c ** 4,
    ]


def sqrt_fraction(x: Fraction) -> Fraction | None:
    if x < 0:
        return None
    rn = math.isqrt(x.numerator)
    rd = math.isqrt(x.denominator)
    if rn * rn == x.numerator and rd * rd == x.denominator:
        return Fraction(rn, rd)
    return None


def polynomial_is_square(coeff: list[int]) -> bool:
    f = [Fraction(x) for x in coeff]
    while f and f[-1] == 0:
        f.pop()
    if not f:
        return True
    k = 0
    while f[k] == 0:
        k += 1
    if k % 2:
        return False
    f = f[k:]
    q0 = sqrt_fraction(f[0])
    if q0 is None:
        return False
    q = [q0]
    m = (len(f) - 1) // 2
    for n in range(1, m + 1):
        known = Fraction(0)
        for i in range(1, n):
            if i < len(q) and n - i < len(q):
                known += q[i] * q[n - i]
        q.append((f[n] - known) / (2 * q0))
    conv = [Fraction(0)] * (2 * len(q) - 1)
    for i, x in enumerate(q):
        for j, y in enumerate(q):
            conv[i + j] += x * y
    return conv == f


def mobius_split_scan(bound: int):
    seen = set()
    hits = []
    for vals in itertools.product(range(-bound, bound + 1), repeat=4):
        a, b, c, d = vals
        if vals == (0, 0, 0, 0) or a * d - b * c == 0:
            continue
        g = math.gcd(math.gcd(abs(a), abs(b)), math.gcd(abs(c), abs(d))) or 1
        tup = tuple(z // g for z in vals)
        first = next(z for z in tup if z)
        if first < 0:
            tup = tuple(-z for z in tup)
        if tup in seen:
            continue
        seen.add(tup)
        if polynomial_is_square(h_coeffs(*tup)):
            hits.append(tup)
    return len(seen), hits


def main() -> None:
    e7 = json.loads(E7.read_text())
    cutoffs = [row['B'] for row in e7['dense_exact_census']]
    euler_expected = {row['B']: row['euler_bricks'] for row in e7['dense_exact_census']}
    max_B = max(cutoffs)

    bricks = enumerate_primitive_euler_bricks(max_B)
    assert len(bricks) == euler_expected[max_B] == 219

    max_w = math.ceil(max_B ** (1 / 3)) + 5
    triples = primitive_pythagorean_triples(max_w)
    saund: dict[tuple[int, int, int], int] = {}
    derived: dict[tuple[int, int, int], int] = {}

    for u, v, w in triples:
        S, gs = saunderson(u, v, w)
        D, gd = derived_saunderson(u, v, w)
        assert gs == 1
        assert gd == 1

        hs = sum(z * z for z in S)
        hd = sum(z * z for z in D)
        assert hs == w ** 6 + 16 * u * u * v * v * w * w
        assert hd == 25 * w ** 8 - 96 * u * u * v * v * w ** 4 + 256 * u ** 4 * v ** 4
        assert w ** 6 <= hs <= 5 * w ** 6
        assert 16 * w ** 8 <= hd <= 25 * w ** 8
        saund[S] = hs
        derived[D] = hd

    rows = []
    for B in cutoffs:
        B2 = B * B
        allset = {br for br, h2 in bricks.items() if h2 <= B2}
        S = {br for br, h2 in saund.items() if h2 <= B2}
        D = {br for br, h2 in derived.items() if h2 <= B2}
        assert len(allset) == euler_expected[B]
        assert S <= allset
        assert D <= allset

        cube_face = set()
        for a, b, c in allset:
            diags = [
                math.isqrt(a * a + b * b),
                math.isqrt(a * a + c * c),
                math.isqrt(b * b + c * c),
            ]
            if any(cube_root(z) is not None for z in diags):
                cube_face.add((a, b, c))

        rows.append({
            'B': B,
            'euler_bricks': len(allset),
            'saunderson': len(S),
            'derived_saunderson': len(D),
            'classical_union': len(S | D),
            'classical_fraction': len(S | D) / len(allset),
            'cube_face_bricks': len(cube_face),
            'cube_face_equals_saunderson_finite': cube_face == S,
            'saund_over_B13': len(S) / (B ** (1 / 3)),
            'derived_over_B14': len(D) / (B ** 0.25),
        })

    relations_tested, split_hits = mobius_split_scan(SCAN_BOUND)
    assert split_hits == []

    report = {
        'metadata': {
            'stage': '14-e8a',
            'track': 'accumulating rational curves / square-root source',
            'height': 'physical Euclidean D_R',
            'max_B': max_B,
        },
        'geometry': {
            'surface': 'U^2=E^2+X^2, V^2=E^2+Y^2, Z^2=X^2+Y^2 in P^5',
            'physical_line_obstruction': 'a line meeting E*X*Y!=0 projects linearly to each nonsingular face conic; every such projection must be a point, and the shared E,X,Y coordinates then force the whole projective line to be constant',
            'physical_projective_lines_exist': False,
            'degree_height_rule': 'for a Q-rational curve C with normalization P1 and O(1)|_C of degree d, bounded-height rational points have exponent 2/d',
            'sqrt_curve_required_projective_degree': 4,
        },
        'classical_families': {
            'saunderson': {
                'formula': ['u(3v^2-u^2)', 'v(3u^2-v^2)', '4uvw'],
                'condition': 'u^2+v^2=w^2 primitive',
                'height_identity': 'D_R^2=w^6+16u^2v^2w^2',
                'height_bounds': 'w^3 <= D_R <= sqrt(5) w^3',
                'euclid_parameter_degree': 6,
                'count_order': 'Theta(B^(1/3))',
                'sqrt_source': False,
            },
            'derived_saunderson': {
                'formula': ['(3v^2-u^2)(3u^2-v^2)', '4uw(3v^2-u^2)', '4vw(3u^2-v^2)'],
                'source': 'primitive normalization of (AB,AC,BC) from a Saunderson brick; the raw product gcd is uv',
                'height_identity': 'D_R^2=25w^8-96u^2v^2w^4+256u^4v^4',
                'height_bounds': '4w^4 <= D_R <= 5w^4',
                'euclid_parameter_degree': 8,
                'count_order': 'Theta(B^(1/4))',
                'sqrt_source': False,
            },
        },
        'finite_census': rows,
        'finite_summary': {
            'B': max_B,
            'euler_bricks': rows[-1]['euler_bricks'],
            'saunderson': rows[-1]['saunderson'],
            'derived_saunderson': rows[-1]['derived_saunderson'],
            'classical_union': rows[-1]['classical_union'],
            'classical_fraction': rows[-1]['classical_fraction'],
            'outside_classical_curves': rows[-1]['euler_bricks'] - rows[-1]['classical_union'],
            'cube_face_bricks': rows[-1]['cube_face_bricks'],
            'cube_face_bricks_all_saunderson_at_B_le_1e6': all(row['cube_face_equals_saunderson_finite'] for row in rows),
        },
        'degree4_search': {
            'toric_base_candidate': 'a generic (1,1) base curve has L-degree 4 for L=-K_Y; a Q-split rational lift is therefore the simplest single-curve sqrt(B) candidate',
            'mobius_form': 's=(a r+b)/(c r+d), ad-bc != 0',
            'coefficient_bound': SCAN_BOUND,
            'primitive_mobius_relations_tested': relations_tested,
            'split_square_hits': len(split_hits),
            'finite_scan_is_global_classification': False,
            'exact_symmetric_subfamilies': {
                's=k r': 'the square-condition discriminant is -4 k^2(k^2-1)^2; k=+/-1 leaves a factor 2 and splits only over Q(sqrt(2)), not Q',
                's=k/r': 'the same discriminant obstruction applies; there is no nondegenerate Q-split member',
            },
        },
        'literature_boundary': {
            'saunderson_himane': 'arXiv:2405.13061',
            'spohn_derived': 'Canad. Math. Bull. 17 (1974), 575-577; DOI 10.4153/CMB-1974-102-6',
            'mckinnon_accumulation': 'J. Number Theory 84 (2000), 49-62; arXiv:math/9903013',
            'peschmann_master_tuple': 'arXiv:2604.28072',
            'direct_degree4_euler_brick_curve': 'NO_COLLISION_FOUND_IN_CURRENT_SEARCH',
            'novelty_by_search_absence': False,
        },
        'status': {
            'STAGE14_E8A': 'COMPLETE_CLASSICAL_CURVE_EXCLUSION_AND_DEGREE4_GATE',
            'SAUNDERSON_SQRT_SOURCE': False,
            'DERIVED_SAUNDERSON_SQRT_SOURCE': False,
            'PHYSICAL_PROJECTIVE_LINE_EXCLUDED': True,
            'SQRT_SINGLE_CURVE_REQUIRED_DEGREE': 4,
            'DEGREE4_CURVE_CLASSIFICATION_COMPLETE': False,
            'SMALL_MOBIUS_SPLIT_SCAN_HITS': 0,
            'E9_FILES_TOUCHED': False,
            'NEXT_E8A_ACTION': 'global Neron-Severi/lattice classification of degree-4 rational curves if pursued',
        },
        'pass': True,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(report, indent=2, sort_keys=True) + '\n')
    print(json.dumps(report['status'], indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
